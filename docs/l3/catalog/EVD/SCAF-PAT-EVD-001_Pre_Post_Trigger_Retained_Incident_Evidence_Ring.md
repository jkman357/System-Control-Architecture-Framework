# SCAF-PAT-EVD-001 — Pre/Post-Trigger Retained Incident Evidence Ring

**Development Release:** v0.0.3rc14  
**Pattern Family:** `EVD` — Evidence & Incident Recording  
**Pattern Kind:** Composite Pattern  
**Catalog Status:** Available  
**Maturity:** M2 — Architecture Reviewed  
**Introduced In:** v0.0.3rc03

## Metadata

| Field | Value |
|---|---|
| Pattern ID | `SCAF-PAT-EVD-001` |
| Pattern Name | Pre/Post-Trigger Retained Incident Evidence Ring |
| Pattern Family | `EVD` |
| Pattern Kind | Composite Pattern |
| Catalog Status | Available |
| Maturity | M2 — Architecture Reviewed |
| Introduced In | v0.0.3rc03 |
| Primary L2 Trace | `SCAF-OBS-016`, `SCAF-OBS-017`, `SCAF-OBS-018` |
| Supporting L2 Trace | `SCAF-OBS-010`, `SCAF-OBS-011`, `SCAF-OBS-012`, `SCAF-OBS-019`, `SCAF-OBS-020`, `SCAF-OBS-021` |
| Constraint Inputs | `SCAF-OBS-009`, `SCAF-OBS-013`, `SCAF-TIME-002`, `SCAF-TIME-011`, `SCAF-LIFE-010` |
| Profile Facets | Embedded/PC/SoC; volatile, retained or persistent evidence tiers; local or multi-source incident evidence |
| Provenance / Reference Basis | Frozen SCAF obligation-derived synthesis plus controlled reference to supplemental `Embedded_Incident_Crash_Recorder_Framework` v1.0.1rc03 (RC donor; no API/layout promotion) |

## 1. Intent

Continuously retain a bounded recent history of selected evidence, preserve the relationship between observations before and after a material trigger, and make the incident evidence set recoverable according to project-defined lifecycle-survivability and retention rules.

## 2. Problem

If evidence collection begins only after an incident is recognized, the initiating/first-observed abnormal condition and propagation sequence may already be lost. Conversely, unlimited continuous logging can exceed memory/storage/timing budgets or materially perturb the observed system. A reset/crash can also destroy the most relevant recent evidence unless survivability is deliberately designed.

## 3. Applicability

Consider this pattern where:

- investigation requires a bounded timeline before and/or after a material event;
- recent observations can be retained with controlled identity/provenance/time information;
- a trigger can mark/freeze/promote an incident evidence set;
- storage, observer effect and lifecycle-survivability can be bounded at project level.

## 4. Non-Applicability / Cautions

The pattern is not sufficient where the required source data never exists at the observation boundary, evidence must be externally durable before the local failure occurs, or the recorder shares a failure mode that destroys all evidence before trigger/preservation. Recorder order or timestamp proximity shall not be treated as proof of root cause.

## 5. L2 Trace

### 5.1 Primary Realization Candidate

- `SCAF-OBS-016` — preserves evidence that can distinguish the first observed abnormal condition from later propagation/terminal outcomes.
- `SCAF-OBS-017` — provides a reusable pre/post incident timeline mechanism without making the ring-buffer structure an L2 obligation.
- `SCAF-OBS-018` — can preserve/promote incident evidence across lifecycle transitions according to project-defined survivability semantics.

### 5.2 Supporting Realization

- `SCAF-OBS-010` — ring records can carry quality/completeness/drop/truncation limitations needed for interpretation.
- `SCAF-OBS-011` — recorder self-health/availability can be represented where confidence in evidence depends on recorder operation.
- `SCAF-OBS-012` — overflow/loss/unavailability can be explicitly represented rather than silently omitted.
- `SCAF-OBS-019` — retained/promoted evidence can support early-boot/crash-loop recovery where normal logging is defeated.
- `SCAF-OBS-020` — incident entries can carry source-defined boot/operational/session/time identities needed for interpretation.
- `SCAF-OBS-021` — incident evidence can be retained and exposed for a controlled horizon/condition.

### 5.3 Constraint Inputs

- `SCAF-OBS-009` — any causal/root-cause or other derived-inference claim using recorder evidence must consume the project-controlled causal-inference basis and evidence limitations; the recorder preserves evidence and uncertainty but does not establish causality by timestamp proximity or recorder order.
- `SCAF-OBS-013` — recorder overhead/observer effect must remain within project-controlled source concern/TIME constraints.
- `SCAF-TIME-002` — evidence chronology uses a controlled timebase identity/authority.
- `SCAF-TIME-011` — RAM/storage/CPU/channel capacity and margin constrain evidence depth/rate.
- `SCAF-LIFE-010` — retained evidence is consumed after lifecycle transition only when its source identity/provenance and lifecycle eligibility are interpretable.

