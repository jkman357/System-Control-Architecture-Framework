# SCAF L4 Minimum Construction Guidance Contract

**Development Release:** v0.1.0rc01  
**Upstream Baselines:** frozen v0.0.2 L1/L2; frozen v0.0.3 L3; frozen v0.0.10 controlled-context baseline  
**Framework Plane:** downstream construction guidance; non-authoritative realization aid  
**Status:** Review Candidate semantic / layer-boundary foundation

## 1. Purpose

L4 exists to bridge accepted architecture reasoning into construction-ready engineering guidance without turning SCAF into Project Design Authority, a product implementation, a coding-standard repository, or a test-procedure repository.

The governing intent is:

> **L4 provides concrete implementation and verification guidance sufficient to begin responsible construction while leaving project-specific architecture values, ownership choices, thresholds, platform bindings, implementation details and final verification decisions under the appropriate project authorities.**

L4 is deliberately expected to evolve more frequently than the frozen L1/L2 normative core and the L3 Pattern / Mechanism Catalog.

## 2. Layer Position

The canonical chain is:

```text
L1 / L2 — concern obligation / authority
        ↓
L3 — reusable candidate Pattern / Mechanism
        ↓
L4 — construction / verification guidance
        ↓
Project Design Authority
        ↓
Project Realization
        ↓
Project Verification / Assurance Authority
```

The chain does **not** mean that L4 owns project implementation decisions.

The governing distinctions are:

```text
L2 obligation
!= L3 pattern selection
!= L4 guidance adoption
!= Project Design Decision
!= implementation
!= verification result
!= closure
```

and:

```text
L4 guidance
!= new framework authority
!= Project Design Authority
!= Project Realization
!= Project Verification / Assurance Authority
```

## 3. L4 Authority Boundary

L4 may:

- describe a concrete implementation shape that preserves an accepted L3 mechanism intent;
- expose construction invariants that should remain true for a claimed realization of the guidance;
- identify assumptions that a project must confirm, replace or reject;
- identify project decisions that remain intentionally unresolved;
- describe interface, state, timing, concurrency, lifecycle, capacity, failure and recovery considerations;
- identify diagnostic / observability hooks needed to make behavior inspectable;
- state verification intent and bounded negative conditions relevant to the construction guidance;
- describe legitimate variants and trade-offs;
- provide clearly marked non-canonical example realizations;
- relate to one or more accepted L3 Patterns / Mechanisms.

L4 shall not:

- create a new L1/L2 obligation through guidance prose;
- silently change an accepted L3 Pattern / Mechanism;
- select a project architecture value, threshold, topology, owner, platform API or concrete implementation on behalf of Project Design Authority;
- treat a recommendation or example as a mandatory universal project implementation;
- define project verification results, compliance status, release readiness, accepted risk or closure;
- claim that following L4 proves implementation correctness;
- grant engineering authority to a human, AI, model, agent or other consumer;
- grant content-use, redistribution, licensing or access authorization;
- require empirical evidence that the current engineering state cannot reasonably produce;
- become a hidden code-template, generated-code, platform SDK or product implementation repository.

## 4. Construction-Ready, Not Immediately Buildable

L4 targets **Construction Readiness**.

Construction Ready means that, within the declared guidance scope, an engineer or AI can identify:

- the intended implementation structure;
- the L2/L3 architecture basis;
- the project decisions still requiring explicit ownership;
- the construction constraints and invariants that must be preserved for the claimed guidance realization;
- assumptions requiring project confirmation;
- relevant state / interface / timing / concurrency / capacity / lifecycle behavior;
- major failure and recovery behavior;
- observability expectations;
- verification intent and important invalid/incomplete construction conditions;
- legitimate variations and trade-offs.

Construction Ready does **not** mean:

```text
source code compiles immediately
implementation is complete
implementation is correct
verification has passed
requirements are satisfied
compliance is complete
release is ready
closure is achieved
```

A generic L4 entry may remain platform-neutral and still be Construction Ready.

## 5. L3 ↔ L4 Relationship

L3 and L4 are related by controlled trace, not by a one-parent / one-child file hierarchy.

Allowed cardinality is conceptually:

```text
one L3 Pattern      -> 0..n L4 guidance entries
one L4 guidance     -> 1..n relevant L3 Patterns
```

A project may also have no accepted L4 guidance for a selected L3 Pattern.

Therefore:

