#!/usr/bin/env python3
"""Produce deterministic validated read-only Project Application views.

Supported public programmatic entry points are query_record(),
query_authority(), and query_scope(). Every public query owns the rc07 Project
Application representation/source-aware validation boundary. Callers cannot
supply pre-parsed records or a caller-created validated context as a substitute
for validation.

The tool does not infer applicability, resolve project-controlled scope or
reference targets, recommend/select Patterns, or determine implementation,
verification, compliance, evidence sufficiency, or closure.
"""

from __future__ import annotations

import argparse
import copy
import json
import sys
import tempfile
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

import yaml

from tools.scaf_project_application_validator.validator import (
    AUTHORITY_REGISTRY_PATH,
    AUTHORITY_SCHEMA_PATH,
    DEFAULT_PROJECT_APPLICATION_PATH,
    EXPECTED_AUTHORITY_CLASS,
    StrictProjectApplicationLoader,
    validate_project_application,
)
from tools.scaf_validator.validator import validate_registry

__all__ = (
    "ProjectApplicationViewError",
    "query_record",
    "query_authority",
    "query_scope",
    "main",
)

PROJECT_APPLICATION_VIEW_VERSION = 1
APPLICABILITY_ORDER = ("applicable", "not_applicable", "undetermined")
RECORD_FIELD_ORDER = (
    "record_id",
    "record_kind",
    "representation_release",
    "scaf_authority_id",
    "scaf_source_release",
    "project_scope_ref",
    "applicability",
    "disposition_basis",
    "decision_refs",
    "authority_refs",
    "supporting_refs",
)
DISPOSITION_BASIS_FIELD_ORDER = (
    "summary",
    "basis_refs",
    "unresolved_reason",
    "awaiting_refs",
)


class ProjectApplicationViewError(RuntimeError):
    """Raised when a validated deterministic Project Application view cannot be produced."""


_VALIDATED_CONTEXT_SEAL = object()


@dataclass(frozen=True)
class _ValidatedProjectApplicationContext:
    """Internal immutable projection context created only after rc07 validation."""

    records: tuple[dict[str, Any], ...]
    _seal: object = field(repr=False, compare=False)

    def __post_init__(self) -> None:
        if self._seal is not _VALIDATED_CONTEXT_SEAL:
            raise ProjectApplicationViewError(
                "validated Project Application context is internal and may only be created after validation"
            )


def _require_non_empty_query(value: str, label: str) -> None:
    if not isinstance(value, str) or not value:
        raise ProjectApplicationViewError(f"{label} must be a non-empty string")


def _resolve_project_application_path(
    repo_root: Path,
    project_application_path: str | Path | None,
) -> Path:
    if project_application_path is None:
        return repo_root / DEFAULT_PROJECT_APPLICATION_PATH
    path = Path(project_application_path)
    if not path.is_absolute():
        path = Path.cwd() / path
    return path.resolve()


def _load_validated_context(
    repo_root: Path,
    project_application_path: str | Path | None,
) -> _ValidatedProjectApplicationContext:
    """Validate and consume an immutable snapshot of the selected dataset."""

    repo_root = repo_root.resolve()
    source_path = _resolve_project_application_path(repo_root, project_application_path)
    try:
        source_bytes = source_path.read_bytes()
        source_bytes.decode("utf-8")
    except (OSError, UnicodeError) as exc:
        raise ProjectApplicationViewError(
            f"cannot read Project Application dataset {source_path.as_posix()}: {exc}"
        ) from exc

    # Validate and project from the same private snapshot so a caller cannot
    # change the selected file between validation and consumption.
    with tempfile.TemporaryDirectory(prefix="scaf-pa-view-") as temp_dir:
        snapshot_path = Path(temp_dir) / "project-application.yaml"
        snapshot_path.write_bytes(source_bytes)

        report = validate_project_application(repo_root, snapshot_path)
        if not report.passed:
            detail = report.errors[0] if report.errors else "Project Application validation failed"
            raise ProjectApplicationViewError(
                f"Project Application validation failed: {detail}"
            )

        try:
            data = yaml.load(
                snapshot_path.read_text(encoding="utf-8"),
                Loader=StrictProjectApplicationLoader,
            )
        except (OSError, UnicodeError, yaml.YAMLError) as exc:
            raise ProjectApplicationViewError(
                f"validated Project Application snapshot could not be loaded: {exc}"
            ) from exc

    if not isinstance(data, dict) or not isinstance(data.get("records"), list):
        raise ProjectApplicationViewError(
            "validated Project Application dataset did not expose a records list"
        )

    records: list[dict[str, Any]] = []
    for index, record in enumerate(data["records"]):
        if not isinstance(record, dict):
            raise ProjectApplicationViewError(
                f"validated Project Application record {index} is not a mapping"
            )
        records.append(copy.deepcopy(record))

    return _ValidatedProjectApplicationContext(
        tuple(records), _VALIDATED_CONTEXT_SEAL
    )


