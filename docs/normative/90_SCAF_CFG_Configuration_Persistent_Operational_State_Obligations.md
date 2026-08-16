# SCAF-CFG — Configuration & Persistent Operational State Obligations

**Release:** v0.0.2rc10  
**Concern:** `SCAF-CFG`  
**Layer:** L1 Concern Authority + L2 Required Project Decisions  
**Status:** Normative RC

## 1. Purpose

`SCAF-CFG` **Defines Framework Semantics / Obligation** for configuration and persistent operational-state source semantics; configuration/persistent-state classification, identity and provenance; defaults/provisioning; validation and consumption eligibility; version and migration; commit/atomicity; persistence; configuration-side rollback/corruption recovery; calibration/parameter state; multi-participant synchronization/consistency; and activation/use relationships with other concerns without prescribing a configuration file format, database, NVM layout, schema language, validator tool, storage medium, serialization format, protocol, calibration store, registry, key-value system or other realization mechanism.

The **Project Design Authority Defines Project Instance / Decision** for the actual project configuration/persistent-state classes, source responsibilities, identities, defaults, validation criteria, versions, migration rules, commit/rollback semantics, calibration/parameter decisions, synchronization requirements and project-specific values, constrained by applicable source concerns and external safety/security/regulatory/risk authority inputs.

`SCAF-CFG` defines configuration/persistent-operational-state source semantics. It does not become source authority for `SCAF-RUN` current operational state, `SCAF-LIFE` boot/reset/power/update transaction results, `SCAF-OBS` evidence identity/provenance/preservation, `SCAF-INT` exchange/session semantics, `SCAF-TIME` measurable timing/capacity properties, `SCAF-ROB` health/failure/resilience meaning, or external security/safety/risk acceptance.

## 2. L1 Authority Boundary

`SCAF-CFG` **Defines Framework Semantics / Obligation** for:

- configuration and persistent operational-state applicability/classification;
- authoritative configuration/persistent-state source responsibility and controlled source representation;
- configuration-item / persistent-state identity and provenance;
- defaults, provisioning, initialization and uninitialized/unknown-state semantics;
- validation and project-defined consumption eligibility;
- version identity, compatibility/migration and migration-result semantics;
- atomic configuration/persistent-state commit and authoritative resulting state;
- persistence requirements and controlled configuration-side rollback/corruption recovery;
- calibration/parameter source state and derived-parameter provenance where Applicable;
- precedence/conflict semantics where multiple controlled sources can propose values;
- cross-participant synchronization/consistency semantics for configuration/persistent state;
- relationships to LIFE activation/update, RUN live operational state, INT exchange, TIME measurable properties, ROB failure response, OBS evidence and external-authority constraints;
- traceability and change/re-evaluation obligations.

The **Project Design Authority Defines Project Instance / Decision** for actual configuration classes, source responsibility, selected values, defaults, validity criteria, versions, migration/commit/rollback rules, calibration semantics, synchronization criteria and project-specific configuration parameters. `SCAF-CFG` does not define a universal configuration schema, file type, NVM record format, migration engine, database, calibration representation or persistence technology.

## 3. Project-Applicable Obligations

### `SCAF-CFG-001` — Material configuration / persistent-state concern identification

**Target:** Project-Applicable Obligation

The project **SHALL** identify each configuration or persistent operational-state concern whose omission, ambiguity, invalidity, staleness, corruption, version mismatch, migration failure, inconsistent replication, loss or unauthorized/uncontrolled substitution can materially affect an applicable Function, Capability, Service, Interaction, architecture decision, operational/lifecycle/resilience decision, verification obligation or external safety/security/regulatory/risk constraint.

### `SCAF-CFG-002` — Configuration / persistent-state semantic classification

**Target:** Project-Applicable Obligation

For each material CFG concern, the project **SHALL** classify the controlled information sufficiently to distinguish configuration, calibration/parameter state, persistent operational state, volatile/current operational state, lifecycle state and diagnostic/incident evidence where those uses have materially different source, validity, version, persistence, rollback, migration, verification or closure consequences.

Physical co-location or identical bytes **SHALL NOT** by itself establish identical semantic authority.

