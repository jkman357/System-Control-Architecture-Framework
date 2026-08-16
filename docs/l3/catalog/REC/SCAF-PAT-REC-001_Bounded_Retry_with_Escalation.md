# SCAF-PAT-REC-001 — Bounded Retry with Escalation

**Development Release:** v0.0.3  
**Pattern Family:** `REC` — Recovery & Reintegration  
**Pattern Kind:** Mechanism  
**Catalog Status:** Available  
**Maturity:** M2 — Architecture Reviewed  
**Introduced In:** v0.0.3rc03

## Metadata

| Field | Value |
|---|---|
| Pattern ID | `SCAF-PAT-REC-001` |
| Pattern Name | Bounded Retry with Escalation |
| Pattern Family | `REC` |
| Pattern Kind | Mechanism |
| Catalog Status | Available |
| Maturity | M2 — Architecture Reviewed |
| Introduced In | v0.0.3rc03 |
| Primary L2 Trace | `SCAF-ROB-032`, `SCAF-ROB-011` |
| Supporting L2 Trace | `SCAF-ROB-015`, `SCAF-ROB-016`, `SCAF-ROB-019` |
| Constraint Inputs | `SCAF-TIME-006`, `SCAF-TIME-011`, `SCAF-TIME-012`; conditional `SCAF-INT-007` where retry repeats/interleaves Interaction exchanges; conditional `SCAF-INT-010` where retry continuity crosses/reuses connection sessions; applicable `SCAF-INT-013` outcomes when retry follows an Interaction failure |
| Profile Facets | Local or distributed recovery; synchronous/asynchronous Interaction; bare metal/RTOS/process/service |
| Provenance / Reference Basis | Frozen SCAF obligation-derived architecture synthesis; retry mechanism explicitly left to L3 by `SCAF-ROB-030` |

## 1. Intent

Allow recovery attempts for conditions that may be transient while guaranteeing a controlled termination point and a defined escalation when retry is no longer permitted or cannot establish the required outcome.

## 2. Problem

Unbounded retry can create infinite recovery loops, recovery storms, hidden unavailability, resource exhaustion or repeated harmful side effects. Conversely, immediate permanent failure on the first transient error can reduce availability unnecessarily.

## 3. Applicability

Consider this pattern where:

- repeating an operation/recovery attempt can plausibly succeed without violating the operation's semantic contract;
- the project can identify a success/completion criterion;
- retry resource/time/side-effect accumulation can be bounded;
- an escalation or terminal consequence exists when the retry budget is exhausted or retry becomes ineligible.

## 4. Non-Applicability / Cautions

Do not use retry as an automatic response where the operation is not idempotent or repeated execution can create duplicate/unsafe state without a controlled semantic basis. Do not use retry to hide an unreconciled session, stale authority, security denial, permanent incompatibility or invalid configuration condition.

## 5. L2 Trace

### 5.1 Primary Realization Candidate

- `SCAF-ROB-032` — directly realizes the architecture idea of bounded retry/recovery with an explicit termination/escalation condition.
- `SCAF-ROB-011` — structures repeated attempts around controlled recovery completion/failure criteria.

### 5.2 Supporting Realization

- `SCAF-ROB-015` — bounding and escalation can reduce cascading recovery storms and peer-dependency amplification.
- `SCAF-ROB-016` — a bounded retry policy can prevent uncontrolled long-run consumption where retries consume finite resources.
- `SCAF-ROB-019` — retry count/state/result can be exposed as robustness-relevant observations when required.

### 5.3 Constraint Inputs

- `SCAF-TIME-006` — retry delay, total recovery deadline and related temporal limits are project values.
- `SCAF-TIME-011` — CPU, energy, storage, channel or other retry resource budget/margin may constrain the pattern.
- `SCAF-TIME-012` — overload/starvation bounds may constrain retry rate or concurrent recovery.
- `SCAF-INT-007` — where retry repeats or interleaves Interaction exchanges, project-defined duplicate, missing, reordered or superseded semantics constrain whether repetition is semantically legal and how side effects are interpreted.
- `SCAF-INT-010` — where retry continuity crosses reconnection, replacement or reuse of a connection/session context, project-defined session/incarnation semantics constrain whether retry history and exchanges remain applicable.
- `SCAF-INT-013` — where retry follows an Interaction result, the contract-level meaning of the negative/unsupported result constrains whether retry is semantically valid.

