# SCAF v0.1.0rc01 — L4 Minimum Construction Guidance Semantic and Layer Boundary Foundation

**Development Release:** v0.1.0rc01  
**Status:** L4 Minimum Construction Guidance Semantic and Layer Boundary Foundation / Review Candidate  
**Date:** 2026-08-20  
**Immediate Predecessor:** frozen v0.0.10 (`a4fa740d32b97108b0eb2a55e48296a94435ef95`)  
**Frozen Basis:** v0.0.2 L1/L2; v0.0.3 L3; v0.0.4 Executable Governance; v0.0.5 L3 Machine-Readable Traceability; v0.0.6 Project Application / Effective Project Profile; v0.0.7 Consumption Selection; v0.0.8 Lifecycle-Proportional Governance; v0.0.9 Context Source Association / Source-Aware Validation; v0.0.10 Controlled Context Assembly / Source-Aware Package Validation

## 1. Decision Purpose

The frozen SCAF baseline now determines and validates engineering authority, project application, profile state, downstream consumption selection, controlled source relationships and a source-aware Controlled Context Package.

The next material gap is no longer context construction. It is the engineering transition from an accepted architecture Pattern / Mechanism into a sufficiently bounded construction starting point.

The user-approved v0.1.0 direction is intentionally modest:

> **Introduce one deliberately coarse L4 layer so an engineer or AI has enough controlled construction guidance to begin implementation, while keeping L1/L2 stable, allowing L3 to evolve moderately, and allowing L4 to evolve frequently without rewriting project authority.**

rc01 does not attempt to populate the L4 catalog. It defines the semantic/layer contract under which later representative guidance can be safely authored.

## 2. Why v0.1.0

The transition is milestone-significant:

```text
v0.0.x
engineering authority / applicability / patterns / trace / controlled context
        ↓
v0.1.x
controlled guidance that can support construction
```

The version change does not imply API stability or a complete L4 catalog. It marks the first formally controlled move from architecture/context governance toward construction-facing guidance.

## 3. Engineering Problem

Without an L4 boundary, a consumer can receive correct authority and L3 Pattern context but still reach implementation with an ungoverned gap:

```text
L2 says what must be addressed
        ↓
L3 says what reusable mechanism may be used
        ↓
consumer improvises implementation structure / assumptions / defaults / failure behavior / verification
```

That gap can cause materially different realizations even when consumers start from the same accepted upstream architecture context.

However, over-solving the gap would create a different failure mode: L4 could become hidden authority, over-prescribe project implementation, embed vendor APIs/default values, or retroactively invalidate project decisions whenever guidance changes.

rc01 therefore establishes the minimum safe construction-guidance boundary before any representative entries are accepted.

## 4. Current Decision Horizon

> **Establish a stable semantic and layer-boundary contract under which a small, deliberately coarse L4 guidance tranche can later be authored as construction-ready engineering guidance without creating new framework authority, silently changing L3, over-prescribing project implementation, or conflating guidance with verification/closure.**

The current decision horizon does not require:

- a populated L4 catalog;
- a machine-readable registry or schema;
- L3↔L4 executable trace;
- project-side L4 adoption records;
- platform-specific guidance;
- reference implementations;
- code generation;
- CI enforcement.

## 5. Accepted Layer Strategy

The intended long-term evolution profile is:

```text
L1 / L2   stable normative core
L3        reusable Pattern / Mechanism catalog; moderate evolution
L4        construction / verification guidance; expected frequent evolution
```

High L4 change frequency is expected and is not itself framework instability.

A realization-only improvement belongs in L4. A reusable architecture-mechanism change triggers L3 reassessment. A genuine obligation/authority semantic problem is separately escalated to L1/L2 rather than patched through downstream prose.

## 6. Canonical L4 Position

```text
L1 / L2 concern obligation / authority
        ↓
L3 reusable candidate Pattern / Mechanism
        ↓
L4 construction / verification guidance
        ↓
Project Design Authority
        ↓
Project Realization
        ↓
Project Verification / Assurance Authority
```

Preserved separations:

```text
L4 guidance != new framework authority
L4 recommendation != Project Design Decision
L4 example != canonical implementation
L4 Verification Intent != verification result
Construction Ready != buildable / complete / correct / verified / compliant / closed
```

## 7. L3 ↔ L4 Trace Model

rc01 establishes a representation-neutral many-to-many relationship:

```text
one accepted L3 Pattern -> 0..n L4 guidance entries
one L4 guidance         -> 1..n accepted L3 Patterns
```

