# SCAF Taxonomy Proposal

> **Frozen architecture reference:** The v0.0.1 taxonomy/authority structure is frozen as the architecture baseline. v0.0.2rc01 normative L1/L2 content is authored under `docs/normative/`; this file remains the architecture reference rather than the sole normative requirements source.

## 1. Purpose

This document records the **v0.0.1 frozen conceptual architecture / authority-kernel baseline** for System Control Architecture Framework (SCAF).

It is intentionally not a final file/directory plan. The purpose is to stabilize ontology, authority and application semantics as the architecture kernel for controlled normative rewriting.

## 2. Scope of “System Control”

SCAF concerns system-level coordination, runtime behavior, interaction, lifecycle, robustness and related architecture decisions.

**Control does not mean control theory and does not mean only host-to-device control.**

Control theory, signal processing or motor-control algorithms may be relevant project domains, but they are outside SCAF unless they create architecture obligations covered by SCAF concerns such as timing, interaction, lifecycle, robustness, evidence or safety interfaces.

## 3. Authority Planes

rc1 mixed several ontology planes into one branch list. rc05 retains five **SCAF framework planes** and one canonical authority relationship to project-side design/realization. Project Design Authority is an external project-side authority bridge, not a sixth SCAF framework plane.

### Plane A — Framework / Governance

Purpose: define how SCAF itself is authoritative and controlled.

Primary concern:

- `SCAF-GOV` Framework Governance & Authority.

Includes:

- normative language;
- authority/precedence;
- provenance;
- RC/freeze/release policy;
- change classification;
- compatibility of SCAF authorities;
- contribution/legal/third-party boundaries where applicable.

### Plane B — System Concerns

Purpose: define properties/decisions of the system being engineered.

Primary concerns:

- `SCAF-CTX` System Context, Mission, Function & Service;
- `SCAF-ARCH` System / Node / Role / Domain Architecture;
- `SCAF-INT` Interfaces, Interaction & Data Contracts;
- `SCAF-RUN` Runtime Behavior, State & Operational Lifecycle;
- `SCAF-TIME` Timing, Concurrency, Capacity & Resource Margin;
- `SCAF-ROB` Robustness & Resilience;
- `SCAF-LIFE` Boot, Power, Reset & Update Lifecycle;
- `SCAF-OBS` Observability, Diagnostics & Incident Evidence;
- `SCAF-SEC` Security Architecture Interface & Robustness;
- `SCAF-CFG` Configuration & Persistent Operational State.

### Plane C — Project Application

Purpose: instantiate SCAF against a project and record applicability, decision, risk, deviation and trace state.

Primary concern:

- `SCAF-APP` Framework Scan / Applicability Analysis.

This plane **Dispositions** SCAF concerns for a project. It is neither the source authority for the underlying SCAF obligation nor the authority that defines the project-specific architecture value. The latter belongs to the project's designated **Project Design Authority**, a project-side decision authority. Controlled architecture specifications, interface contracts, configuration records and similar artifacts record authoritative project decisions but are not themselves the authority role.

### Plane D — Assurance / Evidence

Purpose: establish how architecture obligations are demonstrated.

Primary concern:

- `SCAF-ASSUR` Verification, Fault Injection & Evidence.

### Plane E — Realization / Implementation

Purpose: provide technology-/runtime-/language-specific mechanisms for satisfying system properties.

Primary concern:

- `SCAF-PROF` Realization / Implementation Profiles.

### Relationship to Project-Side Authority

The five planes above are **SCAF framework planes**. They define SCAF authority, project-application semantics, assurance semantics and realization guidance. They do not replace project governance or project architecture authority.

The **Project Design Authority** is the project-side bridge between applicable SCAF concern obligations and the project's actual architecture decisions. **Project Realization** implements those decisions. SCAF Framework / Governance governs SCAF normative sources, precedence and change/release semantics; it does not organizationally govern Project Design Authority or Project Realization.

### Supporting Mechanisms — Not Peer Taxonomy Branches

Examples:

- machine-readable schemas;
- validators;
- regression tests;
- CI;
- generated artifacts;
- AI-assisted engineering process.

They support or enforce authorities after those authorities stabilize.

## 4. Core Metamodel

### 4.1 System

A **System** is the bounded subject to which architecture obligations are applied. A System may include hardware, software, programmable logic, operators, external services and subordinate systems as defined by project scope.

System boundary must state:

- included/excluded elements;
- external actors/systems;
- operating environment;
- mission/use cases/modes;
- assumptions and constraints.

### 4.2 Function

A **Function** is intended system behavior or transformation that contributes to a system objective.

Function is not tied to one implementation entity.

### 4.3 Service

A **Service** is behavior or utility exposed by a provider to one or more consumers under a defined provider/consumer contract and stated conditions.

A service model should be able to identify:

