from __future__ import annotations

import copy
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

import yaml

from tools.scaf_validator.validator import load_registry, load_schema, validate_registry_data


REPO_ROOT = Path(__file__).resolve().parents[3]
REGISTRY_PATH = REPO_ROOT / "authority-registry.yaml"
SCHEMA_PATH = REPO_ROOT / "schemas" / "authority-registry.schema.json"


class AuthorityRegistryValidatorTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.registry = load_registry(REGISTRY_PATH)
        cls.schema = load_schema(SCHEMA_PATH)

    def validate_mutation(self, mutation):
        data = copy.deepcopy(self.registry)
        mutation(data)
        return validate_registry_data(data, self.schema, REPO_ROOT)

    def test_accepted_registry_passes(self):
        report = validate_registry_data(copy.deepcopy(self.registry), self.schema, REPO_ROOT)
        self.assertTrue(report.passed, "\n".join(report.errors))
        self.assertEqual(report.record_count, 294)
        self.assertEqual(report.unique_id_count, 294)
        self.assertEqual(report.source_requirement_count, 294)
        self.assertEqual(report.project_applicable_count, 218)
        self.assertEqual(report.framework_invariant_count, 76)

    def test_duplicate_id_fails(self):
        def mutate(data):
            data["records"][1]["id"] = data["records"][0]["id"]
            data["records"][1]["source_anchor"] = data["records"][0]["id"]

        report = self.validate_mutation(mutate)
        self.assertFalse(report.passed)
        self.assertTrue(any("duplicate authority id" in error for error in report.errors))

    def test_source_anchor_mismatch_fails(self):
        def mutate(data):
            data["records"][0]["source_anchor"] = data["records"][1]["id"]

        report = self.validate_mutation(mutate)
        self.assertFalse(report.passed)
        self.assertTrue(any("source_anchor" in error for error in report.errors))

    def test_source_path_mismatch_fails(self):
        def mutate(data):
            data["records"][0]["source_path"] = "docs/normative/10_SCAF_CTX_System_Context_Obligations.md"

        report = self.validate_mutation(mutate)
        self.assertFalse(report.passed)
        self.assertTrue(any("does not match canonical" in error for error in report.errors))

    def test_authority_class_target_mismatch_fails(self):
        def mutate(data):
            current = data["records"][0]["authority_class"]
            data["records"][0]["authority_class"] = (
                "Framework Normative Invariant"
                if current == "Project-Applicable Obligation"
                else "Project-Applicable Obligation"
            )

        report = self.validate_mutation(mutate)
        self.assertFalse(report.passed)
        self.assertTrue(any("does not match source Target" in error for error in report.errors))

    def test_non_empty_relations_fail_schema(self):
        def mutate(data):
            data["records"][0]["relations"] = ["SCAF-AK-002"]

        report = self.validate_mutation(mutate)
        self.assertFalse(report.passed)
        self.assertTrue(any("schema" in error and "relations" in error for error in report.errors))

    def test_pattern_identity_fails_schema_and_source(self):
        def mutate(data):
            data["records"][0]["id"] = "SCAF-PAT-SUP-001"
            data["records"][0]["source_anchor"] = "SCAF-PAT-SUP-001"

        report = self.validate_mutation(mutate)
        self.assertFalse(report.passed)
        self.assertTrue(any("schema" in error and ".id" in error for error in report.errors))
        self.assertTrue(any("without canonical source requirement" in error for error in report.errors))

    def test_cli_cannot_bypass_canonical_schema(self):
        data = copy.deepcopy(self.registry)
        data["records"][0]["record_kind"] = "not_normative"
        data["records"][0]["relations"] = ["SCAF-AK-002"]

        with tempfile.TemporaryDirectory() as temp_dir:
            temp_root = Path(temp_dir)
            mutated_registry = temp_root / "mutated-registry.yaml"
            lax_schema = temp_root / "lax-schema.json"
            mutated_registry.write_text(
                yaml.safe_dump(data, sort_keys=False, allow_unicode=True),
                encoding="utf-8",
            )
            lax_schema.write_text(json.dumps({}), encoding="utf-8")

            canonical_run = subprocess.run(
                [
                    sys.executable,
                    "-m",
                    "tools.scaf_validator.validator",
                    "--registry",
                    str(mutated_registry),
                ],
                cwd=REPO_ROOT,
                text=True,
                capture_output=True,
                check=False,
            )
            self.assertNotEqual(canonical_run.returncode, 0)
            self.assertIn("RESULT: FAIL", canonical_run.stdout)
            self.assertIn("record_kind", canonical_run.stdout)
            self.assertIn("relations", canonical_run.stdout)

            bypass_attempt = subprocess.run(
                [
                    sys.executable,
                    "-m",
                    "tools.scaf_validator.validator",
                    "--registry",
                    str(mutated_registry),
                    "--schema",
                    str(lax_schema),
                ],
                cwd=REPO_ROOT,
                text=True,
                capture_output=True,
                check=False,
            )
            self.assertNotEqual(bypass_attempt.returncode, 0)
            self.assertIn("unrecognized arguments", bypass_attempt.stderr)


if __name__ == "__main__":
    unittest.main()
