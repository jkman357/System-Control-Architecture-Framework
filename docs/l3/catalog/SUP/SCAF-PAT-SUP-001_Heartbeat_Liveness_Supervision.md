# SCAF-PAT-SUP-001 — Heartbeat / Liveness Supervision

**Development Release:** v0.0.3rc06  
**Pattern Family:** `SUP` — Supervision & Detection  
**Pattern Kind:** Mechanism  
**Catalog Status:** Available  
**Maturity:** M2 — Architecture Reviewed  
**Introduced In:** v0.0.3rc03

## Metadata

| Field | Value |
|---|---|
| Pattern ID | `SCAF-PAT-SUP-001` |
| Pattern Name | Heartbeat / Liveness Supervision |
| Pattern Family | `SUP` |
| Pattern Kind | Mechanism |
| Catalog Status | Available |
| Maturity | M2 — Architecture Reviewed |
| Introduced In | v0.0.3rc03 |
| Primary L2 Trace | `SCAF-ROB-004`, `SCAF-ROB-005` |
| Supporting L2 Trace | `SCAF-ROB-031`, `SCAF-OBS-014`, `SCAF-OBS-015` |
| Constraint Inputs | `SCAF-TIME-002`, `SCAF-TIME-006`, `SCAF-INT-010` where session identity is material |
| Profile Facets | Local or distributed Node; bare metal/RTOS/process/service; local memory or message-based Interaction |
| Provenance / Reference Basis | Frozen SCAF obligation-derived architecture synthesis; no implementation donor promoted by this entry |

## 1. Intent

Provide a reusable architecture mechanism for determining whether a monitored participant, execution responsibility or Service is demonstrating the project-defined evidence of continued liveness/progress within a controlled observation relationship.

## 2. Problem

A participant can stop progressing, become unreachable, execute the wrong lifecycle/session incarnation or cease producing a required Service while other parts of the system continue operating. Without a controlled liveness observation, silence can be ambiguous and may be mistaken for healthy operation.

The pattern does not define what “healthy” means for the project. It provides a candidate mechanism for producing and evaluating liveness evidence that may contribute to the project-defined ROB health/failure decision.

## 3. Applicability

Consider this pattern where:

- continued progress or presence of a participant/responsibility is material;
- an observable recurring or progress-coupled indication can be associated with the monitored responsibility;
- missing, stale or incarnation-mismatched liveness evidence has a project-defined consequence;
- the project can define an applicable timebase and liveness evaluation relationship.

## 4. Non-Applicability / Cautions

This pattern is weak or unsuitable where:

- silence is a valid normal behavior and cannot be distinguished from loss of progress;
- the observation path shares the same failure mode as the monitored responsibility such that apparent liveness can survive the monitored failure;
- network partition or scheduled suspension can invalidate simple absence-based interpretation unless those conditions are explicitly represented;
- the heartbeat proves only scheduler/message activity while the material Function/Service can still be failed.

Heartbeat presence shall not be interpreted as proof of complete system health unless the controlled project health semantics explicitly establish that relationship.

## 5. L2 Trace

### 5.1 Primary Realization Candidate

- `SCAF-ROB-004` — provides a reusable observation mechanism that can feed a project-defined health/liveness classification without defining that classification itself.
- `SCAF-ROB-005` — provides a candidate way to make loss of required liveness/progress detectable during the applicable operating context.

### 5.2 Supporting Realization

- `SCAF-ROB-031` — can contribute to a project-defined diagnostic/detection-coverage objective when heartbeat coverage and limitations are explicitly controlled.
- `SCAF-OBS-014` — can expose routine liveness/status observations needed for operational supervision.
- `SCAF-OBS-015` — heartbeat history, age or missed-progress evidence can contribute to diagnosis while remaining distinct from the authoritative health/failure decision.

### 5.3 Constraint Inputs

- `SCAF-TIME-002` — the timebase used to evaluate liveness age/interval is a project decision.
- `SCAF-TIME-006` — heartbeat period, deadline, tolerance and detection latency are project values, not catalog constants.
- `SCAF-INT-010` — where liveness crosses a reconnectable Interaction, session/incarnation identity must prevent stale heartbeat evidence from being accepted as current-session liveness.

