# SCAF v0.0.4rc09 — External-Pin Local Artifact Symlink Hardening

**Development Release:** v0.0.4rc09  
**Status:** Focused R8-01 Closure RC  
**Date:** 2026-08-17

## 1. Purpose

The independent rc08 review returned:

```text
V0.0.4 RELEASE-INTEGRITY DIAGNOSTIC-CLEANUP / EXTERNAL-PINNING FOUNDATION GATE: YES, AFTER MINOR CLEANUP
```

and opened one Minor finding, `R8-01`: the production external-pin checker documented local pinned-artifact symlink rejection, but `_safe_repo_path()` resolved a fixed artifact path before testing `is_symlink()`. An in-repository same-byte symlink could therefore preserve the pinned SHA-256 and incorrectly return normal `RESULT: PASS`.

rc09 closes only that implementation/policy mismatch. It does not redesign external pinning and does not introduce CI, signing or provenance enforcement.

## 2. R8-01 Deterministic Closure

For each fixed local pinned artifact, production resolution shall execute in this order:

```text
repo_root / fixed repository-relative artifact path
        ↓
lexical artifact-path symlink check
        ↓
resolve path
        ↓
repository-root confinement check
        ↓
regular-file check
        ↓
SHA-256 comparison with external pin
```

The fixed local artifact path itself being a symlink is therefore a fail-closed condition even when:

- the symlink target remains inside the same repository; and
- the target bytes are identical to the externally pinned bytes.

rc09 does not broaden this closure into a new general parent-component symlink policy. Any stronger parent-path policy requires separate review.

## 3. Fixed Pinned Artifacts

The rc08 external-pin contract remains unchanged and continues to pin exactly:

1. `release-integrity/frozen-baseline-manifest.json`;
2. `tools/scaf_release_integrity/checker.py`.

The external pin remains a caller/environment trust input stored outside the repository. The hash algorithm remains SHA-256. No repository-root, artifact-path or hash-algorithm production override is introduced.

## 4. Regression Contract

The external-pin regression suite is extended from 9 to 11 tests. The two new end-to-end production CLI tests shall independently replace each fixed artifact path with an in-repository same-byte symlink and require:

```text
exit code != 0
RESULT: FAIL
pinned repository artifact must not be a symlink
```

The accepted upstream suites shall remain green:

- semantic/source-aware validator: 8 tests / PASS;
- frozen-baseline release-integrity checker: 9 tests / PASS;
- external-pin checker: 11 tests / PASS.

## 5. Non-Regression Requirements

rc09 shall preserve without semantic change:

- `authority-registry.yaml` and its accepted 294 / 218 / 76 population;
- `schemas/authority-registry.schema.json`;
- `tools/scaf_validator/` implementation and tests;
- `release-integrity/frozen-baseline-manifest.json`;
- `tools/scaf_release_integrity/` implementation and tests;
- frozen `docs/normative/` and `docs/l3/` bytes;
- accepted executable-governance records `00_*` through `07_*`;
- external-pin document shape, fixed two-artifact identity set, SHA-256 algorithm, outside-repository pin-file rule, project-state exclusion, empty machine-readable relations and L3 boundary.

## 6. Deferred Scope

rc09 does not add or authorize:

- GitHub Actions / CI enforcement / merge blocking;
- signing, PKI, transparency logs or provenance services;
- canonical external-pin storage/distribution;
- self-authentication of the external-pin checker/package;
- registry generation, generated views/indexes or code generation;
- automatic applicability/compliance/closure inference;
- machine-readable L2→L3 relations;
- new L3 Patterns, M3/M4 or L4.

## 7. Gate

```text
V0.0.4 EXTERNAL-PIN LOCAL-ARTIFACT SYMLINK-HARDENING GATE
```

A `YES` resolves only `R8-01` and accepts the rc08 external-pinning foundation with this focused production-path hardening.
