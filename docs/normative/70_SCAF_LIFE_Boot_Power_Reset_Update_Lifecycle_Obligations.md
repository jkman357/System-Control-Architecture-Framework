# SCAF-LIFE — Boot, Power, Reset & Update Lifecycle Obligations

**Release:** v0.0.2rc08  
**Concern:** `SCAF-LIFE`  
**Layer:** L1 Concern Authority + L2 Required Project Decisions  
**Status:** Normative RC

## 1. Purpose

`SCAF-LIFE` **Defines Framework Semantics / Obligation** for platform/system activation, boot, power, reset and update lifecycle transaction/state meaning, transaction result/atomicity semantics, activation/rollback/resume semantics, lifecycle coordination and Boot Incarnation / Boot Generation identity without prescribing a bootloader architecture, firmware-slot layout, flash algorithm, reset-register sequence, updater daemon, power-sequencing circuit, RTOS mechanism or other realization mechanism.

The **Project Design Authority Defines Project Instance / Decision** for the actual project lifecycle transaction model, lifecycle states/results, completion/commit/abort criteria, boot/reset/power/update coordination, activation/rollback decisions, Boot Incarnation mapping and project-specific lifecycle values, constrained by applicable external safety/security/regulatory/risk authority inputs.

`SCAF-LIFE` consumes controlled structural, contract, temporal, operational-state, resilience, configuration and observability inputs from other concerns. It does not redefine `SCAF-ARCH` structural allocation, `SCAF-INT` request/session/compatibility semantics, `SCAF-TIME` measurable timing properties, `SCAF-RUN` operational-state/readiness semantics, `SCAF-ROB` failure/health/resilience response, `SCAF-CFG` persistent configuration/state source authority or `SCAF-OBS` evidence representation/preservation/export.

## 2. L1 Authority Boundary

`SCAF-LIFE` **Defines Framework Semantics / Obligation** for:

- material boot, power, reset, update, activation, rollback, resume and related lifecycle transaction/state concerns;
- lifecycle transaction/state meaning, authoritative lifecycle result and completion/commit/abort semantics;
- lifecycle request/intent versus actual transaction acceptance, execution, completion, activation and result semantics;
- boot completion and controlled handoff to `SCAF-RUN` readiness/operational-state evaluation;
- Boot Incarnation / Boot Generation identity and its distinction from RUN Operational Incarnation, INT Protocol/Connection Session Identity and TIME Epoch/Time Domain;
- project reset classification/cause semantics and reset-domain consequence where material;
- retained-state validity requirements across applicable lifecycle transitions while preserving `SCAF-CFG` and `SCAF-OBS` authority;
- power lifecycle and brownout-relevant lifecycle outcome semantics where material;
- update transaction coordination, compatibility/precondition inputs, activation and rollback semantics;
- lifecycle transaction atomicity, interrupted-transaction and resume/rollback outcome semantics where Applicable;
- coordinated multi-participant lifecycle transition requirements without prescribing a coordination protocol;
- lifecycle observability/correlation requirements without taking over `SCAF-OBS` evidence semantics;
- lifecycle traceability and change/re-evaluation obligations.

The **Project Design Authority Defines Project Instance / Decision** for actual lifecycle transaction/state models, lifecycle authorities/responsibilities, completion and activation criteria, rollback/resume policies, reset classifications, update coordination and Boot Incarnation rules. External safety/security/regulatory/risk authorities remain source authorities for their own controlled objectives/constraints/acceptance basis.

`SCAF-LIFE` does not define universal lifecycle state names, a universal boot/update state machine, a required A/B image layout, universal reset taxonomy values, a universal rollback algorithm, RUN operational readiness, ROB failure response, CFG persistent-state ownership, OBS recorder/storage mechanisms or universal security authorization mechanisms.

## 3. Project-Applicable Obligations

### `SCAF-LIFE-001` — Material lifecycle concern identification

**Target:** Project-Applicable Obligation

The project **SHALL** identify each boot, power, reset, update, activation, rollback, resume or related lifecycle concern whose omission or mishandling can materially affect an applicable Function, Capability, Service, Interaction, architecture decision, operational state, robustness/resilience condition, persistent-state/configuration decision, security/safety constraint or verification obligation.