- provider(s);
- consumer(s);
- dependencies;
- availability/degradation expectations;
- criticality/mission consequence;
- recovery priority;
- alternate/redundant provider where applicable.

### 4.4 Capability

A **Capability** is an ability of a System or Node to perform a function under stated conditions. A capability may enable one or more services, but it is not defined by the existence of a service.

Capabilities may be declared, negotiated or inferred only according to an applicable contract.

### 4.5 Node

A **Node** is an architectural entity that carries independently meaningful system obligations and has a distinguishable responsibility, lifecycle or interaction identity.

A Node is **not automatically**:

- a physical device;
- a PCB;
- a chip;
- an MCU core;
- a process/thread;
- an FPGA block;
- a network endpoint.

Any of those may be modeled as a Node when separating them is necessary to express independent architectural obligations.

#### Node boundary test

A candidate boundary is more likely to deserve Node status when multiple independently meaningful obligations or one clearly controlling architecture obligation make the separation necessary. Relevant criteria include:

- responsibility/authority ownership;
- lifecycle/readiness/recovery;
- addressability/interaction identity;
- deployment/update identity;
- resource ownership;
- fault isolation expectation;
- independent verification/evidence obligation.

A physical boundary or a verification task alone is insufficient. Avoid creating Nodes that add no distinct architecture decisions, lifecycle/interaction identity or controlled obligations.

#### Hierarchical Nodes

A Node may contain subordinate Node(s) if the subordinate entities have independent obligations. Hierarchy must not be used merely to mirror hardware decomposition.

#### Subordinate System vs subordinate Node

A **subordinate System** has its own explicitly bounded system scope and may have its own SCAF application, context and project authorities. A **subordinate Node** remains an architectural entity inside the current System scope and does not imply a separate system-application boundary.

A subordinate System may be represented at the parent-system level as a participant or Node abstraction when the parent needs a responsibility/lifecycle/interaction identity for it. In that case the parent-level abstraction and the subordinate-system scope must be explicitly related; obligations are not silently duplicated or collapsed across the two scopes.

### 4.6 Role

A **Role** is contextual responsibility or authority exercised by a System/Node in a defined relationship or operating context.

Role is not a containment child class and may change by interaction/context.

Examples that **may** be roles when responsibility semantics are defined:

- coordinator;
- supervisor;
- controller;
- gateway;
- provider;
- consumer;
- diagnostic tool;
- update authority.

`Device` is not automatically a role because it may describe only a physical/deployment category.

### 4.7 Interface

An **Interface** is a defined boundary surface through which information, control, energy or other project-relevant exchanges occur.

SCAF primarily governs information/control interfaces and their architecture implications; physical/electrical detail is included only where it creates relevant architecture obligations.

### 4.8 Interaction

An **Interaction** is behavior/exchange among two or more participants through one or more interfaces.

Examples:

- command/response;
- event publication;
- telemetry/stream;
- shared-memory handoff;
- register access;
- DMA ownership transfer;
- RPC/IPC;
- update transaction;
- supervision/heartbeat;
- failover/reconciliation.

### 4.9 Domain

A **Domain** is a boundary used to reason about a cross-cutting property. Domain boundaries may align with, subdivide or cross Node boundaries.

Required domain types to consider:

- Fault Domain;
- Reset Domain;
- Power Domain;
- Security/Trust Domain;
- Resource Domain;
- Clock / Time Domain.

Projects may add domain types when justified.

## 5. Authority Relation Grammar

Cross-cutting does not mean duplicate authority. rc05 retains the distinction between **framework-level normative authority** and **project-instance design authority** and uses one canonical chain across all documents.

| Relation | Meaning | Typical owner |
|---|---|---|
| **Defines Framework Semantics / Obligation** | Defines SCAF semantics, required consideration, constraint, or required project decision | SCAF concern authority |
| **Defines Project Instance / Decision** | Defines the actual project-specific architecture value, boundary, topology, allocation, threshold, state, or selected design | Project Design Authority |
| **Constrains** | Adds conditions/limits to an item owned elsewhere | SCAF concern or external/project authority |
| **Guides Realization** | Framework-side profile/pattern content constrains or informs implementation without becoming the project realization actor | `SCAF-PROF` / applicable pattern authority |
| **Realizes** | Project-side implementation of a Controlled Decision / required property | Project Realization |
| **Observes** | Provides runtime visibility/evidence about a property | Observability/diagnostic realization |
| **Verifies** | Project-side demonstration/evaluation of an applicable obligation, project decision, realization and evidence | Project Verification / Assurance Authority |
| **Dispositions** | Records project applicability, decision state, risk, deviation and trace status | `SCAF-APP` |

Required authority chain:

