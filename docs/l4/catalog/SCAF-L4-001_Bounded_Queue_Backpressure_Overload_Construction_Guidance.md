# SCAF-L4-001 — Bounded Queue / Backpressure / Overload Construction Guidance

**Development Release:** v0.1.0rc02
**L4 ID:** `SCAF-L4-001` — candidate allocation; becomes accepted only if the rc02 candidate is accepted
**Status:** Representative L4 Construction Guidance / Review Candidate
**Primary L3 Trace:** `SCAF-PAT-TIM-001` — Bounded Queue / Backpressure / Overload Protection
**Upstream Baselines:** frozen v0.0.2 L1/L2; frozen v0.0.3 L3; accepted v0.1.0rc01 L4 semantic/layer contract
**Supersedes:** None

## 1. Purpose / Scope

This guidance turns the accepted `SCAF-PAT-TIM-001` mechanism into a construction-ready starting point for bounded producer/consumer pipelines without deciding project-specific queue depth, thresholds, APIs, scheduling policy, loss semantics, or recovery outcomes.

It applies to software, firmware, host, SoC, FPGA-adjacent control software, distributed participants, storage pipelines, work schedulers, message paths and other systems where produced work can temporarily or persistently exceed service capacity and where finite buffering/admission materially affects timing, resource use, ordering, freshness or failure behavior.

The construction objective is:

> **Place an explicit finite admission/accumulation boundary between demand and constrained service capacity, define what happens when that boundary cannot accept more work, and retain enough observability and verification intent to prove the bounded behavior without treating a larger queue as proof of overload correctness.**

This guidance is not a universal requirement to use a queue. Direct handoff, fixed-rate sampling, coalescing, reservation, credit control, load shedding or other architectures may realize the same upstream obligations when selected by Project Design Authority.

## 2. L2 / L3 Trace

### 2.1 Relevant L2 authority / concern basis

This L4 guidance does not create new L1/L2 authority. It elaborates construction questions already present in the frozen upstream basis traced by `SCAF-PAT-TIM-001`.

Primary basis:

- `SCAF-TIME-009` — where produced demand can exceed service capacity or buffering can grow, the project defines boundedness, capacity and backpressure/admission requirements needed to prevent uncontrolled accumulation or hidden loss of timing/capacity assumptions.
- `SCAF-TIME-012` — where overload, starvation or unfair service can violate a required temporal/capacity property, the project defines the measurable unacceptable condition, limit/bound and architecture-level constraint.

Supporting basis:

- `SCAF-TIME-010` — required capacity, expected demand basis and applicable margin/tolerance remain project decisions.
- `SCAF-TIME-011` — finite queue/buffer/storage/processing resources consume controlled budgets and margin/headroom.
- `SCAF-TIME-013` — long-duration accumulation requires an operating-horizon basis and measurable bounded growth/capacity.

Constraint inputs retained from L3:

- `SCAF-ROB-016` — once a controlled TIME capacity/resource bound is violated and robustness is materially affected, ROB retains authority for the health/failure interpretation and containment/degradation/recovery outcome.
- `SCAF-INT-007` — ordering, duplicate, missing, reordered and superseded information semantics constrain drop/coalesce/reorder policies where applicable.
- `SCAF-INT-008` — freshness-state meaning and consumer-visible stale/expired/invalid consequences constrain queue age/discard behavior where applicable.

### 2.2 Relevant L3 Pattern / Mechanism

- `SCAF-PAT-TIM-001` — **primary construction trace**. This L4 guidance elaborates the Pattern's finite admission/accumulation boundary, explicit overload consequence and measurable occupancy/age/resource behavior.

Commonly composed L3 Patterns remain separate selections, not implicit adoption:

- `SCAF-PAT-REC-001` — when retries materially add demand and require bounded retry/escalation treatment;
- `SCAF-PAT-FTL-001` — when overload propagation across failure domains requires containment;
- `SCAF-PAT-EVD-001` — when overload/queue evidence must be retained across an incident window.

Trace does not imply automatic project adoption, applicability, satisfaction or Project Design Authority transfer.

