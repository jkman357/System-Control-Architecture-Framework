# SCAF v0.0.6rc06 — Project Application Schema Foundation

**Development Release:** v0.0.6rc06  
**Status:** Formal Schema Foundation / Review Candidate  
**Date:** 2026-08-18  
**Upstream Frozen Baselines:** v0.0.2 L1/L2; v0.0.3 L3; v0.0.4 Executable Governance; v0.0.5 L3 Machine-Readable Traceability  
**Accepted Development Basis:** v0.0.6rc04 Concrete Project Application Serialization Foundation; v0.0.6rc05 fixture-coverage closure  
**Immediate Predecessor:** v0.0.6rc05

## 1. Decision Purpose

The independent v0.0.6rc05 review returned a clean gate with zero findings and closed `SCAF-RC04-001`:

```text
Critical: 0
Major:    0
Minor:    0
Trivial:  0

SCAF-RC04-001: CLOSED

V0.0.6RC05 PROJECT APPLICATION SERIALIZATION FIXTURE COVERAGE HARDENING GATE: YES
```

The accepted v0.0.6 development chain now provides a reviewed semantic model, canonical logical record, basis/state hardening, concrete YAML representation, and concrete fixture coverage. rc06 takes the next bounded step: encode the machine-determinable structural and state-compatibility portion of the accepted rc04 representation contract as a formal JSON Schema.

The core boundary is unchanged:

> **Schema validity is representation conformance only. It is not a decision that the project applicability judgment, rationale, authority, design, verification, compliance, or closure is correct.**

## 2. Scope of rc06

rc06 adds exactly one new formal schema artifact:

```text
schemas/project-application.schema.json
```

The schema uses JSON Schema Draft 2020-12 and is intended to validate the parsed data model of the accepted YAML representation.

rc06 also updates navigation/release documentation to identify the new schema foundation.

rc06 does **not** add:

- a Project Application validator executable;
- a YAML loader policy implementation;
- a project-scope registry/resolver;
- a reference locator grammar/resolver;
- source-aware Project Application reconstruction;
- automatic applicability inference;
- AI approval of engineering rationale;
- Project Design Authority automation;
- Pattern recommendation or selection;
- history/supersession/re-evaluation serialization;
- tailoring taxonomy;
- Effective Project Profile generation;
- context packaging;
- CI applicability-completion enforcement;
- code generation;
- new L3 Pattern content;
- L4 guidance.

## 3. Schema Identity and Representation Release

The formal schema identity is:

```text
urn:scaf:schema:project-application:v0.0.6rc06
```

The schema targets the accepted representation contract:

```text
representation_release: v0.0.6rc04
```

This distinction is intentional:

```text
schema release          = v0.0.6rc06
representation contract = v0.0.6rc04
```

rc05 hardened fixture coverage only and did not create a new representation contract. rc06 formalizes that already-accepted rc04 contract; it does not silently rename or revise the serialized representation.

## 4. Schema-Enforced Representation Facts

The rc06 schema encodes the following machine-determinable facts.

### 4.1 Dataset shape

- root instance is an object/mapping;
- root contains exactly one member: `records`;
- `records` is an array;
- exact duplicate full record objects are rejected by `uniqueItems`.

The accepted rc04 `records` population remains zero or more records; rc06 does not invent a minimum project-completion population.

### 4.2 Canonical record field set

Every record requires exactly these eleven members and permits no additional member:

```text
record_id
record_kind
representation_release
scaf_authority_id
scaf_source_release
project_scope_ref
applicability
disposition_basis
decision_refs
authority_refs
supporting_refs
```

The schema enforces:

```text
record_kind:            project_application
representation_release: v0.0.6rc04
scaf_source_release:     v0.0.2
```

`record_id` and `project_scope_ref` remain opaque non-empty strings. rc06 does not invent a grammar for either.

`scaf_authority_id` remains an opaque non-empty string at the schema layer. rc06 deliberately does not invent an authority-ID grammar that the accepted rc04 serialization contract did not freeze. Actual existence and Project-Applicable-Obligation class resolution remain outside schema-only proof and are reserved for a later source-aware validator boundary.

### 4.3 Applicability vocabulary

The schema accepts exactly:

```text
applicable
not_applicable
undetermined
```

No alternative spelling or completion/verification token is introduced.

### 4.4 Repeating reference representation

