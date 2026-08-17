#!/usr/bin/env python3
"""Run the bounded SCAF executable-governance CI gate from external trust input.

This gate is an enforcement orchestrator, not semantic authority. It requires an
external trust bundle stored outside the repository, verifies the identities of
all control-plane artifacts, materializes the accepted external-pin document in
a temporary location, and then executes the three accepted controls in fixed
order:

1. external identity pin verification;
2. frozen-baseline byte integrity;
3. authority-registry/schema/source-aware validation.

The production CLI binds repository context to the lexical current checkout root,
requires the canonical gate path under that root to have no symlink components,
and accepts no caller-selected repository root, artifact set, stage order, schema,
manifest, or hash algorithm.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import subprocess
import sys
import tempfile
import stat
from dataclasses import dataclass
from pathlib import Path
from typing import Any

EXPECTED_BUNDLE_KEYS = {
    "trust_version",
    "trust_scope",
    "hash_algorithm",
    "artifacts",
    "external_pin",
}
EXPECTED_ARTIFACT_KEYS = {"path", "sha256"}
EXPECTED_TRUST_VERSION = 1
EXPECTED_TRUST_SCOPE = "scaf_executable_governance_ci"
EXPECTED_HASH_ALGORITHM = "sha256"
EXPECTED_ARTIFACTS = {
    "tools/scaf_ci_gate/gate.py",
    "tools/scaf_external_pin/checker.py",
    "release-integrity/frozen-baseline-manifest.json",
    "tools/scaf_release_integrity/checker.py",
    "tools/scaf_validator/validator.py",
    "schemas/authority-registry.schema.json",
}
EXPECTED_EXTERNAL_PIN_KEYS = {"pin_version", "pin_scope", "hash_algorithm", "artifacts"}
EXPECTED_EXTERNAL_PIN_ARTIFACTS = {
    "release-integrity/frozen-baseline-manifest.json",
    "tools/scaf_release_integrity/checker.py",
}
EXPECTED_EXTERNAL_PIN_VERSION = 1
EXPECTED_EXTERNAL_PIN_SCOPE = "scaf_frozen_baseline_release_integrity"


@dataclass(frozen=True)
class GateStageResult:
    name: str
    returncode: int
    stdout: str
    stderr: str


@dataclass(frozen=True)
class GateReport:
    passed: bool
    errors: tuple[str, ...]
    artifact_summaries: tuple[str, ...]
    stages: tuple[GateStageResult, ...]


def _production_repo_root() -> Path:
    """Bind the production CLI to the lexical current checkout root.

    The workflow and documented local invocation run the gate from repository root.
    We intentionally do not derive the root from ``__file__.resolve()`` because a
    symlinked parent directory could otherwise pivot root discovery into a shadow
    repository before the gate has a chance to validate path topology.
    """

    repo_root = Path.cwd().absolute()
    expected_gate = _safe_repo_artifact(repo_root, "tools/scaf_ci_gate/gate.py")
    running_gate = Path(__file__).resolve()
    if expected_gate != running_gate:
        raise ValueError(
            "production gate must execute from the repository root using the canonical "
            "non-symlinked tools/scaf_ci_gate/gate.py path"
        )
    return repo_root


def _sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def _unique_object_pairs(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in pairs:
        if key in result:
            raise ValueError(f"duplicate JSON object key: {key}")
        result[key] = value
    return result


def load_trust_bundle(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as handle:
        data = json.load(handle, object_pairs_hook=_unique_object_pairs)
    if not isinstance(data, dict):
        raise ValueError("CI trust bundle root must be an object")
    return data


def _validate_external_file(path: Path, repo_root: Path) -> Path:
    raw = path.expanduser()
    if not raw.is_absolute():
        raw = Path.cwd() / raw
    if raw.is_symlink():
        raise ValueError("CI trust bundle must not be a symlink")
    resolved = raw.resolve()
    try:
        resolved.relative_to(repo_root.resolve())
    except ValueError:
        pass
    else:
        raise ValueError("CI trust bundle must be stored outside the SCAF repository")
    if not resolved.is_file():
        raise ValueError("CI trust bundle is missing or not a regular file")
    return resolved


def _safe_repo_artifact(repo_root: Path, relative: str) -> Path:
    """Resolve a fixed repository artifact without following repository-internal symlinks.

    Every repository-relative component is inspected with lstat before resolution.
    Parent components must be real directories and the terminal component must be a
    real regular file. This prevents a trusted control path from pivoting through a
    symlinked parent into a pristine nested shadow repository.
    """

    rel = Path(relative)
    if rel.is_absolute():
        raise ValueError(f"absolute repository artifact path is not allowed: {relative}")
    if not rel.parts or any(part in {"", ".", ".."} for part in rel.parts):
        raise ValueError(f"unsafe repository artifact path is not allowed: {relative}")

    root = repo_root.absolute()
    if root.is_symlink():
        raise ValueError("repository root must not be a symlink")
    if not root.is_dir():
        raise ValueError("repository root is missing or not a directory")

    current = root
    last_index = len(rel.parts) - 1
    for index, part in enumerate(rel.parts):
        current = current / part
        try:
            mode = os.lstat(current).st_mode
        except FileNotFoundError as exc:
            raise ValueError(f"CI control artifact is missing: {relative}") from exc
        except OSError as exc:
            raise ValueError(f"cannot inspect CI control artifact path: {relative}: {exc}") from exc

        component_rel = current.relative_to(root).as_posix()
        if stat.S_ISLNK(mode):
            raise ValueError(
                f"CI control artifact path component must not be a symlink: {component_rel} "
                f"(artifact {relative})"
            )
        if index < last_index:
            if not stat.S_ISDIR(mode):
                raise ValueError(
                    f"CI control artifact parent component is not a directory: {component_rel} "
                    f"(artifact {relative})"
                )
        elif not stat.S_ISREG(mode):
            raise ValueError(f"CI control artifact is missing/not regular: {relative}")

    resolved = current.resolve(strict=True)
    root_resolved = root.resolve(strict=True)
    try:
        resolved.relative_to(root_resolved)
    except ValueError as exc:
        raise ValueError(f"CI control artifact path escapes repository root: {relative}") from exc
    return resolved


def _reported_repository(stdout: str) -> Path:
    reported = [
        line.split(":", 1)[1].strip()
        for line in stdout.splitlines()
        if line.startswith("Repository:")
    ]
    if len(reported) != 1 or not reported[0]:
        raise ValueError("stage must report exactly one Repository: line")
    return Path(reported[0]).resolve()


def _assert_stage_repository(stage: GateStageResult, repo_root: Path) -> None:
    observed = _reported_repository(stage.stdout)
    expected = repo_root.resolve(strict=True)
    if observed != expected:
        raise ValueError(
            f"stage repository-root mismatch for {stage.name}: expected {expected}, observed {observed}"
        )


def _valid_sha256(value: Any) -> bool:
    return (
        isinstance(value, str)
        and len(value) == 64
        and all(c in "0123456789abcdef" for c in value)
    )


def validate_trust_bundle_data(bundle: dict[str, Any], repo_root: Path) -> tuple[list[str], list[str], dict[str, str]]:
    errors: list[str] = []
    summaries: list[str] = []
    pinned_hashes: dict[str, str] = {}

    if set(bundle) != EXPECTED_BUNDLE_KEYS:
        errors.append(
            "trust bundle keys mismatch: expected "
            f"{sorted(EXPECTED_BUNDLE_KEYS)}, observed {sorted(bundle)}"
        )
    if bundle.get("trust_version") != EXPECTED_TRUST_VERSION:
        errors.append("trust_version must be 1")
    if bundle.get("trust_scope") != EXPECTED_TRUST_SCOPE:
        errors.append(f"trust_scope must be {EXPECTED_TRUST_SCOPE}")
    if bundle.get("hash_algorithm") != EXPECTED_HASH_ALGORITHM:
        errors.append("hash_algorithm must be sha256")

    artifacts = bundle.get("artifacts")
    if not isinstance(artifacts, list):
        errors.append("artifacts must be an array")
        artifacts = []
    if len(artifacts) != len(EXPECTED_ARTIFACTS):
        errors.append(f"artifacts count must be {len(EXPECTED_ARTIFACTS)}")

    observed: set[str] = set()
    for artifact in artifacts:
        if not isinstance(artifact, dict):
            errors.append("artifact entry must be an object")
            continue
        if set(artifact) != EXPECTED_ARTIFACT_KEYS:
            errors.append("artifact entry keys mismatch")
        rel = artifact.get("path")
        digest = artifact.get("sha256")
        if not isinstance(rel, str) or rel not in EXPECTED_ARTIFACTS:
            errors.append(f"unsupported CI control artifact path: {rel!r}")
            continue
        if rel in observed:
            errors.append(f"duplicate CI control artifact path: {rel}")
            continue
        observed.add(rel)
        if not _valid_sha256(digest):
            errors.append(f"invalid SHA-256 value for {rel}")
            continue
        pinned_hashes[rel] = digest

    for rel in sorted(EXPECTED_ARTIFACTS - observed):
        errors.append(f"missing CI control artifact: {rel}")

    external_pin = bundle.get("external_pin")
    if not isinstance(external_pin, dict):
        errors.append("external_pin must be an object")
        external_pin = {}
    if set(external_pin) != EXPECTED_EXTERNAL_PIN_KEYS:
        errors.append("external_pin keys mismatch")
    if external_pin.get("pin_version") != EXPECTED_EXTERNAL_PIN_VERSION:
        errors.append("external_pin.pin_version must be 1")
    if external_pin.get("pin_scope") != EXPECTED_EXTERNAL_PIN_SCOPE:
        errors.append(f"external_pin.pin_scope must be {EXPECTED_EXTERNAL_PIN_SCOPE}")
    if external_pin.get("hash_algorithm") != EXPECTED_HASH_ALGORITHM:
        errors.append("external_pin.hash_algorithm must be sha256")

    ext_artifacts = external_pin.get("artifacts")
    if not isinstance(ext_artifacts, list):
        errors.append("external_pin.artifacts must be an array")
        ext_artifacts = []
    if len(ext_artifacts) != len(EXPECTED_EXTERNAL_PIN_ARTIFACTS):
        errors.append(f"external_pin.artifacts count must be {len(EXPECTED_EXTERNAL_PIN_ARTIFACTS)}")

    ext_observed: set[str] = set()
    for artifact in ext_artifacts:
        if not isinstance(artifact, dict):
            errors.append("external_pin artifact entry must be an object")
            continue
        if set(artifact) != EXPECTED_ARTIFACT_KEYS:
            errors.append("external_pin artifact entry keys mismatch")
        rel = artifact.get("path")
        digest = artifact.get("sha256")
        if not isinstance(rel, str) or rel not in EXPECTED_EXTERNAL_PIN_ARTIFACTS:
            errors.append(f"unsupported external_pin artifact path: {rel!r}")
            continue
        if rel in ext_observed:
            errors.append(f"duplicate external_pin artifact path: {rel}")
            continue
        ext_observed.add(rel)
        if not _valid_sha256(digest):
            errors.append(f"invalid external_pin SHA-256 value for {rel}")
            continue
        top_digest = pinned_hashes.get(rel)
        if top_digest is not None and digest != top_digest:
            errors.append(f"external_pin SHA-256 for {rel} must equal top-level CI trust pin")

    for rel in sorted(EXPECTED_EXTERNAL_PIN_ARTIFACTS - ext_observed):
        errors.append(f"external_pin missing artifact: {rel}")

    for rel in sorted(EXPECTED_ARTIFACTS):
        try:
            path = _safe_repo_artifact(repo_root, rel)
        except ValueError as exc:
            errors.append(str(exc))
            summaries.append(f"{rel}: MISMATCH")
            continue
        expected = pinned_hashes.get(rel)
        actual = _sha256_file(path)
        if expected is None or actual != expected:
            errors.append(f"CI control SHA-256 mismatch for {rel}: expected {expected}, observed {actual}")
            summaries.append(f"{rel}: MISMATCH")
        else:
            summaries.append(f"{rel}: MATCH")

    return errors, summaries, pinned_hashes


def _run_stage(name: str, command: list[str], cwd: Path) -> GateStageResult:
    env = os.environ.copy()
    env["PYTHONDONTWRITEBYTECODE"] = "1"
    completed = subprocess.run(
        command,
        cwd=cwd,
        env=env,
        text=True,
        capture_output=True,
        check=False,
    )
    return GateStageResult(
        name=name,
        returncode=completed.returncode,
        stdout=completed.stdout,
        stderr=completed.stderr,
    )


def execute_gate(bundle_path: Path, repo_root: Path) -> GateReport:
    errors: list[str] = []
    summaries: list[str] = []
    stages: list[GateStageResult] = []

    try:
        external_bundle_path = _validate_external_file(bundle_path, repo_root)
        bundle = load_trust_bundle(external_bundle_path)
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        return GateReport(False, (str(exc),), (), ())

    bundle_errors, artifact_summaries, _ = validate_trust_bundle_data(bundle, repo_root)
    errors.extend(bundle_errors)
    summaries.extend(artifact_summaries)
    if errors:
        return GateReport(False, tuple(errors), tuple(summaries), ())

    with tempfile.TemporaryDirectory(prefix="scaf-ci-gate-") as temp_dir:
        external_pin_path = Path(temp_dir) / "trusted-external-pin.json"
        external_pin_path.write_text(
            json.dumps(bundle["external_pin"], indent=2, sort_keys=True) + "\n",
            encoding="utf-8",
        )

        try:
            external_pin_checker = _safe_repo_artifact(repo_root, "tools/scaf_external_pin/checker.py")
            release_integrity_checker = _safe_repo_artifact(repo_root, "tools/scaf_release_integrity/checker.py")
            semantic_validator = _safe_repo_artifact(repo_root, "tools/scaf_validator/validator.py")
        except ValueError as exc:
            errors.append(str(exc))
            return GateReport(False, tuple(errors), tuple(summaries), ())

        commands = [
            (
                "external-pin verification",
                [
                    sys.executable,
                    "-I",
                    str(external_pin_checker),
                    "--pin-file",
                    str(external_pin_path),
                ],
            ),
            (
                "frozen-baseline release integrity",
                [sys.executable, "-I", str(release_integrity_checker)],
            ),
            (
                "authority-registry semantic/structural validation",
                [sys.executable, "-I", str(semantic_validator)],
            ),
        ]

        for stage_name, command in commands:
            # Re-check the executable path immediately before stage execution so a
            # path-topology change cannot silently reuse the earlier trust pass.
            try:
                _safe_repo_artifact(repo_root, Path(command[2]).relative_to(repo_root).as_posix())
            except (ValueError, OSError) as exc:
                errors.append(str(exc))
                break

            result = _run_stage(stage_name, command, repo_root)
            stages.append(result)
            if result.returncode != 0:
                errors.append(f"stage failed: {stage_name} (exit {result.returncode})")
                break
            try:
                _assert_stage_repository(result, repo_root)
            except ValueError as exc:
                errors.append(str(exc))
                break

    return GateReport(
        passed=not errors,
        errors=tuple(errors),
        artifact_summaries=tuple(summaries),
        stages=tuple(stages),
    )


def main() -> int:
    parser = argparse.ArgumentParser(
        description=(
            "Run the SCAF executable-governance CI gate using an externally supplied trust bundle."
        )
    )
    parser.add_argument(
        "--trust-bundle",
        required=True,
        help="Path to a trusted CI JSON bundle stored outside the SCAF repository",
    )
    args = parser.parse_args()

    try:
        repo_root = _production_repo_root()
    except (OSError, ValueError) as exc:
        print("SCAF Executable Governance CI Gate")
        print(f"Repository: {Path.cwd().absolute()}")
        print(f"ERROR: {exc}")
        print("RESULT: FAIL")
        return 1

    report = execute_gate(Path(args.trust_bundle), repo_root)

    print("SCAF Executable Governance CI Gate")
    print(f"Repository: {repo_root.resolve()}")
    print(f"Trust bundle: {Path(args.trust_bundle).expanduser().resolve()}")
    print(f"Pinned control artifacts: {len(report.artifact_summaries)}")
    for summary in report.artifact_summaries:
        print(summary)
    for stage in report.stages:
        print(f"--- {stage.name} ---")
        if stage.stdout:
            print(stage.stdout.rstrip())
        if stage.stderr:
            print(stage.stderr.rstrip(), file=sys.stderr)
        print(f"Stage exit: {stage.returncode}")
    print(f"Errors: {len(report.errors)}")
    for error in report.errors:
        print(f"ERROR: {error}")
    print("RESULT: PASS" if report.passed else "RESULT: FAIL")
    return 0 if report.passed else 1


if __name__ == "__main__":
    sys.exit(main())
