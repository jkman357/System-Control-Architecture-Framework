#!/usr/bin/env python3
"""Validate SCAF Project Application representation conformance.

Authority / validation order:
1. accepted SCAF-APP semantics and rc04 YAML representation contract;
2. rc06 JSON Schema for parsed-instance structural/state constraints;
3. this rc07 validator for accepted raw-YAML policy, deterministic
   collection ordering, cross-record identity rules, and frozen
   authority-registry target resolution.

The validator does not decide engineering applicability, rationale quality,
project authority sufficiency, implementation, verification, compliance,
Pattern selection, evidence sufficiency, or closure.
"""

from __future__ import annotations

import argparse
import json
import sys
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

try:
    import yaml
except ImportError as exc:  # pragma: no cover - CLI environment only
    raise SystemExit(
        "Missing dependency: PyYAML. Install "
        "tools/scaf_project_application_validator/requirements.txt"
    ) from exc

try:
    from jsonschema import Draft202012Validator
    from jsonschema.exceptions import SchemaError
except ImportError as exc:  # pragma: no cover - CLI environment only
    raise SystemExit(
        "Missing dependency: jsonschema. Install "
        "tools/scaf_project_application_validator/requirements.txt"
    ) from exc

from tools.scaf_validator.validator import validate_registry


DEFAULT_PROJECT_APPLICATION_PATH = Path("examples/project-application.yaml")
PROJECT_APPLICATION_SCHEMA_PATH = Path("schemas/project-application.schema.json")
AUTHORITY_REGISTRY_PATH = Path("authority-registry.yaml")
AUTHORITY_SCHEMA_PATH = Path("schemas/authority-registry.schema.json")

EXPECTED_AUTHORITY_CLASS = "Project-Applicable Obligation"

REFERENCE_LIST_SURFACES = (
    ("disposition_basis.basis_refs", ("disposition_basis", "basis_refs")),
    ("disposition_basis.awaiting_refs", ("disposition_basis", "awaiting_refs")),
    ("decision_refs", ("decision_refs",)),
    ("authority_refs", ("authority_refs",)),
    ("supporting_refs", ("supporting_refs",)),
)


class StrictProjectApplicationLoader(yaml.SafeLoader):
    """Safe YAML loader that rejects ambiguous mapping-key forms."""


def _construct_mapping(
    loader: StrictProjectApplicationLoader,
    node: yaml.MappingNode,
    deep: bool = False,
) -> dict[str, Any]:
    mapping: dict[str, Any] = {}
    for key_node, value_node in node.value:
        if getattr(key_node, "value", None) == "<<":
            raise yaml.constructor.ConstructorError(
                "while constructing a mapping",
                node.start_mark,
                "YAML merge keys are prohibited by the Project Application contract",
                key_node.start_mark,
            )
        key = loader.construct_object(key_node, deep=deep)
        if not isinstance(key, str):
            raise yaml.constructor.ConstructorError(
                "while constructing a mapping",
                node.start_mark,
                f"non-string mapping key {key!r} is prohibited",
                key_node.start_mark,
            )
        if key in mapping:
            raise yaml.constructor.ConstructorError(
                "while constructing a mapping",
                node.start_mark,
                f"found duplicate key {key!r}",
                key_node.start_mark,
            )
        mapping[key] = loader.construct_object(value_node, deep=deep)
    return mapping


StrictProjectApplicationLoader.add_constructor(
    yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG,
    _construct_mapping,
)


@dataclass
class ValidationReport:
    errors: list[str] = field(default_factory=list)
    record_count: int = 0
    loader_policy_valid: bool = False
    schema_valid: bool = False
    record_identity_unique: bool = False
    authority_scope_unique: bool = False
    canonical_order_valid: bool = False
    authority_registry_valid: bool = False
    authority_resolution_valid: bool = False

    @property
    def passed(self) -> bool:
        return not self.errors


def _schema_path(error: Any) -> str:
    if not error.absolute_path:
        return "$"
    parts = ["$"]
    for part in error.absolute_path:
        parts.append(f"[{part}]" if isinstance(part, int) else f".{part}")
    return "".join(parts)


def _scan_yaml_policy(text: str, source_label: str, report: ValidationReport) -> bool:
    document_count = 0
    try:
        for event in yaml.parse(text):
            if isinstance(event, yaml.events.DocumentStartEvent):
                document_count += 1
            if isinstance(event, yaml.events.AliasEvent):
                report.errors.append(
                    f"{source_label}: YAML aliases are prohibited"
                )
            anchor = getattr(event, "anchor", None)
            if anchor is not None:
                report.errors.append(
                    f"{source_label}: YAML anchors are prohibited (anchor {anchor!r})"
                )
            tag = getattr(event, "tag", None)
            if tag is not None and not tag.startswith("tag:yaml.org,2002:"):
                report.errors.append(
                    f"{source_label}: custom YAML tags are prohibited (tag {tag!r})"
                )
    except yaml.YAMLError as exc:
        report.errors.append(f"{source_label}: YAML syntax/event parse failed: {exc}")
        return False

    if document_count != 1:
        report.errors.append(
            f"{source_label}: expected exactly one YAML document; found {document_count}"
        )

    return not report.errors


