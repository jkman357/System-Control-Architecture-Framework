#!/usr/bin/env python3
"""Validate SCAF Context Source Association representation/source consistency.

Validation order:
1. capture the Context Source Association and bound Consumption Selection bytes;
2. enforce the accepted raw-YAML and canonical-order policy;
3. validate the parsed association set against the accepted rc04 Draft 2020-12 schema;
4. prove the exact bound Consumption Selection SHA/kind/release/scope;
5. validate that exact Consumption Selection through the accepted source-aware validator;
6. reconstruct validated included domain I and prove complete Authority Source Entry coverage;
7. prove Source Unit identity/reference completeness and semantic association uniqueness;
8. prove canonical list/order requirements;
9. where an association carries a SHA-256 instance constraint over a bounded repository-local
   ``repo:`` Source Identity, prove the exact repository bytes match that constraint.

A PASS is representation/source-association consistency only. It is not general source
resolution/discovery, source currentness, engineering applicability, Project Design Authority,
obligation satisfaction, verification/compliance, risk acceptance, release readiness, closure,
or Context Assembly.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
import tempfile
from dataclasses import dataclass, field
from pathlib import Path, PurePosixPath
from typing import Any

try:
    import yaml
except ImportError as exc:  # pragma: no cover - CLI environment only
    raise SystemExit(
        "Missing dependency: PyYAML. Install "
        "tools/scaf_context_source_association_validator/requirements.txt"
    ) from exc

try:
    from jsonschema import Draft202012Validator
    from jsonschema.exceptions import SchemaError
except ImportError as exc:  # pragma: no cover - CLI environment only
    raise SystemExit(
        "Missing dependency: jsonschema. Install "
        "tools/scaf_context_source_association_validator/requirements.txt"
    ) from exc

from tools.scaf_consumption_selection_validator.validator import (
    StrictConsumptionSelectionLoader,
    validate_consumption_selection,
)

__all__ = (
    "ValidationReport",
    "validate_context_source_associations",
    "main",
)

DEFAULT_ASSOCIATIONS_PATH = Path("examples/context-source-associations.yaml")
DEFAULT_SELECTION_PATH = Path("examples/consumption-selection.yaml")
DEFAULT_PROFILE_PATH = Path("examples/effective-project-profile.yaml")
DEFAULT_PROJECT_APPLICATION_PATH = Path("examples/project-application.yaml")
ASSOCIATION_SCHEMA_PATH = Path("schemas/context-source-associations.schema.json")

ROOT_FIELD_ORDER = (
    "association_set_kind",
    "representation_release",
    "source_selection_binding",
    "source_units",
    "authority_source_entries",
)
SELECTION_BINDING_FIELD_ORDER = (
    "consumption_selection_source_sha256",
    "selection_kind",
    "selection_representation_release",
    "project_scope_ref",
)
SOURCE_UNIT_FIELD_ORDER = (
    "source_unit_id",
    "source_identity_ref",
    "control_domain",
)
AUTHORITY_SOURCE_ENTRY_FIELD_ORDER = (
    "scaf_authority_id",
    "associations",
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


class StrictContextSourceAssociationLoader(yaml.SafeLoader):
    """Safe loader rejecting ambiguous Context Source Association mappings."""


def _construct_mapping(
    loader: StrictContextSourceAssociationLoader,
    node: yaml.MappingNode,
    deep: bool = False,
) -> dict[str, Any]:
    mapping: dict[str, Any] = {}
    for key_node, value_node in node.value:
        if getattr(key_node, "value", None) == "<<":
            raise yaml.constructor.ConstructorError(
                "while constructing a mapping",
                node.start_mark,
                "YAML merge keys are prohibited by the Context Source Association contract",
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


StrictContextSourceAssociationLoader.add_constructor(
    yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG,
    _construct_mapping,
)


@dataclass
class ValidationReport:
    errors: list[str] = field(default_factory=list)
    loader_policy_valid: bool = False
    schema_valid: bool = False
    canonical_order_valid: bool = False
    selection_binding_valid: bool = False
    upstream_selection_validation_valid: bool = False
    included_domain_valid: bool = False
    source_catalog_valid: bool = False
    association_semantics_valid: bool = False
    instance_constraints_valid: bool = False
    included_authority_count: int = 0
    source_unit_count: int = 0
    association_count: int = 0
    exact_instance_constraint_count: int = 0

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
                    f"{path}: canonical Context Source Association string scalar must be quoted"
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


def _load_association_snapshot(path: Path, report: ValidationReport) -> Any | None:
    source_label = path.as_posix()
    try:
        text = path.read_text(encoding="utf-8")
    except (OSError, UnicodeError) as exc:
        report.errors.append(f"{source_label}: cannot read Context Source Association YAML: {exc}")
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
        data = yaml.load(text, Loader=StrictContextSourceAssociationLoader)
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
    association_data: Any,
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
        validator.iter_errors(association_data),
        key=lambda error: (list(error.absolute_path), error.message),
    )
    if errors:
        for error in errors:
            report.errors.append(
                f"Context Source Association schema: {_schema_path(error)}: {error.message}"
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


def _validate_canonical_order(data: dict[str, Any], report: ValidationReport) -> None:
    errors_before = len(report.errors)
    if tuple(data.keys()) != ROOT_FIELD_ORDER:
        report.errors.append(
            "association root: non-canonical mapping order; expected "
            + ", ".join(ROOT_FIELD_ORDER)
        )

    binding = data["source_selection_binding"]
    if tuple(binding.keys()) != SELECTION_BINDING_FIELD_ORDER:
        report.errors.append(
            "source_selection_binding: non-canonical mapping order; expected "
            + ", ".join(SELECTION_BINDING_FIELD_ORDER)
        )

    source_units = data["source_units"]
    source_ids = [unit["source_unit_id"] for unit in source_units]
    if source_ids != sorted(source_ids):
        report.errors.append("source_units: non-canonical source_unit_id order")
    for index, unit in enumerate(source_units):
        if tuple(unit.keys()) != SOURCE_UNIT_FIELD_ORDER:
            report.errors.append(
                f"source_units[{index}]: non-canonical mapping order; expected "
                + ", ".join(SOURCE_UNIT_FIELD_ORDER)
            )

    entries = data["authority_source_entries"]
    authority_ids = [entry["scaf_authority_id"] for entry in entries]
    if authority_ids != sorted(authority_ids):
        report.errors.append(
            "authority_source_entries: non-canonical scaf_authority_id order"
        )
    for entry_index, entry in enumerate(entries):
        if tuple(entry.keys()) != AUTHORITY_SOURCE_ENTRY_FIELD_ORDER:
            report.errors.append(
                f"authority_source_entries[{entry_index}]: non-canonical mapping order; expected "
                + ", ".join(AUTHORITY_SOURCE_ENTRY_FIELD_ORDER)
            )
        associations = entry["associations"]
        keys = [_association_semantic_key(association) for association in associations]
        if keys != sorted(keys):
            report.errors.append(
                f"authority_source_entries[{entry_index}].associations: non-canonical semantic order"
            )
        for association_index, association in enumerate(associations):
            if tuple(association.keys()) != _expected_association_field_order(association):
                report.errors.append(
                    f"authority_source_entries[{entry_index}].associations[{association_index}]: "
                    "non-canonical mapping order"
                )
            provenance = association["association_provenance"]
            if tuple(provenance.keys()) != PROVENANCE_FIELD_ORDER:
                report.errors.append(
                    f"authority_source_entries[{entry_index}].associations[{association_index}]"
                    ".association_provenance: non-canonical mapping order"
                )
            if provenance["basis_refs"] != sorted(provenance["basis_refs"]):
                report.errors.append(
                    f"authority_source_entries[{entry_index}].associations[{association_index}]"
                    ".association_provenance.basis_refs: non-canonical order"
                )
            if "authority_qualification" in association:
                qualification = association["authority_qualification"]
                if tuple(qualification.keys()) != AUTHORITY_QUALIFICATION_FIELD_ORDER:
                    report.errors.append(
                        f"authority_source_entries[{entry_index}].associations[{association_index}]"
                        ".authority_qualification: non-canonical mapping order"
                    )
                if qualification["authority_basis_refs"] != sorted(
                    qualification["authority_basis_refs"]
                ):
                    report.errors.append(
                        f"authority_source_entries[{entry_index}].associations[{association_index}]"
                        ".authority_qualification.authority_basis_refs: non-canonical order"
                    )
            if "instance_constraint" in association:
                constraint = association["instance_constraint"]
                if tuple(constraint.keys()) != INSTANCE_CONSTRAINT_FIELD_ORDER:
                    report.errors.append(
                        f"authority_source_entries[{entry_index}].associations[{association_index}]"
                        ".instance_constraint: non-canonical mapping order"
                    )
    report.canonical_order_valid = len(report.errors) == errors_before


def _load_validated_selection(path: Path, report: ValidationReport) -> dict[str, Any] | None:
    try:
        text = path.read_text(encoding="utf-8")
        data = yaml.load(text, Loader=StrictConsumptionSelectionLoader)
    except (OSError, UnicodeError, yaml.YAMLError) as exc:
        report.errors.append(f"validated Consumption Selection could not be loaded: {exc}")
        return None
    if not isinstance(data, dict) or not isinstance(data.get("selected_entries"), list):
        report.errors.append("validated Consumption Selection did not expose selected_entries")
        return None
    return data


def _prove_selection_binding(
    association_data: dict[str, Any],
    selection_data: dict[str, Any],
    selection_bytes: bytes,
    report: ValidationReport,
) -> None:
    errors_before = len(report.errors)
    binding = association_data["source_selection_binding"]
    observed_sha = hashlib.sha256(selection_bytes).hexdigest()
    if binding["consumption_selection_source_sha256"] != observed_sha:
        report.errors.append(
            "source_selection_binding.consumption_selection_source_sha256 mismatch: "
            f"recorded {binding['consumption_selection_source_sha256']}, observed {observed_sha}"
        )
    if binding["selection_kind"] != selection_data.get("selection_kind"):
        report.errors.append(
            "source_selection_binding.selection_kind does not match the exact bound Consumption Selection"
        )
    if binding["selection_representation_release"] != selection_data.get(
        "representation_release"
    ):
        report.errors.append(
            "source_selection_binding.selection_representation_release does not match the exact bound Consumption Selection"
        )
    selection_scope = selection_data.get("source_profile_binding", {}).get("project_scope_ref")
    if binding["project_scope_ref"] != selection_scope:
        report.errors.append(
            "source_selection_binding.project_scope_ref does not match the exact bound Consumption Selection"
        )
    report.selection_binding_valid = len(report.errors) == errors_before


def _prove_included_domain(
    association_data: dict[str, Any],
    selection_data: dict[str, Any],
    report: ValidationReport,
) -> None:
    errors_before = len(report.errors)
    included_ids = [entry["scaf_authority_id"] for entry in selection_data["selected_entries"]]
    association_ids = [
        entry["scaf_authority_id"] for entry in association_data["authority_source_entries"]
    ]

    duplicate_ids = sorted({authority_id for authority_id in association_ids if association_ids.count(authority_id) > 1})
    if duplicate_ids:
        report.errors.append(
            "authority_source_entries contain duplicate scaf_authority_id value(s): "
            + ", ".join(duplicate_ids)
        )
    if set(association_ids) != set(included_ids) or len(association_ids) != len(included_ids):
        missing = sorted(set(included_ids) - set(association_ids))
        extra = sorted(set(association_ids) - set(included_ids))
        detail: list[str] = []
        if missing:
            detail.append("missing=" + ",".join(missing))
        if extra:
            detail.append("extra=" + ",".join(extra))
        report.errors.append(
            "authority_source_entries domain does not equal validated Consumption Selection included domain I"
            + (": " + "; ".join(detail) if detail else "")
        )
    report.included_authority_count = len(set(included_ids))
    report.included_domain_valid = len(report.errors) == errors_before


def _prove_catalog_and_associations(
    association_data: dict[str, Any],
    report: ValidationReport,
) -> tuple[dict[str, dict[str, Any]], list[tuple[str, dict[str, Any]]]]:
    catalog_errors_before = len(report.errors)
    source_units = association_data["source_units"]
    source_ids = [unit["source_unit_id"] for unit in source_units]
    identities = [unit["source_identity_ref"] for unit in source_units]

    duplicate_source_ids = sorted({value for value in source_ids if source_ids.count(value) > 1})
    if duplicate_source_ids:
        report.errors.append(
            "source_units contain duplicate source_unit_id value(s): "
            + ", ".join(duplicate_source_ids)
        )
    duplicate_identities = sorted({value for value in identities if identities.count(value) > 1})
    if duplicate_identities:
        report.errors.append(
            "source_units contain duplicate source_identity_ref value(s): "
            + ", ".join(duplicate_identities)
        )

    source_index = {unit["source_unit_id"]: unit for unit in source_units}
    referenced_ids: set[str] = set()
    associations_with_authority: list[tuple[str, dict[str, Any]]] = []
    for entry in association_data["authority_source_entries"]:
        authority_id = entry["scaf_authority_id"]
        seen_semantic_keys: set[tuple[Any, ...]] = set()
        for association in entry["associations"]:
            source_ref = association["source_unit_ref"]
            referenced_ids.add(source_ref)
            associations_with_authority.append((authority_id, association))
            if source_ref not in source_index:
                report.errors.append(
                    f"authority {authority_id}: source_unit_ref {source_ref!r} does not resolve to source_units catalog"
                )
            semantic_key = _association_semantic_key(association)
            if semantic_key in seen_semantic_keys:
                report.errors.append(
                    f"authority {authority_id}: duplicate semantic Controlled Source Association for {semantic_key!r}"
                )
            seen_semantic_keys.add(semantic_key)

    unused = sorted(set(source_ids) - referenced_ids)
    if unused:
        report.errors.append("source_units contain unused Source Unit(s): " + ", ".join(unused))

    report.source_unit_count = len(source_units)
    report.association_count = len(associations_with_authority)
    report.source_catalog_valid = len(report.errors) == catalog_errors_before
    report.association_semantics_valid = report.source_catalog_valid
    return source_index, associations_with_authority


def _repo_identity_path(repo_root: Path, source_identity_ref: str) -> Path | None:
    if not source_identity_ref.startswith("repo:"):
        return None
    raw = source_identity_ref[len("repo:"):]
    if not raw or "\\" in raw:
        return None
    pure = PurePosixPath(raw)
    if pure.is_absolute() or any(part in ("", ".", "..") for part in pure.parts):
        return None
    candidate = (repo_root / Path(*pure.parts)).resolve()
    try:
        candidate.relative_to(repo_root)
    except ValueError:
        return None
    return candidate


def _prove_instance_constraints(
    repo_root: Path,
    source_index: dict[str, dict[str, Any]],
    associations_with_authority: list[tuple[str, dict[str, Any]]],
    report: ValidationReport,
) -> None:
    errors_before = len(report.errors)
    count = 0
    byte_cache: dict[Path, bytes] = {}
    for authority_id, association in associations_with_authority:
        constraint = association.get("instance_constraint")
        if constraint is None:
            continue
        count += 1
        source_ref = association["source_unit_ref"]
        source_unit = source_index.get(source_ref)
        if source_unit is None:
            continue
        identity = source_unit["source_identity_ref"]
        source_path = _repo_identity_path(repo_root, identity)
        if source_path is None:
            report.errors.append(
                f"authority {authority_id}: instance_constraint for Source Unit {source_ref!r} cannot be proven under the bounded repository-local repo: identity boundary"
            )
            continue
        try:
            data = byte_cache.setdefault(source_path, source_path.read_bytes())
        except OSError as exc:
            report.errors.append(
                f"authority {authority_id}: cannot read repository-local constrained source {source_path.as_posix()}: {exc}"
            )
            continue
        observed_sha = hashlib.sha256(data).hexdigest()
        if observed_sha != constraint["value"]:
            report.errors.append(
                f"authority {authority_id}: instance_constraint SHA-256 mismatch for {identity!r}: recorded {constraint['value']}, observed {observed_sha}"
            )
    report.exact_instance_constraint_count = count
    report.instance_constraints_valid = len(report.errors) == errors_before


def validate_context_source_associations(
    repo_root: Path,
    associations_path: Path | None = None,
    selection_path: Path | None = None,
    profile_path: Path | None = None,
    project_application_path: Path | None = None,
) -> ValidationReport:
    """Validate one Context Source Association set against exact upstream/source truth.

    Callers may select project-side association/selection/profile/application inputs. The
    association schema and existing repository-owned SCAF validation sources are fixed to the
    reviewed repository. This function performs no candidate discovery or general source
    resolution.
    """

    repo_root = repo_root.resolve()
    associations_path = _resolve_input_path(repo_root, associations_path, DEFAULT_ASSOCIATIONS_PATH)
    selection_path = _resolve_input_path(repo_root, selection_path, DEFAULT_SELECTION_PATH)
    profile_path = _resolve_input_path(repo_root, profile_path, DEFAULT_PROFILE_PATH)
    project_application_path = _resolve_input_path(
        repo_root, project_application_path, DEFAULT_PROJECT_APPLICATION_PATH
    )

    report = ValidationReport()
    association_bytes = _read_required_bytes(
        associations_path, "Context Source Associations", report
    )
    selection_bytes = _read_required_bytes(selection_path, "Consumption Selection", report)
    schema_bytes = _read_required_bytes(
        repo_root / ASSOCIATION_SCHEMA_PATH, "Context Source Association schema", report
    )
    if None in (association_bytes, selection_bytes, schema_bytes):
        return report

    with tempfile.TemporaryDirectory(prefix="scaf-context-source-association-validator-") as temp_dir:
        temp_root = Path(temp_dir)
        association_snapshot = temp_root / "context-source-associations.yaml"
        selection_snapshot = temp_root / "consumption-selection.yaml"
        association_snapshot.write_bytes(association_bytes)
        selection_snapshot.write_bytes(selection_bytes)

        association_data = _load_association_snapshot(association_snapshot, report)
        if association_data is None:
            return report
        if not _validate_schema(
            association_data,
            schema_bytes,
            (repo_root / ASSOCIATION_SCHEMA_PATH).as_posix(),
            report,
        ):
            return report
        if not isinstance(association_data, dict):  # schema should already prove this
            report.errors.append("Context Source Association root is not a mapping")
            return report

        _validate_canonical_order(association_data, report)

        upstream_report = validate_consumption_selection(
            repo_root,
            selection_snapshot,
            profile_path,
            project_application_path,
        )
        if not upstream_report.passed:
            report.errors.append(
                "bound Consumption Selection failed accepted source-aware validation; Context Source Association source proof cannot proceed"
            )
            for error in upstream_report.errors:
                report.errors.append(f"Consumption Selection: {error}")
            return report
        report.upstream_selection_validation_valid = True

        selection_data = _load_validated_selection(selection_snapshot, report)
        if selection_data is None:
            return report

        _prove_selection_binding(association_data, selection_data, selection_bytes, report)
        _prove_included_domain(association_data, selection_data, report)
        source_index, associations = _prove_catalog_and_associations(association_data, report)
        _prove_instance_constraints(repo_root, source_index, associations, report)

    return report


def _default_repo_root() -> Path:
    return Path(__file__).resolve().parents[2]


def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description=(
            "Validate SCAF Context Source Association representation/source consistency. "
            "Repository-owned schema and upstream validation sources remain fixed to this reviewed SCAF repository."
        )
    )
    parser.add_argument("--associations", type=Path, help="Context Source Association YAML path")
    parser.add_argument("--selection", type=Path, help="bound Consumption Selection YAML path")
    parser.add_argument("--profile", type=Path, help="bound Effective Project Profile YAML path")
    parser.add_argument(
        "--project-application", type=Path, help="bound Project Application YAML path"
    )
    return parser


def _print_report(report: ValidationReport) -> None:
    print("SCAF Context Source Association Source-Aware Validator")
    print("-----------------------------------------------------")
    print(f"YAML loader policy:          {'PASS' if report.loader_policy_valid else 'FAIL'}")
    print(f"Schema validation:           {'PASS' if report.schema_valid else 'FAIL'}")
    print(f"Canonical ordering:          {'PASS' if report.canonical_order_valid else 'FAIL'}")
    print(f"Upstream selection valid:    {'PASS' if report.upstream_selection_validation_valid else 'FAIL'}")
    print(f"Selection binding proof:     {'PASS' if report.selection_binding_valid else 'FAIL'}")
    print(f"Validated-I coverage:        {'PASS' if report.included_domain_valid else 'FAIL'}")
    print(f"Source catalog/reference:    {'PASS' if report.source_catalog_valid else 'FAIL'}")
    print(f"Association uniqueness:      {'PASS' if report.association_semantics_valid else 'FAIL'}")
    print(f"Instance-constraint proof:   {'PASS' if report.instance_constraints_valid else 'FAIL'}")
    print(f"Included authorities:        {report.included_authority_count}")
    print(f"Source Units:                {report.source_unit_count}")
    print(f"Controlled associations:     {report.association_count}")
    print(f"Exact instance constraints:  {report.exact_instance_constraint_count}")
    print(f"Errors: {len(report.errors)}")
    for error in report.errors:
        print(f"ERROR: {error}")
    print("CONTEXT SOURCE ASSOCIATION SOURCE RESULT: " + ("PASS" if report.passed else "FAIL"))


def main(argv: list[str] | None = None) -> int:
    args = _build_parser().parse_args(argv)
    report = validate_context_source_associations(
        _default_repo_root(),
        args.associations,
        args.selection,
        args.profile,
        args.project_application,
    )
    _print_report(report)
    return 0 if report.passed else 1


if __name__ == "__main__":
    sys.exit(main())