## 3. Construction Preconditions

Use this guidance when the project can identify a meaningful demand admission point and can define a finite capacity or finite outstanding-work bound.

Material preconditions typically include:

- producer demand can be described with at least a bounded burst, rate, arrival model, outstanding-work limit or equivalent demand basis;
- consumer/service capacity can be described with at least a bounded service-rate, service-latency, service-pause or equivalent capacity basis;
- the project can determine what semantic consequence is permitted when capacity is unavailable;
- the implementation environment can represent finite admission state and preserve the required ordering/data semantics under the expected concurrency model;
- where age/freshness matters, a suitable time/age basis is available;
- where backpressure is chosen, the producer or upstream admission owner can actually observe and honor the backpressure consequence, or the project defines an alternative reject/drop/degrade consequence.

These are L4 construction preconditions, not Project Application dispositions.

### 3.1 Not Suitable When Applied As-Is

Do not apply this guidance as if a conventional queue were mandatory when:

- the architecture intentionally uses synchronous direct handoff with no meaningful accumulation boundary;
- the required behavior is better represented as latest-value sampling/coalescing rather than queued history;
- the producer cannot be slowed or rejected and semantic loss/degradation has not been defined;
- the project requires effectively unbounded historical retention rather than bounded operational work buffering;
- a different selected mechanism owns the relevant admission/capacity behavior.

Absence of this guidance from a project does not make the upstream TIME concern non-applicable.

## 4. Recommended Implementation Shape

A generic construction shape is:

```text
Producer(s)
    ↓ demand
Admission / Overload Policy Boundary
    ├─ capacity / reservation decision
    ├─ ordering / class decision
    ├─ backpressure / reject / drop / coalesce / replace / degrade consequence
    └─ overload observability
    ↓ accepted work only
Finite Accumulation / Outstanding-Work Boundary
    ↓ service
Consumer(s)
    └─ service / progress observability
```

The key construction boundary is not the container type. It is the point where the project can answer:

```text
Can this work be admitted now?
If yes, under what ordering / age / ownership semantics?
If no, what controlled consequence occurs?
How will the project observe that consequence and prove it remains within the intended bound?
```

A ring buffer, RTOS queue, mailbox, channel, request table, token/credit counter, fixed slot pool, work scheduler, storage queue or another finite representation can realize the shape. L4 does not select the platform primitive.

## 5. Construction Constraints

A realization claiming this guidance shall preserve the following within its declared project scope:

1. **Finite admission/accumulation:** the amount of admitted but uncompleted work governed by this mechanism has an explicit finite capacity or finite outstanding-work bound.
2. **Defined exhaustion consequence:** when new demand cannot be admitted within that bound, the implementation follows a project-defined consequence rather than silently relying on unbounded growth.
3. **Semantic preservation:** rejection, dropping, overwriting, coalescing, reordering or replacement may occur only under project-defined semantics consistent with applicable Interaction/data-contract authority.
4. **Capacity is not proof by itself:** increasing queue/buffer capacity is not sufficient evidence that overload, starvation, latency, freshness or long-duration accumulation is controlled.
5. **Observable boundedness:** the project can obtain evidence sufficient to determine whether the controlled capacity/age/service assumptions are being maintained for the claimed operating horizon.
6. **No hidden secondary accumulation:** a bounded primary queue shall not be treated as bounded end-to-end behavior if retries, driver buffers, transport buffers, deferred work, spill storage or another downstream/upstream structure can accumulate materially without an analyzed bound.
7. **Concurrency-safe accounting:** admission, completion, replacement and discard accounting preserve the claimed capacity and ordering semantics under the project concurrency model.
8. **ROB boundary preserved:** when violation of the TIME-owned bound has a health/failure consequence, the project traces the interpretation and containment/degradation/recovery outcome to the applicable ROB/RUN project decision rather than inventing it in the queue implementation.

These are conditions for the claimed L4 realization. They do not create new universal L2 obligations.

## 6. Construction Invariants

Valid realization variations shall preserve, as applicable:

- admitted outstanding work cannot exceed the project-defined finite bound without entering a separately controlled bounded spill/overflow mechanism;
- every capacity-unavailable outcome maps to one explicit project-owned disposition for the relevant work/information class;
- work that is rejected/dropped/coalesced/replaced is not simultaneously represented as normally accepted work;
- ordering/freshness semantics remain consistent with the project Interaction contract for accepted and discarded/superseded information;
- service completion, discard, replacement and cancellation release or transfer ownership/accounting exactly once according to the project model;
- overload behavior does not depend on an assumption of infinite memory, infinite producer blocking time or infinite consumer catch-up time;
- observability used to claim bounded behavior is sampled/retained at a resolution sufficient for the project-defined overload or starvation condition.

If a project deliberately adapts one of these invariants because another realization preserves the same upstream architecture intent, the material adaptation belongs to Project Design Authority and should retain rationale proportional to impact.

## 7. Construction Assumptions

This guidance does not turn the following assumptions into project facts. The project shall confirm, replace or reject each material assumption it relies upon:

- the producer demand model represents relevant peak, sustained and burst behavior over the intended operating horizon;
- the consumer/service model includes material scheduler, I/O, transport, storage or peer delays rather than only nominal service time;
- capacity accounting includes payload plus material metadata/alignment/descriptor/storage overhead;
- any chosen backpressure path can actually influence upstream admission or has an explicitly defined fallback consequence;
- the synchronization primitive/ownership model preserves atomic capacity and ordering semantics under all allowed execution contexts;
- any age/freshness evaluation uses a timebase suitable for the intended comparison;
- any secondary spill, retry or deferred-work path is separately bounded and included in the end-to-end accumulation analysis;
- overload observability is available before peak occupancy, starvation or discard evidence is irretrievably lost.

```text
L4 assumption != project fact
```

## 8. Required Project Decisions

Project Design Authority shall decide the following where materially applicable. L4 identifies the decision categories; it does not supply project values.

### 8.1 Demand model

Define, by relevant work class:

- expected sustained arrival rate or equivalent demand basis;
- maximum credible burst size and/or burst duration;
- number/concurrency of producers if it changes aggregate demand;
- retry/replay/reconnect/recovery traffic that can add demand;
- intended operating horizon for accumulation analysis.

### 8.2 Service-capacity model

Define:

- expected and minimum credible service capacity;
- worst credible service pause or blocking interval relevant to backlog;
- material scheduling/priority/interference assumptions;
- downstream bottlenecks that can make apparent queue service completion differ from true end-to-end completion.

### 8.3 Capacity and margin basis

Define:

- finite queue/buffer/outstanding-work capacity;
- resource budget consumed by that capacity;
- required margin/headroom or controlled rationale for no separate margin;
- any per-class reservation or shared-capacity rule.

The capacity value shall be a project decision. No number in an example or recommendation becomes the project value automatically.

### 8.4 Admission and exhaustion policy

For each materially distinct work/information class, define what happens when capacity is unavailable. Candidate policy families include:

- apply backpressure / block admission within a separately bounded wait/deadline;
- reject newest work;
- drop or evict oldest work where history loss is semantically permitted;
- coalesce or replace superseded work;
- reserve capacity for a protected class;
- shed lower-priority work;
- enter a degraded/overload operating state;
- escalate to a separately owned health/failure response.

No policy in this list is the SCAF default.

### 8.5 Ordering, fairness and freshness

Define, where applicable:

- FIFO, priority, deadline, key-based or other ordering semantics;
- fairness/starvation limits between competing classes;
- duplicate/missing/superseded semantics;
- maximum acceptable queued age or freshness condition;
- treatment of stale/expired work before service.

### 8.6 Ownership

Define:

- owner of queue/admission state;
- producer-side ownership transfer point;
- consumer-side completion/release point;
- who may cancel, replace, coalesce or discard work;
- who changes overload/degraded state;
- who owns recovery/re-enable after overload;
- who owns evidence/counters used to prove the bounded behavior.

### 8.7 Recovery / escalation

Define what ends an overload episode and, where material:

