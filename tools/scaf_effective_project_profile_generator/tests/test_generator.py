from __future__ import annotations

import copy
import hashlib
import inspect
import shutil
import subprocess
import sys
import tempfile
import unittest
from collections import Counter
from pathlib import Path
from unittest import mock

import yaml

import tools.scaf_effective_project_profile_generator as generator_package
from tools.scaf_effective_project_profile_generator import generator
from tools.scaf_effective_project_profile_validator.validator import (
    validate_effective_project_profile,
)


class EffectiveProjectProfileGeneratorTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.repo_root = Path(__file__).resolve().parents[3]
        cls.project_path = cls.repo_root / "examples/project-application.yaml"
        cls.profile_path = cls.repo_root / "examples/effective-project-profile.yaml"
        cls.project_data = yaml.safe_load(cls.project_path.read_text(encoding="utf-8"))
        cls._generation_cache: dict[str, tuple[bytes, dict]] = {}

    def _generate(self, scope: str, project_path: Path | None = None) -> tuple[bytes, dict]:
        if project_path is None and scope in self._generation_cache:
            return self._generation_cache[scope]
        data = generator.generate_effective_project_profile(
            self.repo_root, scope, project_path
        )
        result = (data, yaml.safe_load(data.decode("utf-8")))
        if project_path is None:
            self._generation_cache[scope] = result
        return result

    def _write_project(self, directory: Path, data: dict, name: str = "project.yaml") -> Path:
        path = directory / name
        path.write_text(
            yaml.safe_dump(data, sort_keys=False, allow_unicode=True),
            encoding="utf-8",
        )
        return path

    def _minimal_repo_copy(self, target: Path) -> Path:
        root = target / "repo"
        (root / "schemas").mkdir(parents=True)
        (root / "docs" / "normative").mkdir(parents=True)
        for rel in (
            "authority-registry.yaml",
            "schemas/authority-registry.schema.json",
            "schemas/project-application.schema.json",
            "schemas/effective-project-profile.schema.json",
        ):
            source = self.repo_root / rel
            dest = root / rel
            dest.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(source, dest)
        for source in sorted((self.repo_root / "docs" / "normative").glob("*.md")):
            shutil.copy2(source, root / "docs" / "normative" / source.name)
        return root

    def test_supported_package_exports_are_bounded(self) -> None:
        self.assertEqual(
            generator_package.__all__,
            (
                "EffectiveProjectProfileGenerationError",
                "generate_effective_project_profile",
            ),
        )

    def test_public_generation_signature_accepts_no_parsed_or_source_override_inputs(self) -> None:
        signature = inspect.signature(generator.generate_effective_project_profile)
        self.assertEqual(
            tuple(signature.parameters),
            ("repo_root", "project_scope_ref", "project_application_path"),
        )

    def test_system_scope_matches_accepted_rc10_fixture_without_comments(self) -> None:
        generated, _ = self._generate("example:scope:system")
        fixture_lines = self.profile_path.read_text(encoding="utf-8").splitlines()
        fixture_without_comments = "\n".join(
            line for line in fixture_lines if not line.startswith("#")
        ).lstrip("\n") + "\n"
        self.assertEqual(generated, fixture_without_comments.encode("utf-8"))

    def test_generation_is_byte_deterministic(self) -> None:
        first = generator.generate_effective_project_profile(
            self.repo_root, "example:scope:system"
        )
        second = generator.generate_effective_project_profile(
            self.repo_root, "example:scope:system"
        )
        self.assertEqual(first, second)

    def test_system_scope_partition_is_1_0_0_217(self) -> None:
        _, profile = self._generate("example:scope:system")
        counts = Counter(entry["profile_state"] for entry in profile["entries"])
        self.assertEqual(counts["applicable"], 1)
        self.assertEqual(counts["not_applicable"], 0)
        self.assertEqual(counts["undetermined"], 0)
        self.assertEqual(counts["no_current_disposition"], 217)
        self.assertEqual(len(profile["entries"]), 218)

    def test_stateless_scope_projects_only_existing_not_applicable_record(self) -> None:
        _, profile = self._generate("example:scope:stateless-node")
        by_id = {entry["scaf_authority_id"]: entry for entry in profile["entries"]}
        self.assertEqual(by_id["SCAF-AK-002"]["profile_state"], "not_applicable")
        self.assertEqual(
            by_id["SCAF-AK-002"]["project_application_record_id"],
            "EXAMPLE-PA-002",
        )
        self.assertEqual(
            by_id["SCAF-AK-001"]["profile_state"], "no_current_disposition"
        )

    def test_interface_scope_preserves_valid_undetermined(self) -> None:
        _, profile = self._generate("example:scope:interface-if3")
        by_id = {entry["scaf_authority_id"]: entry for entry in profile["entries"]}
        self.assertEqual(by_id["SCAF-AK-003"]["profile_state"], "undetermined")
        self.assertEqual(
            by_id["SCAF-AK-003"]["project_application_record_id"],
            "EXAMPLE-PA-003",
        )

    def test_unmatched_scope_generates_complete_all_absence_profile(self) -> None:
        _, profile = self._generate("example:scope:unmatched")
        self.assertEqual(len(profile["entries"]), 218)
        self.assertTrue(
            all(
                entry["profile_state"] == "no_current_disposition"
                for entry in profile["entries"]
            )
        )
        self.assertTrue(
            all("project_application_record_id" not in entry for entry in profile["entries"])
        )

    def test_scope_is_exact_and_not_normalized(self) -> None:
        scope = " example:scope:system "
        _, profile = self._generate(scope)
        self.assertEqual(profile["project_scope_ref"], scope)
        self.assertTrue(
            all(
                entry["profile_state"] == "no_current_disposition"
                for entry in profile["entries"]
            )
        )

    def test_empty_scope_is_rejected(self) -> None:
        with self.assertRaises(generator.EffectiveProjectProfileGenerationError):
            generator.generate_effective_project_profile(self.repo_root, "")

    def test_project_application_sha_binds_exact_captured_bytes(self) -> None:
        _, profile = self._generate("example:scope:system")
        self.assertEqual(
            profile["project_application_source_sha256"],
            hashlib.sha256(self.project_path.read_bytes()).hexdigest(),
        )

    def test_domain_is_complete_unique_and_sorted(self) -> None:
        _, profile = self._generate("example:scope:system")
        ids = [entry["scaf_authority_id"] for entry in profile["entries"]]
        self.assertEqual(len(ids), len(set(ids)))
        self.assertEqual(ids, sorted(ids))
        self.assertEqual(len(ids), 218)

    def test_canonical_mapping_order_is_emitted(self) -> None:
        _, profile = self._generate("example:scope:system")
        self.assertEqual(
            tuple(profile.keys()),
            (
                "profile_kind",
                "representation_release",
                "scaf_source_release",
                "project_scope_ref",
                "project_application_source_sha256",
                "entries",
            ),
        )
        first = profile["entries"][0]
        second = profile["entries"][1]
        self.assertEqual(
            tuple(first.keys()),
            ("scaf_authority_id", "profile_state", "project_application_record_id"),
        )
        self.assertEqual(tuple(second.keys()), ("scaf_authority_id", "profile_state"))

    def test_generated_profile_does_not_duplicate_project_application_truth_fields(self) -> None:
        generated, _ = self._generate("example:scope:system")
        text = generated.decode("utf-8")
        for prohibited in (
            "disposition_basis",
            "decision_refs",
            "authority_refs",
            "supporting_refs",
            "unresolved_reason",
            "awaiting_refs",
        ):
            self.assertNotIn(prohibited, text)

    def test_generated_bytes_pass_rc12_validator(self) -> None:
        generated, _ = self._generate("example:scope:system")
        with tempfile.TemporaryDirectory() as tmp:
            profile_path = Path(tmp) / "generated.yaml"
            profile_path.write_bytes(generated)
            report = validate_effective_project_profile(
                self.repo_root, profile_path, self.project_path
            )
            self.assertTrue(report.passed, report.errors)

    def test_empty_valid_project_dataset_uses_repository_schema_source_binding(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            project_path = Path(tmp) / "empty-project.yaml"
            project_path.write_text("records: []\n", encoding="utf-8")
            generated = generator.generate_effective_project_profile(
                self.repo_root, "example:scope:empty", project_path
            )
            profile = yaml.safe_load(generated.decode("utf-8"))
            self.assertEqual(profile["scaf_source_release"], "v0.0.2")
            self.assertEqual(len(profile["entries"]), 218)
            self.assertTrue(
                all(
                    entry["profile_state"] == "no_current_disposition"
                    for entry in profile["entries"]
                )
            )
            profile_path = Path(tmp) / "profile.yaml"
            profile_path.write_bytes(generated)
            report = validate_effective_project_profile(
                self.repo_root, profile_path, project_path
            )
            self.assertTrue(report.passed, report.errors)

    def test_invalid_project_application_is_rejected_before_generation(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            project = copy.deepcopy(self.project_data)
            project["records"][0]["applicability"] = "no_current_disposition"
            project_path = self._write_project(Path(tmp), project)
            with self.assertRaises(generator.EffectiveProjectProfileGenerationError) as caught:
                generator.generate_effective_project_profile(
                    self.repo_root, "example:scope:system", project_path
                )
            self.assertIn("rc07 validation", str(caught.exception))

    def test_invalid_authority_source_proof_blocks_generation(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = self._minimal_repo_copy(Path(tmp))
            project_path = Path(tmp) / "project.yaml"
            shutil.copy2(self.project_path, project_path)
            registry_path = root / "authority-registry.yaml"
            registry_text = registry_path.read_text(encoding="utf-8")
            registry_path.write_text(
                registry_text.replace(
                    "source_anchor: SCAF-AK-001",
                    "source_anchor: SCAF-AK-999",
                    1,
                ),
                encoding="utf-8",
            )
            with self.assertRaises(generator.EffectiveProjectProfileGenerationError) as caught:
                generator.generate_effective_project_profile(
                    root, "example:scope:system", project_path
                )
            self.assertIn("authority snapshot", str(caught.exception))

    def test_selected_project_application_is_consumed_from_same_snapshot(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            project_path = Path(tmp) / "project.yaml"
            original_bytes = self.project_path.read_bytes()
            project_path.write_bytes(original_bytes)
            real_validate = generator.validate_project_application

            def validate_then_mutate(repo_root: Path, snapshot_path: Path):
                report = real_validate(repo_root, snapshot_path)
                project_path.write_text("records: []\n", encoding="utf-8")
                return report

            with mock.patch.object(
                generator,
                "validate_project_application",
                side_effect=validate_then_mutate,
            ):
                generated = generator.generate_effective_project_profile(
                    self.repo_root, "example:scope:system", project_path
                )
            profile = yaml.safe_load(generated.decode("utf-8"))
            self.assertEqual(
                profile["project_application_source_sha256"],
                hashlib.sha256(original_bytes).hexdigest(),
            )
            by_id = {entry["scaf_authority_id"]: entry for entry in profile["entries"]}
            self.assertEqual(by_id["SCAF-AK-001"]["profile_state"], "applicable")

    def test_authority_and_normative_inputs_are_consumed_from_captured_snapshot(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = self._minimal_repo_copy(Path(tmp))
            project_path = Path(tmp) / "project.yaml"
            shutil.copy2(self.project_path, project_path)
            original_authority = (root / "authority-registry.yaml").read_bytes()
            normative_path = next((root / "docs" / "normative").glob("*.md"))
            original_normative = normative_path.read_bytes()
            real_validate = generator.validate_registry

            def validate_then_mutate(repo_root: Path, registry_path: Path, schema_path: Path):
                report = real_validate(repo_root, registry_path, schema_path)
                (root / "authority-registry.yaml").write_text("records: []\n", encoding="utf-8")
                normative_path.write_text("changed after capture\n", encoding="utf-8")
                return report

            with mock.patch.object(generator, "validate_registry", side_effect=validate_then_mutate):
                generated = generator.generate_effective_project_profile(
                    root, "example:scope:system", project_path
                )
            profile = yaml.safe_load(generated.decode("utf-8"))
            self.assertEqual(len(profile["entries"]), 218)
            self.assertNotEqual((root / "authority-registry.yaml").read_bytes(), original_authority)
            self.assertNotEqual(normative_path.read_bytes(), original_normative)

    def test_generator_source_does_not_hardcode_current_domain_size_or_release(self) -> None:
        source = Path(generator.__file__).read_text(encoding="utf-8")
        self.assertNotIn("218", source)
        self.assertNotIn('"v0.0.2"', source)
        self.assertNotIn("'v0.0.2'", source)

    def test_cli_rejects_repository_boundary_override(self) -> None:
        result = subprocess.run(
            [
                sys.executable,
                "-m",
                "tools.scaf_effective_project_profile_generator.generator",
                "--scope",
                "example:scope:system",
                "--repo-root",
                "/tmp",
            ],
            cwd=self.repo_root,
            capture_output=True,
            text=True,
            check=False,
        )
        self.assertEqual(result.returncode, 2)
        self.assertIn("unrecognized arguments", result.stderr)

    def test_cli_success_emits_only_yaml_on_stdout(self) -> None:
        result = subprocess.run(
            [
                sys.executable,
                "-m",
                "tools.scaf_effective_project_profile_generator.generator",
                "--scope",
                "example:scope:system",
            ],
            cwd=self.repo_root,
            capture_output=True,
            check=False,
        )
        self.assertEqual(result.returncode, 0, result.stderr.decode("utf-8"))
        self.assertEqual(result.stderr, b"")
        profile = yaml.safe_load(result.stdout.decode("utf-8"))
        self.assertEqual(profile["profile_kind"], "effective_project_profile")
        self.assertNotIn(b"PROFILE GENERATION RESULT", result.stdout)

    def test_cli_generated_stdout_passes_rc12(self) -> None:
        result = subprocess.run(
            [
                sys.executable,
                "-m",
                "tools.scaf_effective_project_profile_generator.generator",
                "--scope",
                "example:scope:stateless-node",
            ],
            cwd=self.repo_root,
            capture_output=True,
            check=False,
        )
        self.assertEqual(result.returncode, 0, result.stderr.decode("utf-8"))
        with tempfile.TemporaryDirectory() as tmp:
            profile_path = Path(tmp) / "profile.yaml"
            profile_path.write_bytes(result.stdout)
            report = validate_effective_project_profile(
                self.repo_root, profile_path, self.project_path
            )
            self.assertTrue(report.passed, report.errors)

    def test_generation_does_not_write_persistent_profile_artifacts(self) -> None:
        before = sorted(
            path.relative_to(self.repo_root).as_posix()
            for path in self.repo_root.rglob("*effective*profile*.yaml")
        )
        generator.generate_effective_project_profile(
            self.repo_root, "example:scope:system"
        )
        after = sorted(
            path.relative_to(self.repo_root).as_posix()
            for path in self.repo_root.rglob("*effective*profile*.yaml")
        )
        self.assertEqual(before, after)


if __name__ == "__main__":
    unittest.main()
