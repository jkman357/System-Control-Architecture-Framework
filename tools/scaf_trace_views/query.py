#!/usr/bin/env python3
"""Produce deterministic read-only L2<->L3 trace views.

Supported public programmatic entry points are query_l2() and query_pattern().
Both own the required trace and authority source-aware repository validation
steps. Internal context and projection helpers are deliberately non-public and
cannot be supplied by a supported caller as a substitute for validation.

The tool does not generate or rewrite authority or trace registries and does
not infer project applicability, recommendation, selection, satisfaction,
compliance, verification, evidence, or closure.
"""

from __future__ import annotations

import argparse
import json
import sys
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

import yaml

from tools.scaf_trace_validator.validator import (
    AUTHORITY_REGISTRY_PATH,
    REGISTRY_PATH,
    RELATION_ORDER,
    UniqueKeyLoader,
    validate_repository,
)
from tools.scaf_validator.validator import validate_registry as validate_authority_registry

__all__ = ("TraceViewError", "query_l2", "query_pattern", "main")

TRACE_VIEW_VERSION = 1
AUTHORITY_SCHEMA_PATH = Path("schemas/authority-registry.schema.json")
RELATION_FIELDS = (
    "pattern_id",
    "relation_type",
    "l2_id",
    "pattern_source_path",
    "pattern_source_field",
    "source_release",
    "qualifier",
)


class TraceViewError(RuntimeError):
    """Raised when a deterministic trace view cannot be produced safely."""


_VALIDATED_CONTEXT_SEAL = object()


@dataclass(frozen=True)
class _ValidatedTraceContext:
    """Internal projection context created only after repository validation."""

    relations: tuple[dict[str, Any], ...]
    authority_ids: frozenset[str]
    pattern_ids: frozenset[str]
    _seal: object = field(repr=False, compare=False)

    def __post_init__(self) -> None:
        if self._seal is not _VALIDATED_CONTEXT_SEAL:
            raise TraceViewError(
                "validated trace context is internal and may only be created after repository validation"
            )


def _load_yaml(path: Path) -> Any:
    with path.open("r", encoding="utf-8") as stream:
        return yaml.load(stream, Loader=UniqueKeyLoader)


def _load_validated_context(repo_root: Path) -> _ValidatedTraceContext:
    repo_root = repo_root.resolve()

    trace_report = validate_repository(repo_root)
    if not trace_report.passed:
        detail = (
            trace_report.errors[0]
            if trace_report.errors
            else "source-aware trace validation failed"
        )
        raise TraceViewError(f"repository trace validation failed: {detail}")

    authority_report = validate_authority_registry(
        repo_root,
        repo_root / AUTHORITY_REGISTRY_PATH,
        repo_root / AUTHORITY_SCHEMA_PATH,
    )
    if not authority_report.passed:
        detail = (
            authority_report.errors[0]
            if authority_report.errors
            else "source-aware authority-registry validation failed"
        )
        raise TraceViewError(f"repository authority validation failed: {detail}")

    registry = _load_yaml(repo_root / REGISTRY_PATH)
    authority = _load_yaml(repo_root / AUTHORITY_REGISTRY_PATH)

    if not isinstance(registry, dict) or not isinstance(registry.get("relations"), list):
        raise TraceViewError("validated trace registry did not expose a relations list")
    if not isinstance(authority, dict) or not isinstance(authority.get("records"), list):
        raise TraceViewError("validated authority registry did not expose a records list")

    relations: list[dict[str, Any]] = []
    for index, relation in enumerate(registry["relations"]):
        if not isinstance(relation, dict):
            raise TraceViewError(f"trace registry relation {index} is not a mapping")
        relations.append({field: relation[field] for field in RELATION_FIELDS})

    authority_ids = frozenset(
        record["id"]
        for record in authority["records"]
        if isinstance(record, dict)
        and isinstance(record.get("id"), str)
        and record.get("authority_class") == "Project-Applicable Obligation"
    )
    pattern_ids = frozenset(relation["pattern_id"] for relation in relations)
    return _ValidatedTraceContext(
        tuple(relations), authority_ids, pattern_ids, _VALIDATED_CONTEXT_SEAL
    )


def _l2_view_key(relation: dict[str, Any]) -> tuple[int, str]:
    return (RELATION_ORDER[relation["relation_type"]], relation["pattern_id"])


