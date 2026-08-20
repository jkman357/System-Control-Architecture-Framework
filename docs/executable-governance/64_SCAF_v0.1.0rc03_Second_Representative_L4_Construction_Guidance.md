# SCAF v0.1.0rc03 — Second Representative L4 Construction Guidance

**Development Release:** v0.1.0rc03  
**Status:** Second Representative L4 Construction Guidance / Review Candidate  
**Date:** 2026-08-20  
**Immediate Predecessor:** accepted v0.1.0rc02 (`4b679e2ef779a998b8cd0781612cab2752cfba4d`)  
**Frozen Basis:** v0.0.2 L1/L2; v0.0.3 L3; v0.0.4 Executable Governance; v0.0.5 L3 Machine-Readable Traceability; v0.0.6 Project Application / Effective Project Profile; v0.0.7 Consumption Selection; v0.0.8 Lifecycle-Proportional Governance; v0.0.9 Context Source Association / Source-Aware Validation; v0.0.10 Controlled Context Assembly / Source-Aware Package Validation

## 1. Decision Purpose

The independent v0.1.0rc02 review returned clean `PASS / GATE YES` with zero Critical/Major/Minor/Trivial candidate-source findings and zero blocking review-evidence limitations. The first representative `SCAF-L4-001` was found locally Construction Ready for bounded queue/backpressure/overload construction while preserving the rc01 semantic/layer contract.

The required post-rc02 dependency/value assessment found one remaining material question before considering a minimal v0.1.0 L4 milestone sufficient:

> **Does the rc01 L4 contract generalize beyond capacity/queue construction to a materially different runtime supervision, lifecycle, independence, escalation and evidence problem?**

The current decision horizon for rc03 is therefore:

> **Author exactly one second representative L4 guidance that composes the frozen Heartbeat / Liveness Supervision and Independent Watchdog with Escalation Patterns, and assess cross-pattern Construction Readiness without introducing L4 executable tooling or broad catalog expansion.**

## 2. Why a Second Representative Is Material

`SCAF-L4-001` exercised:

- finite capacity and exhaustion;
- producer/service relationships;
- concurrency and ordering;
- overload policy;
- resource accounting;
- bounded observability and Verification Intent.

It did not materially exercise:

- progress/liveness semantics;
- supervisor failure semantics;
- watchdog-service ownership;
- supervisor/watchdog independence;
- startup/maintenance/degraded supervision;
- session/incarnation freshness;
- reset classification/domain consequence;
- retained evidence around expiry/reset;
- repeated reset/recovery containment.

A second representative is therefore justified as a bounded generalization check, not as catalog-filling work.

## 3. Candidate L4 Identity

rc03 introduces exactly one new candidate allocation:

```text
SCAF-L4-002
Runtime Health Supervision and Watchdog Construction Guidance
```

The identity is release/path independent under the accepted rc01 contract. It becomes accepted only if the rc03 candidate is accepted and committed.

The already accepted rc02 identity remains:

```text
SCAF-L4-001
Bounded Queue / Backpressure / Overload Construction Guidance
```

No third numeric L4 identity or broader tranche is introduced.

## 4. Many-to-Many Trace Proof

rc03 deliberately exercises the accepted many-to-many L3↔L4 model:

```text
SCAF-PAT-SUP-001 — Heartbeat / Liveness Supervision ─┐
                                                     ├─> SCAF-L4-002
SCAF-PAT-SUP-002 — Independent Watchdog with Escalation ┘
```

Relevant frozen L2 basis is inherited without modifying frozen L3 trace:

```text
SUP-001
Primary:    SCAF-ROB-004, SCAF-ROB-005
Supporting: SCAF-ROB-031, SCAF-OBS-014, SCAF-OBS-015
Constraint: SCAF-TIME-002, SCAF-TIME-006, SCAF-INT-010 where applicable

SUP-002
Primary:    SCAF-ROB-006
Supporting: SCAF-ROB-005, SCAF-ROB-011
Constraint: SCAF-TIME-006, SCAF-LIFE-008, SCAF-LIFE-009
```