```text
SCAF Concern Authority
    Defines Framework Semantics / Obligation
        ↓
Project Design Authority
    Defines Project Instance / Decision
        ↓
Project Realization
    Realizes the decision / obligation
        ↓
Project Verification / Assurance Authority
    Verifies satisfaction using SCAF-ASSUR evidence semantics

SCAF-APP cross-cuts the chain by Dispositioning and tracing
applicability, decisions, risks, deviations, verification and evidence.
```

A Framework Scan does not become a project architecture specification. Conversely, a project design artifact does not redefine SCAF semantics.

## 6. System Concern Taxonomy

### 6.1 `SCAF-CTX` — System Context, Mission, Function & Service

**Defines Framework Semantics / Obligation for:**

- system boundary and external-actor definition criteria;
- mission/use-case/operating-mode framing;
- assumptions/constraints/unknowns;
- Function / Service / Capability semantics;
- logical provider/consumer/service-dependency semantics;
- service criticality and consequence-of-loss analysis;
- required consideration of degraded service levels;
- project safety/security context references.

The **Project Design Authority** defines the actual project boundary, actors, mission model, service catalog, logical service dependencies, criticality and project-specific values. `SCAF-APP` dispositions and traces applicability; it does not own those design values.

### 6.2 `SCAF-ARCH` — System / Node / Role / Domain Architecture

**Defines Framework Semantics / Obligation for:**

- Node-boundary and hierarchy criteria;
- role-assignment and role-relativity semantics;
- responsibility/authority ownership;
- structural topology;
- capability/service allocation;
- shared-resource ownership;
- Fault/Reset/Power/Security/Resource/Clock domain modeling;
- structural realization dependencies;
- aggregation/composition.

`SCAF-CTX` owns logical mission/service dependency semantics; `SCAF-ARCH` owns structural allocation and realization-dependency semantics. The **Project Design Authority** defines the actual Node/domain boundaries, topology, allocations and structural dependencies for the project. Implementation technology is not part of the core Node definition.

### 6.3 `SCAF-INT` — Interfaces, Interaction & Data Contracts

**Defines Framework Semantics / Obligation for:**

- interface identity;
- interaction semantics;
- commands/responses/events/telemetry/streams where applicable;
- register/shared-memory/IPC/RPC/DMA contracts where applicable;
- protocol vs transport separation;
- addressing/routing/targeting;
- data representation/serialization;
- validity, freshness, ordering and provenance contract semantics;
- compatibility/evolution;
- protocol / connection session identity and generation semantics where applicable;
- negative behavior;
- machine-readable contract applicability.

**Constrained by:** Security, Timing, Robustness and Lifecycle concerns as applicable.

### 6.4 `SCAF-RUN` — Runtime Behavior, State & Operational Lifecycle

**Defines Framework Semantics / Obligation for:**

- state domains and state ownership;
- transition rules/invariants;
- initialization/readiness at generic runtime level;
- normal/start/stop/suspend/resume behavior;
- service availability state;
- cross-node state consistency;
- operational-state incarnation/generation semantics where needed to distinguish restarted or replaced runtime state;
- generic lifecycle transition obligations.

Partition rule: `SCAF-RUN` covers **service/operational state lifecycle**. `SCAF-LIFE` covers **platform/system activation, boot, reset, power and update lifecycle**. Specialized configuration/interface/security lifecycle authorities remain in `SCAF-CFG`, `SCAF-INT` and `SCAF-SEC`.

### 6.5 `SCAF-TIME` — Timing, Concurrency, Capacity & Resource Margin

**Defines Framework Semantics / Obligation for:**

- clock/timebase identity and authority;
- monotonic vs wall-clock semantics;
- synchronization model, drift and uncertainty;
- time-epoch and time-domain semantics;
- deadlines/periods/latency/jitter;
- time budgets and temporal invariants;
- execution/concurrency ownership requirements;
- queueing/backpressure requirements;
- bandwidth/throughput;
- CPU/memory/stack/storage/logic/channel budgets;
- margin/headroom;
- starvation/fairness/overload constraints;
- long-duration accumulation budgets.

Identity/time partition:

- **Time Epoch / Time Domain** semantics belong to `SCAF-TIME`.
- **Boot Incarnation / Boot Generation** belongs to `SCAF-LIFE`.
- **Protocol / Connection Session Identity** belongs to `SCAF-INT`.
- **Operational State Incarnation** belongs to `SCAF-RUN` where applicable.
- `SCAF-OBS` records these identities, time provenance and correlation metadata as evidence; it does not redefine their primary semantics.

`SCAF-PROF` may **guide or constrain Project Realization** of RTOS/thread/ISR/FPGA scheduling and language/runtime mechanisms; the project realization actor implements them.

### 6.6 `SCAF-ROB` — Robustness & Resilience

#### Fault / Error / Failure semantics

```text
Fault source / condition
  -> activation
  -> erroneous state
  -> propagation
  -> service failure
  -> system consequence
```

The framework must distinguish these concepts rather than treating every symptom as a “fault.”

