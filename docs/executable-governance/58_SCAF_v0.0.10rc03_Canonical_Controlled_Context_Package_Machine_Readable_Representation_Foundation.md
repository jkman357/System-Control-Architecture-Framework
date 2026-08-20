# SCAF v0.0.10rc03 — Canonical Controlled Context Package Machine-Readable Representation Foundation

**Development Release:** v0.0.10rc03  
**Status:** Canonical Controlled Context Package Machine-Readable Representation Foundation / Review Candidate  
**Date:** 2026-08-19  
**Immediate Predecessor:** accepted v0.0.10rc02 (`b510cc2e40af6672be8af173c6e2d8c879444517`)  
**Frozen Basis:** v0.0.2 L1/L2; v0.0.3 L3; v0.0.4 Executable Governance; v0.0.5 L3 Machine-Readable Traceability; v0.0.6 Project Application / Effective Project Profile; v0.0.7 Consumption Selection; v0.0.8 Lifecycle-Proportional Governance; v0.0.9 Context Source Association / Source-Aware Validation

## 1. Decision Purpose

The accepted rc01 semantics defined Controlled Context Assembly and the accepted rc02 logical model fixed the canonical package aggregate, cardinalities, authority/association totality, materialization accounting and provenance constraints before serialization.

The rc02 independent review returned clean `PASS / GATE YES` with zero candidate-source findings and zero blocking review-evidence limitations.

The post-rc02 dependency/value assessment found one material next-step dependency: the logical model is now stable enough that schema, validation or construction work would otherwise have to invent incompatible field shapes, reference conventions, zero-materialization forms and canonical ordering rules.

The Current Decision Horizon for rc03 is therefore:

> **Serialize the accepted rc02 Controlled Context Package logical truth in one deterministic canonical YAML representation, without introducing package schema validation, source/content loading, ranking/token-budget policy, model integration or a general Source Resolver.**

rc03 is a representation decision only.

## 2. Why Representation Is Required Now

Without one shared representation, two implementations could both claim rc02 conformance while encoding materially different contracts for:

```text
exact upstream bindings
Assembly Objective identity
Authority Context Entry coverage
Association Envelope identity/reference
Materialization Decision accounting
explicit zero materialization
package-local Materialized Context Item identity
item-reference resolution
exact Controlled Provenance Bases
source-preserving vs derived context semantics
canonical order / duplicate treatment
```

A later schema or validator must validate one representation contract, not choose among competing interpretations.

Therefore:

```text
canonical logical model
        ↓
canonical machine-readable representation
        ↓
future schema / validator / builder only if separately justified
```

## 3. Representation Boundary

The accepted separations remain:

```text
package representation
!= schema validity
!= source-aware package consistency
!= engineering-context sufficiency

controlled association truth
!= package materialization truth
!= runtime resolution / materialization observation

machine-readable
!= machine-decided
```

The representation records controlled package truth only. It does not prove that the package is sufficient for an engineering task.

## 4. Canonical Artifact

rc03 adds:

```text
examples/controlled-context-package.yaml
```

Its identity is:

```text
package_kind: controlled_context_package
representation_release: v0.0.10rc03
```

YAML is used consistently with the accepted Project Application, Effective Project Profile, Consumption Selection and Context Source Association representations.

The canonical fixture is deliberately bounded and repository-owned. It does not copy third-party content and does not require external source material.

## 5. Canonical Top-Level Shape

The canonical parsed top-level shape is exactly:

```text
package_kind
representation_release
upstream_binding
assembly_objective
authority_context_entries
materialized_context_items
```

Conceptually:

```text
Controlled Context Package
│
├─ upstream_binding
│    ├─ consumption_selection
│    └─ context_source_association_set
│
├─ assembly_objective
│
├─ authority_context_entries
│    └─ exactly one entry per authority in validated I
│         ├─ association_envelope
│         └─ materialization_decisions
│
└─ materialized_context_items
     └─ 0..n package-local items with controlled provenance
```

No runtime-resolution or consumer/model state section is part of rc03.

## 6. Exact Upstream Binding

`upstream_binding` has exactly two members in canonical order:

```text
consumption_selection
context_source_association_set
```

### 6.1 Consumption Selection binding

The canonical shape is:

