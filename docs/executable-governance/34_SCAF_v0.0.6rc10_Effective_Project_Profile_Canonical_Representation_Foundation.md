# SCAF v0.0.6rc10 — Effective Project Profile Canonical Representation Foundation

**Development Release:** v0.0.6rc10  
**Status:** Canonical Representation Foundation / Review Candidate  
**Date:** 2026-08-18  
**Upstream Frozen Baselines:** v0.0.2 L1/L2; v0.0.3 L3; v0.0.4 Executable Governance; v0.0.5 L3 Machine-Readable Traceability  
**Accepted Development Basis:** v0.0.6rc09 Effective Project Profile Semantic Foundation  
**Immediate Predecessor:** v0.0.6rc09

## 1. Decision Purpose

The independent v0.0.6rc09 review returned a clean gate with zero findings:

```text
Critical: 0
Major:    0
Minor:    0
Trivial:  0

V0.0.6RC09 EFFECTIVE PROJECT PROFILE SEMANTIC FOUNDATION GATE: YES
```

rc09 established a deterministic semantic partition for one exact selected project scope over the complete validated Project-Applicable Obligation domain:

```text
applicable
not_applicable
undetermined
no_current_disposition
```

It also established that `no_current_disposition` is profile-only derived absence, not a fourth Project Application applicability token, and that an Effective Project Profile is subordinate derived information rather than engineering/project authority.

rc10 takes the next bounded step: define the first canonical machine-readable YAML representation for that accepted semantic model.

The governing rule remains:

> **The canonical profile representation records a deterministic derived current-state projection. It does not create, approve, replace, or strengthen a Project Application judgment.**

## 2. Scope of rc10

rc10 adds one canonical representation fixture:

```text
examples/effective-project-profile.yaml
```

and defines the serialization contract represented by that fixture.

rc10 does **not** add:

- an Effective Project Profile JSON Schema;
- a profile generator/builder;
- a profile validator;
- a profile API or CLI;
- a persistent profile registry/cache;
- project-scope resolution or hierarchy;
- project-controlled reference resolution;
- automatic applicability inference;
- AI approval of engineering rationale;
- Project Design Authority automation;
- Pattern recommendation or selection;
- implementation/satisfaction/compliance determination;
- verification/evidence/closure determination;
- completion PASS/FAIL;
- AI context packaging;
- CI applicability-completion enforcement;
- code generation;
- new L3 Pattern content;
- L4 guidance;
- Development Context Recovery / `.scaf/work-checkpoint.yaml` state.

A later RC may separately consider schema or executable derivation only after this representation is independently reviewed.

## 3. Representation Identity

The canonical representation release is:

```text
v0.0.6rc10
```

The profile kind token is:

```text
effective_project_profile
```

The accepted YAML fixture begins with:

```yaml
profile_kind: "effective_project_profile"
representation_release: "v0.0.6rc10"
```

The representation release identifies the profile serialization contract. It does not alter the accepted Project Application representation release (`v0.0.6rc04`) and does not create a new applicability vocabulary.

## 4. Canonical Top-Level Model

A canonical rc10 Effective Project Profile YAML document is exactly one YAML document whose root is one mapping containing exactly these six members:

```text
profile_kind
representation_release
scaf_source_release
project_scope_ref
project_application_source_sha256
entries
```

Canonical serialization order is the order shown above.

Canonical physical order exists to make controlled generation, review, diffing, and deterministic serialization straightforward. Physical mapping-member position has no engineering priority or authority meaning.

### 4.1 `profile_kind`

Required exactly once:

```text
profile_kind: effective_project_profile
```

### 4.2 `representation_release`

Required exactly once:

```text
representation_release: v0.0.6rc10
```

### 4.3 `scaf_source_release`

Required exactly once as a non-empty string.

It identifies the SCAF source release whose validated Project-Applicable Obligation population defines the profile domain.

For the current fixture:

```text
scaf_source_release: v0.0.2
```

The representation contract does not define `218` as a permanent profile size. A future source release may have a different validated PAO population.

### 4.4 `project_scope_ref`

