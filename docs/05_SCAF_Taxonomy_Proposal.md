# SCAF Taxonomy Proposal

## 1. Purpose

This document defines the **v0.0.1rc02 conceptual architecture** for System Control Architecture Framework (SCAF).

It is intentionally not a final file/directory plan. The purpose is to stabilize ontology, authority and application semantics before large-scale normative rewriting.

## 2. Scope of “System Control”

SCAF concerns system-level coordination, runtime behavior, interaction, lifecycle, robustness and related architecture decisions.

**Control does not mean control theory and does not mean only host-to-device control.**

Control theory, signal processing or motor-control algorithms may be relevant project domains, but they are outside SCAF unless they create architecture obligations covered by SCAF concerns such as timing, interaction, lifecycle, robustness, evidence or safety interfaces.

## 3. Authority Planes

rc1 mixed several ontology planes into one branch list. rc02 separates them.

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
- `SCAF-SEC` Security Robustness;
- `SCAF-CFG` Configuration & Persistent Operational State.

### Plane C — Project Application

Purpose: instantiate SCAF against a project and record decisions.

Primary concern:

- `SCAF-APP` Framework Scan / Applicability Analysis.

This plane **Dispositions** SCAF concerns for a project. It does not become the source authority for the underlying SCAF obligation.

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
- Resource Domain.

Projects may add domain types when justified.

## 5. Authority Relation Grammar

Cross-cutting does not mean duplicate authority.

| Relation | Meaning |
|---|---|
| **Defines** | Primary normative owner of the concept/property |
| **Constrains** | Adds conditions/limits to a concept owned elsewhere |
| **Realizes** | Implements a required property through a technology/profile mechanism |
| **Observes** | Provides runtime visibility/evidence about a property |
| **Verifies** | Demonstrates satisfaction of an obligation/property |
| **Dispositions** | Records project-specific applicability/decision/exception status |

A topic should have one primary definition authority, even if several concerns constrain/observe/verify it.

## 6. System Concern Taxonomy

### 6.1 `SCAF-CTX` — System Context, Mission, Function & Service

**Defines:**

- system boundary and external actors;
- intended mission/use cases/operating modes;
- assumptions/constraints/unknowns;
- Function / Service / Capability model;
- provider/consumer/dependency relationships;
- service criticality and consequence of loss;
- required degraded service levels where project-defined;
- project safety/security context references.

Does **not** own project disposition records; `SCAF-APP` dispositions applicability.

### 6.2 `SCAF-ARCH` — System / Node / Role / Domain Architecture

**Defines:**

- Node boundaries and hierarchy;
- role assignments and role relativity;
- responsibility/authority ownership;
- topology;
- capability placement;
- shared-resource ownership;
- Fault/Reset/Power/Security/Resource domain boundaries;
- dependency architecture;
- aggregation/composition.

Implementation technology is not part of the core Node definition.

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

Specialized lifecycle authorities remain in `SCAF-LIFE`, `SCAF-CFG`, `SCAF-INT` and `SCAF-SEC`.

### 6.5 `SCAF-TIME` — Timing, Concurrency, Capacity & Resource Margin

**Defines:**

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
- time provenance / clock source;
- synchronization quality/uncertainty where available;
- cross-node correlation and causal correlation;
- evidence quality, survivability and accessibility;
- recorder/observer self-health;
- low-coupling observation and observer-effect limits;
- early-boot salvage/crash-loop evidence where applicable.

Recorder-specific APIs, memory layouts and storage mechanisms belong in realization/reference profiles.

### 6.9 `SCAF-SEC` — Security Robustness

**Defines / constrains:**

- trust boundaries and assets;
- peer identity/authentication/authorization;
- confidentiality/integrity where required;
- anti-replay and hostile freshness;
- key/credential lifecycle;
- privilege separation;
- malformed/hostile input;
- resource-abuse resistance;
- compromised-node containment;
- secure boot/update linkage;
- security-service failure and secure recovery;
- security incident evidence requirements.

Protocol secure-session mechanics are subordinate realizations/profiles.

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
Project Decision / Deviation
        ↓
Implementation Responsibility
        ↓
Verification Obligation
        ↓
Evidence
```

A Framework Scan cannot silently create or delete a SCAF requirement. It records project-specific disposition and may create **project obligations** such as a required design decision, risk treatment, verification activity or evidence item.

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
Concern
  -> scope
  -> applicability
  -> failure consequence / risk
  -> design decision
  -> responsibility
  -> verification obligation
  -> acceptance criteria
  -> evidence
  -> closure / deviation
  -> re-evaluation trigger
```

