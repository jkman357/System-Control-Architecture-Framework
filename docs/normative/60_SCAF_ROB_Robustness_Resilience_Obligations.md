# SCAF-ROB — Robustness & Resilience Obligations

**Release:** v0.0.2rc07  
**Concern:** `SCAF-ROB`  
**Layer:** L1 Concern Authority + L2 Required Project Decisions  
**Status:** Normative RC

## 1. Purpose

`SCAF-ROB` **Defines Framework Semantics / Obligation** for fault/error/failure meaning, health/failure determination, propagation, runtime containment, tolerance, degradation, failover/reconfiguration, recovery/repair/retry, resynchronization/reintegration, distributed failure/reconciliation, correlated/cascading failure and long-run resilience outcomes without prescribing a watchdog, heartbeat, redundancy topology, retry algorithm, recovery implementation or other realization mechanism.

`SCAF-ROB` is the primary framework semantic authority for deciding what a material abnormal/failure/health condition means at runtime and what resilience outcome is required where that concern is Applicable. The **Project Design Authority Defines Project Instance / Decision** for the actual project failure classifications, health criteria, containment/tolerance/degradation/recovery decisions, mappings to the RUN operational-state model and project-specific resilience values.

`SCAF-ROB` consumes controlled context/structure/contract/timing/state/lifecycle/configuration/security inputs from other concerns. It does not redefine `SCAF-CTX` Service consequence, `SCAF-ARCH` structural/Domain boundaries, `SCAF-INT` contract semantics, `SCAF-TIME` measurable limits, `SCAF-RUN` operational-state representation, `SCAF-LIFE` lifecycle transaction semantics, `SCAF-CFG` persistent-state authority or `SCAF-OBS` evidence representation/preservation/export.

## 2. L1 Authority Boundary

`SCAF-ROB` **Defines Framework Semantics / Obligation** for:

- material fault/error/failure and health/resilience concern identification;
- distinction and trace among fault source/condition, activation, erroneous state/effect, propagation, Service failure and System consequence where material;
- health/failure determination and detectability/latent-condition semantics;
- runtime propagation and containment outcomes using controlled structural/Domain inputs from `SCAF-ARCH`;
- tolerance, masking, redundancy, failover and reconfiguration outcome requirements where Applicable;
- graceful degradation and continuity-of-service resilience outcomes constrained by `SCAF-CTX` and applicable external authorities;
- recovery, repair, retry/escalation, resynchronization and reintegration outcome semantics;
- communication partition/reconciliation resilience semantics while preserving `SCAF-INT` contract/session authority;
- common-mode/correlated faults, cascading behavior, recovery storms and peer-recovery dependencies;
- resilience response to resource exhaustion, long-duration accumulation and other measurable limit violations supplied by `SCAF-TIME`;
- failure-response properties when `SCAF-LIFE` lifecycle operations or `SCAF-CFG` controlled configuration/persistent state fail;
- resilience-observability requirements without taking over `SCAF-OBS` evidence semantics;
- traceability and re-evaluation of material robustness/resilience decisions.

The **Project Design Authority Defines Project Instance / Decision** for actual project fault assumptions, health/failure criteria, propagation/containment decisions, degraded-service/recovery outcomes, failure-response mappings, resilience limits and reintegration criteria, constrained by applicable external safety/security/risk authority inputs.

`SCAF-ROB` does not define universal failure names, a universal `Fault/Degraded/Recovery/Safe` RUN state model, project structural Domain boundaries, timing budgets, communication protocols, lifecycle transaction sequences, persistent configuration ownership, evidence storage/export mechanisms or security threat/risk acceptance authority.

## 3. Project-Applicable Obligations

### `SCAF-ROB-001` — Material robustness / resilience concern identification

**Target:** Project-Applicable Obligation

