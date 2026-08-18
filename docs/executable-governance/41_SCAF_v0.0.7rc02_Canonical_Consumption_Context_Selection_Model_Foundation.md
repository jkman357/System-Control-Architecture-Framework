# SCAF v0.0.7rc02 — Canonical Consumption / Context-Selection Model Foundation

**Development Release:** v0.0.7rc02  
**Status:** Canonical Consumption / Context-Selection Logical Model / Review Candidate  
**Date:** 2026-08-18  
**Immediate Predecessor:** v0.0.7rc01 (`e1a1bff5802edca86ae660c129ca20dc1409cdf1`)  
**Frozen Basis:** v0.0.2 L1/L2; v0.0.3 L3; v0.0.4 Executable Governance; v0.0.5 L3 Machine-Readable Traceability; v0.0.6 Machine-Readable Project Application / Effective Project Profile

## 1. Decision Purpose

The independently reviewed v0.0.7rc01 consumption semantic foundation established that a downstream consumer may use validated Effective Project Profile state for deterministic partitioning, filtering, navigation, reporting, and future context preparation without becoming a new source of engineering authority.

rc01 intentionally did not define a machine-readable consumption or context-selection record.

v0.0.7rc02 defines the first **canonical logical model** for one downstream consumption/context-selection result while remaining representation-neutral and executable-neutral.

The model answers these questions:

```text
Which exact validated profile snapshot was consumed?
For which exact project scope?
What selection purpose was declared?
What deterministic eligibility predicate was applied?
Which entries were actually included?
Was any otherwise-eligible material omitted because of a bounded resource constraint?
Can each included entry be traced back to the exact validated profile state?
Can a consumer distinguish predicate exclusion from bounded omission?
```

The governing rule is:

> **A canonical consumption selection records a subordinate deterministic selection over one validated Effective Project Profile snapshot. It may record selection intent, eligibility, inclusion, and bounded omission. It shall not create or reinterpret Project Application applicability, Pattern selection, implementation, verification, compliance, risk, release, or closure authority.**

rc02 is a logical-model foundation only. It does not add YAML/JSON serialization, schema, source-aware validator, builder/generator, query API, CLI, AI orchestration, scope resolver, CI gate, or persistent context state.

## 2. Accepted rc01 Basis

The independent rc01 review returned:

```text
Critical: 0
Major:    0
Minor:    0
Trivial:  0

V0.0.7RC01 EFFECTIVE PROJECT PROFILE CONSUMPTION SEMANTIC FOUNDATION GATE: YES
```

The accepted semantic constraints therefore remain binding in rc02, including:

```text
included in context != applicable
excluded from context != not_applicable

undetermined != no_current_disposition

filtered consumption != complete Effective Project Profile

machine-determinable selection fact
!= engineering judgment
!= Project Design Authority decision
```

rc02 may formalize those semantics into a logical data model, but it may not reopen the frozen v0.0.6 profile meanings or relax the rc01 authority boundary.

## 3. Canonical Logical Entity

The canonical logical entity introduced by rc02 is a **Consumption Selection**.

A Consumption Selection is:

```text
one source-bound
one-scope
one-purpose
one-predicate
one-result
subordinate selection over one validated Effective Project Profile snapshot
```

It is not:

```text
a new Project Application record
a replacement Effective Project Profile
a scope-resolution result
a Pattern-selection record
an implementation-status record
a verification/compliance record
a release/closure record
an AI approval record
```

The concrete serialized record name and field spelling are deferred. rc02 defines logical members, cardinality, relations, and state constraints only.

## 4. Canonical Logical Members

A Consumption Selection contains the following logical members:

