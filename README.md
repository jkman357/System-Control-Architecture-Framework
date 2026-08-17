# System Control Architecture Framework (SCAF)

**Version:** v0.0.4rc05  
**Status:** Authority-Registry Schema & Structural Validator Foundation RC  
**Date:** 2026-08-16

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

Four input classes are kept distinct in this release:

1. **Gen1 formal baseline** — `host-device-control-framework`.
2. **Supplemental resilience source** — `Embedded_Incident_Crash_Recorder_Framework`.
3. **Independent architecture reviews** — correction evidence, not normative Framework sources.
4. **SCAF-new architecture decisions** — concepts introduced because the donor set does not provide sufficient system-level authority.

The supplemental source is not retroactively treated as Gen1 content. SCAF mapping preserves source provenance and source maturity.


## v0.0.4rc05 Executable-Governance Development Position

v0.0.4rc05 opens the separately gated schema + structural-validator stage after the independent v0.0.4rc04 review returned:

```text
V0.0.4 AUTHORITY-REGISTRY RELEASE-STATE CLEANUP GATE: YES
```

The rc04 review resolved `R3-01`, confirmed the accepted rc03 registry and upstream contracts were unchanged, and found no remaining blocker to schema/structural-validator work. rc05 therefore makes the accepted registry contract executable without changing the accepted registry serialization.

Frozen normative Markdown under `docs/normative/` remains canonical semantic authority. Repository-root `authority-registry.yaml` remains the accepted rc03 controlled curated representation and stays byte-identical in rc05, including `representation_release = v0.0.4rc03` for all 294 records.

rc05 adds:

```text
schemas/authority-registry.schema.json
tools/scaf_validator/
```

The schema enforces the accepted ten-field representation shape, exact 294-record population boundary, authorized constants/enumerations, eleven canonical normative source paths, and empty initial `relations`. The executable validator adds source-aware checks for ID uniqueness, bidirectional 294-record source coverage, canonical `source_path`, `source_anchor == id`, exactly-one canonical requirement-heading resolution, and exact source `Target` ↔ `authority_class` fidelity.

The validator is a subordinate conformance check. It cannot override, repair, reinterpret, or complete frozen Markdown semantics and does not infer project applicability, compliance, verification, closure, Pattern selection, or L2→L3 relations.

rc05 also adds focused regression tests for the accepted registry and controlled invalid mutations. It intentionally does **not** add CI enforcement, registry generation, generated reverse indexes/views, code generation, automatic applicability inference, machine-readable L2→L3 relations, new L3 Patterns, M3/M4 or L4 guidance.

The current gate is whether the schema/validator foundation faithfully executes the accepted rc03 registry contract, fails closed on structural/source-fidelity defects, preserves canonical Markdown precedence, and stays within the bounded rc05 scope.


## v0.0.3 Frozen L3 Baseline Position

v0.0.3 is the **Frozen L3 Pattern / Mechanism Catalog Baseline** created by explicit governance freeze decision after the independent v0.0.3rc14 final-navigation closure review returned:

```text
L3 V0.0.3 FREEZE-CANDIDATE CLOSURE GATE: YES
```

The review confirmed `R12-01` **RESOLVED**, opened **0 Critical, 0 Major, 0 Minor and 0 Trivial findings**, preserved the frozen v0.0.2 normative baseline, confirmed exactly twelve published Pattern identities, reproduced 12 / 12 rc13→rc14 Pattern-body non-regression checks, preserved the `FTL-001` trace closure, and found no third-tranche, M3/M4, L4, SEC-primary or executable-governance scope expansion.

The formal v0.0.3 freeze carries forward the reviewed rc14 L3 architecture/trace/lifecycle baseline with **no intended Pattern semantic change**. Pattern current-release metadata advances from `v0.0.3rc14` to `v0.0.3`; the reviewed Pattern mechanism bodies, L2 trace relations, authority boundaries, lifecycle state, identities, families and introduction history remain unchanged.

Frozen L3 catalog state:

```text
12 published Pattern identities
12 x Available / M2 — Architecture Reviewed
Initial tranche: 7 x Introduced In v0.0.3rc03
Second tranche: 5 x Introduced In v0.0.3rc08
```

The frozen v0.0.3 scope includes the reviewed L3 catalog governance, metadata contract, trace/selection model and the twelve current `Available / M2` Pattern entries. `Available` remains bounded to acceptance for project consideration and does not imply project applicability, recommendation, automatic selection, compliance, verification, implementation correctness or L2 satisfaction.

The following remain **outside** the frozen v0.0.3 baseline and require later separately controlled development/gates: third-tranche catalog expansion, the approved-but-deferred EVD export/transformation category, the rejected/reframe PST configuration-activation proposal, SEC-primary realization, M3/M4, L4 implementation/verification guidance, schema, validator, generated registry/reverse index, CI, code generation and executable governance.

**v0.0.3 is frozen and shall not be modified in place.** Any later semantic evolution shall occur on a new RC development line and preserve explicit trace to the frozen v0.0.2 L1/L2 baseline and this frozen v0.0.3 L3 baseline where applicable.

## v0.0.2 Frozen L1/L2 Baseline Position

v0.0.2 is the **Frozen L1/L2 Baseline** created by explicit governance decision after the independent rc15 freeze-candidate audit returned **Yes** with **no Critical, Major, Minor or Trivial issues**, verified the rc15 source SHA-256, confirmed all 294 requirement blocks stable, and found no cross-boundary, identity, source/evidence/closure, Framework Scan, L3/L4 or donor-promotion regression. The frozen baseline preserves the reviewed authority homes, requirement semantics, requirement IDs, Target classes, core metamodel and top-level taxonomy.

Current normative documents are:

- `docs/normative/00_SCAF_Authority_Kernel.md`
- `docs/normative/10_SCAF_CTX_System_Context_Obligations.md`
- `docs/normative/20_SCAF_ARCH_System_Architecture_Obligations.md`
- `docs/normative/30_SCAF_INT_Interface_Interaction_Data_Contract_Obligations.md`
- `docs/normative/40_SCAF_TIME_Timing_Concurrency_Capacity_Obligations.md`
- `docs/normative/50_SCAF_RUN_Runtime_State_Operational_Lifecycle_Obligations.md`
- `docs/normative/60_SCAF_ROB_Robustness_Resilience_Obligations.md`
- `docs/normative/70_SCAF_LIFE_Boot_Power_Reset_Update_Lifecycle_Obligations.md`
- `docs/normative/80_SCAF_OBS_Observability_Diagnostics_Incident_Evidence_Obligations.md`
- `docs/normative/90_SCAF_CFG_Configuration_Persistent_Operational_State_Obligations.md`
- `docs/normative/100_SCAF_SEC_Security_Architecture_Interface_Robustness_Obligations.md`

The complete CTX/ARCH/INT/TIME/RUN/ROB/LIFE/OBS/CFG/SEC L1/L2 authority backbone is now frozen as the upstream architecture baseline. No new concern or normative semantic change is introduced by the freeze action. L3 pattern/mechanism catalogs and L4 implementation/verification guidance remain downstream work and are not part of v0.0.2.

The freeze action introduces no intended normative semantic change. All 294 requirement IDs, 218 Project-Applicable Obligations, 76 Framework Normative Invariants, Target classes, primary authority homes, identity semantics, Framework Scan semantics, verification/evidence/closure semantics and donor-promotion gates are carried forward from rc15.

L3 mechanism catalogs, L4 implementation/verification guidance, schema, validator and CI are not part of this frozen baseline. Formal L3 work may now begin only as downstream specialization that traces to the frozen L1/L2 obligations and does not modify this baseline in place.

Normative precedence for this RC is:

```text
Normative documents under docs/normative/
        ↓
frozen v0.0.1 architecture/taxonomy baseline
        ↓
migration analysis / inventories / historical review material
```

