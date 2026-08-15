# Document Role Analysis

## 1. Purpose

This document analyzes Gen1 by **authority family and engineering role**, rather than merely summarizing filenames. The complete per-file list is in `01_Gen1_Repository_Inventory.md`.

## 2. Root Governance and Repository Control

### `README.md`

Role: repository entry point, operating model, document-domain routing, engineering flow, authority boundary, repository structure and validation entry point.

Assessment:

- valuable as navigation and authority-routing precedent;
- too tightly coupled to Gen1's Coordinator / Node / Protocol / Coding Rules directory model;
- should be rewritten after SCAF taxonomy converges.

### `authority-registry.yaml`

Role: machine-readable mapping between document, version, status, repository role, authority topics, applicability and prerequisite documents.

Assessment:

- one of Gen1's strongest governance concepts;
- solves authority collision and task-routing problems;
- should survive conceptually;
- current entries and paths cannot be copied because the SCAF authority graph will change.

### Legal / contribution / protection files

`LICENSE`, `NOTICE.md`, `CONTRIBUTING.md`, `legal-baseline.yaml`, `third-party-materials.yaml`, `.github/CODEOWNERS`, and `.github/REPOSITORY_PROTECTION.md` collectively control ownership, legal baseline, third-party material, contribution and external repository trust.

Assessment:

- legal and provenance control remains useful;
- GitHub/path-specific enforcement is repository governance, not Framework taxonomy;
- keep the concerns, decouple them from early architecture work.

## 3. Master Framework Family

### `Coordinator_Node_Control_Framework.md`

Role: Gen1 master architecture authority.

Major content:

- Coordinator / Node roles and relative role relationships;
- system layering and responsibility boundaries;
- node identity, capability, registry and lifecycle;
- single-node and multi-node topology;
- protocol/transport separation and protocol source of truth;
- control plane / data plane, streaming, timing and bandwidth;
- queue/buffer policy and stale data;
- transport profiles and link management;
- secure sessions, authentication, authorization, replay and rekey;
- firmware update, bootloader, resume, rollback and safe state;
- RTOS / bare-metal, ISR/callback, static memory, BSP/HAL/driver boundaries;
- configuration, persistence, diagnostics, validation and governance.

Assessment:

This is the largest Gen1 concept donor. It should **not** be renamed and reused unchanged. Its durable concepts should be decomposed into SCAF system concerns. `Coordinator` becomes a role; `embedded` becomes an implementation profile rather than the Framework boundary.

### `Framework_Application_Analysis_Template.md`

Role: method for applying Gen1 to a new project.

Major content:

- product/application identity and context;
- project constraints and evidence quality;
- framework reuse classification;
- protocol inputs;
- responsibility matrix;
- functional analysis;
- timing, bandwidth, topology and resource analysis;
- lifecycle and state ownership;
- error, recovery, safety and security analysis;
- firmware update and bootloader decisions;
- acceptance evidence and conformance gates.

Assessment:

This is the direct ancestor of SCAF **Framework Scan / Applicability Analysis**. It is valuable but too large, partly duplicate with validation checklists, and organized around applying existing Gen1 modules. SCAF should rewrite it as a taxonomy-driven scan where each concern can produce applicability, risk, decision, verification and evidence obligations.

### `AI_Engineering_Usage_Guide.md`

Role: AI task routing, source authority, artifact state, handoff, review, evidence state and human approval.

Assessment:

Useful governance material, but subordinate to the engineering framework. It should not determine the top-level system taxonomy. It may later become an Engineering Process / AI-Assisted Engineering profile.

## 4. Protocol Family

### Definition Guide + Template

`Protocol_YAML_Definition_Guide.md` and `Protocol_YAML_Template.md` jointly define a machine-readable/human-readable/testable protocol contract, registry structure, node model, wire format, transport-neutral semantics, code generation and review expectations.

Strengths:

- single source of truth;
- product semantics separated from wire representation;
- protocol separated from transport;
- version domains explicitly separated;
- multi-node targeting represented in machine-readable form;
- evolution, code generation and validation treated as first-class concerns.

SCAF disposition:

- preserve as **Interface & Data Contract** capabilities;
- do not assume every system interface is a Host/Device command protocol;
- expand contract model to include memory-mapped, shared-memory, streaming, event, IPC, FPGA register, DMA, RPC and other interaction styles where applicable;
- reduce duplication between guide, giant template and review checklist.

### Compatibility, Registry and Security

These three documents provide specialized authority for compatibility/evolution, identifier governance and secure-session behavior.

Assessment:

All remain valuable, but they should become cross-cutting interface-contract concerns. Security robustness must also extend beyond secure session mechanics to availability, abuse resistance, credential failure, fail-secure/fail-safe decisions and recovery.

## 5. Coordinator Family

The Coordinator documents cover software architecture, concurrency, logging, testing and UI engineering.

Strengths:

- clear layering and replaceable presentation boundary;
- per-node context and isolation;
- async/cancellation/backpressure/concurrency ownership;
- structured diagnostics and correlation;
- simulator, race, conflict and multi-node tests;
- stale-state and immutable operation targeting in UI.

SCAF issue:

`Coordinator` is a useful role but not a universal top-level class. A PC process may be a coordinator in one relationship and a subordinate node in another. A SoC may supervise MCUs while itself being controlled by a service system. FPGA logic may participate without having a conventional UI/application architecture.

Disposition:

- merge general principles into System/Node/Interaction/Runtime/Observability concerns;
- keep UI-specific material as an optional Human-Machine Interface implementation/profile document;
- keep desktop concurrency and logging specialization in an implementation profile rather than system core.

## 6. Node Family

`Node_Software_Engineering_Rules.md` defines Node-side layering, identity, targeting, lifecycle, resource ownership, safety, telemetry, diagnostics, bootloader handoff and testing.

Assessment:

- useful core donor for node ownership and isolation;
- current emphasis is software realization;
- SCAF Node must also describe FPGA/DSP/SoC/hardware-assisted nodes and nodes split across heterogeneous compute domains;
- therefore the document should be rewritten into a technology-neutral System / Function / Service / Capability / Node architecture model with implementation profiles below it.

## 7. Coding Rules Family

### Embedded C

Large, detailed rules for product-owned Embedded C, including memory, arithmetic, pointer use, state machines, ISR/callback, RTOS, protocol and review behavior.

### C#

Large, detailed rules for product-owned C#/.NET implementation, including types, nullability, APIs, collections, errors, async/cancellation, time, paths and UI-related boundaries.

Assessment:

Both are valuable but are **implementation authorities**, not system architecture authorities. SCAF should retain them as profiles or linked companion standards. The system Framework should specify the property to achieve (bounded memory, deterministic ownership, safe arithmetic, explicit concurrency, etc.); language-specific rules explain how that property is achieved in a given implementation.

## 8. Validation / Evidence Family

### `Validation_Evidence_Guide.md`

Defines evidence types, evidence state, identity, traceability, reproducibility, environment/tool identification, anomaly handling, retention and integrity.

Assessment: high-value SCAF donor. Evidence should be connected directly to Framework Scan decisions, verification obligations and runtime incident evidence.

### Conformance / Protocol / Coding / Repository checklists

Role: operationalize the authorities into review gates.

Assessment:

- useful evidence of how Gen1 translated principles into checks;
- current checklist boundaries mirror Gen1 documents and therefore should not define SCAF taxonomy;
- regenerate narrower checklists after SCAF concept authority is stable.

### AI artifact validation

Role: prevent fabricated evidence, stale inputs, hallucinated APIs, self-approval and unverified generated artifacts.

Assessment: retain as engineering-process governance, not system core.

## 9. Schema / Examples / Tools / Tests

Gen1 includes:

- protocol schema;
- conformance-claim schema and example;
- positive and negative protocol fixtures;
- protocol, repository and external-anchor validators;
- regression tests;
- CI workflow.

Assessment:

This demonstrates a mature intent: rules should eventually become machine-verifiable where practical. However, these files are strongly coupled to Gen1 paths, schemas, authority names and claim model. They are **not** part of the frozen v0.0.1 baseline; future tooling remains gated on executable-invariant extraction and stable SCAF machine-readable contracts.

The durable SCAF principle is:

> A stable human authority should precede the schema; a stable schema should precede validators; validators should precede CI enforcement.

## 10. Supplemental Crash Recorder

Role: low-coupling incident evidence and recovery architecture.

Major concept donors:

- first-abnormal-state / first-corruption localization;
- probe layering and invariants;
- first-fault latch separate from timeline ring;
- breadcrumbs and operation context;
- task / ISR / fatal writer separation;
- recorder memory isolation and compile-out behavior;
- build identity, timestamp and ordering;
- recorder self-health and degraded mode;
- retained RAM vs persistent evidence;
- torn-write protection and transactional persistence;
- early-boot salvage;
- crash-loop detection;
- reset taxonomy, watchdog evidence and boot epoch;
- evidence quality vs survivability vs accessibility;
- observer-effect audit;
- known-root-cause validation.

Assessment:

These concepts fill a major Gen1 gap in **diagnostic survivability** and **postmortem evidence quality**. Recorder-specific APIs, record layouts and 10 KiB retained-RAM suggestions belong in implementation/reference profiles, not universal SCAF rules.

## 11. Role Analysis Conclusion

Gen1 should be treated as a rich concept repository rather than a directory template. The strongest reusable ideas are responsibility ownership, machine-readable contracts, protocol/transport separation, explicit lifecycle/state, bounded concurrency/resources, update/rollback, evidence governance and multi-node isolation.

The largest structural change required for SCAF is to put these ideas under a **system concern taxonomy** rather than under `coordinator`, `node`, `protocol`, `coding-rules`, and `validation` as largely parallel document domains.


## 12. Metamodel Correction Retained in rc03

The rc1 role analysis correctly identified the need to move beyond Coordinator/Device framing, and the subsequent independent review/convergence work showed that a Node-only generalization is still insufficient.

Therefore source concepts are now re-homed against a broader metamodel:

```text
System
Function / Service / Capability
Node
Role
Interface
Interaction
Cross-cutting Domain
```

A source document can contribute to several of these entities or concerns. A physical `device` is not automatically a Role, and a chip/process is not automatically a Node. The migration mapping in `03_Gen1_to_Gen2_Concept_Mapping.md` is the current authority for those dispositions.
