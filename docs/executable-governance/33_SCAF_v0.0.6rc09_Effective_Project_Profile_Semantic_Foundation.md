# SCAF v0.0.6rc09 — Effective Project Profile Semantic Foundation

**Development Release:** v0.0.6rc09  
**Status:** Effective Project Profile Semantic Foundation / Review Candidate  
**Date:** 2026-08-18  
**Upstream Frozen Baselines:** v0.0.2 L1/L2; v0.0.3 L3; v0.0.4 Executable Governance; v0.0.5 L3 Machine-Readable Traceability  
**Accepted Development Basis:** v0.0.6rc04 Project Application representation; v0.0.6rc06 schema; v0.0.6rc07 validator; v0.0.6rc08 validated read/query views  
**Immediate Predecessor:** v0.0.6rc08

## 1. Decision Purpose

The independent v0.0.6rc08 review returned a clean gate with zero findings:

```text
Critical: 0
Major:    0
Minor:    0
Trivial:  0

V0.0.6RC08 PROJECT APPLICATION VALIDATED READ/QUERY VIEW FOUNDATION GATE: YES
```

The accepted v0.0.6 line can now represent, validate, and deterministically query current Project Application records without transferring project engineering authority to tooling.

The next gap is not another low-level representation check. It is a project-consumption semantic question:

> For one selected project scope, how can SCAF present the complete frozen Project-Applicable Obligation domain together with the current recorded Project Application disposition state, while keeping absence of a record distinct from an explicit unresolved engineering judgment?

v0.0.6rc09 defines the semantic foundation for an **Effective Project Profile**. It deliberately stops before concrete profile serialization, schema, generator, API, CLI, context packaging, or CI behavior.

The governing rule is:

> **An Effective Project Profile is a deterministic derived view of validated framework obligations and validated project-recorded dispositions for one exact selected scope. It is not a new source of applicability authority, engineering approval, compliance, verification, or project completion.**

## 2. Scope of rc09

rc09 defines only the semantic contract required before any machine-readable Effective Project Profile representation or generator is introduced.

It defines:

- the role of an Effective Project Profile;
- its framework obligation domain;
- its selected project-scope boundary;
- the four mutually exclusive current profile states;
- the distinction between explicit `undetermined` and derived `no_current_disposition`;
- total-domain / state-partition semantics;
- source-release and authority boundaries;
- absence-of-record semantics;
- scope-resolution neutrality;
- trace/provenance expectations for later profile representations;
- machine-determinable versus engineering-judgment boundaries.

rc09 does **not** add:

- an Effective Project Profile YAML/JSON representation;
- an Effective Project Profile schema;
- a profile generator or executable builder;
- a profile query API or CLI;
- a persistent/generated profile registry;
- project-scope hierarchy, registry, or resolver;
- project-controlled reference resolution;
- automatic applicability inference;
- AI approval of engineering rationale;
- Project Design Authority automation;
- Pattern recommendation or selection;
- implementation/satisfaction/compliance determination;
- verification/evidence/closure determination;
- completion PASS/FAIL;
- history/supersession/re-evaluation semantics;
- tailoring taxonomy;
- AI context packaging;
- CI applicability-completion enforcement;
- code generation;
- new L3 Pattern content;
- L4 guidance;
- Development Context Recovery / `.scaf/work-checkpoint.yaml` workflow state.

## 3. Effective Project Profile Meaning

An Effective Project Profile is a **derived current-state project-facing projection**.

Conceptually, it combines:

```text
validated frozen Project-Applicable Obligation domain
        +
validated current Project Application dataset
        +
one selected exact project_scope_ref value
        ↓
Effective Project Profile current-state projection
```

The profile does not replace either source.

Framework truth remains owned by the frozen SCAF authority source. Project applicability judgment remains owned by the Project Application records and the project governance authority that created them.

The Effective Project Profile is subordinate derived information.

## 4. Meaning of “Effective”

In `Effective Project Profile`, **Effective** means:

> the current derived projection obtained by combining the accepted framework obligation domain with the currently recorded dispositions for the selected exact scope.