| Logical member | Cardinality | Meaning |
|---|---:|---|
| `source_profile_binding` | exactly 1 | Binds the selection to one exact validated Effective Project Profile snapshot and its frozen provenance. |
| `selection_purpose` | exactly 1 | Opaque non-authoritative description/reference for why this selection exists. |
| `state_selector` | exactly 1 | Explicit subset of the four frozen profile states used in the eligibility predicate. |
| `authority_selector` | exactly 1 | Either the complete PAO domain or an explicit exact set of `scaf_authority_id` values. |
| `bounded_omission` | exactly 1 | States whether otherwise-eligible entries were intentionally omitted because of a bounded resource constraint and, if so, records a non-authoritative omission basis. |
| `selected_entries` | 0..n | Exact included projections from the validated source profile after predicate and any bounded omission are applied. |
| `selection_class` | exactly 1 | Derived classification: `complete` or `filtered`; it is not an engineering state. |

The logical model deliberately does not require a timestamp, filesystem path, AI model identity, user identity, approval identity, random/generated identifier, priority, severity, or release/closure state.

Such metadata, if later needed, requires separate review and shall not change the source-selection semantics defined here.

## 5. Source Profile Binding

Every Consumption Selection is subordinate to exactly one validated Effective Project Profile snapshot.

The logical source binding contains at least these facts:

```text
exact Effective Project Profile source-byte SHA-256
scaf_source_release
project_scope_ref
project_application_source_sha256
```

The exact Effective Project Profile source-byte digest is a consumer-side provenance binding over the profile bytes that were validated and consumed. It does not modify the frozen v0.0.6 profile representation.

The other three values are copied/recovered from the validated profile and must correspond exactly to that source profile.

These provenance values are not independent engineering truth and do not establish:

```text
signer identity
project approval
scope correctness
engineering correctness
compliance
verification
release readiness
closure
```

A later executable boundary must prove that the bound source profile is valid through the accepted frozen v0.0.6 profile validation boundary before trusting these values.

## 6. Exact Scope Preservation

The Consumption Selection inherits the source profile's exact opaque `project_scope_ref`.

The logical model defines no separate caller-selected scope field that could conflict with the source profile.

Consumption selection therefore remains resolution-neutral and does not infer:

```text
scope hierarchy
scope alias
scope inheritance
scope parent/child relation
wildcard scope match
cross-scope carryover
scope existence
scope correctness
```

If a future consumer needs a different scope, it must consume a separately validated Effective Project Profile for that exact scope.

## 7. Selection Purpose

`selection_purpose` records why the subordinate selection was requested or produced.

Examples may include descriptive values such as:

```text
engineering review preparation
unresolved applicability review
bounded AI context preparation
applicable-only navigation
missing-disposition report
```

The purpose is project/tool-owned descriptive metadata only.

It shall not decide or change:

```text
profile state
Project Application state
PAO authority
Pattern selection
implementation state
verification/compliance state
risk acceptance
release/closure state
```

A purpose may explain why a selection was produced. It is not an authority source for what the selected entries mean.

## 8. Frozen State Selector

`state_selector` is an explicit mathematical subset of the frozen profile-state vocabulary:

```text
{ applicable,
  not_applicable,
  undetermined,
  no_current_disposition }
```

No fifth state is introduced.

The selector may contain:

```text
all four states
one state
multiple states
zero states
```

An empty state set is a valid deterministic predicate that yields no eligible entries. It does not represent invalidity or a new state.

The selected state set changes only eligibility for the subordinate selection. It does not rewrite any source profile state.

## 9. Authority Selector

`authority_selector` has exactly one of two logical forms:

```text
all_domain
```

or:

```text
explicit_set(S)
```

where `S` is an exact set of `scaf_authority_id` values.

For `all_domain`, every PAO entry in the validated source profile domain is eligible for authority matching.

For `explicit_set(S)`, only exact IDs in `S` may satisfy the authority portion of the predicate.

An explicit empty set is valid and selects no authority IDs.

A later executable validator shall not silently ignore an explicit unknown ID. An ID that cannot be resolved within the validated source profile domain is a machine-verifiable representation/source inconsistency for the future consumption record, not a reason to invent or infer an engineering state.

No L3 Pattern ID, file path, artifact name, free-text authority title, alias, or AI semantic match may substitute for exact `scaf_authority_id` identity in this selector.

## 10. Canonical Eligibility Predicate

rc02 deliberately avoids an arbitrary Boolean-expression language.

