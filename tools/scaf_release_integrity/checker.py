from __future__ import annotations

import argparse
import hashlib
import json
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any


MANIFEST_RELATIVE_PATH = Path("release-integrity/frozen-baseline-manifest.json")
EXPECTED_MANIFEST_KEYS = {
    "manifest_version",
    "manifest_release",
    "algorithm",
    "aggregate_construction",
    "protected_trees",
}
EXPECTED_TREE_KEYS = {
    "name",
    "baseline_release",
    "root",
    "expected_file_count",
    "aggregate_sha256",
    "files",
}
EXPECTED_FILE_KEYS = {"path", "sha256"}
EXPECTED_MANIFEST_VERSION = 1
EXPECTED_MANIFEST_RELEASE = "v0.0.4rc07"
EXPECTED_ALGORITHM = "sha256"
EXPECTED_AGGREGATE_CONSTRUCTION = "sorted repository-relative path + NUL + sha256(file) + LF"
EXPECTED_TREES = {
    "frozen_l1_l2_normative": ("v0.0.2", "docs/normative", 11),
    "frozen_l3_catalog": ("v0.0.3", "docs/l3", 30),
}


@dataclass(frozen=True)
class IntegrityReport:
    passed: bool
    protected_tree_count: int
    protected_file_count: int
    errors: tuple[str, ...]
    tree_summaries: tuple[str, ...]


def _default_repo_root() -> Path:
    return Path(__file__).resolve().parents[2]