```text
no L4 guidance
!= L2 obligation is not applicable
!= L3 Pattern is invalid
!= project implementation decision is unnecessary
```

The absence of L4 means only that SCAF does not yet provide a controlled construction aid for that scope.

L4 trace does not mean:

```text
L3 selected
!= L4 automatically adopted
L4 available
!= L4 project-selected
L4 traced
!= L2 satisfied
```

## 6. Stable L4 Identity

Published L4 guidance identities use:

```text
SCAF-L4-<NNN>
```

where `<NNN>` is a globally unique three-digit number allocated monotonically when an actual L4 guidance entry is first published.

Rules:

1. a published L4 identity is not reused for a different construction guidance concept;
2. version numbers are not embedded in the identity;
3. editorial clarification or compatible refinement may retain the same identity;
4. a materially different construction intent, invariant set, project-decision contract, failure/recovery behavior or verification intent requires explicit reassessment of whether a new identity and `Supersedes` relation are required;
5. L4 identity is independent of file path and SCAF release number;
6. rc01 allocates no actual L4 entry identity.

This global identity form intentionally avoids forcing one L4 entry under a single L3 family when the guidance legitimately spans multiple accepted Patterns.

## 7. Guidance Strength and Content Classes

L4 content shall distinguish at least the following semantic classes.

### 7.1 Construction Constraint

A Construction Constraint describes a condition that must remain true **when a project claims realization of the guidance in the stated scope**, unless Project Design Authority materially adapts or departs from that guidance and records the necessary rationale.

A Construction Constraint is not a new universal L2 obligation.

### 7.2 Recommended Practice

A Recommended Practice describes a generally preferred construction approach whose adoption remains a project decision.

```text
recommended
!= mandatory
```

### 7.3 Example Realization

An Example Realization illustrates one possible conforming approach.

Every example is non-canonical:

> **An example realization illustrates one possible conforming approach and is not the canonical implementation.**

Example values, names, sequence details or pseudo-code shall not silently become Project Design Decisions.

### 7.4 Required Project Decision

A Required Project Decision identifies a decision category that must be resolved by the appropriate project authority before the applicable construction can be considered sufficiently bounded.

Examples include:

- ownership;
- timing thresholds;
- capacity / queue depth;
- retry / backoff limits;
- escalation behavior;
- authoritative state selection;
- recovery consequences;
- persistence / retention budgets;
- platform binding;
- verification thresholds.

L4 identifies the decision; the project supplies the answer.

## 8. No Hidden Defaults

L4 shall not silently convert illustrative or typical values into project parameters.

```text
example value
!= recommended default
!= adopted project value
```

If a guidance entry presents a typical or recommended value, it shall remain clearly subordinate to an explicit Project Design Decision unless an upstream authority already fixes the value.

AI or human consumers shall not infer project adoption merely because a value appears in an L4 example.

## 9. Construction Invariants

An L4 entry should expose invariants whose preservation defines the intended construction semantics.

Examples of invariant form include:

```text
exactly one role owns a critical state transition
invalid input cannot silently update authoritative state
bounded recovery cannot be indefinitely extended by internal retries
loss of supervised progress cannot be hidden by unrelated healthy participants
persistent replacement cannot expose an intermediate state as committed truth
```

These are examples of invariant **form**, not allocated L4 requirements.

Construction Invariants are especially useful because they connect:

```text
architecture intent
        ↓
construction
        ↓
invalid-condition verification
```

An invariant shall not invent a new upstream obligation; it must remain justified by the traced L3 mechanism and applicable authority context.

## 10. Construction Assumptions

L4 shall expose material assumptions rather than bury them in prose.

Typical assumption categories include:

- monotonic timing availability;
- bounded scheduling or service latency;
- atomicity properties;
- persistence durability behavior;
- ordering guarantees;
- independently controllable recovery/reset capability;
- buffer ownership;
- transport delivery properties;
- execution-context restrictions.

The governing distinction is:

```text
L4 assumption
!= project fact
```

A project that relies on the assumption must confirm it, replace it with a controlled project decision, or reject/adapt the guidance.

## 11. Required Construction Questions

An L4 entry shall consider the following dimensions to the depth material for its scope. A dimension may be explicitly `Not Applicable` where genuinely irrelevant.

### 11.1 Ownership

Identify decisions such as:

- who initializes;
- who owns authoritative state;
- who may write or transition state;
- who retries or escalates;
- who owns a buffer / queue / persistent record;
- who observes / reports failure;
- who owns recovery activation.