- when normal admission may resume;
- whether hysteresis/recovery delay is required to avoid oscillation;
- what persistent overload means to runtime/robustness health;
- whether work is drained, discarded, replayed, reconstructed or abandoned after recovery/reset.

### 8.8 Verification thresholds / evidence

Define measurable project thresholds or criteria needed to verify:

- maximum occupancy / outstanding work;
- unacceptable overload duration;
- maximum queueing age/latency where relevant;
- rejection/drop/coalescing behavior;
- starvation/fairness limits;
- recovery behavior;
- resource usage and margin.

## 9. Interface / State Considerations

The implementation shall make the admission result semantically unambiguous to its caller/upstream owner. Examples of meaningful outcomes include accepted, not accepted because capacity is unavailable, superseded/coalesced, or accepted under a defined degraded policy. Exact API/result names are project-specific.

Where overload state affects externally meaningful behavior, define the state/condition semantics and transition ownership. A project may use explicit states such as normal/pressured/exhausted/recovering, watermarks, credit counts or other representations; this guidance does not require those names or a particular state machine.

If an item carries ordering, sequence, epoch, freshness or provenance semantics, the queue implementation shall not erase the contract meaning merely because the item is buffered.

## 10. Timing Considerations

The project shall establish a demand/service basis sufficient to justify the chosen capacity and latency/freshness behavior.

One possible analysis aid is the maximum positive difference between cumulative arrivals and cumulative service over the analyzed operating/burst window:

```text
required backlog basis ≈ max over relevant windows
                         (admitted demand - completed service)
```

This is an analysis aid, not a universal sizing formula. Priority scheduling, multiple classes, replacement/coalescing, blocking producers, credit systems, service batching, spill storage and other mechanisms may require a different project model.

At minimum, construction shall identify:

- burst interval/horizon being bounded;
- material consumer service pause or slowdown;
- admission/backpressure response latency;
- maximum allowed queueing age/latency where freshness/timing matters;
- overload detection/observation resolution;
- recovery timing where overload state changes behavior.

A queue depth without a demand/service/time basis is not sufficient timing evidence when timing/capacity is material.

## 11. Concurrency / Reentrancy Considerations

The project shall decide, where applicable:

- single-producer / multi-producer behavior;
- single-consumer / multi-consumer behavior;
- ISR/task/thread/process or hardware/software execution boundaries;
- whether enqueue/admit, dequeue/complete, cancel, replace and inspect operations may execute concurrently;
- serialization/atomicity mechanism for capacity and ownership accounting;
- ordering guarantees under concurrency;
- blocking restrictions in contexts that cannot safely wait;
- priority inversion or starvation risk introduced by the synchronization mechanism.

A queue API being documented as thread-safe is not by itself proof that the project's ordering, ownership, timing and starvation semantics are preserved.

## 12. Capacity / Resource Considerations

Capacity analysis shall include all materially relevant finite resources, not only the nominal element count.

Consider:

- payload storage;
- descriptors/metadata;
- alignment/padding;
- ownership bookkeeping;
- synchronization objects;
- per-class reservation;
- DMA/driver/transport buffering;
- spill/deferred storage;
- retry/replay outstanding work;
- downstream capacity that can create hidden retained work.

A larger queue can improve burst tolerance, but it can also increase latency, stale-work retention, memory pressure and time before a persistent throughput mismatch becomes visible.

### 12.1 Bounded Exhaustion Behavior

When the controlled capacity is reached, the implementation shall execute the project-defined policy for the affected class.

The following table is a decision aid only; none is a default:

| Policy family | Useful when | Construction risk to evaluate |
|---|---|---|
| Backpressure / bounded wait | upstream can slow and waiting is semantically acceptable | deadlock, priority inversion, blocked critical progress, excessive producer latency |
| Reject newest | existing accepted work should remain | caller must handle rejection; burst loss semantics must be explicit |
| Drop/evict oldest | newer information is more valuable and history loss is permitted | ordering/history loss, in-flight ownership, stale evidence |
| Coalesce / replace | pending state updates supersede earlier values | key identity, atomic replacement, duplicate/superseded semantics |
| Reservation / class partition | protected work requires admission isolation | stranded capacity, fairness, starvation of unreserved classes |
| Load shedding / degrade | continued partial service is preferable to collapse | transition ownership, restoration criteria, observability, external behavior |

