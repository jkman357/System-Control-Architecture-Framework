# Gen1 to Gen2 Concept Mapping

## 1. Mapping Principle

Mapping is performed by **concept**, not by filename. One Gen1 document may feed several Gen2 authorities, and one Gen2 concern may merge concepts from several Gen1 documents plus supplemental sources.

## 2. Core Mapping

| Concept | Gen1 Source | Supplemental Source | Gen2 Target | Action | Notes |
|---|---|---|---|---|---|
| System architecture baseline | Master Framework | — | System Model & Architecture | **Rewrite** | Remove embedded-only and fixed Coordinator/Node framing |
| Coordinator / Device roles | Master Framework, Coordinator docs, Node rules | — | Node Role Model | **Rewrite** | Coordinator/device/gateway/supervisor become role profiles |
| Role relativity | Master Framework | — | Node Role Model | **Keep / Elevate** | Strong Gen1 idea; becomes central in Gen2 |
| Node identity / capability | Master Framework, Protocol Guide, Registry Governance | — | Node Identity, Capability & Lifecycle | **Merge** | Separate identity/address/route/session remains valid |
| Single-node / multi-node topology | Master Framework, Application Analysis | — | System Topology & Interaction Model | **Keep / Generalize** | Extend to heterogeneous and hierarchical systems |
| Per-node isolation | Master Framework, Coordinator docs | — | Fault / Resource / State Containment | **Move / Elevate** | Treat as system resilience property, not only coordinator design |
| Layering / responsibility boundaries | Framework, Coordinator, Node rules | — | Architecture & Responsibility | **Merge** | One authority; implementation profiles specialize it |
| Protocol single source of truth | Protocol Guide / Template | — | Interface & Data Contract | **Keep / Generalize** | Apply beyond command/response protocols |
| Protocol vs transport separation | Framework, Protocol Guide | — | Interaction Layering | **Keep** | Stable system principle |
| Message / event / stream separation | Framework, Protocol Guide | — | Interaction Semantics | **Keep / Generalize** | Include IPC/shared memory/register/DMA where applicable |
| Compatibility / evolution | Protocol Compatibility Rules | — | Interface Lifecycle & Compatibility | **Move** | No longer protocol-only where versioned interfaces exist |
| Identifier registry | Registry Governance | — | Identity & Namespace Governance | **Move** | Apply to node/interface/event/evidence IDs as appropriate |
| Secure session | Framework, Security Profile | — | Security Robustness | **Merge** | Keep cryptographic/session material as a profile |
| Authentication / authorization | Security Profile | — | Security Robustness | **Move** | Link to safe failure and recovery behavior |
| Replay / counter / rekey | Security Profile | — | Security Profile | **Move** | Specialized protocol security mechanism |
| Control plane / data plane | Framework | — | Interaction & Runtime Architecture | **Keep** | Useful separation where applicable, not mandatory for every node |
| Timing budget | Framework, Application Analysis | — | Timing & Temporal Correctness | **Elevate** | Becomes cross-system concern |
| Bandwidth budget | Framework, Application Analysis | — | Capacity / Resource Margin | **Move** | Include compute, memory, queues, I/O, storage, thermal/power if project-relevant |
| Queue / buffer / backpressure | Framework, Coordinator Concurrency | — | Concurrency & Resource Robustness | **Merge** | Bounded overload behavior becomes resilience concern |
| Stale data | Framework, UI Guide | — | Data Integrity & Freshness | **Elevate** | Expand to validity, age, sequence, provenance and consistency |
| Link management / reconnect | Framework, Coordinator docs | — | Communication Robustness | **Move** | Treat failure/retry/recovery/partition explicitly |
| Wireless specifics | Framework | — | Transport Profile | **Move** | Optional transport specialization |
| Firmware update | Framework, Application Analysis, Security Profile | — | Boot / Update / Rollback | **Merge** | System lifecycle authority, not protocol subtopic |
| Rollback | Framework | — | Recovery + Update | **Elevate** | Connect to health validation and safe activation |
| Safe state during update | Framework | — | Safe State & Degraded Operation | **Merge** | Generalize beyond update |
| RTOS / bare-metal | Framework, Embedded C rules | — | MCU / Embedded Runtime Profile | **Move** | Not core system taxonomy |
| BSP / HAL / driver boundary | Framework, Node / Coding rules | — | Implementation Architecture Profile | **Move** | Applicable mainly to software/embedded nodes |
| Static memory / bounded allocation | Framework, Embedded C rules | recorder static config | Resource Robustness + Embedded C Profile | **Merge** | System property + implementation rule separated |
| C implementation rules | Embedded C Coding Rules | implementation examples | Embedded C Profile | **Move** | Keep detailed rules outside core |
| C# implementation rules | CSharp Coding Rules | — | C#/.NET Profile | **Move** | Keep detailed rules outside core |
| UI engineering | Coordinator UI Guide | — | HMI / Operator Interface Profile | **Move** | Optional node/profile concern |
| Logging | Coordinator Logging Guide | recorder evidence model | Observability / Diagnostics | **Merge** | Separate routine logging from incident evidence |
| Test layering | Coordinator Testing Guide | validation matrix | Verification Strategy | **Merge** | Generalize beyond coordinator |
| Evidence identity / traceability | Validation Evidence Guide | build identity / boot epoch | Verification & Evidence | **Elevate / Merge** | Connect design evidence and runtime evidence without conflating them |
| Framework conformance | Conformance Checklist, claim schema | — | Framework Scan + Conformance | **Rewrite** | Taxonomy-driven claim boundary and evidence obligations |
| Protocol conformance | Protocol Checklist / schema / fixtures | — | Interface Verification | **Move / Rebuild** | Machine-verifiable layer after stable schema |
| Repository validation | Repository checklist / validators / CI | — | Framework Governance Tooling | **Retire / Rebuild later** | Do not make repository structure part of system taxonomy |
| AI task routing / validation | AI guides | — | Engineering Governance | **Move** | Optional process authority |
| Fault prevention | Coding rules, architecture rules, security | low coupling / invariants | Robustness & Resilience | **Merge / Elevate** | Gen1 is fragmented; create explicit system-level concern |
| Fault detection | Errors/diagnostics in several docs | invariants, probes, first-abnormal latch | Fault Detection & Runtime Health | **New authority from merged sources** | Needs unified detection model |
| Runtime health monitoring | Diagnostics fragments | recorder self-health, checkpoints/invariants | Runtime Health Monitoring | **New** | Must cover node/system health, not recorder only |
| Fault containment | Per-node isolation, safety boundaries | failure isolation, degraded recorder | Fault Containment | **Elevate** | Explicit containment domains and propagation paths needed |
| Fault escalation | Error / alarm handling fragments | first-abnormal/fatal distinction | Fault Escalation | **New / Rewrite** | Define escalation criteria, ownership and evidence |
| Recovery | reconnect, rollback, error recovery | boot recovery, salvage, persistence | Recovery | **Merge / Elevate** | Make recovery a lifecycle, not scattered mechanism |
| Graceful degradation | partial results / stale UI / safe update | degraded recorder mode | Graceful Degradation | **New authority** | Need service-level degradation semantics |
| Safe state | safety/update sections | recovery mode boundary | Safe State | **Elevate** | Define trigger, owner, entry/exit, observability and verification |
| Incident evidence | logging / validation evidence only partly related | complete recorder architecture | Diagnostics & Incident Evidence | **New authority from supplemental source** | Keep runtime evidence distinct from design-validation evidence |
| First-abnormal-state | not explicit | strong source | Incident Evidence | **New** | Key diagnostic principle |
| Evidence survivability | not explicit | retained RAM, persistence, torn-write, export | Incident Evidence Survivability | **New** | Include reset/power-loss survivability classes |
| Boot / reset cause evidence | partial boot/update | reset taxonomy, boot epoch, early boot | Boot / Power / Reset | **New / Merge** | Expand lifecycle beyond firmware update |
| Power-loss boundary | limited | explicit persistence boundary | Power / Persistence Robustness | **New** | Needed for state/evidence/data integrity |
| Watchdog behavior | implementation fragments | watchdog integration | Runtime Health & Recovery | **New / Merge** | Policy and evidence both required |
| Data integrity | protocol validation / safe decode | torn-write / completeness metadata | Data Integrity & Freshness | **New authority from merged sources** | End-to-end semantics needed |
| Resource margin | budgets | recorder memory/timing impact | Capacity & Resource Margin | **Elevate** | Include headroom and overload behavior, not just calculated usage |
| Long-run robustness | limited | crash loop, wear budget, retry bounds | Long-Run Robustness | **New** | Include leaks, counters, wear, drift, queue accumulation, repeated recovery |
| Security robustness | security profile | recorder failure isolation indirectly | Security Robustness | **Rewrite / Elevate** | Availability and recovery aspects beyond secure session |
| Fault injection | negative fixtures / tests | known-bug validation | Fault Injection & Adversarial Verification | **New authority** | Systematic fault campaigns absent as top-level method |
| Observer effect | not explicit | explicit audit | Verification & Diagnostics | **New** | Required for probes/health/logging that can perturb behavior |
| Verification evidence | validation docs | recorder validation matrix | Verification & Evidence | **Merge / Elevate** | Tie each applicable concern to evidence requirement |
| Framework application | Application Analysis Template | recorder phased adoption | Framework Scan | **Rewrite** | One scan model spanning architecture + robustness + verification |

## 3. Gen2 Disposition Rules

### Keep

Use when the concept already has the right abstraction and authority boundary. Example: protocol/transport separation.

### Move

Use when the concept is valid but belongs elsewhere in the new taxonomy. Example: C# rules become an implementation profile.

### Merge

Use when several Gen1 documents describe the same system property from different roles. Example: concurrency/resource isolation across Framework, Coordinator and Node documents.

### Rewrite

Use when the concept is important but current wording assumes Gen1 roles, directories, software technology or embedded scope.

### Retire

Use for an artifact that should not exist in Gen2 in its current form. It does not imply that all ideas in that file are discarded.

### New

Use where no sufficient Gen1 authority exists. Supplemental material can reduce the amount of truly new design, but its provenance remains explicit.

## 4. Mapping Conclusion

The highest-value Gen2 transformation is not “Host -> Node” renaming. It is the conversion from a **role/document-domain framework** into a **system-property framework** where roles and implementation technologies are profiles beneath stable system concerns.
