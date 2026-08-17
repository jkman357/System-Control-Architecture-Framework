# SCAF v0.0.4rc07 — Frozen Baseline Release-Integrity Foundation

**Development Release:** v0.0.4rc07  
**Status:** Release-Integrity Foundation RC  
**Date:** 2026-08-17

## 1. Purpose

The accepted rc05/rc06 validator answers a semantic/representation question: whether `authority-registry.yaml` conforms to the accepted structural contract and canonical normative Markdown source semantics.

This RC adds a separate control for a different question:

> Are the frozen upstream Markdown bytes themselves still the reviewed frozen bytes?

The concern is deliberately separated so semantic/source-aware validation is not silently overloaded with release authentication behavior.

## 2. Protected Scope

The canonical rc07 manifest protects exactly:

```text
docs/normative/ — frozen v0.0.2 L1/L2 normative tree — 11 files
docs/l3/        — frozen v0.0.3 L3 catalog tree      — 30 files
```

No other repository tree is placed under this rc07 frozen-baseline manifest.

The manifest records for every protected file:

- repository-relative path;
- SHA-256;
- owning frozen baseline release.

It also records the accepted tree aggregate SHA-256 using:

```text
sorted repository-relative path + NUL + sha256(file) + LF
```

The expected aggregate fingerprints are the same construction used in prior independent reviews.

## 3. Canonical Manifest and Production Binding

Canonical manifest:

```text
release-integrity/frozen-baseline-manifest.json
```

Production command:

```text
python -m tools.scaf_release_integrity.checker
```

The production checker derives the repository from the reviewed checker module location and loads that repository's canonical manifest. It provides no production CLI option to replace repository root, manifest path, protected tree roots or hash algorithm.

Function-level injection remains available only for controlled regression tests.

## 4. Fail-Closed Integrity Contract

The checker shall fail on at least:

- changed protected-file bytes;
- protected file addition;
- protected file removal;
- symlink introduction in a protected tree;
- duplicate/unsupported/malformed manifest structure;
- unsafe or inconsistent manifest paths;
- per-file SHA-256 mismatch;
- protected-tree aggregate mismatch.

Exact tree membership is part of the integrity contract. A newly added file under a frozen tree is drift even if no pre-existing file changed.

## 5. Authority and Trust Boundary

Frozen Markdown remains semantic authority. The manifest does not define requirement or Pattern meaning and the checker does not decide applicability, compliance, verification, closure or Pattern selection.

The manifest is a reviewed cryptographic representation of accepted frozen bytes, not a self-authenticating trust root. A coordinated edit to both source and manifest cannot be proven unauthorized by local comparison alone. Manifest authenticity is supplied by controlled repository/release review; later external pinning, signing or CI policy requires a separate gate.

The semantic validator and release-integrity checker therefore remain distinct:

```text
semantic/representation consistency -> tools.scaf_validator
frozen-byte identity                -> tools.scaf_release_integrity
```

## 6. Non-Regression Requirements

rc07 shall preserve without semantic change:

- accepted `authority-registry.yaml` and all 294 rc03 records;
- accepted `schemas/authority-registry.schema.json`;
- accepted `tools/scaf_validator` behavior and eight-test regression suite;
- accepted rc01–rc06 executable-governance contracts;
- frozen `docs/normative/` bytes and 294 / 218 / 76 inventory;
- frozen `docs/l3/` bytes and twelve `Available / M2 — Architecture Reviewed` Pattern identities;
- canonical Markdown semantic precedence;
- project-state, L3-selection and non-empty-relation exclusion.

## 7. Regression Contract

The rc07 integrity tests shall cover:

1. accepted frozen trees pass;
2. protected file byte modification fails;
3. protected file addition fails;
4. protected file removal fails;
5. manifest file-hash corruption fails;
6. manifest path escape/out-of-tree mapping fails;
7. production checker resolves repository/manifest from reviewed module location rather than current working directory;
8. production CLI rejects attempted `--manifest` and `--repo-root` override arguments.

## 8. Deferred Scope

rc07 does not add or authorize:

- CI enforcement / merge blocking;
- signing, external trust roots or provenance services;
- integrity protection of the registry/schema/validator as a new frozen set;
- registry generation / hybrid ownership;
- generated reverse indexes/views;
- code generation;
- automatic project applicability inference;
- machine-readable L2→L3 relation semantics;
- new L3 Patterns / third tranche / SEC-primary realization;
- M3/M4;
- L4.

## 9. Gate

Expected independent review gate:

```text
V0.0.4 FROZEN-BASELINE RELEASE-INTEGRITY FOUNDATION GATE
```

A `YES` accepts only this local manifest/checker foundation and does not automatically authorize later enforcement or expansion stages.
