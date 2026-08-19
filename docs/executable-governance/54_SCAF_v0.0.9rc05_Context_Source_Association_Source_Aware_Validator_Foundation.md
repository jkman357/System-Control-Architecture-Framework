# SCAF v0.0.9rc05 — Context Source Association Source-Aware Validator Foundation

**Development Release:** v0.0.9rc05  
**Status:** Context Source Association Source-Aware Validator Foundation / Review Candidate  
**Date:** 2026-08-19  
**Immediate Predecessor:** accepted v0.0.9rc04 (`276538253349a84f87ddf57807ded5f3e518860c`)  
**Frozen Basis:** v0.0.2 L1/L2; v0.0.3 L3; v0.0.4 Executable Governance; v0.0.5 L3 Machine-Readable Traceability; v0.0.6 Project Application / Effective Project Profile; v0.0.7 Consumption Selection; v0.0.8 Lifecycle-Proportional Governance

## 1. Decision Purpose

The accepted v0.0.9 chain now contains:

```text
rc01  Context Source Resolution semantics
  ↓
rc02  canonical representation-neutral logical model
  ↓
rc03  canonical deterministic YAML representation
  ↓
rc04  JSON Schema structural contract
```

The rc04 independent review returned clean `PASS / GATE YES` with zero findings and zero blocking review-evidence limitations.

The post-rc04 dependency/value assessment identified one remaining machine-determinable gap before any resolver decision can be made responsibly: schema validity proves only parsed-instance structure. It does not prove that the association set agrees with the exact upstream Consumption Selection or with repository-local source facts explicitly referenced by the representation.

The Current Decision Horizon for rc05 is therefore:

> **Provide one repository-owned production source-aware validator that proves deterministic Context Source Association consistency against the exact validated Consumption Selection and explicitly referenced repository-local source bytes, without becoming a general source resolver or engineering-judgment authority.**

## 2. Engineering Problem

Without rc05, a structurally valid Context Source Association artifact may still be source-inconsistent. Examples include:

```text
recorded Consumption Selection SHA does not match the selected bytes
Authority Source Entry coverage differs from validated I
one authority is represented twice
one Source Unit identity is duplicated under different local IDs
association references a Source Unit not present in the catalog
catalog contains Source Units unused by any controlled association
the same semantic association is asserted twice with different provenance
canonical semantic ordering is violated
an explicit SHA-256 Instance Constraint does not match the referenced repository source bytes
```

These conditions are deterministic and should not remain dependent on reviewer interpretation or per-tool reimplementation.

## 3. Governing Validation Boundary

rc05 preserves the three-level ownership separation:

```text
parsed-instance structural validity
!= source-aware consistency
!= engineering correctness
```

The rc05 validator owns the first two machine-determinable layers needed for its accepted inputs:

```text
Context Source Association bytes
        ↓
strict YAML / canonical raw-representation policy
        ↓
rc04 structural schema
        ↓
exact Consumption Selection binding
        ↓
accepted source-aware Consumption Selection validation
        ↓
validated included domain I
        ↓
association-set source-aware consistency
        ↓
PASS / INVALID
```

A PASS is not an engineering approval.

## 4. Production Artifact

rc05 adds:

```text
tools/scaf_context_source_association_validator/
```

Primary executable entry point:

```text
python -m tools.scaf_context_source_association_validator.validator
```

Default repository-owned fixture inputs are:

```text
examples/context-source-associations.yaml
examples/consumption-selection.yaml
examples/effective-project-profile.yaml
examples/project-application.yaml
```

Project-side input paths may be selected with:

```text
--associations
--selection
--profile
--project-application
```

The repository-owned rc04 association schema and existing SCAF validation sources are not exposed as production CLI override points.

## 5. Validated-Input Ownership

The validator does not trust serialized `I` membership because the Context Source Association representation does not own applicability or selection truth.

It validates the exact bound Consumption Selection through the accepted v0.0.7 source-aware validator before reconstructing the selected domain.

The chain is:

```text
exact Consumption Selection bytes
        ↓
accepted Consumption Selection source-aware validation PASS
        ↓
selected_entries
        ↓
validated I
        ↓
Context Source Association coverage proof
```

If upstream validation fails, downstream association-domain proof stops.

## 6. Exact Selection Binding Proof

The validator captures the exact Consumption Selection bytes selected for validation and proves:

```text
SHA-256(exact selection bytes)
== source_selection_binding.consumption_selection_source_sha256
```

It also proves the recorded:

```text
selection_kind
selection_representation_release
project_scope_ref
```

match the same validated Consumption Selection snapshot.

This preserves exact opaque scope. No scope hierarchy, alias, wildcard, parent/child propagation, path inference or scope resolver is introduced.

## 7. Complete Included-Domain Coverage

After upstream validation succeeds, the validator reconstructs `I` from the exact validated Consumption Selection.

It proves:

```text
authority_source_entries domain == validated I exactly
```

and detects duplicate authority identities.

Therefore:

```text
missing Authority Source Entry
!= explicit Authority Source Entry with associations: []
```

The accepted explicit zero-association representation remains valid.

## 8. Source Unit Catalog Consistency

The validator proves deterministic catalog properties that the rc04 schema cannot establish semantically:

```text
source_unit_id values are unique
source_identity_ref values are unique
every association source_unit_ref resolves to one catalog Source Unit
no Source Unit is unused by all controlled associations
```

This is catalog/reference consistency only.

It does not prove:

```text
source authority
source currentness
source completeness
source engineering correctness
obligation satisfaction
```

## 9. Semantic Association Uniqueness

The accepted rc03/rc04 representation treats one Controlled Source Association as atomic.

