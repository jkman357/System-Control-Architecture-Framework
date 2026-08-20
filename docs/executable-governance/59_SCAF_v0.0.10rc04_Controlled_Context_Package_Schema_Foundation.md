# SCAF v0.0.10rc04 — Controlled Context Package Schema Foundation

**Development Release:** v0.0.10rc04  
**Status:** Controlled Context Package Schema Foundation / Review Candidate  
**Date:** 2026-08-20  
**Immediate Predecessor:** accepted v0.0.10rc03 (`7296c66614cf140dc5b8ca841352c376e557ed3e`)  
**Frozen Basis:** v0.0.2 L1/L2; v0.0.3 L3; v0.0.4 Executable Governance; v0.0.5 L3 Machine-Readable Traceability; v0.0.6 Project Application / Effective Project Profile; v0.0.7 Consumption Selection; v0.0.8 Lifecycle-Proportional Governance; v0.0.9 Context Source Association / Source-Aware Validation

## 1. Decision Purpose

The accepted v0.0.10 chain now contains:

```text
rc01  Controlled Context Assembly semantic foundation
  ↓
rc02  canonical representation-neutral Controlled Context Package logical model
  ↓
rc03  canonical deterministic Controlled Context Package YAML representation
```

The rc03 independent review returned clean `PASS / GATE YES` with zero candidate-source findings and zero blocking review-evidence limitations.

The post-rc03 dependency/value assessment identified one material next-step dependency: the accepted package representation is now concrete enough that future validators/builders should not independently hard-code different object shapes, required/optional members, token vocabularies, branch rules, or SHA syntax.

The Current Decision Horizon for rc04 is therefore:

> **Define one repository-owned JSON Schema Draft 2020-12 structural contract for the accepted v0.0.10rc03 Controlled Context Package parsed representation, without claiming source-aware package consistency, engineering-context sufficiency, construction behavior, source loading, or AI/model integration.**

## 2. Engineering Problem

Without rc04, a package could parse as YAML but still use materially incompatible structural forms such as:

```text
wrong package kind or representation release
missing required top-level members
unexpected members that silently invent runtime/model semantics
invalid upstream-binding object shapes
malformed SHA-256 values
unknown materialization outcomes
materialized decisions with zero item references
not-materialized decisions carrying item references
not-materialized decisions lacking an explicit basis
unknown context semantic values
unknown payload kinds
missing controlled provenance bases
malformed projected Controlled Source Association objects
```

Those are machine-determinable representation facts and should have one repository-owned contract.

## 3. Governing Separation

rc04 preserves the accepted layered boundary:

```text
package representation
!= parsed-instance structural validity
!= source-aware package consistency
!= engineering-context sufficiency
```

The new schema owns only the parsed-instance structural layer.

It does not promote a structurally valid package into a source-consistent or engineering-sufficient package.

## 4. Production Schema Artifact

rc04 adds:

```text
schemas/controlled-context-package.schema.json
```

Schema dialect:

```text
https://json-schema.org/draft/2020-12/schema
```

Schema identity:

```text
urn:scaf:schema:controlled-context-package:v0.0.10rc04
```

The schema validates the accepted rc03 representation release:

```text
representation_release = v0.0.10rc03
```

This distinction is intentional:

```text
representation release = v0.0.10rc03
schema release         = v0.0.10rc04
```

rc04 does not invent a new package representation release.

## 5. Schema-Owned Structural Contract

The schema owns the following parsed-instance facts.

### 5.1 Top-level package identity and shape

Required exact top-level members:

```text
package_kind
representation_release
upstream_binding
assembly_objective
authority_context_entries
materialized_context_items
```

Accepted constants:

```text
package_kind           = controlled_context_package
representation_release = v0.0.10rc03
```

Unknown top-level members are structurally invalid through `additionalProperties: false`.

### 5.2 Exact upstream-binding object shapes

`upstream_binding` has exactly:

```text
consumption_selection
context_source_association_set
```

Consumption Selection binding shape:

```text
source_sha256
selection_kind
representation_release
project_scope_ref
```

