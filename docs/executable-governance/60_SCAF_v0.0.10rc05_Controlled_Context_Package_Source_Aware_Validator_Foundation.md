# SCAF v0.0.10rc05 — Controlled Context Package Source-Aware Validator Foundation

**Development Release:** v0.0.10rc05  
**Status:** Controlled Context Package Source-Aware Validator Foundation / Review Candidate  
**Date:** 2026-08-20  
**Immediate Predecessor:** accepted v0.0.10rc04 (`dfe69dd331dae5164d5343dcf9aa67c399e2eb87`)  
**Frozen Basis:** v0.0.2 L1/L2; v0.0.3 L3; v0.0.4 Executable Governance; v0.0.5 L3 Machine-Readable Traceability; v0.0.6 Project Application / Effective Project Profile; v0.0.7 Consumption Selection; v0.0.8 Lifecycle-Proportional Governance; v0.0.9 Context Source Association / Source-Aware Validation

## 1. Decision Purpose

The accepted v0.0.10 chain now contains:

```text
rc01  Controlled Context Assembly semantic foundation
  ↓
rc02  canonical representation-neutral Controlled Context Package logical model
  ↓
rc03  canonical deterministic Controlled Context Package YAML representation
  ↓
rc04  JSON Schema Draft 2020-12 parsed-instance structural contract
```

The rc04 independent review returned clean `PASS / GATE YES` with zero candidate-source findings and zero blocking review-evidence limitations.

The post-rc04 dependency/value assessment identified one remaining machine-determinable gap before any builder decision can be made responsibly: schema validity cannot prove that a structurally valid Controlled Context Package agrees with the exact accepted upstream Consumption Selection and Context Source Association truth.

The Current Decision Horizon for rc05 is therefore:

> **Provide one repository-owned production source-aware validator that proves deterministic Controlled Context Package consistency against the exact accepted upstream package inputs, authority domain, association envelope, materialization accounting and controlled provenance, without becoming a package builder, source resolver, content loader or engineering-sufficiency authority.**

## 2. Engineering Problem

Without rc05, a structurally valid package may still be source-inconsistent. Examples include:

```text
recorded Consumption Selection SHA does not match selected bytes
recorded Context Source Association SHA does not match selected bytes
package Authority Context Entry domain differs from validated I
Association Envelope differs from accepted upstream association truth
one package-local association_handle is reused
one accepted association has no Materialization Decision
one accepted association has more than one Materialization Decision
one Materialization Decision targets another authority entry's handle
one Materialized Context Item ID is duplicated semantically
one item reference does not resolve
one package item is orphaned
one Controlled Provenance Basis does not resolve
one decision references an item whose provenance does not include that association
one item provenance basis exists without a corresponding materialized decision reference
canonical raw/list ordering is violated
```

These conditions are deterministic package/source facts. They should not remain dependent on reviewer interpretation or separate consumer implementations.

## 3. Governing Separation

rc05 preserves the accepted layered boundary:

```text
package representation
!= parsed-instance structural validity
!= source-aware package consistency
!= engineering-context sufficiency
```

The production validator owns source-aware package consistency after accepted parsed-instance validation.

A PASS is not an engineering approval.

It does not prove:

```text
engineering context is sufficient for the objective
implementation is correct
verification is sufficient
compliance is complete
risk is accepted
release is ready
closure is achieved
source is current / latest / non-superseded
consumer is authorized to receive or redistribute content
AI or human consumer owns engineering authority
```

## 4. Production Artifact

rc05 adds:

```text
tools/scaf_controlled_context_package_validator/
```

Primary executable entry point:

```text
python -m tools.scaf_controlled_context_package_validator.validator
```

Default repository-owned fixture inputs:

```text
examples/controlled-context-package.yaml
examples/context-source-associations.yaml
examples/consumption-selection.yaml
examples/effective-project-profile.yaml
examples/project-application.yaml
```

Project-side inputs may be selected with:

```text
--package
--associations
--selection
--profile
--project-application
```

