# SCAF Executable Governance Development

**Development Release:** v0.0.4rc07  
**Status:** Frozen Baseline Release-Integrity Foundation RC  
**Upstream Baselines:** frozen v0.0.2 L1/L2; frozen v0.0.3 L3

## 1. Purpose

This directory contains separately controlled development toward SCAF executable governance.

The frozen v0.0.2 and v0.0.3 baselines are not modified in place. Executable-governance artifacts are downstream representations, schemas, validators, integrity controls and later enforcement mechanisms that must preserve the authority semantics of those frozen baselines.

## 2. Current rc07 Scope

The independent v0.0.4rc06 review returned:

```text
V0.0.4 CANONICAL-SCHEMA BINDING / VALIDATOR-CLI HARDENING GATE: YES
```

The review resolved `R5-01` with no new finding and accepted the canonical-schema-bound authority-registry validation foundation.

Current executable-governance artifacts are:

- `00_SCAF_Machine_Readable_Authority_Model.md` — accepted authority model and deterministic record contract;
- `01_SCAF_v0.0.4rc02_Authority_Model_Determinism_Cleanup.md` — `R1-01` closure record;
- `02_SCAF_v0.0.4rc03_Initial_Authority_Registry_Serialization.md` — accepted 294-record registry serialization contract;
- `03_SCAF_v0.0.4rc04_Authority_Registry_Release_State_Documentation_Cleanup.md` — resolved `R3-01` cleanup record;
- `04_SCAF_v0.0.4rc05_Authority_Registry_Schema_and_Structural_Validator_Foundation.md` — accepted schema/validator foundation;
- `05_SCAF_v0.0.4rc06_Canonical_Schema_Binding_and_Validator_CLI_Hardening.md` — accepted canonical-schema/CLI hardening; `R5-01` resolved;
- `06_SCAF_v0.0.4rc07_Frozen_Baseline_Release_Integrity_Foundation.md` — current bounded release-integrity contract;
- repository-root `authority-registry.yaml` — accepted rc03 294-record controlled representation;
- `schemas/authority-registry.schema.json` and `tools/scaf_validator/` — accepted semantic/representation conformance path;
- `release-integrity/frozen-baseline-manifest.json` and `tools/scaf_release_integrity/` — current frozen-byte integrity path.

rc07 protects exactly the frozen v0.0.2 normative tree and frozen v0.0.3 L3 tree. It does not hash-own the authority registry/schema/validator and does not change their accepted semantics.

Frozen Markdown remains semantic authority. The integrity manifest is reviewed cryptographic metadata; the checker is a subordinate byte-integrity check. The manifest is not a self-authenticating external trust root.

rc07 does **not** add CI enforcement, manifest signing, registry generation, generated reverse indexes/views, code generation, automatic applicability inference, machine-readable L2→L3 relations, new L3 Patterns, M3/M4 or L4 guidance.

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
frozen-baseline manifest + standalone release-integrity checker (current rc07)
        ↓
later separately gated CI / generated views / executable governance
```

Semantic validation and release integrity are deliberately separate controls. Each transition requires a separately reviewed repository state.

## 4. Current Gate

The independent v0.0.4rc07 review shall determine whether the canonical manifest/checker accurately protects all and only the frozen v0.0.2/v0.0.3 files, fails closed on drift, preserves accepted rc06 semantic-validation boundaries, and makes no unsupported claim of manifest self-authentication or CI enforcement.

Expected gate label:

```text
V0.0.4 FROZEN-BASELINE RELEASE-INTEGRITY FOUNDATION GATE
```
