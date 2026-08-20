#!/usr/bin/env python3
"""Validate SCAF Controlled Context Package representation/source consistency.

Validation order:
1. capture the package and its exact bound upstream fixture bytes;
2. enforce strict package YAML and canonical raw/list ordering policy;
3. validate the parsed package against the accepted rc04 Draft 2020-12 schema;
4. validate the exact bound Context Source Association Set through the accepted
   source-aware validator, which in turn validates the exact bound Consumption Selection;
5. prove the package's exact upstream SHA/kind/release/scope bindings;
6. reconstruct validated included domain I and prove exact Authority Context Entry coverage;
7. prove package Association Envelope fidelity and package-wide handle uniqueness;
8. prove exactly one same-authority Materialization Decision per accepted association;
9. prove Materialized Context Item identity/reference completeness and orphan absence;
10. prove Controlled Provenance Basis resolution and bidirectional decision/provenance
    correspondence.

A PASS is deterministic package representation/source consistency only. It is not
engineering-context sufficiency, implementation correctness, verification/compliance,
risk acceptance, release readiness, closure, source discovery/currentness, content
loading, ranking/token-budget policy, or AI/model authority.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
import tempfile
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

try:
    import yaml
except ImportError as exc:  # pragma: no cover - CLI environment only
    raise SystemExit(
        "Missing dependency: PyYAML. Install "
        "tools/scaf_controlled_context_package_validator/requirements.txt"
    ) from exc

try:
    from jsonschema import Draft202012Validator
    from jsonschema.exceptions import SchemaError
except ImportError as exc:  # pragma: no cover - CLI environment only
    raise SystemExit(
        "Missing dependency: jsonschema. Install "
        "tools/scaf_controlled_context_package_validator/requirements.txt"
    ) from exc

from tools.scaf_context_source_association_validator.validator import (
    validate_context_source_associations,
)

__all__ = (
    "ValidationReport",
    "validate_controlled_context_package",
    "main",
)

DEFAULT_PACKAGE_PATH = Path("examples/controlled-context-package.yaml")
DEFAULT_ASSOCIATIONS_PATH = Path("examples/context-source-associations.yaml")
DEFAULT_SELECTION_PATH = Path("examples/consumption-selection.yaml")
DEFAULT_PROFILE_PATH = Path("examples/effective-project-profile.yaml")
DEFAULT_PROJECT_APPLICATION_PATH = Path("examples/project-application.yaml")
PACKAGE_SCHEMA_PATH = Path("schemas/controlled-context-package.schema.json")

ROOT_FIELD_ORDER = (
    "package_kind",
    "representation_release",
    "upstream_binding",
    "assembly_objective",
    "authority_context_entries",
    "materialized_context_items",
)
UPSTREAM_BINDING_FIELD_ORDER = (
    "consumption_selection",
    "context_source_association_set",
)
SELECTION_BINDING_FIELD_ORDER = (
    "source_sha256",
    "selection_kind",
    "representation_release",
    "project_scope_ref",
)
ASSOCIATION_SET_BINDING_FIELD_ORDER = (
    "source_sha256",
    "association_set_kind",
    "representation_release",
    "consumption_selection_source_sha256",
    "project_scope_ref",
)
ASSEMBLY_OBJECTIVE_FIELD_ORDER = (
    "objective_id",
    "objective_statement",
)
AUTHORITY_CONTEXT_ENTRY_FIELD_ORDER = (
    "scaf_authority_id",
    "association_envelope",
    "materialization_decisions",
)
ASSOCIATION_ENVELOPE_ENTRY_FIELD_ORDER = (
    "association_handle",
    "controlled_association",
)
ASSOCIATION_FIELD_ORDER = (
    "source_unit_ref",
    "relationship_semantic",
    "relationship_scope_ref",
    "association_provenance",
    "authority_qualification",
    "instance_constraint",
)
PROVENANCE_FIELD_ORDER = (
    "assertion_kind",
    "basis_refs",
)
AUTHORITY_QUALIFICATION_FIELD_ORDER = (
    "qualification_kind",
    "authority_scope_ref",
    "authority_basis_refs",
)
INSTANCE_CONSTRAINT_FIELD_ORDER = (
    "constraint_kind",
    "value",
)
MATERIALIZED_DECISION_FIELD_ORDER = (
    "association_handle",
    "outcome",
    "materialized_context_item_refs",
)
NOT_MATERIALIZED_DECISION_FIELD_ORDER = (
    "association_handle",
    "outcome",
    "materialized_context_item_refs",
    "non_materialization_basis",
)
MATERIALIZED_CONTEXT_ITEM_FIELD_ORDER = (
    "materialized_context_item_id",
    "context_semantic",
    "controlled_provenance_bases",
    "payload",
)
CONTROLLED_PROVENANCE_BASIS_FIELD_ORDER = (
    "scaf_authority_id",
    "association_handle",
)
PAYLOAD_FIELD_ORDER = (
    "payload_kind",
    "source_identity_ref",
)


class StrictControlledContextPackageLoader(yaml.SafeLoader):
    """Safe loader rejecting ambiguous Controlled Context Package mappings."""


def _construct_mapping(
    loader: StrictControlledContextPackageLoader,
    node: yaml.MappingNode,
    deep: bool = False,
) -> dict[str, Any]:
    mapping: dict[str, Any] = {}
    for key_node, value_node in node.value:
        if getattr(key_node, "value", None) == "<<":
            raise yaml.constructor.ConstructorError(
                "while constructing a mapping",
                node.start_mark,
                "YAML merge keys are prohibited by the Controlled Context Package contract",
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


StrictControlledContextPackageLoader.add_constructor(
    yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG,
    _construct_mapping,
)


@dataclass
class ValidationReport:
    errors: list[str] = field(default_factory=list)
    loader_policy_valid: bool = False
    schema_valid: bool = False
    canonical_order_valid: bool = False
    upstream_association_validation_valid: bool = False
    upstream_binding_valid: bool = False
    authority_domain_valid: bool = False
    association_fidelity_valid: bool = False
    decision_accounting_valid: bool = False
    item_reference_valid: bool = False
    provenance_valid: bool = False
    included_authority_count: int = 0
    association_handle_count: int = 0
    materialization_decision_count: int = 0
    materialized_context_item_count: int = 0
    provenance_basis_count: int = 0

    @property
    def passed(self) -> bool:
        return not self.errors


def _resolve_input_path(repo_root: Path, path: Path | None, default: Path) -> Path:
    if path is None:
        return (repo_root / default).resolve()
    if path.is_absolute():
        return path.resolve()
    return (Path.cwd() / path).resolve()


def _read_required_bytes(path: Path, label: str, report: ValidationReport) -> bytes | None:
    try:
        data = path.read_bytes()
        data.decode("utf-8")
        return data
    except (OSError, UnicodeError) as exc:
        report.errors.append(f"{label}: cannot read UTF-8 source {path.as_posix()}: {exc}")
        return None


def _schema_path(error: Any) -> str:
    if not error.absolute_path:
        return "$"
    parts = ["$"]
    for part in error.absolute_path:
        parts.append(f"[{part}]" if isinstance(part, int) else f".{part}")
    return "".join(parts)


def _scan_yaml_policy(text: str, source_label: str, report: ValidationReport) -> bool:
    errors_before = len(report.errors)
    document_count = 0
    try:
        for event in yaml.parse(text):
            if isinstance(event, yaml.events.DocumentStartEvent):
                document_count += 1
            if isinstance(event, yaml.events.AliasEvent):
                report.errors.append(f"{source_label}: YAML aliases are prohibited")
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
    return len(report.errors) == errors_before


def _validate_scalar_style(
    node: yaml.Node,
    report: ValidationReport,
    path: str = "$",
    *,
    is_mapping_key: bool = False,
) -> None:
    if isinstance(node, yaml.ScalarNode):
        if not is_mapping_key and node.tag == "tag:yaml.org,2002:str":
            if node.style not in ("'", '"'):
                report.errors.append(
                    f"{path}: canonical Controlled Context Package string scalar must be quoted"
                )
        return
    if isinstance(node, yaml.SequenceNode):
        for index, child in enumerate(node.value):
            _validate_scalar_style(child, report, f"{path}[{index}]")
        return
    if isinstance(node, yaml.MappingNode):
        for key_node, value_node in node.value:
            key_label = getattr(key_node, "value", "?")
            _validate_scalar_style(
                key_node,
                report,
                f"{path}.<key:{key_label}>",
                is_mapping_key=True,
            )
            _validate_scalar_style(value_node, report, f"{path}.{key_label}")


def _load_package_snapshot(path: Path, report: ValidationReport) -> Any | None:
    source_label = path.as_posix()
    try:
        raw = path.read_bytes()
        text = raw.decode("utf-8")
    except (OSError, UnicodeError) as exc:
        report.errors.append(f"{source_label}: cannot read Controlled Context Package YAML: {exc}")
        return None
    if b"\r" in raw:
        report.errors.append(f"{source_label}: canonical package must use LF line endings")
        return None
    if not _scan_yaml_policy(text, source_label, report):
        return None
    try:
        nodes = list(yaml.compose_all(text, Loader=yaml.SafeLoader))
    except yaml.YAMLError as exc:
        report.errors.append(f"{source_label}: YAML node composition failed: {exc}")
        return None
    if len(nodes) != 1 or nodes[0] is None:
        report.errors.append(f"{source_label}: expected exactly one non-empty YAML document")
        return None
    _validate_scalar_style(nodes[0], report)
    if report.errors:
        return None
    try:
        data = yaml.load(text, Loader=StrictControlledContextPackageLoader)
    except yaml.YAMLError as exc:
        report.errors.append(f"{source_label}: YAML loader-policy validation failed: {exc}")
        return None
    report.loader_policy_valid = True
    return data


def _load_json_bytes(data: bytes, source_label: str, report: ValidationReport) -> Any | None:
    try:
        return json.loads(data.decode("utf-8"))
    except (UnicodeError, json.JSONDecodeError) as exc:
        report.errors.append(f"{source_label}: cannot load JSON: {exc}")
        return None


def _validate_schema(
    package_data: Any,
    schema_bytes: bytes,
    schema_label: str,
    report: ValidationReport,
) -> bool:
    schema = _load_json_bytes(schema_bytes, schema_label, report)
    if schema is None:
        return False
    try:
        Draft202012Validator.check_schema(schema)
    except SchemaError as exc:
        report.errors.append(
            f"{schema_label}: invalid JSON Schema Draft 2020-12 contract: {exc.message}"
        )
        return False
    validator = Draft202012Validator(schema)
    errors = sorted(
        validator.iter_errors(package_data),
        key=lambda error: (list(error.absolute_path), error.message),
    )
    if errors:
        for error in errors:
            report.errors.append(
                f"Controlled Context Package schema: {_schema_path(error)}: {error.message}"
            )
        return False
    report.schema_valid = True
    return True


def _expected_association_field_order(association: dict[str, Any]) -> tuple[str, ...]:
    return tuple(field for field in ASSOCIATION_FIELD_ORDER if field in association)


def _authority_qualification_key(association: dict[str, Any]) -> tuple[Any, ...]:
    qualification = association.get("authority_qualification")
    if qualification is None:
        return ("", "", ())
    return (
        qualification["qualification_kind"],
        qualification["authority_scope_ref"],
        tuple(qualification["authority_basis_refs"]),
    )


def _instance_constraint_key(association: dict[str, Any]) -> tuple[str, str]:
    constraint = association.get("instance_constraint")
    if constraint is None:
        return ("", "")
    return (constraint["constraint_kind"], constraint["value"])


def _association_semantic_key(association: dict[str, Any]) -> tuple[Any, ...]:
    return (
        association["source_unit_ref"],
        association["relationship_semantic"],
        association["relationship_scope_ref"],
        _authority_qualification_key(association),
        _instance_constraint_key(association),
    )


def _validate_projected_association_order(
    association: dict[str, Any],
    path: str,
    report: ValidationReport,
) -> None:
    if tuple(association.keys()) != _expected_association_field_order(association):
        report.errors.append(f"{path}: non-canonical controlled_association mapping order")
    provenance = association["association_provenance"]
    if tuple(provenance.keys()) != PROVENANCE_FIELD_ORDER:
        report.errors.append(f"{path}.association_provenance: non-canonical mapping order")
    if provenance["basis_refs"] != sorted(provenance["basis_refs"]):
        report.errors.append(f"{path}.association_provenance.basis_refs: non-canonical order")
    if "authority_qualification" in association:
        qualification = association["authority_qualification"]
        if tuple(qualification.keys()) != AUTHORITY_QUALIFICATION_FIELD_ORDER:
            report.errors.append(f"{path}.authority_qualification: non-canonical mapping order")
        if qualification["authority_basis_refs"] != sorted(
            qualification["authority_basis_refs"]
        ):
            report.errors.append(
                f"{path}.authority_qualification.authority_basis_refs: non-canonical order"
            )
    if "instance_constraint" in association:
        constraint = association["instance_constraint"]
        if tuple(constraint.keys()) != INSTANCE_CONSTRAINT_FIELD_ORDER:
            report.errors.append(f"{path}.instance_constraint: non-canonical mapping order")


def _validate_canonical_order(data: dict[str, Any], report: ValidationReport) -> None:
    errors_before = len(report.errors)
    if tuple(data.keys()) != ROOT_FIELD_ORDER:
        report.errors.append(
            "package root: non-canonical mapping order; expected " + ", ".join(ROOT_FIELD_ORDER)
        )
    upstream = data["upstream_binding"]
    if tuple(upstream.keys()) != UPSTREAM_BINDING_FIELD_ORDER:
        report.errors.append("upstream_binding: non-canonical mapping order")
    selection_binding = upstream["consumption_selection"]
    if tuple(selection_binding.keys()) != SELECTION_BINDING_FIELD_ORDER:
        report.errors.append("upstream_binding.consumption_selection: non-canonical mapping order")
    association_binding = upstream["context_source_association_set"]
    if tuple(association_binding.keys()) != ASSOCIATION_SET_BINDING_FIELD_ORDER:
        report.errors.append(
            "upstream_binding.context_source_association_set: non-canonical mapping order"
        )
    objective = data["assembly_objective"]
    if tuple(objective.keys()) != ASSEMBLY_OBJECTIVE_FIELD_ORDER:
        report.errors.append("assembly_objective: non-canonical mapping order")

    entries = data["authority_context_entries"]
    authority_ids = [entry["scaf_authority_id"] for entry in entries]
    if authority_ids != sorted(authority_ids):
        report.errors.append("authority_context_entries: non-canonical scaf_authority_id order")
    for entry_index, entry in enumerate(entries):
        prefix = f"authority_context_entries[{entry_index}]"
        if tuple(entry.keys()) != AUTHORITY_CONTEXT_ENTRY_FIELD_ORDER:
            report.errors.append(f"{prefix}: non-canonical mapping order")
        envelope = entry["association_envelope"]
        semantic_keys = [
            _association_semantic_key(item["controlled_association"]) for item in envelope
        ]
        if semantic_keys != sorted(semantic_keys):
            report.errors.append(f"{prefix}.association_envelope: non-canonical semantic order")
        for association_index, envelope_item in enumerate(envelope):
            apath = f"{prefix}.association_envelope[{association_index}]"
            if tuple(envelope_item.keys()) != ASSOCIATION_ENVELOPE_ENTRY_FIELD_ORDER:
                report.errors.append(f"{apath}: non-canonical mapping order")
            _validate_projected_association_order(
                envelope_item["controlled_association"],
                f"{apath}.controlled_association",
                report,
            )
        decisions = entry["materialization_decisions"]
        if [decision["association_handle"] for decision in decisions] != [
            item["association_handle"] for item in envelope
        ]:
            report.errors.append(
                f"{prefix}.materialization_decisions: non-canonical association-envelope order"
            )
        for decision_index, decision in enumerate(decisions):
            dpath = f"{prefix}.materialization_decisions[{decision_index}]"
            expected = (
                MATERIALIZED_DECISION_FIELD_ORDER
                if decision["outcome"] == "materialized"
                else NOT_MATERIALIZED_DECISION_FIELD_ORDER
            )
            if tuple(decision.keys()) != expected:
                report.errors.append(f"{dpath}: non-canonical mapping order")
            refs = decision["materialized_context_item_refs"]
            if refs != sorted(refs):
                report.errors.append(f"{dpath}.materialized_context_item_refs: non-canonical order")

    items = data["materialized_context_items"]
    item_ids = [item["materialized_context_item_id"] for item in items]
    if item_ids != sorted(item_ids):
        report.errors.append("materialized_context_items: non-canonical item-ID order")
    for item_index, item in enumerate(items):
        ipath = f"materialized_context_items[{item_index}]"
        if tuple(item.keys()) != MATERIALIZED_CONTEXT_ITEM_FIELD_ORDER:
            report.errors.append(f"{ipath}: non-canonical mapping order")
        bases = item["controlled_provenance_bases"]
        basis_keys = [(basis["scaf_authority_id"], basis["association_handle"]) for basis in bases]
        if basis_keys != sorted(basis_keys):
            report.errors.append(f"{ipath}.controlled_provenance_bases: non-canonical order")
        for basis_index, basis in enumerate(bases):
            if tuple(basis.keys()) != CONTROLLED_PROVENANCE_BASIS_FIELD_ORDER:
                report.errors.append(
                    f"{ipath}.controlled_provenance_bases[{basis_index}]: non-canonical mapping order"
                )
        if tuple(item["payload"].keys()) != PAYLOAD_FIELD_ORDER:
            report.errors.append(f"{ipath}.payload: non-canonical mapping order")
    report.canonical_order_valid = len(report.errors) == errors_before


def _load_validated_yaml(path: Path, label: str, report: ValidationReport) -> dict[str, Any] | None:
    try:
        data = yaml.safe_load(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, yaml.YAMLError) as exc:
        report.errors.append(f"{label}: cannot reload accepted upstream YAML {path.as_posix()}: {exc}")
        return None
    if not isinstance(data, dict):
        report.errors.append(f"{label}: accepted upstream root is not a mapping")
        return None
    return data


def _prove_upstream_binding(
    package: dict[str, Any],
    selection: dict[str, Any],
    selection_bytes: bytes,
    associations: dict[str, Any],
    association_bytes: bytes,
    report: ValidationReport,
) -> None:
    errors_before = len(report.errors)
    upstream = package["upstream_binding"]
    selection_binding = upstream["consumption_selection"]
    expected_selection_sha = hashlib.sha256(selection_bytes).hexdigest()
    observed_selection_values = {
        "source_sha256": expected_selection_sha,
        "selection_kind": selection["selection_kind"],
        "representation_release": selection["representation_release"],
        "project_scope_ref": selection["source_profile_binding"]["project_scope_ref"],
    }
    for field, expected in observed_selection_values.items():
        if selection_binding[field] != expected:
            report.errors.append(
                f"upstream_binding.consumption_selection.{field}: recorded {selection_binding[field]!r}, observed {expected!r}"
            )

    association_binding = upstream["context_source_association_set"]
    expected_association_sha = hashlib.sha256(association_bytes).hexdigest()
    observed_association_values = {
        "source_sha256": expected_association_sha,
        "association_set_kind": associations["association_set_kind"],
        "representation_release": associations["representation_release"],
        "consumption_selection_source_sha256": associations["source_selection_binding"][
            "consumption_selection_source_sha256"
        ],
        "project_scope_ref": associations["source_selection_binding"]["project_scope_ref"],
    }
    for field, expected in observed_association_values.items():
        if association_binding[field] != expected:
            report.errors.append(
                f"upstream_binding.context_source_association_set.{field}: recorded {association_binding[field]!r}, observed {expected!r}"
            )
    if association_binding["consumption_selection_source_sha256"] != selection_binding["source_sha256"]:
        report.errors.append(
            "upstream_binding: Context Source Association nested selection SHA does not equal package Consumption Selection SHA"
        )
    report.upstream_binding_valid = len(report.errors) == errors_before


def _prove_authority_association_and_decisions(
    package: dict[str, Any],
    selection: dict[str, Any],
    associations: dict[str, Any],
    report: ValidationReport,
) -> tuple[dict[tuple[str, str], dict[str, Any]], dict[tuple[str, str], dict[str, Any]]]:
    validated_i = [entry["scaf_authority_id"] for entry in selection["selected_entries"]]
    report.included_authority_count = len(validated_i)
    entries = package["authority_context_entries"]

    domain_errors_before = len(report.errors)
    package_ids = [entry["scaf_authority_id"] for entry in entries]
    if len(package_ids) != len(set(package_ids)):
        report.errors.append("authority_context_entries: duplicate scaf_authority_id")
    if package_ids != validated_i:
        report.errors.append(
            f"authority_context_entries domain/order does not equal validated I exactly: package {package_ids!r}, validated I {validated_i!r}"
        )
    report.authority_domain_valid = len(report.errors) == domain_errors_before

    upstream_by_authority = {
        entry["scaf_authority_id"]: entry["associations"]
        for entry in associations["authority_source_entries"]
    }
    handle_lookup: dict[tuple[str, str], dict[str, Any]] = {}
    decision_lookup: dict[tuple[str, str], dict[str, Any]] = {}
    global_handles: set[str] = set()

    fidelity_errors_before = len(report.errors)
    for entry in entries:
        authority_id = entry["scaf_authority_id"]
        envelope = entry["association_envelope"]
        projected = [item["controlled_association"] for item in envelope]
        upstream_associations = upstream_by_authority.get(authority_id)
        if upstream_associations is None:
            report.errors.append(
                f"authority {authority_id}: no accepted upstream Authority Source Entry exists"
            )
            upstream_associations = []
        if projected != upstream_associations:
            report.errors.append(
                f"authority {authority_id}: Association Envelope does not exactly match accepted upstream association list"
            )
        for item in envelope:
            handle = item["association_handle"]
            if handle in global_handles:
                report.errors.append(f"association_handle {handle!r}: duplicate package-local handle")
            global_handles.add(handle)
            handle_lookup[(authority_id, handle)] = item["controlled_association"]
    report.association_handle_count = len(global_handles)
    report.association_fidelity_valid = len(report.errors) == fidelity_errors_before

    decision_errors_before = len(report.errors)
    for entry in entries:
        authority_id = entry["scaf_authority_id"]
        handles = [item["association_handle"] for item in entry["association_envelope"]]
        decisions = entry["materialization_decisions"]
        decision_handles = [decision["association_handle"] for decision in decisions]
        if decision_handles != handles:
            report.errors.append(
                f"authority {authority_id}: Materialization Decision handles/order do not equal Association Envelope handles exactly"
            )
        if len(decision_handles) != len(set(decision_handles)):
            report.errors.append(f"authority {authority_id}: duplicate Materialization Decision handle")
        for decision in decisions:
            key = (authority_id, decision["association_handle"])
            if key not in handle_lookup:
                report.errors.append(
                    f"authority {authority_id}: Materialization Decision references non-resolving or cross-entry association handle {decision['association_handle']!r}"
                )
            if key in decision_lookup:
                report.errors.append(
                    f"authority {authority_id}: more than one Materialization Decision for handle {decision['association_handle']!r}"
                )
            decision_lookup[key] = decision
    report.materialization_decision_count = sum(
        len(entry["materialization_decisions"]) for entry in entries
    )
    report.decision_accounting_valid = len(report.errors) == decision_errors_before
    return handle_lookup, decision_lookup


def _prove_items_and_provenance(
    package: dict[str, Any],
    handle_lookup: dict[tuple[str, str], dict[str, Any]],
    decision_lookup: dict[tuple[str, str], dict[str, Any]],
    report: ValidationReport,
) -> None:
    item_errors_before = len(report.errors)
    items = package["materialized_context_items"]
    item_ids = [item["materialized_context_item_id"] for item in items]
    if len(item_ids) != len(set(item_ids)):
        report.errors.append("materialized_context_items: duplicate materialized_context_item_id")
    item_index: dict[str, dict[str, Any]] = {}
    for item in items:
        item_id = item["materialized_context_item_id"]
        if item_id not in item_index:
            item_index[item_id] = item

    referenced_ids: set[str] = set()
    for key, decision in decision_lookup.items():
        for item_ref in decision["materialized_context_item_refs"]:
            referenced_ids.add(item_ref)
            if item_ref not in item_index:
                report.errors.append(
                    f"Materialization Decision {key!r}: materialized_context_item_ref {item_ref!r} does not resolve"
                )
    orphan_ids = set(item_index) - referenced_ids
    if orphan_ids:
        report.errors.append(
            "materialized_context_items: orphan item IDs not referenced by any Materialization Decision: "
            + ", ".join(sorted(orphan_ids))
        )
    report.materialized_context_item_count = len(items)
    report.item_reference_valid = len(report.errors) == item_errors_before

    provenance_errors_before = len(report.errors)
    basis_count = 0
    for item in items:
        item_id = item["materialized_context_item_id"]
        basis_keys: list[tuple[str, str]] = []
        for basis in item["controlled_provenance_bases"]:
            basis_count += 1
            key = (basis["scaf_authority_id"], basis["association_handle"])
            basis_keys.append(key)
            if key not in handle_lookup:
                report.errors.append(
                    f"Materialized Context Item {item_id!r}: provenance basis {key!r} does not resolve to an accepted package association"
                )
                continue
            decision = decision_lookup.get(key)
            if decision is None or decision["outcome"] != "materialized" or item_id not in decision[
                "materialized_context_item_refs"
            ]:
                report.errors.append(
                    f"Materialized Context Item {item_id!r}: provenance basis {key!r} has no corresponding materialized decision reference"
                )
        basis_set = set(basis_keys)
        for key, decision in decision_lookup.items():
            if item_id in decision["materialized_context_item_refs"] and key not in basis_set:
                report.errors.append(
                    f"Materialized Context Item {item_id!r}: decision reference from {key!r} lacks matching Controlled Provenance Basis"
                )
    report.provenance_basis_count = basis_count
    report.provenance_valid = len(report.errors) == provenance_errors_before


def validate_controlled_context_package(
    repo_root: Path,
    package_path: Path | None = None,
    associations_path: Path | None = None,
    selection_path: Path | None = None,
    profile_path: Path | None = None,
    project_application_path: Path | None = None,
) -> ValidationReport:
    """Validate one Controlled Context Package against exact accepted upstream truth.

    Callers may select project-side package/association/selection/profile/application inputs.
    The package schema and accepted repository-owned upstream validation implementations remain
    fixed to the reviewed repository. This function performs no source discovery, content loading,
    currentness judgment, ranking/token-budget policy, or engineering-sufficiency judgment.
    """

    repo_root = repo_root.resolve()
    package_path = _resolve_input_path(repo_root, package_path, DEFAULT_PACKAGE_PATH)
    associations_path = _resolve_input_path(repo_root, associations_path, DEFAULT_ASSOCIATIONS_PATH)
    selection_path = _resolve_input_path(repo_root, selection_path, DEFAULT_SELECTION_PATH)
    profile_path = _resolve_input_path(repo_root, profile_path, DEFAULT_PROFILE_PATH)
    project_application_path = _resolve_input_path(
        repo_root, project_application_path, DEFAULT_PROJECT_APPLICATION_PATH
    )

    report = ValidationReport()
    package_bytes = _read_required_bytes(package_path, "Controlled Context Package", report)
    association_bytes = _read_required_bytes(
        associations_path, "Context Source Associations", report
    )
    selection_bytes = _read_required_bytes(selection_path, "Consumption Selection", report)
    schema_bytes = _read_required_bytes(
        repo_root / PACKAGE_SCHEMA_PATH, "Controlled Context Package schema", report
    )
    if None in (package_bytes, association_bytes, selection_bytes, schema_bytes):
        return report

    with tempfile.TemporaryDirectory(prefix="scaf-controlled-context-package-validator-") as temp_dir:
        temp_root = Path(temp_dir)
        package_snapshot = temp_root / "controlled-context-package.yaml"
        association_snapshot = temp_root / "context-source-associations.yaml"
        selection_snapshot = temp_root / "consumption-selection.yaml"
        package_snapshot.write_bytes(package_bytes)
        association_snapshot.write_bytes(association_bytes)
        selection_snapshot.write_bytes(selection_bytes)

        package_data = _load_package_snapshot(package_snapshot, report)
        if package_data is None:
            return report
        if not _validate_schema(
            package_data,
            schema_bytes,
            (repo_root / PACKAGE_SCHEMA_PATH).as_posix(),
            report,
        ):
            return report
        if not isinstance(package_data, dict):
            report.errors.append("Controlled Context Package root is not a mapping")
            return report
        _validate_canonical_order(package_data, report)

        upstream_report = validate_context_source_associations(
            repo_root,
            association_snapshot,
            selection_snapshot,
            profile_path,
            project_application_path,
        )
        if not upstream_report.passed:
            report.errors.append(
                "bound Context Source Association Set failed accepted source-aware validation; Controlled Context Package source proof cannot proceed"
            )
            for error in upstream_report.errors:
                report.errors.append(f"Context Source Association: {error}")
            return report
        report.upstream_association_validation_valid = True

        selection_data = _load_validated_yaml(
            selection_snapshot, "Consumption Selection", report
        )
        association_data = _load_validated_yaml(
            association_snapshot, "Context Source Association Set", report
        )
        if selection_data is None or association_data is None:
            return report

        _prove_upstream_binding(
            package_data,
            selection_data,
            selection_bytes,
            association_data,
            association_bytes,
            report,
        )
        handle_lookup, decision_lookup = _prove_authority_association_and_decisions(
            package_data, selection_data, association_data, report
        )
        _prove_items_and_provenance(
            package_data, handle_lookup, decision_lookup, report
        )

    return report


def _default_repo_root() -> Path:
    return Path(__file__).resolve().parents[2]


def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description=(
            "Validate SCAF Controlled Context Package representation/source consistency. "
            "Repository-owned schema and accepted upstream validators remain fixed to this reviewed SCAF repository."
        )
    )
    parser.add_argument("--package", type=Path, help="Controlled Context Package YAML path")
    parser.add_argument("--associations", type=Path, help="bound Context Source Association YAML path")
    parser.add_argument("--selection", type=Path, help="bound Consumption Selection YAML path")
    parser.add_argument("--profile", type=Path, help="bound Effective Project Profile YAML path")
    parser.add_argument(
        "--project-application", type=Path, help="bound Project Application YAML path"
    )
    return parser


def _print_report(report: ValidationReport) -> None:
    print("SCAF Controlled Context Package Source-Aware Validator")
    print("------------------------------------------------------")
    print(f"YAML loader policy:          {'PASS' if report.loader_policy_valid else 'FAIL'}")
    print(f"Schema validation:           {'PASS' if report.schema_valid else 'FAIL'}")
    print(f"Canonical ordering:          {'PASS' if report.canonical_order_valid else 'FAIL'}")
    print(
        f"Upstream association valid:  {'PASS' if report.upstream_association_validation_valid else 'FAIL'}"
    )
    print(f"Upstream binding proof:      {'PASS' if report.upstream_binding_valid else 'FAIL'}")
    print(f"Validated-I coverage:        {'PASS' if report.authority_domain_valid else 'FAIL'}")
    print(f"Association fidelity:        {'PASS' if report.association_fidelity_valid else 'FAIL'}")
    print(f"Decision accounting:         {'PASS' if report.decision_accounting_valid else 'FAIL'}")
    print(f"Item reference integrity:    {'PASS' if report.item_reference_valid else 'FAIL'}")
    print(f"Provenance correspondence:   {'PASS' if report.provenance_valid else 'FAIL'}")
    print(f"Included authorities:        {report.included_authority_count}")
    print(f"Association handles:         {report.association_handle_count}")
    print(f"Materialization decisions:   {report.materialization_decision_count}")
    print(f"Materialized context items:  {report.materialized_context_item_count}")
    print(f"Controlled provenance bases: {report.provenance_basis_count}")
    print(f"Errors: {len(report.errors)}")
    for error in report.errors:
        print(f"ERROR: {error}")
    print("CONTROLLED CONTEXT PACKAGE SOURCE RESULT: " + ("PASS" if report.passed else "FAIL"))


def main(argv: list[str] | None = None) -> int:
    args = _build_parser().parse_args(argv)
    report = validate_controlled_context_package(
        _default_repo_root(),
        args.package,
        args.associations,
        args.selection,
        args.profile,
        args.project_application,
    )
    _print_report(report)
    return 0 if report.passed else 1


if __name__ == "__main__":
    sys.exit(main())
