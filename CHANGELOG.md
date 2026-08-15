# Changelog

## v0.0.2rc04 — 2026-08-15

INT + TIME controlled L1/L2 normative tranche.

### Added

- `docs/normative/30_SCAF_INT_Interface_Interaction_Data_Contract_Obligations.md`;
- `docs/normative/40_SCAF_TIME_Timing_Concurrency_Capacity_Obligations.md`;
- explicit INT/TIME freshness-state versus measurable-time authority boundary;
- explicit protocol-session versus Time Epoch / Boot Incarnation / Operational Incarnation authority partition in normative form;
- project obligations for Interface/Interaction identity, contract semantics, validity/provenance/order/freshness, compatibility/evolution and session identity;
- project obligations for timebase, synchronization, temporal budgets, concurrency, queue/capacity, resource margin and long-duration bounded-growth properties.

### Changed

- accepted the rc03 independent review result that Authority Kernel / CTX / ARCH have no remaining Critical or Major closure defects;
- split `SCAF-CTX-007` consequence, ordinary continuity/degradation and safety-source provenance into more atomic project obligations;
- split underlying closure authority from SCAF-APP closure/disposition trace in the Authority Kernel;
- removed the remaining `verification obligation/result` lexical collapse from the Authority Kernel relation grammar;
- normalized supporting `SCAF-ASSUR` wording to framework-side verification/evidence-sufficiency criteria plus project-side evidence evaluation;
- updated README and read-coverage status for the INT + TIME tranche.

### Deliberately Not Added

- `SCAF-RUN` normative tranche;
- new top-level taxonomy or core metamodel entities;
- L3 watchdog/heartbeat/CRC/ECC/retry/failover mechanism catalogs;
- L4 MCU/PC/SoC/FPGA/DSP implementation rulebooks;
- schema, validator, generated checklist or CI;
- broad Draft/RC donor promotion, final migration proof or normative freeze.

## v0.0.2rc03 — 2026-08-15

Target/authority precision closure release after independent review of v0.0.2rc02. The frozen v0.0.1 architecture baseline remains unchanged.

### Changed

- split mixed requirement targets so Project-Applicable Obligations no longer contain SCAF framework self-rules;
- separated `SCAF-CTX-007` project consequence/outcome obligations from the `SCAF-CTX` / `SCAF-ROB` / safety-authority framework boundary invariant;
- restored applicable safety/hazard authority as the source authority for safety-significant safety objectives/conditions and risk-acceptance basis, with Project Design Authority integrating those inputs into architecture;
- separated `SCAF-ARCH-008` project containment-structure inputs from the framework-level ARCH/ROB containment-authority invariant;
- separated Decision from Deviation and Verification Obligation from Verification Execution/Result State in `SCAF-AK-003`;
- split evidence-sufficiency evaluation from underlying closure authority by adding `SCAF-AK-012`;
- moved the unqualified relation-language prohibition into the explicit `SCAF-AK-011` Framework Normative Invariant;
- split Node-decomposition applicability from Node-boundary definition into `SCAF-ARCH-002` and `SCAF-ARCH-016`;
- tightened `SCAF-CTX-003` Function traceability and `SCAF-ARCH-015` shared-dependency representation wording;
- normalized frozen-reference wording so current development-line semantics no longer carry stale rc01 labels or outdated evidence/acceptance language.

### Deliberately Not Added

- `SCAF-INT`, `SCAF-TIME` or `SCAF-RUN` normative tranches;
- new top-level taxonomy branches or core metamodel entities;
- L3 mechanism catalogs or L4 implementation rulebooks;
- schema, validator, CI or generated checklist machinery;
- broad donor promotion, final migration proof or normative freeze.

## v0.0.2rc02 — 2026-08-15

Targeted normative-precision correction release after independent review of v0.0.2rc01. The frozen v0.0.1 architecture baseline remains unchanged.

### Changed

- separated **Project-Applicable Obligations** from **Framework Normative Invariants** in the Authority Kernel;
- restored project evidence-sufficiency decisions exclusively to Project Verification / Assurance Authority while keeping `SCAF-ASSUR` as framework-side assurance/evidence semantic authority;
- clarified that external safety/security/regulatory/risk constraints do not automatically turn the external authority into Project Design Authority;
- separated decision/deviation, risk, verification and evidence state dimensions in `SCAF-AK-003`;
- tightened closure semantics so verification authority does not inherit underlying requirement/design/risk/deviation closure authority;
- split cross-cutting project ownership from framework authoring invariants;
- narrowed `SCAF-CTX-007` to consequence and required continuity/degradation/safety constraints, leaving failover/recovery response to `SCAF-ROB` and safety-significant conditions to applicable safety/hazard authority;
- converted `SCAF-CTX-010` into CTX trace-source readiness rather than duplicate architecture-justification authority;
- split material operating-mode context into `SCAF-CTX-012`;
- made Node decomposition explicitly applicability-driven in `SCAF-ARCH-002`;
- constrained Capability/Service allocation to the frozen System/Node metamodel typing;
- corrected `SCAF-ARCH-008` so Project Design Authority defines actual containment-relevant structural/Domain boundaries while `SCAF-ROB` owns runtime containment behavior;
- split compound ARCH obligations into structural context trace, logical-vs-structural dependency distinction and shared-dependency exposure requirements;
- clarified informative summary tables so they do not create duplicate normative obligations;
- normalized residual authority wording in supporting analysis material.

