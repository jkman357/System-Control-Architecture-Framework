# SCAF v0.0.7rc01 — Effective Project Profile Consumption Semantic Foundation

**Development Release:** v0.0.7rc01
**Status:** Consumption Semantic Foundation / Review Candidate
**Date:** 2026-08-18
**Immediate Predecessor:** formal v0.0.6 (`4e0192d9535dba84358b511da399088b0e40dfec`)
**Frozen Basis:** v0.0.2 L1/L2; v0.0.3 L3; v0.0.4 Executable Governance; v0.0.5 L3 Machine-Readable Traceability; v0.0.6 Machine-Readable Project Application / Effective Project Profile

## 1. Decision Purpose

Formal v0.0.6 can deterministically produce and source-validate an Effective Project Profile for one exact project scope. It intentionally stops before defining how a downstream tool, human workflow, or AI-oriented context assembler may consume that profile.

That gap matters because a technically valid profile can still be misused downstream. Examples include:

```text
applicable
    -> incorrectly treated as implementation complete

not_applicable
    -> incorrectly treated as globally irrelevant authority

undetermined
    -> silently dropped as if no issue exists

no_current_disposition
    -> incorrectly converted into undetermined or not_applicable

included in an AI context
    -> incorrectly treated as project applicability authority

excluded from an AI context
    -> incorrectly treated as not_applicable
```

v0.0.7rc01 defines the semantic boundary for **consuming** a validated Effective Project Profile without transferring engineering authority into the consumer.

The governing rule is:

> **A downstream consumer may deterministically project, partition, filter, navigate, or prepare context from validated Effective Project Profile state. It shall not reinterpret that state as a new applicability decision, implementation result, compliance result, verification result, approval, release decision, or closure decision.**

rc01 is semantic-only. It does not add a context-package representation, schema, validator, generator, query API, CLI, scope resolver, CI gate, or AI orchestration implementation.

## 2. Why a Separate Consumption Boundary Is Needed

The frozen v0.0.6 chain establishes:

```text
Project Application truth
        ↓
source-aware validation
        ↓
Effective Project Profile
        ↓
source-aware validation
        ↓
deterministic generation
```

That chain answers:

> What is the current validated project-side applicability disposition state for each PAO in one exact scope?

It does not answer:

> What may a downstream consumer safely infer from that state?

Those are different questions.

Without a separate consumption contract, different tools could assign incompatible meanings to the same four profile states. An AI context builder could also silently turn a selection heuristic into engineering authority merely because selected material was presented to a model.

v0.0.7 begins by making that interpretation boundary explicit before adding any machine-readable context-assembly mechanism.

## 3. Consumer Definition

For this line, a **consumer** is any downstream process that uses a validated Effective Project Profile as an input, including potentially:

```text
human navigation/reporting
repository context preparation
AI context assembly
project status visualization
bounded completeness reporting
future separately reviewed automation
```

The term `consumer` does not imply that all such capabilities are implemented by rc01.

A consumer is subordinate to the frozen profile/source truth. It does not become a new source of Project Application state or SCAF authority.

## 4. Validated-Profile Prerequisite

Consumption semantics apply to a **validated Effective Project Profile**, meaning a profile whose representation/source correspondence has been established through the frozen v0.0.6 rc12 boundary against the selected Project Application snapshot and repository-owned SCAF sources.

A later supported executable consumer shall not treat any of the following as an equivalent substitute for validation:

```text
caller assertion that a profile is valid
caller-supplied parsed profile object
caller-created state index
caller-created validation report
cached label saying PASS
AI statement that the profile looks correct
```

A later executable consumer must own or chain the accepted validation boundary before relying on profile state. The exact executable ownership pattern is deferred to a separately reviewed RC.

rc01 itself adds no executable consumer.

## 5. Frozen Four-State Meaning at Consumption Time

The consumer shall preserve the frozen v0.0.6 state vocabulary exactly:

```text
applicable
not_applicable
undetermined
no_current_disposition
```

No fifth state is introduced by consumption.

### 5.1 `applicable`

At consumption time, `applicable` means only:

```text
A validated current Project Application record exists
for the exact (scaf_authority_id, project_scope_ref) pair
and its applicability is applicable.
```

A consumer may place that PAO into an `applicable`-derived workset, navigation view, report partition, or future context-selection set.

The consumer shall not infer from `applicable` that:

```text
an implementation exists
an L3 Pattern has been selected
an implementation is correct
verification has passed
compliance has been established
risk is accepted
closure is complete
release is ready
```

### 5.2 `not_applicable`

At consumption time, `not_applicable` means only:

```text
A validated current Project Application record exists
for the exact pair and explicitly records not_applicable.
```

A consumer may exclude that PAO from a deliberately defined **applicable-only** workset or context-selection set.

That exclusion does not mean:

```text
the SCAF authority record ceased to exist
the PAO is globally irrelevant
the PAO is not applicable to another project scope
the disposition rationale may be discarded
the Project Application record may be deleted
```

### 5.3 `undetermined`

