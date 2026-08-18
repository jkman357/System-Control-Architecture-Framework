from __future__ import annotations

import copy
import hashlib
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock

import yaml

from tools.scaf_effective_project_profile_validator import validator as profile_validator


class EffectiveProjectProfileValidatorTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.repo_root = Path(__file__).resolve().parents[3]
        cls.profile_path = cls.repo_root / "examples/effective-project-profile.yaml"
        cls.project_path = cls.repo_root / "examples/project-application.yaml"
        cls.profile_text = cls.profile_path.read_text(encoding="utf-8")
        cls.project_text = cls.project_path.read_text(encoding="utf-8")
        cls.profile_data = yaml.safe_load(cls.profile_text)
        cls.project_data = yaml.safe_load(cls.project_text)

    def _write_profile(self, directory: Path, data: dict, name: str = "profile.yaml") -> Path:
        path = directory / name
        path.write_text(
            yaml.safe_dump(data, sort_keys=False, allow_unicode=True),
            encoding="utf-8",
        )
        return path

    def _write_project(self, directory: Path, data: dict, name: str = "project.yaml") -> Path:
        path = directory / name
        path.write_text(
            yaml.safe_dump(data, sort_keys=False, allow_unicode=True),
            encoding="utf-8",
        )
        return path

    def _profile_for_project_bytes(self, profile: dict, project_path: Path) -> dict:
        data = copy.deepcopy(profile)
        data["project_application_source_sha256"] = hashlib.sha256(
            project_path.read_bytes()
        ).hexdigest()
        return data

    def _derive_scope_profile(self, scope: str, recorded_authority: str | None = None) -> dict:
        data = copy.deepcopy(self.profile_data)
        data["project_scope_ref"] = scope
        record_by_authority = {
            record["scaf_authority_id"]: record for record in self.project_data["records"]
        }
        entries = []
        for original in data["entries"]:
            authority_id = original["scaf_authority_id"]
            if authority_id == recorded_authority:
                record = record_by_authority[authority_id]
                entries.append(
                    {
                        "scaf_authority_id": authority_id,
                        "profile_state": record["applicability"],
                        "project_application_record_id": record["record_id"],
                    }
                )
            else:
                entries.append(
                    {
                        "scaf_authority_id": authority_id,
                        "profile_state": "no_current_disposition",
                    }
                )
        data["entries"] = entries
        return data

    def _assert_invalid_profile_data(self, mutator) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            tmp_path = Path(tmp)
            data = copy.deepcopy(self.profile_data)
            mutator(data)
            profile_path = self._write_profile(tmp_path, data)
            report = profile_validator.validate_effective_project_profile(
                self.repo_root, profile_path, self.project_path
            )
            self.assertFalse(report.passed, report)

    def test_accepted_fixture_passes(self) -> None:
        report = profile_validator.validate_effective_project_profile(
            self.repo_root, self.profile_path, self.project_path
        )
        self.assertTrue(report.passed, report.errors)
        self.assertEqual(report.entry_count, 218)
        self.assertTrue(report.absence_proof_valid)

    def test_duplicate_raw_yaml_key_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "profile.yaml"
            path.write_text(self.profile_text + '\nprofile_kind: "effective_project_profile"\n', encoding="utf-8")
            report = profile_validator.validate_effective_project_profile(
                self.repo_root, path, self.project_path
            )
            self.assertFalse(report.passed)
            self.assertTrue(any("duplicate key" in error for error in report.errors))

    def test_yaml_anchor_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            text = self.profile_text.replace(
                'project_scope_ref: "example:scope:system"',
                'project_scope_ref: &scope "example:scope:system"',
                1,
            )
            path = Path(tmp) / "profile.yaml"
            path.write_text(text, encoding="utf-8")
            report = profile_validator.validate_effective_project_profile(self.repo_root, path, self.project_path)
            self.assertFalse(report.passed)
            self.assertTrue(any("anchors are prohibited" in error for error in report.errors))

    def test_yaml_alias_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            text = self.profile_text.replace(
                'project_scope_ref: "example:scope:system"',
                'project_scope_ref: &scope "example:scope:system"\nsource_alias: *scope',
                1,
            )
            path = Path(tmp) / "profile.yaml"
            path.write_text(text, encoding="utf-8")
            report = profile_validator.validate_effective_project_profile(self.repo_root, path, self.project_path)
            self.assertFalse(report.passed)
            self.assertTrue(any("aliases are prohibited" in error for error in report.errors))

    def test_yaml_merge_key_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            text = self.profile_text.replace(
                'profile_kind: "effective_project_profile"',
                '<<: {}\nprofile_kind: "effective_project_profile"',
                1,
            )
            path = Path(tmp) / "profile.yaml"
            path.write_text(text, encoding="utf-8")
            report = profile_validator.validate_effective_project_profile(self.repo_root, path, self.project_path)
            self.assertFalse(report.passed)
            self.assertTrue(any("merge keys are prohibited" in error for error in report.errors))

    def test_custom_yaml_tag_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            text = self.profile_text.replace(
                'profile_kind: "effective_project_profile"',
                'profile_kind: !custom "effective_project_profile"',
                1,
            )
            path = Path(tmp) / "profile.yaml"
            path.write_text(text, encoding="utf-8")
            report = profile_validator.validate_effective_project_profile(self.repo_root, path, self.project_path)
            self.assertFalse(report.passed)
            self.assertTrue(any("custom YAML tags" in error for error in report.errors))

    def test_multi_document_yaml_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "profile.yaml"
            path.write_text(self.profile_text + "\n---\n{}\n", encoding="utf-8")
            report = profile_validator.validate_effective_project_profile(self.repo_root, path, self.project_path)
            self.assertFalse(report.passed)
            self.assertTrue(any("exactly one YAML document" in error for error in report.errors))

    def test_non_string_yaml_key_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "profile.yaml"
            path.write_text(self.profile_text + '\n1: "not-allowed"\n', encoding="utf-8")
            report = profile_validator.validate_effective_project_profile(self.repo_root, path, self.project_path)
            self.assertFalse(report.passed)
            self.assertTrue(any("non-string mapping key" in error for error in report.errors))

    def test_schema_invalid_profile_stops_source_checks(self) -> None:
        def mutate(data):
            data["entries"][0]["profile_state"] = "unsupported"
        with tempfile.TemporaryDirectory() as tmp:
            path = self._write_profile(Path(tmp), copy.deepcopy(self.profile_data))
            data = copy.deepcopy(self.profile_data)
            mutate(data)
            path = self._write_profile(Path(tmp), data)
            report = profile_validator.validate_effective_project_profile(self.repo_root, path, self.project_path)
            self.assertFalse(report.passed)
            self.assertFalse(report.schema_valid)
            self.assertFalse(report.authority_registry_valid)

    def test_noncanonical_root_mapping_order_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            data = copy.deepcopy(self.profile_data)
            reordered = {"representation_release": data["representation_release"]}
            for key, value in data.items():
                if key != "representation_release":
                    reordered[key] = value
            path = self._write_profile(Path(tmp), reordered)
            report = profile_validator.validate_effective_project_profile(self.repo_root, path, self.project_path)
            self.assertFalse(report.passed)
            self.assertTrue(any("profile root: non-canonical mapping order" in e for e in report.errors))

    def test_noncanonical_entry_mapping_order_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            data = copy.deepcopy(self.profile_data)
            first = data["entries"][0]
            data["entries"][0] = {
                "profile_state": first["profile_state"],
                "scaf_authority_id": first["scaf_authority_id"],
                "project_application_record_id": first["project_application_record_id"],
            }
            path = self._write_profile(Path(tmp), data)
            report = profile_validator.validate_effective_project_profile(self.repo_root, path, self.project_path)
            self.assertFalse(report.passed)
            self.assertTrue(any("non-canonical mapping order" in e for e in report.errors))

    def test_noncanonical_entry_list_order_is_rejected(self) -> None:
        self._assert_invalid_profile_data(
            lambda data: data["entries"].__setitem__(slice(0, 2), [data["entries"][1], data["entries"][0]])
        )

    def test_missing_pao_entry_is_rejected(self) -> None:
        self._assert_invalid_profile_data(lambda data: data["entries"].pop())

    def test_duplicate_authority_id_nonidentical_entries_is_rejected(self) -> None:
        def mutate(data):
            data["entries"][1]["scaf_authority_id"] = data["entries"][0]["scaf_authority_id"]
        self._assert_invalid_profile_data(mutate)

    def test_fni_entry_is_rejected(self) -> None:
        self._assert_invalid_profile_data(
            lambda data: data["entries"][-1].__setitem__("scaf_authority_id", "SCAF-AK-009")
        )

    def test_unknown_authority_entry_is_rejected(self) -> None:
        self._assert_invalid_profile_data(
            lambda data: data["entries"][-1].__setitem__("scaf_authority_id", "SCAF-AK-999")
        )

    def test_wrong_source_release_is_rejected(self) -> None:
        self._assert_invalid_profile_data(
            lambda data: data.__setitem__("scaf_source_release", "v0.0.999")
        )

    def test_wrong_project_application_sha_is_rejected(self) -> None:
        self._assert_invalid_profile_data(
            lambda data: data.__setitem__("project_application_source_sha256", "0" * 64)
        )

    def test_invalid_project_application_snapshot_is_rejected_after_digest_match(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            tmp_path = Path(tmp)
            project = copy.deepcopy(self.project_data)
            project["records"][0]["applicability"] = "no_current_disposition"
            project_path = self._write_project(tmp_path, project)
            profile = self._profile_for_project_bytes(self.profile_data, project_path)
            profile_path = self._write_profile(tmp_path, profile)
            report = profile_validator.validate_effective_project_profile(
                self.repo_root, profile_path, project_path
            )
            self.assertFalse(report.passed)
            self.assertTrue(report.source_digest_valid)
            self.assertFalse(report.project_application_valid)

    def test_recorded_entry_unknown_record_id_is_rejected(self) -> None:
        self._assert_invalid_profile_data(
            lambda data: data["entries"][0].__setitem__(
                "project_application_record_id", "EXAMPLE-PA-DOES-NOT-EXIST"
            )
        )

    def test_recorded_entry_wrong_authority_record_is_rejected(self) -> None:
        self._assert_invalid_profile_data(
            lambda data: data["entries"][0].__setitem__(
                "project_application_record_id", "EXAMPLE-PA-002"
            )
        )

    def test_recorded_entry_wrong_scope_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            tmp_path = Path(tmp)
            project = copy.deepcopy(self.project_data)
            project["records"][0]["project_scope_ref"] = "example:scope:other"
            project_path = self._write_project(tmp_path, project)
            profile = self._profile_for_project_bytes(self.profile_data, project_path)
            profile_path = self._write_profile(tmp_path, profile)
            report = profile_validator.validate_effective_project_profile(
                self.repo_root, profile_path, project_path
            )
            self.assertFalse(report.passed)
            self.assertTrue(report.project_application_valid)
            self.assertTrue(any("does not match profile scope" in e for e in report.errors))

    def test_recorded_entry_state_mismatch_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            tmp_path = Path(tmp)
            project = copy.deepcopy(self.project_data)
            project["records"][0]["applicability"] = "not_applicable"
            project_path = self._write_project(tmp_path, project)
            profile = self._profile_for_project_bytes(self.profile_data, project_path)
            profile_path = self._write_profile(tmp_path, profile)
            report = profile_validator.validate_effective_project_profile(
                self.repo_root, profile_path, project_path
            )
            self.assertFalse(report.passed)
            self.assertTrue(report.project_application_valid)
            self.assertTrue(any("does not match Project Application" in e for e in report.errors))

    def test_absence_is_rejected_when_exact_pair_record_exists(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            tmp_path = Path(tmp)
            project = copy.deepcopy(self.project_data)
            project["records"][1]["project_scope_ref"] = "example:scope:system"
            project_path = self._write_project(tmp_path, project)
            profile = self._profile_for_project_bytes(self.profile_data, project_path)
            profile_path = self._write_profile(tmp_path, profile)
            report = profile_validator.validate_effective_project_profile(
                self.repo_root, profile_path, project_path
            )
            self.assertFalse(report.passed)
            self.assertTrue(report.project_application_valid)
            self.assertFalse(report.absence_proof_valid)
            self.assertTrue(any("no_current_disposition is contradicted" in e for e in report.errors))

    def test_valid_not_applicable_scope_profile_passes(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            profile = self._derive_scope_profile("example:scope:stateless-node", "SCAF-AK-002")
            path = self._write_profile(Path(tmp), profile)
            report = profile_validator.validate_effective_project_profile(self.repo_root, path, self.project_path)
            self.assertTrue(report.passed, report.errors)

    def test_valid_undetermined_scope_profile_passes(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            profile = self._derive_scope_profile("example:scope:interface-if3", "SCAF-AK-003")
            path = self._write_profile(Path(tmp), profile)
            report = profile_validator.validate_effective_project_profile(self.repo_root, path, self.project_path)
            self.assertTrue(report.passed, report.errors)

    def test_unmatched_scope_all_absence_profile_passes(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            profile = self._derive_scope_profile("example:scope:no-current-record", None)
            path = self._write_profile(Path(tmp), profile)
            report = profile_validator.validate_effective_project_profile(self.repo_root, path, self.project_path)
            self.assertTrue(report.passed, report.errors)
            self.assertTrue(report.absence_proof_valid)

    def test_selected_project_application_is_consumed_from_same_snapshot(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            tmp_path = Path(tmp)
            selected_project = tmp_path / "selected-project.yaml"
            selected_project.write_bytes(self.project_path.read_bytes())
            profile = self._profile_for_project_bytes(self.profile_data, selected_project)
            selected_profile = self._write_profile(tmp_path, profile)
            original_validate = profile_validator.validate_project_application

            def wrapped(repo_root, snapshot_path):
                result = original_validate(repo_root, snapshot_path)
                selected_project.write_text("records: []\n", encoding="utf-8")
                return result

            with mock.patch.object(
                profile_validator, "validate_project_application", side_effect=wrapped
            ):
                report = profile_validator.validate_effective_project_profile(
                    self.repo_root, selected_profile, selected_project
                )
            self.assertTrue(report.passed, report.errors)

    def test_cli_rejects_repository_override(self) -> None:
        with self.assertRaises(SystemExit):
            profile_validator._build_parser().parse_args(["--repo-root", "/tmp"])

    def test_documented_module_cli_passes_without_stderr(self) -> None:
        completed = subprocess.run(
            [sys.executable, "-m", "tools.scaf_effective_project_profile_validator.validator"],
            cwd=self.repo_root,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            check=False,
        )
        self.assertEqual(completed.returncode, 0, completed.stderr)
        self.assertEqual(completed.stderr, "")
        self.assertIn("PROFILE REPRESENTATION/SOURCE RESULT: PASS", completed.stdout)


if __name__ == "__main__":
    unittest.main()
