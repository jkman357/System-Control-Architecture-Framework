#!/usr/bin/env python3
"""Validate the v0.2.0rc10 candidate multi-source L1/L2 authority representation.

This validator is intentionally separate from the frozen authority validator.
It validates a development candidate authority set, preserves exact formal
projection, and proves per-record semantic provenance against controlled
candidate source artifacts. It does not promote candidate authority or make it
consumable by SCAF-APP.
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

RC01_IDS = tuple(f"SCAF-OBS-{number:03d}" for number in range(41, 46))
RC08_IDS = tuple(f"SCAF-OBS-{number:03d}" for number in range(46, 49))
CANDIDATE_IDS = RC01_IDS + RC08_IDS
CANDIDATE_ID_SET = set(CANDIDATE_IDS)
EXPECTED_TOTAL = 302
EXPECTED_PROJECT_APPLICABLE = 226
EXPECTED_FRAMEWORK_INVARIANTS = 76
EXPECTED_CANDIDATE_COUNT = 8
EXPECTED_SOURCE_ARTIFACT_COUNT = 2
EXPECTED_SOURCE_ID_COUNT = 8
EXPECTED_FROZEN_REGISTRY = "authority-registry.yaml"
EXPECTED_FROZEN_SCHEMA = "schemas/authority-registry.schema.json"
EXPECTED_AUTHORITY_SET_ID = "scaf_candidate_l1_l2_authority_set_v0.2.0rc10"
EXPECTED_SOURCES = {
    "scaf_obs_v0.2.0rc01": {
        "source_path": "docs/normative-evolution/80_SCAF_OBS_Observability_Diagnostics_Incident_Evidence_Obligations_v0.2.0rc01.md",
        "source_release": "v0.2.0rc01",
        "candidate_ids": RC01_IDS,
    },
    "scaf_obs_v0.2.0rc08": {
        "source_path": "docs/normative-evolution/80_SCAF_OBS_Observability_Diagnostics_Incident_Evidence_Obligations_v0.2.0rc08.md",
        "source_release": "v0.2.0rc08",
        "candidate_ids": RC08_IDS,
    },
}

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
                "while constructing a mapping", node.start_mark,
                f"found duplicate key {key!r}", key_node.start_mark,
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
    candidate_source_artifact_count: int = 0
    candidate_source_id_count: int = 0

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
    return yaml.load(path.read_text(encoding="utf-8"), Loader=UniqueKeyLoader)


def _load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def _format_schema_path(error: Any) -> str:
    return "/".join(str(part) for part in error.absolute_path) or "<root>"


def _resolve_repo_path(repo_root: Path, rel: Any, label: str, report: ValidationReport) -> Path | None:
    if not isinstance(rel, str):
        report.errors.append(f"{label} must be a repository-relative string")
        return None
    path = (repo_root / rel).resolve()
    try:
        path.relative_to(repo_root)
    except ValueError:
        report.errors.append(f"{label} escapes repository root")
        return None
    return path


def _extract_targets_for_ids(source_path: Path, ids: tuple[str, ...], report: ValidationReport) -> dict[str, str]:
    if not source_path.is_file():
        report.errors.append(f"candidate source missing: {source_path}")
        return {}
    text = source_path.read_text(encoding="utf-8")
    matches = list(HEADING_RE.finditer(text))
    headings = {m.group("id"): m for m in matches}
    result: dict[str, str] = {}
    for requirement_id in ids:
        match = headings.get(requirement_id)
        if match is None:
            report.errors.append(f"{requirement_id}: no heading in bound candidate source")
            continue
        later = [m.start() for m in matches if m.start() > match.start()]
        end = min(later) if later else len(text)
        block = text[match.end():end]
        targets = TARGET_RE.findall(block)
        if len(targets) != 1:
            report.errors.append(
                f"{requirement_id}: candidate source block has {len(targets)} Target fields; expected exactly 1"
            )
            continue
        result[requirement_id] = targets[0]
    return result


def validate_candidate_data(candidate_data: Any, schema: dict[str, Any], repo_root: Path) -> ValidationReport:
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

    for error in sorted(Draft202012Validator(schema).iter_errors(candidate_data), key=lambda err: (_format_schema_path(err), err.message)):
        report.errors.append(f"schema {_format_schema_path(error)}: {error.message}")

    try:
        frozen_data = frozen_validator.load_registry(frozen_registry_path)
    except Exception as exc:
        report.errors.append(f"cannot load frozen authority registry for projection proof: {exc}")
        frozen_data = {"records": []}
    frozen_records = frozen_data.get("records", []) if isinstance(frozen_data, dict) else []
    frozen_map = {r.get("id"): r for r in frozen_records if isinstance(r, dict) and isinstance(r.get("id"), str)}
    frozen_ids = set(frozen_map)

    if not isinstance(candidate_data, dict):
        candidate_data = {}

    if candidate_data.get("authority_set_id") != EXPECTED_AUTHORITY_SET_ID:
        report.errors.append("authority_set_id does not identify the controlled rc10 candidate authority set")

    declared_frozen_hash = candidate_data.get("formal_registry_sha256")
    if frozen_registry_path.is_file() and declared_frozen_hash != _sha256(frozen_registry_path):
        report.errors.append("formal_registry_sha256 does not match authority-registry.yaml bytes")

    source_entries = candidate_data.get("candidate_sources", [])
    if not isinstance(source_entries, list):
        source_entries = []
    report.candidate_source_artifact_count = len(source_entries)

    source_map: dict[str, dict[str, Any]] = {}
    owned_ids: set[str] = set()
    source_target_index: dict[str, str] = {}
    for position, source in enumerate(source_entries):
        if not isinstance(source, dict):
            report.errors.append(f"candidate_sources[{position}] is not a mapping")
            continue
        source_id = source.get("source_id")
        if not isinstance(source_id, str):
            report.errors.append(f"candidate_sources[{position}].source_id is invalid")
            continue
        if source_id in source_map:
            report.errors.append(f"duplicate candidate source_id: {source_id}")
            continue
        source_map[source_id] = source
        expected = EXPECTED_SOURCES.get(source_id)
        if expected is None:
            report.errors.append(f"unexpected candidate source_id: {source_id}")
            continue
        if source.get("source_path") != expected["source_path"]:
            report.errors.append(f"{source_id}: source_path does not match controlled source")
        if source.get("source_release") != expected["source_release"]:
            report.errors.append(f"{source_id}: source_release does not match controlled source")
        ids = source.get("candidate_ids", [])
        if tuple(ids) != expected["candidate_ids"]:
            report.errors.append(f"{source_id}: candidate_ids do not match controlled source ownership")
        overlap = owned_ids.intersection(ids if isinstance(ids, list) else [])
        if overlap:
            report.errors.append(f"candidate source ownership overlaps for: {', '.join(sorted(overlap))}")
        if isinstance(ids, list):
            owned_ids.update(x for x in ids if isinstance(x, str))
        source_path = _resolve_repo_path(repo_root, source.get("source_path"), f"{source_id}.source_path", report)
        if source_path is not None:
            if not source_path.is_file():
                report.errors.append(f"{source_id}: candidate source file does not exist")
            elif source.get("source_sha256") != _sha256(source_path):
                report.errors.append(f"{source_id}: source_sha256 does not match candidate source bytes")
            source_target_index.update(_extract_targets_for_ids(source_path, expected["candidate_ids"], report))

    if set(source_map) != set(EXPECTED_SOURCES):
        missing = sorted(set(EXPECTED_SOURCES) - set(source_map))
        extra = sorted(set(source_map) - set(EXPECTED_SOURCES))
        if missing:
            report.errors.append(f"candidate source definition missing: {', '.join(missing)}")
        if extra:
            report.errors.append(f"unexpected candidate source definition(s): {', '.join(extra)}")
    if owned_ids != CANDIDATE_ID_SET:
        missing = sorted(CANDIDATE_ID_SET - owned_ids)
        extra = sorted(owned_ids - CANDIDATE_ID_SET)
        if missing:
            report.errors.append(f"candidate source ownership missing candidate id(s): {', '.join(missing)}")
        if extra:
            report.errors.append(f"candidate source ownership contains unexpected id(s): {', '.join(extra)}")
    report.candidate_source_id_count = len(owned_ids & CANDIDATE_ID_SET)

    records = candidate_data.get("records", [])
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
            report.errors.append(f"record[{position}] {record_id}: source_anchor must equal the record id")

    report.unique_id_count = len(candidate_map)
    report.project_applicable_count = project_count
    report.framework_invariant_count = invariant_count
    duplicates = sorted(rid for rid, count in id_counter.items() if count > 1)
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
        source_ref = record.get("source_ref")
        source = source_map.get(source_ref) if isinstance(source_ref, str) else None
        if source is None:
            report.errors.append(f"{candidate_id}: source_ref does not resolve to a controlled candidate source")
            continue
        owned = source.get("candidate_ids", [])
        if candidate_id not in owned:
            report.errors.append(f"{candidate_id}: source_ref points to a source that does not own this candidate id")
        if record.get("source_path") != source.get("source_path"):
            report.errors.append(f"{candidate_id}: record source_path disagrees with source_ref")
        if record.get("source_release") != source.get("source_release"):
            report.errors.append(f"{candidate_id}: record source_release disagrees with source_ref")
        expected_target = source_target_index.get(candidate_id)
        if expected_target is None:
            report.errors.append(f"{candidate_id}: no bound candidate source heading resolves")
        elif record.get("authority_class") != expected_target:
            report.errors.append(
                f"{candidate_id}: authority_class {record.get('authority_class')!r} does not match source Target {expected_target!r}"
            )

    if report.record_count != EXPECTED_TOTAL:
        report.errors.append(f"candidate registry has {report.record_count} records; expected {EXPECTED_TOTAL}")
    if project_count != EXPECTED_PROJECT_APPLICABLE:
        report.errors.append(f"candidate registry has {project_count} Project-Applicable Obligations; expected {EXPECTED_PROJECT_APPLICABLE}")
    if invariant_count != EXPECTED_FRAMEWORK_INVARIANTS:
        report.errors.append(f"candidate registry has {invariant_count} Framework Normative Invariants; expected {EXPECTED_FRAMEWORK_INVARIANTS}")
    if report.candidate_record_count != EXPECTED_CANDIDATE_COUNT:
        report.errors.append(f"candidate registry resolves {report.candidate_record_count} candidate records; expected {EXPECTED_CANDIDATE_COUNT}")
    if report.candidate_source_artifact_count != EXPECTED_SOURCE_ARTIFACT_COUNT:
        report.errors.append(f"candidate registry has {report.candidate_source_artifact_count} candidate source artifacts; expected {EXPECTED_SOURCE_ARTIFACT_COUNT}")
    if report.candidate_source_id_count != EXPECTED_SOURCE_ID_COUNT:
        report.errors.append(f"candidate source ownership resolves {report.candidate_source_id_count} candidate ids; expected {EXPECTED_SOURCE_ID_COUNT}")

    return report


def validate_candidate_registry(repo_root: Path, registry_path: Path, schema_path: Path) -> ValidationReport:
    try:
        candidate_data = _load_yaml(registry_path)
    except (OSError, yaml.YAMLError) as exc:
        report = ValidationReport(); report.errors.append(f"cannot parse candidate registry {registry_path}: {exc}"); return report
    try:
        schema = _load_json(schema_path); Draft202012Validator.check_schema(schema)
    except Exception as exc:
        report = ValidationReport(); report.errors.append(f"cannot load/validate candidate schema {schema_path}: {exc}"); return report
    return validate_candidate_data(candidate_data, schema, repo_root)


def _default_repo_root() -> Path:
    return Path(__file__).resolve().parents[2]


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Validate the repository-owned SCAF v0.2.0rc10 candidate multi-source authority representation.")
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
    print(f"Candidate source artifacts: {report.candidate_source_artifact_count}")
    print(f"Candidate source-owned IDs: {report.candidate_source_id_count}")
    print(f"Project-Applicable Obligations: {report.project_applicable_count}")
    print(f"Framework Normative Invariants: {report.framework_invariant_count}")
    if report.warnings:
        print("Warnings:")
        for warning in report.warnings: print(f"  - {warning}")
    if report.errors:
        print("Errors:")
        for error in report.errors: print(f"  - {error}")
        print("RESULT: FAIL"); return 1
    print("Errors:      0")
    print("RESULT: PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
