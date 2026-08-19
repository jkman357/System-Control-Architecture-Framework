# SCAF v0.0.7rc05 — Consumption Selection Source-Aware Validator Foundation

**Development Release:** v0.0.7rc05  
**Status:** Consumption Selection Source-Aware Validator / Review Candidate  
**Date:** 2026-08-19  
**Immediate Predecessor:** v0.0.7rc04 (`d33d426710fdd51e86b2ee746d9d9531ef81bf82`)  
**Accepted Development Basis:** v0.0.7rc01 consumption semantics; v0.0.7rc02 canonical logical model; v0.0.7rc03 canonical YAML representation; v0.0.7rc04 parsed-instance schema  
**Frozen Basis:** v0.0.2 L1/L2; v0.0.3 L3; v0.0.4 Executable Governance; v0.0.5 L3 Machine-Readable Traceability; v0.0.6 Machine-Readable Project Application / Effective Project Profile

## 1. Decision Purpose

The independently reviewed rc04 schema foundation established the parsed-instance structural/state-shape contract for the accepted rc03 Consumption Selection representation while explicitly leaving source-aware facts outside schema-only proof.

The rc04 independent review returned:

```text
Critical: 0
Major:    0
Minor:    0
Trivial:  0

V0.0.7RC04 CONSUMPTION SELECTION SCHEMA FOUNDATION GATE: YES
```

v0.0.7rc05 adds the first executable **Consumption Selection representation/source-aware validator**.

Its purpose is bounded:

> **Prove that one canonical Consumption Selection is structurally valid, bound to one exact validated Effective Project Profile snapshot, reconstructs the accepted selector/set relations correctly, and preserves exact selected-entry source fidelity without transferring engineering authority into the validator.**

A successful result means only machine-determinable representation/source/selection consistency.

It does **not** mean:

```text
engineering applicability is correct
Project Design Authority approved the selection
selected entries are implemented
Pattern choice is correct or complete
verification evidence is sufficient
compliance is established
risk is accepted
release is ready
closure is complete
AI output is approved
```

## 2. Accepted Upstream Semantics Remain Binding

rc05 does not reopen the accepted rc01→rc04 contracts.

The central distinctions remain:

```text
included in context != applicable
excluded from context != not_applicable
omitted != not_applicable
predicate excluded != bounded omitted
undetermined != no_current_disposition
```

The frozen Effective Project Profile vocabulary remains exactly:

```text
applicable
not_applicable
undetermined
no_current_disposition
```

No fifth profile state is introduced by inclusion, omission, predicate exclusion, validation result, or complete/filtered classification.

The accepted set model remains:

```text
D = complete validated source-profile PAO domain
E = predicate-eligible set
I = serialized included set
O = predicate-eligible but bounded-omitted set
X = predicate-excluded set

E = I + O
D = I + O + X
```

with `I`, `O`, and `X` mutually disjoint.

## 3. New Executable Package

rc05 adds:

```text
tools/scaf_consumption_selection_validator/
```

with:

```text
validator.py
README.md
requirements.txt
__init__.py
tests/__init__.py
tests/test_validator.py
```

The supported production module invocation is:

```text
python -m tools.scaf_consumption_selection_validator.validator
```

The production CLI permits only project-side source selectors:

```text
--selection <path>
--profile <path>
--project-application <path>
```

It intentionally exposes no production CLI override for:

```text
repository root
Consumption Selection schema
Effective Project Profile schema
Project Application schema
authority registry
authority schema
canonical normative sources
```

Those sources remain repository-owned by the reviewed validator package.

## 4. Public Programmatic Boundary

The supported programmatic function is:

```python
validate_consumption_selection(
    repo_root,
    selection_path=None,
    profile_path=None,
    project_application_path=None,
)
```

The function owns source capture and validation before source-profile state is consumed.

Callers do not supply:

```text
parsed Consumption Selection objects
parsed Effective Project Profile objects
prebuilt authority indexes
precomputed E/I/O/X sets
caller-created validation reports
cached PASS labels
AI assertions that a source is valid
```

