# SCAF-OBS — Observability, Diagnostics & Incident Evidence Obligations

**Release:** v0.0.2rc11  
**Concern:** `SCAF-OBS`  
**Layer:** L1 Concern Authority + L2 Required Project Decisions  
**Status:** Normative RC

## 1. Purpose

`SCAF-OBS` **Defines Framework Semantics / Obligation** for observation, diagnostic and incident-evidence meaning; evidence identity/provenance; time/identity correlation; evidence quality/availability representation; preservation/survivability/accessibility/export; observer/recorder self-health; and observer-effect constraints without prescribing a log format, recorder API, ring buffer, retained-RAM layout, persistent-storage technology, telemetry protocol, crash-recorder mechanism, database or other realization mechanism.

The **Project Design Authority Defines Project Instance / Decision** for the actual project observation scope, evidence classes, evidence identity/provenance rules, correlation basis, survivability/retention/accessibility requirements, observer responsibilities and project-specific observation values, constrained by applicable source concerns and external safety/security/regulatory/risk authority inputs.

`SCAF-OBS` observes and preserves source-defined facts. It does not become source authority for `SCAF-RUN` operational state, `SCAF-ROB` fault/health/resilience meaning, `SCAF-LIFE` lifecycle result or Boot Incarnation, `SCAF-INT` contract/session semantics, `SCAF-TIME` timebase/epoch/uncertainty semantics, `SCAF-CFG` configuration/persistent-operational-state source authority, or `SCAF-ASSUR` evidence-sufficiency semantics.

## 2. L1 Authority Boundary

`SCAF-OBS` **Defines Framework Semantics / Obligation** for:

- three observability levels where materially useful: operational observability, diagnostics and incident evidence;
- observation/evidence purpose, identity and provenance;
- representation of observed fact, observation status, evidence quality/completeness/missingness and source uncertainty without redefining the source fact;
- observed time provenance, local chronological evidence ordering and cross-participant correlation using controlled `SCAF-TIME` semantics;
- recording/correlation of Boot Incarnation, Operational Incarnation, Protocol/Connection Session Identity and Time Epoch / Time Domain as defined by their source concerns;
- first-abnormal-state/effect versus later/terminal failure/crash evidence distinction where material;
- diagnostic and incident-evidence scope, timeline/correlation requirements and causal-claim basis without converting correlation into root-cause authority;
- evidence preservation, lifecycle survivability, accessibility, retrieval/export and copy/export provenance;
- observer/recorder self-health, loss-of-observation semantics and low-coupling/observer-effect obligations;
- early-boot/crash-loop evidence needs where Applicable without prescribing a salvage/storage mechanism;
- persistent incident/diagnostic evidence distinction from `SCAF-CFG` persistent configuration/operational state;
- observation/evidence traceability and change/re-evaluation obligations.

The **Project Design Authority Defines Project Instance / Decision** for actual observation/evidence classes, observation responsibilities, evidence identities, provenance fields/concepts, correlation rules, survivability/retention/access criteria and project-specific observation values. `SCAF-OBS` does not define a universal logging schema, universal fault code, universal recorder architecture, universal retention duration or universal evidence-sufficiency threshold.

## 3. Project-Applicable Obligations

### `SCAF-OBS-001` — Material observability / evidence concern identification

**Target:** Project-Applicable Obligation

The project **SHALL** identify each observation, diagnostic or incident-evidence concern whose omission, ambiguity, loss, corruption, mis-correlation or observer effect can materially affect an applicable Function, Capability, Service, Interaction, architecture decision, operational/lifecycle/resilience decision, investigation, verification obligation or external safety/security/regulatory/risk constraint.

### `SCAF-OBS-002` — Observation purpose and evidence class

**Target:** Project-Applicable Obligation

For each material OBS concern, the project **SHALL** define the observation/evidence purpose and applicable class sufficiently to distinguish routine operational observability, diagnostic evidence and incident/postmortem evidence where those uses have materially different identity, preservation, accessibility, correlation or verification consequences.

The project need not use these exact labels when another controlled classification preserves equivalent semantics.

### `SCAF-OBS-003` — Observed-fact source-authority trace

**Target:** Project-Applicable Obligation

For each material observed fact, state, condition, identity, decision or result, the project **SHALL** trace the evidence representation to the controlled source concern/project authority that defines the underlying meaning. Observation **SHALL NOT** by itself establish a new authoritative source fact.