### `SCAF-LIFE-002` — Lifecycle transaction / state model

**Target:** Project-Applicable Obligation

For each material lifecycle concern, the project **SHALL** define the applicable lifecycle transaction/state model sufficiently to distinguish the controlled transaction or lifecycle condition, authoritative result, permitted lifecycle progression and project consequence of incomplete, aborted, interrupted or indeterminate lifecycle state where such outcomes can occur.

### `SCAF-LIFE-003` — Lifecycle authority and authoritative result responsibility

**Target:** Project-Applicable Obligation

For each material lifecycle transaction/state domain, the **Project Design Authority SHALL** define the project responsibility that determines and maintains the authoritative lifecycle transaction/result state and the controlled representation/source by which dependent responsibilities determine that lifecycle result.

A request, UI indication, cached value, message, diagnostic record or evidence artifact **SHALL NOT** become the runtime lifecycle-result authority merely because it carries or records a lifecycle state/result value.

### `SCAF-LIFE-004` — Lifecycle request / intent versus transaction result

**Target:** Project-Applicable Obligation

Where a request, command, policy decision or configuration/security decision can initiate a lifecycle transaction, the project **SHALL** distinguish the initiating request/intent from the authoritative lifecycle transaction result.

Where acceptance, execution, commit/completion and activation are materially distinct project concepts, the project **SHALL** define the controlled meaning/consequence of those distinctions rather than treating request receipt or acceptance as proof of completed/activated lifecycle state.

### `SCAF-LIFE-005` — Lifecycle transition conditions and completion criteria

**Target:** Project-Applicable Obligation

For each material lifecycle transaction, the project **SHALL** define the controlled entry/precondition, permitted transition/progression conditions, completion or abort criteria, and resulting lifecycle state/result required for dependent architecture decisions.

**Boundary note (informative):** `SCAF-INT`, `SCAF-TIME`, `SCAF-RUN`, `SCAF-ROB`, `SCAF-CFG` or applicable external authorities may supply controlled source conditions; LIFE defines framework obligations for lifecycle transaction/state/result semantics.

### `SCAF-LIFE-006` — LIFE-to-RUN readiness handoff

**Target:** Project-Applicable Obligation

Where lifecycle completion does not by itself establish operational readiness, the project **SHALL** define the controlled handoff condition between the applicable LIFE transaction/result and the `SCAF-RUN` readiness/operational-state decision.

Lifecycle completion **SHALL NOT** be treated as proof of RUN readiness unless the project-controlled readiness criteria explicitly establish that relationship.

### `SCAF-LIFE-007` — Boot Incarnation / Boot Generation identity

**Target:** Project-Applicable Obligation

Where restart, reset, boot, replacement or re-creation can make lifecycle evidence, retained state, interaction state or operational state ambiguous across lifecycle instances, the project **SHALL** define a Boot Incarnation / Boot Generation identity semantics sufficient to distinguish the relevant lifecycle-created instances.

The project **SHALL** keep Boot Incarnation distinguishable from `SCAF-RUN` Operational Incarnation, `SCAF-INT` Protocol/Connection Session Identity and `SCAF-TIME` Time Epoch / Time Domain.

### `SCAF-LIFE-008` — Reset classification / cause semantics

**Target:** Project-Applicable Obligation

Where reset cause, reset class or reset scope can materially affect lifecycle, recovery, retained-state validity, evidence interpretation or operational behavior, the project **SHALL** define the applicable reset classifications/causes and their controlled lifecycle meaning/consequence.

This obligation does not require a universal reset taxonomy or a specific hardware reset-cause register.

### `SCAF-LIFE-009` — Reset-domain and coordinated reset consequence

**Target:** Project-Applicable Obligation

Where reset affects only part of the System or coordinated participants have different reset domains, the project **SHALL** define the lifecycle consequence, required coordination/handoff and validity implications for dependent participants sufficiently to avoid treating a local reset as an implicit whole-System lifecycle event.

### `SCAF-LIFE-010` — Retained-state validity across lifecycle transitions

**Target:** Project-Applicable Obligation

