#!/usr/bin/env python3
"""Produce deterministic read-only L2<->L3 trace views.

The tool consumes only a repository state that first passes the reviewed
source-aware L3 trace validator. It does not generate or rewrite authority or
trace registries and does not infer project applicability, recommendation,
selection, satisfaction, compliance, verification, evidence, or closure.
"""

from __future__ import annotations

import argparse
import json
import sys
from dataclasses import dataclass
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

TRACE_VIEW_VERSION = 1
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


@dataclass(frozen=True)
class TraceContext:
    relations: tuple[dict[str, Any], ...]
    authority_ids: frozenset[str]
    pattern_ids: frozenset[str]


def _load_yaml(path: Path) -> Any:
    with path.open("r", encoding="utf-8") as stream:
        return yaml.load(stream, Loader=UniqueKeyLoader)


def _load_validated_context(repo_root: Path) -> TraceContext:
    repo_root = repo_root.absolute()
    report = validate_repository(repo_root)
    if not report.passed:
        detail = report.errors[0] if report.errors else "source-aware trace validation failed"
        raise TraceViewError(f"repository trace validation failed: {detail}")

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
        # The source-aware validator/schema have already proved the exact shape;
        # this copy keeps the accepted seven-field presentation contract explicit.
        relations.append({field: relation[field] for field in RELATION_FIELDS})

    authority_ids = frozenset(
        record["id"]
        for record in authority["records"]
        if isinstance(record, dict)
        and isinstance(record.get("id"), str)
        and record.get("authority_class") == "Project-Applicable Obligation"
    )
    pattern_ids = frozenset(relation["pattern_id"] for relation in relations)
    return TraceContext(tuple(relations), authority_ids, pattern_ids)


def _l2_view_key(relation: dict[str, Any]) -> tuple[int, str]:
    return (RELATION_ORDER[relation["relation_type"]], relation["pattern_id"])


def _pattern_view_key(relation: dict[str, Any]) -> tuple[int, str]:
    return (RELATION_ORDER[relation["relation_type"]], relation["l2_id"])


def build_l2_view(context: TraceContext, l2_id: str) -> dict[str, Any]:
    """Return the deterministic derived view for one known authority identity."""
    if l2_id not in context.authority_ids:
        raise TraceViewError(f"unknown or non-project-applicable L2 authority identity: {l2_id}")

    relations = sorted(
        (dict(relation) for relation in context.relations if relation["l2_id"] == l2_id),
        key=_l2_view_key,
    )
    return {
        "trace_view_version": TRACE_VIEW_VERSION,
        "direction": "l2_to_l3",
        "query_id": l2_id,
        "relation_count": len(relations),
        "relations": relations,
    }


def build_pattern_view(context: TraceContext, pattern_id: str) -> dict[str, Any]:
    """Return the deterministic derived view for one frozen L3 Pattern identity."""
    if pattern_id not in context.pattern_ids:
        raise TraceViewError(f"unknown frozen Pattern identity: {pattern_id}")

    relations = sorted(
        (dict(relation) for relation in context.relations if relation["pattern_id"] == pattern_id),
        key=_pattern_view_key,
    )
    return {
        "trace_view_version": TRACE_VIEW_VERSION,
        "direction": "l3_to_l2",
        "query_id": pattern_id,
        "relation_count": len(relations),
        "relations": relations,
    }


def _render_text(view: dict[str, Any]) -> str:
    lines = [
        "SCAF L3 Deterministic Trace View",
        f"Direction: {view['direction']}",
        f"Query: {view['query_id']}",
        "Validated source: PASS",
        f"Relations: {view['relation_count']}",
    ]
    if not view["relations"]:
        lines.append("No catalog trace relations are currently recorded for this authority identity.")
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
        lines.append(f"  qualifier: {relation['qualifier'] if relation['qualifier'] is not None else 'null'}")
        lines.append(f"  source: {relation['pattern_source_path']} / {relation['pattern_source_field']}")
        lines.append(f"  source_release: {relation['source_release']}")
    return "\n".join(lines)


def _render_json(view: dict[str, Any]) -> str:
    return json.dumps(view, ensure_ascii=False, indent=2)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description=(
            "Produce deterministic read-only L2<->L3 views only after the repository "
            "passes the SCAF source-aware trace validator."
        )
    )
    parser.add_argument(
        "--repository",
        type=Path,
        default=Path.cwd(),
        help="Repository root to query (default: current working directory).",
    )
    target = parser.add_mutually_exclusive_group(required=True)
    target.add_argument("--l2", help="Known frozen Project-Applicable Obligation ID to view from L2 toward L3.")
    target.add_argument("--pattern", help="Known frozen L3 Pattern ID to view toward L2.")
    parser.add_argument(
        "--format",
        choices=("text", "json"),
        default="text",
        help="Deterministic stdout format (default: text).",
    )
    args = parser.parse_args(argv)

    try:
        context = _load_validated_context(args.repository)
        view = build_l2_view(context, args.l2) if args.l2 else build_pattern_view(context, args.pattern)
    except (OSError, UnicodeError, yaml.YAMLError, KeyError, TraceViewError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        print("RESULT: FAIL", file=sys.stderr)
        return 1

    rendered = _render_json(view) if args.format == "json" else _render_text(view)
    print(rendered)
    return 0


if __name__ == "__main__":
    sys.exit(main())