The canonical eligibility predicate is fixed to the intersection of the two selectors:

```text
E = {
      entry in D
      |
      entry.profile_state is in state_selector
      AND
      entry.scaf_authority_id satisfies authority_selector
    }
```

where:

```text
D = complete validated PAO domain represented by the source profile
E = predicate-eligible set
```

This fixed form is deterministic, reviewable, and bounded.

It does not support arbitrary code, regular expressions, semantic similarity, AI classification, scope inference, Pattern inference, artifact-presence inference, or external project logic.

Additional predicate dimensions, if ever needed, require separate controlled review.

## 11. Predicate Exclusion

Entries in the source profile that do not satisfy the canonical predicate form the predicate-excluded set:

```text
X = D - E
```

Predicate exclusion is a selection fact only.

For an entry in `X`, exclusion shall not imply:

```text
not_applicable
unimportant
out of scope
implemented
satisfied
verified
compliant
closed
```

The source profile state remains unchanged and recoverable.

## 12. Selected Entries

`selected_entries` is the exact included set after the eligibility predicate and any explicit bounded omission are applied.

Let:

```text
I = included selected-entry set
```

Every selected entry is a subordinate projection of exactly one source profile entry and preserves exactly:

```text
scaf_authority_id
profile_state
project_application_record_id (if present in the source profile entry)
```

No rationale/provenance text from Project Application is copied into the canonical selected-entry projection by rc02.

For recorded states:

```text
applicable
not_applicable
undetermined
```

`project_application_record_id` remains present exactly as in the source profile.

For:

```text
no_current_disposition
```

`project_application_record_id` remains absent.

A selected entry does not become a new source of profile or Project Application truth. Its values must correspond exactly to the validated source profile entry.

## 13. Bounded Omission

rc01 allowed future bounded omission/truncation only when it is explicit and non-authoritative.

rc02 models that distinction logically.

`bounded_omission` records:

```text
applied: yes | no
basis: non-authoritative descriptive basis when applied == yes
```

Examples of a descriptive basis may include:

```text
token/resource bound
size bound
entry-count bound
latency/resource bound
other separately governed bounded constraint
```

rc02 does not define an omission algorithm, ranking algorithm, token-budget algorithm, priority model, or severity model.

If bounded omission is not applied:

```text
I = E
```

If bounded omission is applied:

```text
I is a subset of E
O = E - I
```

where `O` is the bounded-omitted set.

An omitted eligible entry remains eligible under the declared predicate; it was merely not included in the bounded result.

Omission shall not rewrite its source state or imply not-applicable, unimportant, satisfied, verified, compliant, or closed.

## 14. Canonical Set Algebra

The model preserves three distinct classes of source-profile entries:

```text
I = included entries
O = predicate-eligible but bounded-omitted entries
X = predicate-excluded entries
```

with:

```text
D = I + O + X
```

and the sets are mutually disjoint.

The intermediate eligibility relation remains:

```text
E = I + O
D = E + X
```

This distinction is important because:

```text
predicate excluded
!= bounded omitted
```

and neither condition changes the originating profile state.

## 15. Complete Versus Filtered Selection Class

`selection_class` is a derived machine-determinable classification, not caller-owned engineering judgment.

It is:

```text
complete
```

if and only if:

```text
I = D
O = empty
X = empty
```

Otherwise it is:

```text
filtered
```

Therefore a selection that began with an all-domain/all-state predicate but was later truncated because of a resource bound is **filtered**, not complete.

A future serialized field representing `selection_class`, if included, must be validated against the actual source/profile/set relations and may not be trusted as an unsupported caller assertion.

## 16. Context Inclusion / Exclusion Remains Non-Authoritative

The rc01 central rule remains binding:

```text
included in context != applicable
excluded from context != not_applicable
```

In rc02 terms:

```text
entry in I
    -> included by the declared consumption selection

entry in O or X
    -> not included by this declared consumption selection
```

Neither relation changes `profile_state`.

A `not_applicable` entry may legitimately be in `I` if the declared selector includes that state.

