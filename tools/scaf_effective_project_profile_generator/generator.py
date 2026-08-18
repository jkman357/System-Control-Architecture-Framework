#!/usr/bin/env python3
"""Generate deterministic SCAF Effective Project Profile YAML from validated inputs.

The generator owns the validation path for the selected Project Application and
repository-owned authority sources. It derives only the accepted rc09/rc10
profile projection for one exact project_scope_ref and self-validates the
result through the accepted rc12 source-aware profile validator before
returning or emitting bytes.

Generation is not applicability inference. Recorded profile states are copied
only from validated current Project Application records for the exact scope;
all other PAOs become the profile-only derived state no_current_disposition.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
import tempfile
from pathlib import Path
from typing import Any

try:
    import yaml
except ImportError as exc:  # pragma: no cover - CLI environment only
    raise SystemExit(
        "Missing dependency: PyYAML. Install "
        "tools/scaf_effective_project_profile_generator/requirements.txt"
    ) from exc

from tools.scaf_effective_project_profile_validator.validator import (
    validate_effective_project_profile,
)
from tools.scaf_project_application_validator.validator import (
    StrictProjectApplicationLoader,
    validate_project_application,
)
from tools.scaf_validator.validator import validate_registry

__all__ = (
    "EffectiveProjectProfileGenerationError",
    "generate_effective_project_profile",
    "main",
)

DEFAULT_PROJECT_APPLICATION_PATH = Path("examples/project-application.yaml")
PROFILE_SCHEMA_PATH = Path("schemas/effective-project-profile.schema.json")
PROJECT_APPLICATION_SCHEMA_PATH = Path("schemas/project-application.schema.json")
AUTHORITY_REGISTRY_PATH = Path("authority-registry.yaml")
AUTHORITY_SCHEMA_PATH = Path("schemas/authority-registry.schema.json")
NORMATIVE_ROOT_PATH = Path("docs/normative")
EXPECTED_AUTHORITY_CLASS = "Project-Applicable Obligation"
ABSENCE_STATE = "no_current_disposition"


class EffectiveProjectProfileGenerationError(RuntimeError):
    """Raised when deterministic validated profile generation cannot complete."""


def _resolve_project_path(
    repo_root: Path,
    project_application_path: Path | None,
) -> Path:
    if project_application_path is None:
        return (repo_root / DEFAULT_PROJECT_APPLICATION_PATH).resolve()
    if project_application_path.is_absolute():
        return project_application_path.resolve()
    return (Path.cwd() / project_application_path).resolve()


def _read_utf8_bytes(path: Path, label: str) -> bytes:
    try:
        data = path.read_bytes()
        data.decode("utf-8")
        return data
    except (OSError, UnicodeError) as exc:
        raise EffectiveProjectProfileGenerationError(
            f"{label}: cannot read UTF-8 source {path.as_posix()}: {exc}"
        ) from exc


def _read_normative_snapshot(repo_root: Path) -> dict[str, bytes]:
    source_root = repo_root / NORMATIVE_ROOT_PATH
    snapshot: dict[str, bytes] = {}
    try:
        for source_file in sorted(source_root.glob("*.md")):
            data = source_file.read_bytes()
            data.decode("utf-8")
            snapshot[source_file.name] = data
    except (OSError, UnicodeError) as exc:
        raise EffectiveProjectProfileGenerationError(
            f"cannot read canonical normative-source snapshot: {exc}"
        ) from exc
    if not snapshot:
        raise EffectiveProjectProfileGenerationError(
            "canonical normative-source snapshot is empty"
        )
    return snapshot


def _prepare_validation_boundary(
    boundary_root: Path,
    *,
    authority_bytes: bytes,
    authority_schema_bytes: bytes,
    project_application_schema_bytes: bytes,
    profile_schema_bytes: bytes,
    normative_snapshot: dict[str, bytes],
) -> None:
    try:
        (boundary_root / "schemas").mkdir(parents=True, exist_ok=True)
        (boundary_root / "docs" / "normative").mkdir(parents=True, exist_ok=True)
        (boundary_root / AUTHORITY_REGISTRY_PATH).write_bytes(authority_bytes)
        (boundary_root / AUTHORITY_SCHEMA_PATH).write_bytes(authority_schema_bytes)
        (boundary_root / PROJECT_APPLICATION_SCHEMA_PATH).write_bytes(
            project_application_schema_bytes
        )
        (boundary_root / PROFILE_SCHEMA_PATH).write_bytes(profile_schema_bytes)
        for filename, data in normative_snapshot.items():
            (boundary_root / NORMATIVE_ROOT_PATH / filename).write_bytes(data)
    except OSError as exc:
        raise EffectiveProjectProfileGenerationError(
            f"cannot create private generation validation boundary: {exc}"
        ) from exc


def _load_json_bytes(data: bytes, label: str) -> dict[str, Any]:
    try:
        loaded = json.loads(data.decode("utf-8"))
    except (UnicodeError, json.JSONDecodeError) as exc:
        raise EffectiveProjectProfileGenerationError(
            f"{label}: cannot load JSON: {exc}"
        ) from exc
    if not isinstance(loaded, dict):
        raise EffectiveProjectProfileGenerationError(
            f"{label}: JSON root must be a mapping/object"
        )
    return loaded


def _load_validated_project_application(path: Path) -> dict[str, Any]:
    try:
        text = path.read_text(encoding="utf-8")
        data = yaml.load(text, Loader=StrictProjectApplicationLoader)
    except (OSError, UnicodeError, yaml.YAMLError) as exc:
        raise EffectiveProjectProfileGenerationError(
            f"validated Project Application snapshot could not be loaded: {exc}"
        ) from exc
    if not isinstance(data, dict) or not isinstance(data.get("records"), list):
        raise EffectiveProjectProfileGenerationError(
            "validated Project Application snapshot did not expose a records list"
        )
    return data


def _load_validated_authority_registry(path: Path) -> dict[str, Any]:
    try:
        with path.open("r", encoding="utf-8") as stream:
            data = yaml.safe_load(stream)
    except (OSError, UnicodeError, yaml.YAMLError) as exc:
        raise EffectiveProjectProfileGenerationError(
            f"validated authority-registry snapshot could not be loaded: {exc}"
        ) from exc
    if not isinstance(data, dict) or not isinstance(data.get("records"), list):
        raise EffectiveProjectProfileGenerationError(
            "validated authority-registry snapshot did not expose a records list"
        )
    return data


def _project_source_release(
    project_application: dict[str, Any],
    project_application_schema: dict[str, Any],
) -> str:
    releases = {
        record.get("scaf_source_release")
        for record in project_application["records"]
        if isinstance(record, dict) and isinstance(record.get("scaf_source_release"), str)
    }
    if len(releases) == 1:
        return next(iter(releases))
    if len(releases) > 1:
        raise EffectiveProjectProfileGenerationError(
            "validated Project Application snapshot exposes multiple scaf_source_release values"
        )

    # An empty records list is valid under the accepted current representation.
    # In that case the repository-owned accepted Project Application schema is the
    # only machine-readable source-release binding available to the generator.
    try:
        value = project_application_schema["$defs"]["projectApplicationRecord"][
            "properties"
        ]["scaf_source_release"]["const"]
    except (KeyError, TypeError) as exc:
        raise EffectiveProjectProfileGenerationError(
            "empty Project Application dataset has no record-level source release and the "
            "repository-owned Project Application schema does not expose one accepted "
            "scaf_source_release const"
        ) from exc
    if not isinstance(value, str) or not value:
        raise EffectiveProjectProfileGenerationError(
            "repository-owned Project Application schema exposes an invalid "
            "scaf_source_release const"
        )
    return value


def _profile_identity(profile_schema: dict[str, Any]) -> tuple[str, str]:
    try:
        properties = profile_schema["properties"]
        profile_kind = properties["profile_kind"]["const"]
        representation_release = properties["representation_release"]["const"]
    except (KeyError, TypeError) as exc:
        raise EffectiveProjectProfileGenerationError(
            "repository-owned Effective Project Profile schema does not expose accepted "
            "profile_kind / representation_release constants"
        ) from exc
    if not isinstance(profile_kind, str) or not profile_kind:
        raise EffectiveProjectProfileGenerationError("invalid profile_kind schema constant")
    if not isinstance(representation_release, str) or not representation_release:
        raise EffectiveProjectProfileGenerationError(
            "invalid representation_release schema constant"
        )
    return profile_kind, representation_release


def _derive_domain(
    authority_registry: dict[str, Any],
    source_release: str,
) -> tuple[str, ...]:
    domain = sorted(
        record["id"]
        for record in authority_registry["records"]
        if isinstance(record, dict)
        and isinstance(record.get("id"), str)
        and record.get("authority_class") == EXPECTED_AUTHORITY_CLASS
        and record.get("source_release") == source_release
    )
    if not domain:
        raise EffectiveProjectProfileGenerationError(
            f"validated authority registry exposes no Project-Applicable Obligation domain "
            f"for source release {source_release!r}"
        )
    return tuple(domain)


def _derive_entries(
    domain_ids: tuple[str, ...],
    project_application: dict[str, Any],
    project_scope_ref: str,
) -> list[dict[str, str]]:
    by_pair = {
        (record["scaf_authority_id"], record["project_scope_ref"]): record
        for record in project_application["records"]
    }
    entries: list[dict[str, str]] = []
    for authority_id in domain_ids:
        record = by_pair.get((authority_id, project_scope_ref))
        if record is None:
            entries.append(
                {
                    "scaf_authority_id": authority_id,
                    "profile_state": ABSENCE_STATE,
                }
            )
        else:
            entries.append(
                {
                    "scaf_authority_id": authority_id,
                    "profile_state": record["applicability"],
                    "project_application_record_id": record["record_id"],
                }
            )
    return entries


def _yaml_string(value: str) -> str:
    # JSON double-quoted strings are valid YAML scalars and provide a compact,
    # deterministic escaping rule independent of PyYAML emitter preferences.
    return json.dumps(value, ensure_ascii=False)


def _serialize_profile(
    *,
    profile_kind: str,
    representation_release: str,
    source_release: str,
    project_scope_ref: str,
    project_application_sha256: str,
    entries: list[dict[str, str]],
) -> bytes:
    lines = [
        f"profile_kind: {_yaml_string(profile_kind)}",
        f"representation_release: {_yaml_string(representation_release)}",
        f"scaf_source_release: {_yaml_string(source_release)}",
        f"project_scope_ref: {_yaml_string(project_scope_ref)}",
        f"project_application_source_sha256: {_yaml_string(project_application_sha256)}",
        "entries:",
    ]
    for entry in entries:
        lines.append(
            f"  - scaf_authority_id: {_yaml_string(entry['scaf_authority_id'])}"
        )
        lines.append(f"    profile_state: {_yaml_string(entry['profile_state'])}")
        record_id = entry.get("project_application_record_id")
        if record_id is not None:
            lines.append(
                f"    project_application_record_id: {_yaml_string(record_id)}"
            )
    return ("\n".join(lines) + "\n").encode("utf-8")


def generate_effective_project_profile(
    repo_root: Path,
    project_scope_ref: str,
    project_application_path: Path | None = None,
) -> bytes:
    """Generate one canonical profile from validated repository/source snapshots.

    The exact scope string is caller-selected project input. The Project
    Application schema, Effective Project Profile schema, frozen authority
    registry/schema, and normative source tree remain owned by repo_root.

    Returned bytes are emitted only after the generated representation passes
    the accepted rc12 representation/source-aware validator against the same
    captured Project Application snapshot and private repository boundary.
    """

    if not isinstance(project_scope_ref, str) or project_scope_ref == "":
        raise EffectiveProjectProfileGenerationError(
            "project_scope_ref must be a non-empty exact string"
        )

    repo_root = repo_root.resolve()
    project_application_path = _resolve_project_path(
        repo_root, project_application_path
    )

    project_application_bytes = _read_utf8_bytes(
        project_application_path, "Project Application"
    )
    project_application_schema_bytes = _read_utf8_bytes(
        repo_root / PROJECT_APPLICATION_SCHEMA_PATH,
        "Project Application schema",
    )
    profile_schema_bytes = _read_utf8_bytes(
        repo_root / PROFILE_SCHEMA_PATH,
        "Effective Project Profile schema",
    )
    authority_bytes = _read_utf8_bytes(
        repo_root / AUTHORITY_REGISTRY_PATH,
        "authority registry",
    )
    authority_schema_bytes = _read_utf8_bytes(
        repo_root / AUTHORITY_SCHEMA_PATH,
        "authority schema",
    )
    normative_snapshot = _read_normative_snapshot(repo_root)

    project_schema = _load_json_bytes(
        project_application_schema_bytes, "Project Application schema"
    )
    profile_schema = _load_json_bytes(
        profile_schema_bytes, "Effective Project Profile schema"
    )

    with tempfile.TemporaryDirectory(prefix="scaf-effective-profile-generation-") as tmp:
        boundary_root = Path(tmp) / "repo"
        boundary_root.mkdir(parents=True, exist_ok=True)
        _prepare_validation_boundary(
            boundary_root,
            authority_bytes=authority_bytes,
            authority_schema_bytes=authority_schema_bytes,
            project_application_schema_bytes=project_application_schema_bytes,
            profile_schema_bytes=profile_schema_bytes,
            normative_snapshot=normative_snapshot,
        )

        project_snapshot = boundary_root / "selected-project-application.yaml"
        project_snapshot.write_bytes(project_application_bytes)

        authority_report = validate_registry(
            boundary_root,
            boundary_root / AUTHORITY_REGISTRY_PATH,
            boundary_root / AUTHORITY_SCHEMA_PATH,
        )
        if not authority_report.passed:
            raise EffectiveProjectProfileGenerationError(
                "frozen authority snapshot failed source-aware validation: "
                + "; ".join(authority_report.errors)
            )

        project_report = validate_project_application(
            boundary_root, project_snapshot
        )
        if not project_report.passed:
            raise EffectiveProjectProfileGenerationError(
                "selected Project Application snapshot failed accepted rc07 validation: "
                + "; ".join(project_report.errors)
            )

        project_application = _load_validated_project_application(project_snapshot)
        authority_registry = _load_validated_authority_registry(
            boundary_root / AUTHORITY_REGISTRY_PATH
        )

        source_release = _project_source_release(
            project_application, project_schema
        )
        profile_kind, representation_release = _profile_identity(profile_schema)
        domain_ids = _derive_domain(authority_registry, source_release)
        entries = _derive_entries(
            domain_ids, project_application, project_scope_ref
        )
        source_sha256 = hashlib.sha256(project_application_bytes).hexdigest()

        generated_bytes = _serialize_profile(
            profile_kind=profile_kind,
            representation_release=representation_release,
            source_release=source_release,
            project_scope_ref=project_scope_ref,
            project_application_sha256=source_sha256,
            entries=entries,
        )

        generated_profile = boundary_root / "generated-effective-project-profile.yaml"
        generated_profile.write_bytes(generated_bytes)

        generated_report = validate_effective_project_profile(
            boundary_root,
            generated_profile,
            project_snapshot,
        )
        if not generated_report.passed:
            raise EffectiveProjectProfileGenerationError(
                "internally generated profile failed accepted rc12 representation/source "
                "validation: " + "; ".join(generated_report.errors)
            )

        return generated_bytes


def _default_repo_root() -> Path:
    return Path(__file__).resolve().parents[2]


def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description=(
            "Generate one deterministic SCAF Effective Project Profile from a "
            "validated Project Application snapshot and repository-owned SCAF "
            "authority sources. Output is canonical YAML on stdout."
        )
    )
    parser.add_argument(
        "--scope",
        required=True,
        help="Exact non-empty project_scope_ref to project. No scope resolution is performed.",
    )
    parser.add_argument(
        "--project-application",
        type=Path,
        default=None,
        help=(
            "Project Application YAML to consume. Defaults to "
            "examples/project-application.yaml."
        ),
    )
    return parser


def main(argv: list[str] | None = None) -> int:
    args = _build_parser().parse_args(argv)
    repo_root = _default_repo_root()
    try:
        generated = generate_effective_project_profile(
            repo_root,
            args.scope,
            args.project_application,
        )
    except EffectiveProjectProfileGenerationError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        print("PROFILE GENERATION RESULT: FAIL", file=sys.stderr)
        return 1

    sys.stdout.buffer.write(generated)
    return 0


if __name__ == "__main__":  # pragma: no cover - CLI entry point
    sys.exit(main())
