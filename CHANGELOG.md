# Changelog

## v0.0.3rc03 — 2026-08-16

Initial representative L3 Pattern / Mechanism tranche after the v0.0.3rc02 focused closure review returned **PASS / `L3 CATALOG-CONTRACT CLOSURE GATE: YES`**.

### Added

- published the first seven permanent L3 Pattern identities as `Candidate / M1` entries:
  - `SCAF-PAT-SUP-001` — Heartbeat / Liveness Supervision;
  - `SCAF-PAT-SUP-002` — Independent Watchdog with Escalation;
  - `SCAF-PAT-REC-001` — Bounded Retry with Escalation;
  - `SCAF-PAT-COM-001` — Reconnect plus State Reconciliation;
  - `SCAF-PAT-PST-001` — Atomic Dual-Copy Persistent State;
  - `SCAF-PAT-LCM-001` — Transactional Update with Rollback;
  - `SCAF-PAT-EVD-001` — Pre/Post-Trigger Retained Incident Evidence Ring;
- added family directories only for mechanism families that now contain published entries;
- added pattern-level metadata, L2 trace, PDA-decision, composition, failure-mode, provenance and L3/L4 boundary content for the initial tranche.

### Changed

- closed rc02 review Trivial `R2-01` by aligning the root README gate wording with the completed focused rc02 closure review and the open rc03 initial-pattern tranche;
- advanced L3 governance/metadata/trace/template development labels to v0.0.3rc03;
- updated the L3 index from zero-pattern planning state to the seven-entry Candidate/M1 navigation state;
- made the accepted contract explicitly applicable to current as well as future pattern entries;
- opened the independent initial-tranche conformance review gate while keeping `Available` promotion and broad catalog expansion closed.

### Preserved

- frozen v0.0.2 `docs/normative/` content and all 294 normative IDs / 218 Project-Applicable Obligations / 76 Framework Normative Invariants;
- many-to-many L2→L3 trace semantics and the prohibition on generic L2→L3 `satisfies` shortcuts;
- Project Design Authority ownership of project mechanism selection/configuration;
- separation among Catalog Status, Pattern Maturity and project-side Pattern Selection State;
- the mechanism-family primary-identity rule and post-publication immutability;
- L3/L4 boundary and the gates on schema, validator, CI, code generation and executable governance.

## v0.0.3rc02 — 2026-08-16

Focused L3 catalog-contract cleanup after the independent v0.0.3rc01 architecture review returned **PASS WITH MINOR CLEANUP / L3 CATALOG-CONTRACT GATE: YES, AFTER MINOR CLEANUP**, with no Critical or Major findings.

### Changed

- replaced concrete-looking `SCAF-PAT-*-001` examples with non-allocating `<NNN>` placeholders and defined that an ID is **published** only when assigned to an instantiated catalog entry in a repository release;
- clarified that illustrative pattern identifiers/placeholders do not allocate or reserve identities;
- defined primary pattern family by the pattern's principal reusable mechanism intent rather than by dominant frozen-concern trace;
- made the primary-family component immutable after pattern-ID publication and required a new ID plus explicit `Supersedes` lifecycle relation for genuine post-publication primary-family change;
- narrowed catalog `Constraint Input` targets to frozen L2 obligations and moved actual project Controlled Decision references to project-side selection/application records;
- kept decision categories in `Required PDA Decisions` while separating externally owned safety/security/regulatory/risk inputs into `External Authority Considerations`;
- represented `Subsumes` and `Supersedes` as distinct metadata/template relations;
- corrected the review baseline CTX SHA-256 manifest value used by the focused review instruction.

### Preserved

- frozen v0.0.2 L1/L2 normative baseline;
- 294 normative requirement IDs: 218 Project-Applicable Obligations and 76 Framework Normative Invariants;
- L3 mechanism-family taxonomy;
- many-to-many L2→L3 trace model and prohibition on generic L2→L3 `satisfies`;
- Project Design Authority ownership of project mechanism selection/configuration;
- independent catalog status, pattern maturity and project selection state;
- L3/L4 boundary;
- zero instantiated `SCAF-PAT-*` pattern entries.

### Deliberately Not Added

