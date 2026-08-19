#!/usr/bin/env python3
"""Validate SCAF Consumption Selection representation/source conformance.

Validation order:
1. capture the selected Consumption Selection, Effective Project Profile, and
   Project Application bytes plus repository-owned validation sources;
2. enforce the accepted rc03 raw-YAML and canonical-order policy;
3. validate the parsed Consumption Selection against the accepted rc04
   Draft 2020-12 schema;
4. validate the exact captured Effective Project Profile snapshot through the
   frozen v0.0.6 source-aware profile validator against the same captured
   Project Application snapshot and captured repository-owned SCAF sources;
5. prove the exact source-profile byte SHA-256 and frozen provenance binding;
6. resolve the bounded state/authority selector over the validated profile;
7. prove selected-entry source fidelity and eligibility;
8. reconstruct D/E/I/O/X and prove bounded-omission consistency;
9. prove the serialized complete/filtered classification.

A PASS is representation/source/selection consistency only. It is not an
engineering applicability decision, Project Design Authority approval,
Pattern selection, implementation result, verification/compliance result,
risk acceptance, release readiness, or closure verdict.
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
        "tools/scaf_consumption_selection_validator/requirements.txt"
    ) from exc

try:
    from jsonschema import Draft202012Validator
    from jsonschema.exceptions import SchemaError
except ImportError as exc:  # pragma: no cover - CLI environment only
    raise SystemExit(
        "Missing dependency: jsonschema. Install "
        "tools/scaf_consumption_selection_validator/requirements.txt"
    ) from exc

from tools.scaf_effective_project_profile_validator.validator import (
    StrictEffectiveProjectProfileLoader,
    validate_effective_project_profile,
)

__all__ = (
    "ValidationReport",
    "validate_consumption_selection",
    "main",
)

DEFAULT_SELECTION_PATH = Path("examples/consumption-selection.yaml")
DEFAULT_PROFILE_PATH = Path("examples/effective-project-profile.yaml")
DEFAULT_PROJECT_APPLICATION_PATH = Path("examples/project-application.yaml")

SELECTION_SCHEMA_PATH = Path("schemas/consumption-selection.schema.json")
PROFILE_SCHEMA_PATH = Path("schemas/effective-project-profile.schema.json")
PROJECT_APPLICATION_SCHEMA_PATH = Path("schemas/project-application.schema.json")
AUTHORITY_REGISTRY_PATH = Path("authority-registry.yaml")
AUTHORITY_SCHEMA_PATH = Path("schemas/authority-registry.schema.json")
NORMATIVE_ROOT_PATH = Path("docs/normative")

ROOT_FIELD_ORDER = (
    "selection_kind",
    "representation_release",
    "source_profile_binding",
    "selection_purpose",
    "state_selector",
    "authority_selector",
    "bounded_omission",
    "selected_entries",
    "selection_class",
)
SOURCE_BINDING_FIELD_ORDER = (
    "effective_project_profile_source_sha256",
    "scaf_source_release",
    "project_scope_ref",
    "project_application_source_sha256",
)
ALL_DOMAIN_SELECTOR_FIELD_ORDER = ("mode",)
EXPLICIT_SELECTOR_FIELD_ORDER = ("mode", "scaf_authority_ids")
NO_OMISSION_FIELD_ORDER = ("applied",)
APPLIED_OMISSION_FIELD_ORDER = ("applied", "basis")
RECORDED_ENTRY_FIELD_ORDER = (
    "scaf_authority_id",
    "profile_state",
    "project_application_record_id",
)
ABSENCE_ENTRY_FIELD_ORDER = (
    "scaf_authority_id",
    "profile_state",
)
PROFILE_STATE_ORDER = (
    "applicable",
    "not_applicable",
    "undetermined",
    "no_current_disposition",
)
RECORDED_STATES = frozenset(PROFILE_STATE_ORDER[:3])
ABSENCE_STATE = "no_current_disposition"


class StrictConsumptionSelectionLoader(yaml.SafeLoader):
    """Safe YAML loader that rejects ambiguous Consumption Selection mappings."""


def _construct_mapping(
    loader: StrictConsumptionSelectionLoader,
    node: yaml.MappingNode,
    deep: bool = False,
) -> dict[str, Any]:
    mapping: dict[str, Any] = {}
    for key_node, value_node in node.value:
        if getattr(key_node, "value", None) == "<<":
            raise yaml.constructor.ConstructorError(
                "while constructing a mapping",
                node.start_mark,
                "YAML merge keys are prohibited by the Consumption Selection contract",
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


StrictConsumptionSelectionLoader.add_constructor(
    yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG,
    _construct_mapping,
)


@dataclass
class ValidationReport:
    errors: list[str] = field(default_factory=list)
    loader_policy_valid: bool = False
    schema_valid: bool = False
    canonical_order_valid: bool = False
    profile_validation_valid: bool = False
    source_binding_valid: bool = False
    selector_valid: bool = False
    selected_entry_fidelity_valid: bool = False
    omission_valid: bool = False
    selection_class_valid: bool = False
    domain_count: int = 0
    eligible_count: int = 0
    included_count: int = 0
    omitted_count: int = 0
    excluded_count: int = 0

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


def _read_normative_snapshot(
    repo_root: Path,
    report: ValidationReport,
) -> dict[str, bytes] | None:
    source_root = repo_root / NORMATIVE_ROOT_PATH
    snapshot: dict[str, bytes] = {}
    try:
        for source_file in sorted(source_root.glob("*.md")):
            data = source_file.read_bytes()
            data.decode("utf-8")
            snapshot[source_file.name] = data
    except (OSError, UnicodeError) as exc:
        report.errors.append(f"cannot read canonical normative-source snapshot: {exc}")
        return None
    if not snapshot:
        report.errors.append("canonical normative-source snapshot is empty")
        return None
    return snapshot


def _prepare_profile_validation_boundary(
    boundary_root: Path,
    *,
    authority_bytes: bytes,
    authority_schema_bytes: bytes,
    project_application_schema_bytes: bytes,
    profile_schema_bytes: bytes,
    normative_snapshot: dict[str, bytes],
    report: ValidationReport,
) -> bool:
    try:
        (boundary_root / "schemas").mkdir(parents=True, exist_ok=True)
        (boundary_root / NORMATIVE_ROOT_PATH).mkdir(parents=True, exist_ok=True)
        (boundary_root / AUTHORITY_REGISTRY_PATH).write_bytes(authority_bytes)
        (boundary_root / AUTHORITY_SCHEMA_PATH).write_bytes(authority_schema_bytes)
        (boundary_root / PROJECT_APPLICATION_SCHEMA_PATH).write_bytes(
            project_application_schema_bytes
        )
        (boundary_root / PROFILE_SCHEMA_PATH).write_bytes(profile_schema_bytes)
        for filename, data in normative_snapshot.items():
            (boundary_root / NORMATIVE_ROOT_PATH / filename).write_bytes(data)
    except OSError as exc:
        report.errors.append(f"cannot create private profile-validation boundary: {exc}")
        return False
    return True


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
                    f"{path}: canonical Consumption Selection string scalar must be quoted"
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


def _load_selection_snapshot(path: Path, report: ValidationReport) -> Any | None:
    source_label = path.as_posix()
    try:
        text = path.read_text(encoding="utf-8")
    except (OSError, UnicodeError) as exc:
        report.errors.append(f"{source_label}: cannot read Consumption Selection YAML: {exc}")
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
        data = yaml.load(text, Loader=StrictConsumptionSelectionLoader)
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


def _validate_selection_schema(
    selection_data: Any,
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
        validator.iter_errors(selection_data),
        key=lambda error: (list(error.absolute_path), error.message),
    )
    if errors:
        for error in errors:
            report.errors.append(
                f"Consumption Selection schema: {_schema_path(error)}: {error.message}"
            )
        return False
    report.schema_valid = True
    return True


def _validate_canonical_order(selection: dict[str, Any], report: ValidationReport) -> None:
    errors_before = len(report.errors)

    if tuple(selection.keys()) != ROOT_FIELD_ORDER:
        report.errors.append(
            "selection root: non-canonical mapping order; expected "
            + ", ".join(ROOT_FIELD_ORDER)
        )

    binding = selection["source_profile_binding"]
    if tuple(binding.keys()) != SOURCE_BINDING_FIELD_ORDER:
        report.errors.append(
            "source_profile_binding: non-canonical mapping order; expected "
            + ", ".join(SOURCE_BINDING_FIELD_ORDER)
        )

    states = selection["state_selector"]
    state_rank = {state: index for index, state in enumerate(PROFILE_STATE_ORDER)}
    if [state_rank[state] for state in states] != sorted(state_rank[state] for state in states):
        report.errors.append(
            "state_selector: non-canonical order; use frozen profile-state order"
        )

    authority_selector = selection["authority_selector"]
    if authority_selector["mode"] == "all_domain":
        expected_authority_order = ALL_DOMAIN_SELECTOR_FIELD_ORDER
    else:
        expected_authority_order = EXPLICIT_SELECTOR_FIELD_ORDER
        authority_ids = authority_selector["scaf_authority_ids"]
        if authority_ids != sorted(authority_ids):
            report.errors.append(
                "authority_selector.scaf_authority_ids: non-canonical exact-ID order"
            )
    if tuple(authority_selector.keys()) != expected_authority_order:
        report.errors.append(
            "authority_selector: non-canonical mapping order; expected "
            + ", ".join(expected_authority_order)
        )

    omission = selection["bounded_omission"]
    expected_omission_order = (
        APPLIED_OMISSION_FIELD_ORDER if omission["applied"] else NO_OMISSION_FIELD_ORDER
    )
    if tuple(omission.keys()) != expected_omission_order:
        report.errors.append(
            "bounded_omission: non-canonical mapping order; expected "
            + ", ".join(expected_omission_order)
        )

    entries = selection["selected_entries"]
    entry_ids = [entry["scaf_authority_id"] for entry in entries]
    if entry_ids != sorted(entry_ids):
        report.errors.append(
            "selected_entries: non-canonical order; entries must be ordered by exact "
            "scaf_authority_id ascending"
        )

    seen: set[str] = set()
    duplicate_ids: set[str] = set()
    for authority_id in entry_ids:
        if authority_id in seen:
            duplicate_ids.add(authority_id)
        seen.add(authority_id)
    if duplicate_ids:
        report.errors.append(
            "selected_entries contain duplicate scaf_authority_id value(s): "
            + ", ".join(sorted(duplicate_ids))
        )

    for index, entry in enumerate(entries):
        expected_entry_order = (
            RECORDED_ENTRY_FIELD_ORDER
            if entry["profile_state"] in RECORDED_STATES
            else ABSENCE_ENTRY_FIELD_ORDER
        )
        if tuple(entry.keys()) != expected_entry_order:
            report.errors.append(
                f"selected_entries[{index}]: non-canonical mapping order; expected "
                + ", ".join(expected_entry_order)
            )

    report.canonical_order_valid = len(report.errors) == errors_before


def _load_validated_profile(path: Path, report: ValidationReport) -> dict[str, Any] | None:
    try:
        text = path.read_text(encoding="utf-8")
        data = yaml.load(text, Loader=StrictEffectiveProjectProfileLoader)
    except (OSError, UnicodeError, yaml.YAMLError) as exc:
        report.errors.append(f"validated Effective Project Profile could not be loaded: {exc}")
        return None
    if not isinstance(data, dict) or not isinstance(data.get("entries"), list):
        report.errors.append("validated Effective Project Profile did not expose an entries list")
        return None
    return data


def _prove_source_binding(
    selection: dict[str, Any],
    profile: dict[str, Any],
    profile_bytes: bytes,
    report: ValidationReport,
) -> None:
    errors_before = len(report.errors)
    binding = selection["source_profile_binding"]

    actual_profile_digest = hashlib.sha256(profile_bytes).hexdigest()
    if binding["effective_project_profile_source_sha256"] != actual_profile_digest:
        report.errors.append(
            "effective_project_profile_source_sha256 mismatch: selection records "
            f"{binding['effective_project_profile_source_sha256']!r}, selected profile "
            f"snapshot is {actual_profile_digest!r}"
        )

    provenance_pairs = (
        ("scaf_source_release", "scaf_source_release"),
        ("project_scope_ref", "project_scope_ref"),
        ("project_application_source_sha256", "project_application_source_sha256"),
    )
    for binding_key, profile_key in provenance_pairs:
        if binding[binding_key] != profile[profile_key]:
            report.errors.append(
                f"source_profile_binding.{binding_key}: {binding[binding_key]!r} does not "
                f"match validated profile {profile_key} {profile[profile_key]!r}"
            )

    report.source_binding_valid = len(report.errors) == errors_before


def _derive_sets_and_prove_selection(
    selection: dict[str, Any],
    profile: dict[str, Any],
    report: ValidationReport,
) -> None:
    selector_errors_before = len(report.errors)

    profile_entries = profile["entries"]
    profile_index = {entry["scaf_authority_id"]: entry for entry in profile_entries}
    domain_ids = tuple(entry["scaf_authority_id"] for entry in profile_entries)
    domain_set = set(domain_ids)

    authority_selector = selection["authority_selector"]
    if authority_selector["mode"] == "all_domain":
        allowed_ids = domain_set
    else:
        explicit_ids = authority_selector["scaf_authority_ids"]
        unknown_ids = sorted(set(explicit_ids) - domain_set)
        if unknown_ids:
            report.errors.append(
                "authority_selector.scaf_authority_ids contains ID(s) outside the validated "
                "source-profile PAO domain: " + ", ".join(unknown_ids)
            )
        allowed_ids = set(explicit_ids) & domain_set

    selected_states = set(selection["state_selector"])
    eligible_set = {
        authority_id
        for authority_id, entry in profile_index.items()
        if entry["profile_state"] in selected_states and authority_id in allowed_ids
    }

    report.selector_valid = len(report.errors) == selector_errors_before

    fidelity_errors_before = len(report.errors)
    included_set: set[str] = set()
    for index, selected in enumerate(selection["selected_entries"]):
        authority_id = selected["scaf_authority_id"]
        included_set.add(authority_id)
        source_entry = profile_index.get(authority_id)
        if source_entry is None:
            report.errors.append(
                f"selected_entries[{index}].scaf_authority_id: {authority_id!r} does not "
                "exist in the validated source profile"
            )
            continue
        if authority_id not in eligible_set:
            report.errors.append(
                f"selected_entries[{index}]: authority {authority_id!r} is not eligible under "
                "the declared state/authority selector"
            )
        if selected["profile_state"] != source_entry["profile_state"]:
            report.errors.append(
                f"selected_entries[{index}]: profile_state {selected['profile_state']!r} does "
                f"not match source profile state {source_entry['profile_state']!r}"
            )
        if source_entry["profile_state"] in RECORDED_STATES:
            if selected.get("project_application_record_id") != source_entry.get(
                "project_application_record_id"
            ):
                report.errors.append(
                    f"selected_entries[{index}]: project_application_record_id does not "
                    "match the validated source profile entry"
                )
        elif "project_application_record_id" in selected:
            report.errors.append(
                f"selected_entries[{index}]: no_current_disposition projection must not "
                "carry project_application_record_id"
            )

    report.selected_entry_fidelity_valid = len(report.errors) == fidelity_errors_before

    omitted_set = eligible_set - included_set
    excluded_set = domain_set - eligible_set

    omission_errors_before = len(report.errors)
    if not included_set.issubset(eligible_set):
        report.errors.append("selected_entries set I is not a subset of eligible set E")
    if not selection["bounded_omission"]["applied"] and included_set != eligible_set:
        report.errors.append(
            "bounded_omission.applied is false but selected set I does not equal eligible set E"
        )
    report.omission_valid = len(report.errors) == omission_errors_before

    expected_class = (
        "complete"
        if included_set == domain_set and not omitted_set and not excluded_set
        else "filtered"
    )
    if selection["selection_class"] != expected_class:
        report.errors.append(
            f"selection_class {selection['selection_class']!r} does not match derived "
            f"classification {expected_class!r}"
        )
    else:
        report.selection_class_valid = True

    report.domain_count = len(domain_set)
    report.eligible_count = len(eligible_set)
    report.included_count = len(included_set)
    report.omitted_count = len(omitted_set)
    report.excluded_count = len(excluded_set)


def validate_consumption_selection(
    repo_root: Path,
    selection_path: Path | None = None,
    profile_path: Path | None = None,
    project_application_path: Path | None = None,
) -> ValidationReport:
    """Validate one Consumption Selection against exact selected source snapshots.

    Callers may select only the project-side Consumption Selection, Effective
    Project Profile, and Project Application sources. Repository-owned schemas,
    frozen authority sources, and canonical normative sources are captured from
    the reviewed repository and consumed through a private validation boundary.
    """

    repo_root = repo_root.resolve()
    selection_path = _resolve_input_path(repo_root, selection_path, DEFAULT_SELECTION_PATH)
    profile_path = _resolve_input_path(repo_root, profile_path, DEFAULT_PROFILE_PATH)
    project_application_path = _resolve_input_path(
        repo_root, project_application_path, DEFAULT_PROJECT_APPLICATION_PATH
    )

    report = ValidationReport()

    selection_bytes = _read_required_bytes(selection_path, "Consumption Selection", report)
    profile_bytes = _read_required_bytes(profile_path, "Effective Project Profile", report)
    project_application_bytes = _read_required_bytes(
        project_application_path, "Project Application", report
    )
    selection_schema_bytes = _read_required_bytes(
        repo_root / SELECTION_SCHEMA_PATH, "Consumption Selection schema", report
    )
    profile_schema_bytes = _read_required_bytes(
        repo_root / PROFILE_SCHEMA_PATH, "Effective Project Profile schema", report
    )
    project_application_schema_bytes = _read_required_bytes(
        repo_root / PROJECT_APPLICATION_SCHEMA_PATH, "Project Application schema", report
    )
    authority_bytes = _read_required_bytes(
        repo_root / AUTHORITY_REGISTRY_PATH, "authority registry", report
    )
    authority_schema_bytes = _read_required_bytes(
        repo_root / AUTHORITY_SCHEMA_PATH, "authority schema", report
    )
    if None in (
        selection_bytes,
        profile_bytes,
        project_application_bytes,
        selection_schema_bytes,
        profile_schema_bytes,
        project_application_schema_bytes,
        authority_bytes,
        authority_schema_bytes,
    ):
        return report

    normative_snapshot = _read_normative_snapshot(repo_root, report)
    if normative_snapshot is None:
        return report

    with tempfile.TemporaryDirectory(prefix="scaf-consumption-selection-validator-") as temp_dir:
        temp_root = Path(temp_dir)
        selection_snapshot = temp_root / "consumption-selection.yaml"
        profile_snapshot = temp_root / "effective-project-profile.yaml"
        project_snapshot = temp_root / "project-application.yaml"
        validation_root = temp_root / "validation-repo"

        selection_snapshot.write_bytes(selection_bytes)
        profile_snapshot.write_bytes(profile_bytes)
        project_snapshot.write_bytes(project_application_bytes)

        selection_data = _load_selection_snapshot(selection_snapshot, report)
        if selection_data is None:
            return report

        if not _validate_selection_schema(
            selection_data,
            selection_schema_bytes,
            (repo_root / SELECTION_SCHEMA_PATH).as_posix(),
            report,
        ):
            return report
        if not isinstance(selection_data, dict):  # schema should already prove this
            report.errors.append("Consumption Selection root is not a mapping")
            return report

        _validate_canonical_order(selection_data, report)

        if not _prepare_profile_validation_boundary(
            validation_root,
            authority_bytes=authority_bytes,
            authority_schema_bytes=authority_schema_bytes,
            project_application_schema_bytes=project_application_schema_bytes,
            profile_schema_bytes=profile_schema_bytes,
            normative_snapshot=normative_snapshot,
            report=report,
        ):
            return report

        profile_report = validate_effective_project_profile(
            validation_root,
            profile_snapshot,
            project_snapshot,
        )
        if not profile_report.passed:
            report.errors.append(
                "bound Effective Project Profile snapshot failed frozen v0.0.6 source-aware "
                "validation; Consumption Selection source proof cannot proceed"
            )
            for error in profile_report.errors:
                report.errors.append(f"Effective Project Profile: {error}")
            return report
        report.profile_validation_valid = True

        profile_data = _load_validated_profile(profile_snapshot, report)
        if profile_data is None:
            return report

        _prove_source_binding(selection_data, profile_data, profile_bytes, report)
        _derive_sets_and_prove_selection(selection_data, profile_data, report)

    return report


def _default_repo_root() -> Path:
    return Path(__file__).resolve().parents[2]


def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description=(
            "Validate SCAF Consumption Selection representation/source conformance. "
            "Repository-owned schemas, frozen authority sources, and normative sources "
            "are fixed to this reviewed SCAF repository."
        )
    )
    parser.add_argument(
        "--selection",
        type=Path,
        default=None,
        help=(
            "Consumption Selection YAML to validate. Defaults to "
            "examples/consumption-selection.yaml."
        ),
    )
    parser.add_argument(
        "--profile",
        type=Path,
        default=None,
        help=(
            "Bound Effective Project Profile YAML. Defaults to "
            "examples/effective-project-profile.yaml."
        ),
    )
    parser.add_argument(
        "--project-application",
        type=Path,
        default=None,
        help=(
            "Project Application YAML required by the bound profile validation. Defaults to "
            "examples/project-application.yaml."
        ),
    )
    return parser


def _print_report(report: ValidationReport) -> None:
    print("SCAF Consumption Selection Source-Aware Validation")
    print(f"Domain entries (D):          {report.domain_count}")
    print(f"Eligible entries (E):        {report.eligible_count}")
    print(f"Included entries (I):        {report.included_count}")
    print(f"Bounded-omitted entries (O): {report.omitted_count}")
    print(f"Predicate-excluded (X):      {report.excluded_count}")
    print(f"Selection YAML policy:       {'PASS' if report.loader_policy_valid else 'FAIL'}")
    print(f"Selection schema:            {'PASS' if report.schema_valid else 'FAIL'}")
    print(f"Canonical ordering:          {'PASS' if report.canonical_order_valid else 'FAIL'}")
    print(f"Bound profile proof:         {'PASS' if report.profile_validation_valid else 'FAIL'}")
    print(f"Source-profile binding:      {'PASS' if report.source_binding_valid else 'FAIL'}")
    print(f"Selector/domain proof:       {'PASS' if report.selector_valid else 'FAIL'}")
    print(
        f"Selected-entry fidelity:    {'PASS' if report.selected_entry_fidelity_valid else 'FAIL'}"
    )
    print(f"Bounded-omission proof:      {'PASS' if report.omission_valid else 'FAIL'}")
    print(f"Selection-class proof:       {'PASS' if report.selection_class_valid else 'FAIL'}")
    print(f"Errors: {len(report.errors)}")
    for error in report.errors:
        print(f"ERROR: {error}")
    print(
        "CONSUMPTION SELECTION REPRESENTATION/SOURCE RESULT: "
        + ("PASS" if report.passed else "FAIL")
    )


def main(argv: list[str] | None = None) -> int:
    args = _build_parser().parse_args(argv)
    report = validate_consumption_selection(
        _default_repo_root(),
        args.selection,
        args.profile,
        args.project_application,
    )
    _print_report(report)
    return 0 if report.passed else 1


if __name__ == "__main__":  # pragma: no cover
    sys.exit(main())