### Deliberately Not Added

- `SCAF-INT`, `SCAF-TIME` or `SCAF-RUN` normative tranches;
- new top-level taxonomy branches or core metamodel entities;
- L3 watchdog/heartbeat/CRC/ECC or other mechanism catalogs;
- broad L4 implementation rulebooks;
- schema, validator, CI or generated checklist machinery;
- broad donor promotion, final migration proof or normative freeze.

## v0.0.2rc01 — 2026-08-15

First controlled L1/L2 normative-rewrite release candidate after the frozen v0.0.1 architecture baseline.

### Added

- `docs/normative/00_SCAF_Authority_Kernel.md` with normative authority roles, relation grammar, Applicable Satisfaction Basis, closure semantics and rewrite/promotion gates;
- `docs/normative/10_SCAF_CTX_System_Context_Obligations.md` with initial L1/L2 System Context / Function / Capability / Service obligations;
- `docs/normative/20_SCAF_ARCH_System_Architecture_Obligations.md` with initial L1/L2 System / Node / Role / Domain architecture obligations;
- provisional normative requirement identifiers for the first controlled rewrite tranche.

### Changed

- separated framework-side `SCAF-PROF` from project-side Project Realization: profiles guide/constrain realization; project realization actors actually realize decisions;
- separated framework-side `SCAF-ASSUR` semantics from project-side Project Verification / Assurance Authority;
- normalized Authority Role -> Controlled Decision -> Authoritative Artifact vocabulary;
- normalized the authority relation grammar to distinguish `Guides Realization` from project-side `Realizes`;
- clarified controlled rewrite eligibility vs donor normative-promotion eligibility;
- updated freshness, containment, lifecycle and evidence overlap prose to use framework-side/project-side authority language;
- reframed already-owned Function/Service and Configuration areas as normative-elaboration coverage rather than taxonomy gaps;
- updated deferred CI/fixture wording to reflect the controlled rewrite phase rather than architecture-convergence status.

### Deliberately Not Added

- new top-level taxonomy branches or core metamodel entities;
- L3 mechanism catalogs such as watchdog, heartbeat, CRC or ECC guidance;
- broad L4 MCU/PC/SoC/FPGA/DSP implementation rulebooks;
- final schema, validator, generated checklist or CI enforcement;
- broad Draft/RC donor promotion, final migration proof or normative freeze.

## v0.0.1 — 2026-08-15

Frozen architecture-convergence / authority-kernel baseline.

### Release Decision

- frozen from the reviewed `v0.0.1rc05` baseline after independent review reported **no Critical architecture issues**;
- architecture discovery is closed for this baseline;
- top-level taxonomy expansion is closed unless a future concrete project demonstrates an authority-home failure that cannot be resolved within the existing model;
- Framework Scan is accepted as a new-project startup architecture decision mechanism;
- controlled L1/L2 normative rewrite is permitted on the next development line;
- MD-first / No-CI remains in effect.

### Freeze Scope

The v0.0.1 freeze locks the architecture-convergence baseline and authority kernel. It does **not** claim:

- completed Gen1 requirement-by-requirement migration;
- broad normative promotion of Draft/RC or mixed-maturity donor semantics;
- extraction of all schema/validator/test-fixture executable invariants;
- final machine-readable schema, validator or CI enforcement;
- completion of L1/L2 normative content, L3 pattern catalogs or L4 implementation guidance.

Known lexical/authority-language cleanup identified by the rc05 independent review is intentionally deferred to `v0.0.2rc01` controlled rewrite rather than reopening the v0.0.1 architecture-convergence cycle.

### Deliberately Not Added

- new top-level taxonomy branches or core metamodel entities;
- CI / GitHub Actions;
- validators or final schemas;
- broad implementation rulebooks or mechanism catalogs.

All notable changes to **System Control Architecture Framework (SCAF)** are recorded here.

## v0.0.1rc05 — 2026-08-15

Authority-kernel cleanup / controlled-rewrite baseline release candidate.