with:

```text
selection_kind          = consumption_selection
representation_release  = v0.0.7rc03
source_sha256            = lowercase 64-hex SHA-256 syntax
project_scope_ref        = non-empty string
```

Context Source Association Set binding shape:

```text
source_sha256
association_set_kind
representation_release
consumption_selection_source_sha256
project_scope_ref
```

with:

```text
association_set_kind     = context_source_association_set
representation_release   = v0.0.9rc03
SHA fields               = lowercase 64-hex SHA-256 syntax
project_scope_ref        = non-empty string
```

The schema does not prove that any recorded SHA equals actual source bytes.

### 5.3 Assembly Objective shape

Exactly:

```text
objective_id
objective_statement
```

Both are non-empty strings.

The schema does not decide whether the objective is a good, sufficient, authorized, or correctly scoped engineering objective.

### 5.4 Authority Context Entry shape

Each entry requires:

```text
scaf_authority_id
association_envelope
materialization_decisions
```

`association_envelope` and `materialization_decisions` are arrays and may be empty.

This structurally preserves the accepted explicit zero-association form.

The schema does not prove:

```text
one entry exists for every authority in validated I
no authority outside validated I is present
authority IDs are unique across entries
```

Those are source-aware/package-consistency responsibilities.

### 5.5 Association Envelope Entry shape

Each envelope entry requires:

```text
association_handle
controlled_association
```

`association_handle` is a non-empty string.

The schema does not promote it into an upstream association identity and does not prove package-wide uniqueness or reference resolution.

### 5.6 Controlled Source Association projection shape

The schema structurally preserves the accepted v0.0.9 association shape:

Required:

```text
source_unit_ref
relationship_semantic
relationship_scope_ref
association_provenance
```

Optional:

```text
authority_qualification
instance_constraint
```

Accepted `relationship_semantic` vocabulary:

```text
framework_obligation_source
project_decision_source
realization_source
verification_definition_source
verification_evidence_source
external_constraint_source
supporting_context_source
```

Accepted association provenance assertion kinds:

```text
framework_declared
project_declared
controlled_rule_derived
```

`basis_refs` and `authority_basis_refs` are non-empty arrays of non-empty strings with structural duplicate rejection through `uniqueItems: true`.

Authority Qualification remains bounded to:

```text
qualification_kind = authoritative_for_relationship_scope
```

Instance Constraint remains bounded to:

```text
constraint_kind = sha256
value           = lowercase 64-hex SHA-256 syntax
```

The schema does not prove that the projected association equals one accepted upstream association body.

### 5.7 Materialization Decision discriminated shapes

The accepted outcome vocabulary is exactly:

```text
materialized
not_materialized
```

The schema uses two non-overlapping structural branches.

#### Materialized

Required exact shape:

```text
association_handle
outcome = materialized
materialized_context_item_refs
```

`materialized_context_item_refs` must contain at least one non-empty string.

`non_materialization_basis` is not accepted in this branch.

#### Not materialized

Required exact shape:

```text
association_handle
outcome = not_materialized
materialized_context_item_refs = []
non_materialization_basis
```

`non_materialization_basis` must be a non-empty string.

This structurally preserves:

```text
materialized
!= not_materialized
```

and prevents the two outcome shapes from collapsing into one ambiguous object form.

The schema does not interpret `not_materialized` as applicability, source invalidity, v0.0.7 bounded omission `O`, waiver, risk acceptance, release state, or closure.

### 5.8 Materialized Context Item shape

Each item requires:

```text
materialized_context_item_id
context_semantic
controlled_provenance_bases
payload
```

Accepted `context_semantic` vocabulary:

```text
source_preserving
derived
```

Every parsed item must structurally contain at least one Controlled Provenance Basis.

The schema does not make derived context authoritative.

### 5.9 Controlled Provenance Basis shape

Each basis is exactly:

```text
scaf_authority_id
association_handle
```

Both are non-empty strings.

The schema does not prove that the authority/handle pair resolves to an accepted association in the package or upstream association set.

