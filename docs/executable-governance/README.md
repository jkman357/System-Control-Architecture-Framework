# SCAF Executable Governance Development

**Development Release:** v0.0.4rc05  
**Status:** Authority-Registry Schema & Structural Validator Foundation RC  
**Upstream Baselines:** frozen v0.0.2 L1/L2; frozen v0.0.3 L3

## 1. Purpose

This directory contains separately controlled development toward SCAF executable governance.

The frozen v0.0.2 and v0.0.3 baselines are not modified in place. Executable-governance artifacts are downstream representations, schemas, validators and later enforcement mechanisms that must preserve the authority semantics of those frozen baselines.

## 2. Current rc05 Scope

The independent v0.0.4rc04 review returned:

```text
V0.0.4 AUTHORITY-REGISTRY RELEASE-STATE CLEANUP GATE: YES
```

That review resolved `R3-01`, confirmed the accepted rc03 registry remains byte-identical and source-faithful, and found no remaining blocker to opening the separately reviewed schema + structural-validator stage.

Current executable-governance artifacts are:

- `00_SCAF_Machine_Readable_Authority_Model.md` — accepted authority model and deterministic record contract from rc02;
- `01_SCAF_v0.0.4rc02_Authority_Model_Determinism_Cleanup.md` — closure record for `R1-01`;
- `02_SCAF_v0.0.4rc03_Initial_Authority_Registry_Serialization.md` — accepted rc03 serialization format, ownership, reproducibility and population contract;
- `03_SCAF_v0.0.4rc04_Authority_Registry_Release_State_Documentation_Cleanup.md` — resolved `R3-01` cleanup and non-regression record;
- `04_SCAF_v0.0.4rc05_Authority_Registry_Schema_and_Structural_Validator_Foundation.md` — current schema/validator scope, boundaries, commands, tests and review gate;
- repository-root `authority-registry.yaml` — accepted rc03 294-record controlled representation, unchanged in rc05;
- `schemas/authority-registry.schema.json` — structural schema for the accepted rc03 representation;
- `tools/scaf_validator/` — executable structural/source-aware validator and regression tests.

Accepted registry state remains:

```text
294 unique normative authority records
218 Project-Applicable Obligations
76 Framework Normative Invariants
0 SCAF-PAT-* records
representation_release = v0.0.4rc03
relations = [] for all 294 records
```

Frozen normative Markdown remains semantic authority. rc05 does **not** add CI enforcement, registry generation, generated reverse indexes/views, code generation, automatic applicability inference, machine-readable L2→L3 relations, new L3 Patterns, M3/M4 or L4 guidance.

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
release-state documentation cleanup (accepted rc04)
        ↓
schema + structural/source-aware validator + regression tests (current rc05)
        ↓
later separately gated CI / generated views / executable governance
```

Each transition requires a separately reviewed repository state. A schema or validator does not become normative merely because it can reject a representation.

## 4. Current Gate

The independent v0.0.4rc05 review shall determine whether the schema/validator foundation faithfully executes the accepted rc03 ten-field registry contract, fails closed on structural/source-fidelity defects, preserves canonical Markdown precedence, and introduces no deferred-scope expansion.

Expected gate label:

```text
V0.0.4 AUTHORITY-REGISTRY SCHEMA-VALIDATOR FOUNDATION GATE
```