- actual L3 pattern instances or allocated Pattern IDs;
- L4 implementation / verification guidance;
- schema, validator, CI or executable-governance machinery.

### Gate

- run a focused independent rc02 closure review against rc01 findings L3-01 through L3-05 and T-01;
- confirm each finding is Resolved or explicitly identify any regression/new issue;
- reconfirm the frozen v0.0.2 normative baseline is byte-stable;
- if the focused review passes without Critical/Major findings and no unresolved identity/trace-authority defect remains, allow the next RC to allocate the first small representative `SCAF-PAT-*` tranche.

## v0.0.3rc01 — 2026-08-16

First controlled L3 Pattern / Mechanism Catalog architecture / contract RC downstream of the frozen v0.0.2 L1/L2 baseline.

### Added

- `docs/l3/README.md` establishing the L3 development scope and frozen-upstream rule;
- `docs/l3/00_L3_Catalog_Governance.md` defining the L3 `SCAF-PROF` authority position, mechanism-family taxonomy, `SCAF-PAT-<FAMILY>-<NNN>` identity rule, catalog status/maturity, composition semantics and L3/L4 boundary;
- `docs/l3/01_L3_Pattern_Metadata_Contract.md` defining the human-readable metadata contract, including mandatory `Required PDA Decisions`;
- `docs/l3/02_L3_Trace_and_Selection_Model.md` defining many-to-many L2→L3 trace semantics and separating catalog status from project selection state;
- `docs/l3/03_L3_Pattern_Index.md` as a non-authoritative planning/navigation index;
- `docs/l3/catalog/README.md` defining future mechanism-family placement;
- `docs/l3/templates/L3_Pattern_Template.md` for later pattern authoring.

### Architecture Decisions

- L3 is a downstream `SCAF-PROF` candidate realization catalog, not a third-level extension of the frozen concern requirement tree;
- L3 uses mechanism families (`SUP`, `COM`, `REC`, `FTL`, `TIM`, `PST`, `LCM`, `EVD`, `SYN`, `SEC`) rather than duplicating CTX/ARCH/INT/TIME/RUN/ROB/LIFE/OBS/CFG/SEC authority homes;
- pattern trace relations are `Primary Realization Candidate`, `Supporting Realization` and `Constraint Input`; a generic L2→L3 `satisfies` relation is intentionally prohibited;
- pattern selection/configuration remains a Project Design Authority decision and catalog selection alone does not establish L2 satisfaction;
- catalog lifecycle `Status` and engineering `Maturity` are independent dimensions;
- profile facets are orthogonal to mechanism families;
- project-specific mechanisms outside the catalog remain permitted when the applicable frozen obligations and external constraints are satisfied.

### Frozen Baseline Integrity

- **No `docs/normative/` v0.0.2 file is intentionally changed.**
- No frozen L1/L2 requirement ID, Target class, primary authority home, core metamodel entity or top-level concern taxonomy is reopened by this RC.

### Deliberately Not Added

- actual `SCAF-PAT-*` pattern instances;
- L4 implementation or verification guidance;
- machine-readable schema / authority registry;
- validator, generated reverse-trace index or CI;
- code generation / executable governance.

### Gate

- perform an independent L3 architecture / structure review;
- confirm frozen v0.0.2 normative hashes are unchanged;
- confirm L3 does not redefine L2 semantics or Project Design Authority;
- confirm the many-to-many trace model preserves multiple valid mechanism choices;
- confirm status/maturity, selection semantics and L3/L4 separation are sufficiently stable before allocating the first `SCAF-PAT-*` IDs.

## v0.0.2 — 2026-08-16

Frozen L1/L2 Baseline.

This release is created by explicit governance freeze decision after the independent `v0.0.2rc15` L1/L2 freeze-candidate audit returned **Yes**, with no Critical, Major, Minor or Trivial issues. The audit verified the rc15 archive SHA-256, confirmed all 294 parsed requirement blocks are stable relative to rc14, and found no cross-boundary, identity, source/evidence/closure, Framework Scan, L3/L4 or donor-promotion regression.

### Frozen

