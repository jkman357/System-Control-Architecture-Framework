# SCAF v0.0.7rc03 — Canonical Consumption / Context-Selection Machine-Readable Representation Foundation

**Development Release:** v0.0.7rc03  
**Status:** Canonical Machine-Readable Representation / Review Candidate  
**Date:** 2026-08-18  
**Immediate Predecessor:** v0.0.7rc02 (`c0afc0a7fe4f1419370106dee4a11fe07cbf0a65`)  
**Frozen Basis:** v0.0.2 L1/L2; v0.0.3 L3; v0.0.4 Executable Governance; v0.0.5 L3 Machine-Readable Traceability; v0.0.6 Machine-Readable Project Application / Effective Project Profile

## 1. Decision Purpose

The independently reviewed v0.0.7rc02 logical-model foundation established one canonical Consumption Selection over one validated Effective Project Profile snapshot. It defined exact source binding, bounded state/authority selectors, selected-entry fidelity, bounded omission, and the set relations:

```text
D = I + O + X
E = I + O

I = included
O = predicate-eligible but bounded-omitted
X = predicate-excluded
```

rc02 intentionally remained representation-neutral.

v0.0.7rc03 defines the first canonical machine-readable YAML representation for that accepted logical model. It answers one bounded question:

> How can one Consumption Selection be serialized deterministically without creating new profile state, engineering authority, or a competing copy of upstream Project Application truth?

The governing rule is:

> **The rc03 representation serializes the accepted rc02 selection model only. It shall preserve exact source-profile provenance and selected-entry fidelity while keeping predicate exclusion, bounded omission, and context inclusion separate from Project Application applicability and engineering authority.**

rc03 adds no JSON Schema, source-aware validator, builder/generator, query API, CLI, context-content resolver, AI package, scope resolver, CI completion gate, L4 guidance, or Development Context Recovery mechanism.

## 2. Accepted rc02 Basis

The independent rc02 review returned a clean gate with zero findings:

```text
Critical: 0
Major:    0
Minor:    0
Trivial:  0

V0.0.7RC02 CANONICAL CONSUMPTION / CONTEXT-SELECTION MODEL FOUNDATION GATE: YES
```

The accepted rc01/rc02 constraints remain binding, including:

```text
included in context != applicable
excluded from context != not_applicable

predicate excluded != bounded omitted

undetermined != no_current_disposition

filtered consumption != complete Effective Project Profile

machine-determinable selection fact
!= engineering judgment
!= Project Design Authority decision
```

rc03 may serialize those semantics but may not reopen them.

## 3. Canonical Artifact

rc03 adds:

```text
examples/consumption-selection.yaml
```

The fixture is illustrative and subordinate. It is not a Project Application record, a replacement Effective Project Profile, a Pattern-selection record, an implementation result, verification/compliance evidence, approval, release result, or closure result.

The representation release is:

```text
representation_release: v0.0.7rc03
```

Later schema/validator work may formalize this representation but shall not silently change its accepted semantics. A representation revision requires a separately reviewed representation release.

## 4. Canonical Top-Level Mapping

A serialized Consumption Selection contains exactly these top-level members in this canonical physical order:

```text
selection_kind
representation_release
source_profile_binding
selection_purpose
state_selector
authority_selector
bounded_omission
selected_entries
selection_class
```

Their representation cardinalities are:

| Member | Cardinality | Representation role |
|---|---:|---|
| `selection_kind` | exactly 1 | Record discriminator. |
| `representation_release` | exactly 1 | Representation contract identity. |
| `source_profile_binding` | exactly 1 | Exact consumed profile-byte and frozen provenance binding. |
| `selection_purpose` | exactly 1 | Non-empty non-authoritative descriptive purpose. |
| `state_selector` | exactly 1 | Explicit sequence representing a mathematical subset of the four frozen profile states. |
| `authority_selector` | exactly 1 | `all_domain` or exact `scaf_authority_id` set selector. |
| `bounded_omission` | exactly 1 | Explicit applied/not-applied bounded omission metadata. |
| `selected_entries` | exactly 1 | Sequence containing zero or more exact included source-profile projections. |
| `selection_class` | exactly 1 | Serialized derived class: `complete` or `filtered`. |

Unknown top-level members are outside the rc03 representation.

## 5. Record Discriminator and Representation Release

The discriminator is exactly:

```yaml
selection_kind: "consumption_selection"
```

The representation release is exactly:

```yaml
representation_release: "v0.0.7rc03"
```

These values identify the serialized contract only. They do not establish engineering approval or project status.

## 6. Source Profile Binding Representation

`source_profile_binding` is a mapping with exactly these members in canonical order:

```text
effective_project_profile_source_sha256
scaf_source_release
project_scope_ref
project_application_source_sha256
```