The accepted repository-owned package schema and upstream validator implementations are not production CLI override points.

Programmatic entry point:

```python
validate_controlled_context_package(
    repo_root,
    package_path=None,
    associations_path=None,
    selection_path=None,
    profile_path=None,
    project_application_path=None,
)
```

CLI and programmatic consumers therefore use the same validation-owning implementation.

## 5. Validated-Input Ownership

The Controlled Context Package does not own applicability, selected authority membership or Controlled Source Association truth.

The validator captures the exact selected package, association-set and Consumption Selection bytes before package-domain reasoning.

The accepted validation chain is:

```text
exact Controlled Context Package bytes
        ↓
strict package YAML / canonical representation policy
        ↓
accepted rc04 package schema PASS
        ↓
exact bound Context Source Association Set bytes
        +
exact bound Consumption Selection bytes
        ↓
accepted Context Source Association source-aware validation PASS
        ↓
accepted Consumption Selection source-aware validation PASS
        ↓
validated I + accepted Controlled Source Associations
        ↓
package source-aware consistency proof
```

If accepted upstream validation fails, package-domain proof stops.

Therefore:

```text
package does not self-assert validated I
package does not self-assert accepted association truth
```

## 6. Exact Upstream Binding Proof

The validator proves the package's recorded Consumption Selection binding against the exact selected bytes:

```text
SHA-256(exact selection bytes)
selection_kind
representation_release
project_scope_ref
```

The validator also proves the package's Context Source Association Set binding against the exact selected bytes:

```text
SHA-256(exact association-set bytes)
association_set_kind
representation_release
consumption_selection_source_sha256
project_scope_ref
```

The package's association-set nested Consumption Selection SHA must also equal the package's direct Consumption Selection SHA.

This is exact opaque-scope correspondence only.

rc05 introduces no scope hierarchy, wildcard, alias, path inference or scope resolver.

## 7. Exact Validated-I Coverage

After accepted upstream validation succeeds, the validator reconstructs `I` from the exact validated Consumption Selection.

It proves:

```text
authority_context_entries domain/order == validated I exactly
```

and rejects semantic duplicate `scaf_authority_id` values.

Therefore:

```text
missing Authority Context Entry
!= explicit Authority Context Entry with zero associations
```

The explicit zero-association entry remains valid and required when its authority is in `I`.

## 8. Association Envelope Fidelity

For each authority `A` in validated `I`, the validator proves:

```text
package association_envelope(A).controlled_association bodies
==
accepted upstream associations(A) exactly
```

The package projection may not add, remove or rewrite:

```text
source_unit_ref
relationship_semantic
relationship_scope_ref
association_provenance
authority_qualification
instance_constraint
```

Package-local `association_handle` is deliberately excluded from upstream relationship identity.

The handle remains a package-local deterministic reference only.

## 9. Package-Wide Association Handle Uniqueness

Each `association_handle` shall be unique across the package.

This is required so that package decisions and provenance resolve deterministically.

The validator does not promote a handle into a new upstream Controlled Source Association identity.

Therefore:

```text
package-local association_handle
!= upstream association identity
```

## 10. Complete Materialization Decision Accounting

For each Authority Context Entry, the validator proves:

```text
Association Envelope handles
==
Materialization Decision handles exactly
```

in the accepted canonical association order.

Therefore every accepted association has exactly one same-authority package decision.

The validator rejects:

```text
missing decision
duplicate decision
cross-entry decision handle
extra decision without accepted association
```

The schema continues to own branch shape:

```text
materialized
not_materialized
```

The source-aware validator proves relationship/accounting correspondence, not new outcome semantics.

## 11. Materialized Context Item Identity and Reference Integrity

The validator proves:

```text
materialized_context_item_id values are unique
all materialized_context_item_refs resolve
no Materialized Context Item is orphaned
```

Package-local item identity remains distinct from Source Identity.

Therefore:

```text
materialized_context_item_id
!= source_identity_ref
!= Source Unit identity
```

rc05 does not infer equivalence merely because two payload references or bytes may later be equal.