- Authority Kernel;
- SCAF-CTX;
- SCAF-ARCH;
- SCAF-INT;
- SCAF-TIME;
- SCAF-RUN;
- SCAF-ROB;
- SCAF-LIFE;
- SCAF-OBS;
- SCAF-CFG;
- SCAF-SEC;
- 294 normative requirement IDs;
- 218 Project-Applicable Obligations;
- 76 Framework Normative Invariants;
- primary authority homes and reviewed cross-boundary semantics;
- Boot / Operational / Session / Time Epoch / CFG / Security / OBS identity separation;
- source / evidence / evidence-sufficiency / underlying-closure separation;
- Framework Scan semantics;
- donor-promotion and L1/L2 mechanism-neutrality gates.

### Normative Semantic Change from v0.0.2rc15

- **None intended.**
- The freeze action changes release/freeze state only.
- Normative documents change release metadata from `v0.0.2rc15` to `v0.0.2`; requirement blocks remain unchanged.

### Not Included in the Frozen Baseline

- L3 pattern / mechanism catalogs;
- L4 implementation / verification guidance;
- schema;
- validator;
- CI;
- generated conformance tooling.

### Governance

- `v0.0.2` is frozen and must not be modified in place.
- Later L3/L4 or executable-governance work must trace to this frozen L1/L2 baseline and use a new development version when normative evolution is required.

## v0.0.2rc15 — 2026-08-16

Freeze-candidate release-hygiene closure after the independent rc14 audit found no Critical/Major issues, confirmed the four rc13 editorial findings Resolved, found no normative/cross-boundary/identity/Framework-Scan/L3-L4/donor-promotion regression, and returned the freeze gate Yes after one trivial non-semantic README cleanup.

### Changed

- corrected the stale README sentence that incorrectly described the next gate as another final integrated L1/L2 review;
- aligned the README introduction with the actual rc15 narrow freeze-candidate audit followed by an explicit governance freeze decision;
- synchronized current release / gate positioning to v0.0.2rc15;
- updated normative document release labels to v0.0.2rc15 without intended normative-body semantic change.

### Normative Semantic Change

- **None intended.**
- All 294 requirement IDs and all Target classes are preserved.
- Primary authority homes, cross-boundary semantics, identity semantics, Framework Scan semantics, verification/evidence/closure semantics, Security Authority provenance and donor-promotion gates are carried forward unchanged from rc14.

### Deliberately Not Added

- new top-level concerns or core metamodel entities;
- architecture rediscovery or taxonomy changes;
- L3 pattern / mechanism catalogs;
- L4 implementation / verification guidance;
- schema, validator, CI or generated conformance tooling.

### Gate

- perform a narrow independent rc15 L1/L2 freeze-candidate audit;
- confirm the rc14 audit T-01 README wording is Resolved;
- confirm 294 IDs / Targets and normative semantics remain stable;
- if the audit passes, make the explicit governance L1/L2 freeze decision.

## v0.0.2rc14 — 2026-08-16

Final editorial closure / L1/L2 freeze candidate after the independent rc13 final integrated review found no Critical/Major issues, judged the complete L1/L2 backbone Stable after minor editorial cleanup, and returned the freeze-candidate gate Yes after those editorial items are closed.

### Changed

- removed the lower-case normative-looking `shall` from Authority Kernel descriptive prose outside a Target-classified requirement block;
- normalized `SCAF-OBS-020` second prohibition to the canonical `**SHALL NOT**` normative-keyword form;
- corrected `docs/00_Input_Baseline.md` section numbering so the controlled-rewrite derivation note follows §7 as §8;
- corrected `docs/03_Gen1_to_Gen2_Concept_Mapping.md` duplicate §8 numbering by renumbering the controlled-rewrite-use section to §9;
- synchronized README, Authority Kernel release label, current gate and freeze-candidate positioning to v0.0.2rc14.

### Normative Semantic Change

- **None intended.**
- Requirement IDs, Target classes, primary authority homes, cross-boundary semantics, identity semantics, Framework Scan semantics, verification/evidence/closure semantics and donor-promotion gates are carried forward unchanged from rc13.

### Deliberately Not Added