### `SCAF-OBS-004` — Evidence item identity

**Target:** Project-Applicable Obligation

Where evidence can be confused, duplicated, replaced, merged, exported or correlated across time/participants/lifecycle instances, the project **SHALL** define evidence-item identity semantics sufficient to distinguish the relevant evidence records/items without redefining the identities of the source facts being observed.

### `SCAF-OBS-005` — Evidence provenance

**Target:** Project-Applicable Obligation

For each material evidence class, the project **SHALL** define the provenance needed to interpret the evidence, including the producing/observing responsibility, applicable source object/condition, observation context and other project-defined provenance required to distinguish source fact from observer representation.

### `SCAF-OBS-006` — Observation time provenance / uncertainty

**Target:** Project-Applicable Obligation

Where evidence interpretation depends on time, age, chronology or synchronization quality, the project **SHALL** record or otherwise associate the controlled time provenance required to interpret the observation, including applicable timebase/clock identity, Time Epoch/Time Domain and uncertainty/synchronization quality defined by `SCAF-TIME`.

**Boundary note (informative):** replacement-timebase prohibition is governed normatively by `SCAF-OBS-033`.

### `SCAF-OBS-007` — Local evidence chronological ordering

**Target:** Project-Applicable Obligation

Where local evidence chronology is material, the project **SHALL** define the basis by which observations can be chronologically related, including the controlled TIME source and the project consequence when ordering is unknown, ambiguous or not trustworthy.

Semantic/causal ordering defined by `SCAF-INT`, `SCAF-RUN`, `SCAF-LIFE` or another source concern **SHALL NOT** be inferred solely from local timestamp order.

### `SCAF-OBS-008` — Cross-participant evidence correlation

**Target:** Project-Applicable Obligation

Where observations from multiple participants, Nodes, Domains or evidence sources must be correlated, the project **SHALL** define the controlled correlation basis, source identities/time provenance used, permitted correlation uncertainty/ambiguity and the consequence when a reliable correlation cannot be established.

### `SCAF-OBS-009` — Causal-correlation claim basis

**Target:** Project-Applicable Obligation

Where evidence is used to support a causal or other derived-inference claim, the project **SHALL** define the controlled basis and evidence limitations for that claim and distinguish direct observation, derived inference and unresolved ambiguity.

Correlation, timestamp proximity or recorder order **SHALL NOT** by itself establish root cause, failure classification or source-authority semantics.

### `SCAF-OBS-010` — Evidence quality / completeness / missingness representation

**Target:** Project-Applicable Obligation

For each material evidence class, the project **SHALL** define the evidence-quality information needed to interpret availability, completeness, truncation, corruption, uncertainty, dropped/missing observation, indeterminate provenance or other evidence limitations that can materially affect use of the evidence.

This obligation defines evidence representation/quality semantics; it does not determine `SCAF-ASSUR` evidence sufficiency.

### `SCAF-OBS-011` — Observer / recorder self-health

**Target:** Project-Applicable Obligation

Where a monitor, observer, recorder, logger, diagnostic responsibility or evidence path can materially affect confidence in observation/evidence, the project **SHALL** define the required self-health/availability indication or controlled limitation semantics and the project consequence when the observation responsibility is unavailable, unhealthy or indeterminate.

This obligation does not require a dedicated recorder/monitor component.

### `SCAF-OBS-012` — Loss-of-observation semantics

**Target:** Project-Applicable Obligation

Where loss, interruption, overflow, corruption or unavailability of observation/evidence can materially affect operation, diagnosis, investigation or verification, the project **SHALL** define the observable/evidence consequence, including how unavailable or missing evidence is represented and traced to applicable ROB/RUN/LIFE/ASSUR decisions without treating absence of evidence as proof of absence of the source condition.

### `SCAF-OBS-013` — Observer effect / low-coupling obligation

**Target:** Project-Applicable Obligation

Where observation can materially perturb a controlled system property, the project **SHALL** identify the affected property and define the required observer-effect constraint or margin using the applicable source concern. Measurable time/capacity/resource limits remain controlled by `SCAF-TIME`; resilience consequence remains controlled by `SCAF-ROB` where Applicable.

