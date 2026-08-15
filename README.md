# System Control Architecture Framework (SCAF)

**Version:** v0.0.1rc02  
**Status:** Architecture / taxonomy convergence release candidate  
**Date:** 2026-08-15

System Control Architecture Framework (**SCAF**) is a system-level architecture and decision framework intended to reduce design omission, unclear responsibility, fault propagation, poor diagnosability, unrecoverable behavior, and unverifiable design decisions.

SCAF is the successor to the Gen1 `host-device-control-framework`. The term **Gen2** is retained only as lineage / migration context and is not the long-term framework name.

## Meaning of “Control”

In SCAF, **Control** does **not** mean control theory and does **not** mean only host-to-device control.

It refers to system-level coordination and architectural control concerns such as:

- responsibility and authority;
- functions, services and dependencies;
- runtime behavior and state;
- interaction and interface contracts;
- lifecycle and configuration;
- timing, concurrency, capacity and resource control;
- fault handling, robustness and resilience;
- boot, power, reset and update behavior;
- observability, diagnostics and incident evidence;
- security robustness;
- verification, evidence and project application.

## Source Position

Three inputs are kept distinct in this RC:

1. **Gen1 formal baseline** — `host-device-control-framework`.
2. **Supplemental resilience source** — `Embedded_Incident_Crash_Recorder_Framework`.
3. **Independent architecture review** — used as review evidence and correction input, not as a normative Framework source.

The supplemental source is not retroactively treated as Gen1 content. SCAF mapping preserves source provenance and source maturity.

## RC02 Architecture Position

v0.0.1rc02 responds to the v0.0.1rc1 independent architecture review by separating several dimensions that rc1 had mixed together.

SCAF now distinguishes five authority planes:

```text
Framework / Governance Plane
        ↓ governs
System Concern Plane
        ↓ instantiated by
Project Application Plane
        ↓ produces obligations for
Assurance / Evidence Plane
        ↓ verified against realizations in
Realization / Implementation Plane
```

Supporting tooling and AI-assisted engineering are **not** peer system-taxonomy branches. They are downstream/supporting mechanisms.

## Core Metamodel

The core model is no longer `System -> Node -> Role` alone.

```text
System
 ├─ Function / Service / Capability
 ├─ Node
 │   └─ Role(s) in context
 ├─ Interface
 ├─ Interaction
 └─ Domain
     ├─ Fault
     ├─ Reset
     ├─ Power
     ├─ Security
     └─ Resource
```

Important constraints:

- a **Node is an architectural responsibility / lifecycle / interaction entity**, not automatically a chip, process, board or device;
- physical, deployment, reset, fault, power and security boundaries may align with a Node but are not synonyms for Node;
- a Node may contain subordinate Nodes when the subordinate entities have independent architectural obligations;
- a **Role** is contextual responsibility, not a containment child class;
- `Coordinator`, `controller`, `gateway`, `supervisor`, and similar terms may be roles when their responsibility semantics are defined;
- `device` is not automatically treated as a role because it may only describe a physical/deployment category;
- MCU, PC, SoC, FPGA and DSP are realization technologies, not top-level architecture classes.

## Authority Grammar

To avoid duplicate authority, SCAF uses explicit relation language:

- **Defines** — primary normative authority for the concept.
- **Constrains** — adds required conditions without taking over primary ownership.
- **Realizes** — implementation/profile mechanism used to satisfy a system property.
- **Observes** — supplies runtime visibility or incident evidence about a property.
- **Verifies** — demonstrates that an obligation or property is satisfied.
- **Dispositions** — records a project-specific applicability/decision state without becoming the normative source.

## Robustness / Resilience Position

SCAF no longer models robustness as one linear `Prevention -> Detection -> Containment -> Recovery` lifecycle. It separates:

**Fault / error / failure semantics**

```text
Fault source / condition
  -> activation
  -> erroneous state
  -> propagation
  -> service failure
  -> system consequence
```

**Runtime resilience response**

```text
Detect
  -> isolate / contain
  -> tolerate / mask / reconfigure
  -> fail over / degrade / safe action
  -> recover / repair
  -> resynchronize / reintegrate
```

**Assurance**

```text
Prevent / avoid
Analyze
Inject
Verify coverage
Collect and preserve evidence
```

## Framework Scan / Applicability Analysis

Framework Scan is a project-start engineering mechanism, not the source of SCAF obligations.

```text
SCAF Concern / Obligation
        ↓
Project Applicability
        ↓
Failure Consequence / Risk
        ↓
Required Design Decision
        ↓
Implementation Responsibility
        ↓
Verification Obligation
        ↓
Evidence
        ↓
Closure / Deviation
        ↓
Re-evaluation Trigger
```

Applicability, decision, risk, verification and evidence are separate state dimensions. Their exact enums remain provisional in this RC.

## Repository Content

| File | Purpose |
|---|---|
| `docs/00_Input_Baseline.md` | Input identity, provenance, review input and analysis boundary |
| `docs/01_Gen1_Repository_Inventory.md` | Complete Gen1 and supplemental file inventory with artifact disposition |
| `docs/02_Document_Role_Analysis.md` | Role and content analysis by source document family |
| `docs/03_Gen1_to_Gen2_Concept_Mapping.md` | Source-anchored Gen1/supplemental -> SCAF concept mapping |
| `docs/04_Overlap_Obsolescence_and_Gap_Analysis.md` | Duplicate authority, outdated framing, overlap and unresolved gaps |
| `docs/05_SCAF_Taxonomy_Proposal.md` | SCAF authority planes, metamodel, concern taxonomy and tabletop validation |
| `docs/06_Read_Coverage_Audit.md` | Read coverage, mapping confidence and deferred deep-audit record |
| `CHANGELOG.md` | RC history |

The filenames retain `Gen2` where they describe migration lineage. The framework name in normative-facing prose is SCAF.

## CI / Automation Position

**No CI is included in v0.0.1rc02.**

No validator, schema, test fixture or copied Gen1 workflow is introduced. Gen1 tooling remains evidence of useful machine-verifiable intent, but executable enforcement must follow stable SCAF authority boundaries and stable machine-readable contracts.

Preferred order remains:

```text
Human authority
   -> stable machine-readable contract
   -> validator
   -> regression tests
   -> CI enforcement
```

## Release Policy

Discussion and iterative releases use RC versions. A non-RC version is created only after an explicit **freeze** decision.

Current sequence:

```text
v0.0.1rc1
v0.0.1rc02
```

## Current Gate

v0.0.1rc02 is still a convergence RC, not permission for large-scale normative rewriting.

Before the rewrite gate is opened, the remaining evidence work includes deeper source-semantic reconciliation and independent review of the rc02 authority model. The three representative tabletop archetypes in `docs/05_SCAF_Taxonomy_Proposal.md` are used to test whether the metamodel can represent single-MCU, PC+multi-MCU, and heterogeneous SoC/FPGA/DSP systems without ad-hoc taxonomy exceptions.