### 5.10 Initial payload boundary

The accepted rc03 payload remains reference-only.

Exact payload shape:

```text
payload_kind = source_reference
source_identity_ref
```

`source_identity_ref` is a non-empty string.

The schema introduces no:

```text
inline source bytes
fragment locator
chunk identifier
summary text
structured extract
content hash of materialized payload
source-loading status
current/latest state
```

## 6. Closed Object Shapes

All schema-owned objects use:

```text
additionalProperties: false
```

This is a structural-contract decision.

It prevents an accepted rc03 package from silently carrying new semantics such as:

```text
resolution_status
currentness
model_name
token_budget
prompt_template
verification_status
closure_status
```

Adding a future field requires a separately governed representation decision rather than permissive schema drift.

## 7. Array Uniqueness Boundary

The schema uses `uniqueItems: true` where exact duplicate parsed array members are structurally invalid, including selected lists such as:

```text
authority_context_entries
association_envelope
materialization_decisions
materialized_context_items
controlled_provenance_bases
materialized_context_item_refs
basis_refs
authority_basis_refs
```

This proves only exact parsed-value uniqueness.

It does **not** prove semantic-key uniqueness such as:

```text
unique scaf_authority_id
unique association_handle package-wide
unique materialized_context_item_id
exactly one Materialization Decision per accepted association
```

Those require source-aware/package-consistency validation.

## 8. Schema Does Not Own Canonical Physical YAML

The accepted rc03 representation defines deterministic canonical physical/raw-YAML direction.

JSON Schema operates on the parsed instance and therefore does not prove:

```text
mapping member order
list canonical sort order
quoted-string style
one YAML document only
no YAML anchors/aliases/merge keys/custom tags
raw duplicate YAML keys before parsing
UTF-8 / LF byte convention
byte-stable serialization
```

A future package validator may own strict-YAML/raw-ordering checks if separately justified.

Accordingly:

```text
schema-valid parsed instance
!= canonical physical YAML
```

## 9. Schema Does Not Prove Source-Aware Consistency

The following remain outside rc04 schema authority:

```text
SHA-256(binding) == exact upstream file bytes
accepted Consumption Selection validator PASS
accepted Context Source Association validator PASS
package authority domain == validated I exactly
Association Envelope == accepted upstream associations exactly
association_handle uniqueness and reference resolution
one decision per accepted association
materialized item ID uniqueness and reference resolution
no orphan materialized item
Controlled Provenance Basis resolution
decision -> item provenance correspondence
provenance -> corresponding decision/item-reference correspondence
source_identity_ref consistency with the projected Source Unit
canonical semantic/raw ordering
```

A structurally valid package can still be source-inconsistent.

## 10. Schema Does Not Prove Engineering Sufficiency

A schema PASS shall not be represented as proving:

```text
engineering-context sufficiency
implementation correctness
obligation satisfaction
verification sufficiency
compliance
risk acceptance
release readiness
closure
```

The accepted separation remains:

```text
parsed-instance structural validity
!= source-aware package consistency
!= engineering-context sufficiency
```

## 11. Runtime Observation Separation

rc04 adds no runtime observation representation.

The schema contains no accepted fields for:

```text
resolution_status
resolved_instance
resolved_sha256
constraint_match
load_status
load_error
missing
unresolvable
stale
superseded
currentness
resolver_timestamp
materialization_timestamp
```

Therefore:

```text
controlled association truth
!= package materialization truth
!= runtime resolution/materialization observation
```

remains preserved.

## 12. Consumer and AI Authority Boundary

No schema field transfers engineering authority to a consumer.

The schema contains no:

```text
model
agent
persona
prompt
conversation
approval
engineering_authority
```

The accepted rule remains:

```text
context presented to AI
!= authority granted to AI
```

## 13. Content-Use / Redistribution Boundary

Structural validity does not imply permission to copy, load, display, redistribute, or transform source content.

The accepted rule remains:

```text
controlled source association
!= content-use authorization
!= redistribution permission
!= license grant
```