## 6. Required PDA Decisions

- retry-eligible failure/result classes;
- success/completion criterion for each attempt;
- termination basis: attempt budget, elapsed-time budget, resource budget, state change or combined rule;
- delay/backoff/admission policy where repeated attempts can contend with normal Service;
- idempotency/duplicate-effect treatment;
- escalation target and resulting operational/lifecycle state;
- reset of retry history after recovery, session change or incarnation change;
- observations/evidence required to distinguish transient failure from repeated unsuccessful recovery.

## 7. Mechanism Summary

A failed operation/recovery result is classified for retry eligibility. Eligible attempts enter a controlled retry state that consumes a finite project-defined retry budget. Each attempt either reaches the controlled recovery completion criterion, remains eligible for another attempt while budget remains, or transitions to escalation/terminal handling when eligibility or budget is exhausted.

The pattern separates **retry eligibility**, **retry budget** and **escalation consequence** so that the retry mechanism cannot silently become an infinite loop.

## 8. Variants

- bounded attempt count;
- bounded elapsed recovery interval;
- resource/token-budget retry;
- fixed or increasing delay/backoff;
- circuit-breaker-like suspension followed by controlled re-evaluation;
- per-peer/per-operation budgets versus shared recovery budget.

## 9. Forces / Tradeoffs

- availability gain versus delayed fault declaration;
- rapid retry versus overload/recovery storm risk;
- broader budget versus energy/CPU/channel consumption;
- retry transparency versus diagnosability;
- per-operation isolation versus coordination complexity.

## 10. Failure / Weakness Modes

- retrying a non-idempotent operation duplicates side effects;
- permanent failure is repeatedly retried because eligibility classification is too broad;
- multiple peers retry simultaneously and amplify overload;
- retry history is incorrectly preserved or cleared across session/incarnation changes;
- successful low-level retry does not establish the required end-to-end Service outcome;
- escalation path is undefined or itself repeatedly retried without bound.

## 11. Selection Consequences

Selection creates explicit retry state, budget and escalation decisions and may add timing/resource/evidence obligations. Where retry repeats or interleaves an Interaction exchange, the project must consume the applicable INT-owned duplicate/order/operation semantics; where continuity crosses a connection-session boundary, it must also consume the applicable session/incarnation semantics. The retry pattern does not author those Interface meanings.

## 12. Composition Relations

### Requires

- project-defined retry eligibility and recovery completion criteria;
- a defined terminal/escalation consequence.

### Commonly Composed With

- `SCAF-PAT-SUP-001` — Heartbeat / Liveness Supervision;
- `SCAF-PAT-SUP-002` — Independent Watchdog with Escalation;
- `SCAF-PAT-COM-001` — Reconnect plus State Reconciliation;
- `SCAF-PAT-EVD-001` — Pre/Post-Trigger Retained Incident Evidence Ring.

### Alternative To

- immediate fail-fast handling where retry is not project-appropriate.

### Conflicts With

- unbounded automatic retry or retry after a contract result that explicitly forbids repetition.

### Subsumes

- None.

### Supersedes

- None.

## 13. External Authority Considerations

External safety/security/regulatory/risk authority may forbid retry for certain operations, constrain maximum recovery time, require bounded side effects, or require escalation to a defined safe/security state. Those objectives remain source-authority inputs.

## 14. Re-evaluation Triggers

Re-evaluate when failure classification, Interface contract/idempotency, retry cost, timing/resource budgets, peer count, overload behavior, lifecycle/session semantics or escalation consequence changes.

## 15. Provenance / Reference Basis

SCAF-new synthesis from frozen ROB/TIME/INT obligations. No specific retry algorithm, library or transport behavior is promoted as universal.

## 16. L3 / L4 Boundary Note

L3 does not define numeric retry counts, timeout values, randomization formulas, thread/task implementation, queue layout, transport retransmission settings or test procedures.