The project **SHALL** identify each abnormal-condition, fault/error/failure, health, propagation, containment, degradation, recovery or other resilience concern whose occurrence or mishandling can materially affect an applicable Function, Capability, Service, Interaction, architecture decision, operational state, lifecycle transaction, temporal/resource claim, security/safety constraint or verification obligation.

### `SCAF-ROB-002` — Fault / Error / Failure semantic chain

**Target:** Project-Applicable Obligation

For each material robustness concern, the project **SHALL** define the applicable distinctions and trace among fault source/condition, activation, erroneous state/effect, propagation, Service failure and System consequence to the extent needed to avoid treating all abnormal symptoms as the same failure concept.

Where a stage is not separately meaningful for the project concern, the project **SHALL** preserve sufficient controlled rationale/trace so downstream health, containment and verification decisions are not ambiguous.

### `SCAF-ROB-003` — Failure consequence provenance

**Target:** Project-Applicable Obligation

Each material Service failure or System consequence used to drive a ROB decision **SHALL** trace to the applicable controlled `SCAF-CTX` Function/Service consequence and to applicable external safety, security, regulatory or risk authority constraints/acceptance basis where those authorities govern the consequence.

### `SCAF-ROB-004` — Health / failure determination semantics

**Target:** Project-Applicable Obligation

Where health or failure determination is material, the project **SHALL** define the applicable health/failure states or decision outcomes, the criteria and controlled inputs by which they are assigned, and the project meaning/consequence of unknown, indeterminate or unavailable health information where such a condition can occur.

### `SCAF-ROB-005` — Detectability, latent condition and diagnostic-coverage requirement

**Target:** Project-Applicable Obligation

For each material robustness concern, the project **SHALL** determine whether the relevant condition/effect must be detectable during the required operating context, may remain latent for a controlled period/context, or is otherwise handled by an approved architecture basis. Where detection or diagnostic coverage is required, the project **SHALL** define the required detection/coverage property and its consequence if not achieved.

**Boundary note (informative):** Measurable detection latency or timing bounds are controlled through `SCAF-TIME`; verification/evidence-sufficiency semantics are controlled through `SCAF-ASSUR` and Project Verification / Assurance Authority.

### `SCAF-ROB-006` — Health-monitor / supervisor failure semantics

**Target:** Project-Applicable Obligation

Where a health/failure determination depends on a monitor, supervisor or diagnostic responsibility whose own failure can materially affect the system decision, the project **SHALL** define the consequence of monitor unavailability, degradation, disagreement or invalid output and the controlled project behavior required to prevent an unqualified indication of healthy/normal operation.

### `SCAF-ROB-007` — Failure propagation path

**Target:** Project-Applicable Obligation

For each material fault/error/failure concern, the project **SHALL** identify the applicable propagation path or affected responsibility/Interface/shared resource/Domain sufficiently to establish which Functions, Services, Nodes/participants, lifecycle operations or operational states can be affected.

### `SCAF-ROB-008` — Runtime containment requirement

**Target:** Project-Applicable Obligation

Where containment is required, the project **SHALL** define the required runtime containment outcome and the controlled `SCAF-ARCH` structural/Domain boundaries or responsibilities on which the containment claim depends.

The project **SHALL** define what constitutes containment success/failure at the behavior level without allowing ROB to redefine the actual structural Domain boundary owned by the applicable architecture decision.

### `SCAF-ROB-009` — Tolerance / masking / redundancy / failover / reconfiguration applicability

**Target:** Project-Applicable Obligation

Where continued Service or preservation of an approved property may depend on tolerance, masking, redundancy, failover or reconfiguration, the project **SHALL** determine which of those resilience outcomes are Applicable and define the required project outcome, eligibility/selection criteria and consequence when the required outcome cannot be established.

This obligation does not prescribe a redundancy topology, voting scheme, failover mechanism or reconfiguration algorithm.

### `SCAF-ROB-010` — Graceful degradation and degraded-Service outcome

**Target:** Project-Applicable Obligation