as substitutes for accepted validation.

The returned `ValidationReport` is diagnostic machine output only. It is not an engineering approval object.

## 5. Validation Ownership and Private Snapshot Boundary

rc05 captures the selected bytes before downstream proof:

```text
selected Consumption Selection bytes
selected Effective Project Profile bytes
selected Project Application bytes
repository-owned Consumption Selection schema bytes
repository-owned Effective Project Profile schema bytes
repository-owned Project Application schema bytes
repository-owned authority registry bytes
repository-owned authority schema bytes
repository-owned canonical normative Markdown bytes
```

The selected sources and repository-owned validation sources are then consumed through private temporary snapshots.

The accepted profile proof is executed against the private captured boundary rather than relying on a caller-created parsed profile or an uncaptured validation report.

The intended proof chain is:

```text
Consumption Selection raw bytes
        ↓ private snapshot
rc03 raw-YAML / canonical-order policy
        ↓
rc04 Draft 2020-12 schema

Effective Project Profile raw bytes
        ↓ private snapshot
frozen v0.0.6 source-aware profile validator
        ↓
validated exact source profile

Project Application raw bytes
        ↓ same captured source chain
accepted Project Application proof through profile validation

repository-owned authority/schema/normative sources
        ↓ private validation boundary
frozen authority/source proof through profile validation

validated selection + validated source profile
        ↓
exact profile SHA / provenance binding
        ↓
selector/domain resolution
        ↓
selected-entry fidelity
        ↓
D/E/I/O/X reconstruction
        ↓
bounded-omission proof
        ↓
complete/filtered derivation proof
```

## 6. Consumption Selection Raw-YAML Policy

rc05 makes the accepted rc03 canonical YAML restrictions executable for the supported validator boundary.

The validator rejects:

```text
multiple YAML documents
non-string mapping keys
duplicate mapping keys
YAML anchors
YAML aliases
YAML merge keys
custom YAML tags
unquoted string values in the canonical Consumption Selection representation
```

`bounded_omission.applied` remains a YAML boolean rather than a quoted string.

Comments remain non-authoritative and are not semantic members.

## 7. rc04 Schema Proof

After raw-YAML policy, the parsed Consumption Selection must pass the accepted rc04 schema:

```text
schemas/consumption-selection.schema.json
```

The schema identity remains:

```text
$schema = https://json-schema.org/draft/2020-12/schema
$id     = urn:scaf:schema:consumption-selection:v0.0.7rc04
```

The serialized representation remains:

```text
selection_kind: consumption_selection
representation_release: v0.0.7rc03
```

rc05 does not create a new representation release.

## 8. Canonical Physical Ordering

rc05 validates the accepted deterministic physical ordering that rc04 intentionally could not prove as a parsed-instance schema fact.

The required root member order remains:

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

`source_profile_binding` order remains:

```text
effective_project_profile_source_sha256
scaf_source_release
project_scope_ref
project_application_source_sha256
```

`state_selector` must follow the frozen relative order:

```text
applicable
not_applicable
undetermined
no_current_disposition
```

For `authority_selector.mode: explicit_set`, exact authority IDs must be ascending.

`selected_entries` must be ordered by exact `scaf_authority_id` ascending.

Recorded-state selected-entry member order remains:

```text
scaf_authority_id
profile_state
project_application_record_id
```

Absence-state selected-entry member order remains:

```text
scaf_authority_id
profile_state
```

Ordering has no priority, severity, risk, implementation-sequence, review-sequence, or AI-attention meaning.

## 9. Frozen v0.0.6 Profile Validation Chain

The bound Effective Project Profile is not trusted merely because its SHA-256 matches the Consumption Selection binding.

The exact captured profile must pass the frozen v0.0.6 source-aware profile validation boundary against the same captured Project Application snapshot and captured repository-owned SCAF sources.

Therefore:

```text
profile digest match alone != validated profile
```

and:

```text
caller says profile is valid != validated profile
```

