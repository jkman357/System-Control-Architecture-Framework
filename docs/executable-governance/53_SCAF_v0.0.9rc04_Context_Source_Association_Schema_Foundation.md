# SCAF v0.0.9rc04 — Context Source Association Schema Foundation

**Development Release:** v0.0.9rc04  
**Status:** Context Source Association Schema Foundation / Review Candidate  
**Date:** 2026-08-19  
**Immediate Predecessor:** accepted v0.0.9rc03 (`bd08e8618101dd29ed50933b166cb424adb7c0f6`)  
**Frozen Basis:** v0.0.2 L1/L2; v0.0.3 L3; v0.0.4 Executable Governance; v0.0.5 L3 Machine-Readable Traceability; v0.0.6 Project Application / Effective Project Profile; v0.0.7 Consumption Selection; v0.0.8 Lifecycle-Proportional Governance

## 1. Decision Purpose

The accepted rc03 representation established one deterministic YAML serialization for the accepted rc02 Context Source Association logical model. Its independent review returned `PASS / GATE YES` with zero findings and zero open blocking review-evidence limitations.

The post-rc03 dependency/value assessment identified one material next-step dependency: before any source-aware validator is introduced, the repository needs one machine-checkable structural contract for the parsed rc03 representation. Otherwise each validator implementation could independently hard-code field shapes, token vocabularies and nested-object rules.

The Current Decision Horizon for rc04 is therefore:

> **Define the JSON Schema Draft 2020-12 parsed-instance structural contract for the accepted v0.0.9rc03 Context Source Association representation, while keeping source-aware proof and engineering judgment outside schema authority.**

rc04 adds no production validator, resolver, runtime-resolution representation, content loader, ranking/token-budget policy, Context Assembly, CI gate, authority-registry change, new PAO/FNI, or L4 guidance.

## 2. Engineering Problem

A canonical YAML artifact without a repository-owned structural schema still leaves avoidable implementation divergence around questions such as:

```text
Which members are required?
Which members are optional?
Are unknown members permitted?
What are the allowed relationship/control/provenance tokens?
What exact nested shape does Authority Qualification use?
What exact shape does an Instance Constraint use?
What counts as syntactically valid SHA-256 text?
Can association lists be empty?
```

These are machine-determinable representation facts and should not be reimplemented differently by each future validator.

At the same time, schema must not overclaim source-aware or engineering truth that it cannot prove.

Therefore rc04 deliberately establishes:

```text
parsed-instance structural validity
!= source-aware consistency
!= engineering correctness
```

## 3. Canonical Schema Artifact

rc04 adds:

```text
schemas/context-source-associations.schema.json
```

Schema identity:

```text
$schema = https://json-schema.org/draft/2020-12/schema
$id     = urn:scaf:schema:context-source-associations:v0.0.9rc04
```

The schema validates the accepted rc03 representation identity:

```text
association_set_kind = context_source_association_set
representation_release = v0.0.9rc03
```

The schema release and representation release remain distinct:

```text
representation release: v0.0.9rc03
schema foundation:      v0.0.9rc04
```

rc04 does not create a new representation release.

## 4. Structural Ownership

The schema owns only parsed-instance structure that is determinable from one parsed representation without consulting repository/source truth.

It therefore owns, as applicable:

```text
required top-level members
required/optional nested members
mapping/array/string types
additionalProperties policy
non-empty string shape
bounded enum/const tokens
lowercase 64-hex SHA-256 syntax
minimum non-empty provenance/authority-basis lists
structural array uniqueness where JSON Schema uniqueItems can prove exact-value uniqueness
```

Every modeled object uses `additionalProperties: false` so the accepted representation contract cannot silently absorb unrelated fields, including runtime-resolution/currentness fields.

## 5. Canonical Top-Level Shape

The accepted parsed top-level shape remains exactly:

```text
association_set_kind
representation_release
source_selection_binding
source_units
authority_source_entries
```

All five members are required. Unknown top-level members are invalid under the rc04 schema.

The schema does not prove physical YAML field order. Canonical physical ordering remains a later source-aware/raw-representation validation responsibility if such a validator is justified.

## 6. Source Selection Binding Shape

