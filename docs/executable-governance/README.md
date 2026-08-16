# SCAF Executable Governance Development

**Development Release:** v0.0.4rc04  
**Status:** Authority-Registry Release-State Documentation Cleanup RC  
**Upstream Baselines:** frozen v0.0.2 L1/L2; frozen v0.0.3 L3

## 1. Purpose

This directory contains separately controlled development toward SCAF executable governance.

The frozen v0.0.2 and v0.0.3 baselines are not modified in place. Executable-governance artifacts are downstream representations, indexes, validators and enforcement mechanisms that must preserve the authority semantics of those frozen baselines.

## 2. Current rc04 Scope

The independent v0.0.4rc03 serialization review returned:

```text
V0.0.4 INITIAL AUTHORITY-REGISTRY SERIALIZATION GATE: YES, AFTER MINOR CLEANUP
```

The review accepted `authority-registry.yaml` as a technically complete and source-faithful 294-record representation and opened one Minor finding, `R3-01`, against stale current-state/navigation text in the root `README.md`. rc04 closes that repository-state documentation issue only.

Current executable-governance artifacts are:

- `00_SCAF_Machine_Readable_Authority_Model.md` — accepted authority model and deterministic record contract from rc02;
- `01_SCAF_v0.0.4rc02_Authority_Model_Determinism_Cleanup.md` — closure record for `R1-01`;
- `02_SCAF_v0.0.4rc03_Initial_Authority_Registry_Serialization.md` — accepted rc03 serialization format, ownership, reproducibility and population contract;
- `03_SCAF_v0.0.4rc04_Authority_Registry_Release_State_Documentation_Cleanup.md` — focused `R3-01` cleanup and non-regression record;
- repository-root `authority-registry.yaml` — accepted rc03 294-record controlled representation, unchanged in rc04.

Accepted registry state remains:

```text
294 unique normative authority records
218 Project-Applicable Obligations
76 Framework Normative Invariants
0 SCAF-PAT-* records
representation_release = v0.0.4rc03
relations = [] for all 294 records
```

Frozen normative Markdown remains semantic authority. rc04 intentionally does **not** add schema, validator, generator, generated reverse indexes, CI enforcement, code generation, automatic applicability inference, machine-readable L2→L3 relations, new L3 Patterns, M3/M4 or L4 guidance.


## 3. Development Order

The controlled order is:

```text
frozen human-readable semantic authority
        ↓
authority model / record contract
        ↓
determinism closure
        ↓
machine-readable registry serialization (accepted rc03)
        ↓
release-state documentation cleanup (current rc04)
        ↓
schema + structural validator
        ↓
regression tests
        ↓
CI / generated views / later executable governance
```

Each transition requires a separately reviewed repository state. A machine-readable artifact does not become normative merely because a tool can parse it.

## 4. Current Gate

The independent v0.0.4rc04 review shall determine whether `R3-01` is fully closed and whether the repository's release-state/navigation text now consistently reflects the accepted rc03 registry state without modifying the registry or frozen upstream semantics.

Expected gate label:

```text
V0.0.4 AUTHORITY-REGISTRY RELEASE-STATE CLEANUP GATE
```