Example:

```yaml
source_profile_binding:
  effective_project_profile_source_sha256: "6d53...74aff"
  scaf_source_release: "v0.0.2"
  project_scope_ref: "example:scope:system"
  project_application_source_sha256: "ff9a...145a"
```

`effective_project_profile_source_sha256` is the lowercase hexadecimal SHA-256 of the exact Effective Project Profile source bytes consumed by the selection. The rc03 fixture binds the exact bytes of `examples/effective-project-profile.yaml`, including its non-authoritative leading comments.

The other three values are copied/recovered from that validated profile and must correspond exactly to it.

These digests and identifiers are provenance only. They do not mean signer identity, approval, semantic equivalence, engineering correctness, compliance, verification, release readiness, or closure.

A later source-aware validator must prove this binding against the exact selected profile bytes through the accepted frozen v0.0.6 validation boundary. rc03 does not perform that proof.

## 7. Selection Purpose Representation

`selection_purpose` is one non-empty YAML string.

Example:

```yaml
selection_purpose: "Illustrative bounded context-selection example over three exact PAO identities."
```

It remains descriptive project/tool metadata only. It may not change profile state, Project Application state, PAO authority, Pattern selection, implementation state, verification/compliance state, risk acceptance, release, or closure.

## 8. State Selector Representation

`state_selector` is a YAML sequence containing zero or more unique values from the frozen Effective Project Profile vocabulary:

```text
applicable
not_applicable
undetermined
no_current_disposition
```

No fifth state exists.

Canonical sequence order, when members are present, follows this fixed frozen-state order:

```text
applicable
not_applicable
undetermined
no_current_disposition
```

Therefore an empty sequence is valid representation of the accepted rc02 empty state set:

```yaml
state_selector: []
```

Physical sequence order exists for deterministic serialization only. It does not imply priority, severity, importance, risk, or review order.

## 9. Authority Selector Representation

`authority_selector` has exactly one of two shapes.

### 9.1 Complete-domain selector

```yaml
authority_selector:
  mode: "all_domain"
```

For `all_domain`, `scaf_authority_ids` is absent.

### 9.2 Explicit exact-ID selector

```yaml
authority_selector:
  mode: "explicit_set"
  scaf_authority_ids:
    - "SCAF-AK-001"
    - "SCAF-AK-002"
```

For `explicit_set`, `scaf_authority_ids` is required and may be an empty sequence. IDs are unique and ordered by exact `scaf_authority_id` ascending.

No Pattern ID, file path, authority title, alias, free text, regular expression, semantic similarity result, or AI classification substitutes for exact authority identity.

A later source-aware validator must reject explicit IDs that are not members of the bound validated source-profile domain rather than silently ignoring them.

## 10. Canonical Eligibility Predicate Is Not Serialized as Code

rc03 does not add a free-form predicate field.

The accepted predicate remains derivable exactly from the two selectors:

```text
E = {
      entry in D
      |
      entry.profile_state is in state_selector
      AND
      entry.scaf_authority_id satisfies authority_selector
    }
```

This deliberately avoids arbitrary expression languages, executable code, regular expressions, semantic similarity, AI classification, scope inference, Pattern inference, artifact-presence inference, or external project logic.

## 11. Bounded Omission Representation

`bounded_omission` has one of two shapes.

Not applied:

```yaml
bounded_omission:
  applied: false
```

When `applied` is `false`, `basis` is absent and accepted rc02 semantics require:

```text
I = E
```

Applied:

```yaml
bounded_omission:
  applied: true
  basis: "Illustrative entry-count bound includes two of three predicate-eligible entries."
```

When `applied` is `true`, `basis` is a non-empty descriptive YAML string and:

```text
I is a subset of E
O = E - I
```

The representation intentionally does not serialize a second authoritative `omitted_entries` list. `O` is derived from the validated source profile, selectors, and selected-entry set.

The `basis` does not define a ranking algorithm, token-budget algorithm, severity model, priority model, or engineering disposition.

## 12. Selected Entries Representation

`selected_entries` is a YAML sequence containing zero or more exact included projections from the bound validated source profile.

Every selected entry begins with:

```text
scaf_authority_id
profile_state
```

For recorded profile states:

```text
applicable
not_applicable
undetermined
```

`project_application_record_id` is required and follows `profile_state` in physical mapping order.

For:

```text
no_current_disposition
```

`project_application_record_id` is absent.

Examples:

```yaml
- scaf_authority_id: "SCAF-AK-001"
  profile_state: "applicable"
  project_application_record_id: "EXAMPLE-PA-001"

- scaf_authority_id: "SCAF-AK-002"
  profile_state: "no_current_disposition"
```

Entries are unique by `scaf_authority_id` and are serialized in exact `scaf_authority_id` ascending order.