Where a normative v0.0.2 statement intentionally specializes wording from the frozen architecture baseline, the normative document governs the current development line. The frozen v0.0.1 release itself remains unchanged.

## v0.0.1 Frozen Architecture Position

v0.0.1 freezes the reviewed **architecture-convergence / authority-kernel baseline** reached in rc05. Architecture discovery and top-level taxonomy expansion are closed for this baseline. Controlled L1/L2 normative elaboration proceeds in the next development line; the frozen v0.0.1 release is not modified in place.

### Canonical authority model

There is one canonical authority direction:

```text
SCAF framework side                                      Project side

Framework / Governance
  governs SCAF authority semantics, sources,
  precedence and change/release rules
           |
           v
SCAF Concern Authority -> Project Design Authority -> Project Realization -> Project Verification / Assurance Authority
          \_______________________________________________________________/
                    SCAF-APP cross-cut trace / disposition

Project Design Authority is a project-side authority role. Project Realization is a project-side implementation responsibility/activity. Controlled decisions are recorded in authoritative project artifacts. These are distinct concepts and are not organizationally governed by SCAF Framework / Governance.
```

Interpretation:

- **SCAF Concern Authority** defines framework semantics, obligations and required project decisions.
- **Project Design Authority** defines the actual project-specific boundary, topology, allocation, threshold, state or selected architecture decision.
- **Project Realization** implements the project decision using applicable technologies and mechanisms.
- **Project Verification / Assurance Authority** executes/evaluates project verification using `SCAF-ASSUR` semantics and judges evidence sufficiency without redefining the underlying system property.
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

## Normative Target Classes

Normative SCAF statements distinguish two target classes:

- **Project-Applicable Obligation** — enters project applicability/decision/verification/evidence flow when Applicable.
- **Framework Normative Invariant** — governs SCAF authoring, authority semantics, migration/promotion or framework release behavior and is not itself a project Framework Scan obligation.

Being eligible as controlled rewrite input does **not** make donor content eligible for SCAF normative promotion or freeze.

## Authority Grammar

To avoid duplicate authority, SCAF uses explicit relation language:

- **Defines Framework Semantics / Obligation** — SCAF concern authority defines the concept, required consideration, constraint, or required project decision.
- **Defines Project Instance / Decision** — the designated Project Design Authority defines the actual project-specific boundary, topology, allocation, threshold, state, or selected architecture value.
- **Constrains** — adds required conditions without taking over primary ownership.
- **Guides Realization** — framework-side profile/pattern content constrains or informs implementation without becoming the project realization actor.
- **Realizes** — Project Realization implements a Controlled Decision / required property.
- **Observes** — supplies runtime visibility or incident evidence about a property.
- **Verifies** — Project Verification / Assurance Authority demonstrates/evaluates satisfaction using applicable SCAF assurance semantics.
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
- **ROB vs ASSUR** — `SCAF-ROB` defines resilience obligations; `SCAF-ASSUR` defines verification semantics and evidence-sufficiency criteria for those obligations; Project Verification / Assurance Authority evaluates actual project evidence.
- **Security Authority vs Project Design Authority** — project/external security authority defines threat assumptions, security objectives, security risk evaluation/acceptance and externally imposed security constraints. Project Design Authority integrates those constraints into actual trust boundaries, allocations, mechanisms and architecture values. A security team may also act as Project Design Authority for a decision, but that is one explicit role, not a second competing design authority.

## Framework Scan / Applicability Analysis

Framework Scan is a project-start and architecture-change engineering mechanism, not the source of SCAF obligations.

```text
Initial project framing
        ↓
SCAF Concern / Obligation
        ↓
Applicability
        ↓
Consequence / Risk
        ↓
Required Design Decision
        ↓
Project Design Authority
        ↓
Project Realization
        ↓
Applicable Satisfaction Basis
        ↓
Verification
        ↓
Evidence
        ↓
Closure / Deviation recorded by SCAF-APP
        ↓
Re-evaluation Trigger / re-scan
```

