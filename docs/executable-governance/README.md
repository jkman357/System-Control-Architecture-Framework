# SCAF Executable Governance Development

**Development Release:** v0.0.4rc10  
**Status:** CI Trust-Input / Executable-Governance Gate Foundation RC  
**Upstream Baselines:** frozen v0.0.2 L1/L2; frozen v0.0.3 L3

## 1. Purpose

This directory contains separately controlled development toward SCAF executable governance.

The frozen v0.0.2 and v0.0.3 baselines are not modified in place. Executable-governance artifacts are downstream representations, schemas, validators, integrity controls and later enforcement mechanisms that must preserve the authority semantics of those frozen baselines.

## 2. Current rc10 Scope

The independent v0.0.4rc09 review returned:

```text
V0.0.4 EXTERNAL-PIN LOCAL-ARTIFACT SYMLINK-HARDENING GATE: YES
```

`R8-01` is closed with no new findings. rc10 therefore does not reopen the external-pin architecture; it builds a bounded CI trust-input and orchestration layer above the three accepted executable controls.

Current executable-governance artifacts are:

- `00_SCAF_Machine_Readable_Authority_Model.md` — accepted authority model and deterministic record contract;
- `01_SCAF_v0.0.4rc02_Authority_Model_Determinism_Cleanup.md` — `R1-01` closure record;
- `02_SCAF_v0.0.4rc03_Initial_Authority_Registry_Serialization.md` — accepted 294-record registry serialization contract;
- `03_SCAF_v0.0.4rc04_Authority_Registry_Release_State_Documentation_Cleanup.md` — resolved `R3-01` cleanup record;
- `04_SCAF_v0.0.4rc05_Authority_Registry_Schema_and_Structural_Validator_Foundation.md` — accepted schema/validator foundation;
- `05_SCAF_v0.0.4rc06_Canonical_Schema_Binding_and_Validator_CLI_Hardening.md` — accepted canonical-schema/CLI hardening;
- `06_SCAF_v0.0.4rc07_Frozen_Baseline_Release_Integrity_Foundation.md` — accepted local frozen-baseline release-integrity foundation;
- `07_SCAF_v0.0.4rc08_Release_Integrity_Diagnostic_Cleanup_and_External_Pinning_Foundation.md` — accepted external-pinning foundation;
- `08_SCAF_v0.0.4rc09_External_Pin_Local_Artifact_Symlink_Hardening.md` — accepted `R8-01` closure;
- `09_SCAF_v0.0.4rc10_CI_Trust_Input_Model_and_Executable_Governance_Gate_Foundation.md` — current CI trust-input/gate contract;
- repository-root `authority-registry.yaml` — accepted rc03 representation;
- `schemas/authority-registry.schema.json` and `tools/scaf_validator/` — accepted semantic/representation conformance path;
- `release-integrity/frozen-baseline-manifest.json` and `tools/scaf_release_integrity/` — accepted local frozen-byte integrity path;
- `tools/scaf_external_pin/` — accepted external-pin verification path;
- `tools/scaf_ci_gate/` and `.github/workflows/scaf-executable-governance.yml` — current bounded trusted-main/manual CI foundation.

Frozen Markdown remains semantic authority. rc10 does **not** add fork-PR execution, `pull_request_target`, signing/PKI/provenance, workflow self-authentication, canonical trust-bundle storage/distribution, registry generation, generated views/indexes, code generation, automatic applicability inference, machine-readable L2→L3 relations, new L3 Patterns, M3/M4 or L4 guidance.

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
local pinned-artifact symlink hardening
        ↓
CI trust-input bootstrap + executable-governance gate foundation (current rc10)
        ↓
later separately gated PR/merge enforcement / signing / provenance / generated views
```

Semantic validation, frozen-byte integrity, and external identity pinning remain deliberately separate controls.

## 4. Current Gate

The independent v0.0.4rc10 review shall determine whether the external CI trust bundle is deterministic, gate bootstrap and six control-plane identity pins are fail-closed, the accepted external pin is consistent with top-level trust pins, the three accepted controls execute in fixed order, trusted-main/manual GitHub Actions behavior is correctly bounded, and no deferred PR/signing/L3/M3/M4/L4 scope is introduced.

Expected gate label:

```text
V0.0.4 CI TRUST-INPUT / EXECUTABLE-GOVERNANCE GATE FOUNDATION GATE
```