Trace does not imply project adoption, applicability, satisfaction, watchdog selection, reset selection or Project Design Authority transfer.

## 5. Construction-Ready Target

The representative should allow a competent engineer or AI consumer to construct a project-specific supervision architecture while identifying rather than inventing project decisions for:

- monitored responsibilities/progress properties;
- progress/heartbeat representation;
- health/liveness classifications;
- supervision ownership;
- watchdog-service eligibility;
- supervisor/watchdog independence;
- timing/deadline/expiry relationships;
- startup/suspend/maintenance/degraded modes;
- session/incarnation freshness;
- escalation/recovery/reset scope;
- supervisor/watchdog failure behavior;
- evidence and observability;
- project-specific verification cases.

Construction Readiness remains separate from buildability, correctness, verification PASS, compliance, release or closure.

## 6. Core Semantic Proof Targets

The candidate must preserve:

```text
liveness evidence != complete system health proof
execution activity != useful progress proof
watchdog expiry != root-cause proof
hardware watchdog != automatic independence proof
example timing value != project timing value
L4 guidance != Project Design Authority
L4 Verification Intent != verification result
```

No concrete heartbeat period, missed count, watchdog timeout, register/API, task priority, reset target or project verification threshold is permitted as a SCAF default.

## 7. Supervision Ownership Proof Target

The representative shall make it possible to identify:

```text
monitored responsibility
        ↓
progress / liveness evidence
        ↓
supervision evaluation owner
        ↓
watchdog service-eligibility owner
        ↓
watchdog / supervisory expiry mechanism
        ↓
PDA-owned escalation / recovery result
```

The construction constraint is not that every project must have one software task called “Health Supervisor.” The required property is that the claimed supervision path cannot be silently defeated by unconditional watchdog servicing from the execution context whose progress is being supervised.

## 8. Timing / Lifecycle Proof Target

The entry shall expose project-owned relationships among progress expectation, evaluation/tolerance, watchdog service/expiry and required response without supplying values.

It shall also force explicit handling of the lifecycle periods most likely to defeat a supervision claim:

- startup / partial initialization;
- intentional suspension;
- maintenance/service mode;
- update/activation where applicable;
- degraded operation with a changed monitored set;
- reset/restart/recovery/reintegration.

An indefinite implicit grace/bypass state is not acceptable as proof of bounded supervision.

## 9. Independence / Failure Proof Target

The representative shall distinguish:

```text
independent label
!= analyzed independence
```

A separate task, hardware watchdog or external supervisor does not by itself prove sufficient independence. The project must identify materially shared scheduler/process/reset/power/clock/memory/communication/resource dependencies relevant to the claim.

The entry shall also preserve `SCAF-ROB-006`: supervisor unavailability, degradation, disagreement or invalid output cannot silently become healthy operation.

## 10. Reset / Evidence Boundary

Watchdog expiry is evidence that a supervision condition was violated. It is not automatically the initiating/root cause.

Where escalation produces reset/restart, the project retains authority for:

- reset classification/cause semantics;
- reset-domain / coordinated participant consequence;
- recovery completion criteria;
- retained-state/evidence validity;
- repeated reset/recovery termination/escalation.

The L4 entry may require construction-visible evidence around expiry but shall not treat evidence as health/failure authority merely because it informs diagnosis.

## 11. Verification Intent Horizon

The representative should include bounded Verification Intent for materially different conditions, including:

1. healthy supervision;
2. one required participant stalls;
3. activity continues without the material progress property;
4. stale/wrong-incarnation evidence;
5. supervisor/observation failure;
6. startup/partial initialization;
7. intentional suspension/maintenance/degraded mode;
8. timing/jitter boundary;
9. watchdog expiry/escalation evidence;
10. repeated recovery/reset-loop containment;
11. claimed independence evidence.

