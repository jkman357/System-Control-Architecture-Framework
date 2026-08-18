#!/usr/bin/env python3
"""Validate SCAF Effective Project Profile representation/source conformance.

Validation order:
1. accepted rc10 raw-YAML representation policy;
2. accepted rc11 Draft 2020-12 parsed-instance schema;
3. exact selected Project Application source-byte SHA-256 binding;
4. frozen authority-registry source-aware proof;
5. accepted rc07 Project Application representation/source-aware proof;
6. complete source-release-bound PAO domain and authority identity checks;
7. deterministic entry ordering;
8. recorded-state Project Application trace correspondence;
9. no_current_disposition exact-pair absence proof.

A PASS means only that the selected profile is consistent with the checked
representation and source snapshots. It does not decide engineering
applicability correctness, rationale adequacy, project authority approval,
Pattern selection, implementation, verification, compliance, risk,
completion, release readiness, or closure.
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
        "tools/scaf_effective_project_profile_validator/requirements.txt"
    ) from exc

try:
    from jsonschema import Draft202012Validator
    from jsonschema.exceptions import SchemaError
except ImportError as exc:  # pragma: no cover - CLI environment only
    raise SystemExit(
        "Missing dependency: jsonschema. Install "
        "tools/scaf_effective_project_profile_validator/requirements.txt"
    ) from exc

from tools.scaf_project_application_validator.validator import (
    StrictProjectApplicationLoader,
    validate_project_application,
)
from tools.scaf_validator.validator import validate_registry


DEFAULT_PROFILE_PATH = Path("examples/effective-project-profile.yaml")
DEFAULT_PROJECT_APPLICATION_PATH = Path("examples/project-application.yaml")
PROFILE_SCHEMA_PATH = Path("schemas/effective-project-profile.schema.json")
PROJECT_APPLICATION_SCHEMA_PATH = Path("schemas/project-application.schema.json")
AUTHORITY_REGISTRY_PATH = Path("authority-registry.yaml")
AUTHORITY_SCHEMA_PATH = Path("schemas/authority-registry.schema.json")
NORMATIVE_ROOT_PATH = Path("docs/normative")

EXPECTED_AUTHORITY_CLASS = "Project-Applicable Obligation"

ROOT_FIELD_ORDER = (
    "profile_kind",
    "representation_release",
    "scaf_source_release",
    "project_scope_ref",
    "project_application_source_sha256",
    "entries",
)
RECORDED_ENTRY_FIELD_ORDER = (
    "scaf_authority_id",
    "profile_state",
    "project_application_record_id",
)
ABSENCE_ENTRY_FIELD_ORDER = (
    "scaf_authority_id",
    "profile_state",
)
RECORDED_STATES = frozenset(("applicable", "not_applicable", "undetermined"))
ABSENCE_STATE = "no_current_disposition"


class StrictEffectiveProjectProfileLoader(yaml.SafeLoader):
    """Safe YAML loader that rejects ambiguous profile mapping forms."""


def _construct_mapping(
    loader: StrictEffectiveProjectProfileLoader,
    node: yaml.MappingNode,
    deep: bool = False,
) -> dict[str, Any]:
    mapping: dict[str, Any] = {}
    for key_node, value_node in node.value:
        if getattr(key_node, "value", None) == "<<":
            raise yaml.constructor.ConstructorError(
                "while constructing a mapping",
                node.start_mark,
                "YAML merge keys are prohibited by the Effective Project Profile contract",
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


StrictEffectiveProjectProfileLoader.add_constructor(
    yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG,
    _construct_mapping,
)


@dataclass
class ValidationReport:
    errors: list[str] = field(default_factory=list)
    entry_count: int = 0
    loader_policy_valid: bool = False
    schema_valid: bool = False
    source_digest_valid: bool = False
    authority_registry_valid: bool = False
    project_application_valid: bool = False
    domain_valid: bool = False
    canonical_order_valid: bool = False
    recorded_trace_valid: bool = False
    absence_proof_valid: bool = False

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


def _load_profile_snapshot(path: Path, report: ValidationReport) -> Any | None:
    source_label = path.as_posix()
    try:
        text = path.read_text(encoding="utf-8")
    except (OSError, UnicodeError) as exc:
        report.errors.append(f"{source_label}: cannot read Effective Project Profile YAML: {exc}")
        return None

    if not _scan_yaml_policy(text, source_label, report):
        return None

    try:
        data = yaml.load(text, Loader=StrictEffectiveProjectProfileLoader)
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


def _validate_profile_schema(
    profile_data: Any,
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
        validator.iter_errors(profile_data),
        key=lambda error: (list(error.absolute_path), error.message),
    )
    if errors:
        for error in errors:
            report.errors.append(
                f"Effective Project Profile schema: {_schema_path(error)}: {error.message}"
            )
        return False

    report.schema_valid = True
    return True


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


def _write_normative_snapshot(
    normative_snapshot: dict[str, bytes],
    target_root: Path,
    report: ValidationReport,
) -> bool:
    target = target_root / NORMATIVE_ROOT_PATH
    try:
        target.mkdir(parents=True, exist_ok=True)
        for filename, data in normative_snapshot.items():
            (target / filename).write_bytes(data)
    except OSError as exc:
        report.errors.append(f"cannot create private normative-source snapshot: {exc}")
        return False
    return True


def _prepare_validation_boundary(
    boundary_root: Path,
    authority_bytes: bytes,
    authority_schema_bytes: bytes,
    project_application_schema_bytes: bytes,
    normative_snapshot: dict[str, bytes],
    report: ValidationReport,
) -> bool:
    try:
        (boundary_root / "schemas").mkdir(parents=True, exist_ok=True)
        (boundary_root / AUTHORITY_REGISTRY_PATH).write_bytes(authority_bytes)
        (boundary_root / AUTHORITY_SCHEMA_PATH).write_bytes(authority_schema_bytes)
        (boundary_root / PROJECT_APPLICATION_SCHEMA_PATH).write_bytes(
            project_application_schema_bytes
        )
    except OSError as exc:
        report.errors.append(f"cannot create private validation boundary: {exc}")
        return False
    return _write_normative_snapshot(normative_snapshot, boundary_root, report)


def _load_yaml_mapping(path: Path, label: str, report: ValidationReport) -> dict[str, Any] | None:
    try:
        with path.open("r", encoding="utf-8") as stream:
            data = yaml.safe_load(stream)
    except (OSError, UnicodeError, yaml.YAMLError) as exc:
        report.errors.append(f"{label}: cannot load validated YAML snapshot: {exc}")
        return None
    if not isinstance(data, dict):
        report.errors.append(f"{label}: validated YAML snapshot root is not a mapping")
        return None
    return data


def _load_project_application_mapping(
    path: Path,
    report: ValidationReport,
) -> dict[str, Any] | None:
    try:
        text = path.read_text(encoding="utf-8")
        data = yaml.load(text, Loader=StrictProjectApplicationLoader)
    except (OSError, UnicodeError, yaml.YAMLError) as exc:
        report.errors.append(
            f"validated Project Application snapshot could not be loaded: {exc}"
        )
        return None
    if not isinstance(data, dict) or not isinstance(data.get("records"), list):
        report.errors.append(
            "validated Project Application snapshot did not expose a records list"
        )
        return None
    return data


def _validate_canonical_order(profile: dict[str, Any], report: ValidationReport) -> None:
    errors_before = len(report.errors)

    if tuple(profile.keys()) != ROOT_FIELD_ORDER:
        report.errors.append(
            "profile root: non-canonical mapping order; expected "
            + ", ".join(ROOT_FIELD_ORDER)
        )

    entries = profile["entries"]
    observed_ids = [entry["scaf_authority_id"] for entry in entries]
    if observed_ids != sorted(observed_ids):
        report.errors.append(
            "entries: non-canonical order; entries must be ordered by exact "
            "scaf_authority_id ascending"
        )

    for index, entry in enumerate(entries):
        state = entry["profile_state"]
        expected_order = (
            RECORDED_ENTRY_FIELD_ORDER if state in RECORDED_STATES else ABSENCE_ENTRY_FIELD_ORDER
        )
        if tuple(entry.keys()) != expected_order:
            report.errors.append(
                f"entries[{index}]: non-canonical mapping order for profile_state {state!r}; "
                f"expected {', '.join(expected_order)}"
            )

    report.canonical_order_valid = len(report.errors) == errors_before


def _authority_index_and_domain(
    authority_data: dict[str, Any],
    source_release: str,
    report: ValidationReport,
) -> tuple[dict[str, dict[str, Any]], tuple[str, ...]]:
    records = authority_data.get("records")
    if not isinstance(records, list):
        report.errors.append("validated authority registry did not expose a records list")
        return {}, ()

    authority_index: dict[str, dict[str, Any]] = {}
    domain_ids: list[str] = []
    for record in records:
        if not isinstance(record, dict) or not isinstance(record.get("id"), str):
            continue
        authority_index[record["id"]] = record
        if (
            record.get("authority_class") == EXPECTED_AUTHORITY_CLASS
            and record.get("source_release") == source_release
        ):
            domain_ids.append(record["id"])

    if not domain_ids:
        report.errors.append(
            f"profile scaf_source_release {source_release!r} has no validated "
            "Project-Applicable Obligation domain in the authority registry"
        )

    return authority_index, tuple(sorted(domain_ids))


def _validate_domain(
    profile: dict[str, Any],
    authority_index: dict[str, dict[str, Any]],
    domain_ids: tuple[str, ...],
    report: ValidationReport,
) -> None:
    errors_before = len(report.errors)
    entries = profile["entries"]
    source_release = profile["scaf_source_release"]
    entry_ids = [entry["scaf_authority_id"] for entry in entries]

    seen: set[str] = set()
    duplicate_ids: set[str] = set()
    for authority_id in entry_ids:
        if authority_id in seen:
            duplicate_ids.add(authority_id)
        seen.add(authority_id)
    if duplicate_ids:
        report.errors.append(
            "profile entries contain duplicate scaf_authority_id value(s): "
            + ", ".join(sorted(duplicate_ids))
        )

    domain_set = set(domain_ids)
    entry_set = set(entry_ids)

    for index, entry in enumerate(entries):
        authority_id = entry["scaf_authority_id"]
        authority = authority_index.get(authority_id)
        if authority is None:
            report.errors.append(
                f"entries[{index}].scaf_authority_id: unresolved SCAF authority {authority_id!r}"
            )
            continue
        authority_class = authority.get("authority_class")
        if authority_class != EXPECTED_AUTHORITY_CLASS:
            report.errors.append(
                f"entries[{index}].scaf_authority_id: {authority_id!r} resolves to "
                f"authority_class {authority_class!r}; expected {EXPECTED_AUTHORITY_CLASS!r}"
            )
        actual_release = authority.get("source_release")
        if actual_release != source_release:
            report.errors.append(
                f"entries[{index}].scaf_authority_id: {authority_id!r} source_release "
                f"{actual_release!r} does not match profile scaf_source_release "
                f"{source_release!r}"
            )

    missing = sorted(domain_set - entry_set)
    extra = sorted(entry_set - domain_set)
    if missing:
        report.errors.append(
            f"profile omits {len(missing)} Project-Applicable Obligation(s) from the "
            f"validated {source_release} domain: {', '.join(missing[:10])}"
            + (" ..." if len(missing) > 10 else "")
        )
    if extra:
        report.errors.append(
            f"profile contains {len(extra)} entry ID(s) outside the validated "
            f"{source_release} Project-Applicable Obligation domain: {', '.join(extra[:10])}"
            + (" ..." if len(extra) > 10 else "")
        )
    if len(entries) != len(domain_ids):
        report.errors.append(
            f"profile entry count {len(entries)} does not match validated PAO domain size "
            f"{len(domain_ids)} for {source_release}"
        )

    report.domain_valid = len(report.errors) == errors_before


def _validate_recorded_and_absence_state(
    profile: dict[str, Any],
    project_application: dict[str, Any],
    report: ValidationReport,
) -> None:
    trace_errors_before = len(report.errors)
    records = project_application["records"]
    by_record_id = {record["record_id"]: record for record in records}
    by_pair = {
        (record["scaf_authority_id"], record["project_scope_ref"]): record
        for record in records
    }

    scope = profile["project_scope_ref"]
    source_release = profile["scaf_source_release"]
    absence_errors: list[str] = []

    for index, entry in enumerate(profile["entries"]):
        authority_id = entry["scaf_authority_id"]
        state = entry["profile_state"]
        pair = (authority_id, scope)

        if state in RECORDED_STATES:
            record_id = entry["project_application_record_id"]
            record = by_record_id.get(record_id)
            if record is None:
                report.errors.append(
                    f"entries[{index}].project_application_record_id: {record_id!r} does not "
                    "resolve in the validated selected Project Application snapshot"
                )
                continue
            if record["scaf_authority_id"] != authority_id:
                report.errors.append(
                    f"entries[{index}]: Project Application record {record_id!r} targets "
                    f"{record['scaf_authority_id']!r}, not profile authority {authority_id!r}"
                )
            if record["project_scope_ref"] != scope:
                report.errors.append(
                    f"entries[{index}]: Project Application record {record_id!r} scope "
                    f"{record['project_scope_ref']!r} does not match profile scope {scope!r}"
                )
            if record["applicability"] != state:
                report.errors.append(
                    f"entries[{index}]: profile_state {state!r} does not match Project "
                    f"Application record {record_id!r} applicability {record['applicability']!r}"
                )
            if record["scaf_source_release"] != source_release:
                report.errors.append(
                    f"entries[{index}]: Project Application record {record_id!r} source release "
                    f"{record['scaf_source_release']!r} does not match profile source release "
                    f"{source_release!r}"
                )
            pair_record = by_pair.get(pair)
            if pair_record is None:
                report.errors.append(
                    f"entries[{index}]: no current Project Application record exists for exact "
                    f"pair {pair!r} despite recorded profile state {state!r}"
                )
            elif pair_record["record_id"] != record_id:
                report.errors.append(
                    f"entries[{index}]: exact pair {pair!r} resolves to Project Application "
                    f"record {pair_record['record_id']!r}, not {record_id!r}"
                )
        else:
            record = by_pair.get(pair)
            if record is not None:
                absence_errors.append(
                    f"entries[{index}]: no_current_disposition is contradicted by current "
                    f"Project Application record {record['record_id']!r} for exact pair {pair!r}"
                )

    report.recorded_trace_valid = len(report.errors) == trace_errors_before
    report.errors.extend(absence_errors)
    report.absence_proof_valid = not absence_errors


def _resolve_input_path(repo_root: Path, path: Path | None, default: Path) -> Path:
    if path is None:
        return (repo_root / default).resolve()
    if path.is_absolute():
        return path.resolve()
    return (Path.cwd() / path).resolve()


def validate_effective_project_profile(
    repo_root: Path,
    profile_path: Path | None = None,
    project_application_path: Path | None = None,
) -> ValidationReport:
    """Validate one profile against selected source snapshots and one SCAF repo.

    Callers may select the profile and Project Application source datasets.
    The repository root owns the accepted profile schema, Project Application
    schema, frozen authority registry/schema, and canonical normative sources.
    """

    repo_root = repo_root.resolve()
    profile_path = _resolve_input_path(repo_root, profile_path, DEFAULT_PROFILE_PATH)
    project_application_path = _resolve_input_path(
        repo_root, project_application_path, DEFAULT_PROJECT_APPLICATION_PATH
    )

    report = ValidationReport()

    profile_bytes = _read_required_bytes(
        profile_path, "Effective Project Profile", report
    )
    if profile_bytes is None:
        return report

    profile_schema_bytes = _read_required_bytes(
        repo_root / PROFILE_SCHEMA_PATH,
        "Effective Project Profile schema",
        report,
    )
    if profile_schema_bytes is None:
        return report

    project_application_bytes = _read_required_bytes(
        project_application_path,
        "Project Application",
        report,
    )
    if project_application_bytes is None:
        return report

    authority_bytes = _read_required_bytes(
        repo_root / AUTHORITY_REGISTRY_PATH,
        "authority registry",
        report,
    )
    authority_schema_bytes = _read_required_bytes(
        repo_root / AUTHORITY_SCHEMA_PATH,
        "authority schema",
        report,
    )
    project_application_schema_bytes = _read_required_bytes(
        repo_root / PROJECT_APPLICATION_SCHEMA_PATH,
        "Project Application schema",
        report,
    )
    if None in (authority_bytes, authority_schema_bytes, project_application_schema_bytes):
        return report

    normative_snapshot = _read_normative_snapshot(repo_root, report)
    if normative_snapshot is None:
        return report

    with tempfile.TemporaryDirectory(prefix="scaf-effective-profile-validator-") as temp_dir:
        temp_root = Path(temp_dir)
        profile_snapshot = temp_root / "effective-project-profile.yaml"
        project_snapshot = temp_root / "project-application.yaml"
        validation_root = temp_root / "validation-repo"
        profile_snapshot.write_bytes(profile_bytes)
        project_snapshot.write_bytes(project_application_bytes)

        profile_data = _load_profile_snapshot(profile_snapshot, report)
        if profile_data is None:
            return report

        if not _validate_profile_schema(
            profile_data,
            profile_schema_bytes,
            (repo_root / PROFILE_SCHEMA_PATH).as_posix(),
            report,
        ):
            return report

        if not isinstance(profile_data, dict):  # schema should already prove this
            report.errors.append("Effective Project Profile root is not a mapping")
            return report

        entries = profile_data["entries"]
        report.entry_count = len(entries)

        _validate_canonical_order(profile_data, report)

        actual_digest = hashlib.sha256(project_application_bytes).hexdigest()
        expected_digest = profile_data["project_application_source_sha256"]
        if actual_digest != expected_digest:
            report.errors.append(
                "project_application_source_sha256 mismatch: profile records "
                f"{expected_digest!r}, selected Project Application snapshot is {actual_digest!r}"
            )
        else:
            report.source_digest_valid = True

        if not _prepare_validation_boundary(
            validation_root,
            authority_bytes,
            authority_schema_bytes,
            project_application_schema_bytes,
            normative_snapshot,
            report,
        ):
            return report

        authority_snapshot = validation_root / AUTHORITY_REGISTRY_PATH
        authority_schema_snapshot = validation_root / AUTHORITY_SCHEMA_PATH
        authority_report = validate_registry(
            validation_root,
            authority_snapshot,
            authority_schema_snapshot,
        )
        if not authority_report.passed:
            report.errors.append(
                "frozen authority-registry source-aware proof failed; profile source validation "
                "cannot proceed"
            )
            for error in authority_report.errors:
                report.errors.append(f"authority-registry: {error}")
            return report
        report.authority_registry_valid = True

        project_report = validate_project_application(validation_root, project_snapshot)
        if not project_report.passed:
            report.errors.append(
                "selected Project Application snapshot failed accepted rc07 validation; "
                "profile source validation cannot proceed"
            )
            for error in project_report.errors:
                report.errors.append(f"Project Application: {error}")
            return report
        report.project_application_valid = True

        authority_data = _load_yaml_mapping(
            authority_snapshot,
            "validated authority registry",
            report,
        )
        project_application_data = _load_project_application_mapping(
            project_snapshot,
            report,
        )
        if authority_data is None or project_application_data is None:
            return report

        authority_index, domain_ids = _authority_index_and_domain(
            authority_data,
            profile_data["scaf_source_release"],
            report,
        )
        _validate_domain(profile_data, authority_index, domain_ids, report)
        _validate_recorded_and_absence_state(
            profile_data,
            project_application_data,
            report,
        )

    return report


def _default_repo_root() -> Path:
    return Path(__file__).resolve().parents[2]


def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description=(
            "Validate SCAF Effective Project Profile representation/source conformance. "
            "Repository-owned schemas, frozen authority sources, and normative sources "
            "are fixed to this reviewed SCAF repository."
        )
    )
    parser.add_argument(
        "--profile",
        type=Path,
        default=None,
        help=(
            "Effective Project Profile YAML to validate. Defaults to "
            "examples/effective-project-profile.yaml."
        ),
    )
    parser.add_argument(
        "--project-application",
        type=Path,
        default=None,
        help=(
            "Project Application YAML source snapshot referenced by the profile. Defaults to "
            "examples/project-application.yaml."
        ),
    )
    return parser


def main(argv: list[str] | None = None) -> int:
    args = _build_parser().parse_args(argv)
    repo_root = _default_repo_root()
    profile_path = _resolve_input_path(repo_root, args.profile, DEFAULT_PROFILE_PATH)
    project_path = _resolve_input_path(
        repo_root, args.project_application, DEFAULT_PROJECT_APPLICATION_PATH
    )

    report = validate_effective_project_profile(repo_root, profile_path, project_path)

    print(f"Effective Project Profile: {profile_path.as_posix()}")
    print(f"Project Application:       {project_path.as_posix()}")
    print(f"Entries: {report.entry_count}")
    print(f"Profile YAML policy:       {'PASS' if report.loader_policy_valid else 'FAIL'}")
    print(f"Profile schema:            {'PASS' if report.schema_valid else 'FAIL'}")
    print(f"Project source SHA-256:    {'PASS' if report.source_digest_valid else 'FAIL'}")
    print(f"Authority registry proof:  {'PASS' if report.authority_registry_valid else 'FAIL'}")
    print(f"Project Application proof: {'PASS' if report.project_application_valid else 'FAIL'}")
    print(f"Complete PAO domain:       {'PASS' if report.domain_valid else 'FAIL'}")
    print(f"Canonical ordering:        {'PASS' if report.canonical_order_valid else 'FAIL'}")
    print(f"Recorded-state trace:      {'PASS' if report.recorded_trace_valid else 'FAIL'}")
    print(f"Absence proof:             {'PASS' if report.absence_proof_valid else 'FAIL'}")
    print(f"Errors: {len(report.errors)}")
    for error in report.errors:
        print(f"ERROR: {error}")
    print(
        "PROFILE REPRESENTATION/SOURCE RESULT: "
        + ("PASS" if report.passed else "FAIL")
    )
    return 0 if report.passed else 1


if __name__ == "__main__":  # pragma: no cover - CLI entry point
    sys.exit(main())