Where degraded operation is material, the project **SHALL** define the required degraded Function/Service outcome, the conditions under which the degradation requirement applies, and the controlled consequence when the required degraded outcome cannot be maintained.

The degraded-Service requirement **SHALL** trace to the applicable `SCAF-CTX` consequence and to applicable safety/security/risk authority constraints. The actual operational-state representation/mapping remains a `SCAF-RUN` Project Design Authority decision.

### `SCAF-ROB-011` — Recovery / repair / retry outcome and termination criteria

**Target:** Project-Applicable Obligation

Where recovery, repair or retry is Applicable, the project **SHALL** define the required recovery outcome, the criteria for determining recovery success/failure, and the controlled retry/escalation/termination condition needed to prevent indefinite or ambiguous recovery behavior.

**Boundary note (informative):** Measurable retry/recovery time, count, rate or resource limits are controlled through applicable `SCAF-TIME` project decisions; RUN represents resulting operational state/transition semantics.

### `SCAF-ROB-012` — Resynchronization / reintegration criteria

**Target:** Project-Applicable Obligation

Where a participant, state, resource or service can be resynchronized or reintegrated after degradation/recovery, the project **SHALL** define the required consistency/eligibility criteria that must be satisfied before reintegration and the consequence when those criteria are not satisfied.

The actual RUN operational-state mapping, INT session/contract state and LIFE lifecycle state remain controlled by their respective concerns.

### `SCAF-ROB-013` — Communication partition / reconnect reconciliation resilience

**Target:** Project-Applicable Obligation

Where communication partition, disconnect or later reconnection can create stale ownership/state, replay, inconsistent decisions or unsafe/unacceptable Service behavior, the project **SHALL** define the resilience consequence and reconciliation requirement needed before normal coordinated operation resumes.

**Boundary note (informative):** `SCAF-INT` retains Interface/Interaction/session/compatibility and exchange-contract semantics. ROB defines the required resilience outcome after the partition/reconnect condition affects system robustness.

### `SCAF-ROB-014` — Common-mode / correlated failure assumptions

**Target:** Project-Applicable Obligation

Where redundancy, separation or independent recovery claims rely on independence assumptions, the project **SHALL** identify material common-mode/correlated failure sources or shared dependencies that can invalidate those assumptions and define the required project treatment or residual-risk decision/acceptance under the applicable risk authority.

### `SCAF-ROB-015` — Cascading failure / recovery-storm / peer-dependency resilience

**Target:** Project-Applicable Obligation

Where one failure, recovery action or peer dependency can trigger cascading failure, repeated recovery, oscillation or recovery-storm behavior, the project **SHALL** define the required bounding/containment outcome and the project conditions under which recovery/reconfiguration may proceed or must be inhibited/escalated.

### `SCAF-ROB-016` — Resource exhaustion and long-run resilience response

**Target:** Project-Applicable Obligation

Where violation of a controlled `SCAF-TIME` capacity/resource/accumulation bound or other long-duration condition can materially affect robustness, the project **SHALL** define the health/failure interpretation and required containment/degradation/recovery outcome for the violated condition.

`SCAF-TIME` retains the measurable bound, horizon, threshold, capacity and margin semantics; ROB defines the resilience meaning/response after the controlled condition is violated.

### `SCAF-ROB-017` — Lifecycle-operation failure response

**Target:** Project-Applicable Obligation

Where failure of a boot, reset, power, update, activation or rollback-related lifecycle operation can materially affect system robustness, the project **SHALL** define the required resilience outcome and trace it to the applicable controlled `SCAF-LIFE` transaction/state decision without redefining the lifecycle sequence, atomicity, activation or rollback semantics.

### `SCAF-ROB-018` — Configuration / persistent-state failure response

**Target:** Project-Applicable Obligation

