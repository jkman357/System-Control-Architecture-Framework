# SCAF v0.0.8rc01 — Lifecycle-Proportional Governance Semantic Foundation

**Development Release:** v0.0.8rc01  
**Status:** Lifecycle-Proportional Governance Semantic Foundation / Review Candidate  
**Date:** 2026-08-19  
**Immediate Predecessor:** formal frozen v0.0.7 (`bfb7749f2783c10f9f29669d136192eb1387017f`)  
**Frozen Basis:** v0.0.2 L1/L2; v0.0.3 L3; v0.0.4 Executable Governance; v0.0.5 L3 Machine-Readable Traceability; v0.0.6 Project Application / Effective Project Profile; v0.0.7 Consumption Selection

## 1. Decision Purpose

SCAF already separates framework authority, Project Design Authority, Project Realization, verification/evidence authority and closure authority. It also distinguishes L3 Pattern maturity from project-specific implementation and verification.

A remaining cross-cutting governance gap is **depth control**: a review can continue discovering increasingly detailed questions even when the current engineering subject is already sufficiently bounded for the next intended engineering action and the additional evidence does not yet reasonably exist.

v0.0.8rc01 establishes a representation-neutral semantic foundation for **lifecycle-proportional governance**.

Its governing intent is:

> **Governance depth SHALL be proportional to the current engineering decision horizon, the material consequence of unresolved ambiguity at that horizon, and the evidence reasonably available at that time.**

The purpose is not to reduce engineering rigor. It is to require the **right rigor at the right time**.

The practical objective is:

```text
resolve what must be resolved now
        ↓
make the next engineering action sufficiently bounded
        ↓
record later evidence obligations explicitly
        ↓
defer questions that cannot yet be answered responsibly
        ↓
re-open them when their evidence/decision trigger becomes real
```

## 2. Why This Is a Framework-Governance Concern

Without a proportionality rule, increasingly capable reviewers or automated governance can create a pathological loop:

```text
architecture/specification
        ↓
review discovers a later-stage question
        ↓
later-stage evidence does not yet exist
        ↓
more formal rules are added to compensate
        ↓
more hypothetical corner cases appear
        ↓
implementation is delayed without reducing a current material ambiguity
```

SCAF shall instead distinguish:

```text
necessary current decision depth
!= theoretical maximum detail
!= eventual release evidence depth
```

A question may be important in the final system while still being **premature as a current blocking condition**.

## 3. No New Global Lifecycle State Machine

v0.0.8rc01 does **not** introduce a project-wide `M0/M1/M2/M3/M4` engineering lifecycle state machine.

The existing L3 maturity vocabulary remains owned by the frozen L3 catalog:

```text
M0 — Concept
M1 — Structured
M2 — Architecture Reviewed
M3 — Multi-Context Validated
M4 — Reference / Field Backed
```

Those terms describe **L3 Pattern maturity** and shall not be silently reused as project implementation/validation stages.

Project work is often unevenly mature. One interface may be implemented while another subsystem remains at concept/specification level. Therefore proportional governance is **subject-scoped**, not based on one global project maturity label.

Concept, specification, implementation, validation and release may be used informatively to explain examples, but rc01 does not create canonical lifecycle-stage tokens or a new state machine.

## 4. Current Decision Horizon

The **Current Decision Horizon** is:

> The set of decisions, definitions and currently producible evidence that must be sufficiently resolved for a specific reviewed subject to proceed to its next intended engineering action without material ambiguity, authority contradiction, unacceptable current risk, or avoidable irreversible commitment.

A Current Decision Horizon is always scoped to a concrete subject and next action.

Examples of subjects include:

- one interface/protocol contract;
- one persistent-state design;
- one boot/update flow;
- one architecture allocation;
- one timing contract;
- one implementation tranche;
- one validation activity;
- one release decision.

A horizon should answer at least:

```text
What engineering subject is being reviewed?
What is the next intended engineering action?
What decisions must be stable before that action?
What evidence can reasonably exist now?
What later evidence is required but not yet producible?
What unresolved issue would materially make the next action unsafe or ambiguous?
```

The horizon is not a new authority. The applicable Project Design Authority, external authority, Project Realization and Verification / Assurance Authority retain their existing ownership.

## 5. Governance Proportionality Rule

For a given Current Decision Horizon:

> **Governance depth SHALL be proportional to the decision required now, the consequence of unresolved ambiguity now, and the evidence reasonably available now.**

This means SCAF review should continue until the subject is sufficiently bounded for the next intended engineering action, not until every later-stage concern has been completely proven.

Proportionality shall not be used to omit a decision that is already necessary for current deterministic implementation, current authority consistency, current safety/correctness, or an imminent irreversible commitment.

Equally, theoretical completeness alone shall not convert a later-stage question into a current blocking requirement.

