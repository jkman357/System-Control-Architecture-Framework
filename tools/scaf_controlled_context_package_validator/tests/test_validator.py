from __future__ import annotations

import copy
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

import yaml

from tools.scaf_controlled_context_package_validator.validator import (
    validate_controlled_context_package,
)


REPO_ROOT = Path(__file__).resolve().parents[3]
PACKAGE = REPO_ROOT / "examples/controlled-context-package.yaml"
ASSOCIATIONS = REPO_ROOT / "examples/context-source-associations.yaml"
SELECTION = REPO_ROOT / "examples/consumption-selection.yaml"
PROFILE = REPO_ROOT / "examples/effective-project-profile.yaml"
PROJECT_APPLICATION = REPO_ROOT / "examples/project-application.yaml"


class QuotedDumper(yaml.SafeDumper):
    pass


def _quoted_str(dumper: yaml.SafeDumper, data: str):
    return dumper.represent_scalar("tag:yaml.org,2002:str", data, style='"')


QuotedDumper.add_representer(str, _quoted_str)


def _load(path: Path):
    return yaml.safe_load(path.read_text(encoding="utf-8"))


def _dump(data) -> str:
    return yaml.dump(
        data,
        Dumper=QuotedDumper,
        sort_keys=False,
        allow_unicode=True,
        default_flow_style=False,
        width=120,
    )