- new top-level concerns or core metamodel entities;
- architecture rediscovery or taxonomy changes;
- L3 pattern / mechanism catalogs;
- L4 implementation / verification guidance;
- schema, validator, CI or generated conformance tooling.

### Gate

- perform a narrow independent rc14 freeze-candidate audit;
- confirm the four rc13 editorial findings are Resolved;
- confirm the rc13 normative architecture is unchanged except for non-semantic editorial cleanup;
- if the audit passes, make an explicit governance decision whether to freeze the L1/L2 baseline.

## v0.0.2rc13 — 2026-08-16

Final integrated L1/L2 consolidation after independent rc12 SCAF-SEC review found no Critical/Major issues, judged SEC Stable after minor cleanup, confirmed SEC integration with the existing L1/L2 backbone as Pass, and cleared SCAF to enter final consolidation before a freeze-candidate decision.

### Changed

- corrected `SCAF-SEC-024` to reference the normative `SCAF-SEC-038` SEC/OBS boundary;
- clarified `SCAF-SEC-017` so `SCAF-ROB` resilience obligations apply where resource abuse is robustness-significant;
- narrowed `SCAF-SEC-023` from ambiguous `CFG-controlled authorization` wording to authorization-related CFG input/fact semantics while preserving Security Authority and CFG source authority;
- normalized residual ROB structural-boundary wording to an applicable Project Design Authority decision under SCAF-ARCH;
- normalized residual CTX safety/hazard source-authority wording without changing safety/risk acceptance authority;
- consolidated current release/gate wording for the complete CTX/ARCH/INT/TIME/RUN/ROB/LIFE/OBS/CFG/SEC L1/L2 backbone;
- synchronized README, Authority Kernel release label, read-coverage position and current freeze-candidate gate.

### Deliberately Not Added

- new top-level concerns or core metamodel entities;
- SCAF taxonomy changes or architecture rediscovery;
- L3 pattern / mechanism catalogs;
- L4 implementation / verification guidance;
- cryptographic, resilience, lifecycle, logging, configuration or protocol implementation mechanisms;
- schema, validator, CI or generated conformance tooling.

### Gate

- perform independent final integrated L1/L2 review;
- determine whether the complete L1/L2 backbone is suitable as a freeze candidate;
- keep L3 closed until the integrated review passes and an explicit freeze decision is made.

## v0.0.2rc12 — 2026-08-16

SCAF-SEC controlled L1/L2 normative tranche after independent rc11 integrated review found no Critical/Major issues, accepted CTX/ARCH/INT/TIME/RUN/ROB/LIFE/OBS/CFG as Stable, and cleared SEC to start with parallel minor consolidation cleanup.

### Added

- `docs/normative/100_SCAF_SEC_Security_Architecture_Interface_Robustness_Obligations.md`;
- L1 authority separation for External Security Authority -> SCAF-SEC -> Project Design Authority;
- project obligations for security-relevant assets/subjects/trust relationships, security identity, authentication, authorization, confidentiality, integrity/authenticity, hostile freshness/anti-replay and credential/key lifecycle architecture semantics;
- project obligations for privilege/separation, security-sensitive control paths, hostile input/resource abuse, compromise/trust loss, compromise containment, security degradation/downgrade, security-service dependency and trust re-establishment eligibility;
- project obligations for security-sensitive LIFE/CFG relationships, security evidence needs, multi-participant security-decision consistency, verification-claim trace and re-evaluation;
- explicit SEC/ARCH, SEC/INT, SEC/TIME, SEC/RUN, SEC/ROB, SEC/LIFE, SEC/OBS, SEC/CFG, SEC/ASSUR, identity-partition and SEC/PROF realization boundaries.

### Changed

- normalized older Project-Applicable boundary/non-prescription explanatory prose as informative notes where identified by the rc11 integrated review;
- replaced `SCAF-INT-017` non-canonical `owned by SCAF-ROB` wording with Authority Kernel framework-semantics grammar;
- replaced the stale ROB `persistent configuration ownership` phrase with authoritative CFG source/value semantics;
- synchronized README, Authority Kernel release labels and read-coverage position for the SEC tranche;
- retained the frozen v0.0.1 architecture baseline and stable CTX/ARCH/INT/TIME/RUN/ROB/LIFE/OBS/CFG authority homes.