## 6. Evidence Availability Rule

SCAF shall distinguish **evidence required now** from **evidence required later**.

> **SCAF SHALL NOT require empirical evidence that the current engineering state cannot reasonably produce.**

Where empirical evidence will later be required but is not yet reasonably producible, the current horizon shall instead define, as applicable:

- the property or quantity that must later be verified;
- the semantic meaning of that property;
- the observation or measurement boundary;
- the responsible project authority/role;
- the required evidence trigger or later engineering point;
- any current design constraint needed so that later verification remains possible.

For example, before target implementation exists, a timing review may legitimately require:

```text
quantity definition
measurement start boundary
measurement end boundary
responsible verification owner
required later verification trigger
```

while not requiring:

```text
measured ISR latency
measured jitter
actual WCET
measured transceiver-release latency
```

unless such evidence already reasonably exists or an applicable external authority explicitly requires it at the current horizon.

Absence of not-yet-producible evidence is not by itself a conformance failure when the future evidence obligation and revisit trigger are adequately controlled.

## 7. External Authority and Applicable Constraint Preservation

Lifecycle-proportional governance does not waive applicable safety, security, regulatory, contractual, risk or other external-authority requirements.

If an applicable external authority requires a property, artifact, analysis or evidence before the next intended action, that requirement becomes part of the Current Decision Horizon.

Therefore:

```text
proportional governance
!= permission to ignore an applicable external requirement
!= permission to defer a required safety decision
!= risk acceptance
!= compliance waiver
```

SCAF continues to preserve the existing authority chain and Applicable Satisfaction Basis semantics.

## 8. Progression Sufficiency

The governing review question is:

> **Is the current subject sufficiently bounded for the next intended engineering action?**

This is **Progression Sufficiency**.

Progression Sufficiency is deliberately distinct from eventual implementation completion, validation completion, compliance, release readiness and closure.

A specification may be progression-sufficient for implementation while still containing explicit future measurement obligations. An implementation may be progression-sufficient for integration while still requiring later environmental or system-level validation.

Accordingly:

```text
progression sufficient
!= complete
!= verified
!= compliant
!= released
!= closed
```

## 9. Materiality Stop Rule

For each proposed blocking review issue, the reviewer should determine whether leaving the issue unresolved **at the current horizon** would materially do any of the following:

1. permit materially different externally observable implementation behavior or wire/state behavior;
2. create an authority, source-of-truth or architecture contradiction;
3. create a material correctness, safety, data-integrity, state, timing, capacity, lifecycle, robustness or equivalent engineering risk at the next action;
4. prevent the next intended engineering action from being implemented or meaningfully verified;
5. allow an expensive, difficult-to-reverse or effectively irreversible engineering commitment to occur before the issue can reasonably be resolved.

If at least one answer is **YES**, the issue may legitimately require resolution before progression, subject to applicable authority and engineering judgment.

If all answers are **NO**, the issue shall not block progression **solely for theoretical completeness**.

It may instead be dispositioned as an appropriate later obligation, informative issue or editorial improvement.

The stop rule is a governance sufficiency test. It does not determine the engineering answer and does not prevent a Project Design Authority or applicable external authority from imposing a stricter current requirement within its legitimate authority.

## 10. Engineering Impact Is Not Progression Disposition

Potential engineering impact and current progression disposition are separate dimensions.

A later timing violation may have Major engineering impact while measured timing evidence is not yet available. The current specification review may therefore record:

```text
potential engineering impact: Major
current progression disposition: non-blocking / later evidence required
revisit trigger: first target implementation or defined integration point
```

This is more precise than artificially lowering impact severity merely because the evidence is premature.

Conversely, a seemingly small wording issue may be progression-blocking when it permits two conforming implementers to produce different required behavior.

Therefore:

```text
engineering impact
!= current blocking status
```

v0.0.8rc01 does not create a new canonical finding-severity vocabulary or machine-readable progression-disposition enumeration. It establishes only the semantic separation.

## 11. Deferred Does Not Mean Resolved

A question that is valid but not required for the current horizon may be deferred.

A controlled deferral should identify, as applicable:

```text
what remains unresolved
why it is not blocking now
what future evidence/decision is required
who owns the future action
what event or engineering condition re-opens it
```

A **revisit trigger** shall be concrete enough that the obligation is not silently lost.

Examples include:

- first executable implementation of the relevant path;
- first target-hardware integration;
- availability of a specified measurement point;
- completion of a dependent architecture decision;
- before PCB/tooling/production commitment;
- before validation entry;
- before release review.

Deferred status does not mean:

```text
resolved
verified
accepted risk
waived
not applicable
closed
```

It also does not introduce a fifth Effective Project Profile state and does not redefine `undetermined` or `no_current_disposition`.

