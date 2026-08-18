# SCAF v0.0.6rc05 — Project Application Serialization Fixture Coverage Hardening

**Development Release:** v0.0.6rc05
**Status:** Serialization Fixture Finding Closure / Review Candidate
**Date:** 2026-08-18
**Upstream Frozen Baselines:** v0.0.2 L1/L2; v0.0.3 L3; v0.0.4 Executable Governance; v0.0.5 L3 Machine-Readable Traceability
**Accepted Development Basis:** v0.0.6rc04 Concrete Project Application Serialization Foundation
**Immediate Predecessor:** v0.0.6rc04
**Review Finding Addressed:** `SCAF-RC04-001` (Minor)

## 1. Decision Purpose

The independent v0.0.6rc04 review accepted the concrete Project Application YAML serialization foundation and returned:

```text
Critical: 0
Major:    0
Minor:    1
Trivial:  0

V0.0.6RC04 SCAF-APP CONCRETE PROJECT APPLICATION SERIALIZATION FOUNDATION GATE: YES
```

The single Minor finding, `SCAF-RC04-001`, did not identify ambiguity in the serialization contract. It identified a bounded fixture-coverage gap: every non-empty role-specific reference list in `examples/project-application.yaml` contained only one element, so the fixture did not materially demonstrate the already-defined ascending reference-list ordering rule or duplicate-free multi-item form.

v0.0.6rc05 closes only that fixture-coverage gap. It does not alter the accepted rc04 serialization semantics and does not advance to schema, validator, resolver, automatic applicability inference, CI completion enforcement, or L4.

## 2. Preserved rc04 Serialization Contract

rc05 preserves the accepted rc04 contract unchanged, including:

- one YAML document with exactly one top-level `records` member;
- the accepted eleven Project Application record fields;
- exact applicability tokens `applicable`, `not_applicable`, and `undetermined`;
- direct applicability basis only through `disposition_basis.summary` / `basis_refs`;
- role separation for `basis_refs`, `decision_refs`, `authority_refs`, `supporting_refs`, and `awaiting_refs`;
- current-state compatibility of `summary`, `basis_refs`, `unresolved_reason`, and `awaiting_refs`;
- required empty-list representation and omission/null rules;
- opaque non-empty string reference representation;
- deterministic record ordering by exact `record_id` ascending;
- deterministic repeating-reference ordering by exact serialized string ascending;
- prohibition of duplicate exact strings within one role-specific list;
- prohibition of duplicate mapping keys, anchors/aliases, merge keys, custom tags, multi-document streams, non-string keys, and YAML null placeholders where omission is required;
- separation between representation invalidity and legitimate engineering-unresolved state;
- all Project Design Authority and project-governance authority boundaries.

The canonical representation contract remains identified by:

```text
representation_release: v0.0.6rc04
```

The fixture remains rc04-conformant. rc05 is a coverage-hardening RC, not a new serialization contract revision.

## 3. Finding SCAF-RC04-001 Closure

### 3.1 Coverage requirement

The fixture shall visibly demonstrate the rc04 multi-item ordering and duplicate-free rules rather than satisfying them only vacuously with zero- or one-item lists.

The rc05 fixture therefore retains exactly three Project Application Records and expands existing illustrative reference lists so each canonical repeating reference role is represented by at least one multi-item example across the fixture:

```text
basis_refs
awaiting_refs
decision_refs
authority_refs
supporting_refs
```

### 3.2 Ordering rule remains unchanged

Every expanded list remains ordered by exact serialized string ascending. rc05 does not introduce semantic priority, engineering priority, authority priority, or insertion-order meaning.

Example shape:

```yaml
basis_refs:
  - "example:artifact:ARCH-001"
  - "example:artifact:ARCH-002"
```

The order above is serialization determinism only. It does not rank one controlled source above another.

### 3.3 Duplicate-free rule remains unchanged

No expanded list contains the same exact serialized string more than once.

The fixture demonstrates the accepted form but does not create a validator. A later schema/validator RC may enforce the accepted rule; it shall not redefine it.

## 4. Fixture Population Changes

The fixture remains illustrative only and retains the same three record identities and applicability states:

```text
EXAMPLE-PA-001 -> applicable
EXAMPLE-PA-002 -> not_applicable
EXAMPLE-PA-003 -> undetermined
```

The fixture does not assert real applicability decisions for SCAF.

rc05 expands only illustrative reference populations. It does not change:

- `record_id`;
- `record_kind`;
- `representation_release`;
- `scaf_authority_id`;
- `scaf_source_release`;
- `project_scope_ref`;
- `applicability`;
- current-state basis semantics;
- Project Design Authority ownership;
- any frozen SCAF authority or L3 trace semantics.

## 5. Multi-Item Coverage Matrix

The rc05 fixture is expected to demonstrate at least the following coverage:

| Repeating reference surface | Multi-item coverage | Ordering requirement | Duplicate rule |
|---|---|---|---|
| `disposition_basis.basis_refs` | yes | exact serialized string ascending | no duplicate exact strings |
| `disposition_basis.awaiting_refs` | yes | exact serialized string ascending | no duplicate exact strings |
| `decision_refs` | yes | exact serialized string ascending | no duplicate exact strings |
| `authority_refs` | yes | exact serialized string ascending | no duplicate exact strings |
| `supporting_refs` | yes | exact serialized string ascending | no duplicate exact strings |

This is fixture coverage, not a new semantic dimension.

## 6. Representation Validity Versus Engineering Judgment

A later executable control may objectively determine whether a repeating list is sorted or contains an exact duplicate after the relevant representation contract is accepted. Such checks concern representation conformance only.

They do not authorize a tool to determine:

- whether the referenced engineering rationale is correct;
- whether the referenced decision was appropriate;
- whether the named authority is sufficient under project governance without an accepted authority-resolution contract;
- whether the obligation should be applicable or not applicable;
- whether an `undetermined` engineering question should be resolved in a particular way.

The core SCAF rule remains:

> **Machine-verifiable representation facts may be checked by tools; project engineering judgment remains project-governed and must retain explicit rationale/provenance where required.**

## 7. Negative Conditions Preserved

rc05 does not weaken any accepted rc04 negative condition. In particular, these remain representation/contract-invalid under the accepted contract when a later validator exists:

- duplicate exact reference inside one role-specific list;
- non-ascending repeating reference list;
- unsupported applicability token;
- `applicable` / `not_applicable` without direct basis through non-empty `summary` or `basis_refs`;
- using `decision_refs`, `authority_refs`, or `supporting_refs` alone to satisfy direct basis;
- `undetermined` without non-empty `unresolved_reason`;
- unresolved-only members on resolved states;
- missing `awaiting_refs` for `undetermined`;
- YAML duplicate mapping keys, anchors/aliases, merge keys, custom tags, or multi-document streams.

A structurally conformant `undetermined` record with a genuine open engineering question remains representation-valid in principle.

## 8. Frozen / Non-Target Boundaries

rc05 changes no frozen normative/L3 source and no frozen/existing executable-governance implementation surface. In particular, it does not modify:

```text
docs/normative/
docs/l3/
authority-registry.yaml
l3-trace-registry.yaml
schemas/
tools/scaf_validator/
tools/scaf_trace_validator/
tools/scaf_trace_views/
tools/scaf_release_integrity/
tools/scaf_external_pin/
tools/scaf_ci_gate/
.github/workflows/
release-integrity/
```

The accepted rc01-rc04 controlled records remain historical inputs and are not rewritten by rc05.

## 9. Explicit Non-Goals

rc05 does not introduce:

- JSON Schema or another formal Project Application schema;
- Project Application validator;
- project-scope registry/resolver;
- reference locator grammar/resolver;
- history/supersession/re-evaluation serialization;
- decision/deviation/risk/verification/evidence/closure lifecycle serialization;
- tailoring taxonomy;
- automatic applicability classification;
- AI approval of engineering rationale;
- Project Design Authority automation;
- Pattern recommendation/selection;
- Effective Project Profile generation;
- context resolver/packager;
- CI applicability-completion enforcement;
- code generation;
- new L3 Patterns;
- L4 guidance.

## 10. Review Gate

The rc05 gate should be `YES` only if independent review confirms all of the following:

1. `SCAF-RC04-001` is closed by meaningful multi-item fixture coverage;
2. all five canonical repeating reference roles have at least one multi-item fixture example;
3. each expanded list is visibly ordered by exact serialized string ascending;
4. no expanded list contains a duplicate exact string;
5. the fixture remains exactly three records covering the same three applicability states;
6. `representation_release` remains `v0.0.6rc04`, confirming that rc05 did not silently mint a new serialization contract;
7. no rc04 semantic or authority boundary is changed;
8. frozen validators/regressions/release-integrity remain unchanged and passing;
9. no schema, Project Application validator, resolver, inference, CI completion enforcement, or L4 capability is introduced.

If clean, rc05 may close the fixture-coverage finding and permit the next review-driven RC to consider a formal Project Application schema foundation.