### `SCAF-CFG-003` — Authoritative configuration / persistent-state source responsibility

**Target:** Project-Applicable Obligation

For each material CFG class, the Project Design Authority **SHALL** define the project source model and assign the project responsibility that determines and maintains the authoritative configuration or persistent-state value/version/result used by the project.

A file, NVM location, message, cache, UI representation, OBS evidence record or derived copy **SHALL NOT** become the authoritative source responsibility merely because it carries or stores the value.

### `SCAF-CFG-004` — Configuration item identity and provenance

**Target:** Project-Applicable Obligation

Where configuration or persistent-state items can be confused, replaced, migrated, replicated, copied, provisioned or correlated across lifecycle instances/participants, the project **SHALL** define the item identity and source provenance needed to distinguish the controlled source/value/version without redefining OBS evidence-item identity or another source concern identity.

### `SCAF-CFG-005` — Defaults / provisioning / initialization

**Target:** Project-Applicable Obligation

Where a material CFG item can be absent, unprovisioned, newly created, reset to default or initialized from another controlled source, the project **SHALL** define the applicable default/provisioning/initialization semantics, source authority, eligibility criteria and project consequence when the required controlled value cannot be established.

### `SCAF-CFG-006` — Configuration validity criteria

**Target:** Project-Applicable Obligation

For each material CFG item, the project **SHALL** define the controlled validity criteria needed before the item may be treated as valid for its intended configuration/persistent-state purpose, including applicable value/range/relational/version/provenance constraints and the project consequence when validity is false, unknown or cannot be established.

This obligation defines semantic validation criteria; it does not require a schema language or validator implementation.

### `SCAF-CFG-007` — Unknown / uninitialized / indeterminate state semantics

**Target:** Project-Applicable Obligation

Where absence, initialization status, unknown value, conflicting source, incomplete migration or indeterminate persistent-state status can materially affect behavior, the project **SHALL** define the controlled representation/decision semantics and the consequence of consuming or refusing that state.

### `SCAF-CFG-008` — Version identity and controlled compatibility basis

**Target:** Project-Applicable Obligation

Where configuration/persistent-state interpretation depends on version, the project **SHALL** define the controlled version identity and compatibility basis sufficient to determine which consumer/realization/lifecycle context may interpret or consume the item.

**Boundary note (informative):** Interface/Interaction compatibility semantics for exchanged versions remain governed normatively by `SCAF-INT`.

### `SCAF-CFG-009` — Migration applicability and resulting configuration state

**Target:** Project-Applicable Obligation

Where a material CFG item may require migration across versions, realizations, lifecycle transitions or project revisions, the project **SHALL** define migration applicability, source/target semantic basis, preconditions, completion/failure criteria, resulting authoritative configuration/persistent-state result and the consequence when migration cannot be established.

### `SCAF-CFG-010` — Atomic configuration / persistent-state commit

**Target:** Project-Applicable Obligation

Where partial or interrupted change could create a materially inconsistent, ambiguous or unusable configuration/persistent-state result, the project **SHALL** define the required atomicity/consistency property, commit point/result, incomplete/abort semantics and authoritative resulting state.

This obligation does not prescribe journaling, dual-copy, transactional storage, file-replace, database or another commit mechanism.

### `SCAF-CFG-011` — Configuration activation / application semantics

**Target:** Project-Applicable Obligation

Where a committed/configured value is not automatically active for a consumer or realization, the project **SHALL** define the controlled activation/application eligibility and resulting configuration state, including the relation to applicable `SCAF-LIFE` lifecycle transaction/result and `SCAF-RUN` operational-state decisions.

The project **SHALL NOT** treat CFG activation/application alone as proof of RUN readiness/availability or of a LIFE transaction result unless the applicable controlled RUN/LIFE decisions explicitly establish that relationship.

### `SCAF-CFG-012` — Configuration-side rollback semantics

**Target:** Project-Applicable Obligation

Where configuration or persistent-state rollback is Applicable, the project **SHALL** define rollback eligibility, source/target version/value semantics, completion/failure criteria, authoritative resulting CFG state and the project consequence when rollback cannot establish the required configuration state.

