# SCAF Taxonomy Proposal

## 1. Purpose

This document defines the **v0.0.1rc03 conceptual architecture** for System Control Architecture Framework (SCAF).

It is intentionally not a final file/directory plan. The purpose is to stabilize ontology, authority and application semantics before large-scale normative rewriting.

## 2. Scope of “System Control”

SCAF concerns system-level coordination, runtime behavior, interaction, lifecycle, robustness and related architecture decisions.

**Control does not mean control theory and does not mean only host-to-device control.**

Control theory, signal processing or motor-control algorithms may be relevant project domains, but they are outside SCAF unless they create architecture obligations covered by SCAF concerns such as timing, interaction, lifecycle, robustness, evidence or safety interfaces.

## 3. Authority Planes

rc1 mixed several ontology planes into one branch list. rc03 separates them.

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
- `SCAF-RUN` Runtime Behavior, State & Lifecycle;
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

This plane **Dispositions** SCAF concerns for a project. It is neither the source authority for the underlying SCAF obligation nor the authority that defines the project-specific architecture value. The latter belongs to the project's designated **Project Design Authority** (for example, an architecture specification, interface contract, configuration authority, hazard/security decision, or equivalent controlled design artifact).

### Plane D — Assurance / Evidence

Purpose: establish how architecture obligations are demonstrated.

Primary concern:

- `SCAF-ASSUR` Verification, Fault Injection & Evidence.

### Plane E — Realization / Implementation

Purpose: provide technology-/runtime-/language-specific mechanisms for satisfying system properties.

Primary concern:

- `SCAF-PROF` Realization / Implementation Profiles.

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

A **Service** is a defined capability provided to one or more consumers under stated conditions and contracts.

A service model should be able to identify:

- provider(s);
- consumer(s);
- dependencies;
- availability/degradation expectations;
- criticality/mission consequence;
- recovery priority;
- alternate/redundant provider where applicable.

### 4.4 Capability

A **Capability** is an ability of a System or Node to perform a function or provide a service under stated conditions.

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

A candidate boundary is more likely to deserve Node status when one or more of the following are independently relevant:

- responsibility/authority ownership;
- lifecycle/readiness/recovery;
- addressability/interaction identity;
- deployment/update identity;
- resource ownership;
- fault isolation expectation;
- independent verification/evidence obligation.

A physical boundary alone is insufficient. Avoid creating Nodes that add no distinct architecture decisions.

#### Hierarchical Nodes

A Node may contain subordinate Node(s) if the subordinate entities have independent obligations. Hierarchy must not be used merely to mirror hardware decomposition.

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

Cross-cutting does not mean duplicate authority. rc03 distinguishes **framework-level normative authority** from **project-instance design authority**.

| Relation | Meaning | Typical owner |
|---|---|---|
| **Defines Framework Semantics / Obligation** | Defines SCAF semantics, required consideration, constraint, or required project decision | SCAF concern authority |
| **Defines Project Instance / Decision** | Defines the actual project-specific architecture value, boundary, topology, allocation, threshold, state, or selected design | Project Design Authority |
| **Constrains** | Adds conditions/limits to an item owned elsewhere | SCAF concern or external/project authority |
| **Realizes** | Implements a required property through a technology/profile mechanism | Project realization / implementation |
| **Observes** | Provides runtime visibility/evidence about a property | Observability/diagnostic realization |
| **Verifies** | Demonstrates satisfaction of an applicable obligation, project decision, or realization | `SCAF-ASSUR` / project verification authority |
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
SCAF-ASSUR / Project Verification Authority
    Verifies satisfaction and evidence sufficiency

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

**Defines:**

- interface identity;
- interaction semantics;
- commands/responses/events/telemetry/streams where applicable;
- register/shared-memory/IPC/RPC/DMA contracts where applicable;
- protocol vs transport separation;
- addressing/routing/targeting;
- data representation/serialization;
- validity, freshness, ordering and provenance contract semantics;
- compatibility/evolution;
- negative behavior;
- machine-readable contract applicability.