**Boundary note (informative):** L1/L2 OBS does not prescribe the realization mechanism used to achieve low coupling; the normative mechanism boundary is defined by `SCAF-OBS-040`.

### `SCAF-OBS-014` — Operational observability requirement

**Target:** Project-Applicable Obligation

Where routine operation, supervision, support or verification depends on status/metric/counter/service-state visibility, the project **SHALL** define the required operational observations, their source-authority trace and the project consequence when the required observation is unavailable or ambiguous.

### `SCAF-OBS-015` — Diagnostic evidence requirement

**Target:** Project-Applicable Obligation

Where diagnosis depends on fault indications, invariant violations, health/service data, diagnostic decisions or related observations, the project **SHALL** define the diagnostic evidence needed to distinguish the applicable hypotheses/conditions and trace the evidence to the `SCAF-ROB` or other source semantics that define the underlying condition.

Diagnostic evidence **SHALL NOT** become the health/failure determination merely because it contributes to that determination.

### `SCAF-OBS-016` — Incident evidence: first abnormal versus later/terminal condition

**Target:** Project-Applicable Obligation

Where incident investigation requires distinction between a first-observed abnormal condition/effect and later propagation, terminal failure, crash/reset or recovery outcome, the project **SHALL** define the evidence needed to preserve that distinction and the controlled limitation when the distinction cannot be established. Where an initiating condition is separately claimed, that claim **SHALL** use the controlled causal/inference basis required by `SCAF-OBS-009`.

### `SCAF-OBS-017` — Incident evidence scope / timeline

**Target:** Project-Applicable Obligation

Where reconstruction of a material incident depends on a sequence of observations, the project **SHALL** define the required evidence scope/timeline relationship, participating evidence sources and correlation basis sufficiently to reconstruct the material sequence within project-defined uncertainty/coverage limits.

This obligation does not prescribe a pre-trigger/post-trigger buffer, ring buffer or storage layout.

### `SCAF-OBS-018` — Evidence preservation / lifecycle survivability

**Target:** Project-Applicable Obligation

Where evidence must remain available across a reset, boot, power transition, update, rollback, activation or other lifecycle transition, the project **SHALL** define the required evidence survivability/correlation outcome and trace it to the controlled `SCAF-LIFE` transaction/result/identity semantics that can affect evidence availability.

**Boundary note (informative):** the normative OBS/LIFE authority partition is defined by `SCAF-OBS-031`.

### `SCAF-OBS-019` — Early-boot / crash-loop evidence

**Target:** Project-Applicable Obligation

Where early-boot failure, repeated reset/crash-loop behavior or pre-operational failure can materially defeat normal evidence collection, the project **SHALL** define the evidence that must remain observable/recoverable, the applicable Boot Incarnation/correlation basis and the controlled consequence when such evidence cannot be obtained.

This obligation does not prescribe retained RAM, flash logging, crash recorder, bootloader storage or another salvage mechanism.

### `SCAF-OBS-020` — Source-defined identity recording

**Target:** Project-Applicable Obligation

Where evidence interpretation depends on lifecycle, operational, interaction/session or temporal incarnation, the project **SHALL** record or otherwise associate the applicable source-defined Boot Incarnation / Boot Generation, Operational Incarnation / Operational State Generation, Protocol / Connection Session Identity and Time Epoch / Time Domain needed for unambiguous interpretation.

The project **SHALL** preserve source provenance and shall not synthesize an OBS-owned replacement identity when a source identity is missing or unknown.

### `SCAF-OBS-021` — Evidence retention / accessibility / expiration

**Target:** Project-Applicable Obligation

For each evidence class whose future availability is material, the project **SHALL** define the required retention horizon/condition, accessibility and controlled expiration/loss consequence, traced to applicable project/external requirements. Lifecycle-crossing evidence preservation/survivability is governed by `SCAF-OBS-018`. Any measurable retention duration/capacity is a project value governed by applicable TIME/resource decisions rather than a universal OBS value.

### `SCAF-OBS-022` — Evidence retrieval / export semantics

**Target:** Project-Applicable Obligation

Where evidence must be retrieved or exported, the project **SHALL** define the required evidence identity/provenance/correlation information that must remain associated with the exported representation and the project consequence of partial, transformed, unavailable or ambiguous export.

**Boundary note (informative):** transport/interface contract semantics remain governed by `SCAF-INT`; security/access constraints remain governed by applicable security authority/`SCAF-SEC` interfaces.