### 11.2 Interface and State

Identify:

- externally meaningful interface semantics;
- state ownership and transition responsibility;
- invalid-state handling;
- ordering / freshness requirements;
- initialization and re-entry assumptions.

### 11.3 Timing

Identify timing quantities or relationships that must be decided, without inventing project values.

### 11.4 Concurrency / Reentrancy

Ask whether:

- multiple execution contexts may invoke the mechanism;
- state may be modified concurrently;
- ISR/task/thread boundaries matter;
- reentrancy is allowed;
- ordering/serialization ownership is required.

### 11.5 Capacity / Resource Bounds

Identify bounded-resource questions such as:

- producer burst;
- consumer service rate;
- backlog;
- queue/buffer/storage capacity;
- memory or processing budget;
- overflow / exhaustion behavior.

### 11.6 Lifecycle

Consider behavior across materially relevant phases such as:

```text
initialization
partial initialization
entry to operation
normal operation
reconfiguration
recovery / reintegration
shutdown / reset
update / activation
power transition
```

L4 shall not describe only steady-state behavior where lifecycle transitions materially affect correctness.

### 11.7 Failure / Recovery

Identify:

- detectable invalid/failure conditions;
- containment behavior;
- retry / escalation boundary;
- recovery ownership;
- degraded behavior;
- evidence retained through recovery where material.

## 12. Bounded Capacity and Exhaustion

Where a mechanism consumes a bounded resource, L4 shall ask:

> **What happens when the mechanism reaches its bounded capacity?**

The project should be able to decide the relevant overflow/exhaustion semantics rather than merely increasing an arbitrary limit.

Typical cases include:

```text
queue full
buffer full
storage full
retry exhausted
pending-work limit reached
resource allocation unavailable
processing deadline exceeded
```

The exact policy remains project-owned unless fixed by upstream authority.

## 13. Observability Coupling

L4 construction guidance shall ask:

> **What must be observable to determine whether this mechanism behaved as intended?**

Applicable observability may include:

- current state;
- transition cause;
- error / rejection reason;
- timeout cause;
- retry / escalation count;
- last successful operation;
- selected authoritative source/copy;
- recovery reason;
- reset cause;
- data-integrity failure;
- capacity/overflow event.

L4 may define the observation intent; the project owns concrete logging, event, telemetry, retained-evidence and storage decisions.

## 14. Verification Guidance Boundary

L4 defines **Verification Intent**, not a project verification result or necessarily a concrete project Test Procedure.

Canonical separation:

```text
L4 Verification Intent
        ↓
Project-specific verification design / test case
        ↓
executed evidence
        ↓
Project Verification / Assurance decision
```

An L4 entry should identify:

- observable property to prove;
- important valid / invalid conditions;
- expected externally meaningful behavior;
- relevant timing/capacity/failure boundaries;
- future empirical evidence expected when it becomes reasonably producible.

L4 shall not require empirical evidence before the engineering state can reasonably produce it.

Therefore:

```text
verification guidance present
!= verification executed
verification executed
!= verification passed
verification passed
!= obligation closed
```

## 15. Invalid / Incomplete Construction Conditions

An L4 entry should state bounded machine- or review-checkable conditions that would make a claimed realization inconsistent or materially incomplete for the guidance scope.

These conditions should focus on architecture-preserving construction properties, for example:

- missing required owner;
- contradictory state ownership;
- missing failure path that is necessary to preserve the L3 mechanism;
- unbounded retry where the mechanism requires bounded progress;
- hidden project parameter left undecided;
- missing observability required to verify a critical behavior;
- example value used as an implicit project decision;
- lifecycle transition left undefined where it materially changes behavior.

They shall not convert unresolved engineering judgment into deterministic invalidity merely because a project has not yet reached the relevant decision horizon.

## 16. Material Deviation

A project may follow, adapt or depart from L4 guidance.

L4 shall not require waiver bureaucracy for every local implementation difference.

A material deviation rationale is appropriate when the variation can materially affect one or more of:

- externally observable behavior;
- interface semantics;
- timing/capacity behavior;
- failure / recovery behavior;
- data integrity;
- state ownership;
- architecture-preserving invariant;
- observability needed for meaningful verification;
- verification intent;
- an expensive or difficult-to-reverse implementation commitment.

