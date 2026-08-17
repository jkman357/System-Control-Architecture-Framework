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

    def test_workflow_actions_are_full_sha_pinned_and_read_only(self) -> None:
        workflow = (REPO_ROOT / ".github/workflows/scaf-executable-governance.yml").read_text(encoding="utf-8")
        self.assertIn("permissions:\n  contents: read", workflow)
        self.assertIn("actions/checkout@3d3c42e5aac5ba805825da76410c181273ba90b1", workflow)
        self.assertIn("actions/setup-python@5fda3b95a4ea91299a34e894583c3862153e4b97", workflow)
        self.assertIn("persist-credentials: false", workflow)


if __name__ == "__main__":
    unittest.main()