## 12. Controlled Provenance Basis Resolution

Every Controlled Provenance Basis is the package-local pair:

```text
(scaf_authority_id, association_handle)
```

The validator proves every pair resolves to one accepted package association projection inside the named Authority Context Entry.

This pair is still not an upstream association identifier.

## 13. Bidirectional Decision / Provenance Correspondence

For every Materialization Decision reference:

```text
decision (authority A, handle H) -> item X
```

item `X` must contain:

```text
Controlled Provenance Basis (A, H)
```

Conversely, every item provenance basis `(A, H)` must correspond to a `materialized` decision for `(A, H)` that references that item.

This prevents unrelated package content from being attached to an association merely through an item reference.

The rule supports multi-association and cross-authority items while preserving every basis independently.

Therefore:

```text
shared item
!= merged authority ownership
```

## 14. Canonical Raw / List Ordering

The rc03 canonical representation established raw/list ordering that the rc04 parsed-instance schema deliberately does not own.

rc05 enforces the accepted policy including:

```text
one YAML document only
no duplicate mapping keys
no aliases / anchors / merge keys
no custom YAML tags
string mapping keys only
canonical quoted string values
UTF-8 + LF
canonical mapping member order
authority_context_entries sorted by scaf_authority_id
association_envelope sorted by accepted semantic association tuple
materialization_decisions in corresponding envelope order
materialized_context_item_refs sorted by exact item ID
materialized_context_items sorted by item ID
controlled_provenance_bases sorted by (authority ID, handle)
inherited basis_refs / authority_basis_refs sorted
```

Ordering is representation determinism, not engineering priority.

## 15. Payload Boundary Remains Reference-Only

The accepted rc03 payload remains:

```text
payload_kind: source_reference
source_identity_ref: <non-empty opaque reference>
```

rc05 does not:

```text
load source bytes into the package
extract fragments
chunk content
summarize content
prove source_reference currentness
resolve remote identities
create a derived-artifact registry
```

The validator validates package/source relationships already declared by accepted inputs; it is not a content materializer or general Source Resolver.

## 16. Runtime Observation Remains Separate

The accepted separation remains:

```text
controlled association truth
!= package materialization truth
!= runtime resolution / materialization observation
```

A load failure, inaccessible source, stale source, supersession observation or consumer runtime issue is not silently converted into:

```text
association deletion
not_applicable
waiver
accepted risk
closure
```

rc05 adds no runtime observation schema or currentness model.

## 17. Engineering Authority Separation

A validator PASS means only:

> the accepted package representation is structurally valid and deterministically consistent with the exact validated upstream package inputs under the rc05 machine-checkable contract.

It does not mean:

```text
Project Design Authority approved the design
source content is sufficient
engineering objective is satisfied
verification passed
compliance is complete
risk is accepted
release is ready
project is closed
```

Likewise:

```text
context presented to AI
!= authority granted to AI
```

## 18. Invalid vs Unresolved

The frozen distinction remains:

```text
Invalid
= machine-verifiable representation/source/package inconsistency

Unresolved
= legitimate engineering question not yet decided
```

Examples of rc05-invalid conditions include wrong bound SHA, mismatched validated-I coverage, non-fidelity Association Envelope, non-resolving package reference, duplicate semantic package identity, and broken decision/provenance correspondence.

Examples of unresolved engineering questions include whether the assembled context is sufficient for a task or whether additional engineering evidence should later be materialized.

The validator shall not classify legitimate unresolved engineering judgment as Invalid solely because it is unresolved.

## 19. Determinism and Engineering Judgment

rc05 owns only machine-determinable facts.

The intended invariant remains:

```text
same exact validated inputs
+
same accepted package bytes
        ↓
same validation result
```

Engineering judgment must remain explicit in controlled project/source/package inputs where the accepted model provides for it.

Therefore:

```text
machine-readable
!= machine-decided
```

## 20. External Source / Licensing Boundary

Controlled association or package materialization does not itself establish:

```text
content-use authorization
redistribution permission
license grant
consumer access authorization
```

