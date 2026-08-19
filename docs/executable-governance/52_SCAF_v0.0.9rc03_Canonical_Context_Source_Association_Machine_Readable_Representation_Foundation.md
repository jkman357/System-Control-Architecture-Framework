# SCAF v0.0.9rc03 — Canonical Context Source Association Machine-Readable Representation Foundation

**Development Release:** v0.0.9rc03  
**Status:** Canonical Context Source Association Machine-Readable Representation Foundation / Review Candidate  
**Date:** 2026-08-19  
**Immediate Predecessor:** accepted v0.0.9rc02 (`4f1f4579b9db73bab3f3db7f61da8586bfdf8fc8`)  
**Frozen Basis:** v0.0.2 L1/L2; v0.0.3 L3; v0.0.4 Executable Governance; v0.0.5 L3 Machine-Readable Traceability; v0.0.6 Project Application / Effective Project Profile; v0.0.7 Consumption Selection; v0.0.8 Lifecycle-Proportional Governance

## 1. Decision Purpose

The accepted rc01 semantics defined Context Source Resolution and the accepted rc02 logical model fixed the canonical relationship structure before serialization.

The rc02 independent review returned `PASS / GATE YES` with zero findings and zero open blocking review-evidence limitations.

The post-rc02 dependency/value assessment found one material next-step dependency: the canonical logical model is now sufficiently stable to require one shared machine-readable representation before schema, validation or resolver work can be defined without implementation divergence.

The Current Decision Horizon for rc03 is therefore:

> **Serialize the accepted rc02 controlled-association logical truth in one deterministic canonical YAML shape, while keeping runtime resolution observations outside that representation.**

rc03 intentionally does not add a schema, production validator, resolver, filesystem/Git scan, content loader, ranking/token-budget policy or AI Context Assembly.

## 2. Why a Representation Is Required Now

Without a canonical representation, conforming implementations could still choose incompatible serialized contracts for:

```text
selection binding
complete I coverage
zero-association representation
Source Unit identity and control domain
association atomicity
relationship semantic and scope
association provenance
bounded authority qualification
exact-instance constraint
ordering / duplicate handling
```

Those differences would directly affect a later schema and validator. Defining the representation before those executable layers avoids encoding incompatible assumptions into tooling.

This is therefore not format polish. It is the minimum machine-readable contract needed for the next executable step.

## 3. Representation Boundary

The canonical representation contains **controlled association truth only**.

The frozen rc02 two-plane invariant remains:

```text
controlled association truth
!= runtime resolution observation
```

Accordingly the canonical rc03 artifact shall not record runtime observations such as:

```text
resolved bytes
resolved path state
missing
unresolvable
stale / superseded
currentness unknown
instance-constraint match / mismatch
resolver timestamp
resolver implementation result
```

Those observations belong to a separately gated future resolver-result representation if such a representation is justified.

## 4. Canonical Artifact

The canonical fixture introduced by rc03 is:

```text
examples/context-source-associations.yaml
```

Its identity is:

```text
association_set_kind: context_source_association_set
representation_release: v0.0.9rc03
```

The representation is YAML because existing accepted SCAF Project Application, Effective Project Profile and Consumption Selection machine-readable artifacts already use YAML. This choice is a repository representation convention only; it does not grant YAML content engineering authority.

## 5. Canonical Top-Level Shape

The canonical parsed shape is exactly:

```text
association_set_kind
representation_release
source_selection_binding
source_units
authority_source_entries
```

Conceptually:

```text
Context Source Association Set
│
├─ source_selection_binding
├─ source_units
│    └─ 0..n Source Unit records
└─ authority_source_entries
     └─ exactly one entry for every authority in validated I
          └─ 0..n atomic Controlled Source Associations
```

No runtime-resolution section is part of rc03.

## 6. Exact Upstream Selection Binding

`source_selection_binding` contains:

```text
consumption_selection_source_sha256
selection_kind
selection_representation_release
project_scope_ref
```

The canonical fixture binds the exact bytes of `examples/consumption-selection.yaml`:

```text
SHA-256: 0a99e3d38b0b14129ab922966c757c17509ca91d7d2601dfd35805ffa2628ede
```

The binding values are subordinate provenance. They do not duplicate or replace Project Application, Effective Project Profile or Consumption Selection truth.

A future validator must prove that:

```text
recorded SHA-256
== exact bound Consumption Selection bytes
```

and that the recorded kind/release/scope values agree with that same validated selection.

## 7. Coverage Domain

The bound Consumption Selection fixture has included domain `I`:

```text
SCAF-AK-001
SCAF-AK-002
```

The canonical rc03 artifact therefore contains exactly one `authority_source_entries` record for each of those two authorities and none for `O` or `X`.

The frozen distinction remains:

```text
missing Authority Source Entry
!= explicit zero associations
```

The fixture deliberately records:

```yaml
- scaf_authority_id: "SCAF-AK-002"
  associations: []
```

so zero association is serialized explicitly rather than inferred from omission.

## 8. Source Unit Record

Each `source_units` member has exactly:

```text
source_unit_id
source_identity_ref
control_domain
```

`source_unit_id` is an association-set-local stable identifier used by associations.

`source_identity_ref` is an opaque controlled Source Identity reference. The fixture uses readable `repo:`-prefixed values, but rc03 does **not** define resolver semantics for that prefix or any URI/path scheme.

Therefore:

```text
source_identity_ref
!= proof that a resolver can resolve the source now
!= exact source bytes
```

`control_domain` is one of:

```text
framework
project
external
```

Control domain records governance/ownership domain only. It does not imply applicability, authority for a specific property, verification, correctness or closure.

## 9. Source Identity vs Exact Source Instance

The accepted separation remains:

```text
Source Identity
!= expected/pinned Instance Constraint
!= actual runtime-resolved Source Instance
```

`source_identity_ref` carries Source Identity.

An optional `instance_constraint` may constrain which exact source bytes are acceptable for one association. rc03 supports one canonical constraint form:

```yaml
instance_constraint:
  constraint_kind: "sha256"
  value: "<64 lowercase hexadecimal characters>"
```

The actual source instance observed by a future resolver is not stored in this controlled-association artifact.

## 10. Authority Source Entry

Each `authority_source_entries` record has exactly:

```text
scaf_authority_id
associations
```

`scaf_authority_id` must belong to validated `I` of the exact bound Consumption Selection.

`associations` is an explicit list and may contain zero or more Controlled Source Associations.

The entry does not repeat:

```text
profile_state
Project Application rationale
verification state
closure state
```

Those truths remain upstream or separately owned.

## 11. Atomic Controlled Source Association

Each association serializes one accepted rc02 atomic semantic statement:

```text
one selected authority
+ one Source Unit reference
+ one relationship semantic
+ one relationship scope
+ one controlled association provenance
+ optional bounded authority qualification
+ optional instance constraint
```

The required fields are:

```text
source_unit_ref
relationship_semantic
relationship_scope_ref
association_provenance
```

Optional fields are:

```text
authority_qualification
instance_constraint
```

One association shall not contain a multi-role array. If the same Source Unit has two materially different relationship semantics for the same authority, the artifact records two atomic associations.

## 12. Canonical Relationship Semantic Tokens

rc03 freezes the initial representation vocabulary:

```text
framework_obligation_source
project_decision_source
realization_source
verification_definition_source
verification_evidence_source
external_constraint_source
supporting_context_source
```

These tokens explain **why the source is related**. They do not confer authority.

Therefore:

```text
relationship_semantic
!= authority qualification
```

Any future extension of this token vocabulary requires a separately reviewed representation decision; tools shall not silently invent additional canonical tokens.

## 13. Relationship Scope

`relationship_scope_ref` is a required opaque controlled reference defining the bounded property, decision, behavior, interface, evidence purpose or other engineering subject for which the association is asserted.

The representation deliberately does not define a hierarchy or resolver for these references.

Therefore:

```text
relationship_scope_ref
!= project_scope_ref
!= filesystem path scope
!= implicit parent/child scope propagation
```

The exact opaque project `project_scope_ref` remains separately inherited through the upstream Consumption Selection binding.

## 14. Association Provenance

Every association contains:

```yaml
association_provenance:
  assertion_kind: "..."
  basis_refs:
    - "..."
```

The canonical rc03 `assertion_kind` vocabulary is:

```text
framework_declared
project_declared
controlled_rule_derived
```

A discovered candidate is intentionally not a canonical controlled-association assertion kind.

The frozen boundary remains:

```text
discovered candidate
!= controlled association
```

`basis_refs` are opaque controlled references and shall be non-empty. Multiple basis references support one semantic association rather than creating duplicate relationship truth.

## 15. Bounded Authority Qualification

`authority_qualification` is optional.

When present, its canonical shape is:

```yaml
authority_qualification:
  qualification_kind: "authoritative_for_relationship_scope"
  authority_scope_ref: "..."
  authority_basis_refs:
    - "..."
```

The only rc03 `qualification_kind` is:

```text
authoritative_for_relationship_scope
```

The qualification applies only to the bounded `authority_scope_ref` and must be supported by non-empty `authority_basis_refs` grounded in existing authority ownership.

The representation intentionally does not permit a file-global boolean such as:

```text
authoritative: true
```

and does not create new Project Design Authority, Verification / Assurance Authority, external authority or closure authority.

## 16. Canonical Uniqueness

Within one Authority Source Entry, semantic association uniqueness is determined by the normalized tuple:

```text
source_unit_ref
relationship_semantic
relationship_scope_ref
authority_qualification (if present)
instance_constraint (if present)
```

`association_provenance.basis_refs` may contain multiple supporting bases for that one semantic association and do not create duplicate associations by themselves.

rc03 intentionally does not introduce an `association_id`; the semantic tuple is sufficient for this Current Decision Horizon.

## 17. Canonical Ordering

For byte-stable canonical output:

```text
1. top-level members appear in the rc03 canonical order;
2. source_units sort ascending by source_unit_id;
3. authority_source_entries sort ascending by scaf_authority_id;
4. associations sort ascending by the normalized semantic-identity tuple;
5. basis_refs and authority_basis_refs sort ascending as exact strings;
6. mappings use the field order defined by this record;
7. UTF-8 + LF line endings are used;
8. canonical scalar string values are double-quoted in the fixture.
```

A later generator, if justified, must emit byte-stable output under the accepted representation contract.

## 18. Structural Invariants for Future Schema / Validation

rc03 establishes representation invariants but does not implement their production enforcement.

A future schema/validator, if separately justified, must be able to establish at least:

```text
exact top-level identity and release
exact bound Consumption Selection SHA / kind / release / project scope
accepted upstream validation before downstream semantic use
Authority Source Entry coverage == validated I
no O/X authority entries
unique source_unit_id
unique source_identity_ref within the association set
all source_unit_ref values resolve to Source Unit Catalog entries
no unused Source Unit Catalog entries
valid control_domain token
valid relationship_semantic token
non-empty relationship_scope_ref
valid association provenance token + non-empty unique basis_refs
bounded Authority Qualification shape and non-empty basis
sha256 Instance Constraint shape when present
semantic association uniqueness
canonical ordering
absence of runtime resolution observations
absence of duplicated applicability / verification / closure truth
```

This list is validation ownership direction only. No schema or validator is introduced by rc03.

## 19. Runtime Resolution Observation Remains Separate

The canonical artifact contains no field for:

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

A future resolver may produce such observations in a separate result artifact, but that future artifact shall remain subordinate to the controlled association set and shall not rewrite it merely because source availability changes.

## 20. Source Existence Still Does Not Prove Satisfaction

The representation preserves:

```text
association present != obligation satisfied
source identity resolves != implementation correct
verification source exists != verification executed
evidence source exists != evidence sufficient
authority-qualified source exists != closure
```

Machine-readable representation does not convert these engineering judgments into machine facts.

## 21. Context Assembly Remains Downstream

rc03 is still not a Context Assembly mechanism.

It does not authorize:

```text
content extraction
fragment loading
chunking
summarization
ranking / priority / severity selection
semantic-similarity inclusion
token budget / truncation
prompt structure
model selection
conversation injection
```

The downstream chain remains:

```text
validated Consumption Selection
        ↓
controlled Context Source Association Set
        ↓
future source resolution
        ↓
future separately governed Context Assembly
```

## 22. External Pattern / Licensing Boundary

The rc03 representation is independently defined within SCAF from accepted SCAF semantics and logical-model requirements.

No third-party source code, prompt, schema, documentation text or example content is incorporated into this artifact. External projects may inform general design-pattern study, but direct incorporation remains separately subject to copyright, license, attribution, redistribution, NOTICE and trademark review.

This section records the project boundary; it does not make a legal conclusion about any third-party work.

## 23. Deliberately Not Introduced

rc03 does **not** introduce:

```text
JSON Schema or another validation schema
production source-association validator
source resolver
runtime resolution-result representation
filesystem or Git scanning
locator/URI resolver semantics
remote fetching
external trust-model expansion
content parser / chunker
ranking / priority / token-budget policy
AI context package / prompt model
Context Assembly
CI enforcement
authority-registry change
new PAO / FNI
L4 implementation guidance
```

## 24. Bounded Verification Expectation

Because rc03 introduces a new machine-readable representation but no production executable behavior, review depth should cover:

```text
package / predecessor identity
exact source delta
protected frozen-source preservation
YAML loadability
exact upstream selection SHA binding
complete validated-I coverage
catalog/reference integrity
explicit zero association
association tuple uniqueness
canonical ordering
prohibited runtime-observation absence
six repository-owned bounded production checks
```

The historical full 262-test inventory need not be rerun solely for ritual completeness when no frozen executable surface changes and the bounded checks pass.

## 25. Progression Sufficiency

rc03 is progression-sufficient when one independent review establishes that the YAML representation faithfully serializes the accepted rc02 model without introducing resolver or Context Assembly semantics.

A clean rc03 review authorizes only a new dependency/value assessment.

It does not automatically authorize:

```text
rc04
schema
validator
resolver
```

The next question after a clean review is simply:

> **Is executable structural validation now necessary to prevent representation divergence or invalid source-association data from entering later resolver work?**

If the answer is not materially YES, SCAF shall STOP or defer rather than continue for theoretical completeness.

## 26. Acceptance Statement

v0.0.9rc03 is acceptable for independent review when:

- the exact rc02 predecessor is preserved;
- the source delta is limited to the representation fixture, rc03 controlled record and navigation/history updates;
- the fixture parses as YAML and binds the exact current Consumption Selection bytes;
- its Authority Source Entry domain equals validated `I` exactly;
- Source Unit references are complete and deterministic;
- controlled association truth remains distinct from runtime resolution observation;
- existing authority/applicability/verification/closure boundaries remain unchanged;
- protected frozen sources remain unchanged;
- bounded repository-owned production checks remain PASS.