`basis_refs`, `awaiting_refs`, `decision_refs`, `authority_refs`, and `supporting_refs`, where state-compatible, are arrays of non-empty opaque strings.

The schema uses `uniqueItems: true` to reject exact duplicate values within an individual role-specific list.

The schema does not infer a locator grammar, reference type, hierarchy, authority, existence, or substantive correctness from successful string validation.

### 4.5 Resolved-state direct-basis sufficiency

For `applicable` and `not_applicable`, the schema requires at least one structurally meaningful direct-basis surface:

```text
non-empty disposition_basis.summary
OR
non-empty disposition_basis.basis_refs
```

The schema does not allow `decision_refs`, `authority_refs`, or `supporting_refs` to substitute for direct applicability basis.

This is structural enforcement of the accepted rc03/rc04 contract; it is not a schema judgment that the supplied rationale is technically adequate or correct.

### 4.6 Current-state compatibility

For `applicable` and `not_applicable`:

- `unresolved_reason` is prohibited;
- `awaiting_refs` is prohibited.

For `undetermined`:

- `unresolved_reason` is required and non-empty;
- `awaiting_refs` is required and may be `[]`;
- `summary` remains optional/supplementary;
- `basis_refs` remains required and may be `[]`.

A structurally conformant `undetermined` record remains representation-valid even though the engineering question is unresolved.

### 4.7 Omission / null behavior after YAML parsing

All scalar values accepted by the schema are strings or exact constants/enums; list fields are arrays. A parsed YAML null therefore fails where a string/list is required.

State-prohibited members fail because the relevant state branch forbids their presence.

The schema therefore preserves the accepted distinction among:

```text
member omitted
empty list []
non-empty string/list
parsed null (invalid)
```

## 5. Facts Intentionally Not Claimed by Schema-Only Validation

JSON Schema applies to the parsed instance. Some accepted rc04 representation rules require either pre-parse YAML controls, cross-record logic, source-aware resolution, or engineering judgment. rc06 does not pretend otherwise.

### 5.1 Raw YAML / loader-boundary facts

The schema alone does not reliably prove raw-YAML properties that may disappear or normalize during parsing, including:

- duplicate YAML mapping keys;
- anchors / aliases;
- merge keys;
- custom tags;
- multi-document stream rejection;
- physical mapping-member order.

A later Project Application loader/validator boundary may enforce these accepted rules before/while parsing. rc06 does not add that executable boundary.

### 5.2 Canonical ordering

Standard JSON Schema Draft 2020-12 does not provide a portable keyword for exact serialized-string ascending order of array items or for record ordering by `record_id`.

Therefore rc06 does **not** claim that schema validation proves:

```text
records sorted by record_id
reference lists sorted by exact serialized string
```

Those accepted rc04 rules remain normative representation requirements and are reserved for later validator implementation.

`uniqueItems` enforcement is separate from ordering enforcement.

### 5.3 Cross-record identity uniqueness

`records.uniqueItems: true` rejects exact duplicate full record objects, but JSON Schema does not portably express uniqueness of a selected property across an arbitrary array.

Therefore schema-only validation does not prove:

- unique `record_id` across different record objects;
- absence of two different records asserting the same active `scaf_authority_id` / `project_scope_ref` pair.

Those accepted record-model constraints remain for a later validator.

### 5.4 Framework authority resolution

The schema checks only that `scaf_authority_id` is a non-empty string and does not prove that the ID:

- exists in `authority-registry.yaml`;
- belongs to the frozen `v0.0.2` source population;
- has authority class `Project-Applicable Obligation`.

A later source-aware validator must resolve those facts against the frozen authority representation rather than duplicating the 218-ID authority population into this schema.

### 5.5 Reference and project-scope resolution

Opaque reference strings are intentionally not resolved by the rc06 schema. Successful schema validation does not prove that a scope/reference target exists, is authoritative, is current, or is sufficient.

### 5.6 Engineering judgment

Schema validation shall never be interpreted as proof that:

- an applicability disposition is substantively correct;
- a `summary` is good engineering rationale;
- a `basis_refs` target actually supports the stated judgment;
- an `authority_refs` target has sufficient project authority;
- a project is compliant, verified, complete, or closed;
- a Pattern should be selected or has been implemented.

## 6. Schema Composition Strategy

The schema deliberately separates reusable structural definitions:

```text
nonEmptyString
referenceList
dispositionBasis
resolvedDispositionBasis
undeterminedDispositionBasis
projectApplicationRecord
```

