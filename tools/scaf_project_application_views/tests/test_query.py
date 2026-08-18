from __future__ import annotations

import copy
import inspect
import io
import json
import shutil
import tempfile
import unittest
from contextlib import redirect_stderr, redirect_stdout
from pathlib import Path

import yaml

import tools.scaf_project_application_views as view_package
from tools.scaf_project_application_views import (
    ProjectApplicationViewError,
    query_authority,
    query_record,
    query_scope,
)
from tools.scaf_project_application_views.query import (
    _ValidatedProjectApplicationContext,
    _render_json,
    main,
)


REPO_ROOT = Path(__file__).resolve().parents[3]


class ProjectApplicationViewTests(unittest.TestCase):
    def make_repo(self) -> tuple[tempfile.TemporaryDirectory, Path]:
        temp = tempfile.TemporaryDirectory()
        root = Path(temp.name)
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
        return temp, root

    def read_fixture(self, root: Path) -> dict:
        return yaml.safe_load((root / "examples/project-application.yaml").read_text(encoding="utf-8"))

    def write_fixture(self, root: Path, data: dict) -> None:
        (root / "examples/project-application.yaml").write_text(
            yaml.safe_dump(data, sort_keys=False), encoding="utf-8"
        )

    def test_package_exports_only_validation_owning_query_api(self):
        self.assertEqual(
            set(view_package.__all__),
            {"ProjectApplicationViewError", "query_record", "query_authority", "query_scope"},
        )

    def test_mapping_member_reordering_does_not_change_json_projection(self):
        baseline = _render_json(query_record(REPO_ROOT, "EXAMPLE-PA-001"))
        temp, root = self.make_repo()
        self.addCleanup(temp.cleanup)
        data = self.read_fixture(root)
        reordered_records = []
        for record in data["records"]:
            reordered = {key: record[key] for key in reversed(tuple(record.keys()))}
            basis = reordered["disposition_basis"]
            reordered["disposition_basis"] = {
                key: basis[key] for key in reversed(tuple(basis.keys()))
            }
            reordered_records.append(reordered)
        self.write_fixture(root, {"records": reordered_records})
        observed = _render_json(query_record(root, "EXAMPLE-PA-001"))
        self.assertEqual(observed, baseline)

    def test_query_record_returns_exact_validated_record(self):
        view = query_record(REPO_ROOT, "EXAMPLE-PA-001")
        self.assertEqual(view["query_kind"], "record")
        self.assertEqual(view["record_count"], 1)
        self.assertEqual(view["records"][0]["record_id"], "EXAMPLE-PA-001")
        self.assertEqual(view["applicability_counts"]["applicable"], 1)

    def test_unknown_record_id_fails(self):
        with self.assertRaises(ProjectApplicationViewError):
            query_record(REPO_ROOT, "EXAMPLE-PA-999")

    def test_empty_query_identity_fails(self):
        with self.assertRaises(ProjectApplicationViewError):
            query_record(REPO_ROOT, "")
        with self.assertRaises(ProjectApplicationViewError):
            query_authority(REPO_ROOT, "")
        with self.assertRaises(ProjectApplicationViewError):
            query_scope(REPO_ROOT, "")

    def test_query_authority_returns_validated_records(self):
        view = query_authority(REPO_ROOT, "SCAF-AK-001")
        self.assertEqual(view["query_kind"], "authority")
        self.assertEqual(view["record_count"], 1)
        self.assertEqual(view["records"][0]["project_scope_ref"], "example:scope:system")

    def test_known_authority_without_current_record_returns_zero_view(self):
        authority = yaml.safe_load((REPO_ROOT / "authority-registry.yaml").read_text(encoding="utf-8"))
        used = {"SCAF-AK-001", "SCAF-AK-002", "SCAF-AK-003"}
        known = next(
            record["id"]
            for record in authority["records"]
            if record.get("authority_class") == "Project-Applicable Obligation"
            and record["id"] not in used
        )
        view = query_authority(REPO_ROOT, known)
        self.assertEqual(view["record_count"], 0)
        self.assertEqual(sum(view["applicability_counts"].values()), 0)

    def test_unknown_authority_query_fails(self):
        with self.assertRaises(ProjectApplicationViewError):
            query_authority(REPO_ROOT, "SCAF-DOES-NOT-EXIST")

    def test_framework_normative_invariant_authority_query_fails(self):
        authority = yaml.safe_load((REPO_ROOT / "authority-registry.yaml").read_text(encoding="utf-8"))
        fni = next(
            record["id"]
            for record in authority["records"]
            if record.get("authority_class") == "Framework Normative Invariant"
        )
        with self.assertRaises(ProjectApplicationViewError):
            query_authority(REPO_ROOT, fni)

    def test_query_scope_returns_exact_string_matches(self):
        view = query_scope(REPO_ROOT, "example:scope:system")
        self.assertEqual(view["query_kind"], "scope")
        self.assertEqual(view["record_count"], 1)
        self.assertEqual(view["scope_resolution"], "not_performed")
        self.assertEqual(view["records"][0]["record_id"], "EXAMPLE-PA-001")

    def test_unknown_scope_string_returns_resolution_neutral_zero_view(self):
        view = query_scope(REPO_ROOT, "example:scope:not-recorded")
        self.assertEqual(view["record_count"], 0)
        self.assertEqual(view["scope_resolution"], "not_performed")

    def test_custom_project_application_path_is_validated_and_queried(self):
        temp, root = self.make_repo()
        self.addCleanup(temp.cleanup)
        custom = root / "project" / "application.yaml"
        custom.parent.mkdir(parents=True, exist_ok=True)
        custom.write_bytes((root / "examples/project-application.yaml").read_bytes())
        view = query_record(root, "EXAMPLE-PA-002", custom)
        self.assertEqual(view["records"][0]["applicability"], "not_applicable")

    def test_schema_invalid_selected_input_returns_no_view(self):
        temp, root = self.make_repo()
        self.addCleanup(temp.cleanup)
        data = self.read_fixture(root)
        data["records"][0]["applicability"] = "maybe"
        self.write_fixture(root, data)
        with self.assertRaises(ProjectApplicationViewError):
            query_scope(root, "example:scope:system")

    def test_order_invalid_selected_input_returns_no_view(self):
        temp, root = self.make_repo()
        self.addCleanup(temp.cleanup)
        data = self.read_fixture(root)
        data["records"][0]["decision_refs"] = list(reversed(data["records"][0]["decision_refs"]))
        self.write_fixture(root, data)
        with self.assertRaises(ProjectApplicationViewError):
            query_record(root, "EXAMPLE-PA-001")

    def test_authority_proof_failure_returns_no_view(self):
        temp, root = self.make_repo()
        self.addCleanup(temp.cleanup)
        registry_path = root / "authority-registry.yaml"
        registry = yaml.safe_load(registry_path.read_text(encoding="utf-8"))
        registry["records"][0]["source_anchor"] = "broken-source-anchor"
        registry_path.write_text(yaml.safe_dump(registry, sort_keys=False), encoding="utf-8")
        with self.assertRaises(ProjectApplicationViewError):
            query_record(root, "EXAMPLE-PA-001")

    def test_public_query_signatures_do_not_accept_preparsed_context(self):
        for function in (query_record, query_authority, query_scope):
            parameters = tuple(inspect.signature(function).parameters)
            self.assertEqual(
                parameters,
                (
                    "repo_root",
                    {
                        query_record: "record_id",
                        query_authority: "scaf_authority_id",
                        query_scope: "project_scope_ref",
                    }[function],
                    "project_application_path",
                ),
            )

    def test_internal_context_cannot_be_constructed_by_supported_caller(self):
        with self.assertRaises(ProjectApplicationViewError):
            _ValidatedProjectApplicationContext(tuple(), object())

    def test_view_output_is_copy_not_live_context_state(self):
        view1 = query_record(REPO_ROOT, "EXAMPLE-PA-001")
        view1["records"][0]["record_id"] = "CHANGED"
        view2 = query_record(REPO_ROOT, "EXAMPLE-PA-001")
        self.assertEqual(view2["records"][0]["record_id"], "EXAMPLE-PA-001")

    def test_json_render_is_deterministic(self):
        view = query_scope(REPO_ROOT, "example:scope:system")
        self.assertEqual(_render_json(view), _render_json(copy.deepcopy(view)))
        parsed = json.loads(_render_json(view))
        self.assertEqual(parsed, view)

    def test_cli_record_json_uses_same_public_query_path(self):
        stdout = io.StringIO()
        stderr = io.StringIO()
        with redirect_stdout(stdout), redirect_stderr(stderr):
            result = main(["--record", "EXAMPLE-PA-001", "--format", "json"])
        self.assertEqual(result, 0)
        self.assertEqual(stderr.getvalue(), "")
        payload = json.loads(stdout.getvalue())
        self.assertEqual(payload["query_kind"], "record")
        self.assertEqual(payload["records"][0]["record_id"], "EXAMPLE-PA-001")

    def test_cli_scope_text_marks_scope_resolution_not_performed(self):
        stdout = io.StringIO()
        stderr = io.StringIO()
        with redirect_stdout(stdout), redirect_stderr(stderr):
            result = main(["--scope", "example:scope:not-recorded"])
        self.assertEqual(result, 0)
        self.assertEqual(stderr.getvalue(), "")
        self.assertIn("Scope resolution: not_performed", stdout.getvalue())
        self.assertIn("Records: 0", stdout.getvalue())

    def test_cli_invalid_input_fails_without_view_payload(self):
        temp, root = self.make_repo()
        self.addCleanup(temp.cleanup)
        invalid = root / "invalid.yaml"
        data = self.read_fixture(root)
        data["records"][0]["applicability"] = "invalid"
        invalid.write_text(yaml.safe_dump(data, sort_keys=False), encoding="utf-8")

        # main() is repository-bound to the real repo, but the selected external
        # Project Application path still passes through the rc07 validator.
        stdout = io.StringIO()
        stderr = io.StringIO()
        with redirect_stdout(stdout), redirect_stderr(stderr):
            result = main([
                "--project-application",
                str(invalid),
                "--record",
                "EXAMPLE-PA-001",
                "--format",
                "json",
            ])
        self.assertEqual(result, 1)
        self.assertEqual(stdout.getvalue(), "")
        self.assertIn("RESULT: FAIL", stderr.getvalue())
        self.assertNotIn("project_application_view_version", stderr.getvalue())


if __name__ == "__main__":
    unittest.main()