### Deliberately Not Added

- new top-level taxonomy or core metamodel entities;
- universal threat model, security objective, risk-acceptance policy or certification acceptance authority;
- universal encryption/signature algorithm, key size, certificate/PKI, secure element, TPM/HSM, secure-boot implementation, firewall, sandbox, credential store, password/token format or access-control mechanism;
- L3 pattern/mechanism catalog or L4 implementation/verification guidance;
- schema, validator, generated checklist or CI;
- broad Draft/RC donor promotion, final migration proof or normative freeze.

## v0.0.2rc11 — 2026-08-16

Integrated L1/L2 consolidation after independent rc10 review accepted CFG as Stable after minor cleanup and judged the CTX -> ARCH -> INT -> TIME -> RUN -> ROB -> LIFE -> OBS -> CFG backbone Stable after targeted consolidation. No new concern tranche is added.

### Changed

- narrowed broad CFG `corruption recovery` wording to corruption/loss/unavailability interpretation, CFG source-state disposition/restoration eligibility and authoritative resulting CFG state, while preserving ROB recovery/resilience-response authority;
- completed `SCAF-CFG-016` derived-value provenance with source identity, version/context, derivation basis, resulting-value provenance and invalid/unknown/incompatible-input consequence;
- normalized framework-boundary/non-prescription prose in `SCAF-CFG-006`, `SCAF-CFG-010`, `SCAF-CFG-018` and `SCAF-CFG-022` as informative boundary notes;
- hardened CFG item/version identity so physical storage locators do not by themselves establish semantic CFG identity;
- rewrote `SCAF-CFG-023` as a CFG-source-fact observability need traced to OBS, rather than CFG defining OBS evidence semantics;
- added explicit INT-to-CFG hardening: INT-valid/delivered/decoded configuration data does not by itself establish CFG acceptance, commit, activation/application or authoritative CFG source state;
- normalized older RUN/ROB/LIFE/OBS forward references to PDA-assigned authoritative CFG source responsibility and CFG source/value/version/migration/commit semantics;
- synchronized README, Authority Kernel release label and read-coverage positioning for the pre-SEC consolidation gate;
- retained the frozen v0.0.1 architecture baseline and existing concern taxonomy.

### Deliberately Not Added

- `SCAF-SEC` normative tranche;
- new top-level taxonomy or core metamodel entities;
- L3 pattern/mechanism catalog;
- L4 implementation/verification guidance;
- schema, validator, generated checklist or CI;
- broad Draft/RC donor promotion, final migration proof or normative freeze.

## v0.0.2rc10 — 2026-08-16

SCAF-CFG controlled L1/L2 normative tranche after independent rc09 review cleared the OBS architecture gate and allowed CFG authoring to begin with localized OBS cleanup.

### Added

- `docs/normative/90_SCAF_CFG_Configuration_Persistent_Operational_State_Obligations.md`;
- L1 authority boundaries for configuration/persistent operational-state classification, authoritative source responsibility, item identity/provenance, defaults/provisioning, validation, version/migration, atomic commit, CFG-side rollback/corruption handling, calibration/parameter state and synchronization/consistency;
- project obligations for unknown/uninitialized semantics, multiple-source precedence, LIFE update/activation coordination, RUN persistent/current-state mapping, OBS evidence views of CFG facts and external configuration constraints;
- explicit CFG/OBS, CFG/LIFE, CFG/RUN, CFG/INT, CFG/TIME, CFG/ROB, CFG/ARCH, external-authority, CFG/ASSUR, artifact/source-authority, identity-partition and CFG/PROF realization boundaries.

### Changed

- removed the framework-self timebase prohibition from `SCAF-OBS-006` Project-Applicable target and retained it only as an informative note backed by `SCAF-OBS-033`;
- normalized framework-boundary/non-prescription prose in Project-Applicable OBS obligations as informative notes;
- narrowed `SCAF-OBS-009` to causal/derived-inference claims and separated first-observed abnormal evidence semantics in `SCAF-OBS-016`;
- narrowed `SCAF-OBS-021` to retention/accessibility/expiration while retaining lifecycle survivability in `SCAF-OBS-018`;
- corrected stale README rc08 release/gate/repository-content text and remaining ROB non-normative editorial residue;
- updated all normative release labels and Authority Kernel gate-table label to rc10;
- retained the frozen v0.0.1 architecture baseline and stable Authority Kernel / CTX / ARCH / INT / TIME / RUN / ROB / LIFE authority homes.