def _load_valid_project_applicable_authority_ids(repo_root: Path) -> frozenset[str]:
    """Return the frozen PAO query domain from one source-validated snapshot."""

    registry_path = repo_root / AUTHORITY_REGISTRY_PATH
    schema_path = repo_root / AUTHORITY_SCHEMA_PATH
    try:
        registry_bytes = registry_path.read_bytes()
        registry_bytes.decode("utf-8")
    except (OSError, UnicodeError) as exc:
        raise ProjectApplicationViewError(
            f"cannot read frozen authority registry {registry_path.as_posix()}: {exc}"
        ) from exc

    with tempfile.TemporaryDirectory(prefix="scaf-pa-authority-view-") as temp_dir:
        snapshot_path = Path(temp_dir) / "authority-registry.yaml"
        snapshot_path.write_bytes(registry_bytes)
        report = validate_registry(repo_root, snapshot_path, schema_path)
        if not report.passed:
            detail = report.errors[0] if report.errors else "authority-registry validation failed"
            raise ProjectApplicationViewError(
                f"frozen authority-registry validation failed: {detail}"
            )

        try:
            with snapshot_path.open("r", encoding="utf-8") as stream:
                registry = yaml.safe_load(stream)
        except (OSError, UnicodeError, yaml.YAMLError) as exc:
            raise ProjectApplicationViewError(
                f"validated authority-registry snapshot could not be loaded: {exc}"
            ) from exc

    if not isinstance(registry, dict) or not isinstance(registry.get("records"), list):
        raise ProjectApplicationViewError(
            "validated authority registry did not expose a records list"
        )

    return frozenset(
        record["id"]
        for record in registry["records"]
        if isinstance(record, dict)
        and record.get("authority_class") == EXPECTED_AUTHORITY_CLASS
        and isinstance(record.get("id"), str)
    )


def _applicability_counts(records: list[dict[str, Any]]) -> dict[str, int]:
    return {
        state: sum(1 for record in records if record["applicability"] == state)
        for state in APPLICABILITY_ORDER
    }


def _record_projection(record: dict[str, Any]) -> dict[str, Any]:
    """Return a detached projection with canonical mapping order.

    rc04 makes mapping position non-semantic, so deterministic rc08 JSON must
    not depend on the physical key order used by an otherwise valid YAML input.
    """

    projected: dict[str, Any] = {}
    for field_name in RECORD_FIELD_ORDER:
        value = record[field_name]
        if field_name == "disposition_basis":
            projected[field_name] = {
                member: copy.deepcopy(value[member])
                for member in DISPOSITION_BASIS_FIELD_ORDER
                if member in value
            }
        else:
            projected[field_name] = copy.deepcopy(value)
    return projected


def _build_view(
    query_kind: str,
    query_id: str,
    records: list[dict[str, Any]],
    *,
    scope_resolution: str | None = None,
) -> dict[str, Any]:
    view: dict[str, Any] = {
        "project_application_view_version": PROJECT_APPLICATION_VIEW_VERSION,
        "query_kind": query_kind,
        "query_id": query_id,
        "record_count": len(records),
        "applicability_counts": _applicability_counts(records),
    }
    if scope_resolution is not None:
        view["scope_resolution"] = scope_resolution
    view["records"] = [_record_projection(record) for record in records]
    return view


def _build_record_view(
    context: _ValidatedProjectApplicationContext,
    record_id: str,
) -> dict[str, Any]:
    matches = [record for record in context.records if record["record_id"] == record_id]
    if not matches:
        raise ProjectApplicationViewError(f"unknown Project Application record_id: {record_id}")
    # rc07 validation already proves record_id uniqueness.
    return _build_view("record", record_id, [matches[0]])


def _build_authority_view(
    context: _ValidatedProjectApplicationContext,
    authority_id: str,
) -> dict[str, Any]:
    records = sorted(
        (
            record
            for record in context.records
            if record["scaf_authority_id"] == authority_id
        ),
        key=lambda record: (record["project_scope_ref"], record["record_id"]),
    )
    return _build_view("authority", authority_id, list(records))


def _build_scope_view(
    context: _ValidatedProjectApplicationContext,
    scope_ref: str,
) -> dict[str, Any]:
    records = sorted(
        (
            record
            for record in context.records
            if record["project_scope_ref"] == scope_ref
        ),
        key=lambda record: (record["scaf_authority_id"], record["record_id"]),
    )
    return _build_view(
        "scope",
        scope_ref,
        list(records),
        scope_resolution="not_performed",
    )