class ControlledContextPackageValidatorTests(unittest.TestCase):
    def _validate_data(self, package_data, *, association_data=None, selection_data=None):
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            package_path = root / "package.yaml"
            package_path.write_text(_dump(package_data), encoding="utf-8", newline="\n")
            if association_data is None:
                associations_path = ASSOCIATIONS
            else:
                associations_path = root / "associations.yaml"
                associations_path.write_text(
                    _dump(association_data), encoding="utf-8", newline="\n"
                )
            if selection_data is None:
                selection_path = SELECTION
            else:
                selection_path = root / "selection.yaml"
                selection_path.write_text(
                    _dump(selection_data), encoding="utf-8", newline="\n"
                )
            return validate_controlled_context_package(
                REPO_ROOT,
                package_path,
                associations_path,
                selection_path,
                PROFILE,
                PROJECT_APPLICATION,
            )

    def _validate_text(self, package_text: str):
        with tempfile.TemporaryDirectory() as temp_dir:
            package_path = Path(temp_dir) / "package.yaml"
            package_path.write_text(package_text, encoding="utf-8", newline="\n")
            return validate_controlled_context_package(
                REPO_ROOT,
                package_path,
                ASSOCIATIONS,
                SELECTION,
                PROFILE,
                PROJECT_APPLICATION,
            )

    def test_accepted_fixture_passes(self):
        report = validate_controlled_context_package(REPO_ROOT)
        self.assertTrue(report.passed, report.errors)
        self.assertEqual(report.included_authority_count, 2)
        self.assertEqual(report.association_handle_count, 2)
        self.assertEqual(report.materialization_decision_count, 2)
        self.assertEqual(report.materialized_context_item_count, 1)
        self.assertEqual(report.provenance_basis_count, 1)

    def test_duplicate_raw_yaml_key_is_rejected(self):
        text = PACKAGE.read_text(encoding="utf-8")
        text = text.replace(
            'package_kind: "controlled_context_package"',
            'package_kind: "controlled_context_package"\npackage_kind: "controlled_context_package"',
            1,
        )
        report = self._validate_text(text)
        self.assertFalse(report.passed)
        self.assertTrue(any("duplicate key" in error for error in report.errors), report.errors)

    def test_yaml_anchor_is_rejected(self):
        text = PACKAGE.read_text(encoding="utf-8").replace(
            'objective_id: "CTX-OBJ-EXAMPLE-001"',
            'objective_id: &objective "CTX-OBJ-EXAMPLE-001"',
            1,
        )
        report = self._validate_text(text)
        self.assertFalse(report.passed)
        self.assertTrue(any("anchors are prohibited" in error for error in report.errors), report.errors)

    def test_unquoted_string_is_rejected(self):
        text = PACKAGE.read_text(encoding="utf-8").replace(
            'package_kind: "controlled_context_package"',
            'package_kind: controlled_context_package',
            1,
        )
        report = self._validate_text(text)
        self.assertFalse(report.passed)
        self.assertTrue(any("must be quoted" in error for error in report.errors), report.errors)

    def test_schema_invalid_runtime_field_is_rejected(self):
        data = _load(PACKAGE)
        data["materialized_context_items"][0]["currentness"] = "current"
        report = self._validate_data(data)
        self.assertFalse(report.passed)
        self.assertTrue(any("schema" in error.lower() for error in report.errors), report.errors)

    def test_wrong_selection_sha_is_rejected(self):
        data = _load(PACKAGE)
        data["upstream_binding"]["consumption_selection"]["source_sha256"] = "0" * 64
        report = self._validate_data(data)
        self.assertFalse(report.passed)
        self.assertTrue(any("consumption_selection.source_sha256" in error for error in report.errors), report.errors)

    def test_wrong_association_sha_is_rejected(self):
        data = _load(PACKAGE)
        data["upstream_binding"]["context_source_association_set"]["source_sha256"] = "0" * 64
        report = self._validate_data(data)
        self.assertFalse(report.passed)
        self.assertTrue(any("context_source_association_set.source_sha256" in error for error in report.errors), report.errors)

    def test_invalid_upstream_selection_is_rejected_before_package_domain_proof(self):
        data = _load(PACKAGE)
        selection = _load(SELECTION)
        selection["unexpected_field"] = "invalid"
        report = self._validate_data(data, selection_data=selection)
        self.assertFalse(report.passed)
        self.assertFalse(report.upstream_association_validation_valid)
        self.assertTrue(any("bound Context Source Association Set failed" in error for error in report.errors), report.errors)

    def test_invalid_upstream_association_is_rejected(self):
        data = _load(PACKAGE)
        associations = _load(ASSOCIATIONS)
        associations["authority_source_entries"][0]["associations"][0]["resolution_status"] = "resolved"
        report = self._validate_data(data, association_data=associations)
        self.assertFalse(report.passed)
        self.assertFalse(report.upstream_association_validation_valid)

    def test_missing_authority_context_entry_is_rejected(self):
        data = _load(PACKAGE)
        data["authority_context_entries"] = data["authority_context_entries"][:1]
        report = self._validate_data(data)
        self.assertFalse(report.passed)
        self.assertTrue(any("does not equal validated I" in error for error in report.errors), report.errors)

    def test_extra_authority_context_entry_is_rejected(self):
        data = _load(PACKAGE)
        data["authority_context_entries"].append(
            {"scaf_authority_id": "SCAF-AK-003", "association_envelope": [], "materialization_decisions": []}
        )
        report = self._validate_data(data)
        self.assertFalse(report.passed)
        self.assertTrue(any("does not equal validated I" in error for error in report.errors), report.errors)

    def test_semantic_duplicate_authority_id_is_rejected(self):
        data = _load(PACKAGE)
        duplicate = copy.deepcopy(data["authority_context_entries"][0])
        duplicate["materialization_decisions"][0]["materialized_context_item_refs"] = ["CTX-ITEM-001", "CTX-ITEM-ALT"]
        data["authority_context_entries"].insert(1, duplicate)
        data["materialized_context_items"].append(
            {
                "materialized_context_item_id": "CTX-ITEM-ALT",
                "context_semantic": "source_preserving",
                "controlled_provenance_bases": [
                    {"scaf_authority_id": "SCAF-AK-001", "association_handle": "ASSOC-SCAF-AK-001-001"}
                ],
                "payload": {"payload_kind": "source_reference", "source_identity_ref": "repo:docs/normative/00_SCAF_Authority_Kernel.md"},
            }
        )
        report = self._validate_data(data)
        self.assertFalse(report.passed)
        self.assertTrue(any("duplicate scaf_authority_id" in error for error in report.errors), report.errors)

    def test_association_projection_mismatch_is_rejected(self):
        data = _load(PACKAGE)
        data["authority_context_entries"][0]["association_envelope"][0]["controlled_association"][
            "relationship_semantic"
        ] = "supporting_context_source"
        report = self._validate_data(data)
        self.assertFalse(report.passed)
        self.assertTrue(any("Association Envelope does not exactly match" in error for error in report.errors), report.errors)

    def test_duplicate_package_association_handle_is_rejected(self):
        data = _load(PACKAGE)
        first = data["authority_context_entries"][0]
        first["association_envelope"][1]["association_handle"] = first["association_envelope"][0]["association_handle"]
        first["materialization_decisions"][1]["association_handle"] = first["materialization_decisions"][0]["association_handle"]
        report = self._validate_data(data)
        self.assertFalse(report.passed)
        self.assertTrue(any("duplicate package-local handle" in error for error in report.errors), report.errors)

    def test_missing_materialization_decision_is_rejected(self):
        data = _load(PACKAGE)
        data["authority_context_entries"][0]["materialization_decisions"].pop()
        report = self._validate_data(data)
        self.assertFalse(report.passed)
        self.assertTrue(any("Decision handles/order" in error for error in report.errors), report.errors)

    def test_duplicate_materialization_decision_handle_is_rejected(self):
        data = _load(PACKAGE)
        entry = data["authority_context_entries"][0]
        entry["materialization_decisions"].append(
            {
                "association_handle": "ASSOC-SCAF-AK-001-001",
                "outcome": "not_materialized",
                "materialized_context_item_refs": [],
                "non_materialization_basis": "Duplicate semantic decision for test.",
            }
        )
        report = self._validate_data(data)
        self.assertFalse(report.passed)
        self.assertTrue(any("duplicate Materialization Decision handle" in error for error in report.errors), report.errors)

    def test_cross_entry_decision_handle_is_rejected(self):
        data = _load(PACKAGE)
        data["authority_context_entries"][1]["materialization_decisions"].append(
            {
                "association_handle": "ASSOC-SCAF-AK-001-001",
                "outcome": "not_materialized",
                "materialized_context_item_refs": [],
                "non_materialization_basis": "Cross-entry test.",
            }
        )
        report = self._validate_data(data)
        self.assertFalse(report.passed)
        self.assertTrue(any("cross-entry association handle" in error for error in report.errors), report.errors)

    def test_duplicate_materialized_context_item_id_is_rejected(self):
        data = _load(PACKAGE)
        duplicate = copy.deepcopy(data["materialized_context_items"][0])
        duplicate["context_semantic"] = "derived"
        data["materialized_context_items"].append(duplicate)
        report = self._validate_data(data)
        self.assertFalse(report.passed)
        self.assertTrue(any("duplicate materialized_context_item_id" in error for error in report.errors), report.errors)

    def test_unresolved_item_reference_is_rejected(self):
        data = _load(PACKAGE)
        data["authority_context_entries"][0]["materialization_decisions"][0]["materialized_context_item_refs"] = [
            "CTX-ITEM-MISSING"
        ]
        report = self._validate_data(data)
        self.assertFalse(report.passed)
        self.assertTrue(any("does not resolve" in error for error in report.errors), report.errors)

    def test_orphan_materialized_context_item_is_rejected(self):
        data = _load(PACKAGE)
        data["materialized_context_items"].append(
            {
                "materialized_context_item_id": "CTX-ITEM-ORPHAN",
                "context_semantic": "source_preserving",
                "controlled_provenance_bases": [
                    {"scaf_authority_id": "SCAF-AK-001", "association_handle": "ASSOC-SCAF-AK-001-001"}
                ],
                "payload": {"payload_kind": "source_reference", "source_identity_ref": "repo:docs/normative/00_SCAF_Authority_Kernel.md"},
            }
        )
        report = self._validate_data(data)
        self.assertFalse(report.passed)
        self.assertTrue(any("orphan item IDs" in error for error in report.errors), report.errors)

    def test_nonresolving_provenance_authority_is_rejected(self):
        data = _load(PACKAGE)
        data["materialized_context_items"][0]["controlled_provenance_bases"][0]["scaf_authority_id"] = "SCAF-AK-999"
        report = self._validate_data(data)
        self.assertFalse(report.passed)
        self.assertTrue(any("provenance basis" in error and "does not resolve" in error for error in report.errors), report.errors)

    def test_nonresolving_provenance_handle_is_rejected(self):
        data = _load(PACKAGE)
        data["materialized_context_items"][0]["controlled_provenance_bases"][0]["association_handle"] = "ASSOC-MISSING"
        report = self._validate_data(data)
        self.assertFalse(report.passed)
        self.assertTrue(any("provenance basis" in error and "does not resolve" in error for error in report.errors), report.errors)

    def test_decision_reference_without_matching_provenance_is_rejected(self):
        data = _load(PACKAGE)
        data["materialized_context_items"][0]["controlled_provenance_bases"][0]["association_handle"] = "ASSOC-SCAF-AK-001-002"
        report = self._validate_data(data)
        self.assertFalse(report.passed)
        self.assertTrue(any("lacks matching Controlled Provenance Basis" in error for error in report.errors), report.errors)

    def test_provenance_without_corresponding_materialized_decision_is_rejected(self):
        data = _load(PACKAGE)
        data["materialized_context_items"][0]["controlled_provenance_bases"].append(
            {"scaf_authority_id": "SCAF-AK-001", "association_handle": "ASSOC-SCAF-AK-001-002"}
        )
        report = self._validate_data(data)
        self.assertFalse(report.passed)
        self.assertTrue(any("has no corresponding materialized decision reference" in error for error in report.errors), report.errors)

    def test_noncanonical_root_order_is_rejected(self):
        data = _load(PACKAGE)
        reordered = {"representation_release": data["representation_release"], "package_kind": data["package_kind"]}
        for key, value in data.items():
            if key not in reordered:
                reordered[key] = value
        report = self._validate_data(reordered)
        self.assertFalse(report.passed)
        self.assertTrue(any("package root: non-canonical" in error for error in report.errors), report.errors)

    def test_noncanonical_authority_order_is_rejected(self):
        data = _load(PACKAGE)
        data["authority_context_entries"].reverse()
        report = self._validate_data(data)
        self.assertFalse(report.passed)
        self.assertTrue(any("non-canonical scaf_authority_id order" in error for error in report.errors), report.errors)

    def test_noncanonical_association_envelope_order_is_rejected(self):
        data = _load(PACKAGE)
        entry = data["authority_context_entries"][0]
        entry["association_envelope"].reverse()
        entry["materialization_decisions"].reverse()
        report = self._validate_data(data)
        self.assertFalse(report.passed)
        self.assertTrue(any("association_envelope: non-canonical semantic order" in error for error in report.errors), report.errors)

    def test_noncanonical_decision_order_is_rejected(self):
        data = _load(PACKAGE)
        data["authority_context_entries"][0]["materialization_decisions"].reverse()
        report = self._validate_data(data)
        self.assertFalse(report.passed)
        self.assertTrue(any("materialization_decisions: non-canonical" in error for error in report.errors), report.errors)

    def test_noncanonical_item_reference_order_is_rejected(self):
        data = _load(PACKAGE)
        decision = data["authority_context_entries"][0]["materialization_decisions"][0]
        decision["materialized_context_item_refs"] = ["CTX-ITEM-002", "CTX-ITEM-001"]
        data["materialized_context_items"].append(
            {
                "materialized_context_item_id": "CTX-ITEM-002",
                "context_semantic": "source_preserving",
                "controlled_provenance_bases": [
                    {"scaf_authority_id": "SCAF-AK-001", "association_handle": "ASSOC-SCAF-AK-001-001"}
                ],
                "payload": {"payload_kind": "source_reference", "source_identity_ref": "repo:docs/normative/00_SCAF_Authority_Kernel.md"},
            }
        )
        report = self._validate_data(data)
        self.assertFalse(report.passed)
        self.assertTrue(any("materialized_context_item_refs: non-canonical order" in error for error in report.errors), report.errors)

    def test_noncanonical_materialized_item_order_is_rejected(self):
        data = _load(PACKAGE)
        item2 = copy.deepcopy(data["materialized_context_items"][0])
        item2["materialized_context_item_id"] = "CTX-ITEM-000"
        data["materialized_context_items"].append(item2)
        data["authority_context_entries"][0]["materialization_decisions"][0]["materialized_context_item_refs"] = [
            "CTX-ITEM-000", "CTX-ITEM-001"
        ]
        report = self._validate_data(data)
        self.assertFalse(report.passed)
        self.assertTrue(any("materialized_context_items: non-canonical" in error for error in report.errors), report.errors)

    def test_noncanonical_provenance_order_is_rejected(self):
        data = _load(PACKAGE)
        item = data["materialized_context_items"][0]
        item["controlled_provenance_bases"] = [
            {"scaf_authority_id": "SCAF-AK-002", "association_handle": "ASSOC-Z"},
            {"scaf_authority_id": "SCAF-AK-001", "association_handle": "ASSOC-SCAF-AK-001-001"},
        ]
        report = self._validate_data(data)
        self.assertFalse(report.passed)
        self.assertTrue(any("controlled_provenance_bases: non-canonical order" in error for error in report.errors), report.errors)

    def test_cli_default_fixture_passes_and_has_no_schema_override(self):
        completed = subprocess.run(
            [sys.executable, "-m", "tools.scaf_controlled_context_package_validator.validator"],
            cwd=REPO_ROOT,
            capture_output=True,
            text=True,
            check=False,
        )
        self.assertEqual(completed.returncode, 0, completed.stdout + completed.stderr)
        self.assertIn("CONTROLLED CONTEXT PACKAGE SOURCE RESULT: PASS", completed.stdout)
        rejected = subprocess.run(
            [sys.executable, "-m", "tools.scaf_controlled_context_package_validator.validator", "--schema", "alternate.json"],
            cwd=REPO_ROOT,
            capture_output=True,
            text=True,
            check=False,
        )
        self.assertEqual(rejected.returncode, 2)
        self.assertIn("unrecognized arguments", rejected.stderr)


if __name__ == "__main__":
    unittest.main()