### Deliberately Not Added

- `SCAF-SEC` normative tranche;
- new top-level taxonomy or core metamodel entities;
- universal configuration file/schema/database/NVM layout/migration/rollback/synchronization mechanisms;
- L3/L4 mechanism or implementation guidance;
- schema, validator, generated checklist or CI;
- broad Draft/RC donor promotion, final migration proof or normative freeze.

## v0.0.2rc09 — 2026-08-15

SCAF-OBS controlled L1/L2 normative tranche after independent rc08 review cleared the LIFE architecture gate and allowed OBS authoring to begin with localized LIFE cleanup.

### Added

- `docs/normative/80_SCAF_OBS_Observability_Diagnostics_Incident_Evidence_Obligations.md`;
- L1 authority boundaries for operational observability, diagnostics, incident evidence, evidence identity/provenance, time/identity correlation, evidence quality/missingness, preservation/survivability/accessibility/export, observer self-health and observer effect;
- project obligations for source-authority trace, first-abnormal versus later/terminal evidence, incident timeline/correlation, lifecycle survivability, early-boot/crash-loop evidence, four-way identity recording, evidence copies/transforms, persistent evidence/CFG distinction and external evidence constraints;
- explicit OBS/RUN, OBS/ROB, OBS/LIFE, OBS/INT, OBS/TIME, OBS/CFG, OBS/ASSUR, external-authority, four-way-identity, OBS/ARCH, causal-inference and OBS/PROF realization boundaries.

### Changed

- moved the `SCAF-LIFE-014` framework self-rule out of the Project-Applicable target by converting it to an informative boundary note backed by existing framework invariants;
- narrowed `SCAF-LIFE-007` Boot Incarnation triggers to LIFE-controlled boot/lifecycle instances and preserved RUN authority for runtime-only operational restart/replacement;
- changed `SCAF-LIFE-010` from intrinsic retained-state validity wording to lifecycle-transition consumption eligibility using controlled source-authority validity/provenance/version semantics;
- normalized `SCAF-LIFE-012` and `SCAF-LIFE-013` to PDA-assigned lifecycle authoritative-result responsibility and lifecycle responsibility handoff wording;
- separated `SCAF-LIFE-016` lifecycle activation/eligibility from RUN Service readiness/availability;
- replaced `SCAF-LIFE-018` bare `safely or correctly` wording with applicable controlled continuation/eligibility criteria and source-authority trace;
- corrected minor LIFE/ROB editorial residue and updated README, Authority Kernel gate label and read-coverage position for rc09;
- retained the frozen v0.0.1 architecture baseline and stable Authority Kernel / CTX / ARCH / INT / TIME / RUN / ROB authority homes.

### Deliberately Not Added

- `SCAF-CFG` or `SCAF-SEC` normative tranches;
- new top-level taxonomy or core metamodel entities;
- universal log schema, ring buffer, retained-RAM layout, crash-recorder API, storage technology, telemetry protocol or diagnostic mechanism;
- L3/L4 mechanism or implementation guidance;
- schema, validator, generated checklist or CI;
- broad Draft/RC donor promotion, final migration proof or normative freeze.

## v0.0.2rc08 — 2026-08-15

SCAF-LIFE controlled L1/L2 normative tranche after independent rc07 review cleared the ROB architecture gate and allowed LIFE authoring to begin with localized ROB cleanup.

### Added