**Boundary note (informative):** configuration/persistent-state rollback and `SCAF-LIFE` lifecycle update/activation rollback remain separate framework authority spaces under `SCAF-CFG-028`, even when one project operation coordinates both.

### `SCAF-CFG-013` — Corruption / loss / unavailable persistent-state semantics

**Target:** Project-Applicable Obligation

Where corruption, loss, incomplete commit, unavailable storage/source, inconsistent replica or unreadable persistent state can materially affect behavior, the project **SHALL** define the CFG validity/result interpretation and required project treatment, traced to `SCAF-ROB` where the condition is robustness-significant.

### `SCAF-CFG-014` — Persistent operational-state semantics

**Target:** Project-Applicable Obligation

Where operational information intentionally persists beyond the lifetime of the current RUN operational instance, the project **SHALL** define what persistent operational state means, its authoritative source, validity/version semantics, lifecycle consumption eligibility and the controlled relation to current `SCAF-RUN` operational state.

The project **SHALL NOT** treat persisted operational information as authoritative current RUN state merely because it survives restart/reset/lifecycle transitions; authoritative current-state evaluation remains governed by the applicable RUN decision.

### `SCAF-CFG-015` — Calibration / parameter-state authority

**Target:** Project-Applicable Obligation

Where calibration or parameter state materially affects system behavior, the project **SHALL** define the authoritative parameter/calibration source, item identity/provenance, validity, version/applicability and change/activation semantics, including applicable external authority or controlled measurement provenance where required.

### `SCAF-CFG-016` — Derived configuration / parameter provenance

**Target:** Project-Applicable Obligation

Where a material CFG value is derived, transformed, merged or calculated from other controlled values, the project **SHALL** define the source trace and derivation basis needed to distinguish the derived authoritative CFG value from its source inputs and from OBS evidence representations of the derivation.

### `SCAF-CFG-017` — Multiple-source precedence / conflict semantics

**Target:** Project-Applicable Obligation

Where multiple controlled sources can propose, provision, restore, override or derive a material CFG value, the project **SHALL** define the source-precedence/conflict-resolution decision basis, the responsibility that establishes the authoritative resulting value and the consequence when a controlled result cannot be established.

### `SCAF-CFG-018` — Cross-participant configuration synchronization / consistency

**Target:** Project-Applicable Obligation

Where multiple participants, Nodes, Domains or realizations depend on a common or related configuration/persistent-state decision, the project **SHALL** define the required consistency/synchronization relationship, authoritative source/result responsibility, permitted disagreement/staleness and the consequence when required consistency cannot be established.

Any measurable synchronization age, deadline, rate, capacity or uncertainty remains a project value governed by applicable `SCAF-TIME` decisions.

### `SCAF-CFG-019` — Partition / reconnect / stale-replica configuration consequence

**Target:** Project-Applicable Obligation

Where communication partition, reconnect, delayed delivery or unavailable peer/source can leave a material CFG replica/value stale or divergent, the project **SHALL** define the configuration-consistency consequence and controlled reconciliation/eligibility decision, using `SCAF-INT` contract/session semantics and `SCAF-ROB` resilience semantics as applicable.

### `SCAF-CFG-020` — Configuration import / export / exchange source trace

**Target:** Project-Applicable Obligation

Where configuration/persistent state is imported, exported, provisioned or exchanged through an Interface/Interaction, the project **SHALL** define the source identity/version/provenance and resulting CFG decision needed to prevent transport representation or OBS export evidence from becoming the configuration source merely by carrying the data.

**Boundary note (informative):** `SCAF-INT` remains the normative authority for exchange contract, validity, semantic ordering, compatibility and Session Identity; OBS remains the authority for evidence representation/provenance of the exchange.

### `SCAF-CFG-021` — LIFE lifecycle / update coordination

**Target:** Project-Applicable Obligation

Where a LIFE-controlled boot/reset/update/activation/rollback transaction consumes, migrates, commits, restores or activates a material CFG item, the project **SHALL** define the controlled CFG input/result and the handoff/mapping needed for LIFE to use that result without transferring CFG value/version/migration semantics into LIFE.

### `SCAF-CFG-022` — RUN current-state / persistent-state mapping

**Target:** Project-Applicable Obligation

