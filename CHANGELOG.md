# Changelog

All notable changes to **System Control Architecture Framework (SCAF)** are recorded here.

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

RC versions remain mutable only by creating the next RC. A non-RC release is produced only after an explicit freeze decision.