Persistent overload that cannot be contained within the TIME-owned bound requires the project to apply the relevant ROB/RUN interpretation and response; this L4 entry does not choose that response.

## 13. Lifecycle Considerations

### Initialization / partial initialization

- establish queue/admission ownership before producers can rely on normal admission;
- define behavior for demand arriving before consumer/service readiness;
- avoid exposing uninitialized capacity/accounting as valid available capacity.

### Entry to operation / normal operation

- begin occupancy/age/overload observation early enough to support the claimed bound;
- establish the producer/service assumptions used for the current operating mode.

### Reconfiguration

- define how capacity, class policy, priority, consumer set or thresholds may change without corrupting ownership/accounting;
- define treatment of already admitted work if the new configuration reduces capacity or changes semantics.

### Recovery / reintegration

- define whether pending work remains valid after consumer restart/reconnect/recovery;
- define how admission resumes and how stale/superseded pending work is treated.

### Shutdown / reset / power transition

- define whether pending work is drained, discarded, persisted or reconstructed;
- define whether discard is observable/evidenced when it has contract significance.

Update/activation behavior is relevant only when the mechanism spans that lifecycle transition.

## 14. Failure / Recovery Behavior

Construction shall consider the following bounded failure/invalid conditions where applicable:

- producer continues to generate demand after backpressure/rejection and no bounded consequence exists;
- consumer stalls or service capacity falls below the analyzed bound;
- occupancy/accounting becomes inconsistent with actual retained work;
- synchronization failure permits over-admission or duplicate release;
- discard/coalesce/replace path violates ordering or ownership semantics;
- priority/fairness policy starves a required class;
- overload state oscillates without a bounded restoration rule;
- hidden secondary buffering or retries exceed the analyzed resource model;
- observability loses the peak occupancy/starvation/discard evidence needed for verification.

The L4 response is to identify the condition and the project decision boundary. It does not itself classify the project health state or select the final containment/degradation/recovery policy owned by ROB/RUN/PDA.

## 15. Diagnostics / Observability

The project shall provide enough observation to determine whether the claimed bounded behavior remains valid. Depending on the project, useful evidence can include:

- current occupancy / outstanding work;
- peak/high-water occupancy;
- oldest queued-item age or equivalent backlog-latency indicator;
- accepted/rejected/dropped/evicted/coalesced/replaced counts by material class;
- backpressure or overload-state activation count/duration;
- consumer service/completion rate or progress indicator;
- starvation/fairness evidence for protected classes;
- capacity/resource margin evidence;
- reason/cause for overload disposition where multiple policies exist.

The exact telemetry/log/event/counter mechanism, retention period and sampling rate are Project Design Decisions. The observation method must be capable of seeing the condition used for the project's verification claim; a slowly sampled metric that misses short peak occupancy cannot by itself prove peak boundedness.

## 16. Verification Intent

The project-specific Test Procedure owns concrete stimuli, numbers, instrumentation and pass/fail execution. This L4 entry defines only the properties that a conforming realization should be capable of proving.

### VI-01 — Nominal bounded operation

- **Property:** demand within the analyzed service/capacity envelope is admitted/serviced without violating the project-defined ordering, latency/freshness or resource bound.
- **Condition:** representative valid producer/service behavior below the overload threshold.
- **Expected observable behavior:** occupancy and age remain within the project bound; no undefined loss/exhaustion consequence occurs.

### VI-02 — Burst tolerance to the finite boundary

- **Property:** the implementation preserves finite capacity/accounting during a project-bounded burst.
- **Condition:** demand approaches the analyzed maximum burst/backlog condition.
- **Expected observable behavior:** peak occupancy/outstanding work is measurable and remains within the controlled bound.

### VI-03 — Capacity exhaustion consequence