- `docs/normative/70_SCAF_LIFE_Boot_Power_Reset_Update_Lifecycle_Obligations.md`;
- L1 authority boundaries for boot/power/reset/update/activation/rollback lifecycle transaction/state/result semantics and Boot Incarnation / Boot Generation;
- project obligations for lifecycle authority/result responsibility, request-versus-result semantics, LIFE-to-RUN readiness handoff, reset classification/cause, retained-state validity, power lifecycle, update preconditions/atomicity/activation/rollback/resume and multi-participant lifecycle coordination;
- explicit LIFE/RUN, LIFE/ROB, LIFE/TIME, LIFE/INT, LIFE/CFG, LIFE/OBS, identity-partition, LIFE/ARCH, external safety/security/risk and LIFE/PROF realization boundaries.

### Changed

- split `SCAF-ROB-005` detectability/latent-condition disposition from diagnostic-coverage objective by adding `SCAF-ROB-031`;
- split `SCAF-ROB-011` recovery/repair outcome from retry/escalation termination by adding `SCAF-ROB-032`;
- clarified `SCAF-ROB-014` so residual-risk decision/acceptance is explicitly made by the applicable risk authority;
- split `SCAF-ROB-027` ROB/OBS evidence-observation boundary from ROB/ASSUR evidence-sufficiency boundary by adding `SCAF-ROB-033`;
- normalized health/failure terminology so ROB classifications/decision outcomes are not confused with RUN operational states;
- replaced residual `approved` and project-actor-like ROB prose with controlled Authority Kernel relation language;
- updated README, Authority Kernel gate label and read-coverage position for rc08;
- retained the frozen v0.0.1 architecture baseline and stable Authority Kernel / CTX / ARCH / INT / TIME / RUN authority homes.

### Deliberately Not Added

- `SCAF-OBS`, `SCAF-CFG` or `SCAF-SEC` normative tranches;
- new top-level taxonomy or core metamodel entities;
- universal bootloader/A-B partition/update protocol/reset sequence/power sequencing/watchdog/recovery mechanisms;
- L3/L4 mechanism or implementation guidance;
- schema, validator, generated checklist or CI;
- broad Draft/RC donor promotion, final migration proof or normative freeze.

## v0.0.2rc07 — 2026-08-15

SCAF-ROB controlled L1/L2 normative tranche after independent rc06 review cleared the RUN architecture gate and allowed ROB authoring to begin with localized RUN cleanup.

### Added

- `docs/normative/60_SCAF_ROB_Robustness_Resilience_Obligations.md`;
- L1 authority boundaries for Fault/Error/Failure semantics, health/failure determination, detectability/latent conditions, propagation, runtime containment, tolerance/degradation/failover/reconfiguration, recovery/repair/retry and reintegration;
- project obligations for distributed partition/reconciliation resilience, correlated/common-mode faults, cascading/recovery-storm behavior, resource-exhaustion/long-run resilience, lifecycle/configuration failure response and robustness observability;
- explicit ROB/RUN, ROB/ARCH, ROB/TIME, ROB/INT, ROB/LIFE, ROB/OBS/ASSUR, ROB/CFG, external safety/security/risk and ROB/PROF realization boundaries.

### Changed

- clarified `SCAF-RUN-002` so Project Design Authority defines the project state model and assigns runtime authoritative-current-state responsibility, while state carriers/requests/logs do not become runtime state authority;
- normalized Project-Applicable RUN boundary prose as informative notes or separate trace obligations;
- replaced non-canonical `RUN controls / ROB controls` wording with Authority Kernel framework-semantics plus Project Design Authority project-instance grammar;
- split RUN/CFG from RUN/OBS and CTX operating-mode from incarnation-identity framework invariants;
- added atomic readiness/availability consequence trace and cross-participant measurable-consistency trace obligations;
- replaced RUN `disposition` wording that could be confused with SCAF-APP Disposition vocabulary;
- completed supporting Evidence-state terminology by replacing generic evidence `Accepted` with `Sufficient`;
- updated the Authority Kernel gate-table release label and README/read-coverage position for rc07;
- retained the frozen v0.0.1 architecture baseline and stable Authority Kernel / CTX / ARCH / INT / TIME authority homes.

### Deliberately Not Added

- `SCAF-LIFE`, `SCAF-OBS`, `SCAF-CFG` or `SCAF-SEC` normative tranches;
- new top-level taxonomy or core metamodel entities;
- universal watchdog/heartbeat/redundancy/voting/retry/failover/reset mechanisms;
- L3/L4 mechanism or implementation guidance;
- schema, validator, generated checklist or CI;
- broad Draft/RC donor promotion, final migration proof or normative freeze.

