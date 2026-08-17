from __future__ import annotations

import base64
import hashlib
import json
import os
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock

from tools.scaf_ci_gate import gate


REPO_ROOT = Path(__file__).resolve().parents[3]


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def make_bundle(repo_root: Path) -> dict:
    paths = sorted(gate.EXPECTED_ARTIFACTS)
    artifacts = [{"path": rel, "sha256": sha256(repo_root / rel)} for rel in paths]
    by_path = {item["path"]: item["sha256"] for item in artifacts}
    return {
        "trust_version": 1,
        "trust_scope": "scaf_executable_governance_ci",
        "hash_algorithm": "sha256",
        "artifacts": artifacts,
        "external_pin": {
            "pin_version": 1,
            "pin_scope": "scaf_frozen_baseline_release_integrity",
            "hash_algorithm": "sha256",
            "artifacts": [
                {
                    "path": rel,
                    "sha256": by_path[rel],
                }
                for rel in sorted(gate.EXPECTED_EXTERNAL_PIN_ARTIFACTS)
            ],
        },
    }


class GateTests(unittest.TestCase):
    def test_accepted_external_bundle_runs_all_three_stages(self) -> None:
        bundle = make_bundle(REPO_ROOT)
        with tempfile.TemporaryDirectory() as td:
            pin = Path(td) / "trust.json"
            pin.write_text(json.dumps(bundle), encoding="utf-8")
            report = gate.execute_gate(pin, REPO_ROOT)
        self.assertTrue(report.passed, report.errors)
        self.assertEqual(
            [stage.name for stage in report.stages],
            [
                "external-pin verification",
                "frozen-baseline release integrity",
                "authority-registry semantic/structural validation",
            ],
        )
        self.assertTrue(all(stage.returncode == 0 for stage in report.stages))

    def test_bundle_must_be_outside_repository(self) -> None:
        bundle = make_bundle(REPO_ROOT)
        local = REPO_ROOT / ".scaf-ci-test-trust.json"
        try:
            local.write_text(json.dumps(bundle), encoding="utf-8")
            report = gate.execute_gate(local, REPO_ROOT)
            self.assertFalse(report.passed)
            self.assertTrue(any("outside" in error for error in report.errors))
        finally:
            local.unlink(missing_ok=True)

    def test_control_artifact_hash_mismatch_fails_before_stages(self) -> None:
        bundle = make_bundle(REPO_ROOT)
        for item in bundle["artifacts"]:
            if item["path"] == "tools/scaf_validator/validator.py":
                item["sha256"] = "0" * 64
        with tempfile.TemporaryDirectory() as td:
            pin = Path(td) / "trust.json"
            pin.write_text(json.dumps(bundle), encoding="utf-8")
            report = gate.execute_gate(pin, REPO_ROOT)
        self.assertFalse(report.passed)
        self.assertEqual(report.stages, ())
        self.assertTrue(any("validator.py" in error and "mismatch" in error for error in report.errors))

    def test_external_pin_hash_must_equal_top_level_trust_pin(self) -> None:
        bundle = make_bundle(REPO_ROOT)
        bundle["external_pin"]["artifacts"][0]["sha256"] = "0" * 64
        with tempfile.TemporaryDirectory() as td:
            pin = Path(td) / "trust.json"
            pin.write_text(json.dumps(bundle), encoding="utf-8")
            report = gate.execute_gate(pin, REPO_ROOT)
        self.assertFalse(report.passed)
        self.assertEqual(report.stages, ())
        self.assertTrue(any("must equal top-level CI trust pin" in error for error in report.errors))

    def test_mutated_pinned_validator_file_fails_in_repository_copy(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            repo_copy = Path(td) / "repo"
            shutil.copytree(REPO_ROOT, repo_copy, symlinks=True)
            bundle = make_bundle(REPO_ROOT)
            (repo_copy / "tools/scaf_validator/validator.py").write_text("# mutation\n", encoding="utf-8")
            trust = Path(td) / "trust.json"
            trust.write_text(json.dumps(bundle), encoding="utf-8")
            report = gate.execute_gate(trust, repo_copy)
        self.assertFalse(report.passed)
        self.assertEqual(report.stages, ())

    def test_cli_rejects_repo_root_and_stage_order_overrides(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            trust = Path(td) / "trust.json"
            trust.write_text(json.dumps(make_bundle(REPO_ROOT)), encoding="utf-8")
            script = REPO_ROOT / "tools/scaf_ci_gate/gate.py"
            for extra in (["--repo-root", str(REPO_ROOT)], ["--stage-order", "validator-first"]):
                result = subprocess.run(
                    [sys.executable, "-I", str(script), "--trust-bundle", str(trust), *extra],
                    cwd=REPO_ROOT,
                    text=True,
                    capture_output=True,
                    check=False,
                )
                self.assertEqual(result.returncode, 2)
                self.assertIn("unrecognized arguments", result.stderr)

    def test_workflow_is_trusted_branch_foundation_not_pr_target(self) -> None:
        workflow = (REPO_ROOT / ".github/workflows/scaf-executable-governance.yml").read_text(encoding="utf-8")
        self.assertIn("workflow_dispatch:", workflow)
        self.assertIn("push:", workflow)
        self.assertNotIn("pull_request:", workflow)
        self.assertNotIn("pull_request_target:", workflow)
        self.assertIn("SCAF_CI_TRUST_BUNDLE_B64", workflow)
        self.assertIn("$RUNNER_TEMP/scaf-ci-trust-bundle.json", workflow)
        self.assertIn("python -I tools/scaf_ci_gate/gate.py", workflow)


    def test_all_pinned_artifact_parent_symlinks_fail_before_stages(self) -> None:
        parent_components = {
            "tools/scaf_ci_gate/gate.py": "tools/scaf_ci_gate",
            "tools/scaf_external_pin/checker.py": "tools/scaf_external_pin",
            "release-integrity/frozen-baseline-manifest.json": "release-integrity",
            "tools/scaf_release_integrity/checker.py": "tools/scaf_release_integrity",
            "tools/scaf_validator/validator.py": "tools/scaf_validator",
            "schemas/authority-registry.schema.json": "schemas",
        }
        bundle = make_bundle(REPO_ROOT)
        for artifact, parent_rel in parent_components.items():
            with self.subTest(artifact=artifact), tempfile.TemporaryDirectory() as td:
                base = Path(td)
                repo_copy = base / "repo"
                shadow = repo_copy / "shadow"
                shutil.copytree(REPO_ROOT, repo_copy, symlinks=True)
                shutil.copytree(REPO_ROOT, shadow, symlinks=True)

                parent = repo_copy / parent_rel
                if parent.is_dir() and not parent.is_symlink():
                    shutil.rmtree(parent)
                else:
                    parent.unlink(missing_ok=True)
                target = Path(os.path.relpath(shadow / parent_rel, parent.parent))
                parent.symlink_to(target, target_is_directory=True)

                trust = base / "trust.json"
                trust.write_text(json.dumps(bundle), encoding="utf-8")
                report = gate.execute_gate(trust, repo_copy)
                self.assertFalse(report.passed)
                self.assertEqual(report.stages, ())
                self.assertTrue(
                    any("path component must not be a symlink" in error for error in report.errors),
                    report.errors,
                )

    def test_production_gate_parent_symlink_shadow_repo_fails(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            base = Path(td)
            repo_copy = base / "repo"
            shadow = repo_copy / "shadow"
            shutil.copytree(REPO_ROOT, repo_copy, symlinks=True)
            shutil.copytree(REPO_ROOT, shadow, symlinks=True)

            gate_dir = repo_copy / "tools/scaf_ci_gate"
            shutil.rmtree(gate_dir)
            gate_dir.symlink_to(Path("../shadow/tools/scaf_ci_gate"), target_is_directory=True)
            normative = repo_copy / "docs/normative/10_SCAF_CTX_System_Context_Obligations.md"
            normative.write_text(normative.read_text(encoding="utf-8") + "\nshadow-pivot-mutation\n", encoding="utf-8")

            trust = base / "trust.json"
            trust.write_text(json.dumps(make_bundle(REPO_ROOT)), encoding="utf-8")
            result = subprocess.run(
                [
                    sys.executable,
                    "-I",
                    str(repo_copy / "tools/scaf_ci_gate/gate.py"),
                    "--trust-bundle",
                    str(trust),
                ],
                cwd=repo_copy,
                text=True,
                capture_output=True,
                check=False,
            )
            self.assertNotEqual(result.returncode, 0)
            self.assertIn("RESULT: FAIL", result.stdout)
            self.assertIn("path component must not be a symlink", result.stdout + result.stderr)
            self.assertNotIn(f"Repository: {shadow.resolve()}", result.stdout)

    def test_production_validator_parent_symlink_shadow_repo_fails(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            base = Path(td)
            repo_copy = base / "repo"
            shadow = repo_copy / "shadow"
            shutil.copytree(REPO_ROOT, repo_copy, symlinks=True)
            shutil.copytree(REPO_ROOT, shadow, symlinks=True)

            validator_dir = repo_copy / "tools/scaf_validator"
            shutil.rmtree(validator_dir)
            validator_dir.symlink_to(Path("../shadow/tools/scaf_validator"), target_is_directory=True)
            registry = repo_copy / "authority-registry.yaml"
            registry.write_text(registry.read_text(encoding="utf-8").replace("SCAF-AK-001", "SCAF-AK-999", 1), encoding="utf-8")

            trust = base / "trust.json"
            trust.write_text(json.dumps(make_bundle(REPO_ROOT)), encoding="utf-8")
            script = repo_copy / "tools/scaf_ci_gate/gate.py"
            result = subprocess.run(
                [sys.executable, "-I", str(script), "--trust-bundle", str(trust)],
                cwd=repo_copy,
                text=True,
                capture_output=True,
                check=False,
            )
            self.assertNotEqual(result.returncode, 0)
            self.assertIn("RESULT: FAIL", result.stdout)
            self.assertIn("tools/scaf_validator", result.stdout + result.stderr)
            self.assertIn("path component must not be a symlink", result.stdout + result.stderr)
            self.assertNotIn("--- external-pin verification ---", result.stdout)

    def test_stage_reported_repository_must_match_verified_root(self) -> None:
        bundle = make_bundle(REPO_ROOT)
        wrong_root = REPO_ROOT / "shadow"
        fake_stage = gate.GateStageResult(
            name="external-pin verification",
            returncode=0,
            stdout=f"SCAF External Release-Integrity Pin Verification\nRepository: {wrong_root}\nRESULT: PASS\n",
            stderr="",
        )
        with tempfile.TemporaryDirectory() as td:
            trust = Path(td) / "trust.json"
            trust.write_text(json.dumps(bundle), encoding="utf-8")
            with mock.patch.object(gate, "_run_stage", return_value=fake_stage):
                report = gate.execute_gate(trust, REPO_ROOT)
        self.assertFalse(report.passed)
        self.assertEqual(len(report.stages), 1)
        self.assertTrue(any("repository-root mismatch" in error for error in report.errors))

    def test_workflow_bootstrap_checks_path_components_before_hash(self) -> None:
        workflow = (REPO_ROOT / ".github/workflows/scaf-executable-governance.yml").read_text(encoding="utf-8")
        self.assertIn("os.lstat", workflow)
        self.assertIn("stat.S_ISLNK", workflow)
        self.assertIn("tools/scaf_ci_gate/gate.py", workflow)
        self.assertLess(workflow.index("os.lstat"), workflow.index("sha256sum tools/scaf_ci_gate/gate.py"))

    def test_workflow_actions_are_full_sha_pinned_and_read_only(self) -> None:
        workflow = (REPO_ROOT / ".github/workflows/scaf-executable-governance.yml").read_text(encoding="utf-8")
        self.assertIn("permissions:\n  contents: read", workflow)
        self.assertIn("actions/checkout@3d3c42e5aac5ba805825da76410c181273ba90b1", workflow)
        self.assertIn("actions/setup-python@5fda3b95a4ea91299a34e894583c3862153e4b97", workflow)
        self.assertIn("persist-credentials: false", workflow)


if __name__ == "__main__":
    unittest.main()