#### Runtime resilience response

```text
Detect
  -> isolate / contain
  -> tolerate / mask / reconfigure
  -> fail over / degrade / safe action
  -> recover / repair
  -> resynchronize / reintegrate
```

Not every project uses every step. Framework Scan determines applicability and required decisions.

#### Defines Framework Semantics / Obligation / constrains

- fault assumptions and propagation paths;
- detection/health/supervision;
- diagnostic coverage and latent faults;
- containment behavior;
- redundancy/failover/tolerance/masking;
- reconfiguration;
- graceful degradation;
- recovery/repair/retry limits;
- resynchronization/reintegration;
- communication partition/reconciliation;
- common-mode/correlated faults;
- cascading/recovery-storm behavior;
- resource exhaustion;
- long-run robustness;
- security-related robustness interfaces with `SCAF-SEC`.

#### ROB / LIFE / OBS boundary

- `SCAF-ROB` owns framework semantics for failure/health decision, containment, tolerance, degradation and recovery behavior.
- `SCAF-LIFE` owns boot/power/reset/update transaction and state semantics; when a lifecycle operation fails, `SCAF-ROB` defines the required resilience properties while `SCAF-LIFE` retains lifecycle sequence/atomicity/activation/rollback semantics.
- `SCAF-OBS` owns observation, representation, preservation and export of health/diagnostic/incident evidence; it does not redefine what constitutes a failure or what resilience action is required.
- `SCAF-ASSUR` verifies these obligations and evidence sufficiency; it does not own the runtime behavior.

#### Safe State boundary

SCAF does not independently invent a universal safety-significant Safe State.

For a safety-relevant project, the applicable project safety/hazard authority defines the safety objective/condition and risk-acceptance basis. The Project Design Authority integrates that external constraint into the actual architecture. SCAF governs architecture responsibility, entry/exit behavior, interaction, observability and verification obligations around that definition.

### 6.7 `SCAF-LIFE` — Boot, Power, Reset & Update Lifecycle

**Defines Framework Semantics / Obligation for:**

- power-on/off and brownout-relevant behavior;
- reset taxonomy and reset-domain behavior;
- reset cause;
- boot incarnation / boot generation identity;
- boot ordering/readiness;
- retained-state validity;
- bootloader/application boundary;
- update transaction and coordination;
- activation/health confirmation;
- resume/rollback;
- failed-update recovery;
- coordinated multi-node update/recovery;
- lifecycle effects on evidence survivability.

`SCAF-LIFE` defines lifecycle transaction/state semantics. Fault tolerance or recovery properties required when those operations fail are defined/constrained by `SCAF-ROB`; evidence survivability/recording is defined by `SCAF-OBS`.

### 6.8 `SCAF-OBS` — Observability, Diagnostics & Incident Evidence

**Defines Framework Semantics / Obligation for three observability levels:**

1. Operational observability — metrics/status/routine logs/counters.
2. Diagnostics — fault codes/invariants/health/service data.
3. Incident evidence — first-abnormal-state, timeline, fatal context, retained/persistent evidence, postmortem correlation/export.

**Defines Framework Semantics / Obligation / Constrains:**

- first abnormal vs final crash distinction;
- evidence identity/provenance;
- local evidence ordering;
- recorded boot incarnation, protocol/session identity and operational incarnation as defined by their source concerns;
- observed time provenance / clock source identity;
- recorded synchronization quality/uncertainty defined by `SCAF-TIME`;
- cross-node evidence correlation and causal correlation;
- evidence quality, survivability and accessibility;
- recorder/observer self-health;
- low-coupling observation and observer-effect limits;
- early-boot salvage/crash-loop evidence where applicable.

Recorder-specific APIs, memory layouts and storage mechanisms belong in realization/reference profiles. `SCAF-ROB` defines what constitutes failure/health detection and the required resilience response; `SCAF-OBS` defines how those states and effects are made observable and preserved as evidence.

### 6.9 `SCAF-SEC` — Security Architecture Interface & Robustness

SCAF does **not** replace a project's cybersecurity/threat/risk authority. When security is applicable, the external/project Security Authority defines threat assumptions, security objectives, security risk evaluation/acceptance and externally imposed security constraints. It does not create a competing project architecture authority.

`SCAF-SEC` **Defines Framework Semantics / Obligation and constrains architecture for:**

- representation of assets and trust/security domains;
- peer identity/authentication/authorization architecture obligations;
- confidentiality/integrity architecture obligations where required by project security authority;
- anti-replay and hostile freshness interfaces with `SCAF-INT` / `SCAF-TIME`;
- key/credential lifecycle architecture interfaces;
- privilege separation;
- malformed/hostile input and resource-abuse resistance;
- compromised-node containment with `SCAF-ROB` / `SCAF-ARCH`;
- secure boot/update linkage;
- security-service failure and recovery interfaces;
- security incident evidence requirements.