### `SCAF-OBS-023` — Evidence copy / transformation consistency

**Target:** Project-Applicable Obligation

Where evidence is copied, transformed, aggregated, summarized or exported into another representation, the project **SHALL** define the trace/correlation needed to distinguish the derived representation from the source evidence and preserve material provenance/quality limitations.

A derived representation **SHALL NOT** silently replace the source evidence identity or become source authority for the observed fact.

### `SCAF-OBS-024` — Persistent incident/diagnostic evidence versus persistent operational/configuration state

**Target:** Project-Applicable Obligation

Where persisted information can serve both diagnostic/evidence and configuration/persistent-operational-state purposes, the project **SHALL** define the classification/source-authority boundary and project consequence sufficiently to prevent incident/diagnostic evidence semantics from becoming `SCAF-CFG` configuration/state authority or vice versa.

### `SCAF-OBS-025` — External safety / security / regulatory / risk evidence constraints

**Target:** Project-Applicable Obligation

Where external safety, security, regulatory or risk authority imposes observation, evidence, retention, accessibility, confidentiality, integrity or incident-reporting constraints, the project **SHALL** trace the OBS decision to those controlled source constraints without transferring objective/risk-acceptance authority to OBS.

### `SCAF-OBS-026` — OBS traceability

**Target:** Project-Applicable Obligation

For each material OBS decision, the project **SHALL** trace the decision to the motivating `SCAF-CTX`, `SCAF-ARCH`, `SCAF-INT`, `SCAF-TIME`, `SCAF-RUN`, `SCAF-ROB`, `SCAF-LIFE`, `SCAF-CFG`, `SCAF-SEC`, `SCAF-ASSUR` or applicable external-authority decision as appropriate.

### `SCAF-OBS-027` — OBS change and re-evaluation

**Target:** Project-Applicable Obligation

The project **SHALL** re-evaluate affected OBS and dependent project decisions when observation scope, source semantics, evidence identity/provenance, time/identity correlation, observer responsibility, survivability/retention, lifecycle behavior, robustness semantics, verification need or applicable external-authority constraint materially changes.

## 4. Framework Normative Invariants

### `SCAF-OBS-028` — Observation does not create source authority

**Target:** Framework Normative Invariant

`SCAF-OBS` **Defines Framework Semantics / Obligation** for observing, representing, preserving, correlating and exporting evidence about source-defined facts. Observation/evidence **SHALL NOT** redefine the underlying source fact, state, identity, failure meaning, lifecycle result, contract meaning, time semantics or acceptance decision merely because OBS records or derives a representation of it.

### `SCAF-OBS-029` — OBS / RUN operational-state boundary

**Target:** Framework Normative Invariant

`SCAF-RUN` **Defines Framework Semantics / Obligation** for operational-state meaning, authoritative current-state responsibility, transition/result consistency, readiness/availability and Operational Incarnation.

`SCAF-OBS` **Defines Framework Semantics / Obligation** for evidence representing/recording those source-defined states/results/identities. A displayed/logged/cached OBS representation **SHALL NOT** become authoritative RUN state.

### `SCAF-OBS-030` — OBS / ROB health-failure boundary

**Target:** Framework Normative Invariant

`SCAF-ROB` **Defines Framework Semantics / Obligation** for Fault/Error/Failure meaning, health/failure determination, detection significance, degradation/containment/recovery and required resilience outcome.

`SCAF-OBS` **Defines Framework Semantics / Obligation** for observation/evidence of indications, effects, decisions and outcomes. An observed code/event/counter/log **SHALL NOT** by itself become the ROB health/failure determination, root cause or resilience decision.

### `SCAF-OBS-031` — OBS / LIFE lifecycle boundary

**Target:** Framework Normative Invariant

`SCAF-LIFE` **Defines Framework Semantics / Obligation** for boot/reset/power/update/activation/rollback lifecycle transaction/state/result and Boot Incarnation.

`SCAF-OBS` **Defines Framework Semantics / Obligation** for lifecycle evidence, evidence survivability and correlation. Evidence presence/absence **SHALL NOT** by itself establish a LIFE transaction result.

### `SCAF-OBS-032` — OBS / INT contract and session boundary

**Target:** Framework Normative Invariant