At consumption time, `undetermined` means:

```text
A validated current Project Application record exists
for the exact pair, but the engineering applicability judgment
is explicitly unresolved.
```

A consumer shall preserve `undetermined` as an explicit unresolved state. It shall not silently convert it into:

```text
applicable
not_applicable
no_current_disposition
representation failure
non-compliance
verification failure
closure failure
```

A future context assembler may surface `undetermined` material specifically because engineering resolution is still needed, but presence in context does not itself resolve the judgment.

### 5.4 `no_current_disposition`

At consumption time, `no_current_disposition` means only:

```text
No current Project Application record exists
for the exact (scaf_authority_id, project_scope_ref) pair
in the selected validated Project Application snapshot.
```

It remains distinct from `undetermined`.

A consumer shall not convert it into:

```text
not_applicable
undetermined
scope does not exist
project failure
non-compliance
closure failure
```

A completeness-oriented consumer may surface this state as **missing current disposition**. That phrase is a consumption description of dataset-relative absence; it is not a new Project Application applicability token.

## 6. Canonical State Partitions for Consumption

A consumer may deterministically partition a validated profile into the four source-preserving sets:

```text
A = entries with profile_state == applicable
N = entries with profile_state == not_applicable
U = entries with profile_state == undetermined
M = entries with profile_state == no_current_disposition
```

The frozen complete-domain invariant remains:

```text
D = A + N + U + M
```

where `D` is the validated PAO domain for the profile's bound SCAF source release.

These partitions are deterministic views over existing profile state. They create no new engineering judgment.

## 7. Complete Versus Filtered Consumption

Two semantic classes of consumption are recognized.

### 7.1 Profile-preserving consumption

A profile-preserving consumer represents the complete validated domain and preserves all four states.

Such a result may claim complete-profile coverage only if every profile entry remains represented or recoverably traceable.

### 7.2 Filtered consumption

A filtered consumer may intentionally select a subset, for example:

```text
applicable only
undetermined only
no_current_disposition only
applicable + undetermined
any other explicitly declared state predicate
```

Filtering is permitted only as a **view/selection operation**. It shall not redefine the source state of excluded entries.

A filtered result shall not claim to be the complete Effective Project Profile.

The filtering predicate or selection intent must be explicit or recoverable in any later machine-readable consumption representation. The concrete representation is deferred.

## 8. Context Inclusion Is Not Applicability Authority

A central rule for future AI/context work is:

```text
included in context
!= applicable

excluded from context
!= not_applicable
```

Context assembly may consider profile state, task intent, bounded token/resource budgets, navigation needs, unresolved questions, or other separately governed inputs.

Therefore the act of selecting material for a context window is not itself an engineering applicability decision.

Likewise, omitting material from a bounded context window does not alter SCAF authority or Project Application state.

Any future context-packaging mechanism must preserve this distinction explicitly.

## 9. Context Presence Does Not Establish Engineering Completion

The following implications are prohibited:

```text
PAO present in context
    -> implemented                [invalid inference]

Pattern present in context
    -> selected by project        [invalid inference]

evidence artifact present
    -> verification passed        [invalid inference]

profile entry applicable
    -> requirement satisfied      [invalid inference]

profile entry not_applicable
    -> no rationale needed        [invalid inference]

AI produced an answer
    -> Project Design Authority approval [invalid inference]
```

Context is information availability, not engineering closure.

## 10. Exact-Scope Preservation

Consumption remains bound to the profile's exact opaque `project_scope_ref`.

A consumer shall not infer:

```text
scope hierarchy
parent/child propagation
scope aliases
scope inheritance
wildcard applicability
cross-scope carryover
scope existence/correctness
```

A disposition from another scope cannot be imported merely because the consumer considers the scopes related.

Scope resolution remains deferred.

## 11. Source-Release and Authority Preservation

A consumer remains subordinate to:

```text
profile.scaf_source_release
profile.project_scope_ref
profile.project_application_source_sha256
profile.entries[].scaf_authority_id
profile.entries[].project_application_record_id (when present)
```

These values bind the consumed state back to frozen source/profile semantics.

A later consumption representation must preserve sufficient provenance to recover the originating validated profile state and its exact Project Application trace where applicable.

The concrete field model and serialization are not defined by rc01.

## 12. Do Not Duplicate Project Application Truth

The frozen v0.0.6 profile deliberately avoids copying Project Application rationale/provenance fields into every profile entry.

A downstream consumer shall not create a competing authoritative copy merely for convenience.

When rationale or project-side provenance is needed, the consumer should trace through the accepted `project_application_record_id` to the validated Project Application source rather than treating copied text in a future context package as a new source of truth.

A future consumption package may carry bounded excerpts or references for navigation, but their authority/provenance semantics require separate review.

## 13. Invalid, Unresolved, and Missing Remain Distinct

The existing SCAF distinction remains:

```text
Invalid
= machine-verifiable representation/source inconsistency

Undetermined
= valid current Project Application record with unresolved engineering judgment

No current disposition
= valid profile-level absence of an exact current Project Application record
```