**Constrained by:** Security, Timing, Robustness and Lifecycle concerns as applicable.

### 6.4 `SCAF-RUN` — Runtime Behavior, State & Lifecycle

**Defines:**

- state domains and state ownership;
- transition rules/invariants;
- initialization/readiness at generic runtime level;
- normal/start/stop/suspend/resume behavior;
- service availability state;
- cross-node state consistency;
- generic lifecycle transition obligations.

Partition rule: `SCAF-RUN` covers **service/operational state lifecycle**. `SCAF-LIFE` covers **platform/system activation, boot, reset, power and update lifecycle**. Specialized configuration/interface/security lifecycle authorities remain in `SCAF-CFG`, `SCAF-INT` and `SCAF-SEC`.

### 6.5 `SCAF-TIME` — Timing, Concurrency, Capacity & Resource Margin

**Defines:**

- clock/timebase identity and authority;
- monotonic vs wall-clock semantics;
- synchronization model, drift and uncertainty;
- epoch/session/time-domain semantics;
- deadlines/periods/latency/jitter;
- time budgets and temporal invariants;
- execution/concurrency ownership requirements;
- queueing/backpressure requirements;
- bandwidth/throughput;
- CPU/memory/stack/storage/logic/channel budgets;
- margin/headroom;
- starvation/fairness/overload constraints;
- long-duration accumulation budgets.

Profiles **Realize** RTOS/thread/ISR/FPGA scheduling and language/runtime mechanisms.

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

#### Defines / constrains

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

#### Safe State boundary

SCAF does not independently invent a universal safety-significant Safe State.

For a safety-relevant project, applicable project safety/hazard authority **Defines** the safety objective/condition. SCAF governs architecture responsibility, entry/exit behavior, interaction, observability and verification obligations around that definition.

### 6.7 `SCAF-LIFE` — Boot, Power, Reset & Update Lifecycle

**Defines:**

- power-on/off and brownout-relevant behavior;
- reset taxonomy and reset-domain behavior;
- reset cause;
- boot ordering/readiness;
- retained-state validity;
- bootloader/application boundary;
- update transaction and coordination;
- activation/health confirmation;
- resume/rollback;
- failed-update recovery;
- coordinated multi-node update/recovery;
- lifecycle effects on evidence survivability.

### 6.8 `SCAF-OBS` — Observability, Diagnostics & Incident Evidence

**Defines three levels:**

1. Operational observability — metrics/status/routine logs/counters.
2. Diagnostics — fault codes/invariants/health/service data.
3. Incident evidence — first-abnormal-state, timeline, fatal context, retained/persistent evidence, postmortem correlation/export.

**Defines/Constrains:**

- first abnormal vs final crash distinction;
- evidence identity/provenance;
- local ordering and boot/session epoch;
- observed time provenance / clock source identity;
- recorded synchronization quality/uncertainty defined by `SCAF-TIME`;
- cross-node evidence correlation and causal correlation;
- evidence quality, survivability and accessibility;
- recorder/observer self-health;
- low-coupling observation and observer-effect limits;
- early-boot salvage/crash-loop evidence where applicable.

Recorder-specific APIs, memory layouts and storage mechanisms belong in realization/reference profiles.

### 6.9 `SCAF-SEC` — Security Architecture Interface & Robustness

SCAF does **not** replace a project's cybersecurity/threat/risk authority. When security is applicable, the external/project security authority defines threat assumptions, security objectives, risk acceptance and security-significant project decisions.

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

The **Project Design Authority**, informed by the applicable security authority, defines actual trust boundaries, selected mechanisms and project values. Protocol secure-session mechanics are subordinate realizations/profiles.

### 6.10 `SCAF-CFG` — Configuration & Persistent Operational State

**Defines:**

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
  -> source-owned satisfaction condition
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

SCAF does not require four fields in rc03, but it rejects the assumption that one generic `Owner` is always sufficient.

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

