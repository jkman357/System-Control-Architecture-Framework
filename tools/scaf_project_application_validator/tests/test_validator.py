from __future__ import annotations

import copy
import json
import tempfile
import unittest
from pathlib import Path

import yaml

from tools.scaf_project_application_validator.validator import (
    StrictProjectApplicationLoader,
    validate_project_application,
)


REPO_ROOT = Path(__file__).resolve().parents[3]


class ProjectApplicationValidatorTests(unittest.TestCase):
    def make_repo(self) -> Path:
        temp = tempfile.TemporaryDirectory()
        self.addCleanup(temp.cleanup)
        root = Path(temp.name) / "repo"
        root.mkdir()

        for relative in [
            "examples/project-application.yaml",
            "schemas/project-application.schema.json",
            "authority-registry.yaml",
            "schemas/authority-registry.schema.json",
        ]:
            source = REPO_ROOT / relative
            target = root / relative
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(source.read_bytes())

        source_normative = REPO_ROOT / "docs/normative"
        for source in source_normative.glob("*.md"):
            relative = source.relative_to(REPO_ROOT)
            target = root / relative
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(source.read_bytes())

        return root

    def input_path(self, root: Path) -> Path:
        return root / "examples/project-application.yaml"

    def load_input(self, root: Path):
        with self.input_path(root).open("r", encoding="utf-8") as stream:
            return yaml.load(stream, Loader=StrictProjectApplicationLoader)

    def write_input(self, root: Path, data) -> None:
        self.input_path(root).write_text(
            yaml.safe_dump(data, sort_keys=False, allow_unicode=True),
            encoding="utf-8",
        )

    def mutate_text(self, root: Path, old: str, new: str, count: int = 1) -> None:
        path = self.input_path(root)
        text = path.read_text(encoding="utf-8")
        self.assertIn(old, text)
        path.write_text(text.replace(old, new, count), encoding="utf-8")

    def test_accepted_repository_fixture_passes(self):
        report = validate_project_application(REPO_ROOT)
        self.assertTrue(report.passed, report.errors)
        self.assertEqual(3, report.record_count)
        self.assertTrue(report.loader_policy_valid)
        self.assertTrue(report.schema_valid)
        self.assertTrue(report.record_identity_unique)
        self.assertTrue(report.authority_scope_unique)
        self.assertTrue(report.canonical_order_valid)
        self.assertTrue(report.authority_registry_valid)
        self.assertTrue(report.authority_resolution_valid)

    def test_duplicate_raw_yaml_key_fails(self):
        root = self.make_repo()
        self.mutate_text(
            root,
            '    record_kind: "project_application"\n',
            '    record_kind: "project_application"\n    record_kind: "project_application"\n',
        )
        report = validate_project_application(root)
        self.assertFalse(report.passed)
        self.assertTrue(any("duplicate key" in error for error in report.errors))

    def test_yaml_anchor_fails(self):
        root = self.make_repo()
        self.mutate_text(root, 'record_id: "EXAMPLE-PA-001"', 'record_id: &rid "EXAMPLE-PA-001"')
        report = validate_project_application(root)
        self.assertFalse(report.passed)
        self.assertTrue(any("anchors are prohibited" in error for error in report.errors))

    def test_yaml_alias_fails(self):
        root = self.make_repo()
        self.mutate_text(root, 'record_id: "EXAMPLE-PA-001"', 'record_id: &rid "EXAMPLE-PA-001"')
        self.mutate_text(root, 'project_scope_ref: "example:scope:system"', 'project_scope_ref: *rid')
        report = validate_project_application(root)
        self.assertFalse(report.passed)
        self.assertTrue(any("aliases are prohibited" in error for error in report.errors))

    def test_yaml_merge_key_fails(self):
        root = self.make_repo()
        self.mutate_text(
            root,
            "    disposition_basis:\n      summary:",
            "    disposition_basis:\n      <<: {}\n      summary:",
        )
        report = validate_project_application(root)
        self.assertFalse(report.passed)
        self.assertTrue(any("merge keys are prohibited" in error for error in report.errors))

    def test_custom_yaml_tag_fails(self):
        root = self.make_repo()
        self.mutate_text(root, 'record_id: "EXAMPLE-PA-001"', 'record_id: !example "EXAMPLE-PA-001"')
        report = validate_project_application(root)
        self.assertFalse(report.passed)
        self.assertTrue(any("custom YAML tags are prohibited" in error for error in report.errors))

    def test_multi_document_stream_fails(self):
        root = self.make_repo()
        path = self.input_path(root)
        path.write_text(path.read_text(encoding="utf-8") + "\n---\nrecords: []\n", encoding="utf-8")
        report = validate_project_application(root)
        self.assertFalse(report.passed)
        self.assertTrue(any("expected exactly one YAML document" in error for error in report.errors))

    def test_non_string_mapping_key_fails(self):
        root = self.make_repo()
        self.mutate_text(root, "records:\n", "1:\n")
        report = validate_project_application(root)
        self.assertFalse(report.passed)
        self.assertTrue(any("non-string mapping key" in error for error in report.errors))

    def test_schema_violation_is_rejected_before_cross_record_checks(self):
        root = self.make_repo()
        data = self.load_input(root)
        data["records"][0]["applicability"] = "yes"
        self.write_input(root, data)
        report = validate_project_application(root)
        self.assertFalse(report.passed)
        self.assertFalse(report.schema_valid)
        self.assertTrue(any("schema" in error.lower() for error in report.errors))

    def test_duplicate_record_id_across_nonidentical_records_fails(self):
        root = self.make_repo()
        data = self.load_input(root)
        duplicate = copy.deepcopy(data["records"][0])
        duplicate["project_scope_ref"] = "example:scope:system-2"
        data["records"].append(duplicate)
        data["records"].sort(key=lambda item: item["record_id"])
        self.write_input(root, data)
        report = validate_project_application(root)
        self.assertFalse(report.passed)
        self.assertFalse(report.record_identity_unique)
        self.assertTrue(any("duplicate record_id" in error for error in report.errors))

    def test_duplicate_authority_scope_pair_fails(self):
        root = self.make_repo()
        data = self.load_input(root)
        duplicate = copy.deepcopy(data["records"][0])
        duplicate["record_id"] = "EXAMPLE-PA-001A"
        data["records"].append(duplicate)
        data["records"].sort(key=lambda item: item["record_id"])
        self.write_input(root, data)
        report = validate_project_application(root)
        self.assertFalse(report.passed)
        self.assertFalse(report.authority_scope_unique)
        self.assertTrue(any("duplicate active" in error for error in report.errors))

    def test_noncanonical_record_order_fails(self):
        root = self.make_repo()
        data = self.load_input(root)
        data["records"][0], data["records"][1] = data["records"][1], data["records"][0]
        self.write_input(root, data)
        report = validate_project_application(root)
        self.assertFalse(report.passed)
        self.assertFalse(report.canonical_order_valid)
        self.assertTrue(any("records: non-canonical order" in error for error in report.errors))

    def assert_unsorted_surface_fails(self, record_index: int, accessor) -> None:
        root = self.make_repo()
        data = self.load_input(root)
        values = accessor(data["records"][record_index])
        self.assertGreaterEqual(len(values), 2)
        values[0], values[1] = values[1], values[0]
        self.write_input(root, data)
        report = validate_project_application(root)
        self.assertFalse(report.passed)
        self.assertFalse(report.canonical_order_valid)
        self.assertTrue(any("reference strings must be ordered" in error for error in report.errors))

    def test_noncanonical_basis_refs_order_fails(self):
        self.assert_unsorted_surface_fails(0, lambda record: record["disposition_basis"]["basis_refs"])

    def test_noncanonical_awaiting_refs_order_fails(self):
        self.assert_unsorted_surface_fails(2, lambda record: record["disposition_basis"]["awaiting_refs"])

    def test_noncanonical_decision_refs_order_fails(self):
        self.assert_unsorted_surface_fails(0, lambda record: record["decision_refs"])

    def test_noncanonical_authority_refs_order_fails(self):
        self.assert_unsorted_surface_fails(0, lambda record: record["authority_refs"])

    def test_noncanonical_supporting_refs_order_fails(self):
        self.assert_unsorted_surface_fails(0, lambda record: record["supporting_refs"])

    def test_unresolved_scaf_authority_id_fails(self):
        root = self.make_repo()
        data = self.load_input(root)
        data["records"][0]["scaf_authority_id"] = "SCAF-AK-999"
        self.write_input(root, data)
        report = validate_project_application(root)
        self.assertFalse(report.passed)
        self.assertFalse(report.authority_resolution_valid)
        self.assertTrue(any("unresolved frozen SCAF authority" in error for error in report.errors))

    def test_framework_normative_invariant_target_fails(self):
        root = self.make_repo()
        data = self.load_input(root)
        data["records"][0]["scaf_authority_id"] = "SCAF-AK-009"
        self.write_input(root, data)
        report = validate_project_application(root)
        self.assertFalse(report.passed)
        self.assertFalse(report.authority_resolution_valid)
        self.assertTrue(any("Framework Normative Invariant" in error for error in report.errors))

    def test_authority_source_release_mismatch_fails_source_resolution(self):
        # The accepted rc06 schema normally fixes scaf_source_release at v0.0.2.
        # A controlled test repository relaxes only that temporary schema constant
        # so this test can prove the independent source-aware release check. The
        # production CLI exposes no schema override.
        root = self.make_repo()
        schema_path = root / "schemas/project-application.schema.json"
        schema = json.loads(schema_path.read_text(encoding="utf-8"))
        schema["$defs"]["projectApplicationRecord"]["properties"]["scaf_source_release"] = {
            "const": "v0.0.1"
        }
        schema_path.write_text(json.dumps(schema, indent=2) + "\n", encoding="utf-8")

        data = self.load_input(root)
        for record in data["records"]:
            record["scaf_source_release"] = "v0.0.1"
        self.write_input(root, data)
        report = validate_project_application(root)
        self.assertFalse(report.passed)
        self.assertTrue(report.schema_valid)
        self.assertFalse(report.authority_resolution_valid)
        self.assertTrue(any("source_release" in error for error in report.errors))

    def test_unresolved_project_controlled_reference_remains_valid(self):
        root = self.make_repo()
        data = self.load_input(root)
        data["records"][1]["decision_refs"] = ["project:decision:does-not-exist"]
        self.write_input(root, data)
        report = validate_project_application(root)
        self.assertTrue(report.passed, report.errors)


if __name__ == "__main__":
    unittest.main()
