# SCAF-RUN — Runtime Behavior, State & Operational Lifecycle Obligations

**Release:** v0.0.2rc08  
**Concern:** `SCAF-RUN`  
**Layer:** L1 Concern Authority + L2 Required Project Decisions  
**Status:** Normative RC

## 1. Purpose

`SCAF-RUN` **Defines Framework Semantics / Obligation** for service/operational-state meaning, state-domain responsibility, state-transition consistency, readiness/availability representation, generic operational lifecycle behavior and Operational Incarnation semantics without prescribing a state-machine implementation, scheduler, operating system, language, task/thread model or recovery mechanism.

`SCAF-RUN` is the primary framework semantic authority for the meaning and consistency of project operational states and transitions. The **Project Design Authority Defines Project Instance / Decision** for the actual project state domains, state identities, authoritative state responsibilities, permitted transitions, transition conditions, readiness/availability states and Operational Incarnation rules.

`SCAF-RUN` consumes controlled inputs from `SCAF-CTX`, `SCAF-ARCH`, `SCAF-INT` and `SCAF-TIME`; it does not redefine their logical Service intent, structural allocation, Interaction/data-contract semantics or measurable temporal/capacity properties. Boot/power/reset/update lifecycle semantics remain under `SCAF-LIFE`; fault/health/degradation/recovery semantics remain under `SCAF-ROB`.

## 2. L1 Authority Boundary

`SCAF-RUN` **Defines Framework Semantics / Obligation** for:

- material operational/state-domain identification;
- operational state meaning and state-domain authoritative responsibility;
- state invariants and allowed state-transition semantics;
- transition source/target, trigger/precondition/guard and resulting operational-state semantics where applicable;
- service readiness and availability state representation;
- generic operational start/stop/suspend/resume semantics after applicable platform/lifecycle handoff;
- mapping between CTX operating modes and runtime operational states where such mapping exists;
- cross-participant operational-state consistency where more than one participant observes, derives or acts on the same operational state;
- Operational Incarnation / Operational State Generation semantics where needed to distinguish restarted or replaced runtime state;
- runtime treatment of transitional, unknown or indeterminate operational state where material;
- traceability and re-evaluation of material operational-state decisions.

The **Project Design Authority Defines Project Instance / Decision** for actual project states, transitions, runtime state authority/source, readiness/availability criteria, state-consistency rules and Operational Incarnation semantics.

`SCAF-RUN` does not define project Interface/data semantics (`SCAF-INT`), timing values or measurable concurrency/capacity properties (`SCAF-TIME`), boot/reset/power/update lifecycle semantics (`SCAF-LIFE`), resilience detection/degradation/recovery behavior (`SCAF-ROB`), persistent configuration/state authority (`SCAF-CFG`) or diagnostic/evidence representation (`SCAF-OBS`).

## 3. Project-Applicable Obligations

### `SCAF-RUN-001` — Material operational state-domain identification

**Target:** Project-Applicable Obligation

The project **SHALL** identify each operational/state domain whose state or transition can materially affect an applicable Function, Capability, Service, Interaction, architecture decision, temporal claim or verification obligation.

### `SCAF-RUN-002` — Project state-model authority and runtime authoritative-state responsibility

**Target:** Project-Applicable Obligation

For each material operational/state domain, the Project Design Authority **SHALL** define the actual project state model and assign the project runtime responsibility that determines and/or maintains the authoritative current operational state. The project **SHALL** also define the controlled representation or source by which other project responsibilities determine that authoritative current state.

A display, artifact, variable, cache, message, request or diagnostic/evidence record **SHALL NOT** become the runtime authoritative-state responsibility, nor the Project Design Authority, merely because it carries, requests, displays or records a state value.

### `SCAF-RUN-003` — Operational-state semantics and invariants

**Target:** Project-Applicable Obligation

For each material operational state, the project **SHALL** define the meaning of the state and the invariants, allowed service behavior or other controlled conditions that must hold while the state is asserted.

Where unknown, indeterminate or transitional state can occur and is material, the project **SHALL** define its operational meaning sufficiently to prevent it from being silently treated as a normal stable state.

### `SCAF-RUN-004` — Permitted state transitions

**Target:** Project-Applicable Obligation