def query_record(
    repo_root: str | Path,
    record_id: str,
    project_application_path: str | Path | None = None,
) -> dict[str, Any]:
    """Return one record view only after rc07 validation of the selected dataset."""

    _require_non_empty_query(record_id, "record_id")
    context = _load_validated_context(Path(repo_root), project_application_path)
    return _build_record_view(context, record_id)


def query_authority(
    repo_root: str | Path,
    scaf_authority_id: str,
    project_application_path: str | Path | None = None,
) -> dict[str, Any]:
    """Return all current Project Application records for one frozen PAO identity."""

    _require_non_empty_query(scaf_authority_id, "scaf_authority_id")
    root = Path(repo_root).resolve()
    context = _load_validated_context(root, project_application_path)
    authority_ids = _load_valid_project_applicable_authority_ids(root)
    if scaf_authority_id not in authority_ids:
        raise ProjectApplicationViewError(
            "unknown or non-project-applicable frozen SCAF authority identity: "
            f"{scaf_authority_id}"
        )
    return _build_authority_view(context, scaf_authority_id)


def query_scope(
    repo_root: str | Path,
    project_scope_ref: str,
    project_application_path: str | Path | None = None,
) -> dict[str, Any]:
    """Filter validated records by the exact opaque project_scope_ref string.

    The query does not resolve or prove that the project-controlled scope target
    exists. A zero-record result is valid and remains scope-resolution-neutral.
    """

    _require_non_empty_query(project_scope_ref, "project_scope_ref")
    context = _load_validated_context(Path(repo_root), project_application_path)
    return _build_scope_view(context, project_scope_ref)


def _render_json(view: dict[str, Any]) -> str:
    return json.dumps(view, ensure_ascii=False, indent=2)


def _render_text(view: dict[str, Any]) -> str:
    lines = [
        "SCAF Project Application Validated Read-Only View",
        f"Query kind: {view['query_kind']}",
        f"Query: {view['query_id']}",
        "Validated source: PASS",
        f"Records: {view['record_count']}",
        "Applicability: "
        + ", ".join(
            f"{state}={view['applicability_counts'][state]}"
            for state in APPLICABILITY_ORDER
        ),
    ]
    if "scope_resolution" in view:
        lines.append(f"Scope resolution: {view['scope_resolution']}")

    if not view["records"]:
        lines.append("No matching current Project Application records are recorded.")
        return "\n".join(lines)

    for record in view["records"]:
        lines.extend(
            [
                "",
                f"- {record['record_id']}",
                f"  scaf_authority_id: {record['scaf_authority_id']}",
                f"  project_scope_ref: {record['project_scope_ref']}",
                f"  applicability: {record['applicability']}",
                f"  representation_release: {record['representation_release']}",
                f"  scaf_source_release: {record['scaf_source_release']}",
            ]
        )
    return "\n".join(lines)


def _default_repo_root() -> Path:
    return Path(__file__).resolve().parents[2]


def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description=(
            "Produce deterministic read-only Project Application views only after "
            "the selected dataset passes the rc07 representation/source-aware validator."
        )
    )
    parser.add_argument(
        "--project-application",
        type=Path,
        default=None,
        help=(
            "Project Application YAML to validate/query. Defaults to "
            "examples/project-application.yaml."
        ),
    )
    target = parser.add_mutually_exclusive_group(required=True)
    target.add_argument("--record", help="Project Application record_id to query.")
    target.add_argument(
        "--authority",
        help="Frozen Project-Applicable Obligation identity to query across scopes.",
    )
    target.add_argument(
        "--scope",
        help=(
            "Exact opaque project_scope_ref string to filter. This does not resolve "
            "or prove scope existence."
        ),
    )
    parser.add_argument(
        "--format",
        choices=("text", "json"),
        default="text",
        help="Deterministic stdout format (default: text).",
    )
    return parser


def main(argv: list[str] | None = None) -> int:
    args = _build_parser().parse_args(argv)
    repo_root = _default_repo_root()
    project_path = args.project_application
    if project_path is not None and not project_path.is_absolute():
        project_path = Path.cwd() / project_path

    try:
        if args.record is not None:
            view = query_record(repo_root, args.record, project_path)
        elif args.authority is not None:
            view = query_authority(repo_root, args.authority, project_path)
        else:
            view = query_scope(repo_root, args.scope, project_path)
    except (OSError, UnicodeError, yaml.YAMLError, ProjectApplicationViewError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        print("RESULT: FAIL", file=sys.stderr)
        return 1

    print(_render_json(view) if args.format == "json" else _render_text(view))
    return 0


if __name__ == "__main__":  # pragma: no cover - CLI entry point
    sys.exit(main())