The **Project Design Authority**, informed/constrained by the applicable Security Authority, defines actual trust boundaries, architecture allocations, selected mechanisms and project values. If a security team is delegated authority to make one of those architecture decisions, it is acting as the Project Design Authority for that decision rather than creating a second design-authority chain. Protocol secure-session mechanics are subordinate realizations/profiles.

### 6.10 `SCAF-CFG` — Configuration & Persistent Operational State

**Defines Framework Semantics / Obligation for:**

- configuration ownership and authority;
- defaults/provisioning;
- validation;
- version/migration;
- atomic update/commit;
- persistence;
- rollback/corruption recovery;
- calibration/parameter state;
- synchronization across Nodes;
- provenance and activation state;
- distinction from incident-evidence persistence.

## 7. Project Application Plane — `SCAF-APP`

### 7.1 Framework Scan is not normative source authority

Healthy trace direction:

```text
SCAF Concern / Normative Obligation
        ↓
Project Applicability
        ↓
Required Project Decision
        ↓
Project Design Authority defines actual value / design
        ↓
Project Realization
        ↓
Verification Obligation
        ↓
Evidence
```

A Framework Scan cannot silently create or delete a SCAF requirement and cannot substitute for the project architecture/design artifact. It records project-specific disposition and may expose **project obligations** such as a required design decision, risk treatment, verification activity or evidence item.

### 7.2 Independent state dimensions

Exact enums are not frozen, but these dimensions are distinct:

**Applicability**

```text
Applicable
Not Applicable
Undetermined
```

**Decision**

```text
Decision Required
Decided
Deferred
Exception / Deviation
```

**Risk**

```text
None Identified
Open
Mitigated
Accepted
```

**Verification**

```text
Not Required
Required
Planned
Passed
Failed
```

**Evidence**

```text
Not Required
Required
Available
Accepted
Insufficient
```

These values are provisional conceptual examples, not frozen schema enums.

### 7.3 Scan lifecycle

```text
Initial project framing
  -> provisional CTX
  -> Concern / scope
  -> applicability
  -> failure consequence / risk
  -> required design decision
  -> Project Design Authority / actual project value
  -> realization responsibility
  -> Applicable Satisfaction Basis
  -> verification obligation / method
  -> evidence
  -> closure / deviation
  -> re-evaluation trigger
  -> update CTX/ARCH and re-scan when decisions change the system model
```

The startup model is intentionally iterative. Greenfield projects are not expected to have a complete system boundary, service model or architecture before the first scan pass.

### 7.4 Ownership is not necessarily singular

A project may need distinct:

- Decision Owner;
- Implementation Owner;
- Verification Owner;
- Risk Acceptance Owner.

The architecture baseline does not require four separate owner fields, but it rejects the assumption that one generic `Owner` is always sufficient.


### 7.5 Closure semantics

Closure is not a new single-owner authority. It is a recorded disposition reached after the applicable **Satisfaction Basis** has been evaluated.

The **Applicable Satisfaction Basis** is a traceable combination, as applicable, of:

- SCAF concern semantics / obligation;
- Project Design Authority values, thresholds or architecture decisions;
- external authority constraints (for example safety, security or risk authority);
- any explicitly controlled acceptance condition derived from those sources.

It does not create a new authority and is not owned by `SCAF-ASSUR`.

- `SCAF-ASSUR` defines verification/evidence-sufficiency semantics; the Project Verification / Assurance Authority **Verifies** the obligation/decision and evaluates project evidence.
- the authority that owns the underlying project decision, requirement, risk acceptance or deviation accepts the corresponding closure as applicable;
- `SCAF-APP` **Dispositions** and traces the closure/deviation state, evidence reference and re-evaluation trigger;
- a failed verification, design change, new risk or changed assumption re-opens the affected scan item.

Therefore an `ASSUR closure` is not a valid substitute for Project Design Authority, Risk Acceptance Authority or another source owner.

## 8. Assurance and Realization Planes

### 8.1 `SCAF-ASSUR` — Verification, Fault Injection & Evidence

**Defines Framework Semantics / Obligation for:**

- verification obligation types and methods;
- evidence sufficiency / pass-fail evaluation procedure;
- review/test/analysis/inspection evidence;
- evidence identity, traceability and reproducibility;
- fault-injection assurance;
- coverage claims;
- observer-effect verification;
- unresolved anomaly handling;
- conformance/deviation evidence.

The Applicable Satisfaction Basis is derived from the applicable SCAF concern, Project Design Authority and any applicable external authority constraints. `SCAF-ASSUR` defines verification/evidence-sufficiency semantics and does not redefine the underlying property, project threshold or external acceptance constraint.

Fault injection belongs here as an assurance activity, though injection targets may be defined by `SCAF-ROB`, `SCAF-LIFE`, `SCAF-INT`, `SCAF-SEC`, etc.

