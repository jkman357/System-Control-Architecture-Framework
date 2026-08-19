from __future__ import annotations

import copy
import hashlib
import io
import tempfile
import unittest
from contextlib import redirect_stdout
from pathlib import Path

import yaml

from tools.scaf_context_source_association_validator.validator import (
    main,
    validate_context_source_associations,
)


REPO_ROOT = Path(__file__).resolve().parents[3]
ASSOCIATIONS_PATH = REPO_ROOT / "examples" / "context-source-associations.yaml"
SELECTION_PATH = REPO_ROOT / "examples" / "consumption-selection.yaml"


class QuotedStringDumper(yaml.SafeDumper):
    pass


def _represent_str(dumper: yaml.SafeDumper, data: str):
    return dumper.represent_scalar("tag:yaml.org,2002:str", data, style='"')


QuotedStringDumper.add_representer(str, _represent_str)


def _dump_yaml(data: object) -> bytes:
    return yaml.dump(
        data,
        Dumper=QuotedStringDumper,
        sort_keys=False,
        default_flow_style=False,
        allow_unicode=True,
    ).encode("utf-8")


class ContextSourceAssociationValidatorTests(unittest.TestCase):
    maxDiff = None

    def setUp(self) -> None:
        self.associations = yaml.safe_load(ASSOCIATIONS_PATH.read_text(encoding="utf-8"))
        self.selection = yaml.safe_load(SELECTION_PATH.read_text(encoding="utf-8"))
        self.temp = tempfile.TemporaryDirectory(prefix="scaf-context-source-association-test-")
        self.temp_root = Path(self.temp.name)

    def tearDown(self) -> None:
        self.temp.cleanup()

    def _write_associations_data(self, data: object, name: str = "associations.yaml") -> Path:
        path = self.temp_root / name
        path.write_bytes(_dump_yaml(data))
        return path

    def _write_associations_text(self, text: str, name: str = "associations.yaml") -> Path:
        path = self.temp_root / name
        path.write_text(text, encoding="utf-8")
        return path

    def _write_selection_data(self, data: object, name: str = "selection.yaml") -> Path:
        path = self.temp_root / name
        path.write_bytes(_dump_yaml(data))
        return path

    def _validate(self, associations_path: Path | None = None, selection_path: Path | None = None):
        return validate_context_source_associations(
            REPO_ROOT,
            associations_path,
            selection_path,
        )

    def test_accepted_fixture_passes_with_expected_counts(self) -> None:
        report = self._validate()
        self.assertTrue(report.passed, report.errors)
        self.assertEqual(report.included_authority_count, 2)
        self.assertEqual(report.source_unit_count, 2)
        self.assertEqual(report.association_count, 2)
        self.assertEqual(report.exact_instance_constraint_count, 2)

    def test_duplicate_raw_yaml_key_is_rejected(self) -> None:
        text = ASSOCIATIONS_PATH.read_text(encoding="utf-8").replace(
            'association_set_kind: "context_source_association_set"\n',
            'association_set_kind: "context_source_association_set"\nassociation_set_kind: "context_source_association_set"\n',
            1,
        )
        report = self._validate(self._write_associations_text(text))
        self.assertFalse(report.passed)
        self.assertTrue(any("duplicate key" in error for error in report.errors), report.errors)

    def test_yaml_anchor_is_rejected(self) -> None:
        text = ASSOCIATIONS_PATH.read_text(encoding="utf-8").replace(
            'source_identity_ref: "repo:docs/normative/00_SCAF_Authority_Kernel.md"',
            'source_identity_ref: &identity "repo:docs/normative/00_SCAF_Authority_Kernel.md"',
            1,
        )
        report = self._validate(self._write_associations_text(text))
        self.assertFalse(report.passed)
        self.assertTrue(any("anchors are prohibited" in error for error in report.errors), report.errors)

    def test_unquoted_string_value_is_rejected(self) -> None:
        text = ASSOCIATIONS_PATH.read_text(encoding="utf-8").replace(
            'association_set_kind: "context_source_association_set"',
            'association_set_kind: context_source_association_set',
            1,
        )
        report = self._validate(self._write_associations_text(text))
        self.assertFalse(report.passed)
        self.assertTrue(any("string scalar must be quoted" in error for error in report.errors), report.errors)

    def test_schema_invalid_runtime_field_is_rejected(self) -> None:
        data = copy.deepcopy(self.associations)
        data["authority_source_entries"][0]["associations"][0]["resolution_status"] = "resolved"
        report = self._validate(self._write_associations_data(data))
        self.assertFalse(report.passed)
        self.assertTrue(any("Context Source Association schema" in error for error in report.errors), report.errors)

    def test_wrong_selection_sha_is_rejected(self) -> None:
        data = copy.deepcopy(self.associations)
        data["source_selection_binding"]["consumption_selection_source_sha256"] = "0" * 64
        report = self._validate(self._write_associations_data(data))
        self.assertFalse(report.passed)
        self.assertTrue(any("consumption_selection_source_sha256 mismatch" in error for error in report.errors), report.errors)

    def test_wrong_bound_scope_is_rejected(self) -> None:
        data = copy.deepcopy(self.associations)
        data["source_selection_binding"]["project_scope_ref"] = "example:scope:other"
        report = self._validate(self._write_associations_data(data))
        self.assertFalse(report.passed)
        self.assertTrue(any("project_scope_ref does not match" in error for error in report.errors), report.errors)

    def test_upstream_invalid_selection_is_rejected_before_domain_proof(self) -> None:
        selection = copy.deepcopy(self.selection)
        selection["selected_entries"][0]["scaf_authority_id"] = "SCAF-NOPE-999"
        selection_path = self._write_selection_data(selection)
        data = copy.deepcopy(self.associations)
        data["source_selection_binding"]["consumption_selection_source_sha256"] = hashlib.sha256(
            selection_path.read_bytes()
        ).hexdigest()
        association_path = self._write_associations_data(data)
        report = self._validate(association_path, selection_path)
        self.assertFalse(report.passed)
        self.assertFalse(report.upstream_selection_validation_valid)
        self.assertTrue(any("failed accepted source-aware validation" in error for error in report.errors), report.errors)

    def test_missing_authority_source_entry_is_rejected(self) -> None:
        data = copy.deepcopy(self.associations)
        data["authority_source_entries"] = data["authority_source_entries"][:1]
        report = self._validate(self._write_associations_data(data))
        self.assertFalse(report.passed)
        self.assertTrue(any("does not equal validated Consumption Selection included domain I" in error for error in report.errors), report.errors)

    def test_extra_authority_source_entry_is_rejected(self) -> None:
        data = copy.deepcopy(self.associations)
        data["authority_source_entries"].append(
            {"scaf_authority_id": "SCAF-ZZ-999", "associations": []}
        )
        report = self._validate(self._write_associations_data(data))
        self.assertFalse(report.passed)
        self.assertTrue(any("does not equal validated Consumption Selection included domain I" in error for error in report.errors), report.errors)

    def test_duplicate_authority_id_nonidentical_entry_is_rejected(self) -> None:
        data = copy.deepcopy(self.associations)
        data["authority_source_entries"].append(
            {"scaf_authority_id": "SCAF-AK-002", "associations": [copy.deepcopy(data["authority_source_entries"][0]["associations"][0])]}
        )
        report = self._validate(self._write_associations_data(data))
        self.assertFalse(report.passed)
        self.assertTrue(any("duplicate scaf_authority_id" in error for error in report.errors), report.errors)

    def test_duplicate_source_unit_id_is_rejected(self) -> None:
        data = copy.deepcopy(self.associations)
        data["source_units"][1]["source_unit_id"] = data["source_units"][0]["source_unit_id"]
        report = self._validate(self._write_associations_data(data))
        self.assertFalse(report.passed)
        self.assertTrue(any("duplicate source_unit_id" in error for error in report.errors), report.errors)

    def test_duplicate_source_identity_is_rejected(self) -> None:
        data = copy.deepcopy(self.associations)
        data["source_units"][1]["source_identity_ref"] = data["source_units"][0]["source_identity_ref"]
        report = self._validate(self._write_associations_data(data))
        self.assertFalse(report.passed)
        self.assertTrue(any("duplicate source_identity_ref" in error for error in report.errors), report.errors)

    def test_unknown_source_unit_ref_is_rejected(self) -> None:
        data = copy.deepcopy(self.associations)
        data["authority_source_entries"][0]["associations"][0]["source_unit_ref"] = "SRC-NOT-THERE"
        report = self._validate(self._write_associations_data(data))
        self.assertFalse(report.passed)
        self.assertTrue(any("does not resolve to source_units catalog" in error for error in report.errors), report.errors)

    def test_unused_source_unit_is_rejected(self) -> None:
        data = copy.deepcopy(self.associations)
        data["source_units"].append(
            {
                "source_unit_id": "SRC-Z-UNUSED",
                "source_identity_ref": "opaque:unused",
                "control_domain": "project",
            }
        )
        report = self._validate(self._write_associations_data(data))
        self.assertFalse(report.passed)
        self.assertTrue(any("unused Source Unit" in error for error in report.errors), report.errors)

    def test_duplicate_semantic_association_with_different_provenance_is_rejected(self) -> None:
        data = copy.deepcopy(self.associations)
        duplicate = copy.deepcopy(data["authority_source_entries"][0]["associations"][0])
        duplicate["association_provenance"] = {
            "assertion_kind": "controlled_rule_derived",
            "basis_refs": ["rule:alternate"],
        }
        data["authority_source_entries"][0]["associations"].insert(1, duplicate)
        report = self._validate(self._write_associations_data(data))
        self.assertFalse(report.passed)
        self.assertTrue(any("duplicate semantic Controlled Source Association" in error for error in report.errors), report.errors)

    def test_noncanonical_root_order_is_rejected(self) -> None:
        data = copy.deepcopy(self.associations)
        reordered = {"representation_release": data.pop("representation_release")}
        reordered.update(data)
        report = self._validate(self._write_associations_data(reordered))
        self.assertFalse(report.passed)
        self.assertTrue(any("association root: non-canonical" in error for error in report.errors), report.errors)

    def test_noncanonical_source_unit_order_is_rejected(self) -> None:
        data = copy.deepcopy(self.associations)
        data["source_units"] = list(reversed(data["source_units"]))
        report = self._validate(self._write_associations_data(data))
        self.assertFalse(report.passed)
        self.assertTrue(any("source_units: non-canonical" in error for error in report.errors), report.errors)

    def test_noncanonical_authority_entry_order_is_rejected(self) -> None:
        data = copy.deepcopy(self.associations)
        data["authority_source_entries"] = list(reversed(data["authority_source_entries"]))
        report = self._validate(self._write_associations_data(data))
        self.assertFalse(report.passed)
        self.assertTrue(any("authority_source_entries: non-canonical" in error for error in report.errors), report.errors)

    def test_noncanonical_association_order_is_rejected(self) -> None:
        data = copy.deepcopy(self.associations)
        data["authority_source_entries"][0]["associations"] = list(
            reversed(data["authority_source_entries"][0]["associations"])
        )
        report = self._validate(self._write_associations_data(data))
        self.assertFalse(report.passed)
        self.assertTrue(any("associations: non-canonical semantic order" in error for error in report.errors), report.errors)

    def test_noncanonical_provenance_basis_order_is_rejected(self) -> None:
        data = copy.deepcopy(self.associations)
        provenance = data["authority_source_entries"][0]["associations"][0]["association_provenance"]
        provenance["basis_refs"] = ["Z-BASIS", "A-BASIS"]
        report = self._validate(self._write_associations_data(data))
        self.assertFalse(report.passed)
        self.assertTrue(any("basis_refs: non-canonical order" in error for error in report.errors), report.errors)

    def test_wrong_repository_instance_sha_is_rejected(self) -> None:
        data = copy.deepcopy(self.associations)
        data["authority_source_entries"][0]["associations"][0]["instance_constraint"]["value"] = "0" * 64
        report = self._validate(self._write_associations_data(data))
        self.assertFalse(report.passed)
        self.assertTrue(any("instance_constraint SHA-256 mismatch" in error for error in report.errors), report.errors)

    def test_unsafe_repo_identity_with_instance_constraint_is_rejected(self) -> None:
        data = copy.deepcopy(self.associations)
        data["source_units"][0]["source_identity_ref"] = "repo:../outside.md"
        report = self._validate(self._write_associations_data(data))
        self.assertFalse(report.passed)
        self.assertTrue(any("cannot be proven under the bounded repository-local repo: identity boundary" in error for error in report.errors), report.errors)

    def test_nonrepo_identity_with_instance_constraint_is_not_silently_resolved(self) -> None:
        data = copy.deepcopy(self.associations)
        data["source_units"][0]["source_identity_ref"] = "external:example"
        report = self._validate(self._write_associations_data(data))
        self.assertFalse(report.passed)
        self.assertTrue(any("cannot be proven under the bounded repository-local repo: identity boundary" in error for error in report.errors), report.errors)

    def test_cli_default_fixture_passes(self) -> None:
        stdout = io.StringIO()
        with redirect_stdout(stdout):
            code = main([])
        self.assertEqual(code, 0, stdout.getvalue())
        self.assertIn("CONTEXT SOURCE ASSOCIATION SOURCE RESULT: PASS", stdout.getvalue())


if __name__ == "__main__":
    unittest.main()