Where RAM, persistent operational state, configuration, calibration, queued work, session-related state, incident evidence or other retained information may survive a lifecycle transition, the project **SHALL** define the validity/eligibility condition for consuming that retained information after the transition and the controlled consequence when validity cannot be established.

**Boundary note (informative):** `SCAF-CFG` retains persistent configuration/state source/version/migration authority; `SCAF-OBS` retains evidence provenance/preservation semantics; LIFE defines the lifecycle-transition validity obligation and handoff context.

### `SCAF-LIFE-011` — Power lifecycle / brownout-relevant semantics

**Target:** Project-Applicable Obligation

Where power-on, power-off, power-loss, brownout or partial-power lifecycle conditions can materially affect lifecycle correctness, the project **SHALL** define the applicable lifecycle state/result semantics, required transition outcome and controlled consequence for incomplete or indeterminate power-lifecycle progression.

This obligation does not prescribe a power-sequencing circuit, supervisor IC, voltage threshold or hardware reset mechanism.

### `SCAF-LIFE-012` — Update transaction applicability and authority

**Target:** Project-Applicable Obligation

Where software, firmware, programmable logic, configuration-bearing image or other updateable realization is material to system lifecycle, the project **SHALL** define the applicable update transaction authority/responsibility, transaction scope, authoritative update result and affected participants/resources.

### `SCAF-LIFE-013` — Bootstrap / active-realization lifecycle responsibility boundary

**Target:** Project-Applicable Obligation

Where bootstrap, staging, recovery, update-management or equivalent lifecycle responsibilities are distinct from the realization that provides normal active Service, the project **SHALL** define the controlled lifecycle responsibility boundary, authority handoff and conditions under which the active realization becomes lifecycle-eligible for subsequent RUN readiness evaluation.

This obligation does not require a dedicated bootloader, recovery partition, updater component or separate executable image.

### `SCAF-LIFE-014` — Update preconditions and controlled source inputs

**Target:** Project-Applicable Obligation

For each material update transaction, the project **SHALL** define the controlled preconditions that must be satisfied before the transaction may proceed and trace those preconditions to applicable `SCAF-INT`, `SCAF-TIME`, `SCAF-CFG`, `SCAF-SEC`, `SCAF-RUN`, `SCAF-ROB` or external-authority decisions as applicable.

LIFE **SHALL NOT** redefine the source semantics of compatibility, security authorization, configuration authority, timing constraint, operational-state condition or resilience condition merely because the condition gates an update.

### `SCAF-LIFE-015` — Update transaction atomicity / commit / abort

**Target:** Project-Applicable Obligation

Where partial application of an update or lifecycle change can create a materially inconsistent or unusable system condition, the project **SHALL** define the required transaction atomicity/consistency property, the controlled commit/completion point, the abort/interruption semantics and the authoritative resulting lifecycle state/result.

### `SCAF-LIFE-016` — Activation semantics

**Target:** Project-Applicable Obligation

Where an updated, replaced or newly prepared realization requires a distinct activation decision, the project **SHALL** define the controlled activation criteria, authoritative activation result and relationship between transaction completion and active/use-eligible lifecycle state.

**Boundary note (informative):** A ROB-controlled health/failure determination may be a controlled activation input; `SCAF-ROB` does not thereby become lifecycle activation authority.

### `SCAF-LIFE-017` — Rollback semantics

**Target:** Project-Applicable Obligation

Where rollback is Applicable, the project **SHALL** define rollback eligibility, the lifecycle transaction/result semantics of rollback, the authoritative rollback completion/failure criteria and the controlled consequence when rollback cannot establish the required lifecycle result.

This obligation does not prescribe image slots, copy direction, rollback algorithm or storage layout.

### `SCAF-LIFE-018` — Interrupted transaction / resume semantics

**Target:** Project-Applicable Obligation

Where a lifecycle transaction may be interrupted by reset, power loss, communication loss, participant loss or another controlled condition and later resumed or restarted, the project **SHALL** define whether resume/restart is permitted, the authoritative continuation basis, consistency/eligibility criteria and the required result when continuation cannot be safely or correctly established.

### `SCAF-LIFE-019` — Multi-participant lifecycle coordination