Consumption shall not collapse these states.

In particular:

```text
undetermined != invalid
no_current_disposition != invalid
undetermined != no_current_disposition
```

## 14. Deterministic Fact Versus Engineering Judgment

The consumption boundary preserves the wider SCAF rule:

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

Examples of machine-determinable consumption facts include:

```text
this entry's validated profile state is applicable
this entry belongs to the undetermined partition
this exact pair has no current disposition
this filtered view selected states {applicable, undetermined}
```

Examples that remain engineering/project decisions include:

```text
whether an applicability rationale is substantively adequate
whether a design mechanism satisfies the applicable concern
whether a Pattern should be selected
whether evidence is sufficient
whether the project is compliant
whether a risk is accepted
whether the work is complete
```

## 15. No Priority or Severity Inference from Ordering

Canonical ordering in the frozen profile is deterministic serialization/navigation order.

A consumer shall not infer from entry order:

```text
priority
severity
implementation sequence
review sequence
risk level
importance
```

Any later priority/severity model requires separate project/source authority.

## 16. Consumption Result Is Subordinate

Any future consumption result, selection set, context package, report, or AI input bundle is a **derived subordinate artifact**.

It does not replace:

```text
SCAF normative authority
Project Application source
Effective Project Profile source
Project Design Authority decisions
verification/evidence records
release/closure records
```

Regeneration or re-selection from the same validated inputs may produce a later subordinate view without rewriting the authoritative project disposition source.

## 17. Bounded Omission and Truncation

Future context consumers may operate under token, size, latency, or resource limits.

rc01 permits bounded omission only as explicit selection/truncation behavior. A bounded result shall not imply that omitted material is:

```text
not applicable
unimportant
satisfied
verified
closed
```

A future machine-readable context contract must make completeness/truncation semantics explicit before such results can be relied on programmatically.

No token-budget algorithm is introduced by rc01.

## 18. Semantic Conformance Rules for Later Consumers

A later consumer claiming conformance with this foundation must preserve at least these rules:

1. consume only validated Effective Project Profile state through a validation-owning/chained boundary;
2. preserve the four frozen profile-state meanings;
3. preserve `undetermined != no_current_disposition`;
4. preserve exact-scope semantics;
5. never convert context selection into applicability authority;
6. never convert applicability state into implementation/compliance/verification/closure state;
7. distinguish complete-profile consumption from filtered consumption;
8. keep filtered predicates/selection intent explicit or recoverable;
9. preserve traceability back to the originating profile/Project Application sources;
10. keep consumption artifacts subordinate and non-authoritative.

## 19. Deliberately Not Solved in rc01

v0.0.7rc01 does **not** define or implement:

```text
canonical context-package / consumption-record data model
YAML/JSON representation
JSON Schema
source-aware context validator
context generator/builder
context query API
CLI
persistent context registry/cache/history
project-scope/reference resolver
scope hierarchy / aliases / inheritance
automatic applicability inference
Project Application history/supersession/re-evaluation
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

## 20. Relationship to Future Context Assembly

A possible later progression, subject to independent review at each step, is:

```text
rc01 consumption semantics
        ↓
canonical consumption/context-selection model
        ↓
machine-readable representation
        ↓
schema / source-aware validation
        ↓
deterministic context assembly
        ↓
validated downstream read/query or AI context preparation
```

This sequence is explanatory only. rc01 does not pre-authorize any later stage or require that all stages be implemented.

## 21. Engineering Problem Solved

In plain language, rc01 solves this problem:

> **v0.0.6 can tell a tool what the validated profile says. rc01 defines what a downstream tool is allowed to mean when it uses that profile, so filtering or AI context preparation cannot silently become a new source of engineering authority.**

Without this boundary, two consumers could interpret the same valid profile differently, especially around `undetermined`, `no_current_disposition`, filtering, and context inclusion/exclusion.

## 22. What rc01 Intentionally Does Not Solve

rc01 does not yet answer:

> Which exact files, authority records, L3 Patterns, project artifacts, rationale, or evidence should be packaged into an AI context, and in what machine-readable format?

That is later work. First the consumption meaning must be stable.

## 23. Review Gate Intent

Independent review should determine whether rc01:

- starts exactly from formal frozen v0.0.6;
- adds a semantic consumption boundary without changing frozen behavior;
- preserves all four profile states exactly;
- preserves `undetermined != no_current_disposition`;
- preserves exact-scope and no-inference rules;
- makes context inclusion/exclusion explicitly non-authoritative;
- permits deterministic partition/filter operations without creating engineering decisions;
- keeps complete versus filtered consumption semantically distinct;
- preserves traceability/provenance expectations without inventing a concrete format;
- keeps Project Design Authority, compliance, verification, release and closure outside consumption;
- introduces no executable/context-packaging capability in rc01.

A clean review permits the v0.0.7 line to consider a later separately reviewed canonical consumption/context-selection model. It does not pre-authorize that model.