```text
source_sha256
selection_kind
representation_release
project_scope_ref
```

The fixture binds the exact current bytes of:

```text
examples/consumption-selection.yaml
```

with SHA-256:

```text
0a99e3d38b0b14129ab922966c757c17509ca91d7d2601dfd35805ffa2628ede
```

### 6.2 Context Source Association Set binding

The canonical shape is:

```text
source_sha256
association_set_kind
representation_release
consumption_selection_source_sha256
project_scope_ref
```

The fixture binds the exact current bytes of:

```text
examples/context-source-associations.yaml
```

with SHA-256:

```text
01ab6a5b151a366f8acc4ddaf666b915ac1ddbd327522c43b6af2485c8cb4ccc
```

The nested `consumption_selection_source_sha256` must agree with both the bound association artifact and the package's exact Consumption Selection binding.

A future source-aware package validator must first establish accepted upstream validation before trusting package-domain reasoning.

## 7. Upstream Binding Does Not Recreate Authority

The package binding is subordinate provenance/identity only.

It does not duplicate or replace:

```text
Project Application truth
Effective Project Profile truth
Consumption Selection truth
Context Source Association truth
```

Therefore:

```text
package upstream binding
!= applicability authority
!= selection authority
!= source-association authority
```

## 8. Assembly Objective Representation

`assembly_objective` has exactly:

```text
objective_id
objective_statement
```

`objective_id` is a package-controlled objective identifier.

`objective_statement` is a non-empty bounded engineering-purpose statement.

The representation intentionally does not freeze a task taxonomy, workflow state, lifecycle state or model-specific objective vocabulary.

The objective may guide package construction, but it cannot rewrite validated `I`, accepted associations, applicability or engineering authority.

## 9. Authority Context Entry Domain

The bound Consumption Selection fixture has validated included domain `I`:

```text
SCAF-AK-001
SCAF-AK-002
```

The canonical package therefore records exactly two `authority_context_entries`, in ascending `scaf_authority_id` order.

The rule remains:

```text
Authority Context Entry domain = validated I exactly
```

No `O` or `X` authority may appear merely because content or a similar source is available.

## 10. Authority Context Entry Shape

Each Authority Context Entry has exactly:

```text
scaf_authority_id
association_envelope
materialization_decisions
```

The entry exists even when both lists are empty.

The fixture deliberately serializes:

```yaml
- scaf_authority_id: "SCAF-AK-002"
  association_envelope: []
  materialization_decisions: []
```

This preserves:

```text
missing Authority Context Entry
!= explicit zero-association Authority Context Entry
```

and keeps zero association distinct from associations present with zero materialized content.

## 11. Package-Local Association Handle

Each member of `association_envelope` has:

```text
association_handle
controlled_association
```

`association_handle` is a **package-local reference handle only**.

It does not create or claim an upstream Controlled Source Association identifier.

Therefore:

```text
association_handle
!= upstream association identity
```

The accepted v0.0.9 association representation intentionally has no standalone `association_id`. Exact upstream relationship identity remains defined by the accepted association semantics within its authority entry.

A future validator must prove that each handle's `controlled_association` body resolves to exactly one accepted association for that Authority Context Entry.

Handles shall be unique across the package so Materialization Decisions and provenance bases resolve deterministically.

## 12. Controlled Association Projection

`controlled_association` is a source-fidelity package projection of one accepted upstream association.

Its required members remain:

```text
source_unit_ref
relationship_semantic
relationship_scope_ref
association_provenance
```

Optional members remain:

```text
authority_qualification
instance_constraint
```

The projection preserves the accepted v0.0.9 field shapes and vocabularies. rc03 does not add a new relationship semantic, provenance assertion kind, Authority Qualification kind or Instance Constraint kind.

The package representation does not repeat the Source Unit Catalog because Source Unit identity/control-domain truth remains owned by the exact bound association set.

## 13. Association Envelope Fidelity

For authority `A`:

```text
package association_envelope(A)
= exact accepted upstream associations(A)
```

A package must not:

```text
add a discovered source relationship
delete an association because no content is materialized
retag relationship_semantic
change relationship_scope_ref
change association provenance
change Authority Qualification
change Instance Constraint
```

The envelope is preserved relationship truth, not a new discovery result.