Applicability, decision, risk, verification and evidence are separate state dimensions. Closure is not owned by `SCAF-ASSUR`: Assurance verifies/evaluates evidence; the authority that owns the underlying requirement, project design decision, risk acceptance or deviation accepts the relevant closure, while `SCAF-APP` records the disposition and trace.

The worked scan in `docs/05_SCAF_Taxonomy_Proposal.md` carries complete state/authority/closure traces for selected concerns instead of using a broad row count as proof.

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
| `docs/normative/00_SCAF_Authority_Kernel.md` | Normative authority vocabulary, chain, satisfaction/closure and rewrite/promotion gates |
| `docs/normative/10_SCAF_CTX_System_Context_Obligations.md` | L1/L2 System Context / Function / Capability / Service obligations |
| `docs/normative/20_SCAF_ARCH_System_Architecture_Obligations.md` | L1/L2 System / Node / Role / Domain architecture obligations |
| `docs/normative/30_SCAF_INT_Interface_Interaction_Data_Contract_Obligations.md` | L1/L2 Interface / Interaction / data-contract obligations |
| `docs/normative/40_SCAF_TIME_Timing_Concurrency_Capacity_Obligations.md` | L1/L2 timing / timebase / concurrency / capacity / margin obligations |
| `docs/normative/50_SCAF_RUN_Runtime_State_Operational_Lifecycle_Obligations.md` | L1/L2 operational state / transition / readiness / Operational Incarnation obligations |
| `docs/normative/60_SCAF_ROB_Robustness_Resilience_Obligations.md` | L1/L2 fault/error/failure / health / containment / degradation / recovery / resilience obligations |
| `docs/normative/70_SCAF_LIFE_Boot_Power_Reset_Update_Lifecycle_Obligations.md` | L1/L2 boot / power / reset / update / activation / rollback lifecycle obligations |
| `docs/normative/80_SCAF_OBS_Observability_Diagnostics_Incident_Evidence_Obligations.md` | L1/L2 observability / diagnostics / incident-evidence identity / provenance / correlation / preservation obligations |
| `docs/normative/90_SCAF_CFG_Configuration_Persistent_Operational_State_Obligations.md` | L1/L2 configuration / persistent operational-state source / version / migration / commit / rollback / calibration obligations |
| `docs/normative/100_SCAF_SEC_Security_Architecture_Interface_Robustness_Obligations.md` | L1/L2 security architecture interface / trust / identity / authentication / authorization / protection / security robustness obligations |
| `docs/l3/README.md` | L3 development scope, frozen-upstream rule and catalog file map |
| `docs/l3/00_L3_Catalog_Governance.md` | L3 authority boundary, mechanism-family taxonomy, pattern ID, status/maturity and L3/L4 boundary |
| `docs/l3/01_L3_Pattern_Metadata_Contract.md` | Human-readable metadata contract for current and future `SCAF-PAT-*` entries |
| `docs/l3/02_L3_Trace_and_Selection_Model.md` | Many-to-many L2→L3 trace and project pattern-selection semantics |
| `docs/l3/03_L3_Pattern_Index.md` | Human-readable L3 family/pattern navigation index; not trace authority |
| `docs/l3/catalog/README.md` | Catalog family placement and published-identity rules |
| `docs/l3/templates/L3_Pattern_Template.md` | Controlled template for additional pattern entries |
| `authority-registry.yaml` | Accepted rc03 controlled curated machine-readable representation of the 294 frozen L1/L2 normative authority records |
| `docs/executable-governance/README.md` | v0.0.4 executable-governance development scope, order and current gate |
| `docs/executable-governance/00_SCAF_Machine_Readable_Authority_Model.md` | Authority-record source-of-truth, deterministic initial field semantics, identity, classification, completeness and failure semantics |
| `docs/executable-governance/01_SCAF_v0.0.4rc02_Authority_Model_Determinism_Cleanup.md` | rc01 `R1-01` closure record for `layer`, `source_anchor`, `status` and initial `relations` behavior |
| `docs/executable-governance/02_SCAF_v0.0.4rc03_Initial_Authority_Registry_Serialization.md` | Accepted initial 294-record registry serialization format, ownership, reproducibility and gate contract |
| `docs/executable-governance/03_SCAF_v0.0.4rc04_Authority_Registry_Release_State_Documentation_Cleanup.md` | Focused `R3-01` repository-state documentation cleanup and non-regression record |
| `docs/executable-governance/04_SCAF_v0.0.4rc05_Authority_Registry_Schema_and_Structural_Validator_Foundation.md` | Current schema/validator foundation scope, authority boundary, commands, regression contract and review gate |
| `schemas/authority-registry.schema.json` | JSON Schema Draft 2020-12 structural contract for the accepted rc03 ten-field / 294-record representation |
| `tools/scaf_validator/validator.py` | Executable structural + canonical-source fidelity validator |
| `tools/scaf_validator/tests/test_validator.py` | Regression tests for accepted registry and controlled invalid mutations |
| `tools/scaf_validator/README.md` | Validator installation, execution and validation-boundary guidance |
| `CHANGELOG.md` | RC history and frozen release record |

