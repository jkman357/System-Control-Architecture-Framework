from __future__ import annotations

import copy
import json
import unittest
from pathlib import Path

import yaml

from tools.scaf_candidate_authority_validator.validator import (
    CANDIDATE_IDS,
    validate_candidate_data,
)


class CandidateAuthorityValidatorTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.repo_root = Path(__file__).resolve().parents[3]
        cls.registry = yaml.safe_load(
            (cls.repo_root / "candidate-authority-registry.yaml").read_text(encoding="utf-8")
        )
        cls.schema = json.loads(
            (cls.repo_root / "schemas" / "candidate-authority-registry.schema.json").read_text(encoding="utf-8")
        )

    def validate(self, data):
        return validate_candidate_data(data, self.schema, self.repo_root)

    def test_repository_candidate_passes(self):
        report = self.validate(copy.deepcopy(self.registry))
        self.assertTrue(report.passed, "\n".join(report.errors))
        self.assertTrue(report.frozen_input_valid)
        self.assertEqual(299, report.record_count)
        self.assertEqual(294, report.frozen_projection_count)
        self.assertEqual(5, report.candidate_record_count)
        self.assertEqual(5, report.candidate_source_count)
        self.assertEqual(223, report.project_applicable_count)
        self.assertEqual(76, report.framework_invariant_count)

    def test_missing_candidate_record_fails(self):
        data = copy.deepcopy(self.registry)
        data["records"] = [r for r in data["records"] if r["id"] != CANDIDATE_IDS[-1]]
        report = self.validate(data)
        self.assertFalse(report.passed)
        self.assertTrue(any("missing candidate id" in e or "299" in e for e in report.errors))

    def test_duplicate_candidate_id_fails(self):
        data = copy.deepcopy(self.registry)
        data["records"][-1]["id"] = CANDIDATE_IDS[-2]
        data["records"][-1]["source_anchor"] = CANDIDATE_IDS[-2]
        report = self.validate(data)
        self.assertFalse(report.passed)
        self.assertTrue(any("duplicate authority id" in e for e in report.errors))

    def test_frozen_record_modification_fails_projection(self):
        data = copy.deepcopy(self.registry)
        data["records"][0]["relations"] = ["not-allowed"]
        report = self.validate(data)
        self.assertFalse(report.passed)
        self.assertTrue(any("modifies frozen authority record" in e for e in report.errors))

    def test_candidate_source_path_substitution_fails(self):
        data = copy.deepcopy(self.registry)
        record = next(r for r in data["records"] if r["id"] == CANDIDATE_IDS[0])
        record["source_path"] = "docs/normative/80_SCAF_OBS_Observability_Diagnostics_Incident_Evidence_Obligations.md"
        report = self.validate(data)
        self.assertFalse(report.passed)
        self.assertTrue(any("accepted rc01 OBS overlay" in e or "schema" in e for e in report.errors))

    def test_candidate_anchor_must_equal_id(self):
        data = copy.deepcopy(self.registry)
        record = next(r for r in data["records"] if r["id"] == CANDIDATE_IDS[0])
        record["source_anchor"] = CANDIDATE_IDS[1]
        report = self.validate(data)
        self.assertFalse(report.passed)
        self.assertTrue(any("source_anchor must equal" in e for e in report.errors))

    def test_candidate_authority_class_mismatch_fails(self):
        data = copy.deepcopy(self.registry)
        record = next(r for r in data["records"] if r["id"] == CANDIDATE_IDS[0])
        record["authority_class"] = "Framework Normative Invariant"
        report = self.validate(data)
        self.assertFalse(report.passed)
        self.assertTrue(any("authority_class" in e for e in report.errors))

    def test_frozen_registry_hash_mismatch_fails(self):
        data = copy.deepcopy(self.registry)
        data["formal_registry_sha256"] = "0" * 64
        report = self.validate(data)
        self.assertFalse(report.passed)
        self.assertTrue(any("formal_registry_sha256" in e for e in report.errors))

    def test_candidate_source_hash_mismatch_fails(self):
        data = copy.deepcopy(self.registry)
        data["candidate_source_sha256"] = "0" * 64
        report = self.validate(data)
        self.assertFalse(report.passed)
        self.assertTrue(any("candidate_source_sha256" in e for e in report.errors))


if __name__ == "__main__":
    unittest.main()
