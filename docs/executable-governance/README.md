# SCAF Executable Governance Development

**Development Release:** v0.0.4rc03  
**Status:** Initial 294-record authority-registry serialization RC  
**Upstream Baselines:** frozen v0.0.2 L1/L2; frozen v0.0.3 L3

## 1. Purpose

This directory contains separately controlled development toward SCAF executable governance.

The frozen v0.0.2 and v0.0.3 baselines are not modified in place. Executable-governance artifacts are downstream representations, indexes, validators and enforcement mechanisms that must preserve the authority semantics of those frozen baselines.

## 2. Current rc03 Scope

The independent v0.0.4rc02 determinism-closure review returned:

```text
V0.0.4 AUTHORITY-MODEL DETERMINISM CLOSURE GATE: YES
```

with upstream finding `R1-01` resolved and no remaining blocking finding. rc03 therefore performs the separately reviewable next step: serialization of the initial frozen L1/L2 authority registry.

Current rc03 artifacts are:

- `00_SCAF_Machine_Readable_Authority_Model.md` — accepted authority model and deterministic record contract from rc02;
- `01_SCAF_v0.0.4rc02_Authority_Model_Determinism_Cleanup.md` — closure record for `R1-01`;
- `02_SCAF_v0.0.4rc03_Initial_Authority_Registry_Serialization.md` — rc03 format, ownership, reproducibility, population and gate decision;
- repository-root `authority-registry.yaml` — initial 294-record controlled representation.

The registry is intentionally bounded to:

```text
294 unique normative authority records
218 Project-Applicable Obligations
76 Framework Normative Invariants
0 SCAF-PAT-* records
```

Every record uses the accepted deterministic initial values:

```text
record_kind            = normative_requirement
layer                  = l1_l2_normative_authority
source_anchor          = id
source_release         = v0.0.2
representation_release = v0.0.4rc03
status                 = represented
relations              = []
```

The registry is a controlled curated representation/index. Frozen normative Markdown remains semantic authority.

rc03 intentionally does **not** add schema, validator, generator, generated reverse indexes, CI enforcement, code generation, automatic applicability inference, machine-readable L2→L3 relations, new L3 Patterns, M3/M4 or L4 guidance.

## 3. Development Order

The controlled order is:

```text
frozen human-readable semantic authority
        ↓
authority model / record contract
        ↓
determinism closure
        ↓
machine-readable registry serialization (current rc03)
        ↓
schema + structural validator
        ↓
regression tests
        ↓
CI / generated views / later executable governance
```

Each transition requires a separately reviewed repository state. A machine-readable artifact does not become normative merely because a tool can parse it.

## 4. Current Gate

The independent v0.0.4rc03 review shall determine whether `authority-registry.yaml` is a complete and source-faithful representation of the frozen 294-record L1/L2 inventory without expanding authority semantics or importing project/L3 state.

Expected gate label:

```text
V0.0.4 INITIAL AUTHORITY-REGISTRY SERIALIZATION GATE
```