Required exactly once as a non-empty opaque string.

For rc10, matching remains exact serialized-string equality only. The field does not imply:

```text
scope existence proof
scope hierarchy
scope alias resolution
scope inheritance
scope authority
```

The current fixture uses:

```text
example:scope:system
```

### 4.5 `project_application_source_sha256`

Required exactly once as a lowercase 64-hex-character SHA-256 value over the exact raw bytes of the selected Project Application YAML input from which the profile was derived.

For the accepted fixture input:

```text
examples/project-application.yaml
SHA-256 = ff9a57b7561d51922796fca8e31a1157ef63a5db03d5cce77500ebb669e8145a
```

This field exists because `no_current_disposition` is dataset-relative. The profile must identify the exact Project Application source snapshot against which absence was observed.

The digest means only:

> these exact source bytes were the Project Application input snapshot for this derived profile.

It does **not** mean:

```text
trusted signer identity
project approval
content correctness
compliance evidence
semantic equivalence to another YAML serialization
```

A byte-level edit, including a comment-only edit, changes the digest. That is intentional snapshot provenance, not a semantic-equivalence mechanism.

### 4.6 `entries`

Required exactly once as a sequence.

The sequence contains exactly one entry for every validated Project-Applicable Obligation in the `scaf_source_release` domain for the selected exact scope.

Framework Normative Invariants are excluded.

For current `v0.0.2`, the accepted PAO domain contains 218 entries. This is the current source inventory, not a cross-release constant.

## 5. Canonical Entry Model

Every profile entry begins with exactly these two members:

```text
scaf_authority_id
profile_state
```

Depending on state, a third member may be required:

```text
project_application_record_id
```

Canonical member order is:

```text
scaf_authority_id
profile_state
project_application_record_id   # only when state requires it
```

### 5.1 `scaf_authority_id`

Required exactly once as a non-empty string.

The ID must resolve, under the profile's `scaf_source_release`, to exactly one validated authority record whose class is:

```text
Project-Applicable Obligation
```

An FNI or nonexistent authority ID cannot be a conformant profile entry.

### 5.2 `profile_state`

Required exactly once and limited to the accepted rc09 profile-state vocabulary:

```text
applicable
not_applicable
undetermined
no_current_disposition
```

These are profile-state tokens. The first three mirror the applicability token of an existing validated current Project Application record. The fourth represents validated current-record absence for the exact PAO/scope pair.

### 5.3 `project_application_record_id`

State-dependent trace field.

For:

```text
applicable
not_applicable
undetermined
```

`project_application_record_id` is required exactly once as a non-empty string and must identify the unique validated current Project Application record for the same exact:

```text
scaf_authority_id
project_scope_ref
```

The record's `applicability` token must equal the profile entry's `profile_state`.

For:

```text
no_current_disposition
```

`project_application_record_id` is prohibited and omitted.

The absence state must not manufacture a synthetic Project Application record identity.

## 6. State-Specific Canonical Shapes

### 6.1 Applicable

```yaml
- scaf_authority_id: "SCAF-AK-001"
  profile_state: "applicable"
  project_application_record_id: "EXAMPLE-PA-001"
```

### 6.2 Not applicable

Canonical shape:

```yaml
- scaf_authority_id: "SCAF-EXAMPLE-PAO"
  profile_state: "not_applicable"
  project_application_record_id: "EXAMPLE-PA-NOT-APPLICABLE"
```

The example above demonstrates shape only; it does not assert that the named illustrative IDs belong to the repository fixture.

### 6.3 Undetermined

Canonical shape:

```yaml
- scaf_authority_id: "SCAF-EXAMPLE-PAO"
  profile_state: "undetermined"
  project_application_record_id: "EXAMPLE-PA-UNDETERMINED"
```

A profile does not copy `unresolved_reason` or `awaiting_refs`; consumers follow the record identity back to the Project Application source.

### 6.4 No current disposition

```yaml
- scaf_authority_id: "SCAF-AK-002"
  profile_state: "no_current_disposition"
```

No `project_application_record_id` is permitted for this state.

## 7. Complete-Domain Contract