## 14. Materialization Decision Shape

Each `materialization_decisions` member has:

```text
association_handle
outcome
materialized_context_item_refs
```

When `outcome` is `not_materialized`, it additionally has:

```text
non_materialization_basis
```

The canonical rc03 `outcome` vocabulary is exactly:

```text
materialized
not_materialized
```

These are package-content accounting tokens only.

They are not applicability, source validity, waiver, accepted risk, verification, release or closure tokens.

## 15. Complete Association Accounting

Every package-local `association_handle` in one Authority Context Entry's envelope appears exactly once in that entry's `materialization_decisions`.

No decision may refer to an association handle from another authority entry.

Therefore:

```text
accepted association
        ↓
exactly one package Materialization Decision
```

The fixture demonstrates both outcomes:

```text
ASSOC-SCAF-AK-001-001 -> materialized -> CTX-ITEM-001
ASSOC-SCAF-AK-001-002 -> not_materialized -> [] + explicit basis
```

This makes content absence machine-visible instead of silently dropping association truth.

## 16. Materialized Outcome

For:

```text
outcome: materialized
```

`materialized_context_item_refs` shall contain `1..n` unique package-local item references.

`non_materialization_basis` shall be absent.

This representation does not imply that the referenced items are sufficient for the engineering objective.

## 17. Not-Materialized Outcome

For:

```text
outcome: not_materialized
```

`materialized_context_item_refs` shall be an explicit empty list:

```yaml
materialized_context_item_refs: []
```

and `non_materialization_basis` shall be a non-empty controlled package statement.

rc03 intentionally does not freeze a categorical reason taxonomy. The basis remains text because no current material dependency justifies a global reason vocabulary.

The state remains:

```text
not_materialized
!= association removed
!= source invalid
!= not_applicable
!= v0.0.7 bounded omission O
!= waiver
!= accepted risk
!= closure
```

## 18. Materialized Context Item Catalog

`materialized_context_items` is an explicit list containing `0..n` package-local items.

Each item has exactly:

```text
materialized_context_item_id
context_semantic
controlled_provenance_bases
payload
```

`materialized_context_item_id` is package-local and shall be unique.

Every item must be referenced by at least one Materialization Decision.

No orphan materialized item is valid canonical package content.

## 19. Context Semantic Vocabulary

rc03 freezes the initial `context_semantic` vocabulary:

```text
source_preserving
derived
```

This preserves the rc02 distinction between source-preserving and derived/transformed context.

The token does not grant authority.

Therefore:

```text
derived
!= authoritative source truth
```

A future schema may enforce the token vocabulary; a future source-aware validator may prove package consistency. Neither is introduced here.

## 20. Controlled Provenance Basis

Every item contains `controlled_provenance_bases` with `1..n` members.

Each member has exactly:

```text
scaf_authority_id
association_handle
```

The pair must resolve to one association handle inside the named Authority Context Entry.

This package-local pair is a resolvable pointer to the package projection of one exact accepted upstream Controlled Source Association.

It is not a new upstream association identity.

For a multi-association or cross-authority item, every supporting basis must be listed independently.

Therefore:

```text
shared item
!= merged authority ownership
```

## 21. Provenance / Decision Correspondence

If a Materialization Decision for association handle `H` references item `X`, then item `X` shall include a Controlled Provenance Basis resolving to that same authority + `H` pair.

Conversely, every Controlled Provenance Basis of an item shall correspond to at least one Materialization Decision that references that item.

This prevents unrelated package content from being attached to an association merely through an item reference.

A future validator must be able to prove this bidirectional correspondence.

## 22. Payload Boundary

rc03 deliberately keeps content materialization narrow.

The canonical `payload` shape is:

```text
payload_kind
source_identity_ref
```

The only rc03 `payload_kind` is:

```text
source_reference
```

`source_identity_ref` is an opaque reference identifying the consumer-facing source/derived artifact represented by this package item.

The canonical fixture uses the repository-owned source identity:

```text
repo:docs/normative/00_SCAF_Authority_Kernel.md
```

The package does not inline source text, copy source bytes, define fragment syntax or execute content loading.

This narrow payload form is intentional. Additional payload kinds such as bounded inline fragments or derived text require a separately justified representation extension rather than being silently invented by consumers.