This prevents a false parent-child constraint and allows construction guidance that legitimately composes multiple architecture mechanisms.

Trace does not imply adoption, applicability, satisfaction or project authority.

## 8. Stable Identity Foundation

Published L4 identities will use:

```text
SCAF-L4-<NNN>
```

with globally unique monotonically allocated three-digit identities.

rc01 allocates none.

The ID is independent of SCAF release and file path. Compatible clarification may retain identity; materially different construction intent/invariants/decision contract/failure behavior/verification intent requires explicit identity/supersession reassessment.

## 9. Guidance Semantic Classes

rc01 distinguishes:

### Construction Constraint

Condition necessary to preserve the claimed guidance realization in its declared scope, unless PDA materially adapts/departs with rationale where appropriate.

### Recommended Practice

Preferred construction approach; not automatically mandatory.

### Example Realization

One non-canonical illustration; never automatic project truth.

### Required Project Decision

A decision category L4 intentionally leaves to the appropriate project authority.

This separation prevents example/recommendation prose from becoming accidental authority.

## 10. Construction Invariants and Assumptions

L4 shall make architecture-preserving invariants and material assumptions explicit.

```text
Construction Invariant
= property that valid realization variations must preserve for the claimed guidance

Construction Assumption
= condition the guidance relies on but which is not automatically a project fact
```

Assumptions must be confirmed, replaced or rejected by the project if relied upon.

## 11. No Hidden Defaults

rc01 explicitly preserves:

```text
example value != project parameter
recommended default != adopted project value
```

The presence of a number, API, pseudo-code fragment or typical configuration in guidance cannot silently decide the project design.

## 12. Required Construction Dimensions

Later L4 entries shall consider, as materially applicable:

- ownership;
- interfaces / state;
- timing;
- concurrency / reentrancy;
- capacity / resource bounds;
- lifecycle transitions;
- failure / recovery;
- observability;
- verification intent.

A dimension may be explicitly not applicable with a reason. It shall not be silently ignored when material.

## 13. Bounded Capacity Rule

For bounded resources, L4 shall ask what happens at capacity/exhaustion rather than merely recommending larger limits.

This is intended to prevent construction guidance such as "increase queue depth" from replacing analysis of producer burst, consumer service rate, allowable backlog, memory budget and overflow semantics.

The project owns the concrete bound unless upstream authority fixes it.

## 14. Lifecycle Rule

L4 shall not describe only steady-state construction where initialization, partial initialization, reconfiguration, recovery, reset, update or power transitions materially affect correctness.

The applicable lifecycle subset is guidance-specific.

## 15. Observability / Verification Coupling

Construction guidance and verifiability remain coupled:

```text
implementation shape
        ↕
observable behavior
        ↕
Verification Intent
```

L4 should identify what needs to be observable and what property a later project verification must prove, without pretending that the verification has already occurred.

The frozen v0.0.8 Evidence Availability Rule remains applicable: empirical evidence that cannot reasonably exist at the current state shall not be made an artificial blocker.

## 16. Material Deviation Rule

L4 does not create waiver bureaucracy for every implementation variation.

Material PDA rationale is appropriate when a deviation can materially change:

- externally observable behavior;
- interface semantics;
- timing/capacity behavior;
- failure/recovery behavior;
- data integrity;
- state ownership;
- an architecture-preserving invariant;
- observability needed for meaningful verification;
- verification intent;
- expensive/difficult-to-reverse implementation commitment.

## 17. Anti-Over-Specification

rc01 establishes:

> **L4 SHALL constrain implementation only to the depth necessary to preserve the intended architecture, externally meaningful behavior, robustness, observability and verifiability.**

Generic L4 should prefer capability descriptions over vendor API binding.

Platform-specific realization notes may later specialize generic guidance without forcing platform taxonomy into the L4 identity model.

## 18. Composition / Conflict

Multiple L4 entries may apply together.

A material conflict shall not be silently merged. Project Design Authority resolves the project realization and retains material rationale as appropriate.

L4 cannot override applicable upstream SCAF or external authority.

Repeated conflict indicating a reusable mechanism defect should be escalated to L3 rather than accumulated as L4 workaround prose.

## 19. Non-Retroactivity

A later L4 revision does not silently rewrite an already accepted project decision.

Projects consume a controlled SCAF baseline and may explicitly rebaseline/reassess later.

rc01 intentionally does not yet create machine-readable L4 revision pinning or project adoption records.

