# Gen1 to SCAF Concept Mapping

## 1. Mapping Principle

Mapping is performed by **concept**, not by filename or Gen1 directory. One source artifact may contribute to several SCAF concerns, and one SCAF concern may merge concepts from several Gen1 documents plus supplemental sources.

This RC separates two questions that rc1 mixed together:

1. **Disposition** — what happens to the source artifact/concept in migration?
2. **Transformation** — how must the concept change in abstraction or structure?

## 2. Disposition Vocabulary

| Disposition | Meaning |
|---|---|
| `Keep` | Preserve substantially unchanged as a SCAF concept/artifact role |
| `Move` | Preserve but relocate under a different SCAF authority |
| `Merge` | Consolidate with overlapping concepts into one authority |
| `Rewrite` | Preserve intent but replace framing / responsibility model substantially |
| `Retire` | Do not carry the source artifact/concept forward as an independent SCAF authority |
| `New` | New SCAF concept required because no source provides sufficient authority |

Transformation terms such as `Generalize`, `Elevate`, `Split`, `Specialize`, and `Rebuild` are **not** dispositions.

## 3. Source-Maturity Vocabulary

| Source maturity | Meaning in migration |
|---|---|
| `Baseline` | Accepted Gen1 baseline donor |
| `Draft for Review` | Useful donor, but not silently promoted to accepted Gen1 baseline semantics |
| `Specification RC` | Supplemental RC donor; generic architecture may be adopted after SCAF review |
| `Repository artifact` | Tool/schema/test/governance evidence; semantics may need extraction before migration |
| `SCAF New` | New architecture decision introduced by SCAF |

## 4. Target Concern IDs

| ID | Concern |
|---|---|
| `SCAF-GOV` | Framework Governance & Authority |
| `SCAF-CTX` | System Context, Mission, Function & Service |
| `SCAF-ARCH` | System / Node / Role / Domain Architecture |
| `SCAF-INT` | Interfaces, Interaction & Data Contracts |
| `SCAF-RUN` | Runtime Behavior, State & Lifecycle |
| `SCAF-TIME` | Timing, Concurrency, Capacity & Resource Margin |
| `SCAF-ROB` | Robustness & Resilience |
| `SCAF-LIFE` | Boot, Power, Reset & Update Lifecycle |
| `SCAF-OBS` | Observability, Diagnostics & Incident Evidence |
| `SCAF-SEC` | Security Robustness |
| `SCAF-CFG` | Configuration & Persistent Operational State |
| `SCAF-APP` | Project Application / Framework Scan |
| `SCAF-ASSUR` | Verification, Fault Injection & Evidence |
| `SCAF-PROF` | Realization / Implementation Profiles |

## 5. Source-Anchored Core Mapping

`Anchor` uses source headings as stable human-readable trace points. Line numbers are deliberately not the primary anchor because source edits can shift lines without changing section identity.

