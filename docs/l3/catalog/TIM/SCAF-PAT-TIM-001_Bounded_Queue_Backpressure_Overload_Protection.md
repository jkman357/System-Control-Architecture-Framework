# SCAF-PAT-TIM-001 — Bounded Queue / Backpressure / Overload Protection

**Development Release:** v0.0.3rc09  
**Pattern Family:** `TIM` — Timing & Capacity Realization  
**Pattern Kind:** Mechanism  
**Catalog Status:** Candidate  
**Maturity:** M1 — Structured  
**Introduced In:** v0.0.3rc08

## Metadata

| Field | Value |
|---|---|
| Pattern ID | `SCAF-PAT-TIM-001` |
| Pattern Name | Bounded Queue / Backpressure / Overload Protection |
| Pattern Family | `TIM` |
| Pattern Kind | Mechanism |
| Catalog Status | Candidate |
| Maturity | M1 — Structured |
| Introduced In | v0.0.3rc08 |
| Primary L2 Trace | `SCAF-TIME-009`, `SCAF-TIME-012` |
| Supporting L2 Trace | `SCAF-TIME-010`, `SCAF-TIME-011`, `SCAF-TIME-013` |
| Constraint Inputs | `SCAF-ROB-016`; applicable `SCAF-INT-007`, `SCAF-INT-008` |
| Profile Facets | Bounded producer/consumer pipelines, message/data queues, event streams, buffers, work schedulers and storage pipelines across embedded/host/distributed systems |
| Provenance / Reference Basis | Frozen SCAF TIME/ROB/INT obligations plus rc07 second-tranche planning review approval; SCAF-new technology-neutral synthesis |

## 1. Intent

Keep queued or admitted work within controlled capacity and temporal bounds by combining finite admission/storage with explicit backpressure, rejection, coalescing, dropping or overload-state semantics instead of allowing unbounded accumulation or silent timing collapse.

## 2. Problem

Producers can temporarily or persistently outpace consumers. If queues grow without a controlled bound, latency, memory use and stale-work accumulation can invalidate timing assumptions long before a visible crash occurs. If data is silently dropped or overwritten, Interaction semantics can also become ambiguous.

## 3. Applicability

Consider this pattern where:

- work/data/events can arrive faster than they are serviced;
- buffering or queued work materially affects latency, memory/storage or Service behavior;
- the project can define a finite capacity and overload policy;
- producers, consumers or admission points can expose a controlled consequence when capacity is unavailable.

## 4. Non-Applicability / Cautions

A queue is not automatically required. Direct handoff, sampling, coalescing, reservation or other project architectures may be preferable. Backpressure is ineffective when the producer cannot slow, reject or alter behavior and there is no defined loss/degradation consequence.

This pattern does not define whether dropped/coalesced/reordered information is semantically acceptable; applicable INT contracts retain that authority.

## 5. L2 Trace

### 5.1 Primary Realization Candidate

- `SCAF-TIME-009` — directly realizes bounded queue/capacity and admission/backpressure behavior that prevents uncontrolled accumulation.
- `SCAF-TIME-012` — provides a mechanism for bounding overload/starvation effects rather than allowing unbounded service interference.

### 5.2 Supporting Realization

- `SCAF-TIME-010` — queue admission/service policy can preserve the project-defined throughput/bandwidth capacity and margin assumptions.
- `SCAF-TIME-011` — finite queue/storage/work budgets consume controlled CPU/memory/storage/channel resource budgets.
- `SCAF-TIME-013` — explicit bounded occupancy/retention prevents long-duration queue or retained-work growth from escaping the intended operating horizon.

### 5.3 Constraint Inputs

- `SCAF-ROB-016` — if a controlled capacity/resource bound is violated, ROB owns the health/failure and containment/degradation/recovery consequence; TIM does not take that response authority.
- `SCAF-INT-007` — where queued items are Interaction/data-contract elements, duplicate/missing/reordered/superseded semantics constrain drop/coalescing/reordering policies.
- `SCAF-INT-008` — where age affects validity, the contract meaning of stale/expired/invalid queued data constrains admission/service/discard behavior.

## 6. Required PDA Decisions