### 8.2 `SCAF-PROF` — Realization / Implementation Profiles

Profiles are **composable axes**, not one flat mutually exclusive list.

Candidate axes:

1. **Compute / deployment technology** — MCU, SoC, FPGA, DSP, PC, SBC, etc.
2. **Execution model** — bare metal, RTOS, general-purpose OS, event loop, programmable logic pipeline, etc.
3. **Language / runtime** — Embedded C, C++, C#/.NET, Rust, HDL, etc. as adopted by a project.
4. **Interaction / transport realization** — UART, RS-485, CAN, Ethernet, BLE, shared memory, IPC, register bus, DMA, etc.
5. **Persistence / storage realization** — internal flash, external flash, FRAM, file system, database, remote service, etc.
6. **Human-interface realization** — LCD/HMI/desktop/web/service-tool patterns where applicable.

**Reference subsystems / reusable patterns** (for example an incident recorder reference architecture) may also live in the Realization Plane, but they are not profile axes.

A project may use several axes at once. `SCAF-PROF` **guides or constrains Project Realization**; the project realization actor performs the actual realization. Profiles do not replace system concern authority or Project Design Authority.

## 9. Cross-Cutting Authority Matrix

| Topic | SCAF Defines Framework Obligation | Project Defines Instance / Decision | Constrains / Observes | Realizes | Verifies / Dispositions |
|---|---|---|---|---|---|
| Service criticality / consequence | `SCAF-CTX` | project context/service authority | `SCAF-ROB`, safety/security authorities | Project Realization (guided/constrained by `SCAF-PROF`) | Project Verification / Assurance Authority (using `SCAF-ASSUR`); `SCAF-APP` dispositions/traces |
| Node / domain boundary | `SCAF-ARCH` | project architecture authority | `SCAF-ROB`, `SCAF-SEC`, `SCAF-LIFE`, `SCAF-TIME` | Project Realization (guided/constrained by `SCAF-PROF`) | Project Verification / Assurance Authority (using `SCAF-ASSUR`); `SCAF-APP` dispositions/traces |
| Interface freshness semantics | `SCAF-INT`, temporal semantics from `SCAF-TIME` | project interface authority | `SCAF-ROB`, `SCAF-SEC` | Project Realization (guided/constrained by `SCAF-PROF`) | Project Verification / Assurance Authority (using `SCAF-ASSUR`); `SCAF-APP` dispositions/traces |
| Runtime state ownership | `SCAF-RUN` | project state-machine/runtime authority | `SCAF-ROB`, `SCAF-LIFE` | Project Realization (guided/constrained by `SCAF-PROF`) | Project Verification / Assurance Authority (using `SCAF-ASSUR`); `SCAF-APP` dispositions/traces |
| Timebase / synchronization | `SCAF-TIME` | project timing/clock authority | `SCAF-OBS` observes quality | Project Realization (guided/constrained by `SCAF-PROF`) | Project Verification / Assurance Authority (using `SCAF-ASSUR`); `SCAF-APP` dispositions/traces |
| Timing/resource budget | `SCAF-TIME` | project architecture/performance authority | `SCAF-ROB` | Project Realization (guided/constrained by `SCAF-PROF`) | Project Verification / Assurance Authority (using `SCAF-ASSUR`); `SCAF-APP` dispositions/traces |
| Fault containment behavior | `SCAF-ROB` using domain semantics from `SCAF-ARCH` | project robustness/architecture authority | `SCAF-SEC`, `SCAF-LIFE` | Project Realization (guided/constrained by `SCAF-PROF`) | Project Verification / Assurance Authority (using `SCAF-ASSUR`); `SCAF-APP` dispositions/traces |
| Boot/reset/update | `SCAF-LIFE` | project lifecycle/update authority | `SCAF-ROB`, `SCAF-SEC`, `SCAF-CFG`, `SCAF-OBS` | Project Realization (guided/constrained by `SCAF-PROF`) | Project Verification / Assurance Authority (using `SCAF-ASSUR`); `SCAF-APP` dispositions/traces |
| Incident evidence semantics | `SCAF-OBS` | project diagnostic/evidence authority | `SCAF-LIFE`, `SCAF-ROB`, `SCAF-SEC`, `SCAF-TIME` | Project Realization (guided/constrained by `SCAF-PROF`) | Project Verification / Assurance Authority (using `SCAF-ASSUR`); `SCAF-APP` dispositions/traces |
| Configuration lifecycle | `SCAF-CFG` | project configuration authority | `SCAF-LIFE`, `SCAF-SEC`, `SCAF-ROB` | Project Realization (guided/constrained by `SCAF-PROF`) | Project Verification / Assurance Authority (using `SCAF-ASSUR`); `SCAF-APP` dispositions/traces |
| Security architecture interface | `SCAF-SEC` | project architecture authority informed by security authority | `SCAF-ROB`, `SCAF-INT`, `SCAF-TIME`, `SCAF-LIFE` | Project Realization (guided/constrained by `SCAF-PROF`) | Project Verification / Assurance Authority (using `SCAF-ASSUR`); `SCAF-APP` dispositions/traces |