`source_selection_binding` structurally requires exactly:

```text
consumption_selection_source_sha256
selection_kind
selection_representation_release
project_scope_ref
```

with:

```text
consumption_selection_source_sha256 = lowercase 64-hex text
selection_kind = consumption_selection
selection_representation_release = v0.0.7rc03
project_scope_ref = non-empty opaque string
```

Schema success does **not** prove that the SHA matches the bytes of the intended Consumption Selection, that the bound selection passed accepted source-aware validation, or that the recorded scope matches that selection. Those are future source-aware responsibilities.

## 7. Source Unit Shape

Each `source_units` item structurally contains exactly:

```text
source_unit_id
source_identity_ref
control_domain
```

All are required. `source_unit_id` and `source_identity_ref` are non-empty strings.

`control_domain` is limited to:

```text
framework
project
external
```

The schema does not define resolver semantics for `source_identity_ref`, prove that an identity exists, or confer authority/applicability from `control_domain`.

## 8. Authority Source Entry Shape

Each `authority_source_entries` item structurally contains exactly:

```text
scaf_authority_id
associations
```

Both are required. `scaf_authority_id` is a non-empty string and `associations` is an array that may legitimately be empty.

This structural allowance preserves the accepted rc03 representation of explicit zero associations.

Schema validation alone cannot prove:

```text
authority_source_entries domain == validated I
exactly one entry per authority identity
no authority outside I
missing entry != explicit zero association
```

Those require source-aware comparison to the exact validated Consumption Selection.

## 9. Controlled Source Association Shape

Each association structurally requires:

```text
source_unit_ref
relationship_semantic
relationship_scope_ref
association_provenance
```

and permits only these optional members:

```text
authority_qualification
instance_constraint
```

`source_unit_ref` and `relationship_scope_ref` are non-empty strings.

The initial accepted `relationship_semantic` vocabulary is exactly:

```text
framework_obligation_source
project_decision_source
realization_source
verification_definition_source
verification_evidence_source
external_constraint_source
supporting_context_source
```

Schema success does not prove that `source_unit_ref` names a catalog member, that the relationship is correct, that its scope is semantically appropriate, or that the association is unique under the rc03 semantic tuple.

## 10. Association Provenance Shape

`association_provenance` structurally requires exactly:

```text
assertion_kind
basis_refs
```

`assertion_kind` is limited to:

```text
framework_declared
project_declared
controlled_rule_derived
```

`basis_refs` must contain at least one non-empty string and uses JSON Schema `uniqueItems: true` for exact-value duplication.

The schema does not prove that a basis reference exists, is current, or legitimately authorizes the relationship assertion.

The accepted boundary remains:

```text
discovered candidate != controlled association
```

No discovered-candidate assertion token is introduced by rc04.

## 11. Authority Qualification Shape

When present, `authority_qualification` structurally requires exactly:

```text
qualification_kind
authority_scope_ref
authority_basis_refs
```

with:

```text
qualification_kind = authoritative_for_relationship_scope
authority_scope_ref = non-empty string
authority_basis_refs = non-empty exact-value-unique string list
```

The schema deliberately does not provide a file-global `authoritative: true` field.

Schema validity does not prove that the qualification is legitimate or that the referenced source becomes authoritative beyond the recorded bounded relationship scope.

## 12. Instance Constraint Shape

When present, `instance_constraint` structurally requires exactly:

```text
constraint_kind
value
```

with:

```text
constraint_kind = sha256
value = 64 lowercase hexadecimal characters
```

This validates syntax only.

It does not prove:

```text
recorded SHA == referenced source bytes
source can currently be resolved
source is current
resolver observed a matching instance
```

The accepted separation remains:

```text
Source Identity
!= expected/pinned Instance Constraint
!= actual runtime-resolved Source Instance
```

## 13. Two-Plane Invariant Preservation

The rc04 schema contains no runtime-resolution/currentness state model.

It therefore does not authorize fields such as:

```text
resolution_status
resolved_instance
resolved_sha256
missing
unresolvable
stale
superseded
currentness
constraint_match
resolver_timestamp
```