`SCAF-INT` **Defines Framework Semantics / Obligation** for Interface/Interaction contract meaning, validity, semantic ordering, compatibility and Protocol/Connection Session Identity.

`SCAF-OBS` may record contract events/identities/effects as evidence but **SHALL NOT** redefine INT validity/order/session/compatibility semantics.

### `SCAF-OBS-033` — OBS / TIME time-provenance boundary

**Target:** Framework Normative Invariant

`SCAF-TIME` **Defines Framework Semantics / Obligation** for timebase, clock identity, synchronization, drift/offset/uncertainty, chronological ordering and Time Epoch / Time Domain.

`SCAF-OBS` records/uses those controlled time semantics for evidence chronology/correlation and **SHALL NOT** create a replacement source timebase or silently treat unknown/unsynchronized time as trustworthy chronology.

### `SCAF-OBS-034` — OBS / CFG persistence boundary

**Target:** Framework Normative Invariant

`SCAF-CFG` **Defines Framework Semantics / Obligation** for configuration and persistent operational-state authoritative-source/value semantics, defaults, validity, version/migration, commit/CFG-side rollback, corruption/loss interpretation, CFG source-state restoration/result, calibration and synchronization.

`SCAF-OBS` **Defines Framework Semantics / Obligation** for incident/diagnostic evidence identity/provenance/preservation/export. Persistent storage or shared physical media **SHALL NOT** collapse these semantic authority spaces.

### `SCAF-OBS-035` — OBS / ASSUR evidence-sufficiency boundary

**Target:** Framework Normative Invariant

`SCAF-OBS` **Defines Framework Semantics / Obligation** for runtime/diagnostic/incident evidence representation, provenance, quality/availability, preservation/correlation and export.

`SCAF-ASSUR` **Defines Framework Semantics / Obligation** for verification methods, verification-evidence properties and evidence-sufficiency criteria; the Project Verification / Assurance Authority determines actual project evidence sufficiency. OBS evidence availability/quality **SHALL NOT** be interpreted as verification sufficiency or underlying obligation closure merely because the evidence exists.

### `SCAF-OBS-036` — External safety / security / regulatory / risk authority boundary

**Target:** Framework Normative Invariant

Applicable safety/hazard, security, regulatory and risk authorities remain source authorities for their objectives, constraints and acceptance decisions. `SCAF-OBS` may define observation/evidence obligations needed to support those controlled inputs but **SHALL NOT** invent a universal Safe State, security objective, threat model, confidentiality policy or risk-acceptance basis.

### `SCAF-OBS-037` — Four-way source identity correlation boundary

**Target:** Framework Normative Invariant

Boot Incarnation / Boot Generation belongs to `SCAF-LIFE`; Operational Incarnation / Operational State Generation belongs to `SCAF-RUN`; Protocol / Connection Session Identity belongs to `SCAF-INT`; Time Epoch / Time Domain belongs to `SCAF-TIME`.

`SCAF-OBS` may record/correlate all applicable identities and may represent an identity as unknown/missing/ambiguous, but **SHALL NOT** redefine, merge or synthesize replacement source semantics for those identities.

### `SCAF-OBS-038` — OBS / ARCH structural-context boundary

**Target:** Framework Normative Invariant

`SCAF-ARCH` **Defines Framework Semantics / Obligation** for System/Node/Domain/topology/shared-resource structure and the Project Design Authority defines the actual project structure.

`SCAF-OBS` may use controlled structural identity/context to attribute/correlate evidence but **SHALL NOT** redefine structural boundaries merely to organize logs, diagnostics or evidence sources.

### `SCAF-OBS-039` — Correlation / inference / source meaning boundary

**Target:** Framework Normative Invariant

OBS correlation, chronology and derived inference may support diagnosis/verification but **SHALL NOT** become source authority for causal meaning, root cause, health/failure classification, lifecycle result, operational-state truth or external risk acceptance without a controlled source-authority decision establishing that interpretation.

### `SCAF-OBS-040` — OBS / PROF / Project Realization mechanism boundary

**Target:** Framework Normative Invariant

`SCAF-OBS` **Defines Framework Semantics / Obligation** for observation/evidence properties and required project decisions, not the realization mechanism.