State-dependent behavior is encoded with standard Draft 2020-12 `if` / `then` constraints rather than custom keywords.

No SCAF-specific executable keyword is introduced in rc06. This keeps the formal schema portable and prevents a custom keyword from silently becoming a second semantic authority.

## 7. Negative-Condition Contract

The rc06 schema is expected to reject, at minimum, parsed instances containing:

1. a top-level member other than/in addition to `records`;
2. a missing canonical record field;
3. an additional unknown record field;
4. an unsupported applicability token;
5. a wrong `record_kind`;
6. a wrong `representation_release`;
7. a wrong `scaf_source_release`;
8. a null/empty required scalar where non-empty string is required;
9. a non-array reference-list field;
10. an exact duplicate value within one role-specific reference list;
11. `applicable` with neither `summary` nor a non-empty `basis_refs`;
12. `not_applicable` with neither `summary` nor a non-empty `basis_refs`;
13. `applicable` or `not_applicable` containing `unresolved_reason`;
14. `applicable` or `not_applicable` containing `awaiting_refs` even when `[]`;
15. `undetermined` without `unresolved_reason`;
16. `undetermined` without `awaiting_refs`;
17. `undetermined` with `unresolved_reason: null` or empty string.

The schema is also expected to accept the rc05-hardened illustrative fixture after normal YAML parsing.

The following are **not** claimed as schema-only reject conditions in rc06 because they require a later loader/validator or source-aware boundary:

- unsorted record/reference arrays;
- two non-identical records sharing the same `record_id`;
- two non-identical records sharing the same active authority/scope pair;
- syntactically well-formed but nonexistent `scaf_authority_id`;
- unresolved/nonexistent project-controlled opaque references;
- raw YAML aliases/merge keys/duplicate keys after a permissive parser has already normalized them.

## 8. Invalid Versus Unresolved

The schema formalizes representation-invalid state combinations but does not convert legitimate engineering uncertainty into failure.

For example, this remains valid in principle:

```yaml
applicability: "undetermined"
disposition_basis:
  basis_refs: []
  unresolved_reason: "Interface ownership is not yet assigned."
  awaiting_refs:
    - "project:decision:interface-owner"
```

Schema-valid `undetermined` means the unresolved engineering state is represented consistently. It does not mean the engineering question is resolved, approved, verified, or acceptable indefinitely.

## 9. Authority Separation

The following boundaries remain unchanged:

```text
authority-registry.yaml             = frozen framework authority representation
l3-trace-registry.yaml              = frozen L2↔L3 trace representation
project-application.schema.json     = Project Application structural/state schema
Project Application YAML            = project-side disposition/provenance representation
future validator                     = representation/source-aware conformance checker only
project governance / PDA             = owner of engineering judgment where applicable
```

The schema is subordinate to the accepted SCAF-APP semantics and rc04 serialization contract. It does not become engineering decision authority.

## 10. Frozen / Non-Target Preservation

rc06 shall not change the frozen:

- v0.0.2 normative source;
- v0.0.3 L3 Pattern source;
- `authority-registry.yaml`;
- `l3-trace-registry.yaml`;
- frozen authority schema;
- frozen L3 trace schema;
- authority validator;
- trace validator;
- trace views/query API;
- release-integrity checker/manifest;
- external-pin checker/input model;
- CI gate/workflow;
- accepted regression behavior.

The rc05 fixture remains unchanged in rc06.

## 11. Review Gate

An independent rc06 review shall determine whether:

1. the schema is valid JSON Schema Draft 2020-12;
2. the rc05-hardened fixture validates successfully after normal YAML parsing;
3. schema constants/tokens/required fields exactly match the accepted rc04 contract;
4. direct-basis structural sufficiency is encoded without allowing top-level reference roles to substitute;
5. state-dependent member presence/prohibition exactly matches rc03/rc04;
6. null/empty/list constraints preserve accepted omission rules;
7. exact duplicate values within one reference list are rejected;
8. schema limitations are explicit and no unsupported ordering/cross-record/source-resolution claim is made;
9. `undetermined` remains representation-valid when structurally conformant;
10. no engineering authority is transferred to schema validity;
11. no validator/resolver/inference/CI/L4 capability is introduced;
12. frozen/non-target sources and regressions remain unchanged.

Only after this schema foundation passes review should a later RC consider a Project Application validator boundary.