## 23. Source-Preserving / Derived Semantics with Reference Payload

`context_semantic` and `payload` have different responsibilities:

```text
context_semantic
= whether the package item claims source-preserving or derived consumer semantics

payload
= how the current representation points to the consumer-facing artifact
```

A `derived` item may later reference a controlled derived artifact without converting that artifact into upstream source authority.

rc03 does not define transformation algorithms, derivation fidelity metrics, generated-artifact lifecycle or a derived-artifact registry.

## 24. Package-Local Identity vs Source Identity

The representation keeps:

```text
materialized_context_item_id
!= source_identity_ref
```

Two package items may not be treated as the same logical item merely because they refer to identical bytes or the same source identity if their controlled provenance/materialization semantics differ.

Likewise, a package-local item does not automatically become a new Source Unit.

## 25. Runtime Observation Remains Outside the Package

The canonical representation has no field for:

```text
resolution_status
resolved_instance
resolved_sha256
currentness
stale
superseded
load_status
load_error
consumer_access_result
transformation_status
resolver_timestamp
```

Those are runtime resolution/materialization observations and remain separately gated.

The governing distinction remains:

```text
controlled association truth
!= package Materialization Decision
!= runtime resolution/materialization observation
```

## 26. Package Conformance Is Not Engineering Sufficiency

The representation is designed so a future validator can deterministically prove facts such as:

```text
upstream binding hashes match exact validated inputs
authority entry domain equals validated I
envelopes equal accepted upstream association truth
one decision exists per association handle
item references resolve
provenance bases resolve
no orphan item exists
materialized decision <-> provenance correspondence is complete
canonical order is respected
```

A PASS on those conditions shall not prove:

```text
engineering context is sufficient
implementation is correct
verification is sufficient
compliance is satisfied
risk is accepted
release is ready
work is closed
```

Therefore:

```text
representation/package conformance
!= engineering-context sufficiency
```

## 27. Consumer / AI Authority Boundary

The canonical representation contains no consumer identity, model name, prompt, persona, conversation state or orchestration field.

The same package may later be consumed by a human or AI without changing authority ownership.

Therefore:

```text
context package consumed by AI
!= AI gains engineering authority
```

## 28. Content Authorization Boundary

A controlled association or package item does not itself grant permission to expose or redistribute content.

The accepted boundary remains:

```text
controlled association
!= content-use authorization
!= redistribution permission
!= license grant
```

The fixture uses only repository-owned SCAF references and does not incorporate third-party content.

A future consumer/assembler may require separately controlled authorization inputs. rc03 does not create an access-control, credential, licensing or secret-management system.

## 29. Canonical Ordering

For deterministic byte-stable canonical output:

1. top-level members appear in the order defined in Section 5;
2. `upstream_binding` members appear `consumption_selection`, then `context_source_association_set`;
3. nested mappings use the field order defined by their record sections;
4. `authority_context_entries` sort ascending by exact `scaf_authority_id`;
5. `association_envelope` sorts ascending by the accepted v0.0.9 normalized semantic association tuple, with `association_handle` not contributing upstream semantic identity;
6. `materialization_decisions` sort in the same association order as their corresponding envelope handles;
7. `materialized_context_item_refs` sort ascending by exact item ID;
8. `materialized_context_items` sort ascending by `materialized_context_item_id`;
9. `controlled_provenance_bases` sort ascending by `(scaf_authority_id, association_handle)`;
10. inherited `basis_refs` / `authority_basis_refs` preserve accepted v0.0.9 canonical ordering;
11. UTF-8 + LF line endings are used;
12. canonical scalar string values are double-quoted in the fixture.

Ordering is representation determinism, not engineering priority.

## 30. Canonical Uniqueness and Reference Rules

A future conforming validator shall be capable of proving at least:

```text
unique package_kind/release identity
unique objective_id inside one package
Authority Context Entry domain == validated I exactly
unique package-local association_handle across the package
association envelope fidelity to exact upstream associations
exactly one Materialization Decision per association_handle
unique materialized_context_item_id
all item refs resolve
all provenance authority/handle pairs resolve
no orphan materialized item exists
materialized decisions and item provenance correspond bidirectionally
not_materialized decisions have [] refs + non-empty basis
materialized decisions have 1..n refs + no non_materialization_basis
valid context_semantic token
valid payload_kind token
canonical ordering
```