The frozen profile validator remains responsible for the accepted profile representation/source obligations, including Project Application source binding, complete PAO domain, recorded-state trace, and exact-pair absence proof.

rc05 consumes profile state only after that proof passes.

## 10. Exact Source-Profile Binding Proof

After successful profile validation, rc05 proves:

```text
selection.source_profile_binding.effective_project_profile_source_sha256
== SHA-256(exact captured profile bytes)
```

It also requires the serialized binding values:

```text
scaf_source_release
project_scope_ref
project_application_source_sha256
```

to equal the corresponding values in the validated source profile.

The profile SHA-256 and Project Application SHA-256 remain provenance bindings only.

They do not establish:

```text
signer identity
project approval
semantic equivalence
engineering correctness
compliance
verification
release readiness
closure
```

## 11. Exact Scope Preservation

The selection continues to inherit the exact opaque `project_scope_ref` from the validated source profile.

rc05 introduces no second caller-owned scope and no:

```text
scope hierarchy
scope alias
scope inheritance
wildcard scope matching
parent/child carryover
cross-scope inference
scope existence proof
scope correctness proof
```

A different scope requires a separately validated Effective Project Profile for that exact scope.

## 12. Source Domain D

Because the bound Effective Project Profile must first pass the frozen v0.0.6 validator, its entries form the validated source-release-bound PAO domain for the selected exact scope.

rc05 reconstructs:

```text
D = set of exact scaf_authority_id values in the validated source profile
```

For the current accepted fixture:

```text
|D| = 218
```

The number `218` is current frozen-source inventory, not a permanent cross-release validator constant.

Production code derives `D` from the validated source profile rather than from a hard-coded numeric rule.

## 13. State Selector Proof

The rc04 schema already constrains `state_selector` to a duplicate-free subset of the four frozen profile states.

rc05 additionally consumes that selector against the validated profile domain.

The empty state set remains legitimate and deterministically produces zero eligible entries.

A state selector remains a context-selection predicate only. Selecting or excluding a state does not rewrite upstream profile state.

## 14. Authority Selector Proof

For:

```text
authority_selector.mode: all_domain
```

the authority side of the predicate covers all of `D`.

For:

```text
authority_selector.mode: explicit_set
```

every serialized exact `scaf_authority_id` must exist in the validated source-profile domain.

Syntactically valid but unknown/out-of-domain explicit IDs are rejected rather than silently ignored.

rc05 still does not accept:

```text
Pattern ID as authority identity
file path as authority identity
authority title as identity
alias/free-text matching
regex identity
semantic similarity
AI classification
```

## 15. Eligibility E

The eligibility predicate remains exactly the accepted rc02 rule:

```text
E = {
      entry in D
      |
      entry.profile_state is in state_selector
      AND
      entry.scaf_authority_id satisfies authority_selector
    }
```

rc05 does not add an arbitrary expression language or executable user predicate.

No source outside the validated profile plus the two accepted selectors may make an entry eligible.

## 16. Included Set I and Selected-Entry Fidelity

The serialized `selected_entries` sequence is the included set `I`.

Every selected entry must:

```text
resolve to exactly one source-profile entry
be eligible under E
preserve exact scaf_authority_id
preserve exact profile_state
preserve exact project_application_record_id when the source profile carries one
preserve absence of project_application_record_id for no_current_disposition
```

Cross-entry duplicate `scaf_authority_id` values are rejected even if the complete selected-entry objects differ.

A selected-entry projection does not become a second source of profile or Project Application truth.

## 17. Project Application Truth Remains Upstream

rc05 does not copy authoritative Project Application rationale/provenance into the Consumption Selection.

It does not create competing serialized truth for:

```text
disposition_basis
decision_refs
authority_refs
supporting_refs
unresolved_reason
awaiting_refs
```

For recorded states, `project_application_record_id` remains the trace-back identity already accepted by the source profile.

If later context-content assembly wants Project Application rationale or excerpts, that is a separately reviewed source-resolution/content problem.