Underlying system-property satisfaction conditions and thresholds are defined by the applicable SCAF concern plus the Project Design Authority; `SCAF-ASSUR` does not redefine them.

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

A project may use several axes at once. Profiles **Realize** system requirements; they do not replace system concern authority.

## 9. Cross-Cutting Authority Matrix

| Topic | SCAF Defines Framework Obligation | Project Defines Instance / Decision | Constrains / Observes | Realizes | Verifies / Dispositions |
|---|---|---|---|---|---|
| Service criticality / consequence | `SCAF-CTX` | project context/service authority | `SCAF-ROB`, safety/security authorities | `SCAF-PROF` | `SCAF-ASSUR`, `SCAF-APP` |
| Node / domain boundary | `SCAF-ARCH` | project architecture authority | `SCAF-ROB`, `SCAF-SEC`, `SCAF-LIFE`, `SCAF-TIME` | `SCAF-PROF` | `SCAF-ASSUR`, `SCAF-APP` |
| Interface freshness semantics | `SCAF-INT`, temporal semantics from `SCAF-TIME` | project interface authority | `SCAF-ROB`, `SCAF-SEC` | `SCAF-PROF` | `SCAF-ASSUR`, `SCAF-APP` |
| Runtime state ownership | `SCAF-RUN` | project state-machine/runtime authority | `SCAF-ROB`, `SCAF-LIFE` | `SCAF-PROF` | `SCAF-ASSUR`, `SCAF-APP` |
| Timebase / synchronization | `SCAF-TIME` | project timing/clock authority | `SCAF-OBS` observes quality | `SCAF-PROF` | `SCAF-ASSUR`, `SCAF-APP` |
| Timing/resource budget | `SCAF-TIME` | project architecture/performance authority | `SCAF-ROB` | `SCAF-PROF` | `SCAF-ASSUR`, `SCAF-APP` |
| Fault containment behavior | `SCAF-ROB` using domain semantics from `SCAF-ARCH` | project robustness/architecture authority | `SCAF-SEC`, `SCAF-LIFE` | `SCAF-PROF` | `SCAF-ASSUR`, `SCAF-APP` |
| Boot/reset/update | `SCAF-LIFE` | project lifecycle/update authority | `SCAF-ROB`, `SCAF-SEC`, `SCAF-CFG`, `SCAF-OBS` | `SCAF-PROF` | `SCAF-ASSUR`, `SCAF-APP` |
| Incident evidence semantics | `SCAF-OBS` | project diagnostic/evidence authority | `SCAF-LIFE`, `SCAF-ROB`, `SCAF-SEC`, `SCAF-TIME` | `SCAF-PROF` | `SCAF-ASSUR`, `SCAF-APP` |
| Configuration lifecycle | `SCAF-CFG` | project configuration authority | `SCAF-LIFE`, `SCAF-SEC`, `SCAF-ROB` | `SCAF-PROF` | `SCAF-ASSUR`, `SCAF-APP` |
| Security architecture interface | `SCAF-SEC` | project architecture authority informed by security authority | `SCAF-ROB`, `SCAF-INT`, `SCAF-TIME`, `SCAF-LIFE` | `SCAF-PROF` | `SCAF-ASSUR`, `SCAF-APP` |

## 10. Tabletop Architecture Validation

These exercises are not full project analyses. They test whether the rc03 metamodel requires ad-hoc taxonomy exceptions.

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

This exercise goes beyond representability and tests the project-start decision/evidence chain for the PC + multiple MCU archetype. Values are illustrative project decisions, not normative SCAF defaults.

