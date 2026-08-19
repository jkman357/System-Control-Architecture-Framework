# SCAF v0.0.7rc07 — Consumption Selection Milestone Consolidation and Freeze Candidate

**Development Release:** v0.0.7rc07  
**Status:** Consumption Selection Milestone Consolidation / Freeze Candidate  
**Date:** 2026-08-19  
**Immediate Predecessor:** v0.0.7rc06 (`fb4cf493bc5782bfea57aea4de5321d5e73bff30`)  
**Frozen Basis:** v0.0.2 L1/L2; v0.0.3 L3; v0.0.4 Executable Governance; v0.0.5 L3 Machine-Readable Traceability; v0.0.6 Machine-Readable Project Application / Effective Project Profile

## 1. Decision Purpose

v0.0.7rc01 through v0.0.7rc06 established a bounded, independently reviewed Consumption Selection chain over one validated Effective Project Profile.

The chain now covers:

```text
validated Effective Project Profile
        ↓
consumption semantics
        ↓
canonical logical selection model
        ↓
canonical YAML representation
        ↓
parsed-instance JSON Schema
        ↓
source-aware validation
        ↓
deterministic validated construction
```

The remaining question for the current milestone is not another executable feature. It is whether the accepted rc01→rc06 chain is coherent enough to define a reviewable freeze-candidate boundary before SCAF enters the materially different problem of context-source resolution and context assembly.

v0.0.7rc07 therefore adds **no new semantic or executable capability**. It consolidates the accepted milestone, review history, test inventory, authority boundaries, and deferred capabilities into one explicit freeze-candidate record.

A clean rc07 review may establish **freeze eligibility only**. Formal `v0.0.7` freeze still requires a separate explicit governance decision.

## 2. Accepted Development Chain

The accepted dependency chain entering rc07 is:

```text
formal frozen v0.0.6
Machine-Readable Project Application / Effective Project Profile
        ↓
v0.0.7rc01
Effective Project Profile Consumption Semantic Foundation
        ↓
v0.0.7rc02
Canonical Consumption / Context-Selection Logical Model
        ↓
v0.0.7rc03
Canonical Consumption Selection YAML Representation
        ↓
v0.0.7rc04
Consumption Selection JSON Schema Foundation
        ↓
v0.0.7rc05
Consumption Selection Source-Aware Validator
        ↓
v0.0.7rc06
Deterministic Consumption Selection Builder
        ↓
v0.0.7rc07
Milestone Consolidation / Freeze Candidate
```

Each executable stage consumes the accepted boundary below it rather than silently redefining it.

## 3. Independent Review History

Every accepted v0.0.7 development stage entering rc07 has a clean independent review:

```text
rc01  PASS / GATE YES   0 Critical / 0 Major / 0 Minor / 0 Trivial
rc02  PASS / GATE YES   0 Critical / 0 Major / 0 Minor / 0 Trivial
rc03  PASS / GATE YES   0 Critical / 0 Major / 0 Minor / 0 Trivial
rc04  PASS / GATE YES   0 Critical / 0 Major / 0 Minor / 0 Trivial
rc05  PASS / GATE YES   0 Critical / 0 Major / 0 Minor / 0 Trivial
rc06  PASS / GATE YES   0 Critical / 0 Major / 0 Minor / 0 Trivial
```

No accepted v0.0.7 review finding is open entering rc07.

The rc06 final gate was:

```text
V0.0.7RC06 DETERMINISTIC CONSUMPTION SELECTION BUILDER FOUNDATION GATE: YES
```

That gate authorizes continuation only. It did not freeze v0.0.7 and did not pre-authorize context-source resolution, AI context assembly, CI completion enforcement, L4 guidance, or Development Context Recovery.

## 4. Milestone Scope

The proposed v0.0.7 milestone is bounded to **machine-readable, source-aware, deterministic Consumption Selection** over one exact validated Effective Project Profile.

It answers:

```text
Which exact validated profile snapshot is being consumed?
Which frozen profile states are eligible?
Which exact PAO authorities are eligible?
Which eligible entries are included?
Which eligible entries are explicitly bounded-omitted?
Which entries are predicate-excluded?
Is the result complete or filtered?
Can every included entry be traced exactly to source profile state?
Can the selection be validated and constructed deterministically?
```

It does **not** answer:

```text
Which Markdown/code/test/evidence artifacts should be loaded for each selected PAO?
Which Pattern should a project use?
Which context item is more important?
How should a token budget rank or truncate content?
Whether engineering applicability is correct?
Whether implementation is complete?
Whether verification/compliance is satisfied?
Whether risk is accepted?
Whether a release is ready?
Whether work is closed?
```

Those remain separately gated problems.

## 5. Accepted Consumption Semantic Boundary

The accepted rc01 semantics remain mandatory throughout the milestone:

```text
included in context != applicable
excluded from context != not_applicable
omitted != not_applicable
predicate excluded != bounded omitted
undetermined != no_current_disposition
```

The frozen Effective Project Profile state vocabulary remains exactly:

```text
applicable
not_applicable
undetermined
no_current_disposition
```

Consumption Selection introduces no fifth profile state.

Selection membership and engineering applicability are orthogonal dimensions. A valid selection may therefore include a `not_applicable` or `no_current_disposition` entry when the declared deterministic selector asks for that state, and it may exclude an `applicable` entry when the selector does not request it.

## 6. Accepted Canonical Set Model

The accepted logical model remains:

```text
D = complete validated source-profile domain
E = predicate-eligible set
I = included set
O = predicate-eligible but bounded-omitted set
X = predicate-excluded set

E = I + O
D = I + O + X
```

`I`, `O`, and `X` remain mutually disjoint.

Eligibility remains exactly:

```text
profile_state ∈ state_selector
AND
scaf_authority_id satisfies authority_selector
```

No arbitrary predicate language, semantic similarity, Pattern inference, file-presence inference, scope hierarchy, or AI classifier is part of the accepted selection predicate.

## 7. Accepted Representation

The accepted canonical serialized artifact remains the rc03 representation:

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

with:

```text
selection_kind: consumption_selection
representation_release: v0.0.7rc03
```

The representation binds the exact Effective Project Profile source bytes and preserves:

```text
effective_project_profile_source_sha256
scaf_source_release
project_scope_ref
project_application_source_sha256
```

Those are provenance bindings only. They do not establish signer identity, approval, engineering correctness, compliance, verification, release readiness, or closure.

The representation deliberately does not serialize redundant authoritative `E`, `O`, or `X` lists. Those sets remain reconstructable from the validated source profile, canonical selectors, and selected entries.

## 8. Accepted Parsed-Instance Schema

The accepted schema remains:

```text
schemas/consumption-selection.schema.json
```

with:

```text
$schema = https://json-schema.org/draft/2020-12/schema
$id     = urn:scaf:schema:consumption-selection:v0.0.7rc04
```

It formalizes the accepted rc03 representation and therefore continues to constrain:

```text
representation_release: v0.0.7rc03
```

Schema conformance proves parsed-instance structural/state-shape consistency only.

It does not independently prove source-profile validity, actual digest correspondence, authority-domain membership, selected-entry source fidelity, `D/E/I/O/X` algebra, bounded-omission consistency, physical YAML policy, or engineering authority.

## 9. Accepted Source-Aware Validator

The accepted rc05 validator remains:

```text
tools/scaf_consumption_selection_validator/
```

Supported public boundary:

```python
validate_consumption_selection(
    repo_root,
    selection_path=None,
    profile_path=None,
    project_application_path=None,
)
```

Supported production CLI inputs remain limited to:

```text
--selection
--profile
--project-application
```

The validator owns or chains:

```text
Consumption Selection source capture
raw-YAML / canonical physical policy
rc04 schema validation
exact bound Effective Project Profile capture
frozen v0.0.6 profile source-aware validation
exact source-profile SHA/provenance correspondence
exact source-profile domain D
state/authority selector proof
selected-entry source fidelity
D/E/I/O/X reconstruction
bounded-omission consistency
complete/filtered derivation
```

Accepted success wording remains:

```text
CONSUMPTION SELECTION REPRESENTATION/SOURCE RESULT: PASS
```

That result is not engineering approval, compliance, verification, risk acceptance, release readiness, or closure.

## 10. Accepted Deterministic Builder

The accepted rc06 builder remains:

```text
tools/scaf_consumption_selection_builder/
```

Supported public API:

```python
build_consumption_selection(
    repo_root,
    selection_purpose,
    state_selector=(),
    *,
    authority_mode="all_domain",
    authority_ids=(),
    omitted_authority_ids=(),
    omission_basis=None,
    profile_path=None,
    project_application_path=None,
) -> bytes
```

The builder consumes source-profile state only after frozen source-aware profile validation and constructs only from explicit bounded inputs.