## 6. Required PDA Decisions

- evidence classes/signals/events selected for continuous retention;
- evidence identity/provenance/time/incarnation fields needed for interpretation;
- trigger source/semantics and whether first-observed versus terminal triggers are distinct;
- pre-trigger and post-trigger coverage objectives and storage/resource budget;
- overwrite/freeze/promotion behavior after a trigger;
- survivability tier and lifecycle transitions the evidence must cross;
- overflow/drop/truncation/corruption representation;
- recorder self-health and observer-effect constraints;
- incident correlation across multiple participants/sources where applicable;
- retrieval/retention/expiration/security constraints.

## 7. Mechanism Summary

Selected evidence is continuously written into a bounded circular recent-history store with record identity/provenance and controlled chronological/correlation information. When a project-defined incident trigger occurs, the current history position and trigger identity are captured so the pre-trigger evidence window is preserved logically or physically. Collection may continue for a controlled post-trigger condition before the incident set is frozen, promoted or copied to a more survivable evidence tier.

The mechanism records evidence limitations such as overflow, dropped observations or invalid time/correlation where material. If evidence crosses reset/boot or another lifecycle transition, the retained set remains associated with the applicable source-defined lifecycle/operational/session/time identities rather than inventing a recorder-owned replacement identity.

## 8. Variants

- purely volatile circular evidence ring for live diagnosis;
- retained-memory ring surviving selected reset classes;
- two-tier recent-history ring plus persistent incident promotion;
- per-source local rings correlated at retrieval;
- trigger-freeze or trigger-mark-and-continue post-event capture.

## 9. Forces / Tradeoffs

- evidence depth/rate versus RAM/storage/CPU bandwidth;
- richer provenance/correlation versus record overhead;
- frequent persistence versus wear/latency/observer effect;
- wider pre-event context versus post-event capacity;
- stronger survivability versus coupling to lifecycle/storage mechanisms.

## 10. Failure / Weakness Modes

- ring overwrites the relevant event before trigger/promotion;
- trigger is detected too late or is itself unavailable;
- recorder blocks/perturbs timing and changes the incident behavior;
- reset/power loss destroys the supposedly retained tier;
- evidence time/session/incarnation is ambiguous after reboot;
- overflow/drop is hidden and the evidence is interpreted as complete;
- recorder failure is mistaken for absence of the source fault;
- copied/exported evidence loses provenance or quality limitations.

## 11. Selection Consequences

Selection consumes controlled memory/storage/time budget, requires evidence identity/provenance and trigger semantics, and may require lifecycle-survivable retention/export mechanisms. It can also create a need for recorder self-health and explicit observer-effect analysis.

## 12. Composition Relations

### Requires

- project-defined evidence scope, trigger semantics, time/correlation basis and retention/survivability objective.

### Commonly Composed With

- `SCAF-PAT-SUP-001` — Heartbeat / Liveness Supervision;
- `SCAF-PAT-SUP-002` — Independent Watchdog with Escalation;
- `SCAF-PAT-REC-001` — Bounded Retry with Escalation;
- `SCAF-PAT-PST-001` — Atomic Dual-Copy Persistent State for selected durable evidence metadata/state where semantically appropriate;
- `SCAF-PAT-LCM-001` — Transactional Update with Rollback for lifecycle-failure evidence.

### Alternative To

- continuous append-only logging, external trace capture or another evidence mechanism that establishes the required incident timeline/survivability property.

### Conflicts With

- synchronous high-coupling logging on a critical path where the observer-effect constraint cannot be met.

### Subsumes

- None.

### Supersedes

- None.

## 13. External Authority Considerations

Safety/security/regulatory/risk authority may constrain required evidence, retention duration, confidentiality/integrity, accessibility, incident-reporting scope or preservation across lifecycle transitions. Those source requirements remain external-authority inputs.

## 14. Re-evaluation Triggers

Re-evaluate when incident hypotheses, required evidence scope, execution/timing budget, reset/power/update behavior, evidence retention, storage technology, cross-participant correlation or external evidence constraints change.

## 15. Provenance / Reference Basis

This pattern is a SCAF L3 synthesis from frozen OBS/TIME/LIFE obligations and uses the supplemental `Embedded_Incident_Crash_Recorder_Framework` v1.0.1rc03 only as controlled RC reference input for generic incident-recording concepts. Recorder-specific API/ABI, binary layout, RAM budget, address, storage device and implementation recommendations are not promoted by this pattern.

## 16. L3 / L4 Boundary Note

L3 does not prescribe byte record layout, ring size, sampling period, exact pre/post duration, retained-RAM address, flash sector, file format, ISR/task API, checksum algorithm, export transport, source code or verification procedure.
