# SCAF Executable Governance Development

**Development Release:** v0.0.4rc01  
**Status:** Authority-model foundation RC  
**Upstream Baselines:** frozen v0.0.2 L1/L2; frozen v0.0.3 L3

## 1. Purpose

This directory contains separately controlled development toward SCAF executable governance.

The frozen v0.0.2 and v0.0.3 baselines are not modified in place. Executable-governance artifacts are downstream representations, indexes, validators and enforcement mechanisms that must preserve the authority semantics of those frozen baselines.

## 2. v0.0.4rc01 Scope

v0.0.4rc01 introduces the semantic foundation required before a machine-readable authority registry is serialized or validated:

- the machine-readable authority model;
- the initial registry population boundary;
- source-of-truth and precedence rules;
- record identity and authority-class semantics;
- minimum future record fields and their meaning;
- conflict, omission and stale-representation behavior;
- explicit separation between L1/L2 normative authority and L3 Pattern catalog artifacts.

v0.0.4rc01 intentionally does **not** add:

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

The independent v0.0.4rc01 review shall determine whether the authority model is sufficiently precise to authorize a later RC to serialize the initial frozen L1/L2 authority registry.

Expected gate label:

```text
V0.0.4 AUTHORITY-MODEL FOUNDATION GATE
```
