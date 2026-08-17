# SCAF Executable Governance Baseline

**Release:** v0.0.4  
**Status:** Frozen Executable Governance Baseline  
**Upstream Baselines:** frozen v0.0.2 L1/L2; frozen v0.0.3 L3

## Current Development Line

`v0.0.5rc3 — L3 Machine-Readable Trace Serialization Foundation` follows the clean rc2 model-closure gate. It adds the first concrete subordinate serialization, repository-root `l3-trace-registry.yaml`, containing the accepted frozen population of 119 typed L2-to-L3 relations.

Current v0.0.5 records:

- `14_SCAF_v0.0.5rc1_L3_Machine_Readable_Trace_Representation_Model_Foundation.md` — accepted model foundation as amended by rc2;
- `15_SCAF_v0.0.5rc2_L3_Trace_Model_Determinism_and_Qualifier_Fidelity_Cleanup.md` — accepted `R1-01` / `R1-02` closure;
- `16_SCAF_v0.0.5rc3_L3_Machine_Readable_Trace_Serialization_Foundation.md` — current concrete serialization contract and review candidate.

Detailed version/review history remains in repository-root `CHANGELOG.md`.

## 1. Purpose

This directory contains separately controlled development toward SCAF executable governance.

The frozen v0.0.2 and v0.0.3 baselines are not modified in place. Executable-governance artifacts are downstream representations, schemas, validators, integrity controls and later enforcement mechanisms that must preserve the authority semantics of those frozen baselines.

## 2. Frozen v0.0.4 Position

The independent v0.0.4rc13 closure review returned:

```text
R12-01: RESOLVED
V0.0.4 FREEZE-CANDIDATE CONTROL-CHAIN DOCUMENTATION CLOSURE GATE: YES
Critical: 0
Major: 0
Minor: 0
Trivial: 0
Open upstream findings: 0
```

By subsequent explicit governance decision, the reviewed rc13 milestone is now formally frozen as **SCAF v0.0.4 — Frozen Executable Governance Baseline**. The freeze adds no executable control, CI trigger, trust source, semantic authority, or downstream framework layer; it synchronizes release/freeze state only.

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
- `09_SCAF_v0.0.4rc10_CI_Trust_Input_Model_and_Executable_Governance_Gate_Foundation.md` — accepted trust model / CI-gate foundation record with historical `R10-01` review basis;
- `10_SCAF_v0.0.4rc11_CI_Repository_Path_Component_and_Root_Binding_Hardening.md` — accepted `R10-01` closure;
- `11_SCAF_v0.0.4rc12_Executable_Governance_Milestone_Consolidation_and_Freeze_Candidate.md` — milestone consolidation / freeze-candidate record with rc13 R12-01 clarification;
- `12_SCAF_v0.0.4rc13_Freeze_Candidate_Control_Chain_Documentation_Closure.md` — accepted focused R12-01 documentation closure record;
- `13_SCAF_v0.0.4_Formal_Freeze_Decision.md` — formal v0.0.4 freeze decision and post-freeze governance boundary;
- repository-root `authority-registry.yaml` — accepted rc03 representation;
- `schemas/authority-registry.schema.json` and `tools/scaf_validator/` — accepted semantic/representation conformance path;
- `release-integrity/frozen-baseline-manifest.json` and `tools/scaf_release_integrity/` — accepted local frozen-byte integrity path;
- `tools/scaf_external_pin/` — accepted external-pin verification path;
- `tools/scaf_ci_gate/` and `.github/workflows/scaf-executable-governance.yml` — accepted trusted-main/manual gate with rc11 path/root hardening.

Frozen Markdown remains semantic authority. The formal v0.0.4 freeze does **not** add fork-PR execution, `pull_request_target`, signing/PKI/provenance, workflow self-authentication, canonical trust-bundle storage/distribution, registry generation, generated views/indexes, code generation, automatic applicability inference, machine-readable L2→L3 relations, new L3 Patterns, M3/M4 or L4 guidance.

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
repository path-component + root-binding hardening
        ↓
executable-governance milestone consolidation / freeze candidate (rc12)
        ↓
control-chain documentation closure (rc13)
        ↓
formal v0.0.4 executable-governance freeze
        ↓
later separately gated PR/merge enforcement / signing / provenance / generated views
```

Semantic validation, frozen-byte integrity, and external identity pinning remain deliberately separate controls.

## 4. Frozen Gate State

The independent v0.0.4rc13 review confirmed `R12-01: RESOLVED` and returned:

```text
V0.0.4 FREEZE-CANDIDATE CONTROL-CHAIN DOCUMENTATION CLOSURE GATE: YES
```

The accepted review preserved all 41 regressions, the canonical outside-repository trust-bundle production gate, the capability-layering/runtime-order distinction, frozen L1/L2 and L3 identities, and zero open findings. The later explicit governance decision therefore created the formal v0.0.4 frozen baseline recorded in `13_SCAF_v0.0.4_Formal_Freeze_Decision.md`.

No in-place semantic or executable modification is permitted after this freeze.