Where invalid, corrupt, unavailable, inconsistent or otherwise unusable controlled configuration/persistent operational state can materially affect robustness, the project **SHALL** define the required health/failure interpretation and resilience outcome while preserving `SCAF-CFG` authority for the configuration/persistence source, ownership, version and migration semantics.

### `SCAF-ROB-019` — Robustness observability requirement

**Target:** Project-Applicable Obligation

For each material health/failure/resilience decision whose correct operation or verification depends on observation, the project **SHALL** identify the condition, decision or outcome that must be observable and trace that observation requirement to the applicable controlled ROB/source decision.

**Boundary note (informative):** `SCAF-OBS` defines observation, representation, provenance/correlation, preservation and export semantics, and Project Realization implements the observation mechanism. ROB does not prescribe log format, storage layout, transport or recorder mechanism.

### `SCAF-ROB-020` — Robustness / resilience traceability

**Target:** Project-Applicable Obligation

Each material ROB health/failure, containment, degradation, failover/reconfiguration, recovery/reintegration or other resilience decision **SHALL** trace to the applicable CTX consequence, ARCH boundary/dependency, INT contract, TIME bound, RUN state decision, LIFE lifecycle decision, CFG source, external authority constraint or other controlled source that motivates the ROB decision.

### `SCAF-ROB-021` — Robustness / resilience change and re-evaluation

**Target:** Project-Applicable Obligation

Changes to fault assumptions/classification, health criteria, propagation path, containment boundary dependency, degraded-Service outcome, resilience strategy, recovery/reintegration criteria, common-mode assumption, capacity/resource bound, lifecycle/configuration dependency or external risk/safety/security constraint **SHALL** trigger re-evaluation of affected architecture, Interface, timing, runtime, lifecycle, observability, configuration, security and verification obligations.

## 4. Framework Normative Invariants

### `SCAF-ROB-022` — ROB / RUN failure-condition versus operational-state boundary

**Target:** Framework Normative Invariant

`SCAF-ROB` **Defines Framework Semantics / Obligation** for fault/error/failure, health determination, degradation/recovery meaning and required resilience outcome.

`SCAF-RUN` **Defines Framework Semantics / Obligation** for operational-state representation, permitted transition/result semantics, Operational Incarnation and authoritative current-state consistency. ROB **SHALL NOT** define a universal `Fault`, `Degraded`, `Recovery` or `Safe` RUN state name/sequence merely because a ROB-controlled condition is represented in the project state model.

The **Project Design Authority Defines Project Instance / Decision** for the actual mapping of controlled ROB conditions/outcomes into the project RUN state/transition model.

### `SCAF-ROB-023` — ROB / ARCH containment boundary

**Target:** Framework Normative Invariant

`SCAF-ARCH` **Defines Framework Semantics / Obligation** for structural/Domain boundary representation; the Project Design Authority defines the actual project Domain boundaries and structural responsibilities.

`SCAF-ROB` **Defines Framework Semantics / Obligation** for runtime fault/error propagation and containment/tolerance behavior using those controlled boundaries. ROB **SHALL NOT** redefine an actual project structural/Domain boundary merely to express a containment response.

### `SCAF-ROB-024` — ROB / TIME measurable-limit boundary

**Target:** Framework Normative Invariant

`SCAF-TIME` **Defines Framework Semantics / Obligation** for measurable timing, synchronization, capacity/resource, accumulation, threshold, horizon and margin properties.

`SCAF-ROB` **Defines Framework Semantics / Obligation** for health/failure interpretation, containment, degradation and recovery response after an applicable controlled measurable condition is violated. ROB **SHALL NOT** take ownership of the underlying TIME project value merely because the violation drives a resilience response.

### `SCAF-ROB-025` — ROB / INT contract and session boundary

**Target:** Framework Normative Invariant

`SCAF-INT` **Defines Framework Semantics / Obligation** for Interface/Interaction validity, negative exchange outcome, semantic ordering, compatibility and Protocol/Connection Session Identity.

