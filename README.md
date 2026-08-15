# System Control Architecture Framework (SCAF)

**Version:** v0.0.1rc05  
**Status:** Authority-kernel cleanup / controlled normative rewrite baseline release candidate  
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
- security architecture interfaces and robustness;
- verification, evidence and project application.

## Source Position

Four input classes are kept distinct in this RC:

1. **Gen1 formal baseline** — `host-device-control-framework`.
2. **Supplemental resilience source** — `Embedded_Incident_Crash_Recorder_Framework`.
3. **Independent architecture reviews** — correction evidence, not normative Framework sources.
4. **SCAF-new architecture decisions** — concepts introduced because the donor set does not provide sufficient system-level authority.

The supplemental source is not retroactively treated as Gen1 content. SCAF mapping preserves source provenance and source maturity.

## RC05 Architecture Position

v0.0.1rc05 is a thin **authority-kernel cleanup RC** following the rc04 independent review. Architecture discovery and top-level taxonomy expansion remain closed. This RC canonicalizes the remaining authority-plane, time/session identity, satisfaction-basis and migration-trace semantics before controlled L1/L2 normative content is expanded.

### Canonical authority model

There is one canonical authority direction:

```text
SCAF framework side                                      Project side

Framework / Governance
  governs SCAF authority semantics, sources,
  precedence and change/release rules
           |
           v
SCAF Concern Authority -> Project Design Authority -> Project Realization -> Assurance
          \_______________________________________________________________/
                    SCAF-APP cross-cut trace / disposition

Project Design Authority and Project Realization are project-side authorities/artifacts
constrained by applicable SCAF obligations; they are not governed as organizational
authorities by SCAF Framework / Governance.
```

Interpretation:

- **SCAF Concern Authority** defines framework semantics, obligations and required project decisions.
- **Project Design Authority** defines the actual project-specific boundary, topology, allocation, threshold, state or selected architecture decision.
- **Project Realization** implements the project decision using applicable technologies and mechanisms.
- **Assurance** verifies the applicable obligation, project decision and realization, and judges evidence sufficiency without redefining the underlying system property.
- **SCAF-APP / Framework Scan** cross-cuts the chain by recording applicability, decision, risk, deviation, verification, evidence, closure and re-evaluation trace. It is not a sequential delivery stage and does not become the project architecture authority.
- **Project Design Authority** is a project-side decision authority, not a sixth SCAF framework plane. Authoritative project artifacts (architecture specifications, interface contracts, configuration decisions, etc.) record its decisions but are not themselves the authority role.
- **Framework / Governance** governs SCAF normative sources, authority semantics, precedence and change/release rules. It does **not** govern project organization, Project Design Authority or Project Realization; those project-side authorities are constrained by applicable SCAF obligations.

Supporting tooling and AI-assisted engineering are **not** peer system-taxonomy branches.

## Core Metamodel

The core model is not `System -> Node -> Role` alone.

```text
System
 ├─ Function / Capability
 ├─ Service
 ├─ Node
 ├─ Interface
 ├─ Interaction
 └─ Domain
     ├─ Fault
     ├─ Reset
     ├─ Power
     ├─ Security / Trust
     ├─ Resource
     └─ Clock / Time

Node --plays--> Role (in context)
System/Node --has--> Capability
System/Node --provides/consumes--> Service
Interaction --connects--> participants
Interface --realizes--> interaction boundary
```

Key distinctions:

- **Function** — intended behavior or transformation contributing to a system objective.
- **Capability** — an ability of a System or Node to perform a function under stated conditions.
- **Service** — behavior or utility exposed by a provider to one or more consumers under a defined provider/consumer contract.
- **Node** — an architectural responsibility/lifecycle/interaction entity, not automatically a chip, process, board or device.
- **Role** — contextual responsibility, not a containment child class.
- **Domain** — a cross-cutting reasoning boundary that may align with, subdivide or cross Node boundaries.

A **subordinate System** has its own explicitly bounded system scope and may have its own SCAF application. A **subordinate Node** remains an architectural entity inside the current System scope. If a subordinate System is represented as a participant/Node at a parent-system level, that abstraction and trace relation must be explicit; the two scopes are not silently interchangeable.

MCU, PC, SoC, FPGA and DSP remain realization technologies, not top-level architecture classes.

## Authority Grammar

To avoid duplicate authority, SCAF uses explicit relation language:

- **Defines Framework Semantics / Obligation** — SCAF concern authority defines the concept, required consideration, constraint, or required project decision.
- **Defines Project Instance / Decision** — the designated Project Design Authority defines the actual project-specific boundary, topology, allocation, threshold, state, or selected architecture value.
- **Constrains** — adds required conditions without taking over primary ownership.
- **Realizes** — implementation/profile mechanism used to satisfy a system property.
- **Observes** — supplies runtime visibility or incident evidence about a property.
- **Verifies** — demonstrates that an applicable obligation, project decision, or realization is satisfied.
- **Dispositions** — records project applicability/decision/risk/deviation/closure trace without becoming SCAF normative authority or Project Design Authority.

Bare `Defines` is intentionally avoided in authority declarations when it could confuse framework semantics with project-instance design.

## Robustness / Resilience Position

SCAF does not model robustness as one linear `Prevention -> Detection -> Containment -> Recovery` lifecycle. It separates:

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

**Design-time prevention / avoidance**

Prevention and avoidance are architecture/design/realization strategies owned by the applicable source concerns and Project Design Authority; they are not Assurance-owned runtime stages.

