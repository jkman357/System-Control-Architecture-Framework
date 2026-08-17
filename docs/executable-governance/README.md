# SCAF Executable Governance Development

**Development Release:** v0.0.4rc09  
**Status:** External-Pin Local Artifact Symlink Hardening RC  
**Upstream Baselines:** frozen v0.0.2 L1/L2; frozen v0.0.3 L3

## 1. Purpose

This directory contains separately controlled development toward SCAF executable governance.

The frozen v0.0.2 and v0.0.3 baselines are not modified in place. Executable-governance artifacts are downstream representations, schemas, validators, integrity controls and later enforcement mechanisms that must preserve the authority semantics of those frozen baselines.

## 2. Current rc09 Scope

The independent v0.0.4rc08 review returned:

```text
V0.0.4 RELEASE-INTEGRITY DIAGNOSTIC-CLEANUP / EXTERNAL-PINNING FOUNDATION GATE: YES, AFTER MINOR CLEANUP
```

The review confirmed `R7-01` and `R7-02` resolved and opened one Minor finding, `R8-01`, against local pinned-artifact symlink detection after path resolution.

Current executable-governance artifacts are:

- `00_SCAF_Machine_Readable_Authority_Model.md` — accepted authority model and deterministic record contract;
- `01_SCAF_v0.0.4rc02_Authority_Model_Determinism_Cleanup.md` — `R1-01` closure record;
- `02_SCAF_v0.0.4rc03_Initial_Authority_Registry_Serialization.md` — accepted 294-record registry serialization contract;
- `03_SCAF_v0.0.4rc04_Authority_Registry_Release_State_Documentation_Cleanup.md` — resolved `R3-01` cleanup record;
- `04_SCAF_v0.0.4rc05_Authority_Registry_Schema_and_Structural_Validator_Foundation.md` — accepted schema/validator foundation;
- `05_SCAF_v0.0.4rc06_Canonical_Schema_Binding_and_Validator_CLI_Hardening.md` — accepted canonical-schema/CLI hardening; `R5-01` resolved;
- `06_SCAF_v0.0.4rc07_Frozen_Baseline_Release_Integrity_Foundation.md` — accepted local frozen-baseline release-integrity foundation;
- `07_SCAF_v0.0.4rc08_Release_Integrity_Diagnostic_Cleanup_and_External_Pinning_Foundation.md` — accepted-after-cleanup external-pinning foundation; `R7-01` / `R7-02` resolved;
- `08_SCAF_v0.0.4rc09_External_Pin_Local_Artifact_Symlink_Hardening.md` — current focused `R8-01` closure;
- repository-root `authority-registry.yaml` — accepted rc03 294-record controlled representation;
- `schemas/authority-registry.schema.json` and `tools/scaf_validator/` — accepted semantic/representation conformance path;
- `release-integrity/frozen-baseline-manifest.json` and `tools/scaf_release_integrity/` — accepted local frozen-byte integrity path;
- `tools/scaf_external_pin/` — external-pin verification path with current local-artifact symlink hardening.

rc09 changes only the external-pin local pinned-artifact path handling, its regression suite, and current release/navigation/governance records. The external pin contract itself remains unchanged.

Frozen Markdown remains semantic authority. rc09 does **not** add CI enforcement, signing/PKI, canonical external-pin distribution/storage, registry generation, generated reverse indexes/views, code generation, automatic applicability inference, machine-readable L2→L3 relations, new L3 Patterns, M3/M4 or L4 guidance.

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
frozen-baseline manifest + standalone release-integrity checker
        ↓
external-pin verification foundation
        ↓
local pinned-artifact symlink hardening (current rc09)
        ↓
later separately gated CI / signing / generated views / executable governance
```

Semantic validation, frozen-byte integrity, and external identity pinning remain deliberately separate controls.

## 4. Current Gate

The independent v0.0.4rc09 review shall determine whether `R8-01` is fully closed on the real production CLI path for both fixed pinned artifacts, all accepted upstream controls remain non-regressed, and no deferred CI/signing/L3/M3/M4/L4 scope is introduced.

Expected gate label:

```text
V0.0.4 EXTERNAL-PIN LOCAL-ARTIFACT SYMLINK-HARDENING GATE
```
