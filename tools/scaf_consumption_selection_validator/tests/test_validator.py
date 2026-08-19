from __future__ import annotations

import copy
import hashlib
import io
import subprocess
import sys
import tempfile
import unittest
from contextlib import redirect_stderr, redirect_stdout
from pathlib import Path

import yaml

from tools.scaf_consumption_selection_validator.validator import (
    main,
    validate_consumption_selection,
)


REPO_ROOT = Path(__file__).resolve().parents[3]
SELECTION_PATH = REPO_ROOT / "examples" / "consumption-selection.yaml"
PROFILE_PATH = REPO_ROOT / "examples" / "effective-project-profile.yaml"
PROJECT_APPLICATION_PATH = REPO_ROOT / "examples" / "project-application.yaml"


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


class ConsumptionSelectionValidatorTests(unittest.TestCase):
    maxDiff = None

    def setUp(self) -> None:
        self.selection = yaml.safe_load(SELECTION_PATH.read_text(encoding="utf-8"))
        self.profile = yaml.safe_load(PROFILE_PATH.read_text(encoding="utf-8"))
        self.temp = tempfile.TemporaryDirectory(prefix="scaf-selection-test-")
        self.temp_root = Path(self.temp.name)

    def tearDown(self) -> None:
        self.temp.cleanup()

    def _write_selection_data(self, data: object, name: str = "selection.yaml") -> Path:
        path = self.temp_root / name
        path.write_bytes(_dump_yaml(data))
        return path

    def _write_selection_text(self, text: str, name: str = "selection.yaml") -> Path:
        path = self.temp_root / name
        path.write_text(text, encoding="utf-8")
        return path

    def _write_profile_data(self, data: object, name: str = "profile.yaml") -> Path:
        path = self.temp_root / name
        path.write_bytes(_dump_yaml(data))
        return path

    def _validate(
        self,
        selection_path: Path | None = None,
        profile_path: Path | None = None,
        project_application_path: Path | None = None,
    ):
        return validate_consumption_selection(
            REPO_ROOT,
            selection_path,
            profile_path,
            project_application_path,
        )

    def _selection_for_all_three(self) -> dict:
        data = copy.deepcopy(self.selection)
        data["bounded_omission"] = {"applied": False}
        data["selected_entries"] = [
            {
                "scaf_authority_id": "SCAF-AK-001",
                "profile_state": "applicable",
                "project_application_record_id": "EXAMPLE-PA-001",
            },
            {
                "scaf_authority_id": "SCAF-AK-002",
                "profile_state": "no_current_disposition",
            },
            {
                "scaf_authority_id": "SCAF-AK-003",
                "profile_state": "no_current_disposition",
            },
        ]
        data["selection_class"] = "filtered"
        return data

    def test_accepted_fixture_passes_with_expected_set_counts(self) -> None:
        report = self._validate()
        self.assertTrue(report.passed, report.errors)
        self.assertEqual(
            (report.domain_count, report.eligible_count, report.included_count,
             report.omitted_count, report.excluded_count),
            (218, 3, 2, 1, 215),
        )

    def test_duplicate_raw_yaml_key_is_rejected(self) -> None:
        text = SELECTION_PATH.read_text(encoding="utf-8")
        text = text.replace(
            'selection_kind: "consumption_selection"\n',
            'selection_kind: "consumption_selection"\nselection_kind: "consumption_selection"\n',
            1,
        )
        report = self._validate(self._write_selection_text(text))
        self.assertFalse(report.passed)
        self.assertTrue(any("duplicate key" in error for error in report.errors), report.errors)

    def test_yaml_anchor_is_rejected(self) -> None:
        text = SELECTION_PATH.read_text(encoding="utf-8").replace(
            'selection_purpose: "Illustrative',
            'selection_purpose: &purpose "Illustrative',
            1,
        )
        report = self._validate(self._write_selection_text(text))
        self.assertFalse(report.passed)
        self.assertTrue(any("anchors are prohibited" in error for error in report.errors), report.errors)

    def test_yaml_alias_is_rejected(self) -> None:
        text = SELECTION_PATH.read_text(encoding="utf-8")
        text = text.replace(
            'selection_purpose: "Illustrative bounded context-selection example over three exact PAO identities."',
            'selection_purpose: &purpose "Illustrative bounded context-selection example over three exact PAO identities."',
            1,
        )
        text = text.replace('basis: "Illustrative entry-count', 'basis: *purpose # ', 1)
        report = self._validate(self._write_selection_text(text))
        self.assertFalse(report.passed)
        self.assertTrue(any("aliases are prohibited" in error for error in report.errors), report.errors)

    def test_yaml_merge_key_is_rejected(self) -> None:
        text = SELECTION_PATH.read_text(encoding="utf-8").replace(
            'source_profile_binding:\n',
            'source_profile_binding:\n  <<: {}\n',
            1,
        )
        report = self._validate(self._write_selection_text(text))
        self.assertFalse(report.passed)
        self.assertTrue(any("merge keys are prohibited" in error for error in report.errors), report.errors)

    def test_custom_yaml_tag_is_rejected(self) -> None:
        text = SELECTION_PATH.read_text(encoding="utf-8").replace(
            'selection_purpose: "Illustrative',
            'selection_purpose: !custom "Illustrative',
            1,
        )
        report = self._validate(self._write_selection_text(text))
        self.assertFalse(report.passed)
        self.assertTrue(any("custom YAML tags are prohibited" in error for error in report.errors), report.errors)

    def test_multi_document_yaml_is_rejected(self) -> None:
        text = SELECTION_PATH.read_text(encoding="utf-8") + "\n---\n{}\n"
        report = self._validate(self._write_selection_text(text))
        self.assertFalse(report.passed)
        self.assertTrue(any("expected exactly one YAML document" in error for error in report.errors), report.errors)

    def test_non_string_yaml_key_is_rejected(self) -> None:
        text = SELECTION_PATH.read_text(encoding="utf-8").replace(
            'selection_kind: "consumption_selection"',
            '1: "invalid-key"\nselection_kind: "consumption_selection"',
            1,
        )
        report = self._validate(self._write_selection_text(text))
        self.assertFalse(report.passed)
        self.assertTrue(any("non-string mapping key" in error for error in report.errors), report.errors)

    def test_unquoted_string_value_is_rejected(self) -> None:
        text = SELECTION_PATH.read_text(encoding="utf-8").replace(
            'selection_kind: "consumption_selection"',
            'selection_kind: consumption_selection',
            1,
        )
        report = self._validate(self._write_selection_text(text))
        self.assertFalse(report.passed)
        self.assertTrue(any("string scalar must be quoted" in error for error in report.errors), report.errors)

    def test_schema_invalid_selection_stops_source_checks(self) -> None:
        data = copy.deepcopy(self.selection)
        data["selection_class"] = "invalid"
        report = self._validate(self._write_selection_data(data))
        self.assertFalse(report.passed)
        self.assertFalse(report.profile_validation_valid)
        self.assertTrue(any("Consumption Selection schema" in error for error in report.errors), report.errors)

    def test_noncanonical_root_mapping_order_is_rejected(self) -> None:
        data = copy.deepcopy(self.selection)
        reordered = {"representation_release": data.pop("representation_release")}
        reordered.update(data)
        report = self._validate(self._write_selection_data(reordered))
        self.assertFalse(report.passed)
        self.assertTrue(any("selection root: non-canonical" in error for error in report.errors), report.errors)

    def test_noncanonical_source_binding_mapping_order_is_rejected(self) -> None:
        data = copy.deepcopy(self.selection)
        binding = data["source_profile_binding"]
        data["source_profile_binding"] = {
            "scaf_source_release": binding["scaf_source_release"],
            "effective_project_profile_source_sha256": binding["effective_project_profile_source_sha256"],
            "project_scope_ref": binding["project_scope_ref"],
            "project_application_source_sha256": binding["project_application_source_sha256"],
        }
        report = self._validate(self._write_selection_data(data))
        self.assertFalse(report.passed)
        self.assertTrue(any("source_profile_binding: non-canonical" in error for error in report.errors), report.errors)

    def test_noncanonical_state_selector_order_is_rejected(self) -> None:
        data = copy.deepcopy(self.selection)
        data["state_selector"] = ["no_current_disposition", "applicable"]
        report = self._validate(self._write_selection_data(data))
        self.assertFalse(report.passed)
        self.assertTrue(any("state_selector: non-canonical" in error for error in report.errors), report.errors)

    def test_noncanonical_explicit_authority_order_is_rejected(self) -> None:
        data = copy.deepcopy(self.selection)
        data["authority_selector"]["scaf_authority_ids"] = [
            "SCAF-AK-002", "SCAF-AK-001", "SCAF-AK-003"
        ]
        report = self._validate(self._write_selection_data(data))
        self.assertFalse(report.passed)
        self.assertTrue(any("non-canonical exact-ID order" in error for error in report.errors), report.errors)

    def test_noncanonical_selected_entry_order_is_rejected(self) -> None:
        data = copy.deepcopy(self.selection)
        data["selected_entries"] = list(reversed(data["selected_entries"]))
        report = self._validate(self._write_selection_data(data))
        self.assertFalse(report.passed)
        self.assertTrue(any("selected_entries: non-canonical order" in error for error in report.errors), report.errors)

    def test_duplicate_selected_authority_id_nonidentical_entries_is_rejected(self) -> None:
        data = copy.deepcopy(self.selection)
        data["selected_entries"].append(
            {
                "scaf_authority_id": "SCAF-AK-002",
                "profile_state": "applicable",
                "project_application_record_id": "EXAMPLE-PA-001",
            }
        )
        report = self._validate(self._write_selection_data(data))
        self.assertFalse(report.passed)
        self.assertTrue(any("duplicate scaf_authority_id" in error for error in report.errors), report.errors)

    def test_wrong_profile_source_sha_is_rejected(self) -> None:
        data = copy.deepcopy(self.selection)
        data["source_profile_binding"]["effective_project_profile_source_sha256"] = "0" * 64
        report = self._validate(self._write_selection_data(data))
        self.assertFalse(report.passed)
        self.assertTrue(any("effective_project_profile_source_sha256 mismatch" in error for error in report.errors), report.errors)

    def test_wrong_bound_source_release_is_rejected(self) -> None:
        data = copy.deepcopy(self.selection)
        data["source_profile_binding"]["scaf_source_release"] = "v9.9.9"
        report = self._validate(self._write_selection_data(data))
        self.assertFalse(report.passed)
        self.assertTrue(any("source_profile_binding.scaf_source_release" in error for error in report.errors), report.errors)

    def test_wrong_bound_scope_is_rejected(self) -> None:
        data = copy.deepcopy(self.selection)
        data["source_profile_binding"]["project_scope_ref"] = "example:scope:other"
        report = self._validate(self._write_selection_data(data))
        self.assertFalse(report.passed)
        self.assertTrue(any("source_profile_binding.project_scope_ref" in error for error in report.errors), report.errors)

    def test_wrong_bound_project_application_sha_is_rejected(self) -> None:
        data = copy.deepcopy(self.selection)
        data["source_profile_binding"]["project_application_source_sha256"] = "0" * 64
        report = self._validate(self._write_selection_data(data))
        self.assertFalse(report.passed)
        self.assertTrue(any("source_profile_binding.project_application_source_sha256" in error for error in report.errors), report.errors)

    def test_invalid_bound_profile_is_rejected_after_digest_match(self) -> None:
        profile = copy.deepcopy(self.profile)
        profile["entries"][0]["profile_state"] = "undetermined"
        profile_path = self._write_profile_data(profile)
        profile_bytes = profile_path.read_bytes()
        data = copy.deepcopy(self.selection)
        data["source_profile_binding"]["effective_project_profile_source_sha256"] = hashlib.sha256(profile_bytes).hexdigest()
        report = self._validate(self._write_selection_data(data), profile_path)
        self.assertFalse(report.passed)
        self.assertFalse(report.profile_validation_valid)
        self.assertTrue(any("bound Effective Project Profile snapshot failed" in error for error in report.errors), report.errors)

    def test_explicit_unknown_authority_id_is_rejected(self) -> None:
        data = copy.deepcopy(self.selection)
        data["authority_selector"]["scaf_authority_ids"].append("SCAF-ZZZ-999")
        report = self._validate(self._write_selection_data(data))
        self.assertFalse(report.passed)
        self.assertTrue(any("outside the validated source-profile PAO domain" in error for error in report.errors), report.errors)

    def test_selected_unknown_authority_id_is_rejected(self) -> None:
        data = copy.deepcopy(self.selection)
        data["authority_selector"]["scaf_authority_ids"].append("SCAF-ZZZ-999")
        data["selected_entries"].append(
            {"scaf_authority_id": "SCAF-ZZZ-999", "profile_state": "no_current_disposition"}
        )
        report = self._validate(self._write_selection_data(data))
        self.assertFalse(report.passed)
        self.assertTrue(any("does not exist in the validated source profile" in error for error in report.errors), report.errors)

    def test_selected_entry_ineligible_by_state_is_rejected(self) -> None:
        data = copy.deepcopy(self.selection)
        data["state_selector"] = ["no_current_disposition"]
        report = self._validate(self._write_selection_data(data))
        self.assertFalse(report.passed)
        self.assertTrue(any("not eligible under" in error for error in report.errors), report.errors)

    def test_selected_entry_ineligible_by_authority_is_rejected(self) -> None:
        data = copy.deepcopy(self.selection)
        data["authority_selector"]["scaf_authority_ids"] = ["SCAF-AK-002", "SCAF-AK-003"]
        report = self._validate(self._write_selection_data(data))
        self.assertFalse(report.passed)
        self.assertTrue(any("not eligible under" in error for error in report.errors), report.errors)

    def test_selected_entry_state_mismatch_is_rejected(self) -> None:
        data = copy.deepcopy(self.selection)
        data["selected_entries"][1] = {
            "scaf_authority_id": "SCAF-AK-002",
            "profile_state": "undetermined",
            "project_application_record_id": "EXAMPLE-PA-001",
        }
        data["state_selector"] = ["applicable", "undetermined", "no_current_disposition"]
        report = self._validate(self._write_selection_data(data))
        self.assertFalse(report.passed)
        self.assertTrue(any("does not match source profile state" in error for error in report.errors), report.errors)

    def test_selected_entry_record_id_mismatch_is_rejected(self) -> None:
        data = copy.deepcopy(self.selection)
        data["selected_entries"][0]["project_application_record_id"] = "WRONG-PA"
        report = self._validate(self._write_selection_data(data))
        self.assertFalse(report.passed)
        self.assertTrue(any("project_application_record_id does not match" in error for error in report.errors), report.errors)

    def test_no_omission_requires_included_equals_eligible(self) -> None:
        data = copy.deepcopy(self.selection)
        data["bounded_omission"] = {"applied": False}
        report = self._validate(self._write_selection_data(data))
        self.assertFalse(report.passed)
        self.assertTrue(any("does not equal eligible set E" in error for error in report.errors), report.errors)

    def test_no_omission_exact_eligible_set_passes(self) -> None:
        report = self._validate(self._write_selection_data(self._selection_for_all_three()))
        self.assertTrue(report.passed, report.errors)
        self.assertEqual((report.eligible_count, report.included_count, report.omitted_count), (3, 3, 0))

    def test_applied_omission_with_no_actual_omission_is_allowed_by_rc02_subset_semantics(self) -> None:
        data = self._selection_for_all_three()
        data["bounded_omission"] = {"applied": True, "basis": "Bound was evaluated but did not remove an eligible entry."}
        report = self._validate(self._write_selection_data(data))
        self.assertTrue(report.passed, report.errors)
        self.assertEqual(report.omitted_count, 0)

    def test_wrong_selection_class_is_rejected(self) -> None:
        data = copy.deepcopy(self.selection)
        data["selection_class"] = "complete"
        report = self._validate(self._write_selection_data(data))
        self.assertFalse(report.passed)
        self.assertTrue(any("does not match derived classification" in error for error in report.errors), report.errors)

    def test_all_domain_applicable_only_filtered_selection_passes(self) -> None:
        data = copy.deepcopy(self.selection)
        data["state_selector"] = ["applicable"]
        data["authority_selector"] = {"mode": "all_domain"}
        data["bounded_omission"] = {"applied": False}
        data["selected_entries"] = [copy.deepcopy(self.profile["entries"][0])]
        data["selection_class"] = "filtered"
        report = self._validate(self._write_selection_data(data))
        self.assertTrue(report.passed, report.errors)
        self.assertEqual((report.eligible_count, report.included_count), (1, 1))

    def test_empty_state_selector_zero_eligible_filtered_selection_passes(self) -> None:
        data = copy.deepcopy(self.selection)
        data["state_selector"] = []
        data["authority_selector"] = {"mode": "all_domain"}
        data["bounded_omission"] = {"applied": False}
        data["selected_entries"] = []
        data["selection_class"] = "filtered"
        report = self._validate(self._write_selection_data(data))
        self.assertTrue(report.passed, report.errors)
        self.assertEqual((report.eligible_count, report.included_count, report.excluded_count), (0, 0, 218))

    def test_empty_explicit_authority_set_zero_eligible_filtered_selection_passes(self) -> None:
        data = copy.deepcopy(self.selection)
        data["authority_selector"] = {"mode": "explicit_set", "scaf_authority_ids": []}
        data["bounded_omission"] = {"applied": False}
        data["selected_entries"] = []
        data["selection_class"] = "filtered"
        report = self._validate(self._write_selection_data(data))
        self.assertTrue(report.passed, report.errors)
        self.assertEqual(report.eligible_count, 0)

    def test_all_domain_all_states_complete_selection_passes(self) -> None:
        data = copy.deepcopy(self.selection)
        data["state_selector"] = [
            "applicable", "not_applicable", "undetermined", "no_current_disposition"
        ]
        data["authority_selector"] = {"mode": "all_domain"}
        data["bounded_omission"] = {"applied": False}
        data["selected_entries"] = copy.deepcopy(self.profile["entries"])
        data["selection_class"] = "complete"
        report = self._validate(self._write_selection_data(data))
        self.assertTrue(report.passed, report.errors)
        self.assertEqual(
            (report.domain_count, report.eligible_count, report.included_count,
             report.omitted_count, report.excluded_count),
            (218, 218, 218, 0, 0),
        )

    def test_cli_rejects_repository_override(self) -> None:
        with self.assertRaises(SystemExit) as caught, redirect_stderr(io.StringIO()):
            main(["--repo-root", str(REPO_ROOT)])
        self.assertEqual(caught.exception.code, 2)

    def test_documented_module_cli_passes_without_stderr(self) -> None:
        result = subprocess.run(
            [sys.executable, "-m", "tools.scaf_consumption_selection_validator.validator"],
            cwd=REPO_ROOT,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            check=False,
        )
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertEqual(result.stderr, "")
        self.assertIn("CONSUMPTION SELECTION REPRESENTATION/SOURCE RESULT: PASS", result.stdout)
        self.assertIn("Domain entries (D):          218", result.stdout)
        self.assertIn("Eligible entries (E):        3", result.stdout)
        self.assertIn("Included entries (I):        2", result.stdout)
        self.assertIn("Bounded-omitted entries (O): 1", result.stdout)
        self.assertIn("Predicate-excluded (X):      215", result.stdout)


if __name__ == "__main__":
    unittest.main()