A conformant profile contains the complete validated PAO domain for its bound SCAF source release.

Therefore:

```text
entry count = validated PAO domain size D
```

and each PAO ID occurs exactly once.

Entries are canonically ordered by exact serialized `scaf_authority_id` ascending.

The representation must not:

- omit a PAO merely because no current Project Application record exists;
- include an FNI;
- include an unknown authority ID;
- duplicate a PAO entry;
- carry a disposition from another scope;
- infer a state from L3 trace presence, Pattern availability, implementation artifacts, evidence, or reference names.

When the exact current PAO/scope pair has no Project Application record, its entry is still present and is represented as:

```text
no_current_disposition
```

## 8. Partition Invariant

The rc09 semantic invariant remains unchanged:

```text
D = A + N + U + M
```

where:

```text
D = complete validated PAO domain size
A = applicable entries
N = not_applicable entries
U = undetermined entries
M = no_current_disposition entries
```

rc10 deliberately does **not** serialize redundant state-count fields. Counts are deterministic derivatives of `entries` and can be computed by later read/query tooling.

Avoiding redundant serialized counts prevents a second consistency surface where entry states and summary counts could disagree.

For the rc10 fixture:

```text
D = 218
A = 1
N = 0
U = 0
M = 217
```

`M == 0`, if it occurs in another profile, still means only that every PAO has a current recorded disposition for that exact scope in the selected source dataset. It does not mean project completion or compliance.

## 9. Traceability Without Truth Duplication

The profile deliberately does not copy the Project Application record's:

```text
disposition_basis
decision_refs
authority_refs
supporting_refs
unresolved_reason
awaiting_refs
```

For recorded states, the canonical trace surface is only:

```text
project_application_record_id
```

This keeps the Project Application record as the project-side source of the disposition and avoids profile/source divergence.

The profile also does not copy authority titles, normative text, L3 Patterns, trace relations, implementation status, evidence status, or closure status.

## 10. YAML Representation Rules

The canonical rc10 YAML representation uses these bounded rules:

- exactly one YAML document;
- root mapping only;
- only string mapping keys;
- duplicate mapping keys prohibited;
- YAML anchors prohibited;
- YAML aliases prohibited;
- YAML merge keys prohibited;
- custom YAML tags prohibited;
- multi-document streams prohibited;
- YAML null is outside the contract;
- comments are permitted but non-authoritative;
- canonical top-level/member ordering is defined for deterministic serialization;
- entry ordering is exact `scaf_authority_id` ascending;
- duplicate PAO entries are prohibited.

rc10 does not mandate byte-for-byte YAML equivalence across all conformant serializers. A later schema/validator RC may separately make machine-determinable portions executable.

## 11. Canonical Fixture

The canonical fixture is:

```text
examples/effective-project-profile.yaml
```

It is derived from:

```text
examples/project-application.yaml
```

for exact selected scope:

```text
example:scope:system
```

The input fixture is illustrative only and does not assert real SCAF project applicability decisions. Therefore the derived profile fixture is also illustrative only.

The expected current distribution is:

```text
applicable:             1
not_applicable:         0
undetermined:           0
no_current_disposition: 217
Total:                  218
```

`SCAF-AK-001` traces to `EXAMPLE-PA-001`. Every other current v0.0.2 PAO has no exact `example:scope:system` record in the selected fixture and is represented as `no_current_disposition`.

The fixture does not fabricate not-applicable or undetermined records merely to exercise all four states. State-specific canonical shapes are defined normatively in this record and can be exercised by later schema/validator tests using controlled temporary inputs.

## 12. Representation Invalidity Versus Engineering State

A malformed or inconsistent profile representation is not an engineering disposition.

Examples of future machine-determinable representation invalidity include:

```text
missing/duplicate PAO entry
unknown/FNI authority entry
wrong source-release domain
invalid profile_state token
missing record trace for a recorded state
record trace present for no_current_disposition
record trace whose Project Application state does not match
incorrect source snapshot digest
non-canonical ordering where canonical ordering is required
```

By contrast:

```text
undetermined
```