## v0.0.2rc06 — 2026-08-15

SCAF-RUN controlled L1/L2 normative tranche after independent rc05 review cleared INT/TIME authority boundaries and allowed RUN authoring to begin.

### Added

- `docs/normative/50_SCAF_RUN_Runtime_State_Operational_Lifecycle_Obligations.md`;
- L1 authority boundaries for operational/service state meaning, state domains, transition consistency, readiness/availability, generic operational lifecycle and Operational Incarnation;
- project obligations for state authority, state invariants, permitted transitions, transition conditions, readiness/availability criteria, CTX-mode mapping, LIFE-to-RUN handoff, cross-participant state consistency and Operational Incarnation;
- explicit RUN/INT/TIME, RUN/LIFE, RUN/ROB, RUN/CFG/OBS and operating-mode/incarnation framework invariants.

### Changed

- split `SCAF-TIME-004` clock/synchronization relationship semantics from dependent temporal-claim validity under clock-relationship loss by adding `SCAF-TIME-020`;
- normalized staged forward-reference wording so TIME can trace consequences to controlled INT/RUN/ROB requirements, decisions or obligations without requiring future normative IDs to already exist;
- normalized the supporting Framework Scan evidence-state wording from generic `Accepted` to evidence-sufficiency language;
- updated README and read-coverage status for the RUN tranche;
- retained the frozen v0.0.1 architecture baseline and stable Authority Kernel / CTX / ARCH / INT baselines.

### Deliberately Not Added

- `SCAF-ROB`, `SCAF-LIFE`, `SCAF-OBS`, `SCAF-CFG` or `SCAF-SEC` normative tranches;
- new top-level taxonomy or core metamodel entities;
- state-machine implementation patterns, RTOS/task/thread rules or scheduling mechanisms;
- L3/L4 mechanism or implementation guidance;
- schema, validator, generated checklist or CI;
- broad Draft/RC donor promotion, final migration proof or normative freeze.

## v0.0.2rc05 — 2026-08-15

Targeted INT/TIME authority-boundary closure after independent review of v0.0.2rc04.

### Changed

- tightened `SCAF-TIME-008` so TIME defines concurrency constraints only when needed to establish an explicitly TIME-owned measurable temporal/capacity/resource property;
- added an explicit TIME/INT/RUN concurrency-and-ordering framework invariant so INT keeps semantic ordering and RUN keeps operational-state/transition consistency;
- removed ROB detection/health authority from `SCAF-TIME-012`, leaving TIME with measurable starvation/fairness/overload bounds and prevention/bounding constraints;
- narrowed `SCAF-TIME-013` to accumulation model, operating horizon, measurable bound/capacity and margin, leaving exhaustion detection and rollover/renewal/degradation/recovery behavior to the applicable downstream concern;
- closed synchronization-loss semantics in `SCAF-TIME-004` by requiring dependent temporal claims to define validity/invalidation/re-evaluation behavior when the required clock relationship is unusable;
- normalized TIME wording to distinguish chronological/temporal ordering from `SCAF-INT` semantic ordering;
- strengthened `SCAF-INT-002` to preserve the frozen Interaction-to-Interface boundary relation and added a conditional separately-controlled Interface identity obligation;
- widened `SCAF-INT-003` participant coverage to external Systems/actors/applicable external participants without forcing Node modeling;
- strengthened `SCAF-INT-006` with explicit validity-state assignment criteria and contract-consequence trace;
- retained the frozen v0.0.1 architecture baseline and stable Authority Kernel / CTX / ARCH normative baselines.

### Deliberately Not Added

- `SCAF-RUN` normative tranche;
- new top-level taxonomy or core metamodel entities;
- new Capacity or Concurrency top-level concerns;
- ROB normative elaboration beyond preserving its frozen authority boundary;
- L3/L4 mechanism or implementation guidance;
- schema, validator, generated checklist or CI;
- broad Draft/RC donor promotion, final migration proof or normative freeze.

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