## 12. Irreversible-Commitment Boundary

The stop rule includes irreversible or expensive commitments because some decisions must be made before empirical evidence exists.

Examples may include:

- PCB release;
- connector/pin allocation;
- persistent on-media format publication;
- externally consumed wire protocol release;
- irreversible manufacturing/tooling choice;
- field-compatibility commitment.

Where delaying a decision until later evidence would make correction disproportionately expensive or impossible, the current horizon may legitimately require deeper analysis, simulation, margin, prototype evidence or an explicit controlled decision before progression.

Proportional governance therefore does not always mean “less review.” It means **review depth matched to decision consequence and reversibility**.

## 13. SCAF Self-Application Rule

SCAF shall apply the same proportionality discipline to its own development and review.

A SCAF RC shall not be opened or extended solely to improve theoretical completeness when:

- the current development target is sufficiently bounded for its intended next action;
- no material authority/behavior/correctness ambiguity remains for that target;
- later evidence is not yet reasonably producible; and
- deferred questions have controlled revisit triggers where needed.

A clean review may therefore lead to **STOP / defer future capability** rather than automatically opening the next representational, schema or executable RC.

This rule is particularly important for AI-assisted governance, where generating additional hypothetical issues is cheap but engineering evidence and implementation time are not.

## 14. Relationship to Existing Frozen SCAF Semantics

v0.0.8rc01 does not modify or reopen:

- the 294 frozen authority records;
- the 218 PAO / 76 FNI split;
- frozen Authority Kernel semantics;
- L3 Pattern maturity/status semantics;
- Project Application applicability states;
- Effective Project Profile four-state semantics;
- Consumption Selection representation/schema/validator/builder;
- Project Design Authority, Project Realization, verification/evidence or closure ownership.

In particular:

```text
Current Decision Horizon
!= new authority
!= new applicability state
!= new Effective Project Profile state
!= L3 Pattern maturity
!= compliance state
!= closure state
```

The new semantic foundation is framework-development governance guidance pending independent review. It is **not** promoted into `authority-registry.yaml` or frozen normative authority by rc01.

## 15. Representation and Executable Boundary

v0.0.8rc01 is representation-neutral.

It introduces no:

- YAML/JSON record;
- schema;
- validator;
- CI gate;
- authority-registry field;
- Project Application field;
- Effective Project Profile field;
- finding database;
- automatic severity classifier;
- automatic stop-rule decision engine;
- lifecycle-state machine.

A future executable representation shall require a separate dependency/value decision and separate review. rc01 does not pre-authorize one.

## 16. Deliberately Deferred Scope

The following remain outside rc01:

- Context Source Resolution;
- PAO-to-file/document/code/test/evidence mapping;
- context-content records;
- AI context packaging, prompting, orchestration or model selection;
- ranking, priority, severity automation or token-budget policy;
- automatic review-finding classification;
- automatic engineering-stage inference;
- CI enforcement of progression disposition;
- normative authority-registry expansion;
- L4 implementation/verification guidance expansion;
- Development Context Recovery / `.scaf/work-checkpoint.yaml`;
- external trust-model expansion.

These capabilities shall not be inferred merely because proportional-governance semantics now exist.

## 17. Review Gate for rc01

The rc01 review should answer whether the semantic foundation is sufficient to support responsible use without creating a loophole for under-governance or a new bureaucratic state model.

The intended gate is satisfied only if the review confirms, at minimum:

```text
Current Decision Horizon is subject-scoped and authority-neutral
Governance depth is proportional to current decision/consequence/evidence
Not-yet-producible empirical evidence is not a current automatic blocker
Future evidence obligations retain explicit ownership and revisit triggers
Progression Sufficiency is distinct from completion/verification/closure
The five-question Materiality Stop Rule identifies current blocking relevance
Engineering impact remains distinct from current progression disposition
Deferred remains unresolved until its controlled trigger/action is satisfied
Applicable external authority requirements remain fully effective
No new global lifecycle state machine or L3 maturity reinterpretation appears
No frozen v0.0.7 or earlier authority/representation/executable source is modified
SCAF explicitly applies the stop/proportionality rule to its own RC behavior
```

A clean rc01 review authorizes only a later dependency/value check. It does not automatically authorize rc02.

## 18. Plain-Language Summary

This RC solves one engineering-governance problem:

> **SCAF needs a principled way to know how far a review must go now, and when a valid question should be deferred until real implementation or measurement evidence exists.**

It deliberately does **not** solve lifecycle automation, finding automation, CI enforcement, Context Source Resolution or AI context construction.

The intended behavior is simple:

```text
make the next step unambiguous and responsible
        ↓
record what must be proven later
        ↓
stop when further detail no longer changes the current engineering decision
```
