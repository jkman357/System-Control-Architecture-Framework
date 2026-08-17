# SCAF Executable Governance Development

**Development Release:** v0.0.4rc11  
**Status:** CI Repository Path-Component / Root-Binding Hardening RC  
**Upstream Baselines:** frozen v0.0.2 L1/L2; frozen v0.0.3 L3

## 1. Purpose

This directory contains separately controlled development toward SCAF executable governance.

The frozen v0.0.2 and v0.0.3 baselines are not modified in place. Executable-governance artifacts are downstream representations, schemas, validators, integrity controls and later enforcement mechanisms that must preserve the authority semantics of those frozen baselines.

## 2. Current rc11 Scope

The independent v0.0.4rc10 review returned:

```text
V0.0.4 CI TRUST-INPUT / EXECUTABLE-GOVERNANCE GATE FOUNDATION GATE: NO
```

The review found the trust model conceptually sound but opened `R10-01` (**Major**): parent-directory symlink components could redirect `gate.py` or a downstream control into a pristine nested shadow repository and permit normal PASS while the actual checkout root was modified.

rc11 is limited to closing that path/root-binding failure. It adds no new CI trigger, trust source, semantic authority, or downstream framework layer.

Current executable-governance artifacts are:

- `00_SCAF_Machine_Readable_Authority_Model.md` — accepted authority model and deterministic record contract;
- `01_SCAF_v0.0.4rc02_Authority_Model_Determinism_Cleanup.md` — `R1-01` closure record;
- `02_SCAF_v0.0.4rc03_Initial_Authority_Registry_Serialization.md` — accepted 294-record registry serialization contract;
- `03_SCAF_v0.0.4rc04_Authority_Registry_Release_State_Documentation_Cleanup.md` — resolved `R3-01` cleanup record;
- `04_SCAF_v0.0.4rc05_Authority_Registry_Schema_and_Structural_Validator_Foundation.md` — accepted schema/validator foundation;
- `05_SCAF_v0.0.4rc06_Canonical_Schema_Binding_and_Validator_CLI_Hardening.md` — accepted canonical-schema/CLI hardening;
- `06_SCAF_v0.0.4rc07_Frozen_Baseline_Release_Integrity_Foundation.md` — accepted local frozen-baseline release-integrity foundation;
- `07_SCAF_v0.0.4rc08_Release_Integrity_Diagnostic_Cleanup_and_External_Pinning_Foundation.md` — external-pinning foundation;
- `08_SCAF_v0.0.4rc09_External_Pin_Local_Artifact_Symlink_Hardening.md` — accepted `R8-01` closure;
- `09_SCAF_v0.0.4rc10_CI_Trust_Input_Model_and_Executable_Governance_Gate_Foundation.md` — rc10 trust-input/gate contract and `R10-01` review basis;
- `10_SCAF_v0.0.4rc11_CI_Repository_Path_Component_and_Root_Binding_Hardening.md` — current focused `R10-01` closure;
- repository-root `authority-registry.yaml` — accepted rc03 representation;
- `schemas/authority-registry.schema.json` and `tools/scaf_validator/` — accepted semantic/representation conformance path;
- `release-integrity/frozen-baseline-manifest.json` and `tools/scaf_release_integrity/` — accepted local frozen-byte integrity path;
- `tools/scaf_external_pin/` — accepted external-pin verification path;
- `tools/scaf_ci_gate/` and `.github/workflows/scaf-executable-governance.yml` — current trusted-main/manual gate with rc11 root/path hardening.

Frozen Markdown remains semantic authority. rc11 does **not** add fork-PR execution, `pull_request_target`, signing/PKI/provenance, workflow self-authentication, canonical trust-bundle storage/distribution, registry generation, generated views/indexes, code generation, automatic applicability inference, machine-readable L2→L3 relations, new L3 Patterns, M3/M4 or L4 guidance.

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
CI trust-input bootstrap + executable-governance gate foundation
        ↓
repository path-component + root-binding hardening (current rc11)
        ↓
later separately gated PR/merge enforcement / signing / provenance / generated views
```

Semantic validation, frozen-byte integrity, and external identity pinning remain deliberately separate controls.

## 4. Current Gate

The independent v0.0.4rc11 review shall determine whether `R10-01` is fully closed: parent-directory symlinks must not redirect the gate or any pinned downstream control into a shadow repository; the production gate and workflow bootstrap must bind to the intended checkout root; every successful downstream stage must report that same root; and accepted trust-bundle/stage-order/frozen/authority/L3 boundaries must remain unchanged.

Expected gate label:

```text
V0.0.4 CI REPOSITORY PATH-COMPONENT / ROOT-BINDING HARDENING GATE
```
