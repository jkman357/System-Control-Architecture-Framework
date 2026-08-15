# Changelog

All notable changes to **System Control Architecture Framework (SCAF)** are recorded here.

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