It does **not** mean:

```text
approved
accepted by Project Design Authority
implemented
verified
compliant
complete
released
closed
recommended
selected by SCAF
```

The word `Effective` shall not be used to imply that the profile itself has engineering decision authority.

## 5. Framework Obligation Domain

The Effective Project Profile domain is the validated set of **Project-Applicable Obligations** for the SCAF source release to which the Project Application data is bound.

For the current v0.0.6 development line:

```text
scaf_source_release: v0.0.2
accepted current PAO inventory: 218
```

The semantic rule is **not** “a profile always contains 218 entries.”

The semantic rule is:

> The profile domain shall be derived from the validated Project-Applicable Obligation population for its bound SCAF source release.

The current frozen v0.0.2 population happens to contain 218 PAOs.

Framework Normative Invariants are not Project Application profile entries merely because they exist in the authority registry. They remain outside the Project-Applicable Obligation disposition domain.

## 6. Selected Project Scope Boundary

An Effective Project Profile is defined for exactly one selected non-empty `project_scope_ref` value.

At the current v0.0.6 boundary, `project_scope_ref` remains an opaque project-controlled string.

Therefore the semantic match rule is:

```text
exact serialized project_scope_ref equality
```

rc09 introduces no scope hierarchy, aliasing, inheritance, parent/child containment, wildcard matching, or resolver.

A future profile representation/generator shall remain explicit that scope resolution is not performed unless a separately reviewed scope-resolution capability is introduced.

Consequently, constructing or describing a profile for an arbitrary non-empty scope string does not prove that the scope exists in project governance.

## 7. Four-State Current Profile Partition

For each Project-Applicable Obligation in the bound framework domain and the one selected exact project scope, the profile has exactly one logical current-state classification:

```text
applicable
not_applicable
undetermined
no_current_disposition
```

These four states are mutually exclusive for one `(scaf_authority_id, project_scope_ref)` pair.

They are collectively exhaustive over the profile's validated PAO domain.

### 7.1 State derivation table

| Validated current Project Application record for exact PAO/scope pair | Record applicability | Effective Project Profile state |
|---|---|---|
| present | `applicable` | `applicable` |
| present | `not_applicable` | `not_applicable` |
| present | `undetermined` | `undetermined` |
| absent | n/a | `no_current_disposition` |

No other derivation is authorized by rc09.

### 7.2 `no_current_disposition` is profile-only derived state

`no_current_disposition` is **not** a fourth Project Application applicability token.

The accepted Project Application record vocabulary remains exactly:

```text
applicable
not_applicable
undetermined
```

A future profile representation may need a token for the derived absence state, but rc09 does not modify:

```text
schemas/project-application.schema.json
examples/project-application.yaml
```

and does not authorize a Project Application record such as:

```yaml
applicability: no_current_disposition
```

Such a Project Application record would remain outside the accepted Project Application contract.

## 8. `undetermined` Versus `no_current_disposition`

This distinction is normative for the rc09 semantic foundation.

### 8.1 `undetermined`

`undetermined` means:

- a current Project Application record exists for the exact PAO/scope pair;
- the record has passed the accepted representation/source-aware validation boundary;
- the project explicitly records that the applicability judgment remains unresolved;
- the accepted `unresolved_reason` / `awaiting_refs` state contract applies.

This is **explicit engineering-unresolved state**.

### 8.2 `no_current_disposition`

`no_current_disposition` means only:

- the PAO belongs to the validated profile framework domain; and
- no current Project Application record exists for that exact PAO/scope pair in the selected validated Project Application dataset.

This is **absence of a current recorded disposition in the selected dataset**.

It does not reveal why the record is absent.

### 8.3 Prohibited equivalences

The following equivalences are invalid:

```text
no_current_disposition == undetermined          INVALID
no_current_disposition == not_applicable        INVALID
no_current_disposition == applicable            INVALID
no_current_disposition == project failure       INVALID
no_current_disposition == non-compliance        INVALID
no_current_disposition == scope does not exist  INVALID
no_current_disposition == intentionally omitted INVALID
```