Where a CFG-controlled persistent operational state influences RUN initialization, readiness, transition or current operational behavior, the project **SHALL** define the controlled mapping/eligibility and the project consequence when the persistent state is missing, stale, invalid or inconsistent.

The resulting authoritative current operational state remains governed by `SCAF-RUN`.

### `SCAF-CFG-023` — OBS evidence view of configuration facts

**Target:** Project-Applicable Obligation

Where configuration identity/value/version/validation/migration/commit/rollback or corruption-recovery results must be observed for operation, diagnosis, investigation or verification, the project **SHALL** define the OBS evidence representation/provenance/correlation need while preserving the CFG source fact and authoritative source responsibility.

### `SCAF-CFG-024` — External safety / security / regulatory / risk configuration constraints

**Target:** Project-Applicable Obligation

Where applicable safety, security, regulatory or risk authority constrains configuration values, defaults, authorization, integrity, calibration, change eligibility, migration, rollback or retention, the project **SHALL** trace the CFG decision to those controlled source constraints without transferring objective, threat/risk or acceptance authority to CFG.

### `SCAF-CFG-025` — CFG traceability

**Target:** Project-Applicable Obligation

For each material CFG decision, the project **SHALL** trace the decision to the motivating `SCAF-CTX`, `SCAF-ARCH`, `SCAF-INT`, `SCAF-TIME`, `SCAF-RUN`, `SCAF-ROB`, `SCAF-LIFE`, `SCAF-OBS`, `SCAF-SEC`, `SCAF-ASSUR` or applicable external-authority decision as appropriate.

### `SCAF-CFG-026` — CFG change and re-evaluation

**Target:** Project-Applicable Obligation

The project **SHALL** re-evaluate affected CFG and dependent project decisions when configuration/persistent-state classification, authoritative source responsibility, defaults/provisioning, validity criteria, version/migration, commit/rollback, calibration, synchronization, lifecycle activation/use, RUN mapping, OBS evidence needs or applicable external-authority constraints materially change.

## 4. Framework Normative Invariants

### `SCAF-CFG-027` — CFG / OBS semantic persistence boundary

**Target:** Framework Normative Invariant

`SCAF-CFG` **Defines Framework Semantics / Obligation** for configuration and persistent operational-state source/value/version/validation/migration/commit/rollback/calibration semantics.

`SCAF-OBS` **Defines Framework Semantics / Obligation** for diagnostic/incident evidence identity/provenance/quality/preservation/correlation/export. The same physical bytes, record or storage medium **SHALL NOT** collapse these semantic authority spaces; one persisted item may require explicitly controlled CFG and OBS views when it serves both purposes.

### `SCAF-CFG-028` — CFG / LIFE activation, migration and rollback boundary

**Target:** Framework Normative Invariant

`SCAF-LIFE` **Defines Framework Semantics / Obligation** for boot/reset/power/update/activation/rollback lifecycle transaction/state/result and Boot Incarnation.

`SCAF-CFG` **Defines Framework Semantics / Obligation** for configuration/persistent-state value/version/validation/migration/commit and CFG-side rollback semantics. LIFE may coordinate or consume CFG results, but neither lifecycle rollback nor lifecycle activation **SHALL** become the source authority for CFG value/version/migration meaning merely because both occur in one project transaction.

### `SCAF-CFG-029` — CFG / RUN persistent versus current operational-state boundary

**Target:** Framework Normative Invariant

`SCAF-RUN` **Defines Framework Semantics / Obligation** for authoritative current operational state, readiness/availability, transition/result consistency and Operational Incarnation.

`SCAF-CFG` **Defines Framework Semantics / Obligation** for persistent operational-state source/value/version semantics. Persisted or restored operational information **SHALL NOT** by itself become authoritative current RUN state without the controlled RUN mapping/evaluation defined by the project.

### `SCAF-CFG-030` — CFG / INT exchange boundary

**Target:** Framework Normative Invariant

`SCAF-INT` **Defines Framework Semantics / Obligation** for Interface/Interaction contract meaning, exchanged-data validity, semantic ordering, compatibility/evolution and Protocol/Connection Session Identity.