For each material operational/state domain, the project **SHALL** define the permitted source-to-target state transitions and define the controlled project outcome/handling semantics for attempted transitions that are not permitted by the controlled state model.

### `SCAF-RUN-005` — Transition conditions and resulting-state semantics

**Target:** Project-Applicable Obligation

Where transition correctness depends on a trigger, request, precondition, guard, completion condition or other controlled input, the project **SHALL** identify the applicable controlled condition and define how satisfaction/non-satisfaction of that condition maps to the operational-state transition and resulting state.

**Boundary note (informative):** Source semantics for an Interaction event, temporal condition, lifecycle condition or resilience condition remain under the applicable `SCAF-INT`, `SCAF-TIME`, `SCAF-LIFE` or `SCAF-ROB` framework authority. `SCAF-RUN` defines framework obligations only for how a controlled input participates in operational-state transition semantics.

### `SCAF-RUN-006` — Readiness and availability state semantics

**Target:** Project-Applicable Obligation

Where readiness or availability is material, the project **SHALL** define the applicable operational readiness/availability states, the project criteria for asserting them, and the Service/Function consequence represented by each state.

**Boundary note (informative):** Where readiness/availability depends on a fault or health decision, the applicable `SCAF-ROB` controlled decision/obligation supplies the failure/health semantics. RUN uses that controlled result in the operational-state model without taking ownership of failure interpretation, degradation strategy or recovery response.

### `SCAF-RUN-007` — Generic operational start/stop/suspend/resume lifecycle

**Target:** Project-Applicable Obligation

Where start, stop, suspend, resume or equivalent operational lifecycle behavior is material after applicable platform activation, the project **SHALL** define the relevant operational states, permitted transitions and entry/exit conditions.

**Boundary note (informative):** This requirement does not define boot, power, reset or update lifecycle transactions; those remain under `SCAF-LIFE`.

### `SCAF-RUN-008` — CTX operating-mode to operational-state mapping

**Target:** Project-Applicable Obligation

Where a material operating mode identified through `SCAF-CTX` is represented or enforced through runtime operational state, the project **SHALL** define the mapping and any controlled conditions under which the mode/state relationship changes.

### `SCAF-RUN-009` — LIFE-to-RUN readiness handoff

**Target:** Project-Applicable Obligation

Where completion of a boot, reset, power or update lifecycle transaction does not itself establish required operational readiness, the project **SHALL** define the controlled handoff condition between the applicable `SCAF-LIFE` state/decision and the `SCAF-RUN` readiness/operational state.

### `SCAF-RUN-010` — Cross-participant operational-state consistency

**Target:** Project-Applicable Obligation

Where multiple participants observe, derive, cache or act on the same material operational state, the project **SHALL** define the authoritative current-state source/responsibility and the consistency/divergence semantics necessary to prevent ambiguous operational decisions.

**Boundary note (informative):** Exchange semantics remain under `SCAF-INT`; measurable temporal/capacity conditions used to establish cross-participant consistency remain under `SCAF-TIME`.

### `SCAF-RUN-011` — Operational Incarnation identity

**Target:** Project-Applicable Obligation

Where restart, replacement or re-creation of runtime operational state can make old and new state instances ambiguous, the project **SHALL** define Operational Incarnation / Operational State Generation semantics sufficient to distinguish the applicable runtime incarnations.

The project **SHALL** keep Operational Incarnation distinguishable from Boot Incarnation (`SCAF-LIFE`), Protocol/Connection Session Identity (`SCAF-INT`) and Time Epoch / Time Domain (`SCAF-TIME`).

### `SCAF-RUN-012` — State-change request versus state transition

**Target:** Project-Applicable Obligation

Where an Interaction, command, configuration change or other request can cause an operational-state transition, the project **SHALL** distinguish the request/intent from the authoritative transition result so that receipt or acceptance of the request is not silently treated as proof that the operational state changed.

### `SCAF-RUN-013` — Operational-state traceability

**Target:** Project-Applicable Obligation

Each material operational-state domain and transition decision **SHALL** trace to the applicable CTX Function/Service/mode need, ARCH responsibility/allocation, INT contract, TIME constraint or other controlled source that motivates the runtime decision.

