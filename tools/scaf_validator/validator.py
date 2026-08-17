#!/usr/bin/env python3
"""Validate the accepted SCAF authority registry without becoming authority.

The validator checks two layers:
1. JSON-Schema structural conformance for the accepted rc03 ten-field registry.
2. Source-aware fidelity against canonical frozen Markdown under docs/normative/.

Frozen Markdown remains semantic authority. This tool only reports representation
conformance and exits non-zero on ambiguity or mismatch.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

try:
    import yaml
except ImportError as exc:  # pragma: no cover - exercised by CLI environment only
    raise SystemExit("Missing dependency: PyYAML. Install tools/scaf_validator/requirements.txt") from exc

try:
    from jsonschema import Draft202012Validator
except ImportError as exc:  # pragma: no cover - exercised by CLI environment only
    raise SystemExit("Missing dependency: jsonschema. Install tools/scaf_validator/requirements.txt") from exc


CANONICAL_HEADING_RE = re.compile(
    r"^### `(?P<id>SCAF-(?:AK|CTX|ARCH|INT|TIME|RUN|ROB|LIFE|OBS|CFG|SEC)-\d{3})` — .+$",
    re.MULTILINE,
)
TARGET_RE = re.compile(
    r"^\*\*Target:\*\* (?P<target>Project-Applicable Obligation|Framework Normative Invariant)\s*$",
    re.MULTILINE,
)
EXPECTED_RECORD_COUNT = 294
EXPECTED_PROJECT_APPLICABLE = 218
EXPECTED_FRAMEWORK_INVARIANTS = 76


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


UniqueKeyLoader.add_constructor(
    yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG,
    _construct_mapping,
)


@dataclass(frozen=True)
class SourceRequirement:
    requirement_id: str
    source_path: str
    target: str


@dataclass
class ValidationReport:
    errors: list[str] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)
    record_count: int = 0
    unique_id_count: int = 0
    source_requirement_count: int = 0
    project_applicable_count: int = 0
    framework_invariant_count: int = 0

    @property
    def passed(self) -> bool:
        return not self.errors


def load_registry(path: Path) -> Any:
    with path.open("r", encoding="utf-8") as stream:
        return yaml.load(stream, Loader=UniqueKeyLoader)


def load_schema(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as stream:
        return json.load(stream)


def _relative_repo_path(repo_root: Path, path: Path) -> str:
    return path.relative_to(repo_root).as_posix()


def build_source_index(repo_root: Path, report: ValidationReport) -> dict[str, SourceRequirement]:
    normative_root = (repo_root / "docs" / "normative").resolve()
    if not normative_root.is_dir():
        report.errors.append("canonical normative directory does not exist: docs/normative")
        return {}

    index: dict[str, SourceRequirement] = {}
    for source_file in sorted(normative_root.glob("*.md")):
        text = source_file.read_text(encoding="utf-8")
        matches = list(CANONICAL_HEADING_RE.finditer(text))
        for position, match in enumerate(matches):
            requirement_id = match.group("id")
            block_end = matches[position + 1].start() if position + 1 < len(matches) else len(text)
            block = text[match.start():block_end]
            targets = [m.group("target") for m in TARGET_RE.finditer(block)]
            source_path = _relative_repo_path(repo_root, source_file)

            if len(targets) != 1:
                report.errors.append(
                    f"{requirement_id}: canonical source block in {source_path} has {len(targets)} Target fields; expected exactly 1"
                )
                continue
            if requirement_id in index:
                report.errors.append(
                    f"{requirement_id}: duplicate canonical requirement heading in {source_path} and {index[requirement_id].source_path}"
                )
                continue

            index[requirement_id] = SourceRequirement(
                requirement_id=requirement_id,
                source_path=source_path,
                target=targets[0],
            )

    report.source_requirement_count = len(index)
    if len(index) != EXPECTED_RECORD_COUNT:
        report.errors.append(
            f"canonical source inventory has {len(index)} unique requirements; expected {EXPECTED_RECORD_COUNT}"
        )
    return index


def _format_schema_path(error: Any) -> str:
    if not error.absolute_path:
        return "$"
    parts: list[str] = ["$"]
    for item in error.absolute_path:
        if isinstance(item, int):
            parts.append(f"[{item}]")
        else:
            parts.append(f".{item}")
    return "".join(parts)


def validate_registry_data(
    registry_data: Any,
    schema: dict[str, Any],
    repo_root: Path,
) -> ValidationReport:
    report = ValidationReport()

    schema_validator = Draft202012Validator(schema)
    schema_errors = sorted(
        schema_validator.iter_errors(registry_data),
        key=lambda err: (list(err.absolute_path), err.message),
    )
    for error in schema_errors:
        report.errors.append(f"schema {_format_schema_path(error)}: {error.message}")

    # Continue source-aware checks where the registry shape permits it so one run
    # provides useful diagnostics without treating malformed data as authoritative.
    records: list[Any] = []
    if isinstance(registry_data, dict) and isinstance(registry_data.get("records"), list):
        records = registry_data["records"]
    report.record_count = len(records)

    source_index = build_source_index(repo_root.resolve(), report)

    registry_ids: list[str] = []
    project_count = 0
    invariant_count = 0

    for position, record in enumerate(records):
        if not isinstance(record, dict):
            continue
        record_id = record.get("id")
        if not isinstance(record_id, str):
            continue

        registry_ids.append(record_id)
        authority_class = record.get("authority_class")
        if authority_class == "Project-Applicable Obligation":
            project_count += 1
        elif authority_class == "Framework Normative Invariant":
            invariant_count += 1

        source_anchor = record.get("source_anchor")
        if source_anchor != record_id:
            report.errors.append(
                f"record[{position}] {record_id}: source_anchor {source_anchor!r} must equal id"
            )

        source_path = record.get("source_path")
        if not isinstance(source_path, str):
            continue

        candidate = (repo_root / source_path).resolve()
        repo_resolved = repo_root.resolve()
        try:
            candidate.relative_to(repo_resolved)
        except ValueError:
            report.errors.append(f"record[{position}] {record_id}: source_path escapes repository root: {source_path}")
            continue
        if not candidate.is_file():
            report.errors.append(f"record[{position}] {record_id}: source_path does not exist: {source_path}")
            continue

        expected = source_index.get(record_id)
        if expected is None:
            report.errors.append(f"record[{position}] {record_id}: no canonical frozen requirement heading resolves for id")
            continue
        if source_path != expected.source_path:
            report.errors.append(
                f"record[{position}] {record_id}: source_path {source_path!r} does not match canonical {expected.source_path!r}"
            )
        if authority_class != expected.target:
            report.errors.append(
                f"record[{position}] {record_id}: authority_class {authority_class!r} does not match source Target {expected.target!r}"
            )

        # Enforce exactly one canonical heading in the declared file rather than
        # raw textual occurrence count; cross-references are not authority anchors.
        declared_text = candidate.read_text(encoding="utf-8")
        heading_count = sum(1 for m in CANONICAL_HEADING_RE.finditer(declared_text) if m.group("id") == record_id)
        if heading_count != 1:
            report.errors.append(
                f"record[{position}] {record_id}: canonical heading resolves {heading_count} times in {source_path}; expected exactly 1"
            )

    report.unique_id_count = len(set(registry_ids))
    report.project_applicable_count = project_count
    report.framework_invariant_count = invariant_count

    if len(registry_ids) != len(set(registry_ids)):
        seen: set[str] = set()
        duplicates: set[str] = set()
        for record_id in registry_ids:
            if record_id in seen:
                duplicates.add(record_id)
            seen.add(record_id)
        report.errors.append(f"duplicate authority id(s): {', '.join(sorted(duplicates))}")

    source_ids = set(source_index)
    registry_id_set = set(registry_ids)
    missing = sorted(source_ids - registry_id_set)
    extra = sorted(registry_id_set - source_ids)
    if missing:
        report.errors.append(f"source requirement(s) missing from registry: {', '.join(missing)}")
    if extra:
        report.errors.append(f"registry id(s) without canonical source requirement: {', '.join(extra)}")

    if project_count != EXPECTED_PROJECT_APPLICABLE:
        report.errors.append(
            f"registry has {project_count} Project-Applicable Obligations; expected {EXPECTED_PROJECT_APPLICABLE}"
        )
    if invariant_count != EXPECTED_FRAMEWORK_INVARIANTS:
        report.errors.append(
            f"registry has {invariant_count} Framework Normative Invariants; expected {EXPECTED_FRAMEWORK_INVARIANTS}"
        )

    return report


def validate_registry(repo_root: Path, registry_path: Path, schema_path: Path) -> ValidationReport:
    try:
        registry_data = load_registry(registry_path)
    except (OSError, yaml.YAMLError) as exc:
        report = ValidationReport()
        report.errors.append(f"cannot parse registry {registry_path}: {exc}")
        return report

    try:
        schema = load_schema(schema_path)
    except (OSError, json.JSONDecodeError) as exc:
        report = ValidationReport()
        report.errors.append(f"cannot load schema {schema_path}: {exc}")
        return report

    try:
        Draft202012Validator.check_schema(schema)
    except Exception as exc:  # jsonschema raises SchemaError; keep CLI dependency surface narrow.
        report = ValidationReport()
        report.errors.append(f"invalid validator schema {schema_path}: {exc}")
        return report

    return validate_registry_data(registry_data, schema, repo_root)


def _default_repo_root() -> Path:
    return Path(__file__).resolve().parents[2]


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Validate SCAF authority-registry structural and canonical-source fidelity.")
    parser.add_argument("--repo-root", type=Path, default=_default_repo_root())
    parser.add_argument("--registry", type=Path, default=None)
    parser.add_argument("--schema", type=Path, default=None)
    args = parser.parse_args(argv)

    repo_root = args.repo_root.resolve()
    registry_path = (args.registry or (repo_root / "authority-registry.yaml")).resolve()
    schema_path = (args.schema or (repo_root / "schemas" / "authority-registry.schema.json")).resolve()

    report = validate_registry(repo_root, registry_path, schema_path)

    print("SCAF Authority Registry Validation")
    print(f"Repository: {repo_root}")
    print(f"Registry:   {registry_path}")
    print(f"Schema:     {schema_path}")
    print(f"Records:    {report.record_count}")
    print(f"Unique IDs: {report.unique_id_count}")
    print(f"Source IDs: {report.source_requirement_count}")
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