`SCAF-PROF` may **Guide Realization** / **Constrain** applicable realization choices, and Project Realization implements the selected mechanism. No L1/L2 OBS requirement **SHALL** universally mandate a log schema, ring buffer, retained-RAM section, flash recorder, database, telemetry protocol, crash recorder API, storage medium, compression format or other implementation technology.

## 5. Required Project Decisions / Records

The following table is informative and does not create additional normative requirements.

| Decision / record | Project-side authority / provenance |
|---|---|
| Material OBS concern inventory and evidence class/purpose | Project Design Authority / applicable requirement or external authority |
| Observed-fact source-authority trace | Project Design Authority using controlled source concern/authority |
| Evidence identity / provenance | Project Design Authority under OBS obligations |
| Time provenance / chronological basis | Project Design Authority using controlled TIME decisions |
| Cross-participant correlation / causal-claim limitations | Project Design Authority using controlled source identities/time semantics |
| Evidence quality / missingness semantics | Project Design Authority under OBS obligations |
| Observer/recorder self-health and observer-effect constraint | Project Design Authority using controlled TIME/ROB decisions where applicable |
| Operational/diagnostic/incident evidence scope | Project Design Authority using RUN/ROB/LIFE/ASSUR/external inputs as applicable |
| Evidence survivability / retention / accessibility / export | Project Design Authority using LIFE/TIME/SEC/regulatory inputs as applicable |
| Four-way identity recording/correlation | Project Design Authority using LIFE/RUN/INT/TIME source identities |
| Persistent evidence vs CFG state/configuration boundary | Project Design Authority under OBS/CFG obligations |
| Verification evidence-sufficiency evaluation | Project Verification / Assurance Authority using SCAF-ASSUR semantics |

`SCAF-APP` **Dispositions / Traces** these decisions but does not own them.

## 6. Concern Boundaries

- `SCAF-CTX` **Defines Framework Semantics / Obligation** for Function/Service context/consequence that motivates observation/evidence need.
- `SCAF-ARCH` **Defines Framework Semantics / Obligation** for structural/Domain/topology context used to attribute/correlate evidence.
- `SCAF-INT` **Defines Framework Semantics / Obligation** for interaction contract/validity/order/session semantics observed as evidence.
- `SCAF-TIME` **Defines Framework Semantics / Obligation** for time provenance, synchronization, uncertainty, chronology and Time Epoch/Domain.
- `SCAF-RUN` **Defines Framework Semantics / Obligation** for operational-state/readiness/transition and Operational Incarnation semantics observed by OBS.
- `SCAF-ROB` **Defines Framework Semantics / Obligation** for failure/health/detection/resilience meaning observed and preserved by OBS.
- `SCAF-LIFE` **Defines Framework Semantics / Obligation** for lifecycle transaction/result/Boot Incarnation and lifecycle context affecting evidence survivability.
- `SCAF-OBS` **Defines Framework Semantics / Obligation** for observation/evidence identity/provenance/quality/correlation/preservation/accessibility/export and observer-effect/self-health semantics.
- `SCAF-CFG` **Defines Framework Semantics / Obligation** for persistent configuration/operational-state source/version/migration/rollback semantics distinct from incident/diagnostic evidence persistence.
- `SCAF-SEC` **Defines Framework Semantics / Obligation** for the SCAF security architecture interface/robustness boundary and consumes applicable security-authority objectives/constraints; OBS consumes resulting security evidence constraints without becoming security risk authority.
- `SCAF-ASSUR` **Defines Framework Semantics / Obligation** for verification/evidence-sufficiency semantics; Project Verification / Assurance Authority **Verifies** applicable obligations and determines actual evidence sufficiency.
- `SCAF-PROF` may **Guide Realization** / **Constrain** applicable observation implementations; Project Realization implements the selected mechanism.

## 7. Non-Normative Example

A multi-participant system may record a ROB-defined abnormal-condition indication, RUN operational-state transition, LIFE reset result/Boot Incarnation, INT session identity and TIME clock/epoch provenance around one incident. OBS requires the project to preserve the source identities/provenance, represent gaps/uncertainty, correlate the observations and retain/export the evidence as required. OBS does not decide that the abnormal indication was the root cause, does not redefine the RUN state or LIFE reset result, and does not decide verification evidence sufficiency. Whether the realization uses retained RAM, a ring buffer, flash, a file, a database or streamed telemetry is outside L1/L2 OBS normative scope.