## 10. Tabletop Architecture Validation

These exercises are not full project analyses. They test whether the rc05 metamodel requires ad-hoc taxonomy exceptions.

### 10.1 Archetype A — Single MCU System

Example:

```text
System: standalone embedded controller
Node N1: MCU application entity
Services: sensing, control output, diagnostics
Interactions: local sensor/actuator buses, optional service port
Domains: one power domain; reset domain may include bootloader+application; fault/resource domains project-defined
```

Observations:

- no Host/Device assumption is required;
- MCU is a realization technology, not the system class;
- bootloader need not be a separate Node unless it has independently meaningful lifecycle/update obligations;
- fault/reset/power domains can align with N1 without being defined as N1 itself;
- Framework Scan can still require decisions on watchdog, evidence, update, resource margin and long-run behavior.

**Result:** representable without adding a new top-level category.

### 10.2 Archetype B — PC + Multiple MCU

Example:

```text
System
 ├─ N1 PC supervisory application
 ├─ N2 MCU controller A
 └─ N3 MCU controller B

Services
 ├─ supervisory configuration/monitoring
 ├─ control service A
 └─ control service B

Interactions
 ├─ N1 <-> N2
 └─ N1 <-> N3
```

Possible contextual roles:

- N1 = supervisor/provider/consumer depending on interaction;
- N2/N3 = service providers and controlled peers;
- neither “Host” nor “Device” is required as a permanent class.

Architecture decisions exposed by SCAF:

- per-node identity and lifecycle;
- shared-bus/addressing if applicable;
- service dependency and partial failure;
- stale UI/telemetry behavior;
- multi-node update coordination;
- fault/recovery isolation;
- cross-node incident correlation.

**Result:** representable without making Coordinator a top-level class.

### 10.3 Archetype C — SoC + FPGA + DSP Heterogeneous System

A physical package/chassis does not dictate Node boundaries.

One project might choose:

```text
System
 ├─ N1 supervisory software domain on SoC
 ├─ N2 DSP execution domain
 └─ N3 FPGA control/data-plane domain
```

Another project may legitimately combine or subdivide these if independent architectural obligations differ.

Cross-cutting domains may look different from Node boundaries:

```text
Power Domain P1: N1 + N2 + N3
Reset Domain R1: N1 + N2
Reset Domain R2: N3
Fault Domain F1: N2 signal-processing chain
Fault Domain F2: N3 actuator-control logic
Security Domain S1: external-facing N1
Resource Domain Q1: shared memory / interconnect across N1/N2/N3
```

Architecture decisions exposed by SCAF:

- lifecycle/readiness dependencies;
- shared-memory/data freshness;
- reset/recovery coordination;
- FPGA/DSP state resynchronization;
- fault propagation through shared interconnect/resources;
- service degradation/failover;
- evidence correlation without assuming one clock source.

**Result:** representable without declaring SoC/FPGA/DSP themselves universal Node classes and without forcing domain boundaries to match Node boundaries.

### 10.4 Worked Framework Scan — Archetype B

This exercise proves the independent state dimensions and closure authority on selected concerns rather than using a large row count as proof. Values are **illustrative project decisions**, not normative SCAF defaults.

#### Worked item A — Interface freshness / stale telemetry

| Field | Illustrative project disposition |
|---|---|
| SCAF concern / obligation | `SCAF-INT` requires a validity/freshness contract; `SCAF-TIME` constrains measurable age/time semantics; `SCAF-ROB` constrains behavior after freshness loss. |
| Applicability state | **Applicable** — operator-facing telemetry crosses N2/N3 -> N1. |
| Failure consequence | Stale data may be displayed as current and lead to an incorrect operational decision. |
| Decision state | **Decided** — each telemetry class receives a project-defined maximum age/order rule and explicit stale presentation behavior. |
| Risk state | **Open -> Mitigated** after stale-state handling, bounded age policy and negative-behavior design are accepted. Residual operational risk remains with the project risk authority. |
| Project Design Authority output | Controlled interface/data contract + timing decision defining the actual freshness limits, provenance and stale behavior. |
| Realization responsibility | MCU telemetry producer, transport/serialization realization and PC presentation layer implement the contract; responsibility may be split but remains traced. |
| Applicable Satisfaction Basis | `SCAF-INT/TIME/ROB` obligation semantics + the Project Design Authority's controlled freshness/ordering/stale-behavior values; data outside that basis is never represented or consumed as valid current data and required stale/degraded behavior occurs. |
| Verification state / method | **Required -> Planned -> Passed** using injected delay/drop/reorder/clock-skew scenarios and boundary-value timing tests. |
| Evidence state / item | **Required -> Available -> Accepted** — test report, traces and contract-version identity are linked to the decision. |
| Closure / deviation and authority | Project Interface/Design Authority accepts the implemented project decision; verification authority confirms evidence sufficiency; project risk authority accepts any residual risk; `SCAF-APP` records the resulting closure/deviation and links all authorities/evidence. |
| Re-evaluation trigger | telemetry rate/transport/UI semantics, clock model, freshness threshold, criticality or consumer behavior changes; failed verification re-opens the item. |

