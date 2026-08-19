from __future__ import annotations

import contextlib
import io
import json
import tempfile
import unittest
from pathlib import Path
from unittest import mock

import yaml

from tools.scaf_consumption_selection_builder.builder import (
    AUTHORITY_MODE_ALL_DOMAIN,
    AUTHORITY_MODE_EXPLICIT_SET,
    ConsumptionSelectionBuildError,
    build_consumption_selection,
    main,
)
from tools.scaf_consumption_selection_validator.validator import (
    StrictConsumptionSelectionLoader,
    validate_consumption_selection,
)


REPO_ROOT = Path(__file__).resolve().parents[3]
PURPOSE = "Illustrative bounded context-selection example over three exact PAO identities."
OMISSION_BASIS = (
    "Illustrative entry-count bound includes two of three predicate-eligible entries."
)


def _parse(data: bytes):
    return yaml.load(data.decode("utf-8"), Loader=StrictConsumptionSelectionLoader)


class ConsumptionSelectionBuilderTests(unittest.TestCase):
    def test_fixture_equivalent_build_is_byte_identical_after_comments(self):
        generated = build_consumption_selection(
            REPO_ROOT,
            PURPOSE,
            ["no_current_disposition", "applicable"],
            authority_mode=AUTHORITY_MODE_EXPLICIT_SET,
            authority_ids=["SCAF-AK-003", "SCAF-AK-001", "SCAF-AK-002"],
            omitted_authority_ids=["SCAF-AK-003"],
            omission_basis=OMISSION_BASIS,
        )
        fixture = (REPO_ROOT / "examples/consumption-selection.yaml").read_text(
            encoding="utf-8"
        )
        lines = fixture.splitlines(keepends=True)
        while lines and (lines[0].lstrip().startswith("#") or lines[0].strip() == ""):
            lines.pop(0)
        self.assertEqual(generated, "".join(lines).encode("utf-8"))

    def test_fixture_equivalent_build_self_validates(self):
        generated = build_consumption_selection(
            REPO_ROOT,
            PURPOSE,
            ["applicable", "no_current_disposition"],
            authority_mode=AUTHORITY_MODE_EXPLICIT_SET,
            authority_ids=["SCAF-AK-001", "SCAF-AK-002", "SCAF-AK-003"],
            omitted_authority_ids=["SCAF-AK-003"],
            omission_basis=OMISSION_BASIS,
        )
        with tempfile.TemporaryDirectory() as temp_dir:
            selection_path = Path(temp_dir) / "selection.yaml"
            selection_path.write_bytes(generated)
            report = validate_consumption_selection(REPO_ROOT, selection_path)
        self.assertTrue(report.passed, report.errors)
        self.assertEqual(
            (report.domain_count, report.eligible_count, report.included_count,
             report.omitted_count, report.excluded_count),
            (218, 3, 2, 1, 215),
        )

    def test_state_selector_is_canonicalized(self):
        data = _parse(
            build_consumption_selection(
                REPO_ROOT,
                "purpose",
                ["no_current_disposition", "applicable", "undetermined"],
            )
        )
        self.assertEqual(
            data["state_selector"],
            ["applicable", "undetermined", "no_current_disposition"],
        )

    def test_explicit_authority_ids_are_canonicalized(self):
        data = _parse(
            build_consumption_selection(
                REPO_ROOT,
                "purpose",
                ["applicable", "no_current_disposition"],
                authority_mode=AUTHORITY_MODE_EXPLICIT_SET,
                authority_ids=["SCAF-AK-003", "SCAF-AK-001", "SCAF-AK-002"],
            )
        )
        self.assertEqual(
            data["authority_selector"]["scaf_authority_ids"],
            ["SCAF-AK-001", "SCAF-AK-002", "SCAF-AK-003"],
        )

    def test_empty_state_selector_is_valid_zero_eligible(self):
        data = _parse(build_consumption_selection(REPO_ROOT, "purpose", []))
        self.assertEqual(data["state_selector"], [])
        self.assertEqual(data["selected_entries"], [])
        self.assertEqual(data["selection_class"], "filtered")

    def test_empty_explicit_authority_set_is_valid_zero_eligible(self):
        data = _parse(
            build_consumption_selection(
                REPO_ROOT,
                "purpose",
                ["applicable"],
                authority_mode=AUTHORITY_MODE_EXPLICIT_SET,
                authority_ids=[],
            )
        )
        self.assertEqual(data["authority_selector"]["scaf_authority_ids"], [])
        self.assertEqual(data["selected_entries"], [])

    def test_all_four_states_all_domain_builds_complete_selection(self):
        data = _parse(
            build_consumption_selection(
                REPO_ROOT,
                "purpose",
                [
                    "applicable",
                    "not_applicable",
                    "undetermined",
                    "no_current_disposition",
                ],
            )
        )
        self.assertEqual(data["selection_class"], "complete")
        self.assertEqual(len(data["selected_entries"]), 218)

    def test_applicable_only_all_domain_is_filtered(self):
        data = _parse(
            build_consumption_selection(REPO_ROOT, "purpose", ["applicable"])
        )
        self.assertEqual(data["selection_class"], "filtered")
        self.assertEqual(len(data["selected_entries"]), 1)
        self.assertEqual(data["selected_entries"][0]["scaf_authority_id"], "SCAF-AK-001")

    def test_no_omission_serializes_applied_false(self):
        data = _parse(
            build_consumption_selection(REPO_ROOT, "purpose", ["applicable"])
        )
        self.assertEqual(data["bounded_omission"], {"applied": False})

    def test_applied_omission_can_have_empty_omitted_set(self):
        data = _parse(
            build_consumption_selection(
                REPO_ROOT,
                "purpose",
                ["applicable"],
                omission_basis="descriptive bound",
            )
        )
        self.assertEqual(
            data["bounded_omission"],
            {"applied": True, "basis": "descriptive bound"},
        )
        self.assertEqual(len(data["selected_entries"]), 1)

    def test_exact_omission_removes_only_named_eligible_id(self):
        data = _parse(
            build_consumption_selection(
                REPO_ROOT,
                "purpose",
                ["applicable", "no_current_disposition"],
                authority_mode=AUTHORITY_MODE_EXPLICIT_SET,
                authority_ids=["SCAF-AK-001", "SCAF-AK-002"],
                omitted_authority_ids=["SCAF-AK-002"],
                omission_basis="bounded omission",
            )
        )
        self.assertEqual(
            [entry["scaf_authority_id"] for entry in data["selected_entries"]],
            ["SCAF-AK-001"],
        )

    def test_selected_entries_preserve_record_id_fidelity(self):
        data = _parse(
            build_consumption_selection(REPO_ROOT, "purpose", ["applicable"])
        )
        self.assertEqual(
            data["selected_entries"][0]["project_application_record_id"],
            "EXAMPLE-PA-001",
        )

    def test_absence_selected_entry_omits_record_id(self):
        data = _parse(
            build_consumption_selection(
                REPO_ROOT,
                "purpose",
                ["no_current_disposition"],
                authority_mode=AUTHORITY_MODE_EXPLICIT_SET,
                authority_ids=["SCAF-AK-002"],
            )
        )
        self.assertNotIn("project_application_record_id", data["selected_entries"][0])

    def test_source_binding_profile_sha_matches_exact_bytes(self):
        import hashlib
        data = _parse(build_consumption_selection(REPO_ROOT, "purpose", []))
        expected = hashlib.sha256(
            (REPO_ROOT / "examples/effective-project-profile.yaml").read_bytes()
        ).hexdigest()
        self.assertEqual(
            data["source_profile_binding"]["effective_project_profile_source_sha256"],
            expected,
        )

    def test_invalid_profile_is_rejected_before_build(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            profile_path = Path(temp_dir) / "profile.yaml"
            profile_path.write_text("profile_kind: bad\n", encoding="utf-8")
            with self.assertRaisesRegex(
                ConsumptionSelectionBuildError, "failed frozen v0.0.6 source-aware validation"
            ):
                build_consumption_selection(
                    REPO_ROOT, "purpose", [], profile_path=profile_path
                )

    def test_empty_purpose_rejected(self):
        with self.assertRaisesRegex(ConsumptionSelectionBuildError, "selection_purpose"):
            build_consumption_selection(REPO_ROOT, "", [])

    def test_non_string_purpose_rejected(self):
        with self.assertRaises(ConsumptionSelectionBuildError):
            build_consumption_selection(REPO_ROOT, 1, [])  # type: ignore[arg-type]

    def test_unknown_state_rejected(self):
        with self.assertRaisesRegex(ConsumptionSelectionBuildError, "unsupported state"):
            build_consumption_selection(REPO_ROOT, "purpose", ["unknown"])

    def test_duplicate_state_rejected(self):
        with self.assertRaisesRegex(ConsumptionSelectionBuildError, "duplicate"):
            build_consumption_selection(
                REPO_ROOT, "purpose", ["applicable", "applicable"]
            )

    def test_state_selector_single_string_rejected(self):
        with self.assertRaisesRegex(ConsumptionSelectionBuildError, "sequence"):
            build_consumption_selection(
                REPO_ROOT, "purpose", "applicable"  # type: ignore[arg-type]
            )

    def test_invalid_authority_mode_rejected(self):
        with self.assertRaisesRegex(ConsumptionSelectionBuildError, "authority_mode"):
            build_consumption_selection(
                REPO_ROOT, "purpose", [], authority_mode="invalid"
            )

    def test_all_domain_rejects_authority_ids(self):
        with self.assertRaisesRegex(ConsumptionSelectionBuildError, "all_domain"):
            build_consumption_selection(
                REPO_ROOT, "purpose", [], authority_ids=["SCAF-AK-001"]
            )

    def test_unknown_explicit_authority_rejected(self):
        with self.assertRaisesRegex(ConsumptionSelectionBuildError, "outside"):
            build_consumption_selection(
                REPO_ROOT,
                "purpose",
                ["applicable"],
                authority_mode=AUTHORITY_MODE_EXPLICIT_SET,
                authority_ids=["SCAF-UNKNOWN-999"],
            )

    def test_duplicate_authority_id_rejected(self):
        with self.assertRaisesRegex(ConsumptionSelectionBuildError, "duplicate"):
            build_consumption_selection(
                REPO_ROOT,
                "purpose",
                ["applicable"],
                authority_mode=AUTHORITY_MODE_EXPLICIT_SET,
                authority_ids=["SCAF-AK-001", "SCAF-AK-001"],
            )

    def test_empty_authority_id_rejected(self):
        with self.assertRaisesRegex(ConsumptionSelectionBuildError, "non-empty"):
            build_consumption_selection(
                REPO_ROOT,
                "purpose",
                [],
                authority_mode=AUTHORITY_MODE_EXPLICIT_SET,
                authority_ids=[""],
            )

    def test_omitted_id_requires_basis(self):
        with self.assertRaisesRegex(ConsumptionSelectionBuildError, "omission_basis"):
            build_consumption_selection(
                REPO_ROOT,
                "purpose",
                ["applicable"],
                omitted_authority_ids=["SCAF-AK-001"],
            )

    def test_empty_omission_basis_rejected(self):
        with self.assertRaisesRegex(ConsumptionSelectionBuildError, "omission_basis"):
            build_consumption_selection(
                REPO_ROOT, "purpose", ["applicable"], omission_basis=""
            )

    def test_unknown_omitted_authority_rejected(self):
        with self.assertRaisesRegex(ConsumptionSelectionBuildError, "outside"):
            build_consumption_selection(
                REPO_ROOT,
                "purpose",
                ["applicable"],
                omitted_authority_ids=["SCAF-UNKNOWN-999"],
                omission_basis="bounded",
            )

    def test_ineligible_omitted_authority_rejected(self):
        with self.assertRaisesRegex(ConsumptionSelectionBuildError, "predicate-eligible"):
            build_consumption_selection(
                REPO_ROOT,
                "purpose",
                ["applicable"],
                omitted_authority_ids=["SCAF-AK-002"],
                omission_basis="bounded",
            )

    def test_duplicate_omitted_authority_rejected(self):
        with self.assertRaisesRegex(ConsumptionSelectionBuildError, "duplicate"):
            build_consumption_selection(
                REPO_ROOT,
                "purpose",
                ["applicable"],
                omitted_authority_ids=["SCAF-AK-001", "SCAF-AK-001"],
                omission_basis="bounded",
            )

    def test_builder_self_validation_failure_blocks_return(self):
        failed_report = mock.Mock(passed=False, errors=["forced self-validation failure"])
        with mock.patch(
            "tools.scaf_consumption_selection_builder.builder.validate_consumption_selection",
            return_value=failed_report,
        ):
            with self.assertRaisesRegex(
                ConsumptionSelectionBuildError, "failed accepted rc05"
            ):
                build_consumption_selection(REPO_ROOT, "purpose", [])

    def test_cli_success_stdout_is_yaml_only(self):
        stdout = io.BytesIO()
        stderr = io.StringIO()
        fake_stdout = io.TextIOWrapper(stdout, encoding="utf-8", write_through=True)
        with mock.patch("sys.stdout", fake_stdout), contextlib.redirect_stderr(stderr):
            result = main(["--purpose", "purpose", "--state", "applicable"])
            fake_stdout.flush()
        self.assertEqual(result, 0)
        output = stdout.getvalue().decode("utf-8")
        self.assertTrue(output.startswith('selection_kind: "consumption_selection"\n'))
        self.assertNotIn("PASS", output)
        self.assertEqual(stderr.getvalue(), "")

    def test_cli_invalid_input_returns_one_and_fail_label(self):
        stderr = io.StringIO()
        with contextlib.redirect_stderr(stderr):
            result = main(["--purpose", "purpose", "--state", "unknown"])
        self.assertEqual(result, 1)
        self.assertIn("CONSUMPTION SELECTION BUILD RESULT: FAIL", stderr.getvalue())

    def test_no_ranking_or_context_content_fields_serialized(self):
        data = _parse(build_consumption_selection(REPO_ROOT, "purpose", ["applicable"]))
        serialized = json.dumps(data)
        for forbidden in (
            "priority",
            "severity",
            "rank",
            "context_source",
            "pattern_selection",
            "compliance",
            "verification",
            "closure",
        ):
            self.assertNotIn(forbidden, serialized)


if __name__ == "__main__":
    unittest.main()
