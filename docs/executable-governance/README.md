# SCAF Executable Governance Development

**Development Release:** v0.0.4rc08  
**Status:** Release-Integrity Diagnostic Cleanup / External Pinning Foundation RC  
**Upstream Baselines:** frozen v0.0.2 L1/L2; frozen v0.0.3 L3

## 1. Purpose

This directory contains separately controlled development toward SCAF executable governance.

The frozen v0.0.2 and v0.0.3 baselines are not modified in place. Executable-governance artifacts are downstream representations, schemas, validators, integrity controls and later enforcement mechanisms that must preserve the authority semantics of those frozen baselines.

## 2. Current rc08 Scope

The independent v0.0.4rc07 review returned:

```text
V0.0.4 FROZEN-BASELINE RELEASE-INTEGRITY FOUNDATION GATE: YES
```

The review accepted the rc07 local frozen-baseline integrity foundation with no Critical/Major/Minor finding and only two non-blocking Trivial findings (`R7-01`, `R7-02`).

Current executable-governance artifacts are:

- `00_SCAF_Machine_Readable_Authority_Model.md` — accepted authority model and deterministic record contract;
- `01_SCAF_v0.0.4rc02_Authority_Model_Determinism_Cleanup.md` — `R1-01` closure record;
- `02_SCAF_v0.0.4rc03_Initial_Authority_Registry_Serialization.md` — accepted 294-record registry serialization contract;
- `03_SCAF_v0.0.4rc04_Authority_Registry_Release_State_Documentation_Cleanup.md` — resolved `R3-01` cleanup record;
- `04_SCAF_v0.0.4rc05_Authority_Registry_Schema_and_Structural_Validator_Foundation.md` — accepted schema/validator foundation;
- `05_SCAF_v0.0.4rc06_Canonical_Schema_Binding_and_Validator_CLI_Hardening.md` — accepted canonical-schema/CLI hardening; `R5-01` resolved;
- `06_SCAF_v0.0.4rc07_Frozen_Baseline_Release_Integrity_Foundation.md` — accepted local frozen-baseline release-integrity foundation;
- `07_SCAF_v0.0.4rc08_Release_Integrity_Diagnostic_Cleanup_and_External_Pinning_Foundation.md` — current diagnostic cleanup / external-pinning foundation;
- repository-root `authority-registry.yaml` — accepted rc03 294-record controlled representation;
- `schemas/authority-registry.schema.json` and `tools/scaf_validator/` — accepted semantic/representation conformance path;
- `release-integrity/frozen-baseline-manifest.json` and `tools/scaf_release_integrity/` — accepted local frozen-byte integrity path, with rc08 diagnostic cleanup;
- `tools/scaf_external_pin/` — current external-pin verification path for manifest/checker identities.

rc08 preserves the accepted rc07 manifest/protected scope and closes `R7-01` / `R7-02`. It adds an external-pin checker that requires a trusted JSON pin file from outside the repository and compares exactly the local canonical manifest and local release-integrity checker identities against that external trust input.

Frozen Markdown remains semantic authority. The external pin document is not semantic authority and does not decide project state or L3 selection. The external-pin checker itself is trusted as part of the reviewed rc08 source/package; CI/signing/provenance mechanisms that externally pin that checker/package remain future separately gated work.

rc08 does **not** add CI enforcement, signing/PKI, canonical external-pin distribution/storage, registry generation, generated reverse indexes/views, code generation, automatic applicability inference, machine-readable L2→L3 relations, new L3 Patterns, M3/M4 or L4 guidance.

## 3. Development Order

```text
frozen human-readable semantic authority
        ↓
authority model / deterministic record contract
        ↓
machine-readable registry serialization
        ↓
schema + structural/source-aware validator + regression tests
        ↓
canonical schema binding + validator CLI hardening
        ↓
frozen-baseline manifest + standalone release-integrity checker (accepted rc07)
        ↓
release-integrity diagnostic cleanup + external-pin verification (current rc08)
        ↓
later separately gated CI / generated views / executable governance
```

Semantic validation and release integrity are deliberately separate controls. Each transition requires a separately reviewed repository state.

## 4. Current Gate

The independent v0.0.4rc08 review shall determine whether `R7-01` / `R7-02` are closed, the external-pin checker correctly binds the local canonical manifest/checker identities to a trusted outside-repository pin document, all accepted upstream controls remain non-regressed, and no CI/signing/L3/M3/M4/L4 scope is introduced.

Expected gate label:

```text
V0.0.4 RELEASE-INTEGRITY DIAGNOSTIC-CLEANUP / EXTERNAL-PINNING FOUNDATION GATE
```
