# SCAF-PAT-SUP-002 — Independent Watchdog with Escalation

**Development Release:** v0.0.3rc05  
**Pattern Family:** `SUP` — Supervision & Detection  
**Pattern Kind:** Mechanism  
**Catalog Status:** Candidate  
**Maturity:** M2 — Architecture Reviewed  
**Introduced In:** v0.0.3rc03

## Metadata

| Field | Value |
|---|---|
| Pattern ID | `SCAF-PAT-SUP-002` |
| Pattern Name | Independent Watchdog with Escalation |
| Pattern Family | `SUP` |
| Pattern Kind | Mechanism |
| Catalog Status | Candidate |
| Maturity | M2 — Architecture Reviewed |
| Introduced In | v0.0.3rc03 |
| Primary L2 Trace | `SCAF-ROB-006` |
| Supporting L2 Trace | `SCAF-ROB-005`, `SCAF-ROB-011` |
| Constraint Inputs | `SCAF-TIME-006`, `SCAF-LIFE-008`, `SCAF-LIFE-009` |
| Profile Facets | MCU/SoC/PC/distributed node; supervisor may be scheduling-, process-, reset-domain- or hardware-independent |
| Provenance / Reference Basis | Frozen SCAF obligation-derived architecture synthesis; watchdog mechanism explicitly left to L3 by `SCAF-ROB-030` |

## 1. Intent

Provide a supervising mechanism whose ability to detect loss of required progress and initiate a controlled escalation does not depend solely on the same execution/failure context being supervised.

## 2. Problem

A stalled or corrupted execution context may be unable to diagnose or recover itself. A self-check executing in the same blocked scheduler, process, power/reset domain or shared dependency can fail simultaneously and falsely preserve a healthy indication.

## 3. Applicability

Consider this pattern where:

- failure of the supervised execution context can prevent its own recovery path from executing;
- a materially more independent supervising responsibility can observe required progress;
- the project has a defined escalation consequence when supervision expires or becomes indeterminate;
- reset/restart/failover/degradation consequences can be controlled at architecture level.

## 4. Non-Applicability / Cautions

The pattern is weak where the watchdog shares the same critical clock, scheduler, software path, power source, reset control, communication dependency or corruption domain as the supervised function and that shared dependency can defeat both.

A watchdog expiry is evidence of a violated supervision condition; it is not automatically root-cause proof. The watchdog shall not invent the reset classification, safety objective or recovery outcome.

## 5. L2 Trace

### 5.1 Primary Realization Candidate

- `SCAF-ROB-006` — provides a candidate monitor/supervisor architecture whose own availability/independence and invalid-output consequences must be explicitly considered.

### 5.2 Supporting Realization

- `SCAF-ROB-005` — can make loss of progress detectable when the project requires detection.
- `SCAF-ROB-011` — watchdog escalation may initiate a project-selected recovery/repair mechanism with explicit completion criteria.

### 5.3 Constraint Inputs

- `SCAF-TIME-006` — watchdog observation period, expiry bound and response timing are controlled project values.
- `SCAF-LIFE-008` — escalation that produces reset must use the project reset classification/cause semantics.
- `SCAF-LIFE-009` — escalation must respect reset-domain and coordination consequences.

## 6. Required PDA Decisions

- supervised responsibility/property and required progress evidence;
- required independence/separation between supervisor and supervised context;
- watchdog timeout/expiry semantics and applicable timebase;
- treatment of intentional suspend, boot, update, maintenance and degraded states;
- escalation target: restart, reset, failover, degradation, isolation or another controlled response;
- reset/recovery scope and cross-participant coordination;
- behavior when the watchdog itself is unavailable, invalid or disagrees with another monitor;
- evidence that must be retained around watchdog expiry/escalation.

## 7. Mechanism Summary

A supervising responsibility, placed in a project-defined failure context sufficiently independent from the supervised execution, observes a controlled progress/liveness indication. The supervised context cannot indefinitely defer the supervisory decision merely by remaining alive without required progress. If the required observation is not established within the project-defined bound, the watchdog produces a controlled supervision-expiry result and invokes or authorizes the PDA-selected escalation path.

The escalation path is separate from the watchdog identity: the same supervision mechanism may lead to restart, reset, isolation, failover, degraded operation or another project-defined consequence. If that downstream recovery path itself performs retry, repeated recovery or repeated escalation, the applicable `SCAF-ROB-032` termination semantics are evaluated there; the watchdog supervision mechanism does not acquire retry/recovery authority by itself.

## 8. Variants

- supervisor separated by scheduler/execution context;
- supervisor in a separate process/service;
- supervisor in a distinct reset or power domain;
- dedicated hardware or external supervisory participant;
- windowed/sequence-aware supervision where merely frequent servicing is insufficient to prove valid progress.

## 9. Forces / Tradeoffs

- increased independence versus cost/complexity;
- faster intervention versus risk of nuisance reset/escalation;
- narrow reset scope versus incomplete recovery from shared corruption;
- external supervisor robustness versus additional dependency/interface;
- service continuity versus stronger fault clearing.

## 10. Failure / Weakness Modes

- monitored code services the watchdog without completing material work;
- supervisor shares the failed dependency and never expires or reports incorrectly;
- watchdog reset loops because the recovery outcome does not remove the initiating condition;
- escalation destroys needed evidence before it is preserved;
- reset domain is broader or narrower than assumed, leaving inconsistent peers/retained state;
- intentional long operation exceeds the configured bound without controlled mode awareness.

## 11. Selection Consequences

The project must control supervisor independence, progress evidence, timeout semantics, escalation scope and lifecycle consequences. Selection may also require evidence-survivability and reset-loop containment decisions.

## 12. Composition Relations

### Requires

- controlled progress/liveness semantics;
- project-selected escalation/recovery consequence.

### Commonly Composed With

- `SCAF-PAT-SUP-001` — Heartbeat / Liveness Supervision;
- `SCAF-PAT-REC-001` — Bounded Retry with Escalation;
- `SCAF-PAT-EVD-001` — Pre/Post-Trigger Retained Incident Evidence Ring.

### Alternative To

- another sufficiently independent project supervision mechanism that can establish the required detection/escalation property.

### Conflicts With

- an architecture that assumes watchdog independence without analyzing shared failure dependencies.

### Subsumes

- None.

### Supersedes

- None.

## 13. External Authority Considerations

Applicable safety/security/regulatory/risk sources may constrain independence, maximum detection/recovery time, reset permissibility, failover eligibility or required evidence. These constraints remain externally owned.

## 14. Re-evaluation Triggers

Re-evaluate when execution/scheduling architecture, reset or power domains, shared clocks/resources, progress semantics, watchdog placement, lifecycle behavior, recovery scope or required response timing changes.

## 15. Provenance / Reference Basis

SCAF-new synthesis based on frozen ROB/TIME/LIFE obligations. `SCAF-ROB-030` explicitly leaves watchdog realization to `SCAF-PROF`/Project Realization rather than L1/L2.

## 16. L3 / L4 Boundary Note

This pattern does not prescribe a watchdog peripheral, external supervisor IC, register sequence, service interval value, reset register, task priority, API, ISR design, board wiring or validation procedure.