def _load_project_application(path: Path, report: ValidationReport) -> Any | None:
    source_label = path.as_posix()
    try:
        text = path.read_text(encoding="utf-8")
    except (OSError, UnicodeError) as exc:
        report.errors.append(f"{source_label}: cannot read Project Application YAML: {exc}")
        return None

    if not _scan_yaml_policy(text, source_label, report):
        return None

    try:
        data = yaml.load(text, Loader=StrictProjectApplicationLoader)
    except yaml.YAMLError as exc:
        report.errors.append(f"{source_label}: YAML loader-policy validation failed: {exc}")
        return None

    report.loader_policy_valid = True
    return data


def _load_json(path: Path, report: ValidationReport) -> Any | None:
    try:
        with path.open("r", encoding="utf-8") as stream:
            return json.load(stream)
    except (OSError, UnicodeError, json.JSONDecodeError) as exc:
        report.errors.append(f"{path.as_posix()}: cannot load JSON: {exc}")
        return None


def _validate_schema(
    data: Any,
    schema_path: Path,
    report: ValidationReport,
) -> bool:
    schema = _load_json(schema_path, report)
    if schema is None:
        return False

    try:
        Draft202012Validator.check_schema(schema)
    except SchemaError as exc:
        report.errors.append(
            f"{schema_path.as_posix()}: invalid JSON Schema Draft 2020-12 contract: {exc.message}"
        )
        return False

    validator = Draft202012Validator(schema)
    errors = sorted(
        validator.iter_errors(data),
        key=lambda error: (list(error.absolute_path), error.message),
    )
    if errors:
        for error in errors:
            report.errors.append(
                f"Project Application schema: {_schema_path(error)}: {error.message}"
            )
        return False

    report.schema_valid = True
    return True


def _validate_cross_record_identity(records: list[dict[str, Any]], report: ValidationReport) -> None:
    record_ids: dict[str, int] = {}
    authority_scope_pairs: dict[tuple[str, str], int] = {}

    for index, record in enumerate(records):
        record_id = record["record_id"]
        previous = record_ids.get(record_id)
        if previous is not None:
            report.errors.append(
                f"records[{index}].record_id: duplicate record_id {record_id!r}; "
                f"already used by records[{previous}]"
            )
        else:
            record_ids[record_id] = index

        pair = (record["scaf_authority_id"], record["project_scope_ref"])
        previous_pair = authority_scope_pairs.get(pair)
        if previous_pair is not None:
            report.errors.append(
                f"records[{index}]: duplicate active (scaf_authority_id, project_scope_ref) "
                f"pair {pair!r}; already used by records[{previous_pair}]"
            )
        else:
            authority_scope_pairs[pair] = index

    report.record_identity_unique = len(record_ids) == len(records)
    report.authority_scope_unique = len(authority_scope_pairs) == len(records)


def _lookup_nested(record: dict[str, Any], path: tuple[str, ...]) -> Any:
    current: Any = record
    for part in path:
        if not isinstance(current, dict) or part not in current:
            return None
        current = current[part]
    return current


def _validate_canonical_order(records: list[dict[str, Any]], report: ValidationReport) -> None:
    ordering_errors_before = len(report.errors)

    observed_ids = [record["record_id"] for record in records]
    expected_ids = sorted(observed_ids)
    if observed_ids != expected_ids:
        report.errors.append(
            "records: non-canonical order; records must be ordered by exact record_id ascending"
        )

    for index, record in enumerate(records):
        for label, path in REFERENCE_LIST_SURFACES:
            values = _lookup_nested(record, path)
            if values is None:
                continue
            if values != sorted(values):
                report.errors.append(
                    f"records[{index}].{label}: non-canonical order; reference strings "
                    "must be ordered by exact serialized string ascending"
                )

    report.canonical_order_valid = len(report.errors) == ordering_errors_before


def _load_authority_index(
    repo_root: Path,
    report: ValidationReport,
) -> dict[str, dict[str, Any]] | None:
    registry_path = repo_root / AUTHORITY_REGISTRY_PATH
    schema_path = repo_root / AUTHORITY_SCHEMA_PATH
    authority_report = validate_registry(repo_root, registry_path, schema_path)
    if not authority_report.passed:
        report.errors.append(
            "frozen authority-registry proof failed; Project Application authority resolution "
            "cannot proceed"
        )
        for error in authority_report.errors:
            report.errors.append(f"authority-registry: {error}")
        return None

    report.authority_registry_valid = True

    try:
        with registry_path.open("r", encoding="utf-8") as stream:
            registry = yaml.safe_load(stream)
    except (OSError, UnicodeError, yaml.YAMLError) as exc:
        report.errors.append(
            f"{registry_path.as_posix()}: cannot load validated authority registry: {exc}"
        )
        return None

    records = registry.get("records", []) if isinstance(registry, dict) else []
    return {record["id"]: record for record in records}