## 18. Bounded Omission O

rc05 reconstructs:

```text
O = E - I
```

When:

```text
bounded_omission.applied: false
```

the validator requires:

```text
I = E
```

When:

```text
bounded_omission.applied: true
```

the accepted rc02 semantics remain:

```text
I is a subset of E
O = E - I
```

The rc02 wording permits subset equality; therefore `applied: true` with `O = empty` is not newly rejected by rc05. The non-empty descriptive `basis` remains required by the rc04 shape contract.

The validator does not define whether the declared resource bound was a good engineering or product decision.

## 19. Predicate-Excluded Set X

rc05 reconstructs:

```text
X = D - E
```

Membership in `X` means only that the exact entry did not satisfy the declared bounded selector predicate for this selection.

It does not mean:

```text
not_applicable
out of project scope
unimportant
implemented
satisfied
verified
compliant
closed
```

## 20. Set Algebra Proof

The validator reconstructs all accepted sets from the validated source profile and serialized selection inputs:

```text
D
E
I
O = E - I
X = D - E
```

and enforces the accepted relations:

```text
I subset-or-equal E
E = I + O
D = I + O + X
I / O / X mutually disjoint
```

The representation still does not serialize redundant authoritative lists for `E`, `O`, or `X`.

That avoids a second competing truth surface.

## 21. Complete / Filtered Proof

The serialized `selection_class` is not trusted as caller-owned truth.

rc05 derives:

```text
complete
iff I = D and O = empty and X = empty

filtered
otherwise
```

and requires the serialized token to match the derived result.

Therefore an all-domain/all-state predicate with bounded omission is `filtered`, not `complete`.

Likewise a syntactically valid caller-provided `complete` token is rejected if the actual validated set relations are filtered.

## 22. Accepted Fixture Result

For the accepted rc03 fixture, rc05 reconstructs:

```text
|D| = 218
|E| = 3
|I| = 2
|O| = 1
|X| = 215

O = { SCAF-AK-003 }
selection_class = filtered
```

This materially preserves:

```text
predicate excluded != bounded omitted
included != applicable
omitted != not_applicable
excluded != not_applicable
```

The fixture remains unchanged from accepted rc03.

## 23. Production Success Wording

Successful production validation ends with exactly:

```text
CONSUMPTION SELECTION REPRESENTATION/SOURCE RESULT: PASS
```

This wording is deliberately narrower than:

```text
engineering PASS
project approval
compliance PASS
verification PASS
release PASS
closure PASS
```

## 24. Regression Suite

rc05 adds a bounded Consumption Selection validator regression suite.

Author-side completed result:

```text
Consumption Selection source-aware validator: 37 / 37 PASS
```

Coverage includes:

```text
accepted fixture and D/E/I/O/X counts
raw-YAML duplicate/anchor/alias/merge/tag/document/key restrictions
quoted canonical string values
rc04 schema rejection before source proof
canonical root/nested/list ordering
cross-entry authority identity uniqueness
exact profile SHA mismatch
profile provenance mismatch
invalid bound profile after matching digest
unknown explicit authority identity
selected unknown/ineligible entries
selected state/record-trace mismatch
no-omission I == E requirement
applied omission subset semantics
complete/filtered derivation
all-domain filtered selection
zero-eligible selectors
full-domain complete selection
CLI repository-override exclusion
production CLI PASS output
```

The suite is intentionally bounded to the accepted representation/source contract; it does not test deferred context-content or AI behavior.

## 25. Frozen / Accepted Non-Regression Requirement

rc05 must not modify the frozen v0.0.6 baseline or accepted rc01→rc04 representation/schema semantics.

The inherited review-covered baseline remains:

```text
v0.0.6 development suites: 98
inherited frozen suites:    93
combined inherited total:  191
```

The new rc05 suite is additional development validation and does not rewrite the historical frozen `191` inventory.

## 26. Deliberate Exclusions

rc05 does **not** introduce:

```text
Consumption Selection builder/generator
Consumption Selection query/read API beyond validation
persistent selection/context registry/cache/history
profile history/supersession
scope/reference resolver
scope hierarchy/aliases/inheritance
PAO-to-file/document/context-source resolver
context-content record
AI context package
AI prompt format
AI orchestration/model selection
arbitrary predicate language
semantic-similarity selection
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

These remain separately gated future capabilities.

## 27. Engineering Authority Separation

The validator may determine facts such as:

```text
exact input bytes
schema conformance
source digest equality
source provenance equality
selector membership
selected-entry fidelity
D/E/I/O/X set membership
set-algebra consistency
complete/filtered consistency
```

It does not decide:

```text
whether the project should mark a PAO applicable
whether an engineering rationale is adequate
which Pattern/mechanism should be selected
whether implementation is correct
whether evidence is sufficient
whether compliance is achieved
whether risk is acceptable
whether release should proceed
whether work is closed
```

The permanent SCAF distinction remains:

```text
machine-determinable fact
!= engineering judgment
!= Project Design Authority decision
!= verification result
!= compliance result
!= risk acceptance
!= release readiness
!= closure
```

## 28. Invalid / Unresolved / Absence Distinction

rc05 preserves:

```text
Invalid
= machine-verifiable Consumption Selection representation/source inconsistency

Undetermined
= valid current Project Application record with unresolved engineering applicability judgment

No current disposition
= valid profile-level absence of an exact current Project Application record
```

Therefore:

```text
undetermined != invalid
no_current_disposition != invalid
undetermined != no_current_disposition
```

A malformed Consumption Selection does not rewrite upstream engineering state.

## 29. Expected Development Progression

rc05 establishes executable Consumption Selection source validation only.

Possible later progression remains separately gated:

```text
rc05 source-aware Consumption Selection validator
        ↓
possible deterministic Consumption Selection builder/generator
        ↓
possible validated selection query/view boundary
        ↓
separate context-source resolution semantics/model
        ↓
separate context-content representation/validation
        ↓
possible deterministic context assembly
```

This sequence is explanatory, not pre-authorized.

No later stage should be introduced merely because it appears in this progression.

## 30. rc05 Acceptance Criteria

rc05 is acceptable only if independent review confirms all of the following:

1. package/Git lineage starts from committed accepted rc04;
2. frozen v0.0.6 and accepted rc01→rc04 sources remain unchanged except intended navigation;
3. the validator owns raw input capture and chains accepted source validation;
4. raw-YAML restrictions and canonical physical ordering are enforced consistently with rc03;
5. the accepted rc04 schema is used without creating a new representation release;
6. exact bound profile bytes pass frozen v0.0.6 source-aware validation before consumption;
7. exact profile SHA and frozen provenance equality are proved;
8. explicit authority IDs must belong to the validated source-profile domain;
9. eligibility is exactly state-selector AND authority-selector;
10. every selected entry is source-valid, eligible, and preserves exact source state/record trace;
11. cross-entry selected authority IDs are unique;
12. `D/E/I/O/X` are reconstructed from validated source/input truth rather than redundant serialized lists;
13. `bounded_omission.applied:false` requires `I == E`;
14. accepted `applied:true` subset semantics are preserved without inventing a ranking algorithm;
15. serialized complete/filtered classification is proved from actual set relations;
16. `included != applicable`, `excluded/omitted != not_applicable`, `predicate excluded != bounded omitted`, and `undetermined != no_current_disposition` remain intact;
17. Project Application rationale/provenance remains upstream;
18. rc05 validator regressions complete without unexpected skips;
19. inherited accepted/frozen regressions remain clean;
20. production repository-owned validators/integrity remain clean;
21. no deferred context-source/AI/CI/L4/work-checkpoint capability is silently introduced.

A clean rc05 review authorizes only continuation of the controlled v0.0.7 development line. It does not freeze v0.0.7 and does not pre-authorize a builder, context-source resolver, AI context package, CI completion gate, L4, or Development Context Recovery.