`SCAF-ROB` **Defines Framework Semantics / Obligation** for the required system resilience behavior when an applicable interaction/communication failure or contract violation materially affects robustness. ROB **SHALL NOT** redefine INT contract/session semantics as a resilience mechanism.

### `SCAF-ROB-026` — ROB / LIFE lifecycle-failure boundary

**Target:** Framework Normative Invariant

`SCAF-LIFE` **Defines Framework Semantics / Obligation** for boot/power/reset/update/activation/rollback transaction and state semantics, lifecycle atomicity and Boot Incarnation / Boot Generation.

`SCAF-ROB` **Defines Framework Semantics / Obligation** for resilience properties required when those lifecycle operations fail. ROB **SHALL NOT** redefine lifecycle sequencing/atomicity/activation/rollback semantics merely to specify a failure response.

### `SCAF-ROB-027` — ROB / OBS / ASSUR evidence boundary

**Target:** Framework Normative Invariant

`SCAF-ROB` **Defines Framework Semantics / Obligation** for what constitutes the applicable health/failure/resilience condition and required resilience outcome.

`SCAF-OBS` **Defines Framework Semantics / Obligation** for observation, representation, preservation and export of health/diagnostic/incident evidence. `SCAF-ASSUR` **Defines Framework Semantics / Obligation** for verification/evidence-sufficiency criteria, while Project Verification / Assurance Authority evaluates actual evidence sufficiency. Observation or an evidence-sufficiency determination **SHALL NOT** redefine ROB failure meaning or required resilience behavior.

### `SCAF-ROB-028` — ROB / CFG persistent-state boundary

**Target:** Framework Normative Invariant

`SCAF-CFG` **Defines Framework Semantics / Obligation** for configuration/persistent operational-state ownership, authority, validation, version/migration, atomic update/commit and persistence semantics.

`SCAF-ROB` **Defines Framework Semantics / Obligation** for required robustness/resilience behavior when controlled configuration/persistent state is invalid, corrupt, unavailable or inconsistent. ROB **SHALL NOT** become the configuration source authority.

### `SCAF-ROB-029` — Safety / security / risk authority boundary

**Target:** Framework Normative Invariant

SCAF does not independently invent a universal safety-significant `Safe State`, safety objective, security objective or risk-acceptance basis.

For safety-significant conditions, the applicable project safety/hazard authority remains the source authority for the safety objective/condition and risk-acceptance basis. Applicable security authority remains the source of security objectives/threat/risk constraints. The Project Design Authority integrates those controlled inputs into the actual project ROB/RUN/ARCH decisions.

`SCAF-ROB` **SHALL NOT** convert the specificity of an external safety/security/regulatory/risk constraint into ROB or PDA ownership of that external source authority.

### `SCAF-ROB-030` — ROB / PROF / Project Realization mechanism boundary

**Target:** Framework Normative Invariant

`SCAF-ROB` **Defines Framework Semantics / Obligation** for required robustness/resilience properties and project decisions, not the realization mechanism.

`SCAF-ROB` **SHALL NOT** require a specific watchdog, heartbeat, redundancy topology, voting mechanism, retry algorithm, failover implementation, reset mechanism, storage layout, communication protocol or scheduler as a universal L1/L2 rule. `SCAF-PROF` may **Guide Realization** and **Constrain** applicable realization choices where an implementation profile is later Applicable, and Project Realization implements the controlled project decision.

## 5. Required Project Decisions / Records

The following table is informative and does not create additional normative requirements.

