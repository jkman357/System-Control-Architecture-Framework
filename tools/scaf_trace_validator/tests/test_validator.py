from __future__ import annotations

import copy
import tempfile
import unittest
from pathlib import Path

import yaml

from tools.scaf_trace_validator.validator import UniqueKeyLoader, validate_repository


REPO_ROOT = Path(__file__).resolve().parents[3]


class TraceValidatorTests(unittest.TestCase):
    def make_repo(self) -> Path:
        temp = tempfile.TemporaryDirectory()
        self.addCleanup(temp.cleanup)
        root = Path(temp.name) / "repo"
        root.mkdir()

        # Copy only the validator inputs needed by the rc5 proof path.
        for relative in [
            "l3-trace-registry.yaml",
            "authority-registry.yaml",
            "schemas/l3-trace-registry.schema.json",
        ]:
            source = REPO_ROOT / relative
            target = root / relative
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(source.read_bytes())

        source_catalog = REPO_ROOT / "docs/l3/catalog"
        for source in source_catalog.glob("*/SCAF-PAT-*.md"):
            relative = source.relative_to(REPO_ROOT)
            target = root / relative
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(source.read_bytes())
        return root

    def load_registry(self, root: Path):
        with (root / "l3-trace-registry.yaml").open("r", encoding="utf-8") as stream:
            return yaml.load(stream, Loader=UniqueKeyLoader)

    def write_registry(self, root: Path, data) -> None:
        (root / "l3-trace-registry.yaml").write_text(
            yaml.safe_dump(data, sort_keys=False, allow_unicode=True), encoding="utf-8"
        )

    def test_accepted_repository_passes(self):
        report = validate_repository(REPO_ROOT)
        self.assertTrue(report.passed, report.errors)
        self.assertEqual(119, report.relation_count)
        self.assertEqual(15, report.qualifier_count)
        self.assertEqual(82, report.unique_l2_count)

    def test_omitted_relation_fails(self):
        root = self.make_repo()
        data = self.load_registry(root)
        data["relations"].pop()
        self.write_registry(root, data)
        self.assertFalse(validate_repository(root).passed)

    def test_invented_relation_fails_source_reconstruction(self):
        root = self.make_repo()
        data = self.load_registry(root)
        replacement = copy.deepcopy(data["relations"][0])
        replacement["l2_id"] = "SCAF-AK-001"
        data["relations"][0] = replacement
        self.write_registry(root, data)
        report = validate_repository(root)
        self.assertFalse(report.passed)
        self.assertFalse(report.source_reconstruction_match)

    def test_duplicate_projected_tuple_fails(self):
        root = self.make_repo()
        data = self.load_registry(root)
        duplicate = copy.deepcopy(data["relations"][0])
        duplicate["qualifier"] = "synthetic qualifier"
        data["relations"][1] = duplicate
        self.write_registry(root, data)
        report = validate_repository(root)
        self.assertTrue(any("duplicate (pattern_id, relation_type, l2_id) tuple" in e for e in report.errors))

    def test_canonical_order_shuffle_fails(self):
        root = self.make_repo()
        data = self.load_registry(root)
        data["relations"][0], data["relations"][1] = data["relations"][1], data["relations"][0]
        self.write_registry(root, data)
        report = validate_repository(root)
        self.assertFalse(report.canonical_order_valid)
        self.assertFalse(report.passed)

    def test_qualifier_omission_fails(self):
        root = self.make_repo()
        data = self.load_registry(root)
        relation = next(item for item in data["relations"] if item["qualifier"] == "applicable")
        relation["qualifier"] = None
        self.write_registry(root, data)
        report = validate_repository(root)
        self.assertFalse(report.source_reconstruction_match)
        self.assertFalse(report.passed)

    def test_qualifier_reassociation_fails(self):
        root = self.make_repo()
        data = self.load_registry(root)
        qualified_index = next(i for i, item in enumerate(data["relations"]) if item["qualifier"] == "applicable")
        unqualified_index = next(i for i, item in enumerate(data["relations"]) if item["qualifier"] is None)
        data["relations"][unqualified_index]["qualifier"] = data["relations"][qualified_index]["qualifier"]
        data["relations"][qualified_index]["qualifier"] = None
        self.write_registry(root, data)
        report = validate_repository(root)
        self.assertFalse(report.source_reconstruction_match)
        self.assertFalse(report.passed)

    def test_unresolved_but_well_formed_l2_id_fails(self):
        root = self.make_repo()
        data = self.load_registry(root)
        data["relations"][0]["l2_id"] = "SCAF-INT-999"
        self.write_registry(root, data)
        report = validate_repository(root)
        self.assertTrue(any("unresolved L2 authority identities" in e for e in report.errors))

    def test_wrong_source_path_fails(self):
        root = self.make_repo()
        data = self.load_registry(root)
        data["relations"][0]["pattern_source_path"] = data["relations"][-1]["pattern_source_path"]
        self.write_registry(root, data)
        self.assertFalse(validate_repository(root).passed)

    def test_wrong_source_field_fails(self):
        root = self.make_repo()
        data = self.load_registry(root)
        data["relations"][0]["pattern_source_field"] = "Constraint Inputs"
        self.write_registry(root, data)
        self.assertFalse(validate_repository(root).passed)

    def test_primary_source_prose_fails_closed(self):
        root = self.make_repo()
        source = next((root / "docs/l3/catalog").glob("*/SCAF-PAT-*.md"))
        text = source.read_text(encoding="utf-8")
        text = text.replace("| Primary L2 Trace |", "| Primary L2 Trace | narrative ", 1)
        source.write_text(text, encoding="utf-8")
        report = validate_repository(root)
        self.assertTrue(any("unsupported Primary/Supporting syntax" in e for e in report.errors))

    def test_unknown_constraint_qualifier_fails_closed(self):
        root = self.make_repo()
        source = root / "docs/l3/catalog/TIM/SCAF-PAT-TIM-002_Timebase_Clock_Relationship_Epoch_Validity.md"
        text = source.read_text(encoding="utf-8")
        text = text.replace("Constraint Inputs | applicable `SCAF-INT-008`", "Constraint Inputs | relevant `SCAF-INT-008`", 1)
        source.write_text(text, encoding="utf-8")
        report = validate_repository(root)
        self.assertTrue(any("unsupported or ambiguous text before L2 ID" in e for e in report.errors))

    def test_conditional_multiple_ids_fails_closed(self):
        root = self.make_repo()
        source = root / "docs/l3/catalog/REC/SCAF-PAT-REC-001_Bounded_Retry_with_Escalation.md"
        text = source.read_text(encoding="utf-8")
        text = text.replace(
            "conditional `SCAF-INT-007` where retry repeats/interleaves Interaction exchanges",
            "conditional `SCAF-INT-007`, `SCAF-INT-008` where retry repeats/interleaves Interaction exchanges",
            1,
        )
        source.write_text(text, encoding="utf-8")
        report = validate_repository(root)
        self.assertTrue(any("conditional clause must contain exactly one L2 ID" in e for e in report.errors))

    def test_trailing_context_followed_by_id_fails_closed(self):
        root = self.make_repo()
        source = root / "docs/l3/catalog/PST/SCAF-PAT-PST-001_Atomic_Dual_Copy_Persistent_State.md"
        text = source.read_text(encoding="utf-8")
        text = text.replace(
            "`SCAF-TIME-011` where storage/resource budget is material",
            "`SCAF-TIME-011` where storage/resource budget is material, `SCAF-TIME-012`",
            1,
        )
        source.write_text(text, encoding="utf-8")
        report = validate_repository(root)
        self.assertTrue(any("unsupported or ambiguous text before L2 ID" in e for e in report.errors))

    def test_duplicate_authoritative_metadata_row_fails_closed(self):
        root = self.make_repo()
        source = next((root / "docs/l3/catalog").glob("*/SCAF-PAT-*.md"))
        text = source.read_text(encoding="utf-8")
        row = next(line for line in text.splitlines() if line.startswith("| Primary L2 Trace |"))
        source.write_text(text.replace(row, row + "\n" + row, 1), encoding="utf-8")
        report = validate_repository(root)
        self.assertTrue(any("occurs 2 times; expected exactly 1" in e for e in report.errors))

    def test_narrative_l2_trace_prose_does_not_create_edges(self):
        root = self.make_repo()
        source = next((root / "docs/l3/catalog").glob("*/SCAF-PAT-*.md"))
        with source.open("a", encoding="utf-8") as stream:
            stream.write("\n## Review-only narrative\nNarrative mentions `SCAF-INT-999` but is not metadata authority.\n")
        report = validate_repository(root)
        self.assertTrue(report.passed, report.errors)


if __name__ == "__main__":
    unittest.main()
