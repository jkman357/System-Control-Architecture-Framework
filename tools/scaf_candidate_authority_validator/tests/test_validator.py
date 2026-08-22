from __future__ import annotations

import copy
import json
import unittest
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import patch

import yaml

from tools.scaf_candidate_authority_validator.validator import (
    CANDIDATE_IDS,
    RC01_IDS,
    RC08_IDS,
    validate_candidate_data,
)


class CandidateAuthorityValidatorTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.repo_root = Path(__file__).resolve().parents[3]
        cls.registry = yaml.safe_load((cls.repo_root / "candidate-authority-registry.yaml").read_text(encoding="utf-8"))
        cls.schema = json.loads((cls.repo_root / "schemas" / "candidate-authority-registry.schema.json").read_text(encoding="utf-8"))

    def validate(self, data):
        return validate_candidate_data(data, self.schema, self.repo_root)

    def test_repository_candidate_passes(self):
        report = self.validate(copy.deepcopy(self.registry))
        self.assertTrue(report.passed, "\n".join(report.errors))
        self.assertTrue(report.frozen_input_valid)
        self.assertEqual(302, report.record_count)
        self.assertEqual(294, report.frozen_projection_count)
        self.assertEqual(8, report.candidate_record_count)
        self.assertEqual(2, report.candidate_source_artifact_count)
        self.assertEqual(8, report.candidate_source_id_count)
        self.assertEqual(226, report.project_applicable_count)
        self.assertEqual(76, report.framework_invariant_count)

    def test_missing_candidate_record_fails(self):
        data = copy.deepcopy(self.registry)
        data["records"] = [r for r in data["records"] if r["id"] != CANDIDATE_IDS[-1]]
        report = self.validate(data)
        self.assertFalse(report.passed)
        self.assertTrue(any("missing candidate id" in e or "302" in e for e in report.errors))

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

    def test_rc08_record_cannot_claim_rc01_source_ref(self):
        data = copy.deepcopy(self.registry)
        record = next(r for r in data["records"] if r["id"] == RC08_IDS[0])
        record["source_ref"] = "scaf_obs_v0.2.0rc01"
        report = self.validate(data)
        self.assertFalse(report.passed)
        self.assertTrue(any("does not own" in e or "schema" in e for e in report.errors))

    def test_unknown_source_ref_fails(self):
        data = copy.deepcopy(self.registry)
        record = next(r for r in data["records"] if r["id"] == RC01_IDS[0])
        record["source_ref"] = "unknown_source"
        report = self.validate(data)
        self.assertFalse(report.passed)
        self.assertTrue(any("source_ref" in e for e in report.errors))

    def test_record_source_release_must_match_source_ref(self):
        data = copy.deepcopy(self.registry)
        record = next(r for r in data["records"] if r["id"] == RC08_IDS[0])
        record["source_release"] = "v0.2.0rc01"
        report = self.validate(data)
        self.assertFalse(report.passed)
        self.assertTrue(any("source_release" in e or "schema" in e for e in report.errors))

    def test_candidate_anchor_must_equal_id(self):
        data = copy.deepcopy(self.registry)
        record = next(r for r in data["records"] if r["id"] == RC01_IDS[0])
        record["source_anchor"] = RC01_IDS[1]
        report = self.validate(data)
        self.assertFalse(report.passed)
        self.assertTrue(any("source_anchor must equal" in e for e in report.errors))

    def test_candidate_authority_class_mismatch_fails(self):
        data = copy.deepcopy(self.registry)
        record = next(r for r in data["records"] if r["id"] == RC08_IDS[0])
        record["authority_class"] = "Framework Normative Invariant"
        report = self.validate(data)
        self.assertFalse(report.passed)
        self.assertTrue(any("authority_class" in e or "schema" in e for e in report.errors))

    def test_frozen_registry_hash_mismatch_fails(self):
        data = copy.deepcopy(self.registry)
        data["formal_registry_sha256"] = "0" * 64
        report = self.validate(data)
        self.assertFalse(report.passed)
        self.assertTrue(any("formal_registry_sha256" in e for e in report.errors))

    def test_candidate_source_hash_mismatch_fails(self):
        data = copy.deepcopy(self.registry)
        data["candidate_sources"][1]["source_sha256"] = "0" * 64
        report = self.validate(data)
        self.assertFalse(report.passed)
        self.assertTrue(any("source_sha256" in e or "schema" in e for e in report.errors))

    def test_candidate_source_path_substitution_fails(self):
        data = copy.deepcopy(self.registry)
        data["candidate_sources"][1]["source_path"] = data["candidate_sources"][0]["source_path"]
        report = self.validate(data)
        self.assertFalse(report.passed)
        self.assertTrue(any("source_path" in e or "schema" in e for e in report.errors))

    def test_candidate_source_ownership_overlap_fails(self):
        data = copy.deepcopy(self.registry)
        data["candidate_sources"][1]["candidate_ids"] = [RC01_IDS[-1], *RC08_IDS]
        report = self.validate(data)
        self.assertFalse(report.passed)
        self.assertTrue(any("overlaps" in e or "candidate_ids" in e or "schema" in e for e in report.errors))

    def test_candidate_source_missing_owned_id_fails(self):
        data = copy.deepcopy(self.registry)
        data["candidate_sources"][1]["candidate_ids"] = list(RC08_IDS[:-1])
        report = self.validate(data)
        self.assertFalse(report.passed)
        self.assertTrue(any("ownership missing" in e or "candidate_ids" in e or "schema" in e for e in report.errors))

    def test_extra_candidate_source_fails(self):
        data = copy.deepcopy(self.registry)
        extra = copy.deepcopy(data["candidate_sources"][0])
        extra["source_id"] = "arbitrary_candidate_source"
        data["candidate_sources"].append(extra)
        report = self.validate(data)
        self.assertFalse(report.passed)
        self.assertTrue(any("unexpected candidate source" in e or "schema" in e for e in report.errors))

    def test_frozen_validation_failure_stops_candidate_processing(self):
        data = copy.deepcopy(self.registry)
        frozen_failure = SimpleNamespace(passed=False, errors=["synthetic frozen prerequisite failure"])
        with patch("tools.scaf_candidate_authority_validator.validator.frozen_validator.validate_registry", return_value=frozen_failure):
            report = self.validate(data)
        self.assertFalse(report.passed)
        self.assertFalse(report.frozen_input_valid)
        self.assertTrue(any("synthetic frozen prerequisite failure" in e for e in report.errors))
        self.assertEqual(0, report.record_count)
        self.assertEqual(0, report.unique_id_count)
        self.assertEqual(0, report.frozen_projection_count)
        self.assertEqual(0, report.candidate_record_count)
        self.assertEqual(0, report.candidate_source_artifact_count)
        self.assertEqual(0, report.candidate_source_id_count)
        self.assertEqual(0, report.project_applicable_count)
        self.assertEqual(0, report.framework_invariant_count)


if __name__ == "__main__":
    unittest.main()