### Changed

- accepted the rc04 independent review conclusion that no Critical architecture flaw remains and controlled normative rewrite may continue;
- clarified that the five authority planes are **SCAF framework planes** and that Project Design Authority is a project-side authority bridge rather than an implicit sixth SCAF plane;
- narrowed Framework / Governance to SCAF normative-source, authority, precedence and release/change governance, explicitly excluding organizational governance of project design/realization;
- separated authority roles from the controlled artifacts that record their decisions;
- renamed `SCAF-RUN` to **Runtime Behavior, State & Operational Lifecycle** without changing the concern ID;
- partitioned Time Epoch / Time Domain (`SCAF-TIME`), Boot Incarnation (`SCAF-LIFE`), Protocol/Connection Session Identity (`SCAF-INT`), Operational Incarnation (`SCAF-RUN`) and OBS-recorded provenance/correlation;
- replaced ambiguous `source-owned satisfaction condition` wording with **Applicable Satisfaction Basis**, traceable to SCAF obligations, Project Design Authority values and applicable external authority constraints;
- aligned worked Framework Scan closure examples with the Applicable Satisfaction Basis terminology;
- split Gen1 Node identity / capability mapping into Node identity, capability semantics and capability allocation destinations;
- reframed Crash Recorder `boot epoch` as LIFE-owned boot-incarnation identity recorded by OBS, distinct from TIME-owned time epoch;
- strengthened per-donor promotion gating for stale-data, domain and implementation-rulebook donor families;
- reframed resolved robustness areas as coverage requiring normative elaboration rather than unresolved taxonomy gaps;
- changed stale `before normative rewrite` wording to controlled-rewrite / broad-expansion / promotion / freeze priorities;
- retained MD-first / No-CI policy and stopped top-level taxonomy expansion.

### Deliberately Not Added

- new top-level taxonomy branches or concerns;
- CI / GitHub Actions;
- validators or final schemas;
- broad L3 mechanism catalogs or L4 implementation rulebooks;
- frozen Draft/RC donor semantics;
- claims of completed Gen1 migration or normative freeze.

## v0.0.1rc04 — 2026-08-15

Architecture-closure / controlled-rewrite-entry release candidate.

### Changed

- accepted the rc03 independent review conclusion that the SCAF skeleton is converged enough for **controlled normative rewrite**;
- established one canonical authority model: Concern -> Project Design -> Realization -> Assurance, with `SCAF-APP` cross-cutting for disposition/trace and Governance governing the authorities;
- removed ambiguous bare `Defines` authority headings in system concerns and applied the full Framework-vs-Project authority grammar consistently;
- broke the Service/Capability circular definition and clarified subordinate System vs subordinate Node scope semantics;
- tightened the Node-boundary test so physical boundaries or verification tasks alone do not create Nodes;
- clarified `SCAF-ROB` vs `SCAF-LIFE` vs `SCAF-OBS` vs `SCAF-ASSUR` ownership for lifecycle failure, health decisions, evidence and verification;
- clarified Security Authority vs Project Design Authority: security authority owns threat/objective/risk constraints, while Project Design owns actual trust boundaries and architecture decisions;
- corrected the README robustness model so prevention/avoidance is design/realization strategy rather than Assurance ownership;
- replaced the broad eleven-row Framework Scan proof with complete state/authority/closure traces for selected concerns;
- clarified that Assurance verifies evidence sufficiency, source/project/risk authorities accept applicable closure, and `SCAF-APP` records the closure/deviation trace;
- strengthened per-donor maturity binding in multi-source migration rows and aligned distributed incident time provenance with both `SCAF-TIME` and `SCAF-OBS`;
- removed stale release-specific fixture wording from the Gen1 inventory;
- moved the project gate from architecture discovery to **controlled authority-preserving normative rewrite** while keeping migration/promotion/freeze gates explicit.

### Deliberately Not Added

- new top-level taxonomy branches;
- CI / GitHub Actions;
- validators or final schemas;
- generated checklists;
- broad MCU / FPGA / DSP / C / C# rulebooks;
- full cybersecurity or safety frameworks;
- frozen Draft/RC donor semantics;
- claims of completed Gen1 migration.

## v0.0.1rc03 — 2026-08-15

Authority-semantics and project-application convergence release candidate.

### Changed

