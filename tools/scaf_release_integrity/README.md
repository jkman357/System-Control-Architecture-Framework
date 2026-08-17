# SCAF Frozen Baseline Release-Integrity Checker

This package verifies byte-level integrity of the SCAF frozen upstream trees protected by the reviewed rc07 manifest.

## Production command

Run from any working directory with the repository available on Python's module path (normally from repository root):

```text
python -m tools.scaf_release_integrity.checker
```

The production checker is intentionally bound to:

- the repository containing the reviewed checker module;
- `release-integrity/frozen-baseline-manifest.json` from that repository;
- the two protected frozen trees recorded by the manifest.

There is no production CLI override for repository root, manifest path, protected roots, or hash algorithm.

## Protected scope

rc07 protects only:

- `docs/normative/` — frozen v0.0.2 L1/L2 normative tree;
- `docs/l3/` — frozen v0.0.3 L3 catalog tree.

For every protected file, the manifest records SHA-256. It also records the accepted aggregate tree fingerprint using the same construction already used by independent SCAF reviews:

```text
sorted repository-relative path + NUL + sha256(file) + LF
```

The checker fails on changed bytes, added files, removed files, symlinks in protected trees, path/manifest inconsistency, or aggregate mismatch.

## Authority boundary

This checker does **not** decide what SCAF requirements or Patterns mean. Frozen Markdown remains semantic authority. The manifest is a reviewed release-integrity representation of accepted bytes; the checker is a subordinate byte-integrity checker.

The manifest does not self-authenticate. If both a protected source and the manifest are maliciously changed together, a local checker alone cannot establish provenance. Authenticity of the reviewed manifest is supplied by release/repository review and may later be pinned by separately gated CI/release controls.

Release-integrity checking remains separate from `tools.scaf_validator`, which validates the machine-readable authority registry against its canonical schema and canonical Markdown semantics.

## Tests

```text
python -m unittest discover -s tools/scaf_release_integrity/tests -v
```

The tests cover the accepted tree plus content modification, file addition, file removal, manifest-hash corruption, manifest path escape, production module/CWD binding, and rejection of manifest/repository CLI override attempts.