rc03 establishes these representation invariants but does not implement their production enforcement.

## 31. Strict Representation Policy Direction

To preserve deterministic future tooling, the canonical fixture is intended for a future strict YAML policy comparable to accepted SCAF machine-readable artifacts:

```text
one YAML document only
no duplicate mapping keys
no aliases / anchors / merge keys
no custom tags
string mapping keys only
canonical quoted string values
canonical member/list ordering
```

This section defines future validation direction only. No new production validator is added in rc03.

## 32. Invalid vs Unresolved

The frozen distinction remains:

```text
Invalid
= machine-verifiable representation/source/package inconsistency

Unresolved
= legitimate engineering question not yet decided
```

A malformed package or broken deterministic reference may later be classified Invalid.

Whether the package contains enough engineering information for one objective may remain Unresolved or require human engineering judgment.

The representation shall not collapse those categories.

## 33. Deliberately Not Introduced

rc03 does **not** introduce:

```text
JSON Schema or other package schema
production Controlled Context Package validator
package builder / generator
content loader
inline source content
fragment / selector syntax
chunking
summarization / extraction algorithm
ranking / priority policy
token budget / tokenizer dependency
prompt construction
model adapter / orchestration / persona
repository source discovery
general Source Resolver
Git history traversal
remote fetching
source currentness / supersession model
runtime resolution/materialization observation schema
access-control / credential / secret-management system
CI package gate
authority-registry change
new PAO / FNI
L4 implementation guidance
```

## 34. External Pattern / Licensing Boundary

This representation is independently defined from accepted SCAF semantics and the reviewed rc02 logical model.

No third-party source code, prompt, schema body, documentation passage or example content is directly incorporated into the rc03 delta.

External designs may inform general engineering patterns, but direct reuse remains separately subject to copyright, license, attribution, redistribution, NOTICE, trademark and related obligations.

This is a project-governance boundary, not a legal opinion about any specific third-party source.

## 35. Bounded Verification Expectation

Because rc03 adds a machine-readable representation but no new production executable behavior, independent review should establish at least:

```text
ZIP / predecessor identity and safe root
exact effective source delta
protected frozen-source preservation
YAML parseability and strict single-document sanity
exact Consumption Selection SHA binding
exact Context Source Association Set SHA binding
upstream metadata correspondence
authority_context_entries domain == validated I
association envelope fidelity
exact one-decision-per-association accounting
explicit zero-association and zero-materialization cases
item reference integrity
controlled provenance resolution and bidirectional correspondence
canonical ordering
prohibited runtime/model/resolver fields absent
repository-owned production validation/integrity PASS
git diff --check PASS
```

The historical broader regression inventory need not be rerun solely for ritual completeness when no accepted executable surface changes and the bounded checks pass.

## 36. Progression Sufficiency

rc03 is progression-sufficient when independent review establishes that the canonical YAML faithfully serializes the accepted rc02 logical model without adding source/content resolution, engineering authority or consumer/model semantics.

A clean review authorizes only a new dependency/value assessment.

It does not automatically authorize:

```text
rc04
package schema
package validator
package builder
content loader
ranking/token-budget policy
model integration
Source Resolver
```

The next question after a clean review is:

> **Is a parsed-instance structural schema materially necessary now to prevent incompatible package shapes from entering future validation/construction work?**

If not materially YES, SCAF shall STOP or defer rather than continue for theoretical completeness.

## 37. Acceptance Statement

v0.0.10rc03 is acceptable for independent review when:

- the exact accepted rc02 predecessor is preserved;
- the source delta is limited to the canonical package fixture, rc03 controlled record and navigation/history updates;
- the YAML parses and exact upstream byte bindings match current accepted fixtures;
- authority entry coverage equals validated `I` exactly;
- association envelope / decision accounting preserves every accepted association;
- explicit zero cases remain distinct;
- every package item reference/provenance basis resolves deterministically;
- canonical ordering is preserved;
- runtime resolution/materialization observation, prompt/model and engineering-authority semantics remain absent;
- protected frozen sources remain unchanged;
- bounded repository-owned production checks and `git diff --check` remain PASS.