`SCAF-CFG` may consume configuration data transported through an Interaction but **SHALL NOT** redefine the INT contract/session semantics merely because the exchanged value becomes configuration.

### `SCAF-CFG-031` — CFG / TIME measurable-property boundary

**Target:** Framework Normative Invariant

`SCAF-TIME` **Defines Framework Semantics / Obligation** for measurable timebase, synchronization, uncertainty, latency/deadline, capacity/resource budget, horizon and margin properties.

`SCAF-CFG` **Defines Framework Semantics / Obligation** for configuration/persistent-state semantics that may use those controlled properties. CFG **SHALL NOT** create universal migration time, synchronization age, commit duration, retention/capacity or retry values.

### `SCAF-CFG-032` — CFG / ROB failure-response boundary

**Target:** Framework Normative Invariant

`SCAF-CFG` **Defines Framework Semantics / Obligation** for invalid/corrupt/missing/inconsistent configuration or persistent-state interpretation and required configuration-side project decisions.

`SCAF-ROB` **Defines Framework Semantics / Obligation** for Fault/Error/Failure meaning, health determination, containment/degradation/recovery and resilience response when a CFG-controlled condition becomes robustness-significant. CFG **SHALL NOT** re-own the resilience response merely because configuration failure is its trigger.

### `SCAF-CFG-033` — CFG / ARCH structural allocation boundary

**Target:** Framework Normative Invariant

`SCAF-ARCH` **Defines Framework Semantics / Obligation** for System/Node/Domain/topology/shared-resource structure and the Project Design Authority defines the actual project structural allocation.

`SCAF-CFG` may define configuration source/replica/synchronization responsibility using controlled structural identities but **SHALL NOT** redefine Node/Domain/topology boundaries merely to organize configuration storage or distribution.

### `SCAF-CFG-034` — CFG / external security, safety, regulatory and risk authority boundary

**Target:** Framework Normative Invariant

Applicable safety/hazard, security, regulatory and risk authorities remain source authorities for their objectives, constraints, authorization/risk assumptions and acceptance decisions. `SCAF-CFG` may define configuration obligations needed to satisfy those controlled inputs but **SHALL NOT** invent a universal security objective, trust policy, Safe State, calibration acceptance criterion or risk-acceptance basis.

### `SCAF-CFG-035` — CFG / ASSUR evidence-sufficiency and closure boundary

**Target:** Framework Normative Invariant

`SCAF-CFG` **Defines Framework Semantics / Obligation** for configuration/persistent-state project decisions and source semantics.

`SCAF-ASSUR` **Defines Framework Semantics / Obligation** for verification methods, verification-evidence properties and evidence-sufficiency criteria; the Project Verification / Assurance Authority determines actual project evidence sufficiency. A valid or successfully migrated/committed CFG item **SHALL NOT** by itself establish verification sufficiency or underlying requirement/risk/deviation closure.

### `SCAF-CFG-036` — Artifact / storage / source-authority boundary

**Target:** Framework Normative Invariant

A configuration artifact, record, database entry, NVM location, file, registry item, message, cache or derived copy may record/carry a controlled project decision but **SHALL NOT** become an authority role merely by storing the value. Authority remains with the applicable project/external authority and PDA-assigned source responsibility.

### `SCAF-CFG-037` — CFG / identity partition boundary

**Target:** Framework Normative Invariant

CFG item/version identity is distinct from OBS evidence-item identity, LIFE Boot Incarnation, RUN Operational Incarnation, INT Protocol/Connection Session Identity and TIME Epoch/Time Domain. `SCAF-CFG` may trace/correlate those source identities where configuration applicability depends on them but **SHALL NOT** redefine or merge them.

### `SCAF-CFG-038` — CFG / PROF / Project Realization mechanism boundary

**Target:** Framework Normative Invariant

`SCAF-CFG` **Defines Framework Semantics / Obligation** for configuration/persistent-state properties and required project decisions, not the realization mechanism.

`SCAF-PROF` may **Guide Realization** / **Constrain** applicable realization choices, and Project Realization implements the selected mechanism. No L1/L2 CFG requirement **SHALL** universally mandate a file format, database, registry, EEPROM/FRAM/flash layout, redundant copy, journal, checksum/CRC, schema language, validator, configuration protocol, calibration store, synchronization algorithm or other implementation technology.