| Concept | Source document | Anchor | Source maturity | SCAF target | Disposition | Transformation | Confidence | Deep audit |
|---|---|---|---|---|---|---|---|---|
| System architecture baseline | `Coordinator_Node_Control_Framework.md` | Part I §1.1–1.4 Framework Position / System Layers / Layer Responsibilities | Baseline v1.1.7 | `SCAF-ARCH` | Rewrite | Generalize beyond Coordinator/embedded framing | High | Partial |
| Control-role authority | `Coordinator_Node_Control_Framework.md` | §1.6 Control Role and State Authority; §2.2–2.4 Coordinator/Node/Role Relativity | Baseline v1.1.7 | `SCAF-ARCH` | Merge | Convert fixed classes to contextual Role semantics | High | Partial |
| Role relativity | `Coordinator_Node_Control_Framework.md` | §2.4 Role Relativity | Baseline v1.1.7 | `SCAF-ARCH` | Keep | Elevate to core metamodel | High | Partial |
| Node identity / capability | `Coordinator_Node_Control_Framework.md` | §2.8 Node Identity and Capability; §2.11.1–2.11.3 | Baseline v1.1.7 | `SCAF-ARCH` | Merge | Separate Node identity from address/route/session and from physical device identity | High | Partial |
| Single/multi-node topology | `Coordinator_Node_Control_Framework.md` | §2.11 Single-Node and Multi-Node Architecture Baseline | Baseline v1.1.7 | `SCAF-ARCH` | Keep | Generalize to hierarchical/heterogeneous systems | High | Partial |
| Per-node isolation | `Coordinator_Node_Control_Framework.md` | §2.11.2 Per-Node Context and Isolation | Baseline v1.1.7 | `SCAF-ARCH`, `SCAF-ROB` | Move | Split architecture domain definition from fault/runtime containment behavior | High | Partial |
| Function / service model | `Framework_Application_Analysis_Template.md` | §6.2 Services; §8 Functional Analysis | Baseline v1.1.9 | `SCAF-CTX` | Rewrite | Elevate service/function/dependency to first-class system model | High | Partial |
| System context / operating modes | `Framework_Application_Analysis_Template.md` | §3.3 System Context; §3.4 Scope; §3.5 Operating Modes | Baseline v1.1.9 | `SCAF-CTX` | Keep | Generalize | High | Partial |
| Project responsibility matrix | `Framework_Application_Analysis_Template.md` | §7.1–7.4 Responsibility Boundary | Baseline v1.1.9 | `SCAF-APP`, `SCAF-ARCH` | Rewrite | Separate framework authority from project disposition/ownership | High | Partial |
| Framework application analysis | `Framework_Application_Analysis_Template.md` | §1.3 Expected Outputs; §1.4 Decision Criteria; §5 Framework Application Map | Baseline v1.1.9 | `SCAF-APP` | Rewrite | Rebuild as multi-axis Framework Scan lifecycle | High | Partial |
| Protocol single source of truth | `Protocol_YAML_Definition_Guide.md` | §1.1 Single Source of Truth; §1.2 Machine-Readable, Human-Readable, and Testable | Baseline v1.1.7 | `SCAF-INT` | Keep | Generalize from protocol-only contract to interface/data contracts | High | Partial |
| Product semantics vs representation | `Protocol_YAML_Definition_Guide.md` | §1.3 Product Semantics and Wire Format Shall Be Separated | Baseline v1.1.7 | `SCAF-INT` | Keep | Generalize | High | Partial |
| Protocol vs transport separation | `Protocol_YAML_Definition_Guide.md` | §1.4 Transport-Neutral Contract; framework §3.7 Protocol and Transport Decoupling | Baseline v1.1.7 | `SCAF-INT` | Keep | Apply to broader interaction technologies | High | Partial |
| Message/event/stream semantics | `Protocol_YAML_Definition_Guide.md` | §8 Message Model; §10 Telemetry and Streaming | Baseline v1.1.7 | `SCAF-INT` | Keep | Extend to IPC/shared memory/register/DMA/RPC where applicable | High | Partial |
| Compatibility / evolution | `Protocol_Compatibility_Rules.md` | Part II §5–10; Part III §11–15; Part IV §16–19 | Draft for Review v1.1.0 | `SCAF-INT` | Move | Generalize to versioned interfaces while preserving protocol specialization | Medium | Deferred |
| Identifier / namespace governance | `Protocol_YAML_Definition_Guide.md`; `Protocol_Registry_Governance.md` | Guide §5 Namespace, Service, and ID Allocation; Registry authority sections | Baseline + Draft | `SCAF-INT`, `SCAF-GOV` | Merge | Split namespace rules from repository governance | Medium | Deferred |
| Secure-session mechanics | `Protocol_Security_Profile.md` | Secure session / authentication / replay / rekey sections | Draft for Review v1.1.0 | `SCAF-SEC`, `SCAF-INT` | Move | Security defines constraints; protocol profile realizes mechanics | Medium | Deferred |
| Timing budget | `Coordinator_Node_Control_Framework.md` | Part IV §4.3–4.5 Sample/Record Period, Timing Budget, Bandwidth Budget | Baseline v1.1.7 | `SCAF-TIME` | Move | Elevate to system temporal correctness | High | Partial |
| Queue / bounded backpressure | `Coordinator_Node_Control_Framework.md`; `Coordinator_Concurrency_Guide.md` | Framework §4.7 Queue and Buffer Policy; Concurrency §6 Bounded Queues and Backpressure | Baseline + Draft | `SCAF-TIME`, `SCAF-ROB` | Merge | Separate capacity definition from overload resilience response | High | Partial |
| Concurrency ownership | `Coordinator_Concurrency_Guide.md` | §2 Explicit Concurrency Model; §3 Thread and State Ownership; §8 Timeout Ownership; §9 Synchronization | Draft for Review v1.1.0 | `SCAF-TIME`, `SCAF-PROF` | Merge | Core states required ownership; profiles realize mechanisms | Medium | Deferred |
| Stale data / freshness | `Coordinator_Node_Control_Framework.md`; UI guidance | Framework §4.9 Stale Data | Baseline v1.1.7 | `SCAF-INT`, `SCAF-TIME`, `SCAF-ROB`, `SCAF-SEC` | Merge | One semantic owner plus explicit cross-concern constraints | High | Partial |
| Link/reconnect behavior | `Coordinator_Node_Control_Framework.md`; `Protocol_Compatibility_Rules.md` | Framework §5.6 Link Management State Machine; Compatibility §15 Reconnect and Reconciliation | Baseline + Draft | `SCAF-ROB`, `SCAF-INT` | Merge | Generalize communication failure/recovery/partition handling | High | Partial |
| Boot / reset / recovery | `Node_Software_Engineering_Rules.md` | §24 Reset Cause and Recovery; §25 Startup Sequence; §26 Shutdown and Power Transition | Draft for Review v1.1.0 | `SCAF-LIFE` | Move | Generalize beyond software Node | Medium | Deferred |
| Firmware update | `Coordinator_Node_Control_Framework.md`; Node Rules | Framework §2.11.8 Firmware Update Coordination; Node §38–40.1 | Baseline + Draft | `SCAF-LIFE` | Merge | System lifecycle authority across heterogeneous nodes | High | Partial |
| Configuration ownership | `Node_Software_Engineering_Rules.md`; Application Analysis | Node §34 Configuration Ownership; Application §8.2 Configuration | Draft + Baseline | `SCAF-CFG` | Merge | Create explicit configuration lifecycle authority | High | Partial |
| Persistent operational state | `Node_Software_Engineering_Rules.md` | §35 Persistent State | Draft for Review v1.1.0 | `SCAF-CFG`, `SCAF-LIFE` | Move | Separate operational persistence from incident evidence persistence | Medium | Deferred |
| Local safety / degraded state | `Node_Software_Engineering_Rules.md` | §19 Local Safety Ownership; §20 Fault Classification; §22 Degraded and Safe States | Draft for Review v1.1.0 | `SCAF-ROB` | Rewrite | Require project safety/hazard authority for safety-significant Safe State definition | Medium | Deferred |
| Fault injection | `Node_Software_Engineering_Rules.md` | §43 Fault Injection | Draft for Review v1.1.0 | `SCAF-ASSUR` | Move | Treat as assurance, not runtime fault lifecycle | Medium | Deferred |
| Evidence model | `Validation_Evidence_Guide.md` | Part I Evidence Model; Part III Identity/Traceability/Reproducibility; Part IV Result/Review Control | Draft for Review v1.1.0 | `SCAF-ASSUR` | Merge | Connect evidence to SCAF concern/decision/verification trace | Medium | Deferred |
| Runtime operational logs | `Coordinator_Logging_Guide.md` | logging identity/correlation/structured diagnostic sections | Draft for Review v1.1.1 | `SCAF-OBS`, `SCAF-PROF` | Merge | Core defines observability intent; implementation profile realizes logging | Medium | Deferred |
| First-abnormal-state localization | Crash Recorder `README.md` | Part A §A4–A8 Probe Layers / First-Fault Latch / Timeline / Breadcrumbs | Specification RC v1.0.1rc03 | `SCAF-OBS`, `SCAF-ROB` | Merge | Generalize evidence objective; keep recorder mechanics subordinate | High | Partial |
| Evidence survivability | Crash Recorder `README.md` | Part B §B8–B18 Evidence State/Persistence/Crash Loop; Part E Evidence Quality vs Survivability | Specification RC v1.0.1rc03 | `SCAF-OBS`, `SCAF-LIFE` | Merge | Generalize survival classes and boot salvage | High | Partial |
| Reset cause / boot epoch | Crash Recorder `README.md` | §B31 Reset Cause as Evidence; §B32 Boot Epoch | Specification RC v1.0.1rc03 | `SCAF-LIFE`, `SCAF-OBS` | Merge | Generalize correlation semantics | High | Partial |
| Observer effect | Crash Recorder `README.md` | §A23 Observer-Effect Audit; §B37 Observer-Effect Audit | Specification RC v1.0.1rc03 | `SCAF-ASSUR`, `SCAF-OBS` | Merge | Elevate diagnostic self-interference as assurance obligation | High | Partial |
| Evidence accessibility/export | Crash Recorder `README.md` | §B13 Automatic Export; §B14 Manual UI Role; §B15–B16 Export Failure/Completion | Specification RC v1.0.1rc03 | `SCAF-OBS`, `SCAF-PROF` | Move | Define accessibility intent; keep media/UI mechanics in profiles | High | Partial |
| Fault/error/failure semantic chain | — | — | SCAF New | `SCAF-ROB` | New | Introduce explicit condition→activation→error→propagation→service failure→consequence model | High | New |
| Fault-tolerance mechanisms | — | — | SCAF New | `SCAF-ROB` | New | Add redundancy/failover/reconfiguration/repair/resynchronization/reintegration | High | New |
| Cross-cutting domains | Gen1 isolation/reset/security/resource concepts | Multiple anchors above | Mixed | `SCAF-ARCH` | Rewrite | Model Fault/Reset/Power/Security/Resource domains independently of Node | High | Partial |
| Distributed incident time provenance | Crash Recorder timestamp/boot-epoch concepts + SCAF extension | A16 Timestamp and Ordering; B32 Boot Epoch | Supplemental + SCAF New | `SCAF-OBS` | Rewrite | Add synchronization quality, uncertainty and causal correlation across Nodes | High | Partial |
| Implementation rulebooks | C# / Embedded C rules | Full language authorities | Baseline + Draft | `SCAF-PROF` | Move | Keep language/runtime mechanisms outside system concern authority | High | Deferred |
| Machine-verifiable governance | schemas/tools/tests/workflow | repository artifacts | Repository artifact | `SCAF-GOV`, `SCAF-ASSUR` | Retire | Rebuild only after stable human authority and machine contracts | High | Deferred |

