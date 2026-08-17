from __future__ import annotations

import copy
import json
import os
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from tools.scaf_release_integrity.checker import (
    load_manifest,
    validate_release_integrity,
    validate_release_integrity_data,
)


REPO_ROOT = Path(__file__).resolve().parents[3]
MANIFEST_PATH = REPO_ROOT / "release-integrity" / "frozen-baseline-manifest.json"


class FrozenBaselineReleaseIntegrityTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.manifest = load_manifest(MANIFEST_PATH)

    def _copy_protected_trees(self, target_root: Path) -> None:
        for rel in ("docs/normative", "docs/l3"):
            dst = target_root / rel
            dst.parent.mkdir(parents=True, exist_ok=True)
            shutil.copytree(REPO_ROOT / rel, dst)

    def test_accepted_frozen_trees_pass(self):
        report = validate_release_integrity(REPO_ROOT, MANIFEST_PATH)
        self.assertTrue(report.passed, "\n".join(report.errors))
        self.assertEqual(report.protected_tree_count, 2)
        self.assertEqual(report.protected_file_count, 41)

    def test_modified_protected_file_fails(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            self._copy_protected_trees(root)
            target = root / "docs/normative/00_SCAF_Authority_Kernel.md"
            target.write_bytes(target.read_bytes() + b"\nmutation\n")
            report = validate_release_integrity_data(copy.deepcopy(self.manifest), root)
            self.assertFalse(report.passed)
            self.assertTrue(any("SHA-256 mismatch" in e for e in report.errors))

    def test_added_protected_file_fails(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            self._copy_protected_trees(root)
            (root / "docs/l3/UNEXPECTED.md").write_text("unexpected", encoding="utf-8")
            report = validate_release_integrity_data(copy.deepcopy(self.manifest), root)
            self.assertFalse(report.passed)
            self.assertTrue(any("unexpected protected file added" in e for e in report.errors))

    def test_removed_protected_file_fails(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            self._copy_protected_trees(root)
            (root / "docs/l3/00_L3_Catalog_Governance.md").unlink()
            report = validate_release_integrity_data(copy.deepcopy(self.manifest), root)
            self.assertFalse(report.passed)
            self.assertTrue(any("protected file missing" in e for e in report.errors))

    def test_manifest_hash_corruption_fails(self):
        manifest = copy.deepcopy(self.manifest)
        manifest["protected_trees"][0]["files"][0]["sha256"] = "0" * 64
        report = validate_release_integrity_data(manifest, REPO_ROOT)
        self.assertFalse(report.passed)
        self.assertTrue(any("SHA-256 mismatch" in e for e in report.errors))

    def test_manifest_path_escape_fails(self):
        manifest = copy.deepcopy(self.manifest)
        manifest["protected_trees"][0]["files"][0]["path"] = "../outside.md"
        report = validate_release_integrity_data(manifest, REPO_ROOT)
        self.assertFalse(report.passed)
        self.assertTrue(any("outside protected tree" in e for e in report.errors))

    def test_symlink_failure_marks_tree_summary_mismatch(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            self._copy_protected_trees(root)
            link = root / "docs/l3/SYMLINK.md"
            link.symlink_to(root / "docs/l3/README.md")
            report = validate_release_integrity_data(copy.deepcopy(self.manifest), root)
            self.assertFalse(report.passed)
            self.assertTrue(any("symlink is not allowed" in e for e in report.errors))
            self.assertIn("docs/l3: 30 files / MISMATCH", report.tree_summaries)

    def test_production_checker_uses_module_repository_not_cwd(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            fake_cwd = Path(temp_dir)
            fake_manifest = fake_cwd / "release-integrity/frozen-baseline-manifest.json"
            fake_manifest.parent.mkdir(parents=True)
            fake_manifest.write_text(json.dumps({}), encoding="utf-8")
            env = os.environ.copy()
            env["PYTHONPATH"] = str(REPO_ROOT)
            run = subprocess.run(
                [sys.executable, "-m", "tools.scaf_release_integrity.checker"],
                cwd=fake_cwd,
                env=env,
                text=True,
                capture_output=True,
                check=False,
            )
            self.assertEqual(run.returncode, 0, run.stdout + run.stderr)
            self.assertIn(f"Repository: {REPO_ROOT}", run.stdout)
            self.assertIn(f"Manifest:   {MANIFEST_PATH}", run.stdout)
            self.assertIn("RESULT: PASS", run.stdout)

    def test_production_checker_rejects_manifest_and_repo_overrides(self):
        env = os.environ.copy()
        env["PYTHONPATH"] = str(REPO_ROOT)
        for args in (("--manifest", "anything.json"), ("--repo-root", "anything")):
            run = subprocess.run(
                [sys.executable, "-m", "tools.scaf_release_integrity.checker", *args],
                cwd=REPO_ROOT,
                env=env,
                text=True,
                capture_output=True,
                check=False,
            )
            self.assertEqual(run.returncode, 2)
            self.assertIn("unrecognized arguments", run.stderr)
            self.assertNotIn("RESULT: PASS", run.stdout)


if __name__ == "__main__":
    unittest.main()