def _validate_authority_targets(
    records: list[dict[str, Any]],
    authority_index: dict[str, dict[str, Any]],
    report: ValidationReport,
) -> None:
    errors_before = len(report.errors)

    for index, record in enumerate(records):
        authority_id = record["scaf_authority_id"]
        authority = authority_index.get(authority_id)
        if authority is None:
            report.errors.append(
                f"records[{index}].scaf_authority_id: unresolved frozen SCAF authority {authority_id!r}"
            )
            continue

        authority_class = authority.get("authority_class")
        if authority_class != EXPECTED_AUTHORITY_CLASS:
            report.errors.append(
                f"records[{index}].scaf_authority_id: {authority_id!r} resolves to "
                f"authority_class {authority_class!r}; expected {EXPECTED_AUTHORITY_CLASS!r}"
            )

        expected_source_release = record["scaf_source_release"]
        actual_source_release = authority.get("source_release")
        if actual_source_release != expected_source_release:
            report.errors.append(
                f"records[{index}].scaf_authority_id: {authority_id!r} source_release "
                f"{actual_source_release!r} does not match record scaf_source_release "
                f"{expected_source_release!r}"
            )

    report.authority_resolution_valid = len(report.errors) == errors_before


def validate_project_application(
    repo_root: Path,
    project_application_path: Path | None = None,
) -> ValidationReport:
    """Validate one Project Application YAML document against one SCAF repo root.

    repo_root owns the accepted schema and frozen authority-registry validation
    boundary. project_application_path may point to a project-controlled dataset;
    if omitted, the repository illustrative fixture is validated.
    """

    repo_root = repo_root.resolve()
    if project_application_path is None:
        project_application_path = repo_root / DEFAULT_PROJECT_APPLICATION_PATH
    else:
        project_application_path = project_application_path.resolve()

    report = ValidationReport()
    data = _load_project_application(project_application_path, report)
    if data is None:
        return report

    schema_path = repo_root / PROJECT_APPLICATION_SCHEMA_PATH
    if not _validate_schema(data, schema_path, report):
        return report

    records = data["records"]
    report.record_count = len(records)

    _validate_cross_record_identity(records, report)
    _validate_canonical_order(records, report)

    authority_index = _load_authority_index(repo_root, report)
    if authority_index is not None:
        _validate_authority_targets(records, authority_index, report)

    return report


def _default_repo_root() -> Path:
    return Path(__file__).resolve().parents[2]


def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description=(
            "Validate SCAF Project Application representation conformance. "
            "The canonical schema and frozen authority registry are bound to "
            "this SCAF repository."
        )
    )
    parser.add_argument(
        "--project-application",
        type=Path,
        default=None,
        help=(
            "Project Application YAML to validate. Defaults to "
            "examples/project-application.yaml."
        ),
    )
    return parser


def main(argv: list[str] | None = None) -> int:
    args = _build_parser().parse_args(argv)
    repo_root = _default_repo_root()
    project_path = args.project_application
    if project_path is None:
        project_path = repo_root / DEFAULT_PROJECT_APPLICATION_PATH
    elif not project_path.is_absolute():
        project_path = Path.cwd() / project_path

    report = validate_project_application(repo_root, project_path)

    print(f"Project Application: {project_path.resolve().as_posix()}")
    print(f"Records: {report.record_count}")
    print(f"YAML loader policy:       {'PASS' if report.loader_policy_valid else 'FAIL'}")
    print(f"Schema validation:        {'PASS' if report.schema_valid else 'FAIL'}")
    print(f"Record ID uniqueness:     {'PASS' if report.record_identity_unique else 'FAIL'}")
    print(f"Authority/scope uniqueness: {'PASS' if report.authority_scope_unique else 'FAIL'}")
    print(f"Canonical ordering:       {'PASS' if report.canonical_order_valid else 'FAIL'}")
    print(f"Authority registry proof: {'PASS' if report.authority_registry_valid else 'FAIL'}")
    print(f"Authority target resolution: {'PASS' if report.authority_resolution_valid else 'FAIL'}")
    print(f"Errors: {len(report.errors)}")
    for error in report.errors:
        print(f"ERROR: {error}")
    print(f"REPRESENTATION RESULT: {'PASS' if report.passed else 'FAIL'}")
    return 0 if report.passed else 1


if __name__ == "__main__":  # pragma: no cover - CLI entry point
    sys.exit(main())