## 5. Required Project Decisions / Records

The following table is informative and does not create additional normative requirements.

| Decision / record | Project-side authority / provenance |
|---|---|
| Material CFG concern inventory / semantic classification | Project Design Authority / applicable requirement or external authority |
| Authoritative configuration/persistent-state source responsibility | Project Design Authority |
| CFG item identity / provenance | Project Design Authority under CFG obligations |
| Defaults / provisioning / initialization | Project Design Authority using controlled source constraints |
| Validity / unknown / indeterminate semantics | Project Design Authority under CFG obligations |
| Version / compatibility / migration result | Project Design Authority using applicable CFG/INT/LIFE constraints |
| Commit / activation / rollback semantics | Project Design Authority under CFG obligations with LIFE mapping as applicable |
| Persistent operational-state / RUN mapping | Project Design Authority using CFG and RUN obligations |
| Calibration / parameter authority and provenance | Project Design Authority / applicable external authority |
| Cross-participant consistency / synchronization | Project Design Authority using ARCH/INT/TIME constraints |
| OBS evidence view of CFG facts | Project Design Authority using OBS obligations |
| Verification evidence-sufficiency evaluation | Project Verification / Assurance Authority using SCAF-ASSUR semantics |

`SCAF-APP` **Dispositions / Traces** these decisions but does not own them.

## 6. Concern Boundaries

- `SCAF-CTX` **Defines Framework Semantics / Obligation** for Function/Service context and consequence that motivates configuration/persistent-state need.
- `SCAF-ARCH` **Defines Framework Semantics / Obligation** for structural/Domain/topology/shared-resource context used to allocate configuration/persistent-state responsibilities.
- `SCAF-INT` **Defines Framework Semantics / Obligation** for exchange contract/validity/order/compatibility/session semantics used to transport configuration.
- `SCAF-TIME` **Defines Framework Semantics / Obligation** for measurable synchronization, age, deadline, capacity and resource properties used by CFG decisions.
- `SCAF-RUN` **Defines Framework Semantics / Obligation** for authoritative current operational state/readiness/transition semantics that may consume persistent CFG state.
- `SCAF-ROB` **Defines Framework Semantics / Obligation** for failure/health/resilience meaning and response when CFG conditions become robustness-significant.
- `SCAF-LIFE` **Defines Framework Semantics / Obligation** for boot/reset/power/update/activation/rollback lifecycle transactions that may consume/coordinate CFG results.
- `SCAF-OBS` **Defines Framework Semantics / Obligation** for evidence representing/preserving/correlating CFG facts/results without becoming CFG source authority.
- `SCAF-CFG` **Defines Framework Semantics / Obligation** for configuration/persistent operational-state source/value/version/validation/migration/commit/rollback/calibration/synchronization semantics.
- `SCAF-SEC` **Defines Framework Semantics / Obligation** for the SCAF security architecture interface/robustness boundary and consumes applicable Security Authority objectives/constraints; CFG consumes resulting authorization/integrity/confidentiality constraints without becoming security risk authority.
- `SCAF-ASSUR` **Defines Framework Semantics / Obligation** for verification/evidence-sufficiency semantics; Project Verification / Assurance Authority **Verifies** applicable obligations and determines actual evidence sufficiency.
- `SCAF-PROF` may **Guide Realization** / **Constrain** applicable configuration/persistence implementations; Project Realization implements the selected mechanism.

## 7. Non-Normative Example

A distributed system may retain a calibration parameter, a last-known persistent operational setting and incident evidence in the same physical nonvolatile device. CFG requires the project to define the authoritative configuration/persistent-state sources, identity/version/validity/migration/commit semantics and cross-participant consistency rules. OBS may preserve copies of those values as incident evidence with evidence provenance, but the evidence copy does not become the configuration source. LIFE may coordinate an update/activation/rollback transaction that consumes a CFG migration/commit result, but lifecycle transaction completion does not redefine the CFG version/migration meaning. Whether the realization uses a file, database, EEPROM, FRAM, flash, registry, redundant copy or journal is outside L1/L2 CFG normative scope.