| Decision / record | Project-side authority / provenance |
|---|---|
| Material ROB concern inventory | Project Design Authority / applicable risk or requirement authority |
| Fault/Error/Failure semantic classification | Project Design Authority, constrained by applicable source authority |
| Service/System consequence trace | CTX-controlled source + applicable external authority; integrated by Project Design Authority |
| Health/failure criteria and indeterminate-health semantics | Project Design Authority |
| Detectability / latent-condition / diagnostic-coverage requirement | Project Design Authority, verified using SCAF-ASSUR semantics |
| Health-monitor/supervisor failure consequence | Project Design Authority |
| Propagation path / affected dependencies | Project Design Authority, traced to ARCH/INT/TIME/RUN/LIFE as applicable |
| Runtime containment outcome | Project Design Authority, using controlled ARCH boundary decisions |
| Tolerance/masking/redundancy/failover/reconfiguration outcome | Project Design Authority |
| Degraded-Service outcome | Project Design Authority, constrained by CTX and applicable external authorities |
| Recovery/repair/retry outcome and termination criteria | Project Design Authority, constrained by TIME values where applicable |
| Resynchronization / reintegration criteria | Project Design Authority |
| Partition / reconciliation resilience requirement | Project Design Authority, constrained by INT contract/session decisions |
| Common-mode / correlated failure assumptions | Project Design Authority / applicable risk authority |
| Cascade / recovery-storm bounding outcome | Project Design Authority |
| Resource-exhaustion / long-run resilience response | Project Design Authority, triggered by controlled TIME condition |
| LIFE / CFG failure-response mapping | Project Design Authority, traced to applicable LIFE/CFG decision |
| ROB observability requirement | Project Design Authority, realized through applicable OBS decisions |

`SCAF-APP` may Disposition / Trace these decisions but does not own them.

## 6. Concern Boundaries

- `SCAF-CTX` **Defines Framework Semantics / Obligation** for Function/Service consequence and degraded-service need; applicable external authorities define safety/security/risk source constraints.
- `SCAF-ARCH` **Defines Framework Semantics / Obligation** for structural/Domain boundary representation; Project Design Authority defines actual boundaries.
- `SCAF-INT` **Defines Framework Semantics / Obligation** for Interface/Interaction/contract/session semantics.
- `SCAF-TIME` **Defines Framework Semantics / Obligation** for measurable time/capacity/resource limits, thresholds, horizons and margins.
- `SCAF-RUN` **Defines Framework Semantics / Obligation** for operational-state representation, transition/result/current-state consistency and Operational Incarnation.
- `SCAF-ROB` **Defines Framework Semantics / Obligation** for fault/error/failure, health determination, propagation/containment, degradation and resilience response.
- `SCAF-LIFE` **Defines Framework Semantics / Obligation** for boot/power/reset/update/activation/rollback lifecycle transactions/states and Boot Incarnation.
- `SCAF-CFG` **Defines Framework Semantics / Obligation** for configuration/persistent-state source authority and lifecycle.
- `SCAF-OBS` **Defines Framework Semantics / Obligation** for observation, representation, preservation and export of health/incident evidence.
- `SCAF-SEC` **Defines Framework Semantics / Obligation** for the SCAF security architecture interface/robustness boundary and consumes applicable security-authority objectives/constraints; it does not replace external security risk authority.
- `SCAF-ASSUR` **Defines Framework Semantics / Obligation** for verification/evidence-sufficiency semantics; Project Verification / Assurance Authority **Verifies** ROB obligations against the Applicable Satisfaction Basis.
- `SCAF-PROF` may **Guide Realization** and **Constrain** applicable realization choices; Project Realization implements the selected robustness/resilience mechanisms.

## 7. Non-Normative Example

A multi-participant service may require a scoped participant failure not to cascade through a shared resource and may require an approved degraded Service outcome until reintegration criteria are met. `SCAF-ARCH` supplies the controlled structural/Domain boundaries, `SCAF-ROB` requires the project to define the containment/degradation/reintegration outcomes, `SCAF-RUN` represents the resulting project operational states/transitions, `SCAF-TIME` supplies any measurable detection/recovery/capacity limits, and `SCAF-OBS` supplies evidence semantics. Whether the realization uses a watchdog, redundant provider, reconnect algorithm, reset action or another mechanism is outside L1/L2 ROB normative scope.