- **Property:** capacity unavailability executes the project-defined disposition rather than silent/unbounded accumulation.
- **Condition:** demand reaches/exceeds available capacity under a controlled test condition.
- **Expected observable behavior:** the correct backpressure/reject/drop/coalesce/reservation/degrade behavior occurs and its material consequence is observable.

### VI-04 — Sustained demand greater than service

- **Property:** persistent throughput mismatch does not create unbounded accumulation or indefinite hidden timing collapse.
- **Condition:** producer demand remains above consumer service for longer than the normal burst envelope.
- **Expected observable behavior:** bounded exhaustion/overload semantics engage; project-owned escalation/degradation behavior can be observed where applicable.

### VI-05 — Consumer stall / service pause

- **Property:** a bounded or failed consumer does not invalidate queue accounting and overload policy.
- **Condition:** service is delayed/stalled for a project-defined interval.
- **Expected observable behavior:** backlog follows the analyzed model until the bounded policy activates; ownership/accounting remains consistent.

### VI-06 — Concurrency integrity

- **Property:** concurrent producer/consumer/cancel/replace paths preserve capacity and ownership semantics.
- **Condition:** exercise allowed concurrent execution contexts and boundary transitions.
- **Expected observable behavior:** no over-admission, duplicate release, lost ownership transition or ordering violation beyond the project-defined semantics.

### VI-07 — Ordering / freshness / class semantics

- **Property:** overload policies preserve applicable `SCAF-INT` ordering/freshness meaning.
- **Condition:** apply reject/drop/coalesce/replace/priority behavior to information for which ordering/freshness semantics matter.
- **Expected observable behavior:** missing/superseded/stale/priority behavior matches the project contract.

### VI-08 — Recovery from overload

- **Property:** exit from overload/degraded behavior is controlled and does not create oscillation, stale backlog replay or hidden loss outside the project policy.
- **Condition:** remove/reduce the overload cause after overload behavior is active.
- **Expected observable behavior:** admission/service returns according to project restoration criteria; pending work treatment and evidence are consistent.

### VI-09 — Long-duration boundedness

- **Property:** repeated operation over the intended horizon does not create hidden growth in secondary queues, retries, counters or retained work.
- **Condition:** run a duration/workload sufficient to exercise accumulation assumptions when reasonably producible.
- **Expected observable behavior:** resource/occupancy trends remain within the project-defined horizon/bound or the controlled exhaustion behavior occurs.

Future empirical evidence is required only when reasonably producible at the current engineering state, consistent with the frozen Evidence Availability Rule.

## 17. Invalid / Incomplete Construction Conditions

For a project claiming realization of this guidance, the following are deterministic invalid/incomplete conditions when they are applicable to the claimed scope:

- no finite capacity/outstanding-work bound exists for the admitted work governed by the mechanism;
- capacity exhaustion has no explicit project-owned consequence;
- a loss/coalesce/overwrite/reorder policy is implemented without the required project Interaction semantics;
- a queue-size increase is presented as the only justification for a persistent producer/service mismatch;
- hidden secondary accumulation materially defeats the claimed end-to-end bound;
- concurrent admission/completion can violate capacity or ownership accounting;
- backpressure is selected even though the producer cannot honor it and no alternative bounded consequence is defined;
- freshness is material but queued age can grow beyond the project validity horizon with no defined treatment;
- overload/starvation behavior is material but the project cannot observe the condition at sufficient resolution to verify the claim;
- concrete capacity/threshold/policy values are taken from an example rather than an explicit Project Design Decision;
- persistent TIME-bound violation has a material robustness consequence but no applicable project ROB/RUN response decision exists.

A project value or empirical threshold that is legitimately unresolved at an earlier decision horizon is not automatically Invalid merely because it has not yet been decided. It becomes a progression blocker only when the corresponding construction decision must be fixed to proceed without material ambiguity or difficult-to-reverse commitment.

## 18. Known Variations / Trade-offs