Concrete project values, stimuli, instrumentation, execution and pass/fail remain outside L4 ownership.

## 12. Cross-Representative Generalization Questions

Independent review should determine whether the accepted L4 contract now works across both representative problem classes:

```text
SCAF-L4-001
capacity / overload / concurrency / exhaustion

SCAF-L4-002
runtime progress / supervision / independence / lifecycle / escalation
```

Questions:

1. Does the same Construction Constraint / Invariant / Assumption / Required Project Decision distinction remain useful?
2. Does platform-neutral-first remain workable for watchdog/supervision construction?
3. Does the L4 contract preserve Project Design Authority even when failure/recovery/reset behavior is involved?
4. Can Verification Intent be concrete enough for later project tests without becoming a Test Procedure?
5. Does the many-to-many trace model work for one L4 entry composing two L3 Patterns?
6. Are lifecycle and evidence questions exposed without over-specifying an implementation?
7. Can a consumer begin implementation without hidden timing or reset defaults?

## 13. rc03 Non-Goals

rc03 adds no:

- third L4 identity or broad catalog tranche;
- change to `SCAF-L4-001` construction semantics;
- change to the accepted rc01 L4 contract/template;
- L4 registry/index with machine authority;
- YAML/JSON representation;
- schema;
- validator;
- machine-readable L3↔L4 trace;
- project L4 adoption/pinning record;
- platform-specific watchdog/RTOS/MCU guidance;
- watchdog register/API/reference implementation;
- project Test Procedure;
- code generator;
- CI gate;
- Controlled Context Package builder/materialization-policy work;
- Source Resolver/currentness/model/ranking/token/content-loader capability;
- new L1/L2 authority, PAO/FNI, L3 Pattern or L3 relation.

## 14. Post-Review Rule

A clean rc03 review does not automatically authorize rc04, a third L4 entry or executable L4 governance.

A new dependency/value assessment shall decide among:

- repair if the second representative exposes a real L4 contract defect;
- milestone consolidation / freeze-candidate work if two materially different representative entries demonstrate sufficient L4 generalization and no further capability is required now;
- another narrowly justified representative only if a material untested construction class remains;
- STOP if additional work would be catalog growth for theoretical completeness.

The preferred disposition after a clean cross-representative result is to test whether v0.1.0 is already progression-sufficient rather than continue adding entries by default.

## 15. Expected Source Delta

Expected candidate delta relative to exact committed rc02 predecessor:

```text
Added:   2
Changed: 4
Removed: 0
```

Expected added paths:

- `docs/l4/catalog/SCAF-L4-002_Runtime_Health_Supervision_and_Watchdog_Construction_Guidance.md`;
- `docs/executable-governance/64_SCAF_v0.1.0rc03_Second_Representative_L4_Construction_Guidance.md`.

Expected changed paths:

- `README.md`;
- `CHANGELOG.md`;
- `docs/l4/README.md`;
- `docs/executable-governance/README.md`.

No protected/frozen/executable/schema/registry source path is expected to change.

## 16. Acceptance Position

rc03 is progression-sufficient only if independent review can establish that:

- exactly one new candidate L4 identity exists;
- it faithfully composes frozen `SCAF-PAT-SUP-001` and `SCAF-PAT-SUP-002`;
- L2 authority ownership remains intact;
- supervision/progress/watchdog-service/escalation responsibilities are construction-visible;
- no hidden timing/reset/platform defaults are introduced;
- supervisor failure and independence semantics are bounded;
- startup/maintenance/reset/recovery lifecycle behavior is constructible;
- evidence/observability and Verification Intent are useful but non-authoritative;
- the entry is locally Construction Ready;
- the two representative entries collectively provide credible cross-problem evidence for the L4 layer contract;
- all rc03 non-goals remain absent.

A clean rc03 outcome authorizes only the required post-review dependency/value assessment.
