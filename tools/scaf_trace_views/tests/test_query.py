from __future__ import annotations

import copy
import io
import json
import tempfile
import unittest
from contextlib import redirect_stderr, redirect_stdout
from pathlib import Path
from unittest.mock import patch

import yaml

import tools.scaf_trace_views as trace_views_package
import tools.scaf_trace_views.query as query_module
from tools.scaf_trace_validator.validator import UniqueKeyLoader
from tools.scaf_trace_views.query import (
    RELATION_FIELDS,
    TraceViewError,
    _ValidatedTraceContext,
    _build_l2_view,
    _build_pattern_view,
    _load_validated_context,
    _render_json,
    main,
    query_l2,
    query_pattern,
)


REPO_ROOT = Path(__file__).resolve().parents[3]


class TraceViewTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.context = _load_validated_context(REPO_ROOT)

    def make_repo(self) -> Path:
        temp = tempfile.TemporaryDirectory()
        self.addCleanup(temp.cleanup)
        root = Path(temp.name) / "repo"
        root.mkdir()
        for relative in [
            "l3-trace-registry.yaml",
            "authority-registry.yaml",
            "schemas/l3-trace-registry.schema.json",
        ]:
            source = REPO_ROOT / relative
            target = root / relative
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(source.read_bytes())
        for source in (REPO_ROOT / "docs/l3/catalog").glob("*/SCAF-PAT-*.md"):
            relative = source.relative_to(REPO_ROOT)
            target = root / relative
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(source.read_bytes())
        return root

    def test_l2_view_returns_typed_relation_and_qualifier(self):
        view = _build_l2_view(self.context, "SCAF-ROB-004")
        self.assertEqual("l2_to_l3", view["direction"])
        self.assertGreaterEqual(view["relation_count"], 1)
        match = next(r for r in view["relations"] if r["pattern_id"] == "SCAF-PAT-TIM-002")
        self.assertEqual("constraint_input", match["relation_type"])
        self.assertEqual("applicable", match["qualifier"])

    def test_pattern_view_preserves_multi_type_pairs(self):
        view = _build_pattern_view(self.context, "SCAF-PAT-COM-001")
        int010 = [r["relation_type"] for r in view["relations"] if r["l2_id"] == "SCAF-INT-010"]
        self.assertEqual(["primary_realization_candidate", "constraint_input"], int010)
        cfg019 = [r["relation_type"] for r in view["relations"] if r["l2_id"] == "SCAF-CFG-019"]
        self.assertEqual(["supporting_realization", "constraint_input"], cfg019)

    def test_known_untraced_authority_returns_zero_relation_view(self):
        view = _build_l2_view(self.context, "SCAF-AK-001")
        self.assertEqual(0, view["relation_count"])
        self.assertEqual([], view["relations"])

    def test_unknown_authority_fails_closed(self):
        with self.assertRaises(TraceViewError):
            _build_l2_view(self.context, "SCAF-INT-999")

    def test_framework_invariant_is_outside_l2_trace_query_domain(self):
        with self.assertRaises(TraceViewError):
            _build_l2_view(self.context, "SCAF-AK-009")

    def test_unknown_pattern_fails_closed(self):
        with self.assertRaises(TraceViewError):
            _build_pattern_view(self.context, "SCAF-PAT-XYZ-999")

    def test_l2_view_order_is_relation_type_then_pattern(self):
        target = next(
            l2_id
            for l2_id in sorted({r["l2_id"] for r in self.context.relations})
            if sum(1 for r in self.context.relations if r["l2_id"] == l2_id) >= 2
        )
        view = _build_l2_view(self.context, target)
        order = {"primary_realization_candidate": 0, "supporting_realization": 1, "constraint_input": 2}
        keys = [(order[r["relation_type"]], r["pattern_id"]) for r in view["relations"]]
        self.assertEqual(sorted(keys), keys)

    def test_pattern_view_order_is_relation_type_then_l2(self):
        view = _build_pattern_view(self.context, "SCAF-PAT-COM-001")
        order = {"primary_realization_candidate": 0, "supporting_realization": 1, "constraint_input": 2}
        keys = [(order[r["relation_type"]], r["l2_id"]) for r in view["relations"]]
        self.assertEqual(sorted(keys), keys)

    def test_relation_records_preserve_exact_seven_fields(self):
        view = _build_pattern_view(self.context, "SCAF-PAT-COM-001")
        for relation in view["relations"]:
            self.assertEqual(list(RELATION_FIELDS), list(relation.keys()))

    def test_all_pattern_views_cover_registry_exactly_once(self):
        projected = []
        for pattern_id in sorted(self.context.pattern_ids):
            projected.extend(_build_pattern_view(self.context, pattern_id)["relations"])
        self.assertEqual(len(self.context.relations), len(projected))
        self.assertEqual(
            sorted(self.context.relations, key=lambda r: (r["pattern_id"], r["relation_type"], r["l2_id"])),
            sorted(projected, key=lambda r: (r["pattern_id"], r["relation_type"], r["l2_id"])),
        )

    def test_all_l2_views_cover_registry_exactly_once(self):
        projected = []
        for l2_id in sorted(self.context.authority_ids):
            projected.extend(_build_l2_view(self.context, l2_id)["relations"])
        self.assertEqual(len(self.context.relations), len(projected))
        self.assertEqual(
            sorted(self.context.relations, key=lambda r: (r["pattern_id"], r["relation_type"], r["l2_id"])),
            sorted(projected, key=lambda r: (r["pattern_id"], r["relation_type"], r["l2_id"])),
        )

    def test_view_payload_has_no_project_decision_state(self):
        view = _build_l2_view(self.context, "SCAF-ROB-004")
        self.assertEqual(
            {"trace_view_version", "direction", "query_id", "relation_count", "relations"},
            set(view),
        )
        forbidden = {"recommended", "selected", "satisfied", "compliant", "verified", "closed"}
        self.assertTrue(forbidden.isdisjoint(view.keys()))
        for relation in view["relations"]:
            self.assertTrue(forbidden.isdisjoint(relation.keys()))

    def test_json_rendering_is_byte_deterministic(self):
        view = _build_pattern_view(self.context, "SCAF-PAT-REC-001")
        self.assertEqual(_render_json(view), _render_json(copy.deepcopy(view)))

    def test_invalid_repository_blocks_public_l2_query_before_consumption(self):
        root = self.make_repo()
        with (root / "l3-trace-registry.yaml").open("r", encoding="utf-8") as stream:
            data = yaml.load(stream, Loader=UniqueKeyLoader)
        data["relations"].pop()
        (root / "l3-trace-registry.yaml").write_text(
            yaml.safe_dump(data, sort_keys=False, allow_unicode=True), encoding="utf-8"
        )
        with self.assertRaises(TraceViewError):
            query_l2(root, "SCAF-ROB-004")

    def test_invalid_frozen_source_blocks_public_pattern_query_before_consumption(self):
        root = self.make_repo()
        source = root / "docs/l3/catalog/COM/SCAF-PAT-COM-001_Reconnect_plus_State_Reconciliation.md"
        text = source.read_text(encoding="utf-8").replace(
            "`SCAF-INT-007`, `SCAF-INT-008`",
            "`SCAF-INT-007` `SCAF-INT-008`",
            1,
        )
        source.write_text(text, encoding="utf-8")
        with self.assertRaises(TraceViewError):
            query_pattern(root, "SCAF-PAT-COM-001")

    def test_cli_json_is_machine_parseable(self):
        stdout = io.StringIO()
        stderr = io.StringIO()
        with redirect_stdout(stdout), redirect_stderr(stderr):
            code = main(["--repository", str(REPO_ROOT), "--l2", "SCAF-ROB-004", "--format", "json"])
        self.assertEqual(0, code, stderr.getvalue())
        payload = json.loads(stdout.getvalue())
        self.assertEqual("l2_to_l3", payload["direction"])
        self.assertEqual("SCAF-ROB-004", payload["query_id"])

    def test_cli_unknown_id_fails_without_view_payload(self):
        stdout = io.StringIO()
        stderr = io.StringIO()
        with redirect_stdout(stdout), redirect_stderr(stderr):
            code = main(["--repository", str(REPO_ROOT), "--l2", "SCAF-INT-999", "--format", "json"])
        self.assertEqual(1, code)
        self.assertEqual("", stdout.getvalue())
        self.assertIn("RESULT: FAIL", stderr.getvalue())

    def test_public_l2_query_owns_validation(self):
        original = query_module.validate_repository
        with patch.object(query_module, "validate_repository", wraps=original) as validator:
            view = query_l2(REPO_ROOT, "SCAF-ROB-004")
        self.assertEqual("l2_to_l3", view["direction"])
        validator.assert_called_once()
        self.assertEqual(REPO_ROOT.absolute(), validator.call_args.args[0])

    def test_public_pattern_query_owns_validation(self):
        original = query_module.validate_repository
        with patch.object(query_module, "validate_repository", wraps=original) as validator:
            view = query_pattern(REPO_ROOT, "SCAF-PAT-COM-001")
        self.assertEqual("l3_to_l2", view["direction"])
        validator.assert_called_once()
        self.assertEqual(REPO_ROOT.absolute(), validator.call_args.args[0])

    def test_internal_validated_context_rejects_caller_constructed_seal(self):
        with self.assertRaises(TraceViewError):
            _ValidatedTraceContext(tuple(), frozenset(), frozenset(), object())

    def test_legacy_public_builder_symbols_are_removed(self):
        self.assertFalse(hasattr(query_module, "TraceContext"))
        self.assertFalse(hasattr(query_module, "build_l2_view"))
        self.assertFalse(hasattr(query_module, "build_pattern_view"))

    def test_package_exports_only_validation_owning_query_api(self):
        self.assertEqual(
            ("TraceViewError", "query_l2", "query_pattern"),
            trace_views_package.__all__,
        )
        self.assertTrue(callable(trace_views_package.query_l2))
        self.assertTrue(callable(trace_views_package.query_pattern))

    def test_cli_uses_same_public_query_entry_point(self):
        stdout = io.StringIO()
        stderr = io.StringIO()
        original = query_module.query_l2
        with patch.object(query_module, "query_l2", wraps=original) as public_query:
            with redirect_stdout(stdout), redirect_stderr(stderr):
                code = main(["--repository", str(REPO_ROOT), "--l2", "SCAF-ROB-004", "--format", "json"])
        self.assertEqual(0, code, stderr.getvalue())
        public_query.assert_called_once_with(REPO_ROOT, "SCAF-ROB-004")


if __name__ == "__main__":
    unittest.main()