An `applicable` entry may legitimately be in `O` or `X` if the declared selector or bounded omission excludes it from this particular consumption result.

That is not a contradiction because selection membership and applicability state are different dimensions.

## 17. State Fidelity

For every source profile entry, the frozen meanings remain unchanged:

```text
applicable
not_applicable
undetermined
no_current_disposition
```

A Consumption Selection shall not:

```text
map undetermined to applicable
map undetermined to no_current_disposition
map no_current_disposition to undetermined
map absence to not_applicable
create context_selected as a fifth profile state
create omitted as a fifth profile state
create excluded as a fifth profile state
```

Selection/omission membership is separate metadata over the source profile state.

## 18. Invalid, Unresolved, and Missing Remain Distinct

The established SCAF distinction remains:

```text
Invalid
= machine-verifiable representation/source inconsistency

Undetermined
= valid current Project Application record with unresolved engineering judgment

No current disposition
= valid profile-level absence of an exact current Project Application record
```

Future consumption-record invalid conditions may include source digest mismatch, unknown source authority ID, state mismatch, duplicate selected ID, selected entry outside the declared eligibility set, or inconsistent completeness/omission claims.

Such invalidity is not equivalent to `undetermined` or `no_current_disposition`.

## 19. Project Application Truth Remains Upstream

The selected-entry projection intentionally carries only the existing profile trace identifier for recorded states.

If a downstream workflow needs:

```text
disposition rationale
decision_refs
authority_refs
supporting_refs
unresolved_reason
awaiting_refs
```

it must trace through the accepted `project_application_record_id` to the validated Project Application source.

rc02 does not create a competing authoritative copy of Project Application truth inside the consumption model.

Future bounded excerpts or rendered summaries require separate provenance/authority rules.

## 20. Deterministic Ordering

A future representation shall use deterministic ordering for reproducibility and validation.

At the logical level, selected entries are ordered by exact `scaf_authority_id` ascending unless a later separately reviewed representation defines an equivalent canonical source order.

Ordering has no engineering meaning and shall not imply:

```text
priority
severity
risk
importance
implementation sequence
review sequence
AI attention priority
```

Any priority/ranking model requires separate project authority.

## 21. Source Snapshot Ownership for Later Executable Boundaries

rc02 remains non-executable, but it fixes the ownership expectation for later tooling.

A supported executable consumer or validator shall not accept caller-supplied parsed profile state, caller-created indexes, caller-created PASS reports, or cached labels as substitutes for source validation.

A later executable boundary must own or chain:

```text
exact selected profile bytes
        ↓
accepted frozen v0.0.6 profile validation
        ↓
validated private source snapshot
        ↓
consumption predicate / selected-entry proof
```

The exact implementation pattern is deferred, but source ownership is not optional.

## 22. Logical Consistency Conditions

A conformant future representation/validator must eventually be able to prove at least:

1. the bound profile snapshot passes the accepted frozen profile validation boundary;
2. the profile SHA-256 binds the exact consumed profile bytes;
3. copied provenance values exactly match the validated profile;
4. every `state_selector` value belongs to the four frozen states;
5. every explicit authority ID belongs to the validated profile domain;
6. eligibility is exactly the fixed state-selector AND authority-selector intersection;
7. every selected entry exists exactly once in the validated source profile;
8. every selected entry preserves source `profile_state` and record ID shape exactly;
9. every selected entry belongs to the eligible set;
10. if bounded omission is not applied, selected set equals eligible set;
11. if bounded omission is applied, selected set is a subset of eligible set and the omission basis is explicit;
12. `selection_class` matches the actual complete/filtered relation;
13. selected-entry ordering is canonical;
14. no selection fact is interpreted as a new applicability or engineering state.

These are logical obligations. rc02 does not yet implement a schema or validator for them.

## 23. Machine-Determinable Fact Versus Engineering Judgment

rc02 preserves the wider SCAF rule:

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

Examples of machine-determinable facts introduced by the logical model include:

```text
this entry is eligible under the declared predicate
this entry is included in the selection
this eligible entry was omitted by an explicit bounded constraint
this entry was excluded by the predicate
this selection is complete
this selection is filtered
this selected entry preserves source profile state
```