- **Single FIFO:** simple ordering and ownership; may provide poor class isolation or fairness under mixed criticality.
- **Per-class queues:** stronger isolation and policy separation; increases capacity partitioning and coordination complexity.
- **Latest-value coalescing:** bounds supersedable state updates efficiently; unsuitable when every historical event must be retained.
- **Credit/token admission:** can bound outstanding distributed work without one physical queue; requires correct credit ownership/recovery.
- **Bounded spill storage:** increases burst horizon; introduces a second capacity, durability, age and recovery problem that must itself be bounded.
- **Early load shedding:** protects service for important work; changes externally visible service/loss behavior and requires clear PDA/verification treatment.
- **Larger capacity:** improves short burst absorption; consumes resources and can mask persistent throughput mismatch while increasing latency/staleness.

## 19. Material Deviation Considerations

Retained Project Design Authority rationale is appropriate when a departure from this guidance materially changes:

- the finite admission/accumulation boundary;
- ordering/freshness/loss semantics;
- ownership or concurrency model;
- producer/service/capacity basis;
- overload consequence;
- starvation/fairness behavior;
- robustness/recovery boundary;
- observability needed to prove the controlled bound;
- Verification Intent;
- a difficult-to-reverse architecture/resource commitment.

Local implementation differences that preserve the accepted construction invariants and project decisions do not require waiver-style bureaucracy.

## 20. Example Realization — Non-Canonical

> **This example realization illustrates one possible conforming approach and is not the canonical implementation.**

A project could implement a fixed-capacity pending-work store with symbolic project-owned parameters:

```text
CAPACITY_N        = <Project Design Decision>
HIGH_WATER_H      = <Project Design Decision, if used>
MAX_ITEM_AGE_T    = <Project Design Decision, if freshness is material>
OVERLOAD_POLICY   = <Project Design Decision by work class>
```

Conceptual flow:

```text
submit(work):
    validate ownership / class / freshness metadata
    if admission policy accepts work within CAPACITY_N:
        transfer ownership to bounded pending-work store
        update observable occupancy/high-water evidence
        return accepted
    else:
        execute OVERLOAD_POLICY for this work class
        update observable overload/disposition evidence
        return the defined admission result

complete(work):
    release/transfer ownership exactly once
    update occupancy/service evidence
```

This example does **not** define the queue depth, high-water threshold, age limit, overload policy, API shape, data structure, lock, RTOS primitive, interrupt policy or test threshold. Those remain project decisions.

## 21. Construction Readiness Check

This entry is intended to be locally Construction Ready when a competent engineer or AI consumer can use it with the traced project context to:

- identify producer, admission-boundary, finite accumulation and consumer responsibilities;
- enumerate the project decisions that must be supplied before committing a concrete realization;
- derive or justify a capacity basis from demand/service/resource assumptions instead of guessing a queue depth;
- select a controlled exhaustion policy without treating any listed option as a default;
- preserve ordering/freshness/ownership semantics;
- identify concurrency, lifecycle and failure/recovery questions material to the realization;
- define sufficient observability for the claimed bound;
- derive project-specific verification cases from the Verification Intent;
- begin implementation without requiring SCAF to prescribe a vendor API, exact data structure, source-file layout or project parameter value.

Construction Readiness does not prove that the project has made every decision, that code can compile immediately, that implementation is correct, that verification passed, or that an obligation is closed.

## 22. Provenance / Reference Basis

This guidance is SCAF-original construction elaboration of:

- frozen L2 `SCAF-TIME-009`, `SCAF-TIME-010`, `SCAF-TIME-011`, `SCAF-TIME-012`, `SCAF-TIME-013`;
- frozen constraint inputs `SCAF-ROB-016`, applicable `SCAF-INT-007`, `SCAF-INT-008`;
- frozen L3 `SCAF-PAT-TIM-001` architecture mechanism;
- accepted v0.1.0rc01 L4 Minimum Construction Guidance semantic/layer contract.

No external code, prompt, schema, document passage or example implementation is directly incorporated.

## 23. Revision / Supersession Notes

Initial representative candidate. No predecessor is superseded.

Material future changes to the finite-admission intent, Construction Invariants, Required Project Decision contract, overload/failure behavior or Verification Intent require explicit compatibility/supersession reassessment. Clarifications that do not change those semantics may retain the identity after the appropriate controlled review.