Because modeled objects reject additional properties, insertion of such fields into the controlled-association parsed structure is structurally invalid unless a future separately reviewed representation changes the contract.

The governing invariant remains:

```text
controlled association truth
!= runtime resolution observation
```

## 14. What JSON Schema Deliberately Cannot Prove

The rc04 schema shall not be represented as proving any of the following:

```text
exact bound Consumption Selection bytes
accepted source-aware validation of that selection
validated-I reconstruction or complete I coverage
Source Unit ID/reference integrity across arrays
unused Source Unit absence
semantic association uniqueness
canonical physical YAML ordering
basis-reference existence/authority
property-specific engineering authority correctness
instance-constraint source-byte correspondence
source resolvability
source currentness/staleness/supersession
applicability
obligation satisfaction
implementation correctness
verification result/sufficiency
compliance
risk acceptance
release readiness
closure
Context Assembly inclusion
```

These require later source-aware executable logic and/or existing engineering authority and judgment.

This non-ownership list is part of the rc04 contract, not an implementation gap to be hidden inside schema tricks.

## 15. Invalid-Condition Boundary

At the rc04 Current Decision Horizon, structurally invalid examples include:

```text
unknown top-level or nested member
missing required member
wrong primitive/container type
unknown control_domain token
unknown relationship_semantic token
unknown association assertion token
empty required basis list
unknown authority qualification token
unknown instance constraint token
non-lowercase/non-64-hex SHA text
runtime-resolution field inserted into a controlled-association object
```

These are deterministic representation failures suitable for schema validation.

By contrast, a structurally valid representation can still be source-inconsistent or engineering-invalid. That distinction is intentional.

## 16. Current Decision Horizon Completion

rc04 is progression-sufficient when:

```text
1. the accepted rc03 parsed shape has one repository-owned Draft 2020-12 schema;
2. required/optional members and nested objects are closed with additionalProperties: false;
3. accepted rc03 token vocabularies are structurally encoded;
4. SHA-256 text syntax is bounded;
5. the accepted rc03 fixture validates against the schema;
6. bounded negative structural cases fail as intended;
7. the schema explicitly does not claim source-aware/engineering proof;
8. frozen upstream authority/representation/executable surfaces remain unchanged.
```

Progression Sufficiency does not require a production source-aware validator or resolver in this RC.

## 17. Deliberately Deferred Scope

rc04 does not add or authorize:

```text
production Context Source Association validator
raw-YAML canonical-order validator
source-aware Consumption Selection binding proof
validated-I reconstruction/coverage proof
Source Unit reference-integrity proof
semantic association uniqueness proof
source-byte Instance Constraint proof
filesystem/Git/URI resolver
runtime Resolution Observation representation
currentness/staleness policy
content extraction / loading / chunking
ranking / priority / token-budget policy
AI Context Assembly / prompting / orchestration
CI source-mapping gate
authority-registry promotion or new PAO/FNI
scope resolver / hierarchy / wildcard / inference
L4 implementation / verification guidance
```

Each remains subject to a later dependency/value decision.

## 18. External Pattern / Licensing Boundary

This rc04 schema and controlled record are independently authored SCAF artifacts based on the accepted internal rc03 representation contract.

No third-party code, prompt, schema, documentation text, example content, or implementation is directly incorporated by this RC. External projects may continue to be studied for design patterns, but direct incorporation requires separate license/copyright/attribution/NOTICE/trademark review before inclusion.

## 19. Verification Breadth

Because rc04 adds one schema and one controlled record plus navigation/history updates, with no change to frozen executable code or prior accepted representations, proportional verification is bounded to:

```text
schema meta-validation
accepted rc03 fixture -> schema PASS
bounded invalid structural cases -> schema FAIL
exact source delta / protected-surface check
repository-owned production validators/integrity checks
```

The historical 262-test inventory is not required solely for ritual completeness unless an unexpected executable/representation change is discovered.

## 20. Progression Rule

A clean rc04 review authorizes only a new dependency/value assessment.

It does not automatically authorize:

```text
rc05
production validator
resolver
runtime-observation representation
Context Assembly
CI enforcement
L4
```

The next development step must again demonstrate a material dependency under the frozen v0.0.8 proportional-governance rule.