rc05 introduces no new direct third-party source incorporation into the canonical package fixture or validator implementation beyond normal declared software dependencies already used by accepted SCAF validators.

This is a framework/source-incorporation boundary, not legal advice.

## 21. Deferred Capabilities

rc05 does not add or authorize:

```text
Controlled Context Package builder / generator
content loader
inline source content
fragment locator / extraction
chunking
summarization / synthesis algorithm
ranking / priority policy
token budget / tokenizer dependency
prompt construction
model adapter / orchestration / persona
repository-wide source discovery
general Source Resolver
Git history traversal
remote fetch
source currentness / supersession model
runtime materialization observation schema
access-control / credential / secret-management system
CI package gate
new authority-registry records
new PAO / FNI
L4 implementation guidance
```

Any such capability requires a new dependency/value assessment.

## 22. Production CLI / API Boundary

Supported public API:

```python
validate_controlled_context_package(
    repo_root,
    package_path=None,
    associations_path=None,
    selection_path=None,
    profile_path=None,
    project_application_path=None,
)
```

Supported CLI selectors:

```text
--package
--associations
--selection
--profile
--project-application
```

There is no production package-schema override selector.

The schema and accepted upstream validators remain repository-owned parts of the reviewed validation chain.

## 23. Regression Coverage

rc05 adds a bounded production-validator regression suite covering the accepted canonical fixture and negative conditions including:

```text
raw duplicate YAML key
YAML anchor
unquoted canonical string
schema-invalid runtime field
wrong Consumption Selection SHA
wrong Context Source Association SHA
invalid upstream Consumption Selection
invalid upstream Context Source Association Set
missing / extra / duplicate Authority Context Entry identity
Association Envelope mismatch
duplicate package association handle
missing / duplicate / cross-entry Materialization Decision
semantic duplicate Materialized Context Item ID
unresolved item reference
orphan item
non-resolving provenance authority / handle
decision reference lacking matching provenance
provenance lacking corresponding materialized decision
non-canonical root / authority / association / decision / item-ref / item / provenance order
CLI default-path validation and absence of schema override
```

The accepted upstream Context Source Association validator remains independently testable through its existing regression suite.

## 24. Current Decision Horizon Closure

rc05 is progression-sufficient when independent review establishes that:

1. the exact rc04 predecessor and expected source delta are correct;
2. frozen/accepted surfaces outside the rc05 package/docs/navigation delta remain unchanged;
3. strict YAML and rc04 schema validation occur before package source-aware proof;
4. the exact bound Context Source Association / Consumption Selection chain passes accepted source-aware validation before package-domain reasoning;
5. exact upstream binding proof passes;
6. Authority Context Entry domain equals validated `I` exactly;
7. Association Envelope fidelity and package-wide handle uniqueness are deterministic;
8. one same-authority decision exists per accepted association;
9. item identity/reference completeness and orphan absence are deterministic;
10. provenance bases resolve and decision/provenance correspondence is bidirectional;
11. canonical raw/list ordering is deterministic;
12. validator PASS remains separate from engineering sufficiency/authority/completion;
13. all bounded regressions and required production checks pass; and
14. deferred builder/content/model/resolver/CI/L4 capabilities remain absent.

A clean rc05 review authorizes only a new dependency/value assessment.

It does not automatically authorize rc06, a builder/generator, content loading, or any later capability.

## 25. Dependency / Value Stop Rule After rc05

After a clean review, SCAF shall ask whether another rc is materially required.

The next assessment shall explicitly consider whether the v0.0.10 milestone is already complete enough to STOP/freeze with:

```text
semantic foundation
+
canonical logical model
+
canonical machine-readable representation
+
parsed-instance schema
+
source-aware validation
```

A builder shall not be introduced merely because construction automation is possible.

The builder becomes justified only if a concrete next capability materially depends on deterministic package construction and the construction policy is sufficiently defined by available evidence.

This applies the frozen v0.0.8 lifecycle-proportional governance rule to SCAF itself.