The schema encodes no licensing or access-control engine.

## 14. Invalid vs Unresolved

rc04 may classify a parsed package instance as structurally invalid when it violates a schema-owned deterministic contract.

It does not convert a legitimate undecided engineering question into Invalid merely because the question is unresolved.

The frozen distinction remains:

```text
Invalid
= machine-verifiable representation/source/package inconsistency

Unresolved
= legitimate engineering question not yet decided
```

## 15. External Pattern / Licensing Boundary

rc04 defines an original SCAF schema from the accepted SCAF rc03 representation.

No external project schema, prompt, code body, documentation passage, or example content is required to define this contract.

Repository runtime tooling continues to use existing third-party dependencies under their existing dependency posture; rc04 introduces no new runtime dependency.

This statement is a bounded source-incorporation boundary, not legal advice.

## 16. Required Bounded Schema Verification

Before review, rc04 must demonstrate at minimum:

```text
JSON Schema Draft 2020-12 meta-validation PASS
accepted rc03 fixture validation PASS
```

Bounded negative structural cases should include:

```text
wrong package_kind rejected
wrong representation_release rejected
unexpected top-level field rejected
missing upstream binding member rejected
invalid lowercase SHA-256 syntax rejected
unknown materialization outcome rejected
materialized + empty item refs rejected
materialized + non_materialization_basis rejected
not_materialized + non-empty item refs rejected
not_materialized without basis rejected
unknown context_semantic rejected
unknown payload_kind rejected
materialized item without provenance basis rejected
runtime/resolver field rejected structurally
unexpected Controlled Source Association field rejected
```

These checks prove schema structural behavior only.

## 17. Required Non-Regression Boundary

rc04 shall not modify accepted/frozen prior surfaces except the expected documentation/navigation delta and the new schema artifact.

Expected inventories remain:

```text
Authority records:                     294
Project-Applicable Obligations:        218
Framework Normative Invariants:         76
L3 Patterns:                            12
L3 Relations:                          119
Effective Project Profile entries:     218
Consumption Selection D/E/I/O/X:       218 / 3 / 2 / 1 / 215
Context Source Association included I:   2
Context Source Units:                    2
Controlled associations:                 2
Exact instance constraints:              2
```

## 18. Explicit Non-Goals / Deferred Capabilities

v0.0.10rc04 does **not** add:

```text
production Controlled Context Package validator
source-aware package consistency validator
Controlled Context Package builder/generator
source/content loader
inline source-content representation
fragment locator or chunk syntax
summarization/extraction algorithm
ranking / priority policy
token-budget policy or tokenizer dependency
prompt construction
model adapter / orchestration / persona
repository-wide source discovery
general Source Resolver
Git-history traversal
remote fetch
source currentness / supersession model
runtime resolution/materialization observation schema
access-control / credential / secret-management system
CI package gate
authority-registry changes
new PAO/FNI
L4 implementation guidance
```

No item above is authorized merely because the schema now exists.

## 19. Current Decision Horizon Closure

rc04 is progression-sufficient when independent review establishes that:

1. the schema is valid Draft 2020-12;
2. the accepted rc03 fixture validates;
3. required/optional members and closed object shapes match rc03;
4. bounded vocabularies and SHA syntax match rc03;
5. materialized and not-materialized branches are structurally non-overlapping;
6. the initial payload remains reference-only;
7. schema authority does not expand into source-aware package proof or engineering judgment;
8. prior accepted/frozen surfaces and inventories remain intact; and
9. deferred validator/builder/loader/model/resolver/CI/L4 capabilities remain absent.

A clean review authorizes only a new dependency/value assessment.

It does **not** automatically authorize rc05 or a package validator.

## 20. Reconsideration Trigger

A subsequent capability may be considered only if the post-review dependency/value assessment establishes a material gap, such as:

```text
structurally valid packages can still disagree with exact validated upstream truth
and that disagreement is now a blocking machine-determinable consistency problem
for the next intended engineering action.
```

If no such dependency exists, SCAF shall stop rather than add another RC for theoretical completeness.