Non-material implementation freedom remains project-owned without special SCAF ceremony.

## 17. Anti-Over-Specification Rule

> **L4 SHALL constrain implementation only to the depth necessary to preserve the intended architecture, externally meaningful behavior, robustness, observability and verifiability.**

L4 shall avoid unnecessary prescription of:

- variable/function names;
- file/module names;
- exact code layout;
- vendor-specific APIs;
- device register values;
- arbitrary numeric defaults;
- product-specific directory/table/storage layouts;
- concrete test-step sequences that belong to project verification artifacts.

Specific details may appear only where they are essential to the guidance scope or are clearly isolated as platform/reference examples.

## 18. Platform-Neutral First

Generic L4 guidance should prefer capability descriptions over vendor/product names.

Prefer:

```text
execution environment provides independently schedulable participants
platform provides a monotonic time source
recovery mechanism can independently reset/restart the protected execution context
storage provides the stated atomicity/durability property
```

over prematurely binding generic guidance to a specific RTOS, MCU, OS, language, library or API.

Platform-specific realization notes may later specialize generic guidance without changing the generic L4 identity where the construction semantics remain compatible.

rc01 defines no platform-note representation or registry.

## 19. Applicability / Preconditions Boundary

L4 may state construction preconditions and unsuitable conditions.

These answer:

> **When is this guidance a valid construction aid for the selected mechanism?**

They do not create a second Project Application system.

```text
L4 construction precondition
!= Project Application applicability disposition
```

A guidance entry may say `Not suitable when ...` without setting the upstream L2 obligation or L3 Pattern to `not_applicable`.

## 20. Composition and Conflict

Multiple L4 entries may legitimately apply to the same project construction scope.

When guidance entries compose cleanly, the project may use them together.

When they conflict materially:

```text
L4 conflict
        ↓
shall not be silently merged
        ↓
Project Design Authority resolves the project realization
        ↓
material rationale retained where required
```

L4 cannot override applicable L1/L2 or external authority.

A repeated conflict that reveals a reusable architecture-mechanism problem should trigger L3 reassessment rather than indefinite L4 workaround accumulation.

## 21. L4 ↔ L3 Escalation Rule

Use the lowest layer that genuinely owns the change:

```text
change only affects realization detail
        -> keep in L4

change alters reusable architecture mechanism / selection semantics
        -> reassess L3

change reveals obligation / authority semantic defect
        -> separately reassess L1/L2 authority baseline
```

A frequent L4 change rate is not itself framework instability.

The intended evolution profile is:

```text
L1/L2  very low change rate
L3     moderate evolution
L4     expected frequent evolution
```

## 22. Non-Retroactivity and Project Pinning

A later L4 revision shall not silently rewrite an already accepted project architecture decision.

```text
new L4 revision
!= retroactive Project Design Decision change
```

Projects consume a controlled SCAF baseline and may later rebaseline/reassess explicitly.

Future project-side records may pin L4 identities/revisions more precisely if concrete use demonstrates that need. rc01 defines no machine-readable pinning representation.

## 23. Revision / Supersession Semantics

L4 is expected to evolve. The framework shall preserve enough distinction to tell whether a change is:

- editorial clarification;
- compatible guidance improvement;
- behaviorally significant guidance revision;
- replacement/supersession.

rc01 does not freeze these as machine-readable status enums.

A change is materially significant when it changes one or more of:

- implementation structure required to preserve the guidance;
- construction invariant;
- required project-decision category;
- externally meaningful behavior;
- timing/capacity semantics;
- failure/recovery behavior;
- observability required for verification;
- verification intent.

Historical published identities shall not be deleted merely because a newer guidance replaces them.

## 24. Catalog Completeness vs Entry Completeness

The first L4 baseline may intentionally contain only a small representative tranche.

```text
L4 catalog completeness
!= individual L4 guidance completeness
```

The catalog may be partial, but an entry accepted as Construction Ready should be locally sufficient for its declared scope rather than silently unfinished.

This permits a deliberately coarse first L4 baseline without pretending comprehensive coverage.

## 25. Partial Use / Adaptation

Projects may use only part of a guidance or adapt it, but shall not claim full realization while discarding a material invariant or decision boundary without acknowledgement.

rc01 does not freeze `adopted / adapted / reference-only` as project-side status enums. Actual usage-state representation remains deferred until concrete project consumption demonstrates need.

## 26. Reference Code / Templates Boundary

