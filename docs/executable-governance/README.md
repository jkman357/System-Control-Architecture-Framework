# SCAF Executable Governance Development

**Development Release:** v0.0.4rc06  
**Status:** Canonical Schema Binding & Validator CLI Hardening RC  
**Upstream Baselines:** frozen v0.0.2 L1/L2; frozen v0.0.3 L3

## 1. Purpose

This directory contains separately controlled development toward SCAF executable governance.

The frozen v0.0.2 and v0.0.3 baselines are not modified in place. Executable-governance artifacts are downstream representations, schemas, validators and later enforcement mechanisms that must preserve the authority semantics of those frozen baselines.

## 2. Current rc06 Scope

The independent v0.0.4rc05 review returned:

```text
V0.0.4 AUTHORITY-REGISTRY SCHEMA-VALIDATOR FOUNDATION GATE: YES, AFTER MINOR CLEANUP
```

The review accepted the default canonical schema/validator path and all seven rc05 regression tests, but opened one Minor finding, `R5-01`: the public `--schema` CLI override could substitute an arbitrary valid JSON Schema and still emit normal `RESULT: PASS`.

Current executable-governance artifacts are:

- `00_SCAF_Machine_Readable_Authority_Model.md` — accepted authority model and deterministic record contract from rc02;
- `01_SCAF_v0.0.4rc02_Authority_Model_Determinism_Cleanup.md` — closure record for `R1-01`;
- `02_SCAF_v0.0.4rc03_Initial_Authority_Registry_Serialization.md` — accepted rc03 serialization format, ownership, reproducibility and population contract;
- `03_SCAF_v0.0.4rc04_Authority_Registry_Release_State_Documentation_Cleanup.md` — resolved `R3-01` cleanup and non-regression record;
- `04_SCAF_v0.0.4rc05_Authority_Registry_Schema_and_Structural_Validator_Foundation.md` — accepted schema/validator foundation subject only to `R5-01` cleanup;
- `05_SCAF_v0.0.4rc06_Canonical_Schema_Binding_and_Validator_CLI_Hardening.md` — current focused `R5-01` closure contract;
- repository-root `authority-registry.yaml` — accepted rc03 294-record controlled representation, unchanged;
- `schemas/authority-registry.schema.json` — accepted rc05 structural schema, unchanged;
- `tools/scaf_validator/` — validator with canonical production CLI binding plus regression tests.

The production CLI no longer accepts caller-selected `--schema` or `--repo-root` arguments. It derives the repository root from the reviewed module location and always uses that repository's canonical schema/source. `--registry <path>` remains available only to choose the representation being checked.

Accepted registry state remains:

```text
294 unique normative authority records
218 Project-Applicable Obligations
76 Framework Normative Invariants
0 SCAF-PAT-* records
representation_release = v0.0.4rc03
relations = [] for all 294 records
```

Frozen normative Markdown remains semantic authority. rc06 does **not** add CI enforcement, registry generation, generated reverse indexes/views, code generation, automatic applicability inference, machine-readable L2→L3 relations, new L3 Patterns, M3/M4 or L4 guidance.

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
schema + structural/source-aware validator + regression tests (accepted rc05, conditional cleanup)
        ↓
canonical schema binding + validator CLI hardening (current rc06)
        ↓
later separately gated CI / generated views / executable governance
```

Each transition requires a separately reviewed repository state. A schema or validator does not become normative merely because it can reject a representation.

## 4. Current Gate

The independent v0.0.4rc06 review shall determine whether `R5-01` is fully closed: the production CLI must be bound to the canonical repository schema/source, the prior alternate-schema false-PASS path must be unavailable, the new CLI regression must pass, and accepted upstream registry/schema/frozen content must remain unchanged.

Expected gate label:

```text
V0.0.4 CANONICAL-SCHEMA BINDING / VALIDATOR-CLI HARDENING GATE
```