The filenames retain `Gen2` where they describe migration lineage. The framework name in normative-facing prose is SCAF.

## CI / Automation Position

**v0.0.4rc05 adds local schema validation, source-aware structural validation and regression tests, but still introduces no CI enforcement.**

The accepted rc03 `authority-registry.yaml` remains unchanged and subordinate to frozen normative Markdown. The rc05 schema/validator executes the accepted representation contract and fails closed on representation/source inconsistencies; it does not become a competing authority source.

Local commands from repository root:

```text
python -m pip install -r tools/scaf_validator/requirements.txt
python -m tools.scaf_validator.validator
python -m unittest discover -s tools/scaf_validator/tests -v
```

Expected accepted-registry validation summary:

```text
Records:    294
Unique IDs: 294
Source IDs: 294
Project-Applicable Obligations: 218
Framework Normative Invariants: 76
Errors:      0
RESULT: PASS
```

CI merge blocking, generated reverse indexes/views, registry generation, code generation, automatic project applicability inference and machine-readable L2→L3 relations remain later separately gated work.

Preferred order now is:

```text
Human semantic authority
   -> controlled normative content
   -> stable machine-readable authority model
   -> accepted 294-record registry serialization
   -> schema + structural/source-aware validator + regression tests
   -> later CI / generated views / executable governance
```


## Release Policy

Discussion and iterative releases use RC versions. A non-RC version is created only after an explicit **freeze** decision. Frozen releases are not modified in place; semantic work continues on a new RC development line.

Current sequence:

```text
v0.0.1rc1   # historical first RC spelling
v0.0.1rc02
v0.0.1rc03
v0.0.1rc04
v0.0.1rc05
v0.0.1       # frozen architecture-convergence baseline
v0.0.2rc01   # first controlled L1/L2 normative rewrite
v0.0.2rc02   # targeted normative precision correction
v0.0.2rc03   # target/authority precision closure
v0.0.2rc04   # INT + TIME controlled L1/L2 normative tranche
v0.0.2rc05   # targeted INT/TIME authority-boundary closure
v0.0.2rc06   # RUN controlled L1/L2 normative tranche
v0.0.2rc07   # ROB controlled L1/L2 normative tranche + RUN minor closure
v0.0.2rc08   # LIFE controlled L1/L2 normative tranche + ROB minor closure
v0.0.2rc09   # OBS controlled L1/L2 normative tranche + LIFE minor closure
v0.0.2rc10   # CFG controlled L1/L2 normative tranche + OBS minor closure
v0.0.2rc11   # integrated L1/L2 consolidation before SEC
v0.0.2rc12   # SEC controlled L1/L2 normative tranche + parallel minor cleanup
v0.0.2rc13   # final integrated L1/L2 consolidation + SEC minor closure
v0.0.2rc14   # final editorial closure / L1/L2 freeze candidate
v0.0.2rc15   # freeze-candidate release-hygiene closure
v0.0.2       # frozen L1/L2 baseline
v0.0.3rc01   # L3 catalog architecture / contract RC
v0.0.3rc02   # L3 catalog contract cleanup / closure RC
v0.0.3rc03   # first representative Candidate/M1 L3 pattern tranche
v0.0.3rc04   # localized initial-tranche trace cleanup
v0.0.3rc05   # initial-tranche M2 maturity decision; Candidate status retained
v0.0.3rc06   # initial-tranche availability acceptance; seven entries Available / M2
v0.0.3rc07   # L3 trace-reference coverage audit / second-tranche planning; no new Pattern ID
v0.0.3rc08   # controlled second representative tranche; FTL/TIM/SYN Candidate/M1 patterns
v0.0.3rc09   # localized FTL-001 trace-relation cleanup / focused closure RC
v0.0.3rc10   # second-tranche M2 maturity decision; Candidate status retained
v0.0.3rc11   # second-tranche explicit availability acceptance
v0.0.3rc12   # L3 milestone consolidation / freeze-candidate audit
v0.0.3rc13   # focused freeze-candidate release-record cleanup / closure RC
v0.0.3rc14   # final Pattern Index navigation cleanup / freeze-candidate closure RC
v0.0.3       # frozen L3 Pattern / Mechanism Catalog baseline
v0.0.4rc01   # machine-readable authority-model foundation; independent gate YES, AFTER MINOR CLEANUP
v0.0.4rc02   # focused authority-model determinism cleanup; independent gate YES
v0.0.4rc03   # initial 294-record authority-registry serialization; independent gate YES, AFTER MINOR CLEANUP
v0.0.4rc04   # focused authority-registry release-state documentation cleanup for R3-01
v0.0.4rc05   # authority-registry schema + structural/source-aware validator foundation
```

The historical `rc1` tag/name is retained as released. From `rc02` onward this line uses two-digit RC numbering for consistency.


## Current Governance State

The frozen upstream baselines remain:

```text
v0.0.2 — Frozen L1/L2 Baseline
v0.0.3 — Frozen L3 Pattern / Mechanism Catalog Baseline
```

The accepted executable-governance progression is:

```text
v0.0.4rc01 — Authority Model Foundation
              gate: YES, AFTER MINOR CLEANUP
v0.0.4rc02 — Authority Model Determinism Cleanup
              gate: YES
v0.0.4rc03 — Initial 294-Record Authority Registry Serialization
              gate: YES, AFTER MINOR CLEANUP
v0.0.4rc04 — Authority-Registry Release-State Documentation Cleanup
              gate: YES; R3-01 RESOLVED
v0.0.4rc05 — Authority Registry Schema & Structural Validator Foundation
              current validation-foundation RC
```

The rc04 independent review found no open Critical, Major, Minor or Trivial findings and authorized opening the schema/structural-validator stage. rc05 therefore adds only a local structural schema, an executable structural/source-aware validator, dependency/install guidance and focused regression tests against the already accepted rc03 registry contract.

`authority-registry.yaml` remains unchanged from rc03/rc04, including all 294 `representation_release = v0.0.4rc03` values. The accepted authority model, rc02 determinism closure, rc03 serialization record, rc04 release-state cleanup record, frozen `docs/normative/`, and frozen `docs/l3/` remain unchanged.

The immediate independent-review question is whether rc05 faithfully executes those accepted contracts without becoming a competing authority source, without changing the registry population, and without introducing deferred CI/generation/project-inference/L3/M3/M4/L4 scope.

Expected review gate:

```text
V0.0.4 AUTHORITY-REGISTRY SCHEMA-VALIDATOR FOUNDATION GATE: YES / YES, AFTER MINOR CLEANUP / NO
```

A `YES` accepts only the schema + structural/source-aware validator foundation and authorizes planning a later separately controlled executable-governance step. It does not automatically authorize CI enforcement, code generation, registry generation, generated indexes/views, automatic project applicability inference, machine-readable L2→L3 relations, Pattern expansion, M3/M4 or L4 work.