### `SCAF-RUN-014` — Operational-state change and re-evaluation

**Target:** Project-Applicable Obligation

Changes to operational states, authoritative state responsibility, transition semantics, readiness/availability criteria, CTX-mode mapping, cross-participant consistency or Operational Incarnation rules **SHALL** trigger re-evaluation of affected Interface, timing, robustness, lifecycle, configuration, observability, security and verification obligations.

### `SCAF-RUN-020` — Readiness / availability consequence trace

**Target:** Project-Applicable Obligation

Where readiness or availability is material, the project **SHALL** trace the Service/Function consequence represented by each readiness/availability state to the applicable controlled `SCAF-CTX` source and to applicable external safety/security/risk constraints where those constraints govern the consequence.

### `SCAF-RUN-021` — Cross-participant measurable-consistency constraint trace

**Target:** Project-Applicable Obligation

Where cross-participant operational-state consistency depends on a measurable delay, age, synchronization, capacity or other TIME-owned property, the project **SHALL** trace the RUN consistency decision to the applicable controlled `SCAF-TIME` project decision; where it depends on exchange semantics, the project **SHALL** trace to the applicable `SCAF-INT` contract decision.

## 4. Framework Normative Invariants

### `SCAF-RUN-015` — RUN / INT / TIME authority boundary

**Target:** Framework Normative Invariant

`SCAF-RUN` **Defines Framework Semantics / Obligation** for operational-state meaning and state-transition consistency.

`SCAF-RUN` **SHALL NOT** redefine Interface/Interaction/data-contract meaning, semantic ordering or protocol/connection session identity for which `SCAF-INT` is the primary framework semantic authority, nor timebase, synchronization, chronological ordering, deadline/latency/freshness-age or measurable concurrency/capacity/resource properties for which `SCAF-TIME` is the primary framework semantic authority.

RUN may use those controlled inputs to define operational-state transitions without becoming their source authority.

### `SCAF-RUN-016` — RUN / LIFE operational-lifecycle boundary

**Target:** Framework Normative Invariant

`SCAF-RUN` **Defines Framework Semantics / Obligation** for service/operational-state lifecycle and operational readiness after applicable lifecycle handoff.

`SCAF-LIFE` retains primary framework semantic authority for boot, power, reset, update and activation transaction/state semantics and for Boot Incarnation / Boot Generation. A lifecycle transaction may constrain or trigger a RUN transition without transferring lifecycle authority to RUN.

### `SCAF-RUN-017` — RUN / ROB failure-response boundary

**Target:** Framework Normative Invariant

`SCAF-RUN` **Defines Framework Semantics / Obligation** for the representation and consistency of operational states and transitions, including project-defined non-normal states where applicable.

`SCAF-RUN` **SHALL NOT** become the source authority for fault/error/failure interpretation, health classification, containment, degradation strategy, recovery, repair, resynchronization or reintegration; those runtime resilience semantics belong to `SCAF-ROB`.

`SCAF-ROB` **Defines Framework Semantics / Obligation** for the applicable failure/health/resilience condition and required resilience outcome. `SCAF-RUN` **Defines Framework Semantics / Obligation** for operational-state representation, permitted-transition/result and authoritative current-state consistency semantics. The **Project Design Authority Defines Project Instance / Decision** for the actual project mapping and state model.

### `SCAF-RUN-018` — RUN / CFG persistent-state boundary

**Target:** Framework Normative Invariant

`SCAF-RUN` **Defines Framework Semantics / Obligation** for current operational-state meaning and transition consistency.

`SCAF-CFG` retains primary framework semantic authority for configuration and persistent operational-state ownership/version/migration semantics where persistence is required. Persistence of a state **SHALL NOT** transfer RUN operational-state semantic authority to CFG.

### `SCAF-RUN-019` — CTX operating-mode / RUN operational-state boundary

**Target:** Framework Normative Invariant

Mission/context significance of material operating modes belongs to `SCAF-CTX`; operational runtime representation/transition semantics belong to `SCAF-RUN` where those modes are realized as state. `SCAF-RUN` **SHALL NOT** redefine the mission/context significance of an operating mode merely because the mode is represented by runtime state.

### `SCAF-RUN-022` — RUN / OBS evidence boundary