rc05 uses the accepted semantic identity tuple:

```text
source_unit_ref
relationship_semantic
relationship_scope_ref
authority_qualification if present
instance_constraint if present
```

Association provenance is not part of semantic relationship identity.

Therefore two otherwise identical relationship assertions do not become two different controlled truths merely because their provenance differs.

The validator rejects duplicate semantic associations.

## 10. Canonical Raw-Representation Policy

The production validator owns deterministic raw-representation requirements not expressible as the rc04 parsed-instance schema, including:

```text
one YAML document only
no aliases
no anchors
no merge keys
no custom YAML tags
string mapping keys only
no duplicate mapping keys
canonical string quoting
canonical mapping field order
Source Units sorted by source_unit_id
Authority Source Entries sorted by scaf_authority_id
associations sorted by the accepted semantic tuple
provenance basis_refs sorted
Authority Qualification basis refs sorted
```

The purpose is byte-stable, implementation-consistent tooling, not stylistic preference.

## 11. Bounded Repository-Local Instance Proof

rc03 intentionally left `source_identity_ref` opaque and did not define a general resolver.

rc05 still does not create one.

For the narrow case where an association contains an explicit SHA-256 `instance_constraint`, rc05 supports one bounded repository-local proof convention already used by the accepted canonical fixture:

```text
repo:<repository-relative POSIX path>
```

Under that bounded validator boundary only, rc05 may map the explicit identity directly to a path inside the selected repository root and prove:

```text
SHA-256(exact referenced repository bytes)
== instance_constraint.value
```

The validator rejects path traversal, absolute paths, backslash-based path reinterpretation, repository escape, and unsupported identity forms when an exact instance constraint requires proof.

This capability means only:

```text
explicit repository-local identity + exact constraint
→ deterministic byte proof
```

It does **not** mean:

```text
repository scan
candidate discovery
Git history traversal
URI fetching
external acquisition
semantic source search
source-currentness decision
supersession decision
```

## 12. Two-Plane Invariant

The accepted invariant remains unchanged:

```text
controlled association truth
!= runtime resolution observation
```

rc05 does not add or persist runtime states such as:

```text
missing
unresolvable
stale
superseded
currentness
resolved instance
constraint-match status
resolver timestamp
```

A validation failure caused by inability to prove an explicit current instance constraint is a validator result for the evaluated input boundary. It is not persisted as new controlled association truth.

## 13. Discovery Boundary

The validator consumes declared controlled associations only.

It does not search for candidate sources and does not infer associations from:

```text
filename similarity
text mention
semantic similarity
repository proximity
Git history
code-reference search
```

The accepted rule remains:

```text
discovered candidate != controlled association
```

## 14. Authority and Engineering-Judgment Boundary

A validator PASS does not establish:

```text
that an association was a good engineering decision
that a Source Unit is authoritative beyond recorded/existing authority semantics
that a project decision is correct
that implementation satisfies an obligation
that a test has executed
that evidence is sufficient
that compliance has been achieved
that risk is acceptable
that a release is ready
that an item is closed
```

Those remain owned by the frozen Authority Kernel and applicable project/external authorities.

The validator produces machine facts, not engineering judgment.

## 15. Failure Semantics

rc05 preserves:

```text
INVALID
= machine-verifiable representation/source inconsistency
```

It does not redefine legitimate engineering `undetermined` or unresolved conditions.

A validator failure does not automatically mean:

```text
not applicable
waived
unsafe
noncompliant
rejected design
closed
```

It means the evaluated association artifact cannot be accepted as source-consistent under the validator's defined deterministic boundary.

## 16. Public API Boundary

The supported programmatic API is:

```python
validate_context_source_associations(
    repo_root,
    associations_path=None,
    selection_path=None,
    profile_path=None,
    project_application_path=None,
)
```

The validator returns a `ValidationReport` with precise error records and bounded status facts.

The CLI and programmatic API share the same validation-owning path.

## 17. Deliberate Non-Goals

rc05 does not add:

```text
a general Source Resolver
filesystem source discovery
Git history traversal
external URI/network fetching
candidate-source discovery
semantic similarity mapping
runtime Resolution Observation representation
source currentness/supersession policy
content extraction
fragment/chunk loading
ranking / priority / token budget
AI prompt/context assembly
model orchestration
CI gate integration
new authority-registry entries
new PAO/FNI
L4 implementation guidance
```

## 18. External Pattern / Licensing Boundary

No third-party source code, prompt, schema body, documentation passage, or example content is incorporated into rc05.

External projects may continue to be studied for abstract design patterns. Direct incorporation remains separately gated by license, copyright, attribution/NOTICE, redistribution, patent and trademark review as applicable.

## 19. Verification Horizon

Because rc05 introduces a new executable validator, verification should cover more than documentation-only bounded checks.

Required rc05 evidence includes:

```text
new rc05 validator test suite PASS
accepted canonical fixture PASS
bounded invalid-condition cases PASS
six repository-owned production validators/integrity checks PASS
existing accepted/frozen regression suites PASS unless an explicit evidence limitation is documented
```

This is justified executable-change verification, not ritual completeness.

## 20. Progression Boundary

A clean rc05 review does not automatically authorize a resolver or rc06.

After review, SCAF shall perform a new dependency/value assessment asking whether a real consumer now requires deterministic source-instance resolution beyond the bounded validator proof already provided.

Possible outcomes are deliberately open:

```text
CONTINUE
→ a separately justified resolver/current-source capability is materially required

STOP
→ controlled mapping + source-aware validation is sufficient for the current milestone
```

No resolver is pre-authorized by rc05.
