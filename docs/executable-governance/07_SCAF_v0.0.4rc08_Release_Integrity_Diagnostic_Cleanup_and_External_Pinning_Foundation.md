# SCAF v0.0.4rc08 — Release-Integrity Diagnostic Cleanup & External Pinning Foundation

**Development Release:** v0.0.4rc08  
**Status:** Diagnostic Cleanup / External Pinning Foundation RC  
**Date:** 2026-08-17

## 1. Purpose

The independent rc07 review returned `V0.0.4 FROZEN-BASELINE RELEASE-INTEGRITY FOUNDATION GATE: YES` with no Critical/Major/Minor findings and two non-blocking Trivial findings. rc08 closes those diagnostics and establishes one new bounded trust control: verification of the local rc07 manifest and rc08 release-integrity checker against a trusted pin document supplied from outside the repository.

## 2. rc07 Trivial Cleanup

- `R7-01`: per-tree summaries now report `MISMATCH` when a tree has any structural/integrity error, including symlink-only failure; overall fail-closed behavior is unchanged.
- `R7-02`: the rc07 CHANGELOG regression enumeration now explicitly includes production CLI override rejection as the eighth category.

The rc08 release-integrity regression suite adds a symlink-summary regression, raising that suite from 8 to 9 tests.

## 3. External Pinning Contract

New tool: `tools/scaf_external_pin/checker.py`.

Production command:

```text
python -m tools.scaf_external_pin.checker --pin-file <outside-repository-pin.json>
```

The external pin document is an explicit external trust input. It must be outside the SCAF repository, must be a regular non-symlink JSON file, and must pin exactly two local artifacts by lowercase SHA-256:

1. `release-integrity/frozen-baseline-manifest.json`;
2. `tools/scaf_release_integrity/checker.py`.

The pin document cannot choose alternate repository artifacts, repository roots, hash algorithms or local manifest paths.

## 4. Trust Boundary

The control chain is intentionally layered:

```text
external pin document (trust supplied outside repository)
        ↓
external pin checker verifies local manifest/checker identities
        ↓
release-integrity checker verifies frozen source bytes
        ↓
docs/normative + docs/l3
```

Frozen Markdown remains semantic authority. The external pin document does not define requirement/Pattern semantics. The external pin checker does not verify registry semantics or project state.

The external pin checker itself is not self-authenticated by the external pin document. Its trust comes from execution of the reviewed rc08 source/package. Pinning/signing the rc08 checker/package, selecting the external storage/distribution mechanism, and enforcing this sequence in CI/merge/release policy remain separately gated.

## 5. Production Binding / Failure Policy

The production pin checker derives the repository from its reviewed module location and accepts only `--pin-file`. It fails closed on malformed/unsupported pin shape, duplicate JSON object keys, missing/duplicate/unsupported artifact paths, invalid SHA-256 syntax, external pin stored inside the repository, pin symlink, missing local pinned artifact, local pinned-artifact symlink, or SHA-256 mismatch.

## 6. Non-Regression Requirements

rc08 shall preserve without semantic change:

- accepted `authority-registry.yaml` / 294 / 218 / 76 state;
- accepted authority-registry schema and `tools.scaf_validator` implementation/tests;
- rc07 `release-integrity/frozen-baseline-manifest.json`;
- frozen `docs/normative/` and `docs/l3/` bytes;
- accepted rc01–rc07 executable-governance semantics other than the explicitly authorized R7 diagnostic/navigation cleanup;
- project-state exclusion, empty machine-readable relations, and the 12 `Available / M2` L3 Pattern inventory.

## 7. Regression Contract

- semantic validator: 8 tests / PASS;
- release-integrity checker: 9 tests / PASS;
- external-pin checker: 9 tests / PASS.

The external-pin regression set covers accepted pins, manifest/checker hash mismatch, duplicate/extra pin artifact, in-repository pin rejection, external pin symlink rejection, CWD/module binding, production bad-pin failure, and rejection of repository/artifact/hash-algorithm CLI override attempts.

## 8. Deferred Scope

rc08 does not add or authorize:

- GitHub Actions / CI enforcement / merge blocking;
- signing, certificate/PKI, transparency log or provenance service;
- canonical external pin storage/distribution policy;
- self-authentication of the external-pin checker/package;
- registry generation / generated indexes/views / code generation;
- project applicability/compliance inference;
- machine-readable L2→L3 relations;
- new L3 Patterns, M3/M4 or L4.

## 9. Gate

```text
V0.0.4 RELEASE-INTEGRITY DIAGNOSTIC-CLEANUP / EXTERNAL-PINNING FOUNDATION GATE
```

A `YES` accepts only the rc07 Trivial cleanup and the bounded external-pin verification foundation.