## 6. Required PDA Decisions

- monitored participant, Service or execution responsibility;
- exact project meaning of liveness, progress, late, missing, unknown and indeterminate observation;
- heartbeat/progress source and the responsibility that evaluates it;
- timebase, interval/deadline/tolerance and acceptable detection latency;
- session/incarnation correlation where restart/reconnection can occur;
- treatment of maintenance, suspension, partition or intentionally quiescent states;
- consequence/escalation when required liveness cannot be established;
- independence needed between monitored responsibility and liveness observer.

## 7. Mechanism Summary

The monitored responsibility produces or exposes a recurring or progress-coupled liveness indication. A supervising responsibility associates that indication with the correct participant/session/incarnation and evaluates its age or expected progression using a controlled project timebase. The result is mapped into the project-defined liveness/health decision input, including an explicit unknown/indeterminate outcome where the evidence is unavailable or ambiguous.

The indication may be explicit or carried by otherwise useful progress evidence. The mechanism should preserve enough identity/provenance to prevent an old session, restarted participant or stale observation from appearing current.

## 8. Variants

- explicit push heartbeat;
- supervisor poll/read of a liveness token;
- monotonic progress/generation counter;
- piggybacked liveness indication on normal Interaction traffic;
- milestone/event heartbeat where meaningful progress is naturally event-driven.

## 9. Forces / Tradeoffs

- detection latency versus observation traffic/CPU/wakeup cost;
- observer independence versus architecture complexity;
- false failure classification under jitter/partition/overload versus slower detection;
- progress fidelity versus low coupling;
- additional identity/timebase management where participants can restart independently.

## 10. Failure / Weakness Modes

- heartbeat producer remains active while the material Function/Service is stalled;
- supervisor and monitored responsibility share a common failure;
- stale/session-mismatched heartbeat is accepted after reconnect/restart;
- timebase drift or scheduling delay creates false timeout decisions;
- observation overload causes heartbeat loss that is mistaken for monitored failure;
- missing heartbeat evidence is silently interpreted as a definitive failure without an indeterminate state.

## 11. Selection Consequences

Selection creates a need to control liveness source identity, timing, incarnation/session handling, supervisor behavior and failure consequence. It also creates evidence and observer-effect considerations if heartbeat generation/evaluation can materially perturb the monitored property.

## 12. Composition Relations

### Requires

- project-defined liveness/health decision semantics and applicable timebase.

### Commonly Composed With

- `SCAF-PAT-SUP-002` — Independent Watchdog with Escalation;
- `SCAF-PAT-REC-001` — Bounded Retry with Escalation;
- `SCAF-PAT-EVD-001` — Pre/Post-Trigger Retained Incident Evidence Ring.

### Alternative To

- other project-specific progress/deadline supervision mechanisms that establish the same required observation property.

### Conflicts With

- designs that treat any traffic or heartbeat receipt as unconditional proof of complete health.

### Subsumes

- None.

### Supersedes

- None.

## 13. External Authority Considerations

External safety/security/regulatory/risk authority may constrain detection latency, independence, diagnostic coverage, acceptable false-negative/false-positive behavior or required response. Those inputs remain owned by their source authorities.

## 14. Re-evaluation Triggers

Re-evaluate when monitored responsibility, Service consequence, execution model, scheduling/transport latency, timebase, session/incarnation behavior, partition assumptions, observer independence or required detection coverage materially changes.

## 15. Provenance / Reference Basis

This pattern is a SCAF-new reusable synthesis derived from the frozen `SCAF-ROB`, `SCAF-TIME`, `SCAF-INT` and `SCAF-OBS` obligations. It does not promote a technology-specific heartbeat implementation or donor API.

## 16. L3 / L4 Boundary Note

L3 intentionally does not define timer values, heartbeat packet formats, register use, RTOS task structure, transport framing, counter width, scheduling priority, source code or verification procedure. Those are project-realization/L4 decisions.
