# SCAF v0.0.5rc7 — L3 Deterministic Trace Views / Query Foundation

## 1. Purpose

v0.0.5rc7 introduces the first controlled **consumption** capability over the accepted and source-validated L3 machine-readable trace.

The objective is deliberately bounded:

```text
validated l3-trace-registry.yaml
        ↓
read-only deterministic view/query
        ↓
L2 authority -> typed L3 Pattern relations
or
L3 Pattern -> typed L2 authority relations
```

This RC does not create another semantic authority, persisted index, resolver, recommender, project-applicability engine, Pattern-selection engine, or CI/trust-chain control.

## 2. Dependency Basis

The rc7 capability is downstream of the accepted v0.0.5 trace chain:

```text
frozen v0.0.3 Pattern Markdown authority
        ↓
rc1/rc2 trace representation model
        ↓
rc3 l3-trace-registry.yaml
        ↓
rc4 schema + deterministic source-extraction contract
        ↓
rc5 source-aware trace validator
        ↓
rc6 fail-closed source-boundary hardening
        ↓
rc7 deterministic read-only trace consumption
```

The independent rc6 review resolved `R5-01` and `R5-02`, opened no new findings, and returned:

```text
V0.0.5 L3 TRACE VALIDATOR FAIL-CLOSED SOURCE-BOUNDARY HARDENING GATE: YES
```

## 3. New Development Control

rc7 adds:

```text
tools/scaf_trace_views/
```

Canonical examples:

```text
python -m tools.scaf_trace_views.query --l2 SCAF-ROB-004
python -m tools.scaf_trace_views.query --pattern SCAF-PAT-COM-001
python -m tools.scaf_trace_views.query --l2 SCAF-ROB-004 --format json
```

The tool is stdout-only. It does not create or rewrite repository artifacts.

## 4. Validated-Source-Only Contract

A view shall be produced only after `tools.scaf_trace_validator.validator.validate_repository()` returns a complete PASS for the requested repository root.

If source-aware validation fails, rc7 shall fail closed before emitting a view payload.

Therefore:

```text
invalid frozen source
or
invalid / drifted trace registry
or
schema/source/authority/order failure
        ↓
NO VIEW
RESULT: FAIL
```

The rc7 tool does not create an alternate validation path and does not bypass the rc6 source-aware proof.

## 5. View Directions

### 5.1 L2 -> L3

A frozen `Project-Applicable Obligation` identity may be queried to return every accepted typed L3 trace relation that references it. Framework Normative Invariants are outside the current L2-to-L3 catalog-trace query domain.

View ordering shall be:

1. relation type in accepted order:
   1. `primary_realization_candidate`;
   2. `supporting_realization`;
   3. `constraint_input`;
2. `pattern_id` ascending.

A known Project-Applicable Obligation with no current L3 trace is a valid deterministic result:

```text
relation_count: 0
relations: []
```

Zero relations means only that the current frozen catalog carries no accepted L3 trace edge for that authority identity. It is not a negative applicability or compliance decision.

An ID that is absent from the frozen authority registry or is not classified as a `Project-Applicable Obligation` shall fail closed for this L2-to-L3 query surface.

### 5.2 L3 -> L2

A known frozen L3 Pattern identity may be queried to return every accepted typed L2 trace relation for that Pattern.

View ordering shall be:

1. relation type in accepted order;
2. `l2_id` ascending.

An unknown Pattern identity shall fail closed.

## 6. Relation Fidelity

Every view relation preserves the accepted seven-field serialized record exactly:

```text
pattern_id
relation_type
l2_id
pattern_source_path
pattern_source_field
source_release
qualifier
```

The query layer shall not:

- flatten the three relation classes;
- drop or rewrite material qualifier context;
- collapse a multi-type Pattern/L2 pair;
- substitute generic `satisfies` / `related_to` / `implements` semantics;
- add recommendation, ranking, confidence, applicability, selection, compliance, verification, evidence or closure state.

The two accepted multi-type pairs in `SCAF-PAT-COM-001` therefore remain distinct typed records.

## 7. Derived-View Boundary

rc7 views are reproducible navigation/consumption only.

```text
Queried / Traced / Serialized / Schema-valid / Source-validated / Resolved
!= Applicable
!= Recommended
!= Selected
!= Satisfied
!= Compliant
!= Verified
!= Closed
```

No view output has project decision authority.

## 8. Output Contract

The CLI supports deterministic text and deterministic JSON on stdout.

The JSON view object contains exactly:

```text
trace_view_version
direction
query_id
relation_count
relations
```

`trace_view_version` is `1` for this foundation.

The JSON representation carries no timestamp, environment path, recommendation score, ranking score, or other run-dependent data. Repeated queries over the same validated repository state shall therefore produce byte-stable JSON output.

The human-readable text form is navigation-oriented only and preserves relation type, qualifier, source locator, and source release.

## 9. Regression Foundation

rc7 adds an independent development suite under:

```text
tools/scaf_trace_views/tests/
```

The suite shall cover at least:

- known L2 -> L3 query;
- known Pattern -> L2 query;
- current multi-type Pattern/L2 preservation;
- material qualifier preservation;
- known-but-untraced L2 zero-result semantics;
- unknown L2 fail closed;
- Framework Normative Invariant rejection from the Project-Applicable L2 trace-query domain;
- unknown Pattern fail closed;
- deterministic view ordering in both directions;
- exact seven-field relation shape preservation;
- complete 119-relation coverage through all Pattern views;
- complete 119-relation coverage through all L2 views;
- absence of project-decision state in the view contract;
- deterministic JSON rendering;
- invalid serialized registry blocking consumption;
- invalid frozen source blocking consumption;
- CLI machine-readable output and failure behavior.

The initial rc7 suite contains **17 tests**. It is a v0.0.5 development regression inventory and does not alter the frozen v0.0.4 41-test inventory or the rc6 trace-validator 24-test inventory.

## 10. Preserved Upstream State

rc7 does not modify:

- frozen v0.0.2 normative authority;
- frozen v0.0.3 L3 Pattern sources;
- frozen v0.0.4 executable-governance controls/trust bundle;
- `authority-registry.yaml`;
- `l3-trace-registry.yaml`;
- `schemas/l3-trace-registry.schema.json`;
- `tools/scaf_trace_validator/`;
- `.github/workflows/scaf-executable-governance.yml`.

## 11. Explicit Non-Goals / Deferred Work

rc7 does not implement:

- persisted/generated forward or reverse index files;
- trace-registry generation or rewriting;
- authority/context resolver selection logic;
- semantic relevance/ranking;
- project applicability inference;
- Pattern recommendation or auto-selection;
- satisfaction/compliance/verification/evidence/closure inference;
- new L3 Patterns, M3/M4, or L4 guidance;
- code generation;
- trace-view CI/merge enforcement;
- expansion of the frozen v0.0.4 six-artifact trust chain.

Any of those capabilities requires a later separately bounded decision and review.

## 12. rc7 Gate Intent

The rc7 review should establish that the new query layer is a deterministic, lossless, read-only consumer of already validated trace data and cannot silently become a second authority, recommendation engine, or bypass around rc6 validation.