**Assurance**

```text
Analyze
Inject
Verify coverage
Evaluate evidence sufficiency
Verify observer effect / failure response
```

No additional top-level robustness taxonomy is planned at this stage. Watchdog, heartbeat, CRC, ECC, redundancy mechanisms, retained RAM and similar techniques belong to later obligation/pattern/realization layers rather than new top-level concerns.

## Concern Boundary Rules

Several intentionally cross-cutting topics have explicit primary-authority partitions:

- **ROB vs LIFE** — `SCAF-LIFE` defines lifecycle transaction/state semantics for boot, power, reset and update. `SCAF-ROB` defines the required fault-response/tolerance/recovery behavior when lifecycle operations fail or propagate faults.
- **ROB vs OBS** — `SCAF-ROB` defines failure/health decision semantics and resilience behavior. `SCAF-OBS` defines how health/diagnostic/evidence information is observed, represented, preserved and exported.
- **ROB vs ASSUR** — `SCAF-ROB` defines resilience obligations; `SCAF-ASSUR` defines how those obligations are verified and what evidence is sufficient.
- **Security Authority vs Project Design Authority** — project/external security authority defines threat assumptions, security objectives, security risk evaluation/acceptance and externally imposed security constraints. Project Design Authority integrates those constraints into actual trust boundaries, allocations, mechanisms and architecture values. A security team may also act as Project Design Authority for a decision, but that is one explicit role, not a second competing design authority.

## Framework Scan / Applicability Analysis

Framework Scan is a project-start and architecture-change engineering mechanism, not the source of SCAF obligations.

```text
Initial project framing
        ↓
SCAF Concern / Obligation
        ↓
Applicability + Consequence / Risk
        ↓
Required Design Decision
        ↓
Project Design Authority
        ↓
Project Realization
        ↓
Applicable Satisfaction Basis
        ↓
Verification + Evidence
        ↓
Closure / Deviation recorded by SCAF-APP
        ↓
Re-evaluation Trigger / re-scan
```

Applicability, decision, risk, verification and evidence are separate state dimensions. Closure is not owned by `SCAF-ASSUR`: Assurance verifies/evaluates evidence; the authority that owns the underlying requirement, project design decision, risk acceptance or deviation accepts the relevant closure, while `SCAF-APP` records the disposition and trace.

The worked scan in `docs/05_SCAF_Taxonomy_Proposal.md` now carries complete state/authority/closure traces for selected concerns instead of using a broad row count as proof.

## Repository Content

| File | Purpose |
|---|---|
| `docs/00_Input_Baseline.md` | Input identity, provenance, review input and analysis boundary |
| `docs/01_Gen1_Repository_Inventory.md` | Complete Gen1 and supplemental file inventory with artifact disposition |
| `docs/02_Document_Role_Analysis.md` | Role and content analysis by source document family |
| `docs/03_Gen1_to_Gen2_Concept_Mapping.md` | Source-anchored Gen1/supplemental -> SCAF concept mapping |
| `docs/04_Overlap_Obsolescence_and_Gap_Analysis.md` | Duplicate authority, outdated framing, resolved coverage, remaining promotion/audit gaps and rewrite priorities |
| `docs/05_SCAF_Taxonomy_Proposal.md` | SCAF authority planes, metamodel, concern taxonomy and tabletop validation |
| `docs/06_Read_Coverage_Audit.md` | Read coverage, mapping confidence and deferred deep-audit record |
| `CHANGELOG.md` | RC history |

The filenames retain `Gen2` where they describe migration lineage. The framework name in normative-facing prose is SCAF.

## CI / Automation Position

**No CI is included in v0.0.1rc05.**

No validator, schema, test fixture or copied Gen1 workflow is introduced. Gen1 tooling remains evidence of useful machine-verifiable intent, but executable enforcement must follow stable SCAF authority boundaries and stable machine-readable contracts.

Preferred order remains:

```text
Human semantic authority
   -> controlled normative content
   -> stable machine-readable contract
   -> validator
   -> regression tests
   -> CI enforcement
```

## Release Policy

Discussion and iterative releases use RC versions. A non-RC version is created only after an explicit **freeze** decision.

Current sequence:

```text
v0.0.1rc1   # historical first RC spelling
v0.0.1rc02
v0.0.1rc03
v0.0.1rc04
v0.0.1rc05
```

The historical `rc1` tag/name is retained as released. From `rc02` onward this line uses two-digit RC numbering for consistency.

## Current Gate

v0.0.1rc05 preserves the closed architecture-discovery phase and serves as the cleaned authority-kernel baseline for **controlled normative rewrite**.

Permitted initial rewrite scope:

- the authority kernel and normative language;
- the core metamodel and stable concern boundaries;
- SCAF-new architecture semantics that have passed architecture review;
- high-confidence Gen1 **Baseline** donor concepts after source-anchor/maturity confirmation;
- project-application and assurance semantics that preserve the canonical authority chain.

Not yet permitted as frozen SCAF authority without additional audit:

- Draft/RC donor-derived requirements that have not been reconciled;
- invariants known only through schemas, validators or executable fixtures and not yet extracted;
- claims of completed Gen1 migration;
- normative freeze / non-RC release;
- broad implementation rulebooks, final schemas, validators or CI enforcement.

Donor source identity is available, but immutable/retrievable donor snapshot locators remain pending. This is a **migration/promotion gate**, not a reason to reopen the SCAF taxonomy.