| Concern | Applicability / consequence | Required decision | Project Design Authority output | Verification / evidence | Re-evaluation trigger |
|---|---|---|---|---|---|
| `SCAF-CTX` system boundary | Applicable; unclear boundary creates ownership gaps | define PC app, MCU A/B, external operator and external services in/out of scope | controlled system-context diagram + scope statement | architecture review evidence | new external service / deployment boundary |
| `SCAF-CTX` service dependency | Applicable; supervisor loss may affect configuration/visibility but not necessarily local control | define which services depend on PC vs remain autonomous | service dependency model + consequence-of-loss table | scenario review against loss of N1 | change in service criticality or autonomy |
| `SCAF-ARCH` Node/domain boundaries | Applicable; shared reset/power/fault assumptions can cause hidden coupling | define N1/N2/N3 Nodes and fault/reset/power/security domains | architecture allocation/domain diagram | review against Node boundary test and failure scenarios | hardware/deployment topology change |
| `SCAF-INT` freshness | Applicable; stale telemetry may mislead operator | define age/ordering validity contract for each telemetry class | interface/data contract with stale behavior | injected delay/drop/reorder test + trace | rate/transport/UI behavior change |
| `SCAF-TIME` timebase | Applicable; cross-node timeout/evidence correlation depends on clock semantics | define monotonic clocks, synchronization source, allowed uncertainty | project timing/time-domain decision | clock drift/sync-loss test + recorded uncertainty | clock source, sync protocol or tolerance change |
| `SCAF-ROB` partial failure | Applicable; one MCU may fail while peer remains healthy | define containment, degraded service, retry/failover/recovery limits | robustness decision + failure response state model | fault injection / peer-loss scenarios | new shared resource or recovery mechanism |
| `SCAF-LIFE` update | Applicable; mixed versions can create incompatible behavior | define update order, compatibility window, activation and rollback | multi-node update/rollback design | interrupted-update and version-skew test evidence | protocol/version/update mechanism change |
| `SCAF-CFG` configuration authority | Applicable; conflicting writes can corrupt coordinated behavior | define authoritative owner, version, atomicity and resync rules | configuration ownership/migration contract | power-loss/update/reconnect persistence tests | new config source or schema version |
| `SCAF-OBS` incident correlation | Applicable; faults may span nodes | define correlation ID, boot/session identity, time provenance and export path | diagnostic/evidence architecture | cross-node incident reconstruction exercise | logging/timebase/reset architecture change |
| `SCAF-SEC` trust boundary | Applicable when PC/external link is exposed; compromise may propagate | security authority defines objectives; project architecture defines trust boundary and containment | security-context reference + architecture constraint decision | security review / negative-input / privilege evidence as applicable | threat model, external exposure or credential model change |
| `SCAF-ASSUR` closure | Applicable to all selected concerns | define verification method and evidence sufficiency for each source-owned condition | project verification plan linked to concern + design artifact | accepted evidence record / unresolved anomaly record | failed verification, design change, new risk |

**Observed startup loop:** the first scan pass produces provisional CTX/ARCH decisions. Those decisions then change the scope and dependencies used by later concerns, so the scan must re-enter CTX/ARCH rather than run once as a linear checklist.

**Result:** the current state dimensions and authority chain can carry an end-to-end project-start exercise without inventing a new status category or allowing `SCAF-APP` to become the project architecture authority.

### 10.5 Tabletop conclusion

The rc03 metamodel can describe all three representative archetypes **without adding an ad-hoc top-level taxonomy branch**.

The three architecture exercises establish representability; the worked Archetype B scan additionally demonstrates a provisional project-start operating model. Independent review and remaining migration-evidence work are still required before the normative rewrite gate opens.

## 11. Current Rewrite Gate

Do **not** start large-scale normative content production yet.

rc03 closes the rc02 blocking authority ambiguity by separating SCAF normative authority from Project Design Authority and demonstrates one worked Framework Scan. Remaining gate conditions are:

1. independent review of the rc03 authority semantics and worked scan;
2. deeper audit of Gen1 Draft/RC donors used for core SCAF semantics;
3. extraction/reconciliation of durable invariants from schemas/tests/validators before declaring Gen1 migration complete;
4. immutable/retrievable donor snapshot references sufficient for independent source-semantic re-review;
5. confirmation that security/timebase/CTX-vs-ARCH boundaries remain stable under review.

If these converge without a new Critical architecture ambiguity, the next gate may move to **controlled normative rewrite** rather than further taxonomy expansion.
