# SCAF v0.0.4 — Executable Governance Formal Freeze Decision

**Release:** v0.0.4  
**Date:** 2026-08-17  
**Status:** Frozen Executable Governance Baseline  
**Upstream Baselines:** frozen v0.0.2 L1/L2; frozen v0.0.3 L3

## 1. Decision

By explicit governance decision, the reviewed `v0.0.4rc13` executable-governance milestone is frozen as **SCAF v0.0.4 — Frozen Executable Governance Baseline**.

The independent rc13 freeze-candidate documentation-closure review returned:

```text
R12-01: RESOLVED
V0.0.4 FREEZE-CANDIDATE CONTROL-CHAIN DOCUMENTATION CLOSURE GATE: YES
```

The review recorded:

- Critical: 0;
- Major: 0;
- Minor: 0;
- Trivial: 0;
- open accepted upstream findings: 0.

The reviewed rc13 source artifact identity was:

```text
0cff9b950d5c92c661ff1f66664825f2337d88ab1a72fce84a0ef37875dbf979
```

The explicit formal freeze decision was made after that accepted review result.

## 2. Frozen Scope

The v0.0.4 frozen executable-governance baseline includes the reviewed authority-representation, validation, release-integrity, external-identity and CI-enforcement foundation necessary to reproduce the accepted executable-governance state, including:

- repository-root `authority-registry.yaml` containing the accepted 294-record representation;
- `schemas/authority-registry.schema.json`;
- `tools/scaf_validator/` semantic/structural/source-aware validation control;
- `release-integrity/frozen-baseline-manifest.json`;
- `tools/scaf_release_integrity/` local frozen-source byte-integrity control;
- `tools/scaf_external_pin/` repository-external identity-pin verification control;
- `tools/scaf_ci_gate/` external-trust executable-governance orchestration control;
- `.github/workflows/scaf-executable-governance.yml` trusted-main/manual executor;
- executable-governance governance records `00_*` through `12_*` necessary to reconstruct the accepted control semantics, review history, trust boundaries and freeze-candidate closure;
- repository navigation/release documentation necessary to identify the formal frozen state.

Accepted authority inventory:

```text
294 normative authority records
218 Project-Applicable Obligations
76 Framework Normative Invariants
0 SCAF-PAT-* authority-registry records
294 / 294 machine-readable relations empty
```

Accepted regression inventory:

```text
scaf_validator:          8 tests
scaf_release_integrity:  9 tests
scaf_external_pin:      11 tests
scaf_ci_gate:           13 tests
Total:                  41 tests
```

Accepted production runtime sequence:

```text
external CI trust input
        ↓
six fixed control-plane path/topology + SHA-256 identity checks
        ↓
external-pin verification
        ↓
frozen-baseline release integrity
        ↓
authority-registry semantic / structural / source validation
        ↓
each successful stage attests the same verified Repository root
        ↓
CI gate RESULT: PASS / FAIL
```

## 3. Freeze Delta from v0.0.4rc13

No executable-governance semantic or control-plane behavior change is intended.

The formal freeze permits only release/freeze-state synchronization, including:

- current version `v0.0.4rc13` -> `v0.0.4` in current release/navigation state;
- current freeze-candidate wording -> frozen-baseline wording;
- addition of this formal freeze-decision record;
- CHANGELOG release entry for `v0.0.4`.

The following remain unchanged from the reviewed rc13 candidate:

- authority-registry contents and identity;
- canonical registry schema;
- semantic validator implementation and regression suite;
- frozen-baseline manifest;
- release-integrity checker and regression suite;
- external-pin checker and regression suite;
- CI gate implementation and regression suite;
- GitHub Actions workflow behavior and trust boundary;
- six fixed CI control-plane identities;
- frozen v0.0.2 normative bytes and inventory;
- frozen v0.0.3 L3 bytes and twelve `Available / M2 — Architecture Reviewed` Pattern identities;
- authority/trust non-equivalence and deferred-scope boundaries.

## 4. Upstream Frozen Integrity

The v0.0.4 freeze consumes but does not reopen the two upstream frozen baselines.

Frozen v0.0.2 L1/L2 remains:

```text
11 normative Markdown files
294 unique normative requirement IDs
218 Project-Applicable Obligations
76 Framework Normative Invariants
aggregate SHA-256:
86ca06dbb586b8e0f47c8efbe731635633484bf58de2ddd3e90639a42090775f
```

Frozen v0.0.3 L3 remains:

```text
30 protected L3 files
12 published Pattern identities
12 x Available / M2 — Architecture Reviewed
aggregate SHA-256:
eddb26826ce83d7a9aae028cf3c4f7f630b304c41e3bcbbfe8f00e51d3248eeb
```

## 5. Authority and Trust Boundaries Preserved

The freeze preserves the accepted non-equivalence:

```text
Frozen Markdown semantic authority
        !=
authority-registry / schema conformance
        !=
frozen-source byte identity
        !=
external identity trust input
        !=
CI executor / enforcement policy
```

No schema, registry, validator, integrity manifest, external pin, CI trust bundle, workflow or gate acquires authority to redefine normative meaning, project applicability, compliance, verification, evidence, closure, Pattern selection or L3 maturity.

## 6. Explicitly Not Frozen / Not Authorized by v0.0.4

The following remain separately gated future work and are not implied by the v0.0.4 freeze:

- fork-PR / privileged `pull_request_target` enforcement;
- branch-protection / merge-blocking administration;
- workflow/package self-authentication;
- signing, PKI, transparency, attestation or provenance services;
- canonical external trust-bundle storage/distribution;
- generated authority views/indexes or reverse indexes;
- authority-registry generation or hybrid ownership;
- code generation;
- automatic project applicability/compliance/verification/evidence/closure inference;
- non-empty machine-readable L2-to-L3 relation semantics;
- new/third-tranche L3 Pattern work or SEC-primary realization;
- M3/M4;
- L4 implementation / verification guidance.

## 7. Post-Freeze Governance

`v0.0.4` is immutable as a frozen formal baseline and shall not be modified in place.

Future executable-governance capability or semantic work must proceed under a new controlled RC/version line. Such work shall preserve explicit trace to the frozen v0.0.2 L1/L2 authority, frozen v0.0.3 L3 catalog, and frozen v0.0.4 executable-governance baseline rather than silently rewriting any of them.
