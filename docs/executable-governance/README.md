# SCAF Executable Governance Development

**Development Release:** v0.0.4rc02  
**Status:** Authority-model determinism cleanup / closure RC  
**Upstream Baselines:** frozen v0.0.2 L1/L2; frozen v0.0.3 L3

## 1. Purpose

This directory contains separately controlled development toward SCAF executable governance.

The frozen v0.0.2 and v0.0.3 baselines are not modified in place. Executable-governance artifacts are downstream representations, indexes, validators and enforcement mechanisms that must preserve the authority semantics of those frozen baselines.

## 2. Current rc02 Scope

The independent v0.0.4rc01 authority-model foundation review returned:

```text
V0.0.4 AUTHORITY-MODEL FOUNDATION GATE: YES, AFTER MINOR CLEANUP
```

with one blocking Minor finding, `R1-01`. v0.0.4rc02 is a focused cleanup RC that closes only the initial serialization ambiguity for:

- `layer`;
- `source_anchor`;
- `status`;
- and the review-recommended initial empty/omitted `relations` population rule.

The deterministic initial values/rules are defined in `00_SCAF_Machine_Readable_Authority_Model.md` and summarized in `01_SCAF_v0.0.4rc02_Authority_Model_Determinism_Cleanup.md`.

rc02 intentionally does **not** add:

- `authority-registry.yaml` or equivalent serialization;
- JSON Schema or another schema language;
- validator implementation;
- generated reverse index;
- CI enforcement;
- code generation;
- automatic applicability inference;
- L3 Pattern expansion, M3/M4 or L4 guidance.

## 3. Development Order

The controlled order is:

```text
frozen human-readable semantic authority
        ↓
authority model / record contract
        ↓
determinism closure (current rc02)
        ↓
machine-readable registry serialization
        ↓
schema + structural validator
        ↓
regression tests
        ↓
CI / generated views / later executable governance
```

Each transition requires a separately reviewed repository state. A later machine-readable artifact must not silently become normative merely because a tool can parse it.

## 4. Current Gate

The independent v0.0.4rc02 review shall determine whether upstream finding `R1-01` is fully closed and whether the accepted authority model is now deterministic enough to authorize a later RC to serialize the initial 294 frozen L1/L2 authority records.

Expected gate label:

```text
V0.0.4 AUTHORITY-MODEL DETERMINISM CLOSURE GATE
```