#### Worked item B — Partial Node failure / peer isolation and recovery

| Field | Illustrative project disposition |
|---|---|
| SCAF concern / obligation | `SCAF-ROB` requires explicit partial-failure consequence, containment/degradation/recovery decisions using domain semantics from `SCAF-ARCH`. |
| Applicability state | **Applicable** — N2 and N3 provide independent control services while N1 supervises both. |
| Failure consequence | Failure/recovery of one controller may cascade through shared supervisor/resources, reset a healthy peer or leave the system in an incoherent degraded state. |
| Decision state | **Decided** — project architecture defines containment boundary, healthy-peer behavior, degraded-service indication, bounded reconnect/recovery and reintegration criteria. |
| Risk state | **Open -> Mitigated** after architecture and fault-response decisions; residual common-mode/shared-resource risk is separately owned/accepted. |
| Project Design Authority output | Fault/domain architecture + failure-response state model + project recovery limits. |
| Realization responsibility | Supervisory PC logic, MCU local recovery logic and any shared-bus/resource mechanism realize the approved behavior. |
| Applicable Satisfaction Basis | `SCAF-ROB/ARCH` obligation semantics + the Project Design Authority's containment, degraded-service and recovery/reintegration decisions + applicable risk constraints; a single scoped Node failure does not violate the approved containment basis and recovery/reintegration occurs only under defined conditions. |
| Verification state / method | **Required -> Planned -> Passed** using peer-loss, timeout, restart, shared-resource stress and repeated recovery fault injection. |
| Evidence state / item | **Required -> Available -> Accepted** — fault-injection report, state/event traces, reset cause + boot-incarnation identity + applicable protocol/operational incarnation identity, and unresolved-anomaly disposition. |
| Closure / deviation and authority | Project Architecture/Robustness Design Authority accepts the project decision/realization; verification authority accepts evidence sufficiency; risk authority accepts residual risk/deviation if any; `SCAF-APP` records closure and the re-open trigger. |
| Re-evaluation trigger | shared-resource topology, recovery mechanism, service criticality, Node/domain boundary or lifecycle/update behavior changes. |

**Observed startup loop:** the first scan pass produces provisional CTX/ARCH decisions. Those decisions change the scope and dependencies used by later concerns, so the scan re-enters CTX/ARCH rather than running once as a linear checklist.

**Result:** the current independent state dimensions, Project Design/Realization/Assurance authority chain and closure semantics can carry a project-start exercise without inventing a new status category or allowing `SCAF-APP` / `SCAF-ASSUR` to become project architecture authority.

### 10.5 Tabletop conclusion

The v0.0.1 metamodel can describe all three representative archetypes **without adding an ad-hoc top-level taxonomy branch**.

The three architecture exercises establish representability; the worked Archetype B scan now demonstrates complete state/authority/closure traces for selected concerns. This is sufficient to begin controlled normative rewrite, while migration-completion and donor-promotion gates remain separate.

## 11. Current Rewrite Gate

**Controlled L1/L2 normative rewrite is active in v0.0.2rc01 and is based on the frozen v0.0.1 architecture baseline.**

The architecture skeleton remains closed to taxonomy exploration unless a concrete project demonstrates an authority-home failure. The first normative tranche is intentionally bounded to:

1. Authority Kernel normative language;
2. `SCAF-CTX` L1/L2 obligations;
3. `SCAF-ARCH` L1/L2 obligations;
4. lexical/authority cleanup needed to preserve the frozen v0.0.1 model.

Later concern rewrite tranches may expand L1/L2 coverage without reopening top-level taxonomy.

The following remain gated and must not be silently promoted/frozen:

- Draft/RC donor-derived requirements before deep reconciliation;
- executable invariants known only through schemas/validators/tests before extraction and review;
- final requirement-by-requirement Gen1 migration proof;
- donor source-semantic reproducibility until immutable/retrievable donor locators exist;
- final machine-readable schema / validator / CI enforcement;
- broad implementation rulebooks and pattern catalogs before the corresponding L1/L2 authority/obligation content is stable;
- modification of the frozen v0.0.1 baseline in place; semantic changes proceed on a new RC development line.

These are **migration/promotion/completion gates**, not reasons to add new top-level taxonomy branches.
