# SCAF v0.0.5rc6 — L3 Trace Validator Fail-Closed Source-Boundary Hardening

**Development Release:** v0.0.5rc6  
**Status:** Focused R5-01 / R5-02 Closure Candidate  
**Upstream Review:** v0.0.5rc5 gate `NO` with two Major findings  
**Frozen Baselines:** v0.0.2 L1/L2; v0.0.3 L3; v0.0.4 Executable Governance

## 1. Purpose

The rc5 source-aware trace validator correctly passed the accepted repository and reproduced the accepted 119-record trace population, but independent adversarial review identified two fail-open implementation defects:

- `R5-01` — Constraint Inputs parsing accepted missing or misplaced comma separators outside the reviewed rc4 extraction language.
- `R5-02` — required metadata-row extraction scanned same-key table rows outside the authoritative `## Metadata` table.

rc6 is limited to closing those implementation defects and adding focused regression coverage. It does not add a new trace semantic, representation, generator, resolver, or enforcement capability.

## 2. Authority Boundary

The accepted order remains:

```text
Frozen v0.0.3 Pattern Markdown metadata
        ↓ semantic trace authority
accepted rc4 source-extraction contract
        ↓ deterministic source interpretation
accepted rc4 trace JSON Schema
        ↓ structural representation contract
accepted rc3 l3-trace-registry.yaml
        ↓ subordinate representation under test
rc6 hardened source-aware trace validator
        ↓ executable conformance proof
```

The validator remains subordinate to the reviewed rc4 contract. Parser convenience must not broaden the accepted source language or authority surface.

## 3. R5-01 Closure — Delimiter Position Hardening

Constraint Inputs parsing now distinguishes clause start from inter-item transition.

At clause start:

- whitespace is permitted;
- an optional reviewed leading qualifier (`applicable` or `conditional`) is permitted;
- a leading comma is rejected.

Between later L2 IDs/items:

- an explicit comma separator is mandatory;
- comma + whitespace is permitted;
- comma + reviewed leading qualifier is permitted;
- whitespace-only adjacency is rejected;
- a later leading qualifier without the preceding comma is rejected;
- repeated/empty comma-separated item forms are rejected.

This change does not add any new qualifier token, grouping rule, or semantic interpretation. The accepted semicolon scope reset and trailing-context rules are preserved.

## 4. R5-02 Closure — Metadata-Table Authority Binding

Machine-authoritative extraction now requires exactly one section heading:

```text
## Metadata
```

Within that section, the validator requires exactly one metadata table beginning with:

```text
| Field | Value |
|---|---|
```

Only contiguous rows in that table may supply the required machine-authoritative fields:

```text
Pattern ID
Primary L2 Trace
Supporting L2 Trace
Constraint Inputs
```

Each required row must occur exactly once in that table.

Rows with the same key under later narrative headings or narrative tables do not create, replace, or supplement machine authority. If the authoritative Metadata table is incomplete, validation fails even if an identical same-key row exists elsewhere in the Markdown file.

## 5. Regression Expansion

The trace-validator development suite expands from 16 to 24 tests. New rc6 coverage includes:

1. adjacent Constraint Input IDs without comma -> FAIL;
2. missing comma before later `applicable` -> FAIL;
3. leading comma before first Constraint Input ID -> FAIL;
4. authoritative row moved to later narrative table -> FAIL;
5. authoritative row removed while altered same-key narrative row exists -> FAIL;
6. missing `## Metadata` section -> FAIL;
7. Metadata table missing a required trace row -> FAIL;
8. same-key narrative table while authoritative Metadata remains complete -> ignored, accepted repository remains PASS.

The existing tests continue to cover source/serialization mismatch, qualifier fidelity, tuple uniqueness, canonical ordering, authority resolution, unsupported qualifier syntax, metadata-row duplication, and narrative prose non-authority.

## 6. Preserved Artifacts and Non-Capabilities

rc6 does not modify:

- `l3-trace-registry.yaml`;
- `schemas/l3-trace-registry.schema.json`;
- `authority-registry.yaml`;
- frozen `docs/normative/`;
- frozen `docs/l3/`;
- frozen v0.0.4 validator/release-integrity/external-pin/CI-gate controls;
- frozen CI workflow/trust bundle.

rc6 does not add:

- trace registry generation/rewriting;
- generated forward/reverse views;
- resolver/context packaging;
- project applicability or Pattern-selection inference;
- satisfaction/compliance/verification/evidence/closure inference;
- new L3, M3/M4, or L4 content;
- code generation;
- CI/merge/trust-chain expansion.

## 7. Acceptance Target

The rc6 review shall independently reproduce both rc5 fail-open classes and confirm they now fail closed while the accepted repository still reconstructs the exact accepted 119-record / 15-qualifier population.

Expected closure target:

```text
R5-01: RESOLVED
R5-02: RESOLVED

V0.0.5 L3 TRACE VALIDATOR FAIL-CLOSED SOURCE-BOUNDARY HARDENING GATE: YES
```