**Target:** Project-Applicable Obligation

Where a lifecycle transaction spans multiple participants, Nodes, domains or updateable responsibilities, the project **SHALL** define the required coordination relationship, authoritative transaction/result responsibility, permitted partial-progress condition and required consistency before the coordinated lifecycle transaction is considered complete.

This obligation does not prescribe a consensus protocol, coordinator algorithm, leader election, two-phase commit implementation or transport.

### `SCAF-LIFE-020` — Lifecycle failure handoff to ROB

**Target:** Project-Applicable Obligation

Where a LIFE-controlled lifecycle result represents failed, incomplete, interrupted, inconsistent or otherwise unusable lifecycle outcome that is robustness-significant, the project **SHALL** trace that controlled LIFE result/condition to the applicable `SCAF-ROB` health/failure/resilience decision without redefining the ROB response inside the LIFE transaction model.

### `SCAF-LIFE-021` — Lifecycle observability requirement

**Target:** Project-Applicable Obligation

For each material lifecycle transaction/result whose correct operation, recovery, correlation or verification depends on observation, the project **SHALL** identify the lifecycle condition/result/identity that must be observable and trace that observation requirement to the applicable LIFE/source decision.

**Boundary note (informative):** `SCAF-OBS` defines observation, representation, provenance/correlation, preservation and export semantics; Project Realization implements the observation mechanism.

### `SCAF-LIFE-022` — Lifecycle traceability

**Target:** Project-Applicable Obligation

Each material LIFE decision **SHALL** trace to its motivating controlled `SCAF-CTX`, `SCAF-ARCH`, `SCAF-INT`, `SCAF-TIME`, `SCAF-RUN`, `SCAF-ROB`, `SCAF-CFG`, `SCAF-SEC`, external-authority or other applicable source obligation/decision.

### `SCAF-LIFE-023` — Lifecycle change and re-evaluation

**Target:** Project-Applicable Obligation

A material change to lifecycle transaction/state semantics, boot/reset/power/update structure, activation/rollback criteria, Boot Incarnation semantics, retained-state validity, coordination assumptions, update preconditions or source-authority constraints **SHALL** trigger re-evaluation of affected LIFE obligations and dependent RUN/ROB/INT/TIME/CFG/OBS/SEC/external-authority decisions as applicable.

## 4. Framework Normative Invariants

### `SCAF-LIFE-024` — LIFE / RUN lifecycle-handoff boundary

**Target:** Framework Normative Invariant

`SCAF-LIFE` **Defines Framework Semantics / Obligation** for boot/power/reset/update/activation/rollback transaction and lifecycle-state/result semantics and Boot Incarnation / Boot Generation.

`SCAF-RUN` **Defines Framework Semantics / Obligation** for operational/service state, readiness/availability, operational transitions and Operational Incarnation. LIFE **SHALL NOT** redefine RUN readiness/current-state semantics merely because a lifecycle result triggers or constrains a RUN transition.

### `SCAF-LIFE-025` — LIFE / ROB lifecycle-failure boundary

**Target:** Framework Normative Invariant

`SCAF-LIFE` **Defines Framework Semantics / Obligation** for lifecycle transaction/state/result, sequencing/coordination, atomicity, activation/rollback and Boot Incarnation semantics.

`SCAF-ROB` **Defines Framework Semantics / Obligation** for fault/error/failure interpretation, health determination and resilience response when a lifecycle operation fails. ROB **SHALL NOT** define the LIFE transaction/state model, and LIFE **SHALL NOT** absorb ROB failure-response authority.

### `SCAF-LIFE-026` — LIFE / TIME measurable-property boundary

**Target:** Framework Normative Invariant

`SCAF-TIME` **Defines Framework Semantics / Obligation** for measurable lifecycle-related timebase, deadline, duration, synchronization, capacity/resource, threshold, horizon and uncertainty properties.

`SCAF-LIFE` **Defines Framework Semantics / Obligation** for lifecycle transaction/state/result semantics that use those controlled properties. LIFE **SHALL NOT** become source authority for the underlying TIME project value merely because a temporal condition gates a lifecycle transition.