The representation does not duplicate Project Application rationale/provenance fields such as `disposition_basis`, `decision_refs`, `authority_refs`, `supporting_refs`, `unresolved_reason`, or `awaiting_refs`.

## 13. Selection Class Representation

`selection_class` is one of:

```text
complete
filtered
```

It serializes the accepted rc02 derived classification only. It is not caller-owned engineering truth.

The accepted derivation remains:

```text
complete
iff I = D and O = empty and X = empty

filtered
otherwise
```

A later validator must recompute and prove the serialized value. rc03 does not trust or validate it executablely.

## 14. No Serialized E, O, or X Truth Lists

The rc02 algebra remains:

```text
D = I + O + X
E = I + O
```

rc03 serializes only the source binding, selector inputs, bounded-omission metadata, included set `I`, and derived `selection_class`.

It deliberately does **not** serialize redundant authoritative lists for:

```text
eligible_entries (E)
omitted_entries (O)
predicate_excluded_entries (X)
```

Given the validated source profile and canonical record, a future validator can reconstruct:

```text
D
E
I
O = E - I
X = D - E
```

Avoiding redundant serialized truth reduces inconsistency surfaces and keeps the source profile authoritative for profile state.

## 15. Canonical Fixture Semantics

The rc03 fixture selects from the exact current `examples/effective-project-profile.yaml` bytes.

Its selector inputs are:

```text
state_selector = { applicable, no_current_disposition }
authority_selector = explicit_set({
  SCAF-AK-001,
  SCAF-AK-002,
  SCAF-AK-003
})
```

The bound profile contains:

```text
SCAF-AK-001 -> applicable -> EXAMPLE-PA-001
SCAF-AK-002 -> no_current_disposition
SCAF-AK-003 -> no_current_disposition
```

Therefore:

```text
|D| = 218
|E| = 3
```

The illustrative bounded omission includes:

```text
I = { SCAF-AK-001, SCAF-AK-002 }
```

so:

```text
O = { SCAF-AK-003 }
|O| = 1
|X| = 215
selection_class = filtered
```

This fixture deliberately exercises three different membership outcomes without creating new profile states:

```text
SCAF-AK-001 -> included / applicable
SCAF-AK-002 -> included / no_current_disposition
SCAF-AK-003 -> bounded-omitted / no_current_disposition
all remaining source entries -> predicate-excluded / source state unchanged
```

In particular:

```text
included != applicable
omitted != not_applicable
excluded != not_applicable
```

## 16. Canonical YAML Restrictions

rc03 defines a bounded canonical YAML subset for this representation:

- one YAML document only;
- mapping keys are strings;
- duplicate mapping keys are not part of the representation;
- YAML anchors/aliases, merge keys, and custom tags are not part of the representation;
- scalar strings are emitted quoted in the canonical fixture;
- `bounded_omission.applied` is a YAML boolean (`true` / `false`);
- canonical mapping-member order is the order defined by this contract;
- `state_selector` follows the fixed frozen-state order;
- explicit authority IDs and selected entries use exact ascending `scaf_authority_id` order;
- comments are non-authoritative and are not semantic members.

A later raw-YAML policy/validator may enforce these physical restrictions. rc03 does not add such a validator.

## 17. Representation Determinism

For the same logical selection and same exact source-profile bytes, canonical serialization is intended to be byte-stable except for non-authoritative comments, if a later generator is separately introduced.

Determinism shall come from:

```text
fixed root mapping order
fixed nested mapping order
fixed frozen-state selector order
exact authority-ID lexical order
exact selected-entry lexical order
fixed scalar token spelling
no timestamps
no environment-specific paths
no random identifiers
```

Physical order is for reproducibility only and does not carry engineering priority or severity.

## 18. Exact Scope and Source Fidelity Remain Frozen

The representation contains no caller-owned second scope selector. `project_scope_ref` exists only inside `source_profile_binding` and is copied from the validated Effective Project Profile.

The representation introduces no scope hierarchy, alias, inheritance, wildcard, parent/child propagation, cross-scope carryover, scope existence proof, or scope correctness proof.

Selected-entry state and conditional `project_application_record_id` remain exact projections from the same bound source profile.

## 19. Context Inclusion / Exclusion Remains Non-Authoritative

The accepted rules remain:

```text
included in context != applicable
excluded from context != not_applicable
```

The rc03 fixture intentionally includes a `no_current_disposition` entry. That is valid because selection membership is orthogonal to profile-state meaning.

Similarly, a future valid record may predicate-exclude or bounded-omit an `applicable` entry without changing it to `not_applicable`, unimportant, satisfied, verified, compliant, or closed.

## 20. Invalid, Undetermined, and Missing Remain Distinct

The representation preserves:

```text
Invalid
= machine-verifiable representation/source inconsistency

Undetermined
= valid recorded unresolved engineering judgment

No current disposition
= valid exact-pair dataset-relative absence in the source profile
```

Therefore:

```text
undetermined != invalid
no_current_disposition != invalid
undetermined != no_current_disposition
```

A malformed future Consumption Selection record may be invalid without changing any upstream engineering state.

## 21. Project Application Truth Remains Upstream

The canonical representation does not copy Project Application rationale/provenance truth into the Consumption Selection.

For recorded states, `project_application_record_id` remains the trace back to the accepted Project Application source.

If a future context assembler needs rationale or supporting references, source resolution and excerpt provenance require separate review. rc03 does not add those fields or a PAO-to-content resolver.

## 22. Machine-Determinable Representation Facts

The following are intended to become machine-verifiable in a later validation stage:

```text
record discriminator/release
root/member shape
source-profile SHA lexical form and exact-byte correspondence
provenance equality with validated source profile
selector token vocabulary and ordering
explicit authority-domain membership
eligibility predicate reconstruction
selected-entry eligibility and source fidelity
bounded-omission consistency
D/E/I/O/X set relations
complete/filtered classification consistency
canonical ordering
raw-YAML restrictions
```

Those facts remain distinct from engineering judgment and Project Design Authority decisions.

## 23. Engineering Authority Remains Outside the Representation

A syntactically or source-conformant Consumption Selection does not establish:

```text
applicability correctness
adequacy of Project Application rationale
Pattern/mechanism choice
implementation correctness or completeness
verification/evidence sufficiency
compliance
risk acceptance
release readiness
closure
AI approval
```

The representation records subordinate selection facts only.

## 24. Deliberately Not Solved in rc03

rc03 does not introduce:

```text
Consumption Selection JSON Schema
raw-YAML validator
source-aware Consumption Selection validator
selection builder/generator
selection read/query API
CLI
persistent consumption/context registry/cache/history
profile history/supersession
project-scope/reference resolver or hierarchy
PAO-to-file/document/context-source resolver
context content record
AI context package
AI prompt format or orchestration/model selection
arbitrary predicate language
semantic similarity selection
priority/ranking/severity model
automatic applicability inference
Pattern recommendation/selection
AI approval / Project Design Authority automation
CI applicability-completion enforcement
implementation/compliance/verification/closure determination
profile-driven code generation
new L3 tranche / M3 / M4
L4 guidance
Development Context Recovery / .scaf/work-checkpoint.yaml
external-trust-model expansion
```

Absence of these capabilities is intentional and is not a defect in rc03.

## 25. Expected Future Progression

If rc03 is accepted, possible later separately reviewed stages include:

```text
accepted consumption semantics
        ↓
accepted canonical logical model
        ↓
accepted canonical machine-readable representation
        ↓
parsed-instance schema
        ↓
source-aware Consumption Selection validator
        ↓
deterministic selection builder / validated query
        ↓
separately governed context-source resolution
        ↓
separately governed context assembly
```

This progression is explanatory only. rc03 does not pre-authorize any later stage.

## 26. Engineering Problem Solved

Before rc03, the Consumption Selection model was precise but representation-neutral. Different tools or AI workflows could serialize the same logical selection differently, increasing ambiguity before executable validation could be introduced.

rc03 solves that bounded problem by defining one deterministic YAML shape and one illustrative source-bound fixture while preserving the accepted semantic and authority boundaries.

## 27. What rc03 Intentionally Does Not Solve

rc03 does not yet prove that a Consumption Selection is valid. It does not validate the bound profile SHA, recompute eligibility/omission sets, reject malformed YAML executablely, or build the record automatically.

Those belong to later schema/validator/builder stages after this representation itself is independently reviewed.

## 28. Review Gate Intent

The rc03 review should determine whether:

1. the YAML representation faithfully serializes the accepted rc02 logical model;
2. the exact source-profile binding is sufficient without assigning trust/approval meaning to hashes;
3. selectors preserve the frozen four-state/exact-authority semantics;
4. omission is explicit without duplicating redundant O/X truth lists;
5. selected entries preserve source identity/state/record trace exactly;
6. the illustrative fixture materially satisfies `D = I + O + X` and `E = I + O`;
7. complete/filtered classification is still derived rather than an engineering state;
8. canonical ordering is deterministic without priority/severity meaning;
9. Project Application rationale/provenance remains upstream;
10. frozen v0.0.6 and accepted rc01/rc02 boundaries remain unchanged;
11. no deferred schema/validator/builder/context-source/AI/CI/L4/work-checkpoint capability has been introduced.

A clean rc03 review authorizes only continuation of the controlled v0.0.7 development line. It does not freeze v0.0.7 and does not pre-authorize the next stage.