def _sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def load_manifest(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as handle:
        data = json.load(handle)
    if not isinstance(data, dict):
        raise ValueError("release-integrity manifest root must be an object")
    return data


def _safe_repo_path(repo_root: Path, relative: str) -> Path:
    rel = Path(relative)
    if rel.is_absolute():
        raise ValueError(f"absolute repository path is not allowed: {relative}")
    candidate = (repo_root / rel).resolve()
    try:
        candidate.relative_to(repo_root.resolve())
    except ValueError as exc:
        raise ValueError(f"repository path escapes root: {relative}") from exc
    return candidate


def _aggregate(entries: list[tuple[str, str]]) -> str:
    digest = hashlib.sha256()
    for path, file_hash in sorted(entries):
        digest.update(path.encode("utf-8"))
        digest.update(b"\0")
        digest.update(file_hash.encode("ascii"))
        digest.update(b"\n")
    return digest.hexdigest()


def validate_release_integrity_data(
    manifest: dict[str, Any], repo_root: Path
) -> IntegrityReport:
    errors: list[str] = []
    tree_summaries: list[str] = []
    protected_file_count = 0

    if set(manifest) != EXPECTED_MANIFEST_KEYS:
        errors.append(
            "manifest keys mismatch: expected "
            f"{sorted(EXPECTED_MANIFEST_KEYS)}, observed {sorted(manifest)}"
        )
    if manifest.get("manifest_version") != EXPECTED_MANIFEST_VERSION:
        errors.append("manifest_version must be 1")
    if manifest.get("manifest_release") != EXPECTED_MANIFEST_RELEASE:
        errors.append("manifest_release must be v0.0.4rc07")
    if manifest.get("algorithm") != EXPECTED_ALGORITHM:
        errors.append("algorithm must be sha256")
    if manifest.get("aggregate_construction") != EXPECTED_AGGREGATE_CONSTRUCTION:
        errors.append("aggregate_construction does not match the accepted construction")

    trees = manifest.get("protected_trees")
    if not isinstance(trees, list):
        errors.append("protected_trees must be an array")
        trees = []

    if len(trees) != len(EXPECTED_TREES):
        errors.append(f"protected_trees count must be {len(EXPECTED_TREES)}")

    seen_tree_names: set[str] = set()
    seen_manifest_paths: set[str] = set()

    for tree in trees:
        tree_error_start = len(errors)
        if not isinstance(tree, dict):
            errors.append("protected tree entry must be an object")
            continue
        if set(tree) != EXPECTED_TREE_KEYS:
            errors.append(f"protected tree keys mismatch for {tree.get('name', '<unknown>')}")

        name = tree.get("name")
        if not isinstance(name, str) or name not in EXPECTED_TREES:
            errors.append(f"unsupported protected tree name: {name!r}")
            continue
        if name in seen_tree_names:
            errors.append(f"duplicate protected tree name: {name}")
            continue
        seen_tree_names.add(name)

        expected_release, expected_root, expected_count = EXPECTED_TREES[name]
        if tree.get("baseline_release") != expected_release:
            errors.append(f"{name}: baseline_release must be {expected_release}")
        if tree.get("root") != expected_root:
            errors.append(f"{name}: root must be {expected_root}")
        if tree.get("expected_file_count") != expected_count:
            errors.append(f"{name}: expected_file_count must be {expected_count}")

        files = tree.get("files")
        if not isinstance(files, list):
            errors.append(f"{name}: files must be an array")
            files = []
        if len(files) != expected_count:
            errors.append(f"{name}: manifest file count must be {expected_count}")

        expected_paths: set[str] = set()
        manifest_hashes: dict[str, str] = {}
        root_prefix = expected_root.rstrip("/") + "/"
        for item in files:
            if not isinstance(item, dict):
                errors.append(f"{name}: file entry must be an object")
                continue
            if set(item) != EXPECTED_FILE_KEYS:
                errors.append(f"{name}: file entry keys mismatch")
            rel = item.get("path")
            file_hash = item.get("sha256")
            if not isinstance(rel, str) or not rel.startswith(root_prefix):
                errors.append(f"{name}: manifest file path outside protected tree: {rel!r}")
                continue
            if rel in seen_manifest_paths:
                errors.append(f"duplicate manifest file path: {rel}")
                continue
            seen_manifest_paths.add(rel)
            expected_paths.add(rel)
            if not isinstance(file_hash, str) or len(file_hash) != 64 or any(c not in "0123456789abcdef" for c in file_hash):
                errors.append(f"{name}: invalid SHA-256 value for {rel}")
                continue
            manifest_hashes[rel] = file_hash

        try:
            tree_root = _safe_repo_path(repo_root, expected_root)
        except ValueError as exc:
            errors.append(f"{name}: {exc}")
            continue
        if not tree_root.is_dir():
            errors.append(f"{name}: protected tree is missing: {expected_root}")
            continue

        actual_paths: set[str] = set()
        actual_hashes: dict[str, str] = {}
        for path in sorted(tree_root.rglob("*")):
            if path.is_symlink():
                errors.append(f"{name}: symlink is not allowed in protected tree: {path.relative_to(repo_root).as_posix()}")
                continue
            if path.is_file():
                rel = path.relative_to(repo_root).as_posix()
                actual_paths.add(rel)
                actual_hashes[rel] = _sha256_file(path)

        missing = sorted(expected_paths - actual_paths)
        added = sorted(actual_paths - expected_paths)
        for rel in missing:
            errors.append(f"{name}: protected file missing: {rel}")
        for rel in added:
            errors.append(f"{name}: unexpected protected file added: {rel}")

        for rel in sorted(expected_paths & actual_paths):
            expected_hash = manifest_hashes.get(rel)
            actual_hash = actual_hashes[rel]
            if expected_hash is not None and expected_hash != actual_hash:
                errors.append(
                    f"{name}: SHA-256 mismatch for {rel}: expected {expected_hash}, observed {actual_hash}"
                )

        actual_entries = [(rel, actual_hashes[rel]) for rel in sorted(actual_paths)]
        actual_aggregate = _aggregate(actual_entries)
        expected_aggregate = tree.get("aggregate_sha256")
        if not isinstance(expected_aggregate, str) or len(expected_aggregate) != 64:
            errors.append(f"{name}: invalid aggregate_sha256")
        elif actual_aggregate != expected_aggregate:
            errors.append(
                f"{name}: aggregate SHA-256 mismatch: expected {expected_aggregate}, observed {actual_aggregate}"
            )

        protected_file_count += len(actual_paths)
        tree_summaries.append(
            f"{expected_root}: {len(actual_paths)} files / "
            + ("MATCH" if len(errors) == tree_error_start else "MISMATCH")
        )

    missing_tree_names = sorted(set(EXPECTED_TREES) - seen_tree_names)
    for name in missing_tree_names:
        errors.append(f"missing protected tree entry: {name}")

    return IntegrityReport(
        passed=not errors,
        protected_tree_count=len(trees),
        protected_file_count=protected_file_count,
        errors=tuple(errors),
        tree_summaries=tuple(tree_summaries),
    )


def validate_release_integrity(repo_root: Path, manifest_path: Path) -> IntegrityReport:
    return validate_release_integrity_data(load_manifest(manifest_path), repo_root.resolve())


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Verify SCAF frozen v0.0.2/v0.0.3 baseline byte integrity against the canonical repository manifest."
    )
    parser.parse_args()
    repo_root = _default_repo_root().resolve()
    manifest_path = (repo_root / MANIFEST_RELATIVE_PATH).resolve()
    try:
        report = validate_release_integrity(repo_root, manifest_path)
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        print("SCAF Frozen Baseline Release Integrity")
        print(f"Repository: {repo_root}")
        print(f"Manifest:   {manifest_path}")
        print(f"ERROR: {exc}")
        print("RESULT: FAIL")
        return 1

    print("SCAF Frozen Baseline Release Integrity")
    print(f"Repository: {repo_root}")
    print(f"Manifest:   {manifest_path}")
    print(f"Protected trees: {report.protected_tree_count}")
    print(f"Protected files: {report.protected_file_count}")
    for summary in report.tree_summaries:
        print(summary)
    print(f"Errors: {len(report.errors)}")
    for error in report.errors:
        print(f"ERROR: {error}")
    print("RESULT: PASS" if report.passed else "RESULT: FAIL")
    return 0 if report.passed else 1


if __name__ == "__main__":
    sys.exit(main())
