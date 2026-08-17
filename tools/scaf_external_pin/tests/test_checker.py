from __future__ import annotations

import hashlib
import json
import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from tools.scaf_external_pin.checker import (
    EXPECTED_PIN_SCOPE,
    validate_external_pin_data,
    validate_external_pin_file,
)


REPO_ROOT = Path(__file__).resolve().parents[3]
MANIFEST_REL = "release-integrity/frozen-baseline-manifest.json"
CHECKER_REL = "tools/scaf_release_integrity/checker.py"


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    h.update(path.read_bytes())
    return h.hexdigest()


def accepted_pin() -> dict:
    return {
        "pin_version": 1,
        "pin_scope": EXPECTED_PIN_SCOPE,
        "hash_algorithm": "sha256",
        "artifacts": [
            {"path": MANIFEST_REL, "sha256": sha256_file(REPO_ROOT / MANIFEST_REL)},
            {"path": CHECKER_REL, "sha256": sha256_file(REPO_ROOT / CHECKER_REL)},
        ],
    }


class ExternalPinTests(unittest.TestCase):
    def test_accepted_external_pin_data_passes(self):
        report = validate_external_pin_data(accepted_pin(), REPO_ROOT)
        self.assertTrue(report.passed, "\n".join(report.errors))
        self.assertEqual(report.pinned_artifact_count, 2)
        self.assertEqual(set(report.artifact_summaries), {f"{MANIFEST_REL}: MATCH", f"{CHECKER_REL}: MATCH"})

    def test_manifest_pin_mismatch_fails(self):
        pin = accepted_pin()
        pin["artifacts"][0]["sha256"] = "0" * 64
        report = validate_external_pin_data(pin, REPO_ROOT)
        self.assertFalse(report.passed)
        self.assertTrue(any(MANIFEST_REL in e and "SHA-256 mismatch" in e for e in report.errors))

    def test_checker_pin_mismatch_fails(self):
        pin = accepted_pin()
        pin["artifacts"][1]["sha256"] = "0" * 64
        report = validate_external_pin_data(pin, REPO_ROOT)
        self.assertFalse(report.passed)
        self.assertTrue(any(CHECKER_REL in e and "SHA-256 mismatch" in e for e in report.errors))

    def test_extra_or_duplicate_artifact_fails(self):
        pin = accepted_pin()
        pin["artifacts"].append(dict(pin["artifacts"][0]))
        report = validate_external_pin_data(pin, REPO_ROOT)
        self.assertFalse(report.passed)
        self.assertTrue(any("artifacts count" in e or "duplicate pinned artifact" in e for e in report.errors))

    def test_external_pin_file_must_be_outside_repository(self):
        report = validate_external_pin_file(REPO_ROOT / "README.md", REPO_ROOT)
        self.assertFalse(report.passed)
        self.assertTrue(any("outside the SCAF repository" in e for e in report.errors))

    def test_external_pin_symlink_fails(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            temp = Path(temp_dir)
            real_pin = temp / "real-pin.json"
            real_pin.write_text(json.dumps(accepted_pin()), encoding="utf-8")
            link_pin = temp / "pin-link.json"
            try:
                link_pin.symlink_to(real_pin)
            except (OSError, NotImplementedError):
                self.skipTest("symlink creation unavailable")
            report = validate_external_pin_file(link_pin, REPO_ROOT)
            self.assertFalse(report.passed)
            self.assertTrue(any("must not be a symlink" in e for e in report.errors))

    def test_production_cli_passes_with_external_pin_and_is_cwd_independent(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            temp = Path(temp_dir)
            pin_path = temp / "trusted-pin.json"
            pin_path.write_text(json.dumps(accepted_pin(), indent=2), encoding="utf-8")
            fake_cwd = temp / "cwd"
            fake_cwd.mkdir()
            env = os.environ.copy()
            env["PYTHONPATH"] = str(REPO_ROOT)
            run = subprocess.run(
                [sys.executable, "-m", "tools.scaf_external_pin.checker", "--pin-file", str(pin_path)],
                cwd=fake_cwd,
                env=env,
                text=True,
                capture_output=True,
                check=False,
            )
            self.assertEqual(run.returncode, 0, run.stdout + run.stderr)
            self.assertIn(f"Repository: {REPO_ROOT}", run.stdout)
            self.assertIn("Pinned artifacts: 2", run.stdout)
            self.assertIn("RESULT: PASS", run.stdout)

    def test_production_cli_wrong_pin_fails(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            pin = accepted_pin()
            pin["artifacts"][0]["sha256"] = "0" * 64
            pin_path = Path(temp_dir) / "bad-pin.json"
            pin_path.write_text(json.dumps(pin), encoding="utf-8")
            env = os.environ.copy()
            env["PYTHONPATH"] = str(REPO_ROOT)
            run = subprocess.run(
                [sys.executable, "-m", "tools.scaf_external_pin.checker", "--pin-file", str(pin_path)],
                cwd=REPO_ROOT,
                env=env,
                text=True,
                capture_output=True,
                check=False,
            )
            self.assertEqual(run.returncode, 1)
            self.assertIn("RESULT: FAIL", run.stdout)
            self.assertIn("SHA-256 mismatch", run.stdout)

    def test_production_cli_rejects_repo_and_artifact_overrides(self):
        env = os.environ.copy()
        env["PYTHONPATH"] = str(REPO_ROOT)
        with tempfile.TemporaryDirectory() as temp_dir:
            pin_path = Path(temp_dir) / "trusted-pin.json"
            pin_path.write_text(json.dumps(accepted_pin()), encoding="utf-8")
            for args in (("--repo-root", "anything"), ("--artifact", "anything"), ("--hash-algorithm", "md5")):
                run = subprocess.run(
                    [sys.executable, "-m", "tools.scaf_external_pin.checker", "--pin-file", str(pin_path), *args],
                    cwd=REPO_ROOT,
                    env=env,
                    text=True,
                    capture_output=True,
                    check=False,
                )
                self.assertEqual(run.returncode, 2)
                self.assertIn("unrecognized arguments", run.stderr)
                self.assertNotIn("RESULT: PASS", run.stdout)

    def _run_cli_against_repo_copy_with_artifact_symlink(self, artifact_rel: str):
        with tempfile.TemporaryDirectory() as temp_dir:
            temp = Path(temp_dir)
            repo_copy = temp / "System-Control-Architecture-Framework"
            import shutil
            shutil.copytree(REPO_ROOT, repo_copy, symlinks=True)

            artifact = repo_copy / artifact_rel
            real_artifact = artifact.with_name(artifact.name + ".real")
            artifact.rename(real_artifact)
            try:
                artifact.symlink_to(real_artifact.name)
            except (OSError, NotImplementedError):
                self.skipTest("symlink creation unavailable")

            pin = {
                "pin_version": 1,
                "pin_scope": EXPECTED_PIN_SCOPE,
                "hash_algorithm": "sha256",
                "artifacts": [
                    {"path": MANIFEST_REL, "sha256": sha256_file(repo_copy / MANIFEST_REL)},
                    {"path": CHECKER_REL, "sha256": sha256_file(repo_copy / CHECKER_REL)},
                ],
            }
            pin_path = temp / "trusted-pin.json"
            pin_path.write_text(json.dumps(pin), encoding="utf-8")

            env = os.environ.copy()
            env["PYTHONPATH"] = str(repo_copy)
            run = subprocess.run(
                [sys.executable, "-m", "tools.scaf_external_pin.checker", "--pin-file", str(pin_path)],
                cwd=repo_copy,
                env=env,
                text=True,
                capture_output=True,
                check=False,
            )
            self.assertEqual(run.returncode, 1, run.stdout + run.stderr)
            self.assertIn("RESULT: FAIL", run.stdout)
            self.assertIn(f"pinned repository artifact must not be a symlink: {artifact_rel}", run.stdout)
            self.assertNotIn(f"{artifact_rel}: MATCH", run.stdout)

    def test_production_cli_rejects_manifest_artifact_same_byte_symlink(self):
        self._run_cli_against_repo_copy_with_artifact_symlink(MANIFEST_REL)

    def test_production_cli_rejects_checker_artifact_same_byte_symlink(self):
        self._run_cli_against_repo_copy_with_artifact_symlink(CHECKER_REL)


if __name__ == "__main__":
    unittest.main()