L4 itself is engineering guidance.

```text
L4 guidance
!= reference implementation
!= code template
!= code generator
```

A future L4 entry may link to a controlled reference realization as supporting evidence or example, but the reference code does not automatically become the canonical implementation.

Reference code, platform adapters, generators and templates require separately justified capability decisions.

## 27. AI / Consumer Boundary

L4 should be structured so that an engineer or AI can reliably extract:

- constraints;
- recommendations;
- assumptions;
- open Project Design Decisions;
- interfaces/state/timing;
- failure/recovery behavior;
- observability;
- verification intent;
- variations/trade-offs.

L4 shall remain model-neutral engineering content.

It shall not embed model-specific personas, prompts, orchestration instructions or conversation-state assumptions.

```text
AI-consumable structure
!= AI-specific prompt
context presented to AI
!= authority granted to AI
```

## 28. Minimum L4 Entry Structure

A later published L4 guidance entry should contain, at minimum:

1. Identity / Title / Status;
2. Purpose / Scope;
3. L2 / L3 Trace;
4. Construction Preconditions / Not-Suitable Conditions;
5. Recommended Implementation Shape;
6. Construction Constraints;
7. Construction Invariants;
8. Construction Assumptions;
9. Required Project Decisions;
10. Interface / State / Timing / Concurrency / Capacity / Lifecycle Considerations as applicable;
11. Failure / Recovery Behavior;
12. Diagnostics / Observability;
13. Verification Intent;
14. Invalid / Incomplete Construction Conditions;
15. Known Variations / Trade-offs;
16. Material Deviation Considerations;
17. Example Realization, if any, clearly non-canonical;
18. Provenance / Reference Basis;
19. Revision / Supersession notes when applicable.

The repository template introduced in rc01 is an authoring aid for this contract. It does not allocate an L4 identity or create a new machine-readable authority source.

## 29. Construction Readiness Acceptance Concept

The v0.1.0 milestone should eventually be evaluated by whether representative L4 guidance allows a new engineer or AI, given controlled upstream authority / pattern / project decisions, to:

- describe a coherent first implementation structure;
- identify remaining Project Design Decisions rather than inventing them;
- distinguish constraints, recommendations and examples;
- preserve important invariants;
- identify material assumptions;
- identify failure/recovery and bounded-resource behavior;
- identify observability points;
- state meaningful verification intent;
- begin a first project realization without treating L4 as project authority.

This is the milestone-level **Construction Readiness** concept.

It is not satisfied merely by counting Markdown files.

## 30. Lifecycle-Proportional Governance

L4 follows the frozen v0.0.8 proportional-governance rules.

A review shall not block a guidance merely because field evidence or measurements cannot yet exist at the current decision horizon.

When later evidence will be required but is not yet producible, the guidance should identify, as applicable:

- the property to observe or measure;
- its semantic meaning;
- observation / measurement boundary;
- owner;
- future evidence trigger;
- present construction constraints preserving future verifiability.

The Materiality Stop Rule applies to L4 development itself. SCAF shall not expand the L4 catalog, schema or tooling solely for theoretical completeness.

## 31. rc01 Deliberate Non-Goals

v0.1.0rc01 does **not**:

- instantiate a published L4 guidance entry;
- allocate a real `SCAF-L4-<NNN>` identity;
- create an L4 machine-readable registry;
- create an L4 JSON/YAML schema;
- create an L4 validator;
- create an L3↔L4 machine-readable trace registry;
- change the frozen L3 Pattern bodies or their `Available / M2` lifecycle state;
- change the frozen 294 / 218 / 76 authority inventory;
- create new PAOs or FNIs;
- create project-side L4 adoption/pinning records;
- define platform-specific implementation APIs;
- provide product-specific code;
- create a code generator or reference implementation;
- create project test procedures;
- reopen the v0.0.10 Controlled Context Package builder decision;
- change source resolution/currentness semantics;
- add CI enforcement.

A clean rc01 review authorizes only a new dependency/value assessment for the smallest representative L4 construction-guidance tranche.

## 32. Current Decision Horizon

The rc01 decision horizon is intentionally narrow:

> **Establish a stable semantic and layer-boundary contract under which a small, deliberately coarse L4 guidance tranche can later be authored as construction-ready engineering guidance without creating new framework authority, silently changing L3, over-prescribing project implementation, or conflating guidance with verification/closure.**

No broader L4 completion claim is made.