### `SCAF-LIFE-027` — LIFE / INT request, compatibility and session boundary

**Target:** Framework Normative Invariant

`SCAF-INT` **Defines Framework Semantics / Obligation** for lifecycle-related Interface/Interaction request/response contract, data validity, semantic ordering, compatibility/evolution and Protocol/Connection Session Identity.

`SCAF-LIFE` **Defines Framework Semantics / Obligation** for the lifecycle transaction/state/result driven or constrained by those controlled inputs. LIFE **SHALL NOT** redefine INT contract/session semantics as lifecycle semantics.

### `SCAF-LIFE-028` — LIFE / CFG persistent-state boundary

**Target:** Framework Normative Invariant

`SCAF-CFG` **Defines Framework Semantics / Obligation** for controlled configuration/persistent operational-state ownership, authority, defaults, validation, version/migration, commit/rollback/corruption-recovery and persistence semantics.

`SCAF-LIFE` **Defines Framework Semantics / Obligation** for lifecycle transition/transaction conditions, lifecycle activation/rollback and retained-state validity context that consume those controlled CFG decisions. `SCAF-CFG` retains configuration/persistent-state commit/rollback/migration semantics; `SCAF-LIFE` retains boot/update lifecycle activation/rollback transaction semantics. Neither concern **SHALL** take over the other's source authority merely because one project transaction coordinates both.

### `SCAF-LIFE-029` — LIFE / OBS evidence-survivability boundary

**Target:** Framework Normative Invariant

`SCAF-LIFE` **Defines Framework Semantics / Obligation** for lifecycle transition/result/identity semantics that may affect evidence availability or correlation.

`SCAF-OBS` **Defines Framework Semantics / Obligation** for evidence observation, identity/provenance, correlation, preservation/survivability and export. LIFE **SHALL NOT** prescribe an evidence recorder/storage format merely because evidence must survive or correlate across lifecycle transitions.

### `SCAF-LIFE-030` — Boot / operational / session / time identity partition

**Target:** Framework Normative Invariant

Boot Incarnation / Boot Generation belongs to `SCAF-LIFE`; Operational Incarnation / Operational State Generation belongs to `SCAF-RUN`; Protocol / Connection Session Identity belongs to `SCAF-INT`; Time Epoch / Time Domain belongs to `SCAF-TIME`.

No identity **SHALL** be inferred to be semantically identical to another merely because a project event commonly changes more than one identity. `SCAF-OBS` may record/correlate all applicable identities without redefining them.

### `SCAF-LIFE-031` — LIFE / ARCH structural-boundary boundary

**Target:** Framework Normative Invariant

`SCAF-ARCH` **Defines Framework Semantics / Obligation** for structural allocation, Node/Domain boundaries, topology and shared-resource structure; the Project Design Authority defines the actual project structure.

`SCAF-LIFE` **Defines Framework Semantics / Obligation** for lifecycle transaction/coordination behavior using those controlled structural decisions. LIFE **SHALL NOT** redefine topology or structural Domain boundaries merely to express lifecycle sequencing/coordination.

### `SCAF-LIFE-032` — External safety / security / risk authority boundary

**Target:** Framework Normative Invariant

SCAF does not independently invent a universal safety-significant lifecycle state, update authorization policy, security objective or risk-acceptance basis.

Applicable safety/hazard, security, regulatory and risk authorities remain source authorities for their controlled objectives, constraints and acceptance decisions. The Project Design Authority integrates those controlled inputs into actual LIFE decisions. `SCAF-LIFE` **SHALL NOT** convert constraint specificity into LIFE/PDA ownership of the external source authority.

### `SCAF-LIFE-033` — LIFE / PROF / Project Realization mechanism boundary

**Target:** Framework Normative Invariant

`SCAF-LIFE` **Defines Framework Semantics / Obligation** for lifecycle transaction/state/result and required project decisions, not the realization mechanism.

`SCAF-LIFE` **SHALL NOT** require a specific bootloader, A/B partition layout, image format, flash-copy algorithm, reset-register sequence, watchdog, update protocol, power-sequencing circuit, updater service, journaling/checkpoint mechanism or scheduler as a universal L1/L2 rule. `SCAF-PROF` may **Guide Realization** and **Constrain** applicable realization choices where an implementation profile is later Applicable, and Project Realization implements the controlled project decision.