**Target:** Framework Normative Invariant

`SCAF-RUN` **Defines Framework Semantics / Obligation** for authoritative current operational-state meaning and state-transition/result consistency.

`SCAF-OBS` **Defines Framework Semantics / Obligation** for observing, representing, preserving and exporting runtime state/transition/incarnation evidence. Observation or preservation of a state **SHALL NOT** transfer runtime authoritative-state responsibility or RUN semantic authority to OBS.

### `SCAF-RUN-023` — Operational / boot / session / time identity partition

**Target:** Framework Normative Invariant

Operational Incarnation / Operational State Generation belongs to `SCAF-RUN`; Boot Incarnation / Boot Generation belongs to `SCAF-LIFE`; Protocol / Connection Session Identity belongs to `SCAF-INT`; Time Epoch / Time Domain belongs to `SCAF-TIME`. `SCAF-OBS` may record or correlate these identities without redefining their primary semantics.

## 5. Required Project Decisions / Records

The following table is informative and does not create additional normative requirements.

| Decision / record | Project-side authority / provenance |
|---|---|
| Material operational/state-domain inventory | Project Design Authority |
| Project state model / runtime authoritative-state responsibility and representation | Project Design Authority |
| Operational-state meanings / invariants | Project Design Authority, constrained by CTX/ROB/external authority where applicable |
| Permitted transitions / transition conditions | Project Design Authority |
| Readiness / availability state criteria and consequence trace | Project Design Authority, traced to applicable CTX need/external constraints and ROB-controlled health/failure inputs where applicable |
| Operational start/stop/suspend/resume semantics | Project Design Authority, constrained by LIFE handoff where applicable |
| CTX mode ↔ RUN state mapping | Project Design Authority |
| Cross-participant state-consistency semantics and cross-concern constraint trace | Project Design Authority, constrained by INT/TIME decisions |
| Operational Incarnation semantics | Project Design Authority |
| State-change request versus transition-result semantics | Project Design Authority, constrained by INT/CFG source decisions as applicable |

`SCAF-APP` may Disposition / Trace these decisions but does not own them.

## 6. Concern Boundaries

- `SCAF-CTX` **Defines Framework Semantics / Obligation** for mission, Function/Service need, material operating-mode significance and consequence context.
- `SCAF-ARCH` **Defines Framework Semantics / Obligation** for structural responsibilities, Nodes/Domains and allocation.
- `SCAF-INT` **Defines Framework Semantics / Obligation** for Interface/Interaction/data-contract semantics and protocol/connection session identity.
- `SCAF-TIME` **Defines Framework Semantics / Obligation** for timebase/synchronization, temporal values and measurable concurrency/capacity/resource constraints.
- `SCAF-RUN` **Defines Framework Semantics / Obligation** for operational-state meaning, transition consistency, readiness/availability representation and Operational Incarnation.
- `SCAF-ROB` **Defines Framework Semantics / Obligation** for fault/error/failure, health, containment, degradation and recovery semantics.
- `SCAF-LIFE` **Defines Framework Semantics / Obligation** for boot/power/reset/update/activation lifecycle and Boot Incarnation.
- `SCAF-CFG` **Defines Framework Semantics / Obligation** for configuration and persistent operational-state ownership/version/migration semantics.
- `SCAF-OBS` **Observes** and records runtime state/transition/incarnation evidence without becoming source authority.
- `SCAF-SEC` **Constrains** operational-state decisions using applicable security-authority inputs.
- `SCAF-ASSUR` **Defines Framework Semantics / Obligation** for assurance/evidence semantics; Project Verification / Assurance Authority **Verifies** RUN obligations against the Applicable Satisfaction Basis.

## 7. Non-Normative Example

A system may expose `Not Ready`, `Ready` and `Running` operational states. `SCAF-RUN` requires the project to define what those states mean, who is authoritative for them, which transitions are permitted and what conditions establish readiness. A command received through an Interface may request `Running`, while `SCAF-INT` defines the command contract and `SCAF-TIME` may define a project-specific transition deadline. The receipt of the command is not itself proof that the RUN state changed. If a failed transition is classified as a fault and requires degradation/recovery, that failure interpretation and response belongs to `SCAF-ROB`, not RUN.
