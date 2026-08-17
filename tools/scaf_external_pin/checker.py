from __future__ import annotations

import argparse
import hashlib
import json
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any


EXPECTED_PIN_KEYS = {"pin_version", "pin_scope", "hash_algorithm", "artifacts"}
EXPECTED_ARTIFACT_KEYS = {"path", "sha256"}
EXPECTED_PIN_VERSION = 1
EXPECTED_PIN_SCOPE = "scaf_frozen_baseline_release_integrity"
EXPECTED_HASH_ALGORITHM = "sha256"
EXPECTED_ARTIFACTS = {
    "release-integrity/frozen-baseline-manifest.json",
    "tools/scaf_release_integrity/checker.py",
}


@dataclass(frozen=True)
class ExternalPinReport:
    passed: bool
    pinned_artifact_count: int
    errors: tuple[str, ...]
    artifact_summaries: tuple[str, ...]


def _default_repo_root() -> Path:
    return Path(__file__).resolve().parents[2]


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


def load_external_pin(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as handle:
        data = json.load(handle, object_pairs_hook=_unique_object_pairs)
    if not isinstance(data, dict):
        raise ValueError("external pin document root must be an object")
    return data


def _safe_repo_path(repo_root: Path, relative: str) -> Path:
    rel = Path(relative)
    if rel.is_absolute():
        raise ValueError(f"absolute repository artifact path is not allowed: {relative}")

    lexical_candidate = repo_root / rel
    if lexical_candidate.is_symlink():
        raise ValueError(f"pinned repository artifact must not be a symlink: {relative}")

    resolved_candidate = lexical_candidate.resolve()
    try:
        resolved_candidate.relative_to(repo_root.resolve())
    except ValueError as exc:
        raise ValueError(f"repository artifact path escapes root: {relative}") from exc
    return resolved_candidate


def validate_external_pin_data(pin: dict[str, Any], repo_root: Path) -> ExternalPinReport:
    errors: list[str] = []
    summaries: list[str] = []

    if set(pin) != EXPECTED_PIN_KEYS:
        errors.append(
            "pin keys mismatch: expected "
            f"{sorted(EXPECTED_PIN_KEYS)}, observed {sorted(pin)}"
        )
    if pin.get("pin_version") != EXPECTED_PIN_VERSION:
        errors.append("pin_version must be 1")
    if pin.get("pin_scope") != EXPECTED_PIN_SCOPE:
        errors.append(f"pin_scope must be {EXPECTED_PIN_SCOPE}")
    if pin.get("hash_algorithm") != EXPECTED_HASH_ALGORITHM:
        errors.append("hash_algorithm must be sha256")

    artifacts = pin.get("artifacts")
    if not isinstance(artifacts, list):
        errors.append("artifacts must be an array")
        artifacts = []
    if len(artifacts) != len(EXPECTED_ARTIFACTS):
        errors.append(f"artifacts count must be {len(EXPECTED_ARTIFACTS)}")

    observed_paths: set[str] = set()
    pinned_hashes: dict[str, str] = {}
    for artifact in artifacts:
        if not isinstance(artifact, dict):
            errors.append("artifact entry must be an object")
            continue
        if set(artifact) != EXPECTED_ARTIFACT_KEYS:
            errors.append("artifact entry keys mismatch")
        rel = artifact.get("path")
        digest = artifact.get("sha256")
        if not isinstance(rel, str) or rel not in EXPECTED_ARTIFACTS:
            errors.append(f"unsupported pinned artifact path: {rel!r}")
            continue
        if rel in observed_paths:
            errors.append(f"duplicate pinned artifact path: {rel}")
            continue
        observed_paths.add(rel)
        if not isinstance(digest, str) or len(digest) != 64 or any(c not in "0123456789abcdef" for c in digest):
            errors.append(f"invalid SHA-256 value for {rel}")
            continue
        pinned_hashes[rel] = digest

    missing = sorted(EXPECTED_ARTIFACTS - observed_paths)
    extra = sorted(observed_paths - EXPECTED_ARTIFACTS)
    for rel in missing:
        errors.append(f"missing pinned artifact: {rel}")
    for rel in extra:
        errors.append(f"unexpected pinned artifact: {rel}")

    for rel in sorted(EXPECTED_ARTIFACTS):
        try:
            artifact_path = _safe_repo_path(repo_root, rel)
        except ValueError as exc:
            errors.append(str(exc))
            summaries.append(f"{rel}: MISMATCH")
            continue
        if artifact_path.is_symlink():
            errors.append(f"pinned repository artifact must not be a symlink: {rel}")
            summaries.append(f"{rel}: MISMATCH")
            continue
        if not artifact_path.is_file():
            errors.append(f"pinned repository artifact is missing/not regular: {rel}")
            summaries.append(f"{rel}: MISMATCH")
            continue
        expected = pinned_hashes.get(rel)
        actual = _sha256_file(artifact_path)
        if expected is None or expected != actual:
            errors.append(
                f"SHA-256 mismatch for {rel}: expected {expected}, observed {actual}"
            )
            summaries.append(f"{rel}: MISMATCH")
        else:
            summaries.append(f"{rel}: MATCH")

    return ExternalPinReport(
        passed=not errors,
        pinned_artifact_count=len(artifacts),
        errors=tuple(errors),
        artifact_summaries=tuple(summaries),
    )


def validate_external_pin_file(pin_path: Path, repo_root: Path) -> ExternalPinReport:
    repo_root = repo_root.resolve()
    raw_pin_path = pin_path.expanduser()
    if not raw_pin_path.is_absolute():
        raw_pin_path = Path.cwd() / raw_pin_path
    if raw_pin_path.is_symlink():
        return ExternalPinReport(
            passed=False,
            pinned_artifact_count=0,
            errors=("external pin file must not be a symlink",),
            artifact_summaries=(),
        )
    pin_path = raw_pin_path.resolve()
    try:
        pin_path.relative_to(repo_root)
    except ValueError:
        pass
    else:
        return ExternalPinReport(
            passed=False,
            pinned_artifact_count=0,
            errors=("external pin file must be stored outside the SCAF repository",),
            artifact_summaries=(),
        )
    if not pin_path.is_file():
        return ExternalPinReport(
            passed=False,
            pinned_artifact_count=0,
            errors=("external pin file is missing or not a regular file",),
            artifact_summaries=(),
        )
    return validate_external_pin_data(load_external_pin(pin_path), repo_root)


def main() -> int:
    parser = argparse.ArgumentParser(
        description=(
            "Verify the local canonical SCAF frozen-baseline manifest and release-integrity "
            "checker against a caller-supplied external pin document stored outside the repository."
        )
    )
    parser.add_argument("--pin-file", required=True, help="Path to a trusted external JSON pin document outside the SCAF repository")
    args = parser.parse_args()

    repo_root = _default_repo_root().resolve()
    pin_path = Path(args.pin_file)
    try:
        report = validate_external_pin_file(pin_path, repo_root)
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        print("SCAF External Release-Integrity Pin Verification")
        print(f"Repository: {repo_root}")
        print(f"Pin file:   {pin_path.resolve()}")
        print(f"ERROR: {exc}")
        print("RESULT: FAIL")
        return 1

    print("SCAF External Release-Integrity Pin Verification")
    print(f"Repository: {repo_root}")
    print(f"Pin file:   {pin_path.resolve()}")
    print(f"Pinned artifacts: {report.pinned_artifact_count}")
    for summary in report.artifact_summaries:
        print(summary)
    print(f"Errors: {len(report.errors)}")
    for error in report.errors:
        print(f"ERROR: {error}")
    print("RESULT: PASS" if report.passed else "RESULT: FAIL")
    return 0 if report.passed else 1


if __name__ == "__main__":
    sys.exit(main())