None of those facts establish substantive engineering correctness or completion.

## 24. Canonical Model Does Not Define Context Content

The Consumption Selection model answers **which profile entries are selected**, not **which repository files or text fragments are placed into an AI/model context**.

rc02 therefore does not define mappings from PAOs to:

```text
normative Markdown excerpts
L3 Pattern documents
source-code files
requirements
architecture documents
test cases
evidence artifacts
Project Application rationale excerpts
issue/ticket content
AI prompts
conversation history
```

Those are later context-assembly/source-resolution concerns.

This separation prevents the context-content resolver from being silently embedded inside the selection model.

## 25. Deliberately Not Solved in rc02

v0.0.7rc02 does **not** define or implement:

```text
YAML/JSON consumption serialization
JSON Schema
raw-YAML policy
source-aware consumption validator
consumption builder/generator
consumption read/query API
CLI
persistent consumption/context registry or cache
profile history/supersession model
project-scope/reference resolver
scope hierarchy / alias / inheritance
PAO-to-file or PAO-to-document context resolver
AI context package
AI prompt format
AI orchestration / model selection
arbitrary predicate language
semantic similarity selection
priority/ranking/severity model
automatic applicability inference
Pattern recommendation/selection
AI approval of engineering rationale
Project Design Authority automation
CI applicability-completion enforcement
implementation/compliance/verification/closure determination
profile-driven code generation
new L3 tranche / M3 / M4
L4 implementation/verification guidance
Development Context Recovery / .scaf/work-checkpoint.yaml
external-trust-model expansion
```

These remain separately gated future work.

## 26. Expected Future Progression

A possible later progression, subject to independent review at each step, is:

```text
rc01 consumption semantics
        ↓
rc02 canonical consumption/context-selection logical model
        ↓
canonical machine-readable representation
        ↓
schema
        ↓
source-aware validation
        ↓
deterministic selection builder
        ↓
separately governed context-source resolution / context assembly
```

This is explanatory only. rc02 does not pre-authorize the next stage.

## 27. Engineering Problem Solved

In plain language, rc02 solves this problem:

> **rc01 said that a tool may filter a validated profile without turning filtering into engineering authority. rc02 now defines the exact logical accounting needed to describe that filtering: what source profile was used, what predicate made entries eligible, what was actually included, what was excluded by the predicate, and what was merely omitted because of a bounded resource limit.**

That distinction becomes essential before any AI context builder is allowed to operate programmatically.

## 28. What rc02 Intentionally Does Not Solve

rc02 still does not answer:

> Which files, Pattern documents, code, rationale, evidence, or other repository material should be attached to each selected PAO and sent to an AI/model context?

That mapping is deliberately later work.

The current line first stabilizes **selection truth** before introducing **context-content resolution**.

## 29. Review Gate Intent

Independent review should determine whether rc02:

- begins exactly from accepted committed v0.0.7rc01;
- preserves formal v0.0.6 unchanged;
- faithfully carries forward the clean rc01 consumption semantic boundary;
- defines one subordinate canonical Consumption Selection without creating new authority;
- binds one exact validated profile snapshot and exact scope;
- defines a bounded deterministic state-selector AND authority-selector predicate;
- distinguishes predicate eligibility, predicate exclusion, included result, and bounded omission;
- preserves the set algebra `D = I + O + X` and `E = I + O`;
- derives complete versus filtered classification rather than trusting an unsupported assertion;
- preserves selected entry state/record-trace fidelity exactly;
- preserves `included != applicable` and `excluded != not_applicable`;
- introduces no fifth profile state;
- keeps Project Application rationale/provenance upstream;
- preserves deterministic ordering without priority/severity meaning;
- defines future validation-owning expectations without implementing them;
- introduces no serialization, schema, validator, builder, context-source resolver, AI package, CI/L4, or work-checkpoint capability.

A clean review permits the v0.0.7 line to consider a later separately reviewed canonical machine-readable representation. It does not pre-authorize that representation.