### 7.4 Ownership is not necessarily singular

A project may need distinct:

- Decision Owner;
- Implementation Owner;
- Verification Owner;
- Risk Acceptance Owner.

SCAF does not require four fields in rc02, but it rejects the assumption that one generic `Owner` is always sufficient.

## 8. Assurance and Realization Planes

### 8.1 `SCAF-ASSUR` — Verification, Fault Injection & Evidence

**Defines:**

- verification obligation types;
- acceptance criteria;
- review/test/analysis/inspection evidence;
- evidence identity, traceability and reproducibility;
- fault-injection assurance;
- coverage claims;
- observer-effect verification;
- unresolved anomaly handling;
- conformance/deviation evidence.

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
7. **Reference subsystem / pattern** — e.g. incident recorder reference architecture.

A project may use several axes at once. Profiles **Realize** system requirements; they do not replace system concern authority.

## 9. Cross-Cutting Authority Matrix

| Topic | Defines | Constrains / Observes | Realizes | Verifies / Dispositions |
|---|---|---|---|---|
| Service criticality / consequence | `SCAF-CTX` | `SCAF-ROB`, safety/security project authorities | `SCAF-PROF` | `SCAF-ASSUR`, `SCAF-APP` |
| Node / domain boundary | `SCAF-ARCH` | `SCAF-ROB`, `SCAF-SEC`, `SCAF-LIFE` | `SCAF-PROF` | `SCAF-ASSUR`, `SCAF-APP` |
| Interface freshness semantics | `SCAF-INT` | `SCAF-TIME`, `SCAF-ROB`, `SCAF-SEC` | `SCAF-PROF` | `SCAF-ASSUR`, `SCAF-APP` |
| Runtime state ownership | `SCAF-RUN` | `SCAF-ROB`, `SCAF-LIFE` | `SCAF-PROF` | `SCAF-ASSUR`, `SCAF-APP` |
| Timing/resource budget | `SCAF-TIME` | `SCAF-ROB` | `SCAF-PROF` | `SCAF-ASSUR`, `SCAF-APP` |
| Fault containment behavior | `SCAF-ROB` using domains from `SCAF-ARCH` | `SCAF-SEC`, `SCAF-LIFE` | `SCAF-PROF` | `SCAF-ASSUR`, `SCAF-APP` |
| Boot/reset/update | `SCAF-LIFE` | `SCAF-ROB`, `SCAF-SEC`, `SCAF-CFG`, `SCAF-OBS` | `SCAF-PROF` | `SCAF-ASSUR`, `SCAF-APP` |
| Incident evidence semantics | `SCAF-OBS` | `SCAF-LIFE`, `SCAF-ROB`, `SCAF-SEC` | `SCAF-PROF` | `SCAF-ASSUR`, `SCAF-APP` |
| Configuration lifecycle | `SCAF-CFG` | `SCAF-LIFE`, `SCAF-SEC`, `SCAF-ROB` | `SCAF-PROF` | `SCAF-ASSUR`, `SCAF-APP` |
| Project applicability | SCAF concern authority defines source obligation | `SCAF-APP` dispositions project state | project implementation | `SCAF-ASSUR` verifies evidence |

## 10. Tabletop Architecture Validation

These exercises are not full project analyses. They test whether the rc02 metamodel requires ad-hoc taxonomy exceptions.

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

### 10.4 Tabletop conclusion

The rc02 metamodel can describe all three representative archetypes **without adding an ad-hoc top-level taxonomy branch**.

This is useful architecture evidence, but it is not enough by itself to open the normative rewrite gate. Remaining migration-evidence and independent-review work is recorded in `06_Read_Coverage_Audit.md`.

## 11. Current Rewrite Gate

Do **not** start large-scale normative content production yet.

Recommended gate conditions:

1. independent review of rc02 authority planes/metamodel;
2. resolution of any new Critical authority ambiguity;
3. deeper audit of Gen1 Draft/RC donors used for core SCAF semantics;
4. extraction of durable invariants from schemas/tests/validators before declaring Gen1 migration complete;
5. agreement that Framework Scan lifecycle can drive real project decisions rather than merely populate a checklist.

Only after these converge should SCAF expand into formal normative authority documents.