## 6. Cross-Concern Authority Examples

A concept can cross several concerns without creating duplicate authority when the relation is explicit.

### Freshness

- `SCAF-INT` **Defines** data-age / ordering / validity contract semantics.
- `SCAF-TIME` **Constrains** temporal budgets and measurable age limits.
- `SCAF-ROB` **Constrains** behavior when freshness guarantees are lost.
- `SCAF-SEC` **Constrains** anti-replay / hostile-staleness behavior where security-relevant.
- `SCAF-ASSUR` **Verifies** the applicable obligations.

### Containment

- `SCAF-ARCH` **Defines** containment-domain boundaries and ownership.
- `SCAF-ROB` **Defines/Constrains** runtime behavior under fault propagation across those boundaries.
- `SCAF-SEC` **Constrains** behavior under malicious or compromised-node propagation.
- `SCAF-PROF` **Realizes** the required mechanisms.
- `SCAF-ASSUR` **Verifies** containment properties.

### Incident Evidence

- `SCAF-OBS` **Defines** required evidence semantics and accessibility.
- `SCAF-LIFE` **Constrains** survivability across reset/boot/power transitions.
- `SCAF-ROB` **Constrains** what failures/effects must be observable.
- `SCAF-PROF` **Realizes** retention/persistence/export mechanisms.
- `SCAF-ASSUR` **Verifies** evidence quality and observer-effect limits.

## 7. Artifact Disposition vs Concept Disposition

A source artifact can have several concept outcomes. Example:

```text
Coordinator_Software_Engineering_Rules.md
    general layering / ownership concepts -> Merge into SCAF core concerns
    desktop async mechanisms              -> Move to realization profiles
    Coordinator-only taxonomy             -> Retire as top-level classification
    original artifact as SCAF authority   -> Retire / replace later
```

Therefore the complete file inventory remains an **artifact-level preliminary disposition**, while this document is the more important **concept-level migration map**.

## 8. Migration Evidence Status

The mapping above is strong enough for architecture convergence, but it is **not yet a requirement-by-requirement migration baseline**.

Remaining work includes:

- deep audit of Gen1 Draft/RC donors before any semantics are promoted as normative SCAF requirements;
- extraction of invariants encoded only in schemas, validators and negative/positive test fixtures;
- contradiction review where multiple source authorities cover the same topic;
- final target authority IDs after taxonomy freeze.

The correct current interpretation is:

> **source-anchored migration hypothesis with explicit confidence and audit state**, not final migration proof.
