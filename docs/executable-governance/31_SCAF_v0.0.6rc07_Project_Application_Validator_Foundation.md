# SCAF v0.0.6rc07 — Project Application Validator Foundation

**Development Release:** v0.0.6rc07  
**Status:** Source-Aware Representation Validator Foundation / Review Candidate  
**Date:** 2026-08-18  
**Upstream Frozen Baselines:** v0.0.2 L1/L2; v0.0.3 L3; v0.0.4 Executable Governance; v0.0.5 L3 Machine-Readable Traceability  
**Accepted Development Basis:** v0.0.6rc04 Project Application representation; v0.0.6rc05 fixture coverage; v0.0.6rc06 JSON Schema foundation  
**Immediate Predecessor:** v0.0.6rc06

## 1. Decision Purpose

The independent v0.0.6rc06 review returned a clean gate with zero findings:

```text
Critical: 0
Major:    0
Minor:    0
Trivial:  0

V0.0.6RC06 PROJECT APPLICATION SCHEMA FOUNDATION GATE: YES
```

The rc06 review confirmed that the JSON Schema faithfully encodes the accepted parsed-instance structure while correctly leaving several machine-determinable concerns outside schema-only proof:

- raw YAML duplicate-key / anchor / alias / merge / custom-tag / multi-document policy;
- deterministic record/reference-list ordering;
- cross-record `record_id` uniqueness;
- active `(scaf_authority_id, project_scope_ref)` uniqueness;
- frozen SCAF authority existence/class resolution;
- project-controlled reference existence;
- engineering rationale correctness and project authority sufficiency.

rc07 adds the first Project Application validator boundary. It closes only the machine-determinable representation/source-resolution portion that is ready to automate without converting project engineering judgment into tool authority.

The governing rule is:

> **The rc07 validator may determine representation conformance and frozen SCAF target identity facts. It shall not determine whether the project's engineering judgment is substantively correct.**

## 2. Scope of rc07

rc07 adds:

```text
tools/scaf_project_application_validator/
```

The validator performs this controlled pipeline:

```text
Project Application YAML
        ↓
raw-YAML policy validation
        ↓
strict safe load
        ↓
rc06 JSON Schema validation
        ↓
cross-record identity validation
        ↓
deterministic collection ordering validation
        ↓
frozen authority-registry source proof
        ↓
scaf_authority_id target resolution
```

rc07 does **not** add:

- a project-scope registry or scope resolver;
- a project reference locator grammar/resolver;
- project decision/reference content reconstruction;
- automatic applicability inference;
- AI approval of engineering rationale;
- Project Design Authority automation;
- Pattern recommendation or selection;
- implementation/satisfaction/compliance determination;
- verification/evidence/closure determination;
- history/supersession/re-evaluation serialization;
- tailoring taxonomy;
- Effective Project Profile generation;
- context packaging;
- CI applicability-completion enforcement;
- code generation;
- new L3 Pattern content;
- L4 guidance.

## 3. Production CLI Authority Boundary

The production CLI is:

```text
python -m tools.scaf_project_application_validator.validator
```

By default it validates:

```text
examples/project-application.yaml
```

A caller may select another Project Application dataset:

```text
python -m tools.scaf_project_application_validator.validator \
  --project-application <path>
```

The caller cannot select:

- a different SCAF repository root;
- a different Project Application schema;
- a different authority registry;
- a different authority-registry schema.

Those contract inputs remain owned by the repository containing the validator.

The function-level API accepts a repository root so isolated regression tests can construct controlled repositories. That testability surface does not create a production CLI override.

## 4. Raw YAML Policy

rc04 already prohibited YAML representation features that can obscure the accepted logical contract. rc07 makes those machine-determinable loader-boundary rules executable before parsed-instance schema validation.

The validator rejects:

```text
duplicate mapping keys
YAML anchors
YAML aliases
YAML merge keys
custom YAML tags
multi-document streams
non-string mapping keys
```