A missing record shall not be promoted into an engineering judgment.

## 9. Absence Is Dataset-Relative

`no_current_disposition` is relative to:

```text
one selected validated Project Application dataset
+
one exact selected scope
+
one validated PAO source domain
```

It is not a universal claim that no project decision exists anywhere else.

A future profile consumer shall not infer that an absent record means:

- nobody has considered the obligation;
- the project has rejected the obligation;
- the project has accepted the obligation;
- a decision document does not exist elsewhere;
- the selected scope is invalid;
- the project is incomplete;
- the project is non-compliant.

Only the selected controlled Project Application dataset is in the rc09 derivation boundary.

## 10. Total-Domain Semantics

An Effective Project Profile covers the complete validated Project-Applicable Obligation domain for its bound SCAF source release, not merely the subset with Project Application records.

Let:

```text
D = validated PAO domain size
A = applicable entries
N = not_applicable entries
U = undetermined entries
M = no_current_disposition entries
```

The semantic partition invariant is:

```text
D = A + N + U + M
```

For the current frozen v0.0.2 domain:

```text
D = 218
```

but later source releases may have a different validated PAO population.

### 10.1 Recorded-disposition coverage fact

The following is a machine-determinable recording fact:

```text
recorded disposition population = A + N + U
absence population              = M
```

A later representation may expose counts or ratios based on those facts.

However:

```text
M == 0
```

means only that every PAO in the bound domain has a current recorded disposition for the exact selected scope in the selected dataset.

It does **not** mean:

```text
project complete
engineering complete
compliance achieved
verification complete
risk closed
release ready
```

## 11. Input Validity Boundary

The Effective Project Profile semantic derivation is defined only over inputs that satisfy the accepted machine-determinable boundaries.

The Project Application side must satisfy the accepted rc07 representation/source-aware validator contract before profile derivation is supported.

The framework PAO domain must come from the validated frozen authority source for the bound release.

An invalid Project Application dataset is not transformed into profile states.

A failed framework authority proof is not transformed into a partial profile domain.

The future profile-generation implementation must own or reuse a validated-input boundary; caller-supplied unvalidated parsed mappings shall not become an alternate supported profile source.

rc09 defines this semantic requirement but introduces no generator/API implementation.

## 12. Source-Release Binding

An Effective Project Profile is source-release-bound.

The profile semantics require an explicit relationship to the SCAF source release that defines its PAO domain.

For the current Project Application representation:

```text
scaf_source_release: v0.0.2
```

A future profile representation shall not silently combine Project Application dispositions bound to one SCAF source release with a different PAO population.

Source-release migration or re-evaluation is outside rc09 and requires separate reviewed semantics.

## 13. Traceability of Derived Profile States

A future concrete profile representation shall preserve the distinction between state derived from a current Project Application record and state derived from record absence.

For a profile entry classified as:

```text
applicable
not_applicable
undetermined
```

there is exactly one validated current Project Application record for the exact PAO/scope pair under the current-state rc07 uniqueness contract.

A future representation should therefore be able to trace the profile state back to that Project Application record identity without copying the Project Application record into a new source of truth.

For:

```text
no_current_disposition
```

there is intentionally no Project Application record identity to cite for that pair.

The derived state comes from validated domain membership plus validated absence in the selected current dataset.

rc09 does not yet define concrete profile field names or serialization for this trace.

## 14. No Applicability Inference From Other SCAF Layers

The profile state for one PAO/scope pair is not inferred from:

```text
L3 Pattern availability
L2↔L3 trace presence
Primary / Supporting / Constraint trace relation
Pattern recommendation
implementation artifact presence
verification evidence
project reference naming
scope string naming
other project scopes
other PAO dispositions
```

In particular:

```text
PAO has L3 traces + no Project Application record
        ↓
no_current_disposition
```

not:

```text
applicable
not_applicable
undetermined
recommended
selected
```

The v0.0.5 no-inference boundary remains intact.

## 15. Cross-Scope Non-Inference

A disposition recorded for one exact `project_scope_ref` does not automatically apply to another scope.

Example:

```text
SCAF-AK-001 + project:scope:A -> applicable
```

does not imply any state for:

```text
SCAF-AK-001 + project:scope:B
```

If no current record exists for scope B, its profile state is:

```text
no_current_disposition
```

unless a separately reviewed scope inheritance/resolution model is introduced later.

rc09 defines no cross-scope inheritance.

## 16. Profile Authority Boundary

The Effective Project Profile is a derived consumption surface.

It is not:

- framework normative authority;
- Project Design Authority;
- automatic applicability authority;
- rationale approval authority;
- Pattern-selection authority;
- verification/compliance authority;
- evidence/closure authority;
- risk/deviation authority;
- release approval authority.

A profile may faithfully report that the project recorded:

```text
applicable
not_applicable
undetermined
```

It may also report that no current disposition is recorded.

It shall not decide whether those project judgments are substantively correct.

## 17. Representation Invalidity Versus Project State

The following remain separate concepts:

```text
invalid Project Application representation
engineering-undetermined Project Application record
no current Project Application disposition
profile derivation result
project compliance / verification / closure
```

They shall not be collapsed into one generic status.

A structurally/semantically invalid Project Application dataset produces no supported Effective Project Profile.

A valid `undetermined` record produces an `undetermined` profile state.

A valid dataset with no record for a PAO/scope pair produces `no_current_disposition` for that profile entry.

## 18. Logical Profile Identity

At semantic level, an Effective Project Profile is identified by at least:

```text
bound SCAF source release
selected exact project_scope_ref
selected validated Project Application current-state dataset
```

The selected dataset matters because `no_current_disposition` is dataset-relative.

rc09 does not yet define a serialized profile identifier, profile file naming convention, persistent profile lifecycle, digest, signature, version field, or cache identity.

Those belong to a later representation/generator review if the capability advances.

## 19. Ordering Semantics

The logical Effective Project Profile is a total set of PAO entries for one selected scope.

rc09 does not assign engineering meaning to physical entry order.

A later concrete representation/generator should define deterministic serialization ordering independently, likely using exact SCAF authority identity ordering, but rc09 does not freeze a physical format or ordering algorithm.

No priority, severity, applicability preference, or authority precedence shall be inferred from profile entry position.

## 20. Machine-Determinable Facts Versus Engineering Judgment

The following can be machine-determinable after accepted input validation:

- whether a PAO belongs to the bound validated framework domain;
- whether exactly one current Project Application record exists for the exact PAO/scope pair;
- which accepted applicability token that record contains;
- whether no current record exists for the pair;
- counts of the four profile states;
- whether the state counts partition the complete validated PAO domain.

The following remain engineering/project authority matters:

- whether an `applicable` decision is correct;
- whether a `not_applicable` rationale is adequate;
- how an `undetermined` issue should be resolved;
- whether the right project scope was selected;
- whether a Project Design Authority approved a disposition;
- which Pattern should be selected;
- whether implementation satisfies an obligation;
- whether verification/evidence is sufficient;
- whether the project is compliant or complete;
- whether release/closure criteria are met.

The core rule remains:

> **machine-determinable fact != engineering judgment != project authority decision != verification result != closure**

## 21. Deferred Representation / Generator Work

If rc09 is accepted, later review-driven work may consider, in separate bounded RCs:

```text
canonical logical profile record/model
        ↓
concrete profile representation
        ↓
profile schema
        ↓
validated deterministic profile generator/API
```

This sequence is illustrative, not pre-authorized.

Each later step must preserve the rc09 semantic boundary and must be selected based on actual review/gap analysis.

In particular, rc09 acceptance does not automatically authorize:

- AI context package generation;
- automatic Pattern recommendation;
- CI disposition-completion gating;
- L4 guidance.

## 22. Required Negative-Condition Semantics

A conforming later implementation must preserve at least these outcomes:

| Condition | Required semantic outcome |
|---|---|
| PAO has current `applicable` record for exact scope | profile state `applicable` |
| PAO has current `not_applicable` record for exact scope | profile state `not_applicable` |
| PAO has current `undetermined` record for exact scope | profile state `undetermined` |
| PAO has no current record for exact scope | profile state `no_current_disposition` |
| PAO has no current record but has L3 trace relations | still `no_current_disposition` |
| PAO has disposition in a different scope only | selected scope remains `no_current_disposition` |
| Framework Normative Invariant exists | excluded from Project Application profile-entry domain |
| selected scope string matches no records | PAO domain may all be `no_current_disposition`; no scope-existence conclusion |
| Project Application dataset fails rc07 validation | no supported profile derivation |
| framework authority source proof fails | no supported profile domain/derivation |
| all PAOs have current dispositions | no `no_current_disposition`; still no compliance/completion conclusion |
| `no_current_disposition` entry exists | no automatic `undetermined`, `not_applicable`, failure, or non-compliance inference |

## 23. Frozen Baseline / Accepted Development Preservation

rc09 changes no frozen or accepted executable input surface.

The following remain unchanged:

```text
docs/normative/
docs/l3/
authority-registry.yaml
l3-trace-registry.yaml
schemas/authority-registry.schema.json
schemas/l3-trace-registry.schema.json
schemas/project-application.schema.json
examples/project-application.yaml
tools/scaf_validator/
tools/scaf_trace_validator/
tools/scaf_trace_views/
tools/scaf_project_application_validator/
tools/scaf_project_application_views/
tools/scaf_release_integrity/
tools/scaf_external_pin/
tools/scaf_ci_gate/
.github/workflows/
release-integrity/
```

rc09 is a semantic/documentation-only development step.

It shall not revise the frozen v0.0.2 L1/L2, v0.0.3 L3, v0.0.4 executable-governance, or v0.0.5 machine-readable traceability baselines.

It shall not revise the accepted rc04 Project Application representation, rc06 schema, rc07 validator, or rc08 validated query behavior.

## 24. Regression / Verification Expectations

Because rc09 changes no executable behavior, all accepted validator/query behavior must remain unchanged.

Expected regression inventory remains:

```text
frozen executable-governance tests:          41 / 41 PASS
frozen trace-validator tests:                24 / 24 PASS
frozen trace-view/query tests:               28 / 28 PASS
accepted rc07 Project Application validator: 21 / 21 PASS
accepted rc08 Project Application views:     22 / 22 PASS
```

The authority inventory remains:

```text
294 authority records
218 Project-Applicable Obligations
76 Framework Normative Invariants
```

The L3 trace inventory remains:

```text
12 Patterns
119 relations
```

Frozen release integrity must remain PASS.

## 25. Acceptance Boundary

v0.0.6rc09 is acceptable only if independent review confirms that:

1. Effective Project Profile is clearly subordinate derived current-state information, not new engineering/project authority.
2. The profile domain is the validated Project-Applicable Obligation population for the bound SCAF source release.
3. Framework Normative Invariants are excluded from the Project Application profile-entry domain.
4. One profile is bound to one exact opaque project scope at the current no-resolver boundary.
5. `applicable`, `not_applicable`, `undetermined`, and `no_current_disposition` form a mutually exclusive and exhaustive four-state profile partition.
6. `no_current_disposition` is explicitly profile-derived and is not added to the Project Application applicability vocabulary.
7. `undetermined` remains explicit engineering-unresolved state and is not conflated with record absence.
8. record absence remains dataset-relative and does not imply scope nonexistence, failure, non-compliance, intentional omission, or any applicability conclusion.
9. the total-domain partition invariant is clear without hard-coding 218 as a permanent cross-release constant.
10. cross-scope and L3-trace inference remain prohibited.
11. invalid input cannot be reinterpreted as a profile state.
12. machine-determinable profile facts remain separate from applicability correctness, Project Design Authority, Pattern selection, compliance, verification, evidence, and closure.
13. no profile representation/schema/generator/API/CLI/context package/CI/L4 capability is introduced prematurely.
14. frozen and accepted development surfaces/regressions remain unchanged.

A clean gate permits later review-driven consideration of the next profile representation/model step. It does not pre-authorize that step or freeze v0.0.6.