- bounded capacity and required resource margin basis;
- producer demand model and service-capacity basis;
- admission point(s) and what happens when capacity is unavailable;
- backpressure/rejection/drop/coalesce/overwrite policy by information/work class;
- fairness/priority/starvation policy where multiple classes compete;
- acceptable queueing latency/age and stale-work treatment;
- Interaction semantics for missing, duplicate, superseded or coalesced items;
- overload observability and threshold evidence;
- downstream ROB/RUN consequence when the controlled TIME bound is violated.

## 7. Mechanism Summary

The mechanism places a finite **admission and accumulation boundary** between producers and constrained service capacity. When demand approaches or reaches that boundary, it applies a project-selected policy such as backpressure, rejection, load shedding, coalescing, replacement of superseded work or controlled degradation. The mechanism keeps occupancy/age/resource use observable enough to establish whether the TIME-owned bound remains valid.

The mechanism's success is not “the queue never fills.” Success is that demand and queued work remain within the project-defined bounded behavior, and that overload has an explicit consequence rather than unbounded accumulation or hidden semantic loss.

## 8. Variants

- fixed-capacity FIFO with producer backpressure;
- per-class bounded queues with controlled admission/reservation;
- latest-value coalescing for supersedable state updates;
- token/credit admission controlling outstanding work;
- bounded spill-to-secondary storage where the storage horizon is itself controlled;
- load-shedding mode that rejects lower-priority work under overload.

## 9. Forces / Tradeoffs

- buffering burst tolerance versus latency/resource growth;
- producer decoupling versus stale-work accumulation;
- fairness versus priority for critical work;
- lossless behavior versus bounded resource requirements;
- early rejection/degradation versus delayed overload detection;
- larger capacity versus masking a persistent throughput mismatch.

## 10. Failure / Weakness Modes

- queue size increases but root throughput mismatch remains uncontrolled;
- backpressure path is ignored or itself blocks critical progress;
- overflow silently corrupts ordering/loss semantics;
- old work remains queued beyond its validity horizon;
- priority policy starves a required class;
- overload oscillates around a threshold and repeatedly sheds/restores load;
- resource use outside the modeled queue defeats the capacity budget;
- metrics are sampled too late to show peak occupancy or starvation.

## 11. Selection Consequences

Selection requires finite capacity/admission semantics, overload behavior and measurable occupancy/age/resource criteria. It also forces project decisions about semantic loss/reordering and the ROB/RUN response to TIME-bound violation. It does not establish those downstream health or recovery decisions itself.

## 12. Composition Relations

### Requires

- controlled demand/capacity/resource assumptions and an admission/overload consequence.

### Commonly Composed With

- `SCAF-PAT-REC-001` — Bounded Retry with Escalation, where retries add demand and must not create retry storms;
- `SCAF-PAT-FTL-001` where overload must be prevented from propagating across domains;
- `SCAF-PAT-EVD-001` where overload/queue evidence is retained.

### Alternative To

- architectures that avoid queues through synchronous handoff, fixed-rate sampling or source-side aggregation when those alternatives meet the same project requirements.

### Conflicts With

- unbounded buffering used as a substitute for an explicit capacity/throughput decision.

### Subsumes

- None.

### Supersedes

- None.

## 13. External Authority Considerations

Applicable safety/security/regulatory/risk authorities may constrain which work may be dropped, delayed, reordered or degraded; retention/privacy rules may constrain spill/queued data; resource exhaustion may have externally controlled hazard consequences.

## 14. Re-evaluation Triggers

Re-evaluate when producer rates, consumer capacity, scheduler/priority architecture, payload size, memory/storage/channel budgets, freshness semantics, operating horizon, workload mix or overload consequences change.

## 15. Provenance / Reference Basis

SCAF-new synthesis of frozen TIME/ROB/INT obligations. The rc07 independent planning review approved this as complementary to `REC-001`: this pattern bounds admitted/queued demand, while `REC-001` bounds repeated recovery attempts.

## 16. L3 / L4 Boundary Note

This pattern does not prescribe queue depth, ring-buffer implementation, RTOS queue API, scheduler policy, semaphore primitive, network flow-control protocol, transport credit format, memory allocator, exact watermark, timeout or verification stress-test sequence.