- separated **SCAF Concern Authority** from **Project Design Authority** so framework semantics/obligations cannot be confused with project-specific architecture values;
- clarified that `SCAF-APP` dispositions/traces project state but does not become the project architecture authority;
- clarified that `SCAF-ASSUR` owns verification/evidence sufficiency, not underlying system-property thresholds;
- replaced the README's linear five-plane pipeline with non-linear governance / concern / project-design / realization / assurance relations;
- partitioned `SCAF-CTX` logical mission/service dependencies from `SCAF-ARCH` structural allocation/realization dependencies;
- defined `SCAF-RUN` as service/operational lifecycle and `SCAF-LIFE` as platform/system boot/reset/power/update lifecycle;
- moved primary timebase/clock/synchronization semantics to `SCAF-TIME` and added Clock/Time Domain;
- limited `SCAF-OBS` to observing/recording time provenance and synchronization quality for evidence;
- scoped `SCAF-SEC` as a system-control architecture interface to external/project cybersecurity authority rather than a replacement threat/risk framework;
- changed reference subsystems/patterns from a profile axis to a Realization Plane pattern category;
- made Framework Scan explicitly iterative for greenfield startup;
- added an end-to-end worked Framework Scan for the PC + multiple MCU archetype across eleven concerns;
- added per-donor source-maturity binding examples for multi-source migration rows;
- distinguished donor **source identity** from **source retrievability** and kept immutable donor locators as an explicit remaining gate item;
- incorporated the v0.0.1rc02 independent architecture review as non-normative correction input.

### Deliberately Not Added

- CI / GitHub Actions;
- validators or schemas;
- generated checklists;
- new normative rulebooks;
- large-scale normative rewrite.

## v0.0.1rc02 — 2026-08-15

Architecture / taxonomy convergence release candidate.

### Changed

- adopted the long-term framework name **System Control Architecture Framework (SCAF)**;
- retained `Gen2` only as lineage / migration context;
- defined that **Control** means system-level coordination/runtime/lifecycle/robustness concerns, not control theory and not only host-to-device control;
- separated **Framework/Governance**, **System Concern**, **Project Application**, **Assurance/Evidence**, and **Realization/Implementation** authority planes;
- removed Tooling and AI-Assisted Engineering from peer system-taxonomy status;
- expanded the core metamodel beyond Node-centric structure with Function / Service / Capability, Interface, Interaction and cross-cutting Domains;
- defined Node boundary criteria and clarified that Node is not synonymous with chip/process/device/fault/reset/power/security domain;
- introduced explicit authority relations: Defines / Constrains / Realizes / Observes / Verifies / Dispositions;
- separated artifact disposition from transformation in the migration mapping;
- added source document, section anchor, source maturity, target concern ID, confidence and deep-audit state to the concept mapping;
- replaced the linear robustness lifecycle with separate Fault/Error/Failure semantics, Runtime Resilience Response and Assurance models;
- added redundancy, failover, reconfiguration, repair, resynchronization, reintegration, diagnostic coverage and distributed-failure concerns;
- clarified that Safe State authority must come from applicable project safety/hazard authority when safety-relevant;
- made Function/Service dependency and Configuration/Persistent Operational State explicit concern homes;
- reworked Framework Scan into a decision/evidence lifecycle with independent Applicability / Decision / Risk / Verification / Evidence dimensions;
- clarified that Framework Scan dispositions project obligations but does not create or delete SCAF normative obligations;
- reorganized implementation profiles as composable axes instead of one mixed profile list;
- added distributed incident time provenance / synchronization quality / causal-correlation concerns;
- added three tabletop architecture archetypes to exercise the metamodel without adding new top-level branches;
- corrected read-coverage terminology from “three levels” to **four levels**;
- normalized the supplemental-source inventory action vocabulary.

### Deliberately Not Added

- CI / GitHub Actions;
- validators;
- Python tooling;
- test fixtures;
- machine-readable schemas;
- generated checklists;
- MCU / FPGA / DSP / .NET rulebooks;
- large-scale normative rewrite.

These remain deferred until the authority model and migration evidence converge.

## v0.0.1rc1 — 2026-08-15

Initial Framework Gen2 repository-archaeology / taxonomy working draft.

### Added

- formal separation between Gen1 baseline and supplemental Crash Recorder source;
- complete 72-file Gen1 repository inventory;
- complete supplemental-source inventory;
- document-role analysis;
- concept-level Gen1 -> Gen2 mapping;
- Keep / Move / Merge / Rewrite / Retire / New disposition model;
- overlap, outdated framing, responsibility-overlap and gap analysis;
- initial system-level taxonomy proposal;
- initial Robustness & Resilience direction;
- initial Framework Scan / Applicability Analysis direction;
- read-coverage audit with unread-file declaration.

## Release Rule

RC versions remain mutable only by creating the next RC. A non-RC release is produced only after an explicit freeze decision. `v0.0.1` was frozen on 2026-08-15 from the reviewed `v0.0.1rc05` baseline; future semantic work continues on a new RC development line and does not modify v0.0.1 in place.