remains a legitimate explicit engineering-unresolved state inherited from a valid current Project Application record.

And:

```text
no_current_disposition
```

remains legitimate derived dataset-relative absence, not an invalid state.

## 13. Authority Boundary

A conformant Effective Project Profile may establish machine-determinable facts such as:

```text
PAO domain membership
exact selected scope string
exact source snapshot digest
current exact-pair record presence/absence
accepted recorded applicability token
profile state partition
record trace identity
```

It shall not decide:

```text
whether applicability is substantively correct
whether not_applicable rationale is adequate
how an undetermined issue should be resolved
whether a missing disposition is acceptable
whether the selected scope is the correct engineering scope
whether Project Design Authority approved a decision
which Pattern should be selected
whether implementation satisfies an obligation
whether evidence is sufficient
whether the project is compliant
whether risk is acceptable
whether the project is complete/release-ready/closed
```

The profile remains subordinate derived information.

## 14. No-Inference Rules

A profile entry state may be derived only from:

```text
validated PAO domain membership
+
validated exact PAO/scope Project Application record presence/state
or validated exact-pair absence
```

It may not be inferred from:

```text
L3 Pattern availability
L2↔L3 trace presence or relation class
other project scopes
scope naming
project reference naming
implementation artifacts
verification evidence
compliance evidence
record absence outside the selected validated dataset
```

No Pattern recommendation/selection or applicability inference is introduced.

## 15. Deliberately Omitted Fields

rc10 deliberately does not serialize:

```text
profile_id
generated_at
generator_version
state_counts
scope_resolution status
project_application_source_path
copied rationale/provenance lists
authority title/text
Pattern recommendations
implementation state
verification/compliance/closure state
```

Reasons include:

- avoid non-deterministic timestamps;
- avoid environment-specific path identity;
- avoid redundant count consistency surfaces;
- avoid duplicating Project Application truth;
- avoid introducing capabilities not accepted by rc09.

A later separately reviewed RC may add a field only if a concrete machine-readable need justifies it without weakening these authority boundaries.

## 16. Future Review Boundary

A later RC may consider an Effective Project Profile schema and/or deterministic generator only after rc10 is accepted.

Such a later executable boundary would need to prove at minimum:

- validated Project Application input ownership;
- validated PAO source-domain ownership;
- same-snapshot consumption where relevant;
- exact scope matching;
- complete PAO-domain coverage;
- exact four-state derivation;
- record-trace consistency;
- source snapshot SHA-256 consistency;
- deterministic entry ordering;
- no engineering-authority transfer.

rc10 does not pre-authorize implementation details for that later boundary.

## 17. Acceptance Conditions

rc10 is acceptable only if independent review confirms all of the following:

1. rc09 semantic meaning is preserved without reinterpretation.
2. The profile representation is subordinate derived data, not new project authority.
3. The six-member top-level representation is deterministic and sufficient for current provenance needs.
4. `project_application_source_sha256` correctly binds exact source bytes without claiming approval/trust.
5. The complete validated PAO domain is represented exactly once per entry.
6. FNI and unknown authority identities are excluded.
7. The four profile-state tokens remain exactly the rc09 states.
8. `project_application_record_id` is required for recorded states and prohibited for `no_current_disposition`.
9. The profile does not duplicate Project Application rationale/provenance truth.
10. `no_current_disposition` remains profile-only and dataset-relative.
11. `undetermined` remains explicit engineering-unresolved state.
12. Exact project scope remains opaque/resolution-neutral.
13. No L3/cross-scope/Pattern/implementation/evidence inference is introduced.
14. No schema/generator/API/CLI/CI/context-package/L4 capability is introduced.
15. Accepted rc07/rc08 and frozen regressions remain unchanged and passing.

## 18. Boundary Statement

v0.0.6rc10 freezes only the first canonical machine-readable representation shape for the accepted rc09 Effective Project Profile semantics.

It does not freeze or implement a generator, schema, validator, query layer, context package, completion gate, or engineering decision engine.

The core distinction remains:

```text
machine-readable representation
!= machine-decided engineering judgment
```