## 5. Required Project Decisions / Records

The following table is informative and does not create additional normative requirements.

| Decision / record | Project-side authority / provenance |
|---|---|
| Material LIFE concern inventory | Project Design Authority / applicable requirement or external authority |
| Lifecycle transaction/state model and authoritative result responsibility | Project Design Authority |
| Request/acceptance/completion/activation/result semantics | Project Design Authority, constrained by INT/SEC/CFG inputs as applicable |
| LIFE-to-RUN readiness handoff | Project Design Authority under LIFE and RUN obligations |
| Boot Incarnation / Boot Generation semantics | Project Design Authority under LIFE obligations |
| Reset classification/cause and reset-domain consequence | Project Design Authority, constrained by platform/external requirements as applicable |
| Retained-state validity after lifecycle transition | Project Design Authority, using controlled CFG/OBS/INT/RUN decisions as applicable |
| Power lifecycle / brownout-relevant outcome | Project Design Authority |
| Update transaction scope/authority/preconditions | Project Design Authority, using controlled INT/TIME/CFG/SEC/RUN/ROB inputs |
| Atomicity / commit / abort / activation / rollback / resume semantics | Project Design Authority |
| Multi-participant lifecycle coordination | Project Design Authority, using controlled ARCH/INT/TIME inputs |
| LIFE failure -> ROB handoff | Project Design Authority under LIFE/ROB obligations |
| LIFE observability requirement | Project Design Authority, realized through applicable OBS decisions |

`SCAF-APP` may Disposition / Trace these decisions but does not own them.

## 6. Concern Boundaries

- `SCAF-CTX` **Defines Framework Semantics / Obligation** for Function/Service context/consequence that lifecycle operations must preserve or restore.
- `SCAF-ARCH` **Defines Framework Semantics / Obligation** for structural/Domain/topology decisions used by lifecycle coordination.
- `SCAF-INT` **Defines Framework Semantics / Obligation** for lifecycle request/response, compatibility and session contract semantics.
- `SCAF-TIME` **Defines Framework Semantics / Obligation** for measurable lifecycle timing/synchronization/capacity/resource properties.
- `SCAF-RUN` **Defines Framework Semantics / Obligation** for operational readiness/state/transition semantics after LIFE handoff.
- `SCAF-ROB` **Defines Framework Semantics / Obligation** for failure/health/resilience response when LIFE-controlled operations fail.
- `SCAF-LIFE` **Defines Framework Semantics / Obligation** for boot/power/reset/update/activation/rollback lifecycle transaction/state/result semantics and Boot Incarnation.
- `SCAF-CFG` **Defines Framework Semantics / Obligation** for configuration/persistent-state source/ownership/version/migration/persistence semantics.
- `SCAF-OBS` **Defines Framework Semantics / Obligation** for lifecycle evidence observation/provenance/correlation/preservation/export.
- `SCAF-SEC` **Defines Framework Semantics / Obligation** for the SCAF security architecture interface/robustness boundary and consumes applicable security-authority objectives/constraints; it does not replace external security risk authority.
- `SCAF-ASSUR` **Defines Framework Semantics / Obligation** for verification/evidence-sufficiency semantics; Project Verification / Assurance Authority **Verifies** LIFE obligations against the Applicable Satisfaction Basis.
- `SCAF-PROF` may **Guide Realization** and **Constrain** applicable realization choices; Project Realization implements the selected lifecycle mechanism.

## 7. Non-Normative Example

A multi-participant product may receive an update request over an INT-controlled management Interface. LIFE requires the project to distinguish the request from transaction acceptance, completion, activation and resulting Boot Incarnation; TIME supplies any measurable timeout/deadline; CFG supplies controlled version/persistent-state semantics; ROB defines required resilience response if the update or rollback fails; RUN evaluates operational readiness after the lifecycle handoff; OBS records/correlates lifecycle evidence. Whether the realization uses an A/B image layout, bootloader flags, a particular flash algorithm, a daemon or a hardware reset sequence is outside L1/L2 LIFE normative scope.
