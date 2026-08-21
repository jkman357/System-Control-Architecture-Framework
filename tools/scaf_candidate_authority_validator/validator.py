#!/usr/bin/env python3
"""Validate the v0.2.0rc03 candidate L1/L2 authority representation.

This validator is intentionally separate from the frozen authority validator.
It validates a development candidate representation without promoting that
representation into formal SCAF authority or making it consumable by SCAF-APP.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from collections import Counter
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

import yaml
from jsonschema import Draft202012Validator

from tools.scaf_validator import validator as frozen_validator


CANDIDATE_IDS = tuple(f"SCAF-OBS-{number:03d}" for number in range(41, 46))
CANDIDATE_ID_SET = set(CANDIDATE_IDS)
EXPECTED_TOTAL = 299
EXPECTED_PROJECT_APPLICABLE = 223
EXPECTED_FRAMEWORK_INVARIANTS = 76
EXPECTED_CANDIDATE_COUNT = 5
EXPECTED_CANDIDATE_SOURCE = (
    "docs/normative-evolution/"
    "80_SCAF_OBS_Observability_Diagnostics_Incident_Evidence_Obligations_v0.2.0rc01.md"
)
EXPECTED_FROZEN_REGISTRY = "authority-registry.yaml"
EXPECTED_FROZEN_SCHEMA = "schemas/authority-registry.schema.json"

HEADING_RE = re.compile(
    r"^### `(?P<id>SCAF-(?:AK|CTX|ARCH|INT|TIME|RUN|ROB|LIFE|OBS|CFG|SEC)-\d{3})` — .+$",
    re.MULTILINE,
)
TARGET_RE = re.compile(
    r"^\*\*Target:\*\* (?P<target>Project-Applicable Obligation|Framework Normative Invariant)\s*$",
    re.MULTILINE,
)


class UniqueKeyLoader(yaml.SafeLoader):
    """PyYAML loader that rejects duplicate mapping keys."""


def _construct_mapping(loader: UniqueKeyLoader, node: yaml.MappingNode, deep: bool = False) -> dict[Any, Any]:
    mapping: dict[Any, Any] = {}
    for key_node, value_node in node.value:
        key = loader.construct_object(key_node, deep=deep)
        if key in mapping:
            raise yaml.constructor.ConstructorError(
                "while constructing a mapping",
                node.start_mark,
                f"found duplicate key {key!r}",
                key_node.start_mark,
            )
        mapping[key] = loader.construct_object(value_node, deep=deep)
    return mapping


UniqueKeyLoader.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, _construct_mapping)


@dataclass
class ValidationReport:
    errors: list[str] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)
    frozen_input_valid: bool = False
    record_count: int = 0
    unique_id_count: int = 0
    project_applicable_count: int = 0
    framework_invariant_count: int = 0
    frozen_projection_count: int = 0
    candidate_record_count: int = 0
    candidate_source_count: int = 0

    @property
    def passed(self) -> bool:
        return not self.errors


def _sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def _load_yaml(path: Path) -> Any:
    with path.open("r", encoding="utf-8") as stream:
        return yaml.load(stream, Loader=UniqueKeyLoader)


def _load_json(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as stream:
        return json.load(stream)


def _format_schema_path(error: Any) -> str:
    if not error.absolute_path:
        return "$"
    parts = ["$"]
    for item in error.absolute_path:
        parts.append(f"[{item}]" if isinstance(item, int) else f".{item}")
    return "".join(parts)


def _extract_candidate_source(
    source_path: Path,
    frozen_ids: set[str],
    report: ValidationReport,
) -> dict[str, str]:
    if not source_path.is_file():
        report.errors.append(f"candidate source does not exist: {source_path}")
        return {}

    text = source_path.read_text(encoding="utf-8")
    matches = list(HEADING_RE.finditer(text))
    seen_ids = [match.group("id") for match in matches]
    new_ids = set(seen_ids) - frozen_ids
    if new_ids != CANDIDATE_ID_SET:
        missing = sorted(CANDIDATE_ID_SET - new_ids)
        extra = sorted(new_ids - CANDIDATE_ID_SET)
        if missing:
            report.errors.append(f"candidate source missing candidate heading(s): {', '.join(missing)}")
        if extra:
            report.errors.append(f"candidate source introduces unexpected authority heading(s): {', '.join(extra)}")

    result: dict[str, str] = {}
    for position, match in enumerate(matches):
        requirement_id = match.group("id")
        if requirement_id not in CANDIDATE_ID_SET:
            continue
        block_end = matches[position + 1].start() if position + 1 < len(matches) else len(text)
        block = text[match.start():block_end]
        targets = [target.group("target") for target in TARGET_RE.finditer(block)]
        if len(targets) != 1:
            report.errors.append(
                f"{requirement_id}: candidate source block has {len(targets)} Target fields; expected exactly 1"
            )
            continue
        if requirement_id in result:
            report.errors.append(f"{requirement_id}: duplicate candidate authority heading")
            continue
        result[requirement_id] = targets[0]

    report.candidate_source_count = len(result)
    return result


def validate_candidate_data(
    candidate_data: Any,
    schema: dict[str, Any],
    repo_root: Path,
) -> ValidationReport:
    repo_root = repo_root.resolve()
    report = ValidationReport()

    frozen_registry_path = repo_root / EXPECTED_FROZEN_REGISTRY
    frozen_schema_path = repo_root / EXPECTED_FROZEN_SCHEMA
    frozen_report = frozen_validator.validate_registry(repo_root, frozen_registry_path, frozen_schema_path)
    if not frozen_report.passed:
        for error in frozen_report.errors:
            report.errors.append(f"frozen authority input invalid: {error}")
        return report

    report.frozen_input_valid = True

    for error in sorted(
        Draft202012Validator(schema).iter_errors(candidate_data),
        key=lambda err: (_format_schema_path(err), err.message),
    ):
        report.errors.append(f"schema {_format_schema_path(error)}: {error.message}")

    try:
        frozen_data = frozen_validator.load_registry(frozen_registry_path)
    except Exception as exc:  # bounded diagnostic; frozen validator already reports detail.
        report.errors.append(f"cannot load frozen authority registry for projection proof: {exc}")
        frozen_data = {"records": []}
    frozen_records = frozen_data.get("records", []) if isinstance(frozen_data, dict) else []
    frozen_map = {
        record.get("id"): record
        for record in frozen_records
        if isinstance(record, dict) and isinstance(record.get("id"), str)
    }
    frozen_ids = set(frozen_map)

    if isinstance(candidate_data, dict):
        declared_frozen_hash = candidate_data.get("formal_registry_sha256")
        if frozen_registry_path.is_file() and declared_frozen_hash != _sha256(frozen_registry_path):
            report.errors.append("formal_registry_sha256 does not match authority-registry.yaml bytes")

        candidate_source_rel = candidate_data.get("candidate_source_path")
        candidate_source_hash = candidate_data.get("candidate_source_sha256")
        if isinstance(candidate_source_rel, str):
            candidate_source_path = (repo_root / candidate_source_rel).resolve()
            try:
                candidate_source_path.relative_to(repo_root)
            except ValueError:
                report.errors.append("candidate_source_path escapes repository root")
                candidate_source_path = repo_root / "__invalid_candidate_source__"
        else:
            candidate_source_path = repo_root / "__invalid_candidate_source__"
        if candidate_source_path.is_file() and candidate_source_hash != _sha256(candidate_source_path):
            report.errors.append("candidate_source_sha256 does not match accepted candidate source bytes")
    else:
        candidate_source_path = repo_root / "__invalid_candidate_source__"

    candidate_source_index = _extract_candidate_source(candidate_source_path, frozen_ids, report)

    records = candidate_data.get("records", []) if isinstance(candidate_data, dict) else []
    if not isinstance(records, list):
        records = []
    report.record_count = len(records)

    id_counter: Counter[str] = Counter()
    candidate_map: dict[str, dict[str, Any]] = {}
    project_count = 0
    invariant_count = 0
    for position, record in enumerate(records):
        if not isinstance(record, dict):
            continue
        record_id = record.get("id")
        if not isinstance(record_id, str):
            continue
        id_counter[record_id] += 1
        if record_id not in candidate_map:
            candidate_map[record_id] = record
        if record.get("authority_class") == "Project-Applicable Obligation":
            project_count += 1
        elif record.get("authority_class") == "Framework Normative Invariant":
            invariant_count += 1
        if record.get("source_anchor") != record_id:
            report.errors.append(
                f"record[{position}] {record_id}: source_anchor must equal the record id"
            )

    report.unique_id_count = len(candidate_map)
    report.project_applicable_count = project_count
    report.framework_invariant_count = invariant_count

    duplicates = sorted(record_id for record_id, count in id_counter.items() if count > 1)
    if duplicates:
        report.errors.append(f"duplicate authority id(s): {', '.join(duplicates)}")

    frozen_projection_matches = 0
    for frozen_id, frozen_record in frozen_map.items():
        candidate_record = candidate_map.get(frozen_id)
        if candidate_record is None:
            report.errors.append(f"frozen authority record missing from candidate projection: {frozen_id}")
        elif candidate_record != frozen_record:
            report.errors.append(f"candidate projection modifies frozen authority record: {frozen_id}")
        else:
            frozen_projection_matches += 1
    report.frozen_projection_count = frozen_projection_matches

    candidate_only_ids = set(candidate_map) - frozen_ids
    if candidate_only_ids != CANDIDATE_ID_SET:
        missing = sorted(CANDIDATE_ID_SET - candidate_only_ids)
        extra = sorted(candidate_only_ids - CANDIDATE_ID_SET)
        if missing:
            report.errors.append(f"candidate registry missing candidate id(s): {', '.join(missing)}")
        if extra:
            report.errors.append(f"candidate registry contains unexpected candidate id(s): {', '.join(extra)}")
    report.candidate_record_count = len(candidate_only_ids & CANDIDATE_ID_SET)

    for candidate_id in CANDIDATE_IDS:
        record = candidate_map.get(candidate_id)
        if record is None:
            continue
        expected_target = candidate_source_index.get(candidate_id)
        if expected_target is None:
            report.errors.append(f"{candidate_id}: no accepted candidate source heading resolves")
            continue
        if record.get("authority_class") != expected_target:
            report.errors.append(
                f"{candidate_id}: authority_class {record.get('authority_class')!r} "
                f"does not match source Target {expected_target!r}"
            )
        if record.get("source_path") != EXPECTED_CANDIDATE_SOURCE:
            report.errors.append(f"{candidate_id}: candidate source_path is not the accepted rc01 OBS overlay")

    if report.record_count != EXPECTED_TOTAL:
        report.errors.append(f"candidate registry has {report.record_count} records; expected {EXPECTED_TOTAL}")
    if project_count != EXPECTED_PROJECT_APPLICABLE:
        report.errors.append(
            f"candidate registry has {project_count} Project-Applicable Obligations; "
            f"expected {EXPECTED_PROJECT_APPLICABLE}"
        )
    if invariant_count != EXPECTED_FRAMEWORK_INVARIANTS:
        report.errors.append(
            f"candidate registry has {invariant_count} Framework Normative Invariants; "
            f"expected {EXPECTED_FRAMEWORK_INVARIANTS}"
        )
    if report.candidate_record_count != EXPECTED_CANDIDATE_COUNT:
        report.errors.append(
            f"candidate registry resolves {report.candidate_record_count} accepted candidate records; "
            f"expected {EXPECTED_CANDIDATE_COUNT}"
        )

    return report


def validate_candidate_registry(repo_root: Path, registry_path: Path, schema_path: Path) -> ValidationReport:
    try:
        candidate_data = _load_yaml(registry_path)
    except (OSError, yaml.YAMLError) as exc:
        report = ValidationReport()
        report.errors.append(f"cannot parse candidate registry {registry_path}: {exc}")
        return report

    try:
        schema = _load_json(schema_path)
        Draft202012Validator.check_schema(schema)
    except Exception as exc:
        report = ValidationReport()
        report.errors.append(f"cannot load/validate candidate schema {schema_path}: {exc}")
        return report

    return validate_candidate_data(candidate_data, schema, repo_root)


def _default_repo_root() -> Path:
    return Path(__file__).resolve().parents[2]


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Validate the repository-owned SCAF v0.2.0rc03 candidate authority representation."
    )
    parser.parse_args(argv)

    repo_root = _default_repo_root().resolve()
    registry_path = repo_root / "candidate-authority-registry.yaml"
    schema_path = repo_root / "schemas" / "candidate-authority-registry.schema.json"
    report = validate_candidate_registry(repo_root, registry_path, schema_path)

    print("SCAF Candidate Authority Registry Validation")
    print(f"Repository: {repo_root}")
    print(f"Registry:   {registry_path}")
    print(f"Schema:     {schema_path}")
    print(f"Frozen authority input valid: {'YES' if report.frozen_input_valid else 'NO'}")
    print(f"Records:    {report.record_count}")
    print(f"Unique IDs: {report.unique_id_count}")
    print(f"Frozen projection matches: {report.frozen_projection_count}")
    print(f"Candidate records: {report.candidate_record_count}")
    print(f"Candidate source IDs: {report.candidate_source_count}")
    print(f"Project-Applicable Obligations: {report.project_applicable_count}")
    print(f"Framework Normative Invariants: {report.framework_invariant_count}")

    if report.warnings:
        print("Warnings:")
        for warning in report.warnings:
            print(f"  - {warning}")
    if report.errors:
        print("Errors:")
        for error in report.errors:
            print(f"  - {error}")
        print("RESULT: FAIL")
        return 1

    print("Errors:      0")
    print("RESULT: PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