## 20. Revision / Supersession Boundary

L4 evolution must distinguish at least conceptually between clarification, compatible improvement, behaviorally significant revision and replacement/supersession.

rc01 does not freeze these as status enums.

Material change indicators include changed construction structure, invariant, project-decision category, externally meaningful behavior, timing/capacity semantics, failure/recovery semantics, observability needed for verification or verification intent.

## 21. Partial Catalog Is Allowed

The v0.1.0 baseline does not need complete coverage of all twelve frozen L3 Patterns.

```text
catalog completeness != individual guidance completeness
```

A small representative tranche is acceptable if each accepted guidance is locally Construction Ready for its declared scope.

This permits SCAF to become construction-capable without requiring a large speculative authoring campaign.

## 22. Project Use / Partial Adoption Boundary

Projects may follow, adapt or use a guidance only as reference.

However, they shall not claim full realization of a guidance while silently discarding a material invariant or project-decision boundary.

rc01 does not create usage-state enums or a project-side representation.

## 23. Reference Code Boundary

```text
L4 guidance != reference implementation != code template != code generator
```

Reference realizations may later be linked as supporting artifacts when justified, but they do not become canonical merely because they exist.

## 24. AI-Consumable, Model-Neutral

L4 should be structured enough for human/AI extraction of constraints, recommendations, assumptions, open project decisions, interfaces/state/timing, failures, observability, verification intent and variations.

It shall not embed model-specific prompts, personas or orchestration behavior.

```text
AI-consumable structure != AI-specific prompt
context presented to AI != authority granted to AI
```

## 25. Construction Readiness Acceptance

The eventual v0.1.0 milestone should be judged by demonstrated construction usefulness, not document count.

A representative guidance should allow a new engineer or AI, when given controlled upstream authority / pattern / project context, to:

- describe a coherent first implementation structure;
- identify unresolved Project Design Decisions instead of inventing them;
- distinguish constraint/recommendation/example;
- preserve important invariants;
- expose material assumptions;
- identify failure/recovery and bounded-resource behavior;
- identify observability points;
- state meaningful verification intent;
- begin implementation without mistaking L4 for project authority.

## 26. New Repository Artifacts

rc01 adds:

```text
docs/l4/00_L4_Minimum_Construction_Guidance_Contract.md
docs/l4/README.md
docs/l4/templates/L4_Construction_Guidance_Template.md
```

The template is deliberately non-instantiating: it allocates no `SCAF-L4-<NNN>` identity and is not itself an L4 catalog entry.

## 27. Frozen-Surface Preservation

rc01 does not modify:

- `docs/normative/` frozen v0.0.2 semantic authority;
- `docs/l3/` frozen v0.0.3 Pattern / Mechanism Catalog;
- `authority-registry.yaml`;
- `l3-trace-registry.yaml`;
- existing schemas;
- existing production validators/builders/query APIs;
- `release-integrity/` protected baseline artifacts;
- v0.0.10 Controlled Context Package representation/schema/validator.

No new authority ID, PAO, FNI, L3 Pattern or L3 relation is introduced.

## 28. Explicit Non-Goals

rc01 adds no:

- published L4 guidance entry;
- L4 machine-readable registry;
- L4 schema;
- L4 validator;
- L3↔L4 executable trace registry;
- project-side L4 adoption / revision pinning representation;
- platform-specific API guidance;
- product code;
- reference implementation;
- code template library or generator;
- concrete project Test Procedure;
- CI gate;
- Controlled Context Package builder;
- content loader / ranking / token budget / model adapter;
- Source Resolver/currentness capability;
- L1/L2/L3 frozen-baseline change.

## 29. Why Not Build Tooling Yet

The repository has not yet exercised even one accepted L4 guidance entry. Creating a registry/schema/validator before representative guidance would risk formalizing guessed fields rather than observed construction needs.

The proportional sequence is therefore:

```text
rc01 semantic/layer contract
        ↓
review
        ↓
dependency/value assessment
        ↓
small representative L4 tranche, if justified
        ↓
observe construction friction
        ↓
only then assess machine-readable/tooling needs
```

## 30. Post-Review Gate

A clean rc01 review authorizes only a new dependency/value assessment.

It does not automatically authorize:

- rc02;
- a particular L4 topic;
- an L4 registry/schema;
- broad catalog completion;
- platform profiles;
- reference code;
- executable L4 tooling.

The next RC, if any, must justify the smallest representative construction-guidance tranche by construction value and dependency rather than roadmap momentum.
