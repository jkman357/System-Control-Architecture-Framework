# SCAF v0.0.4rc13 — Freeze-Candidate Control-Chain Documentation Closure

**Release:** v0.0.4rc13  
**Status:** Focused Freeze-Candidate Documentation Closure RC  
**Date:** 2026-08-17

## 1. Purpose

v0.0.4rc13 is a documentation-only closure RC for the sole v0.0.4rc12 review finding, `R12-01`.

The rc12 independent review returned:

```text
V0.0.4 EXECUTABLE-GOVERNANCE MILESTONE CONSOLIDATION / FREEZE-CANDIDATE GATE: YES, AFTER MINOR CLEANUP
```

and opened exactly one Minor finding:

```text
R12-01 — the freeze-candidate consolidation diagrams could be read as production execution order even though their arrow ordering differed from the actual fail-closed CI-gate runtime sequence.
```

rc13 adds no executable-governance capability and does not alter the accepted production gate. Its purpose is solely to make the audit-facing freeze-candidate documentation unambiguous before any explicit formal `v0.0.4` freeze decision.

## 2. R12-01 Closure

The documentation now distinguishes two different views.

### 2.1 Capability / development layering

This view explains how executable-governance capabilities were added over the frozen semantic baselines. It is **not** runtime execution order.

```text
Frozen normative Markdown semantic authority
        ↓
294-record authority registry
        ↓
canonical registry schema + source-aware validator capability
        ↓
frozen-baseline manifest + release-integrity capability
        ↓
external identity pin verification capability
        ↓
external CI trust model + executable-governance orchestration
        ↓
path-component / repository-root / stage-root hardening
```

### 2.2 Production runtime execution order

The production gate sequence remains exactly:

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

This sequence matches the accepted `tools/scaf_ci_gate/gate.py` behavior and the canonical rc11/rc12 production-gate executions.

## 3. Controlled Documentation Changes

rc13 changes only:

```text
README.md
CHANGELOG.md
docs/executable-governance/README.md
docs/executable-governance/11_SCAF_v0.0.4rc12_Executable_Governance_Milestone_Consolidation_and_Freeze_Candidate.md
```

and adds this closure record:

```text
docs/executable-governance/12_SCAF_v0.0.4rc13_Freeze_Candidate_Control_Chain_Documentation_Closure.md
```

The rc12 consolidation record is changed only to label its former control-chain diagram as capability/development layering and to place the verified production runtime sequence beside it. No historical rc01→rc11 review outcome is rewritten.

## 4. Preserved Executable / Frozen State

rc13 intentionally preserves byte-for-byte:

- `authority-registry.yaml`;
- `schemas/authority-registry.schema.json`;
- `tools/scaf_validator/` implementation and tests;
- `release-integrity/frozen-baseline-manifest.json`;
- `tools/scaf_release_integrity/` implementation and tests;
- `tools/scaf_external_pin/` implementation and tests;
- `tools/scaf_ci_gate/` implementation and tests;
- `.github/workflows/scaf-executable-governance.yml`;
- accepted executable-governance records `00_*` through `10_*`;
- frozen `docs/normative/`;
- frozen `docs/l3/`.

The accepted inventories remain:

```text
294 normative / registry IDs
218 Project-Applicable Obligations
76 Framework Normative Invariants
0 SCAF-PAT-* records in authority-registry.yaml
294 / 294 relations empty
12 L3 Pattern identities
12 / 12 Available
12 / 12 M2 — Architecture Reviewed
```

Regression inventory remains:

```text
scaf_validator:          8
scaf_release_integrity:  9
scaf_external_pin:      11
scaf_ci_gate:           13
Total:                  41
```

## 5. Freeze State

rc13 is still an RC. It does **not** create `v0.0.4` and does **not** perform the formal freeze.

A successful rc13 closure review establishes only that the documentation cleanup is accepted and the freeze candidate is eligible for a separate explicit governance freeze decision.

The reserved formal milestone name remains:

```text
SCAF v0.0.4 — Frozen Executable Governance Baseline
```

## 6. Deferred Scope

rc13 does not add or claim completion of:

- fork-PR / privileged `pull_request_target` enforcement;
- branch-protection / merge-blocking administration;
- workflow/package self-authentication;
- signing / PKI / provenance / transparency / attestation services;
- canonical external trust-bundle storage or distribution;
- generated authority views/indexes;
- authority-registry generation;
- code generation;
- automatic project applicability/compliance/verification/evidence/closure inference;
- non-empty machine-readable L2→L3 relation semantics;
- new L3 / third-tranche / SEC-primary work;
- M3/M4;
- L4.

## 7. Closure Acceptance Criteria

The rc13 closure gate may return `YES` only if an independent review confirms:

1. `R12-01` is resolved consistently in root README and the rc12 consolidation record.
2. Capability/development layering is explicitly labeled as non-runtime.
3. The documented production runtime sequence matches the executable CI gate.
4. No executable code, workflow, registry/schema, manifest, test, frozen normative, or frozen L3 content changed.
5. All 41 regressions remain green with no unexpected skip or reduction.
6. The externally trusted production CI gate remains PASS with the same six control-plane identities.
7. The historical rc10 `NO`, rc11 `YES`, and rc12 `YES, AFTER MINOR CLEANUP` dispositions remain visible and accurate.
8. No deferred scope is introduced.
9. rc13 remains a freeze candidate closure RC and does not falsely claim formal `v0.0.4` freeze.

Expected closure gate label:

```text
V0.0.4 FREEZE-CANDIDATE CONTROL-CHAIN DOCUMENTATION CLOSURE GATE
```
