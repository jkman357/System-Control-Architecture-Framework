# Gen2 Taxonomy Proposal

## 1. Status

This taxonomy is a **v0.0.1rc1 proposal**. It is intentionally not frozen and should be used to challenge the mapping before detailed Gen2 normative documents are produced.

## 2. Taxonomy Design Rules

The top level should describe stable **system engineering concerns**, not directory history, programming language, or one product topology.

A concern belongs near the core when it applies across implementation technologies. Technology-specific realization belongs in an implementation profile.

## 3. Proposed Top-Level Model

```text
0. Framework Governance & Authority
1. System Context, Scope & Applicability
2. System / Node / Role Architecture
3. Interfaces, Interaction & Data Contracts
4. Runtime Behavior, State & Lifecycle
5. Timing, Concurrency & Capacity
6. Robustness & Resilience
7. Boot, Power, Reset & Update Lifecycle
8. Observability, Diagnostics & Incident Evidence
9. Security Robustness
10. Implementation Profiles
11. Verification, Fault Injection & Evidence
12. Project Application / Framework Scan
13. Machine-Verifiable Framework & Tooling
14. Engineering Process / AI-Assisted Engineering
```

The numbering is organizational only and is not yet a document numbering commitment.

## 4. Branch Detail

### 0. Framework Governance & Authority

Owns:

- normative language;
- topic authority and precedence;
- version / RC / freeze policy;
- provenance;
- change classification;
- compatibility of Framework authorities;
- legal / contribution / third-party boundaries where repository governance is included.

Gen1 donors: authority registry, README authority boundary, document governance sections, repository protection concepts.

### 1. System Context, Scope & Applicability

Owns:

- system boundary;
- environment and external actors;
- use cases / operating modes;
- constraints / assumptions / unknowns;
- criticality / safety / security context;
- applicability decisions;
- project-specific exclusions and deferrals.

This branch is the entry point for Framework Scan.

### 2. System / Node / Role Architecture

Core model:

```text
System
 ├─ Node A [roles: supervisor, gateway]
 ├─ Node B [roles: controller]
 ├─ Node C [roles: sensing / actuation]
 └─ External System / Operator / Service
```

Owns:

- node boundary and identity;
- role assignment and role relativity;
- responsibility / authority ownership;
- topology and hierarchy;
- capability declaration;
- containment domains;
- lifecycle ownership;
- shared-resource ownership;
- system aggregation.

Implementation technology is intentionally absent from the core model.

### 3. Interfaces, Interaction & Data Contracts

Owns:

- interface identity;
- commands / responses / events / telemetry / streams;
- register/shared-memory/IPC/message interfaces where applicable;
- protocol vs transport separation;
- addressing / routing / targeting;
- compatibility and evolution;
- serialization / representation;
- data validity / freshness / ordering contracts;
- negative behavior;
- interface security requirements;
- machine-readable contract applicability.

Gen1 Protocol YAML remains a major donor but becomes one profile of a broader interface-contract concept.

### 4. Runtime Behavior, State & Lifecycle

Owns:

- state domains;
- state ownership;
- transitions and invariants;
- initialization / readiness;
- normal operation;
- start / stop / suspend / resume;
- connection/session lifecycle;
- service availability;
- cross-node state consistency;
- lifecycle transition evidence where required.

### 5. Timing, Concurrency & Capacity

Owns:

- deadlines / periods / latency;
- jitter / age / freshness limits;
- temporal invariants;
- execution ownership;
- concurrency model;
- synchronization / races;
- queueing / backpressure;
- bandwidth / throughput;
- CPU / memory / stack / storage / logic / channel budgets;
- margin / headroom;
- overload policy;
- starvation / fairness;
- long-duration accumulation.

This branch states system properties; C/RTOS/.NET/FPGA-specific mechanisms belong in profiles.

### 6. Robustness & Resilience

This is a central Gen2 addition.

Recommended lifecycle:

```text
Fault Prevention
      ↓
Fault Detection / Runtime Health
      ↓
Fault Containment
      ↓
Fault Escalation
      ↓
Recovery ── or ── Graceful Degradation ── or ── Safe State
      ↓
Reintegration / Return to Service
```

Cross-cutting subconcerns:

- fault model and fault assumptions;
- fault propagation paths;
- common-cause / shared-resource faults;
- liveness and health monitoring;
- watchdog / supervision;
- communication robustness;
- data integrity and freshness;
- resource exhaustion;
- retry/reconnect storms;
- long-run robustness;
- latent failure;
- recovery limits and retry bounds;
- system-level degraded capability.

### 7. Boot, Power, Reset & Update Lifecycle

Owns:

- power-on / power-off behavior;
- reset taxonomy and reset domains;
- initialization order;
- reset cause;
- retained-state validity;
- brownout / interrupted operation where relevant;
- bootloader / application boundary;
- update transaction;
- authenticity / integrity of update;
- activation / health confirmation;
- resume;
- rollback;
- failed update recovery;
- safe state during update/recovery;
- update coordination across nodes.

This is separated from general robustness because boot/update/reset are major lifecycle planes with dedicated state and evidence requirements, while still linking into resilience.

### 8. Observability, Diagnostics & Incident Evidence

Owns three distinct levels:

1. **Operational observability** — metrics, status, routine logs, counters.
2. **Diagnostics** — fault codes, invariant failures, health state, service data.
3. **Incident evidence** — first-abnormal-state, timeline, fatal context, retained/persistent evidence, export and postmortem correlation.

Key supplemental concepts:

- first abnormal vs final crash;
- separate first-fault snapshot and timeline;
- low-coupling probes;
- evidence quality / survivability / accessibility;
- reset/power survivability classes;
- build identity and boot epoch;
- recorder self-health;
- early-boot salvage;
- crash-loop evidence;
- observer-effect limits.

### 9. Security Robustness

Owns:

- trust boundaries and assets;
- peer identity;
- authentication / authorization;
- confidentiality / integrity where needed;
- anti-replay / freshness;
- key / credential lifecycle;
- privilege separation;
- malformed/hostile input;
- resource-abuse resistance;
- compromised-node containment;
- secure boot/update linkage;
- security-service failure;
- secure recovery;
- security incident evidence.

Protocol secure-session mechanics are subordinate profiles, not the complete security model.

### 10. Implementation Profiles

Examples:

```text
MCU / Bare-Metal Profile
MCU / RTOS Profile
Embedded C Profile
PC / .NET Profile
PC / Native Profile
Linux / SoC Profile
FPGA Profile
DSP / Real-Time Signal Processing Profile
HMI / UI Profile
Transport Profiles
Storage / Persistence Profiles
Incident Recorder Reference Profile
```

A project selects only applicable profiles. Profiles cannot weaken system-level requirements without an explicit deviation/risk decision.

### 11. Verification, Fault Injection & Evidence

Owns:

- verification strategy and level;
- analysis / review / inspection / test evidence;
- objective evidence identity;
- reproducibility and tool/environment identity;
- positive / negative / boundary testing;
- fault injection;
- stress / overload testing;
- reset/power interruption testing;
- long-run / soak testing;
- recovery and degraded-mode testing;
- interoperability / compatibility testing;
- security robustness testing;
- observer-effect audit;
- anomaly handling;
- residual risk / unresolved issue record.

Every `Verification Required` or `Evidence Required` scan result should resolve into this branch.

### 12. Project Application / Framework Scan

This is a primary operational interface to Gen2.

A scan item should be able to record at least:

```text
Concern ID
Question / Design Property
Applicability
Rationale
Risk / Failure Consequence
Owner
Design Decision
Verification Obligation
Evidence Obligation
Status
References
Re-evaluation Trigger
```

Candidate status / disposition vocabulary from the project brief:

- Applicable
- Not Applicable
- TBD / Deferred
- Risk Identified
- Design Decision Required
- Verification Required
- Evidence Required

Important open question for the next RC: these labels mix **applicability**, **risk state**, and **obligation state**. Gen2 may model them as separate fields rather than one flat status enum, while preserving the requested user-facing vocabulary.

### 13. Machine-Verifiable Framework & Tooling

Owns future:

- schemas;
- semantic lint;
- registry validation;
- traceability checks;
- conformance claim structure;
- generated checklists;
- test fixtures;
- repository validation;
- release validation;
- CI integration.

**v0.0.1rc1 intentionally contains none of this implementation.**

### 14. Engineering Process / AI-Assisted Engineering

Owns optional process guidance:

- source authority and trust;
- AI task routing;
- generated artifact status;
- human approval;
- fabricated evidence prohibition;
- work continuity / handoff;
- review severity;
- tool/version provenance.

This branch cannot override system engineering authorities.

## 5. Cross-Cutting Matrices

A pure tree will not be enough. Gen2 should eventually maintain several cross-cutting matrices.

### 5.1 Concern x Node / Interface

Determines where a concern applies.

### 5.2 Fault Lifecycle x System Concern

Example:

| Concern | Prevent | Detect | Contain | Escalate | Recover/Degrade | Evidence | Verify |
|---|---|---|---|---|---|---|---|
| Communication | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| Data integrity | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| Resource exhaustion | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| Update | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| Security | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |

This avoids creating separate disconnected robustness documents for every bullet in the project brief.

### 5.3 Concern x Implementation Profile

Ensures an MCU, PC, SoC, FPGA or DSP profile explains how the same system property is realized without redefining the property.

### 5.4 Concern x Verification / Evidence

Ensures every mandatory design property has a verification route and evidence expectation when required.

## 6. Proposed Authority Shape

Do not immediately create 15 large documents. A likely later structure is:

```text
Core System Framework
Framework Scan / Applicability Method
Interface & Data Contract Authority
Robustness & Resilience Authority
Verification & Evidence Authority
Implementation Profiles (selected, modular)
Engineering Governance (selected, modular)
```

The exact file split remains open. The taxonomy should converge before the file split.

## 7. Taxonomy Exit Criteria

Before moving to large-scale rewrite, confirm that:

- every durable Gen1 concept has a Gen2 home;
- every requested robustness/resilience concern has a Gen2 home;
- no top-level branch exists only because Gen1 had a folder with that name;
- Node roles are not confused with implementation technologies;
- system properties are not duplicated inside implementation profiles;
- verification/evidence obligations can be traced from Framework Scan;
- runtime incident evidence is distinguished from assurance evidence;
- the taxonomy can represent MCU, PC, SoC, FPGA, DSP and heterogeneous systems without exceptions.