It supports bounded omission only through exact caller-declared predicate-eligible `scaf_authority_id` values. It adds no ranking, token-budget, priority, severity, semantic-similarity, or AI selection algorithm.

Every successful generated result must pass accepted rc05 source-aware validation against the same captured source boundary before return or stdout emission.

The builder preserves the accepted rc03 representation release and does not create a new serialization contract.

## 11. Exact-Scope Boundary

Consumption Selection inherits the exact opaque `project_scope_ref` from its validated source profile.

The milestone defines no:

```text
scope hierarchy
scope alias
scope inheritance
wildcard scope
parent/child propagation
cross-scope carryover
scope resolver
scope correctness proof
```

A different scope requires a separately validated Effective Project Profile for that exact scope.

## 12. Project Application Truth Remains Upstream

Consumption Selection does not create a competing authoritative Project Application truth surface.

Selected recorded states preserve only the accepted trace:

```text
scaf_authority_id
profile_state
project_application_record_id
```

For `no_current_disposition`, the Project Application record ID remains absent.

Authoritative Project Application rationale/provenance remains upstream. Consumption Selection does not duplicate authoritative copies of:

```text
disposition_basis
decision_refs
authority_refs
supporting_refs
unresolved_reason
awaiting_refs
```

## 13. Machine-Determinable Fact Versus Engineering Authority

The milestone preserves the framework-wide distinction:

```text
machine-determinable fact
!= engineering judgment
!= Project Design Authority decision
!= implementation result
!= verification result
!= compliance result
!= risk acceptance
!= release readiness
!= closure
```

Machine-determinable facts in this milestone include source identity, schema/representation consistency, exact selector membership, deterministic set reconstruction, exact omission membership, source-entry fidelity, and complete/filtered classification.

Engineering ownership remains outside those proofs.

## 14. Accepted Regression Inventory

The rc06 independent review completed:

```text
rc06 Consumption Selection builder:   34 / 34 PASS
rc05 Consumption Selection validator: 37 / 37 PASS
historical accepted/frozen baseline: 191 / 191 PASS
                                      ------------
total rc06 review execution:         262 tests
unexpected skips:                       0
```

The historical frozen baseline remains `191 / 191`; it is not redefined as 262.

The 191-test inherited baseline remains:

```text
Project Application validator         21
Project Application views/query       22
Effective Project Profile validator   30
Effective Project Profile generator   25
                                     ---
v0.0.6 development subtotal           98

SCAF authority validator               8
Frozen release integrity               9
External pin                           11
CI gate                                13
L3 trace validator                     24
L3 trace views/query                   28
                                     ---
inherited frozen subtotal              93

combined historical baseline          191
```

## 15. Accepted Production Validation State

The accepted repository-owned production validation chain remains:

```text
python -m tools.scaf_validator.validator
python -m tools.scaf_trace_validator.validator
python -m tools.scaf_release_integrity.checker
python -m tools.scaf_project_application_validator.validator
python -m tools.scaf_effective_project_profile_validator.validator
python -m tools.scaf_consumption_selection_validator.validator
```

Stable current inventories remain:

```text
Authority records: 294
PAO:               218
FNI:                76
L3 Patterns:         12
L3 Relations:       119
```

The accepted default Consumption Selection fixture remains:

```text
D = 218
E = 3
I = 2
O = 1
X = 215
O = { SCAF-AK-003 }
Errors: 0
CONSUMPTION SELECTION REPRESENTATION/SOURCE RESULT: PASS
```

Fresh deterministic Effective Project Profile generation remains expected to produce:

```text
SHA-256:
6f6485077022f3686064876b0891ff45c6f4e4f69a81ab4bb557d6b7a09c3433

representation_release: v0.0.6rc10
entries: 218
applicable: 1
not_applicable: 0
undetermined: 0
no_current_disposition: 217
```

and pass accepted rc12 source-aware validation.

Fixture-equivalent fresh Consumption Selection construction remains expected to produce:

```text
SHA-256:
e23531f2e8b3ae8052cf5cbf5b3e80115ef53837a0831afbc2fe160a982dbdc2
```

and be byte-identical to the accepted rc03 fixture after removing only leading non-authoritative comments/blank lines, then pass rc05 with `218/3/2/1/215`.

## 16. External Production Trust Boundary

The repository-external production trust bundle was not supplied in the accepted rc01→rc06 independent review inputs.

Therefore actual production external-trust execution remains:

```text
NOT INDEPENDENTLY VERIFIED
```

Passing frozen external-pin and CI-gate unit tests is not represented as execution of that unavailable production bundle.

This is not a v0.0.7 finding because the v0.0.7 Consumption Selection line does not modify the frozen external-trust implementation or production trust-set boundary.

## 17. Freeze-Candidate Boundary

A clean rc07 review should establish only that the accepted Consumption Selection milestone is coherent enough to be eligible for a separate formal freeze decision.

The proposed freeze-candidate boundary is:

```text
Effective Project Profile consumption semantics
+ canonical Consumption Selection logical model
+ canonical YAML representation
+ parsed-instance JSON Schema
+ source-aware Consumption Selection validation
+ deterministic validated Consumption Selection construction
```

This candidate does not reopen or redefine frozen v0.0.6.

Formal freeze is not automatic. A subsequent explicit governance decision is required to create `v0.0.7` as an immutable baseline.

## 18. Deliberately Deferred Capabilities

The following remain outside the v0.0.7 freeze-candidate scope:

```text
PAO-to-file/document/context-source resolution
context-content records
AI context package
AI prompt format
AI orchestration / model selection
semantic-similarity context selection
ranking / priority / severity policy
token-budget calculation or automated truncation policy
scope/reference resolver
scope hierarchy / aliases / inheritance
profile history / supersession
Consumption Selection history / persistent registry / cache
automatic applicability inference
Pattern recommendation / selection
AI approval / Project Design Authority automation
CI applicability-completion enforcement
implementation/compliance/verification/closure determination
profile-driven code generation
new L3 tranche / M3 / M4
L4 implementation / verification guidance
Development Context Recovery / .scaf/work-checkpoint.yaml
external-trust-model expansion
```

These are not defects in rc07. They are separate dependency/value-selected stages.

## 19. Why Context-Source Resolution Is Not Part of This Milestone

Consumption Selection answers **which PAO/profile entries are selected**.

Context-source resolution would answer a different authority question:

```text
selected PAO
    ↓
which normative Markdown?
which L3 Pattern documents?
which project architecture documents?
which source code?
which tests/evidence?
which Project Application rationale excerpts?
which issues/tickets or other project sources?
```

That stage introduces new source ownership, resolver semantics, content provenance, omission behavior, and potentially AI-context packaging rules.

Mixing that work into the Consumption Selection freeze candidate would blur a clean architectural boundary. It therefore remains deferred beyond v0.0.7.

## 20. rc07 Source-Change Policy

rc07 is a consolidation-only candidate.

Expected source change is limited to:

```text
CHANGELOG.md
README.md
docs/executable-governance/README.md
docs/executable-governance/46_SCAF_v0.0.7rc07_Consumption_Selection_Milestone_Consolidation_and_Freeze_Candidate.md
```

No accepted representation, schema, validator, builder, fixture, frozen source, workflow, release-integrity artifact, authority registry, trace registry, test implementation, or trust-boundary implementation is changed by rc07.

## 21. Freeze Eligibility Criteria

v0.0.7rc07 is eligible for a clean freeze-candidate gate only if independent review confirms all of the following:

```text
1. exact committed rc06 predecessor and package lineage are correct;
2. rc07 is documentation/navigation/consolidation-only;
3. formal frozen v0.0.6 remains unchanged;
4. accepted rc01→rc06 semantics and executable behavior remain unchanged;
5. all accepted review findings entering rc07 are closed (current expected count: zero open findings);
6. Consumption Selection state/selection/authority distinctions remain intact;
7. exact-scope and source-provenance boundaries remain intact;
8. rc05 validator and rc06 builder ownership remain validation-first and deterministic;
9. review-covered regression suites remain PASS;
10. repository-owned production validators/integrity remain PASS;
11. fixture-equivalent builder→rc05 and fresh profile→rc12 chains remain PASS;
12. deferred context-source/AI/CI/L4/work-checkpoint capabilities remain unimplemented and unauthorized.
```

## 22. Governance Consequence of a Clean rc07 Review

If independent review returns a clean gate such as:

```text
V0.0.7 CONSUMPTION SELECTION MILESTONE CONSOLIDATION / FREEZE-CANDIDATE GATE: YES
```

then the only consequence is:

```text
v0.0.7 is eligible for an explicit formal freeze decision.
```

It does not itself create the formal release.

The formal release must be created only after an explicit governance instruction to freeze.