def _pattern_view_key(relation: dict[str, Any]) -> tuple[int, str]:
    return (RELATION_ORDER[relation["relation_type"]], relation["l2_id"])


def _build_l2_view(context: _ValidatedTraceContext, l2_id: str) -> dict[str, Any]:
    if l2_id not in context.authority_ids:
        raise TraceViewError(f"unknown or non-project-applicable L2 authority identity: {l2_id}")

    relations = sorted(
        (
            dict(relation)
            for relation in context.relations
            if relation["l2_id"] == l2_id
        ),
        key=_l2_view_key,
    )
    return {
        "trace_view_version": TRACE_VIEW_VERSION,
        "direction": "l2_to_l3",
        "query_id": l2_id,
        "relation_count": len(relations),
        "relations": relations,
    }


def _build_pattern_view(
    context: _ValidatedTraceContext, pattern_id: str
) -> dict[str, Any]:
    if pattern_id not in context.pattern_ids:
        raise TraceViewError(f"unknown frozen Pattern identity: {pattern_id}")

    relations = sorted(
        (
            dict(relation)
            for relation in context.relations
            if relation["pattern_id"] == pattern_id
        ),
        key=_pattern_view_key,
    )
    return {
        "trace_view_version": TRACE_VIEW_VERSION,
        "direction": "l3_to_l2",
        "query_id": pattern_id,
        "relation_count": len(relations),
        "relations": relations,
    }


def query_l2(repo_root: str | Path, l2_id: str) -> dict[str, Any]:
    """Return an L2->L3 view after validating all consumed repository inputs."""
    context = _load_validated_context(Path(repo_root))
    return _build_l2_view(context, l2_id)


def query_pattern(repo_root: str | Path, pattern_id: str) -> dict[str, Any]:
    """Return an L3->L2 view after validating all consumed repository inputs."""
    context = _load_validated_context(Path(repo_root))
    return _build_pattern_view(context, pattern_id)


def _render_text(view: dict[str, Any]) -> str:
    lines = [
        "SCAF L3 Deterministic Trace View",
        f"Direction: {view['direction']}",
        f"Query: {view['query_id']}",
        "Validated source: PASS",
        f"Relations: {view['relation_count']}",
    ]
    if not view["relations"]:
        lines.append(
            "No catalog trace relations are currently recorded for this authority identity."
        )
        return "\n".join(lines)

    current_type: str | None = None
    for relation in view["relations"]:
        if relation["relation_type"] != current_type:
            current_type = relation["relation_type"]
            lines.append("")
            lines.append(f"[{current_type}]")
        counterpart = (
            relation["pattern_id"]
            if view["direction"] == "l2_to_l3"
            else relation["l2_id"]
        )
        lines.append(f"- {counterpart}")
        lines.append(
            f"  qualifier: {relation['qualifier'] if relation['qualifier'] is not None else 'null'}"
        )
        lines.append(
            f"  source: {relation['pattern_source_path']} / {relation['pattern_source_field']}"
        )
        lines.append(f"  source_release: {relation['source_release']}")
    return "\n".join(lines)


def _render_json(view: dict[str, Any]) -> str:
    return json.dumps(view, ensure_ascii=False, indent=2)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description=(
            "Produce deterministic read-only L2<->L3 views only after the repository "
            "passes the SCAF source-aware trace and authority-registry validators."
        )
    )
    parser.add_argument(
        "--repository",
        type=Path,
        default=Path.cwd(),
        help="Repository root to query (default: current working directory).",
    )
    target = parser.add_mutually_exclusive_group(required=True)
    target.add_argument(
        "--l2",
        help="Known frozen Project-Applicable Obligation ID to view from L2 toward L3.",
    )
    target.add_argument(
        "--pattern", help="Known frozen L3 Pattern ID to view toward L2."
    )
    parser.add_argument(
        "--format",
        choices=("text", "json"),
        default="text",
        help="Deterministic stdout format (default: text).",
    )
    args = parser.parse_args(argv)

    try:
        view = (
            query_l2(args.repository, args.l2)
            if args.l2
            else query_pattern(args.repository, args.pattern)
        )
    except (OSError, UnicodeError, yaml.YAMLError, KeyError, TraceViewError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        print("RESULT: FAIL", file=sys.stderr)
        return 1

    rendered = _render_json(view) if args.format == "json" else _render_text(view)
    print(rendered)
    return 0


if __name__ == "__main__":
    sys.exit(main())