The loader is based on `yaml.SafeLoader` with a strict mapping constructor. It does not enable arbitrary object construction.

Comments remain permitted and non-authoritative.

Schema/state rules continue to reject null values where the accepted contract requires non-empty strings or arrays.

## 5. Schema Chaining

After raw-YAML policy validation and strict safe loading, the validator applies:

```text
schemas/project-application.schema.json
```

using JSON Schema Draft 2020-12.

The rc06 schema remains authoritative for machine-determinable parsed-instance facts in its accepted scope. rc07 does not duplicate or redefine those rules in independent validator logic merely because an executable now exists.

Examples of schema-owned facts include:

- exact top-level shape;
- exact eleven record fields;
- `record_kind` / `representation_release` / `scaf_source_release` constants;
- applicability token vocabulary;
- non-empty string/list typing;
- resolved-state direct-basis structural sufficiency;
- `undetermined` member compatibility;
- exact duplicate rejection within one role-specific reference list.

If schema validation fails, later cross-record/source-aware checks do not convert the malformed representation into an engineering-state diagnosis.

## 6. Cross-Record Identity Rules

### 6.1 `record_id` uniqueness

Each `record_id` shall occur exactly once in one validated Project Application dataset.

This closes the rc06 schema limitation in which two non-identical complete record objects could share the same `record_id` while remaining schema-valid.

### 6.2 Active authority/scope uniqueness

The accepted canonical model prohibits ambiguous duplicate applicability assertions for the same target/scope pair.

For the current-state rc04 representation, the validator therefore requires each pair below to occur at most once:

```text
(scaf_authority_id, project_scope_ref)
```

rc07 has no history/supersession model. It therefore does not attempt to interpret multiple historical records as current versus superseded. Such lifecycle semantics remain separately gated.

## 7. Deterministic Collection Ordering

The validator enforces the accepted rc04 deterministic collection rules:

```text
records
  -> exact record_id ascending

basis_refs
awaiting_refs
decision_refs
authority_refs
supporting_refs
  -> exact serialized string ascending
```

Ordering is representation determinism only.

It does not mean:

- engineering priority;
- authority priority;
- review priority;
- preferred Pattern/mechanism;
- decision sequence.

Exact duplicate strings within one reference list remain rejected by the rc06 schema `uniqueItems` rule; rc07 ordering validation does not redefine that rule.

The rc04 mapping-order guidance for controlled generators/fixtures remains documentation/generation guidance in rc07. rc07 does not promote physical mapping-member order into a new universal project-input validity rule without a separately reviewed decision.

## 8. Frozen Authority-Registry Proof

Before a Project Application record's `scaf_authority_id` is accepted as resolved, rc07 invokes the existing frozen authority-registry validator against the same repository root.

This establishes that Project Application target resolution is not performed against an unvalidated or caller-substituted authority registry.

The existing frozen authority-registry validator remains unchanged.

If that proof fails, rc07 reports representation/source-validation failure and does not claim target resolution.

## 9. `scaf_authority_id` Source-Aware Resolution

For each schema-valid Project Application record, rc07 checks that `scaf_authority_id`:

1. exists in the validated frozen `authority-registry.yaml`;
2. resolves to:

```text
authority_class: Project-Applicable Obligation
```

3. has `source_release` equal to the record's accepted `scaf_source_release`.

This means the validator may reject:

- a nonexistent SCAF authority ID;
- a Framework Normative Invariant used as a Project Application target;
- a source-release mismatch if such an instance reaches source-aware validation under a future compatible schema revision.

This is target identity/class/provenance validation only.

It does not determine whether the obligation is actually applicable to the declared project scope.

## 10. Project-Controlled References Remain Opaque

rc07 deliberately does not resolve:

```text
project_scope_ref
basis_refs
awaiting_refs
decision_refs
authority_refs
supporting_refs
```

Their accepted representation remains opaque non-empty strings.

The validator may check their structural list representation and canonical ordering, but it does not infer from the textual form that:

- a target exists;
- a target is current;
- a target belongs to a particular artifact kind;
- an authority reference actually approves the judgment;
- a basis reference is technically sufficient;
- a decision reference constitutes direct basis;
- a supporting reference proves implementation or verification.

A project-scope/reference resolution model remains a future separately reviewed concern.

## 11. Invalid Versus Unresolved

The existing distinction remains unchanged:

```text
representation invalidity
!=
engineering-unresolved state
```

Examples of representation-invalid conditions include:

- prohibited YAML representation features;
- schema-invalid field/state structure;
- duplicate current record identity;
- duplicate current authority/scope pair;
- non-canonical accepted collection ordering;
- unresolved or wrong-class SCAF authority target.

A conformant record with:

```text
applicability: undetermined
```

and the accepted required unresolved-state members remains representation-valid even though the engineering question remains open.

The validator shall not convert `undetermined` into project failure, non-compliance, verification failure, or closure failure.

## 12. PASS Meaning

The CLI intentionally reports:

```text
REPRESENTATION RESULT: PASS
```

rather than a project-level compliance/approval statement.

PASS means only that the checked Project Application representation:

- passed the accepted YAML loader policy;
- passed the accepted rc06 schema;
- satisfied accepted cross-record identity constraints;
- satisfied accepted collection ordering rules;
- resolved every SCAF authority target against a validated frozen authority registry with the accepted target class/provenance.

PASS does **not** mean:

- applicability is correct;
- rationale is sufficient;
- Project Design Authority approved the record;
- a project-controlled reference exists;
- implementation is complete;
- verification/evidence is sufficient;
- compliance is achieved;
- closure is achieved;
- a Pattern is selected or recommended.

## 13. Regression Contract

The rc07 test suite shall cover at least:

- accepted repository fixture PASS;
- duplicate raw YAML key rejection;
- anchor rejection;
- alias rejection;
- merge-key rejection;
- custom-tag rejection;
- multi-document rejection;
- non-string key rejection;
- schema chaining / invalid applicability rejection;
- duplicate `record_id` rejection;
- duplicate `(scaf_authority_id, project_scope_ref)` rejection;
- non-canonical record ordering rejection;
- non-canonical ordering for each of the five canonical repeating reference roles;
- nonexistent SCAF authority rejection;
- Framework Normative Invariant target rejection.

The existing frozen regression suites remain unchanged.

## 14. Preserved Frozen Boundaries

rc07 changes no:

- frozen v0.0.2 normative source;
- frozen v0.0.3 L3 source;
- frozen authority registry;
- frozen L3 trace registry;
- frozen authority/L3 trace schemas;
- frozen authority validator;
- frozen L3 trace validator;
- frozen trace views/query implementation;
- frozen release-integrity data/tooling;
- frozen external-pin/CI gate/workflow trust model;
- accepted rc04 Project Application fixture;
- accepted rc06 Project Application schema.

The validator is new v0.0.6 development capability layered above those accepted/frozen inputs.

## 15. Explicitly Deferred

A future RC may separately review one or more of:

- project-scope identity model;
- controlled project reference grammar/resolution;
- validator diagnostics/API hardening;
- deterministic Project Application read/query views;
- Effective Project Profile construction;
- AI context assembly;
- selective CI integration.

No such future capability is authorized merely because rc07 exists.

## 16. Review Gate

rc07 may advance only if independent review confirms that:

1. the validator correctly chains raw-YAML policy, rc06 schema, cross-record checks, ordering checks, validated-authority proof, and target resolution;
2. the accepted fixture passes without modifying rc04/rc05/rc06 artifacts;
3. bounded invalid-condition cases are rejected deterministically;
4. `undetermined` remains legitimate representation of unresolved engineering work;
5. project-controlled references remain opaque/unresolved;
6. Project Design Authority and engineering judgment remain outside tool authority;
7. frozen regressions/integrity remain unchanged and passing;
8. no resolver/inference/Pattern/CI/L4 expansion is introduced.
