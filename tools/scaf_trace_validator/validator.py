#!/usr/bin/env python3
"""Validate the SCAF L3 trace registry against frozen Pattern metadata.

Authority order:
1. frozen v0.0.3 Pattern Markdown metadata is semantic trace authority;
2. the reviewed rc4 source-extraction contract defines deterministic parsing;
3. the rc4 JSON Schema defines structural representation conformance;
4. l3-trace-registry.yaml is a subordinate representation checked by this tool.

This validator does not decide project applicability, Pattern selection,
satisfaction, compliance, verification, evidence sufficiency, or closure.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Iterable

try:
    import yaml
except ImportError as exc:  # pragma: no cover - CLI environment only
    raise SystemExit(
        "Missing dependency: PyYAML. Install tools/scaf_trace_validator/requirements.txt"
    ) from exc

try:
    from jsonschema import Draft202012Validator
    from jsonschema.exceptions import SchemaError
except ImportError as exc:  # pragma: no cover - CLI environment only
    raise SystemExit(
        "Missing dependency: jsonschema. Install tools/scaf_trace_validator/requirements.txt"
    ) from exc


REGISTRY_PATH = Path("l3-trace-registry.yaml")
SCHEMA_PATH = Path("schemas/l3-trace-registry.schema.json")
AUTHORITY_REGISTRY_PATH = Path("authority-registry.yaml")
PATTERN_ROOT = Path("docs/l3/catalog")

REQUIRED_METADATA_ROWS = (
    "Pattern ID",
    "Primary L2 Trace",
    "Supporting L2 Trace",
    "Constraint Inputs",
)

RELATION_FIELD_MAP = {
    "Primary L2 Trace": "primary_realization_candidate",
    "Supporting L2 Trace": "supporting_realization",
    "Constraint Inputs": "constraint_input",
}

RELATION_ORDER = {
    "primary_realization_candidate": 0,
    "supporting_realization": 1,
    "constraint_input": 2,
}

EXPECTED_PATTERN_COUNT = 12
EXPECTED_RELATION_COUNT = 119
EXPECTED_PRIMARY_COUNT = 23
EXPECTED_SUPPORTING_COUNT = 41
EXPECTED_CONSTRAINT_COUNT = 55
EXPECTED_QUALIFIER_COUNT = 15
EXPECTED_UNIQUE_L2_COUNT = 82
EXPECTED_SOURCE_RELEASE = "v0.0.3"

L2_ID_PATTERN = r"SCAF-(?:AK|CTX|ARCH|INT|TIME|RUN|ROB|LIFE|OBS|CFG|SEC)-\d{3}"
L2_ID_RE = re.compile(rf"^{L2_ID_PATTERN}$")
CODE_ID_RE = re.compile(rf"`(?P<id>{L2_ID_PATTERN})`")
PATTERN_ID_RE = re.compile(r"^SCAF-PAT-[A-Z]{3}-\d{3}$")
TABLE_ROW_RE = re.compile(r"^\|\s*(?P<key>[^|]+?)\s*\|\s*(?P<value>.*?)\s*\|\s*$")
SIMPLE_ID_LIST_RE = re.compile(
    rf"^\s*`{L2_ID_PATTERN}`(?:\s*,\s*`{L2_ID_PATTERN}`)*\s*$"
)
WHITESPACE_RE = re.compile(r"\s+")


class UniqueKeyLoader(yaml.SafeLoader):
    """PyYAML loader that rejects duplicate mapping keys."""


def _construct_mapping(
    loader: UniqueKeyLoader,
    node: yaml.MappingNode,
    deep: bool = False,
) -> dict[Any, Any]:
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
class TraceRelation:
    pattern_id: str
    relation_type: str
    l2_id: str
    pattern_source_path: str
    pattern_source_field: str
    source_release: str
    qualifier: str | None

    def as_dict(self) -> dict[str, Any]:
        return {
            "pattern_id": self.pattern_id,
            "relation_type": self.relation_type,
            "l2_id": self.l2_id,
            "pattern_source_path": self.pattern_source_path,
            "pattern_source_field": self.pattern_source_field,
            "source_release": self.source_release,
            "qualifier": self.qualifier,
        }


@dataclass
class ValidationReport:
    errors: list[str] = field(default_factory=list)
    pattern_count: int = 0
    relation_count: int = 0
    unique_tuple_count: int = 0
    unique_l2_count: int = 0
    qualifier_count: int = 0
    primary_count: int = 0
    supporting_count: int = 0
    constraint_count: int = 0
    schema_valid: bool = False
    source_reconstruction_match: bool = False
    authority_resolution_valid: bool = False
    canonical_order_valid: bool = False

    @property
    def passed(self) -> bool:
        return not self.errors


def _load_yaml(path: Path) -> Any:
    with path.open("r", encoding="utf-8") as stream:
        return yaml.load(stream, Loader=UniqueKeyLoader)


def _load_json(path: Path) -> Any:
    with path.open("r", encoding="utf-8") as stream:
        return json.load(stream)


def _normalize_qualifier(text: str) -> str:
    return WHITESPACE_RE.sub(" ", text.strip())


def _canonical_relation_key(relation: dict[str, Any] | TraceRelation) -> tuple[str, int, str]:
    if isinstance(relation, TraceRelation):
        pattern_id = relation.pattern_id
        relation_type = relation.relation_type
        l2_id = relation.l2_id
    else:
        pattern_id = relation.get("pattern_id", "")
        relation_type = relation.get("relation_type", "")
        l2_id = relation.get("l2_id", "")
    return (pattern_id, RELATION_ORDER.get(relation_type, 999), l2_id)


def _schema_path(error: Any) -> str:
    if not error.absolute_path:
        return "$"
    parts = ["$"]
    for part in error.absolute_path:
        parts.append(f"[{part}]" if isinstance(part, int) else f".{part}")
    return "".join(parts)


def _extract_metadata_rows(source_path: Path, report: ValidationReport) -> dict[str, str] | None:
    try:
        text = source_path.read_text(encoding="utf-8")
    except (OSError, UnicodeError) as exc:
        report.errors.append(f"{source_path}: cannot read frozen Pattern source: {exc}")
        return None

    found: dict[str, list[str]] = {key: [] for key in REQUIRED_METADATA_ROWS}
    for line in text.splitlines():
        match = TABLE_ROW_RE.match(line)
        if not match:
            continue
        key = match.group("key").strip()
        if key in found:
            found[key].append(match.group("value").strip())

    for key, values in found.items():
        if len(values) != 1:
            report.errors.append(
                f"{source_path.as_posix()}: metadata row {key!r} occurs {len(values)} times; expected exactly 1"
            )

    if any(len(values) != 1 for values in found.values()):
        return None
    return {key: values[0] for key, values in found.items()}


def _parse_simple_id_list(value: str, source_label: str) -> list[str]:
    if not SIMPLE_ID_LIST_RE.fullmatch(value):
        raise ValueError(
            f"{source_label}: unsupported Primary/Supporting syntax; expected only comma-separated Markdown code-span L2 IDs"
        )
    ids = [match.group("id") for match in CODE_ID_RE.finditer(value)]
    if not ids:
        raise ValueError(f"{source_label}: no L2 IDs found")
    return ids


def _leading_marker(prefix: str, source_label: str) -> str | None:
    """Interpret text immediately before an ID inside one semicolon clause."""
    stripped = prefix.strip()
    if not stripped:
        return None

    # Between IDs, a leading comma is the item separator. The remaining text may
    # be empty or one reviewed leading qualifier keyword.
    if stripped.startswith(","):
        stripped = stripped[1:].strip()
        if not stripped:
            return None

    if stripped == "applicable":
        return "applicable"
    if stripped == "conditional":
        return "conditional"

    raise ValueError(f"{source_label}: unsupported or ambiguous text before L2 ID: {prefix!r}")


def _parse_constraint_clause(clause: str, source_label: str) -> list[tuple[str, str | None]]:
    matches = list(CODE_ID_RE.finditer(clause))
    if not matches:
        if clause.strip():
            raise ValueError(f"{source_label}: non-empty clause contains no valid Markdown code-span L2 ID")
        return []

    active_leading: str | None = None
    result: list[tuple[str, str | None]] = []

    for index, match in enumerate(matches):
        previous_end = matches[index - 1].end() if index > 0 else 0
        prefix = clause[previous_end:match.start()]
        marker = _leading_marker(prefix, source_label)
        if marker is not None:
            active_leading = marker

        if active_leading == "conditional" and len(matches) != 1:
            raise ValueError(
                f"{source_label}: conditional clause must contain exactly one L2 ID under the reviewed rc4 contract"
            )

        next_start = matches[index + 1].start() if index + 1 < len(matches) else len(clause)
        suffix = clause[match.end():next_start]
        qualifier = active_leading

        if index + 1 < len(matches):
            # Before another ID, only comma/whitespace or comma + a reviewed
            # leading qualifier is legal. Any prose here would be trailing
            # context followed by another ID, which rc4 requires to fail closed.
            _leading_marker(suffix, source_label)
        else:
            tail = suffix.strip()
            if tail:
                if tail.startswith(","):
                    raise ValueError(f"{source_label}: trailing comma or unsupported item after final L2 ID")
                if tail.startswith("where ") or tail == "where":
                    trailing = tail
                elif tail.startswith("outcomes when ") or tail == "outcomes when":
                    trailing = tail
                else:
                    raise ValueError(
                        f"{source_label}: unsupported trailing qualifier context: {tail!r}"
                    )
                if trailing in {"where", "outcomes when"}:
                    raise ValueError(f"{source_label}: trailing context marker has no material text")
                qualifier = f"{qualifier} {trailing}" if qualifier else trailing

        if active_leading == "conditional" and not qualifier.startswith("conditional where "):
            raise ValueError(
                f"{source_label}: conditional requires reviewed 'where ...' trailing context"
            )

        result.append((match.group("id"), _normalize_qualifier(qualifier) if qualifier else None))

    return result


def _parse_constraint_inputs(value: str, source_label: str) -> list[tuple[str, str | None]]:
    relations: list[tuple[str, str | None]] = []
    clauses = value.split(";")
    for clause_index, clause in enumerate(clauses, start=1):
        if not clause.strip():
            raise ValueError(f"{source_label}: empty semicolon clause at position {clause_index}")
        relations.extend(_parse_constraint_clause(clause, f"{source_label} clause {clause_index}"))
    if not relations:
        raise ValueError(f"{source_label}: no Constraint Inputs extracted")
    return relations


def reconstruct_relations(repo_root: Path, report: ValidationReport) -> list[TraceRelation]:
    pattern_root = repo_root / PATTERN_ROOT
    if not pattern_root.is_dir():
        report.errors.append(f"missing frozen Pattern catalog root: {PATTERN_ROOT.as_posix()}")
        return []

    pattern_files = sorted(pattern_root.glob("*/SCAF-PAT-*.md"), key=lambda path: path.as_posix())
    report.pattern_count = len(pattern_files)
    if len(pattern_files) != EXPECTED_PATTERN_COUNT:
        report.errors.append(
            f"frozen Pattern source inventory has {len(pattern_files)} files; expected {EXPECTED_PATTERN_COUNT}"
        )

    relations: list[TraceRelation] = []
    seen_pattern_ids: set[str] = set()

    for source_file in pattern_files:
        relative_source = source_file.relative_to(repo_root).as_posix()
        rows = _extract_metadata_rows(source_file, report)
        if rows is None:
            continue

        pattern_value = rows["Pattern ID"]
        pattern_match = re.fullmatch(r"`(?P<id>SCAF-PAT-[A-Z]{3}-\d{3})`", pattern_value)
        if not pattern_match:
            report.errors.append(
                f"{relative_source}: Pattern ID metadata must be exactly one Markdown code-span Pattern ID"
            )
            continue
        pattern_id = pattern_match.group("id")
        if not PATTERN_ID_RE.fullmatch(pattern_id):
            report.errors.append(f"{relative_source}: malformed Pattern ID {pattern_id!r}")
            continue
        if pattern_id in seen_pattern_ids:
            report.errors.append(f"{relative_source}: duplicate Pattern ID {pattern_id}")
            continue
        seen_pattern_ids.add(pattern_id)

        for source_field in ("Primary L2 Trace", "Supporting L2 Trace"):
            try:
                ids = _parse_simple_id_list(rows[source_field], f"{relative_source} / {source_field}")
            except ValueError as exc:
                report.errors.append(str(exc))
                continue
            for l2_id in ids:
                relations.append(
                    TraceRelation(
                        pattern_id=pattern_id,
                        relation_type=RELATION_FIELD_MAP[source_field],
                        l2_id=l2_id,
                        pattern_source_path=relative_source,
                        pattern_source_field=source_field,
                        source_release=EXPECTED_SOURCE_RELEASE,
                        qualifier=None,
                    )
                )

        try:
            constraint_items = _parse_constraint_inputs(
                rows["Constraint Inputs"], f"{relative_source} / Constraint Inputs"
            )
        except ValueError as exc:
            report.errors.append(str(exc))
            continue
        for l2_id, qualifier in constraint_items:
            relations.append(
                TraceRelation(
                    pattern_id=pattern_id,
                    relation_type="constraint_input",
                    l2_id=l2_id,
                    pattern_source_path=relative_source,
                    pattern_source_field="Constraint Inputs",
                    source_release=EXPECTED_SOURCE_RELEASE,
                    qualifier=qualifier,
                )
            )

    relations.sort(key=_canonical_relation_key)
    return relations


def _load_authority_ids(repo_root: Path, report: ValidationReport) -> set[str]:
    path = repo_root / AUTHORITY_REGISTRY_PATH
    try:
        data = _load_yaml(path)
    except (OSError, UnicodeError, yaml.YAMLError) as exc:
        report.errors.append(f"cannot load {AUTHORITY_REGISTRY_PATH.as_posix()}: {exc}")
        return set()

    if not isinstance(data, dict) or not isinstance(data.get("records"), list):
        report.errors.append("authority-registry.yaml: expected top-level records list")
        return set()

    ids: set[str] = set()
    for index, record in enumerate(data["records"]):
        if not isinstance(record, dict) or not isinstance(record.get("id"), str):
            report.errors.append(f"authority-registry.yaml records[{index}]: missing string id")
            continue
        requirement_id = record["id"]
        if requirement_id in ids:
            report.errors.append(f"authority-registry.yaml: duplicate authority id {requirement_id}")
        ids.add(requirement_id)
    return ids


def _collect_relation_stats(relations: Iterable[dict[str, Any]], report: ValidationReport) -> None:
    relation_list = list(relations)
    report.relation_count = len(relation_list)
    tuples = {
        (relation.get("pattern_id"), relation.get("relation_type"), relation.get("l2_id"))
        for relation in relation_list
        if isinstance(relation, dict)
    }
    report.unique_tuple_count = len(tuples)
    report.unique_l2_count = len(
        {relation.get("l2_id") for relation in relation_list if isinstance(relation, dict) and isinstance(relation.get("l2_id"), str)}
    )
    report.qualifier_count = sum(
        1 for relation in relation_list if isinstance(relation, dict) and isinstance(relation.get("qualifier"), str)
    )
    report.primary_count = sum(
        1 for relation in relation_list if isinstance(relation, dict) and relation.get("relation_type") == "primary_realization_candidate"
    )
    report.supporting_count = sum(
        1 for relation in relation_list if isinstance(relation, dict) and relation.get("relation_type") == "supporting_realization"
    )
    report.constraint_count = sum(
        1 for relation in relation_list if isinstance(relation, dict) and relation.get("relation_type") == "constraint_input"
    )


def validate_repository(repo_root: Path) -> ValidationReport:
    repo_root = repo_root.absolute()
    report = ValidationReport()

    registry_path = repo_root / REGISTRY_PATH
    schema_path = repo_root / SCHEMA_PATH

    try:
        registry_data = _load_yaml(registry_path)
    except (OSError, UnicodeError, yaml.YAMLError) as exc:
        report.errors.append(f"cannot load {REGISTRY_PATH.as_posix()}: {exc}")
        return report

    try:
        schema = _load_json(schema_path)
        Draft202012Validator.check_schema(schema)
    except (OSError, UnicodeError, json.JSONDecodeError, SchemaError) as exc:
        report.errors.append(f"cannot load/validate {SCHEMA_PATH.as_posix()}: {exc}")
        return report

    validator = Draft202012Validator(schema)
    schema_errors = sorted(
        validator.iter_errors(registry_data),
        key=lambda error: (tuple(str(part) for part in error.absolute_path), error.message),
    )
    if schema_errors:
        for error in schema_errors:
            report.errors.append(f"schema {_schema_path(error)}: {error.message}")
    else:
        report.schema_valid = True

    serialized_relations: list[dict[str, Any]] = []
    if isinstance(registry_data, dict) and isinstance(registry_data.get("relations"), list):
        serialized_relations = [item for item in registry_data["relations"] if isinstance(item, dict)]
        _collect_relation_stats(serialized_relations, report)
    else:
        report.errors.append("l3-trace-registry.yaml: expected top-level relations list")

    raw_relations = registry_data.get("relations", []) if isinstance(registry_data, dict) else []
    if isinstance(raw_relations, list) and len(serialized_relations) != len(raw_relations):
        report.errors.append("l3-trace-registry.yaml: one or more relation records are not mappings")

    # Composite tuple uniqueness is deliberately source-aware and not delegated
    # to JSON Schema uniqueItems.
    tuples: list[tuple[Any, Any, Any]] = [
        (relation.get("pattern_id"), relation.get("relation_type"), relation.get("l2_id"))
        for relation in serialized_relations
    ]
    if len(set(tuples)) != len(tuples):
        report.errors.append("l3-trace-registry.yaml: duplicate (pattern_id, relation_type, l2_id) tuple")

    expected_order = sorted(serialized_relations, key=_canonical_relation_key)
    if serialized_relations == expected_order:
        report.canonical_order_valid = True
    else:
        report.errors.append("l3-trace-registry.yaml: relation records are not in canonical order")

    reconstructed = reconstruct_relations(repo_root, report)
    reconstructed_dicts = [relation.as_dict() for relation in reconstructed]
    if serialized_relations == reconstructed_dicts:
        report.source_reconstruction_match = True
    else:
        if len(serialized_relations) != len(reconstructed_dicts):
            report.errors.append(
                f"source reconstruction count mismatch: registry={len(serialized_relations)} source={len(reconstructed_dicts)}"
            )
        else:
            mismatch_index = next(
                (index for index, pair in enumerate(zip(serialized_relations, reconstructed_dicts)) if pair[0] != pair[1]),
                None,
            )
            if mismatch_index is not None:
                report.errors.append(
                    f"source reconstruction mismatch at canonical relation index {mismatch_index}: "
                    f"registry={serialized_relations[mismatch_index]!r} source={reconstructed_dicts[mismatch_index]!r}"
                )

    authority_ids = _load_authority_ids(repo_root, report)
    unresolved = sorted(
        {
            relation["l2_id"]
            for relation in serialized_relations
            if isinstance(relation.get("l2_id"), str) and relation["l2_id"] not in authority_ids
        }
    )
    if unresolved:
        report.errors.append(f"unresolved L2 authority identities: {', '.join(unresolved)}")
    elif serialized_relations and authority_ids:
        report.authority_resolution_valid = True

    # Stable accepted-population checks provide concise diagnostics in addition
    # to schema/source equality. They are not a substitute for reconstruction.
    expected_stats = {
        "pattern_count": EXPECTED_PATTERN_COUNT,
        "relation_count": EXPECTED_RELATION_COUNT,
        "unique_tuple_count": EXPECTED_RELATION_COUNT,
        "unique_l2_count": EXPECTED_UNIQUE_L2_COUNT,
        "qualifier_count": EXPECTED_QUALIFIER_COUNT,
        "primary_count": EXPECTED_PRIMARY_COUNT,
        "supporting_count": EXPECTED_SUPPORTING_COUNT,
        "constraint_count": EXPECTED_CONSTRAINT_COUNT,
    }
    for attribute, expected in expected_stats.items():
        observed = getattr(report, attribute)
        if observed != expected:
            report.errors.append(f"{attribute}: observed {observed}; expected {expected}")

    return report


def _print_report(repo_root: Path, report: ValidationReport) -> None:
    print("SCAF L3 Source-Aware Trace Validation")
    print(f"Repository: {repo_root.absolute()}")
    print(f"Schema:     {SCHEMA_PATH.as_posix()}")
    print(f"Registry:   {REGISTRY_PATH.as_posix()}")
    print(f"Patterns:   {report.pattern_count}")
    print(f"Relations:  {report.relation_count}")
    print(f"Primary:    {report.primary_count}")
    print(f"Supporting: {report.supporting_count}")
    print(f"Constraint: {report.constraint_count}")
    print(f"Unique tuples: {report.unique_tuple_count}")
    print(f"Unique L2 IDs: {report.unique_l2_count}")
    print(f"Qualifiers:    {report.qualifier_count}")
    print(f"Schema validation:      {'PASS' if report.schema_valid else 'FAIL'}")
    print(f"Source reconstruction:  {'PASS' if report.source_reconstruction_match else 'FAIL'}")
    print(f"Authority resolution:   {'PASS' if report.authority_resolution_valid else 'FAIL'}")
    print(f"Canonical ordering:     {'PASS' if report.canonical_order_valid else 'FAIL'}")
    for error in report.errors:
        print(f"ERROR: {error}")
    print(f"Errors: {len(report.errors)}")
    print(f"RESULT: {'PASS' if report.passed else 'FAIL'}")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Validate l3-trace-registry.yaml against the reviewed rc4 schema and frozen L3 source-extraction contract."
    )
    parser.add_argument(
        "--repository",
        type=Path,
        default=Path.cwd(),
        help="Repository root to validate (default: current working directory).",
    )
    args = parser.parse_args(argv)

    report = validate_repository(args.repository)
    _print_report(args.repository, report)
    return 0 if report.passed else 1


if __name__ == "__main__":
    sys.exit(main())
