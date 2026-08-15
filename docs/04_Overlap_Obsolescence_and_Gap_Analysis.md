# Overlap, Obsolescence, Responsibility Overlap, and Gap Analysis

## 1. Summary

Gen1 is content-rich but structurally mature around its own history. Gen2 should correct four different classes of problem:

1. **duplicate or distributed authority**;
2. **Gen1-specific framing that is no longer the right abstraction**;
3. **responsibility overlap between architecture, implementation and verification**;
4. **system resilience gaps that are missing or only implicit**.

## 2. Major Overlaps

### 2.1 Master Framework vs Specialized Protocol / Security / Update Rules

The master Framework contains substantial normative detail on protocol, security, firmware update, runtime and implementation boundaries while specialized documents also govern those areas.

Risk:

- same topic can evolve in two places;
- “one rule, one authority” becomes harder to maintain;
- reviewers need routing knowledge before they can know which wording wins.

Gen2 direction:

- master architecture defines concern boundaries and mandatory decisions;
- topic authorities define detailed normative behavior;
- implementation profiles define realization rules.

### 2.2 Application Analysis vs Conformance Checklists

The application template already asks many architecture, timing, topology, recovery, security and validation questions. Framework/Protocol/Coding checklists ask related questions again.

Gen2 direction:

Use one **Framework Scan record** as the source of applicability and obligation. Specialized checklists are generated/referenced views of that record rather than separate competing decision inventories.

### 2.3 Protocol Guide vs Protocol Template

Both are very large and include structural guidance, examples and review expectations.

Gen2 direction:

- concise normative interface-contract model;
- separate reusable template/example;
- machine schema only after model stability.

### 2.4 Coordinator Rules vs Coordinator Topic Guides

Architecture, concurrency, logging, testing and UI have valid specialization, but responsibilities overlap with the master Coordinator rules and master Framework.

Gen2 direction:

General rules go to System/Node/Runtime/Observability; role-specific desktop/HMI patterns remain profiles.

### 2.5 Validation Evidence vs Incident Evidence

These are different kinds of evidence:

- **engineering assurance evidence** proves a design/verification claim;
- **runtime incident evidence** survives a system failure and supports diagnosis.

They should share identity, provenance, integrity and retention principles but must not be conflated.

## 3. Outdated or Too-Narrow Framing

### 3.1 Host / Device and Coordinator / Node as structural anchors

Gen1 already recognizes role relativity, which is a strong foundation. Gen2 should complete that idea: roles are assigned to Nodes for an interaction or responsibility; they do not define the entire system taxonomy.

### 3.2 “Cross-Platform Embedded Control” as Framework boundary

The existing master document already includes PC, Linux SBC, mobile app and service-tool cases, but its title and many implementation discussions remain embedded-centric.

Gen2 must natively support:

- MCU;
- PC;
- SoC;
- FPGA;
- DSP;
- heterogeneous systems;
- mixed runtime and hardware/software partitions.

### 3.3 Software-only Node engineering

An FPGA node may have clocks, reset domains, CDC, register interfaces, FIFOs, watchdog/status logic and fault containment without conventional tasks, heap, exceptions or source-code layering. A DSP may have real-time pipeline constraints distinct from a desktop coordinator.

Therefore Node engineering must be technology-neutral at core and technology-specific below it.

## 4. Responsibility Boundary Problems to Correct

| Problem | Gen1 Pattern | Gen2 Correction |
|---|---|---|
| System requirement vs implementation rule | Framework and coding guides both mention bounded memory/concurrency | Core defines required property; profile defines realization |
| Protocol security vs system security | secure-session details dominate security material | security robustness covers system assets, availability, privilege, failure and recovery; protocol crypto is a profile |
| Diagnostics vs logging | logging is strongest on Coordinator side | observability model applies to every relevant node and interaction |
| Recovery ownership | reconnect, update rollback, errors and boot recovery are separate | one recovery lifecycle with domain-specific mechanisms |
| Verification ownership | several checklist families | scan item creates explicit verification/evidence obligation |
| Node isolation | mostly multi-node coordinator concern | explicit containment domain across system architecture |

## 5. Gen2 Gaps

### 5.1 Fault Model and Fault Lifecycle

Gen1 has error handling and many defensive rules but lacks one system-level lifecycle connecting:

```text
Prevent
  -> Detect
  -> Contain
  -> Escalate
  -> Recover / Degrade / Enter Safe State
  -> Diagnose
  -> Preserve Evidence
  -> Verify
```

This should become a core Gen2 model.

### 5.2 Runtime Health Monitoring

Needed decisions include:

- what health means for each node/service/interface;
- local vs system health ownership;
- heartbeat/checkpoint semantics;
- liveness vs correctness vs freshness;
- watchdog scope;
- false-positive / false-negative behavior;
- escalation and recovery thresholds;
- health evidence and observability.

### 5.3 Explicit Fault Containment and Propagation Analysis

Per-node isolation exists in Gen1, but Gen2 needs explicit containment domains and propagation paths for:

- shared memory;
- shared bus;
- shared clock/power/reset;
- common storage;
- common services;
- coordinator failure;
- malformed/stale/corrupt data;
- resource exhaustion;
- security compromise.

### 5.4 Graceful Degradation

Gen1 discusses partial results and some safe behavior, but not a unified degradation contract.

Gen2 should ask:

- which service can be lost independently;
- what reduced capability remains;
- how degraded mode is entered/exited;
- whether a degraded state is safe and diagnosable;
- what must be communicated to peer nodes/operators;
- how degraded operation is verified.

### 5.5 Safe State

Safe state must become a defined project decision, not a phrase attached only to firmware update or specific faults.

Required analysis:

- trigger;
- owning node/domain;
- commanded vs autonomous entry;
- power/reset interaction;
- persistence across reboot;
- exit authorization;
- observability;
- verification evidence.

### 5.6 Incident Evidence and First-Abnormal-State

This is the largest gap filled by the supplemental recorder source. Gen2 requires a technology-neutral incident-evidence model with optional retained/persistent implementation profiles.

### 5.7 Boot / Power / Reset as a Full Lifecycle Concern

Gen1 has firmware update and bootloader material, but Gen2 should explicitly analyze:

- cold boot / warm reset / watchdog / brownout / external reset / software reset;
- reset domain interactions;
- initialization order and readiness;
- retained state validity;
- incomplete transaction recovery;
- early-boot fault containment;
- reset cause evidence;
- power-fail boundaries.

### 5.8 Data Integrity and Freshness

Gen1 has safe decoding, stale data and protocol validation. Gen2 should expand this to end-to-end data properties:

- validity;
- completeness;
- age/freshness;
- ordering;
- uniqueness / duplicate handling;
- consistency across replicas/participants;
- integrity during storage and transfer;
- provenance and version;
- invalidation rules;
- recovery after partial update.

### 5.9 Resource Margin and Overload

A budget is not enough. Gen2 should distinguish:

```text
nominal use
worst-case analyzed use
reserved margin
hard capacity
overload behavior
recovery behavior
long-run accumulation
```

Resources can include CPU, memory, stack, queue depth, bandwidth, storage, write endurance, handles, tasks/threads, DMA channels, FPGA logic/memory, power and other project-relevant capacities.

### 5.10 Long-Run Robustness

Not sufficiently first-class in Gen1. Examples:

- memory/resource leaks;
- counter/sequence wrap;
- timestamp rollover;
- log/storage growth;
- flash wear;
- queue drift/accumulation;
- retry storms;
- reconnect loops;
- repeated update/recovery cycles;
- clock drift and stale-state accumulation;
- days/weeks/months soak behavior.

### 5.11 Security Robustness

Gen1 has good protocol security detail, but Gen2 must also consider:

- denial-of-service / resource abuse;
- malformed but authenticated input;
- compromised or untrusted node containment;
- credential expiry/loss/rotation failure;
- security service unavailable;
- secure recovery;
- fail-secure vs fail-operational vs safe-state tradeoff;
- audit evidence.

### 5.12 Fault Injection

Gen1 has negative protocol fixtures and robust testing concepts but lacks a unified system fault-injection method.

Candidate fault classes:

- communication drop/corruption/delay/reorder/duplicate;
- memory corruption / invalid state;
- task/thread stall;
- timing overrun;
- storage failure / torn write;
- power loss / reset;
- resource exhaustion;
- peer disappearance / reboot;
- update interruption;
- security failure;
- sensor/actuator invalidity;
- clock/reset-domain faults where applicable.

### 5.13 Observer Effect

Diagnostics, probes, tracing, health checks and incident recorders can alter timing, memory layout, scheduling or failure behavior. Gen2 should explicitly require observer-effect assessment where instrumentation is non-trivial.

## 6. What Should Not Be Added Yet

v0.0.1rc1 should not create:

- a separate normative document for every gap listed above;
- MCU, PC, FPGA and DSP rulebooks before the core taxonomy stabilizes;
- schemas for an unsettled scan model;
- CI around temporary filenames and directory structures;
- copied Gen1 validators that enforce Gen1 concepts.

## 7. Conclusion

The Gen2 design problem is primarily **authority and abstraction restructuring**, followed by resilience completion. Adding more documents before that restructuring would increase the exact risk the Framework is intended to reduce: duplicated rules and unclear responsibility.
