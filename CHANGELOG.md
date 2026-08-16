## v0.0.4rc04 — 2026-08-16

Focused repository-state documentation cleanup after the independent v0.0.4rc03 serialization review returned **`V0.0.4 INITIAL AUTHORITY-REGISTRY SERIALIZATION GATE: YES, AFTER MINOR CLEANUP`**, accepted the 294-record registry population, and opened one Minor finding, `R3-01`, against stale current-state/navigation text in the root README.

### Changed

- updated root release identity to v0.0.4rc04 / Authority-Registry Release-State Documentation Cleanup RC;
- synchronized the root README repository file map with `authority-registry.yaml`, the rc03 serialization record, and the rc04 cleanup record;
- corrected CI / Automation Position to state that registry serialization is already accepted and schema/validator remain future scope;
- extended the release sequence through rc03 and current rc04;
- corrected Current Governance State so rc03 is the accepted serialization stage and rc04 is the focused `R3-01` cleanup stage;
- synchronized executable-governance navigation and current-gate text to the rc04 cleanup state;
- added `docs/executable-governance/03_SCAF_v0.0.4rc04_Authority_Registry_Release_State_Documentation_Cleanup.md`.

### Preserved

- `authority-registry.yaml` byte-for-byte from rc03, including all 294 `representation_release = v0.0.4rc03` values;
- accepted authority-model semantics and rc02 determinism closure;
- accepted rc03 serialization format, population and ownership contract;
- frozen v0.0.2 L1/L2 normative content and 294 / 218 / 76 inventory;
- frozen v0.0.3 L3 content, twelve Pattern identities, lifecycle/maturity and trace semantics;
- canonical Markdown precedence and project/L3 authority boundaries.

### Deliberately Not Added

- no schema or validator implementation;
- no test fixtures or regression-test framework;
- no generator or generated reverse indexes/views;
- no CI enforcement or code generation;
- no automatic applicability inference;
- no machine-readable L2→L3 relation vocabulary;
- no new L3 Pattern, SEC-primary realization, M3/M4 or L4 work.

### Gate

- independently verify `R3-01` is fully closed;
- verify root README current-state/navigation text is internally consistent with accepted rc03 serialization and current rc04 cleanup status;
- verify `authority-registry.yaml`, accepted authority-model/serialization contracts, `docs/normative/`, and `docs/l3/` are unchanged from rc03;
- return an explicit `V0.0.4 AUTHORITY-REGISTRY RELEASE-STATE CLEANUP GATE` decision.

## v0.0.4rc03 — 2026-08-16

Initial controlled serialization of the frozen v0.0.2 L1/L2 authority inventory after the independent v0.0.4rc02 review returned **`V0.0.4 AUTHORITY-MODEL DETERMINISM CLOSURE GATE: YES`**, resolved upstream `R1-01`, and found no remaining blocking issue.

### Added

- added repository-root `authority-registry.yaml` as the first machine-readable SCAF authority representation;
- serialized exactly 294 frozen L1/L2 normative requirement records;
- reproduced exactly 218 `Project-Applicable Obligation` and 76 `Framework Normative Invariant` source Target classifications;
- used exactly one record per frozen requirement ID and excluded all `SCAF-PAT-*` identities;
- populated the accepted deterministic values `record_kind = normative_requirement`, `layer = l1_l2_normative_authority`, `source_anchor = id`, `source_release = v0.0.2`, `representation_release = v0.0.4rc03`, `status = represented`, and empty `relations`;
- added `docs/executable-governance/02_SCAF_v0.0.4rc03_Initial_Authority_Registry_Serialization.md` to define the concrete YAML shape, controlled-curated ownership, audit reproducibility, completeness claim and review gate;
- synchronized current README and executable-governance navigation to the rc03 serialization stage.

### Preserved

- frozen normative Markdown as canonical semantic authority over the machine-readable registry;
- frozen v0.0.2 L1/L2 semantics, IDs, Target classes and 294 / 218 / 76 inventory;
- frozen v0.0.3 L3 Pattern bodies, twelve identities, `Available / M2` states, trace semantics and L3/L4 boundary;
- accepted rc02 deterministic authority-record semantics without adding per-record inferred layers or new status vocabulary;
- project Applicability / PDA / realization / verification / evidence / closure boundaries;
- initial `relations` as empty and non-semantic until a separately reviewed relation contract exists.

### Deliberately Not Added

- no schema or validator;
- no generator or hybrid registry ownership;
- no generated registry/reverse index;
- no CI enforcement or code generation;
- no automatic project applicability inference;
- no machine-readable L2→L3 relations;
- no new L3 Pattern, third tranche, SEC-primary realization, M3/M4 or L4 work.

### Gate

- independently verify YAML parseability and exact rc03 record shape;
- verify 294 / 294 unique IDs and exact 218 / 76 source classification reproduction;
- verify every record resolves through `source_path` + `source_anchor == id` to exactly one canonical source requirement block;
- verify all deterministic constants and empty `relations` values;
- verify there are no `SCAF-PAT-*` records and no project-owned state fields;
- verify rc02→rc03 frozen `docs/normative/` and `docs/l3/` byte/hash non-regression;
- return an explicit `V0.0.4 INITIAL AUTHORITY-REGISTRY SERIALIZATION GATE` decision.

## v0.0.4rc02 — 2026-08-16

Focused authority-model determinism cleanup after the independent v0.0.4rc01 review returned **PASS CONDITIONALLY / `V0.0.4 AUTHORITY-MODEL FOUNDATION GATE: YES, AFTER MINOR CLEANUP`** with 0 Critical, 0 Major, 1 Minor (`R1-01`) and 0 Trivial findings.

### Changed

- closed `R1-01` by fixing the initial `layer` semantic value to exactly `l1_l2_normative_authority`;
- prohibited serializer inference of per-record `L1`/`L2` classification where the frozen source does not provide such a record-level classification;
- fixed initial `source_anchor` to exactly the authority `id` and defined canonical resolution as exactly one matching requirement heading/block inside `source_path`;
- explicitly rejected renderer-generated Markdown slugs, line numbers and generated-index positions as canonical authority anchors;
- fixed the only initial record `status` value to exactly `represented`, with representation-only meaning and no source/project lifecycle, applicability, compliance, verification, closure, maturity, availability or Pattern-selection semantics;
- made the initial `relations` population rule explicitly empty/omitted unless a separately reviewed relation contract exists;
- added `docs/executable-governance/01_SCAF_v0.0.4rc02_Authority_Model_Determinism_Cleanup.md`;
- synchronized current README and executable-governance navigation/gate wording to rc02.

### Preserved

- frozen v0.0.2 L1/L2 normative semantics, identities and 294 / 218 / 76 inventory;
- frozen v0.0.3 L3 Pattern bodies, twelve identities, `Available / M2` states, trace semantics and L3/L4 boundary;
- frozen normative Markdown as canonical semantic authority;
- exactly two initial authority classes;
- project Applicability / PDA / realization / verification / evidence / closure boundaries;
- exclusion of all `SCAF-PAT-*` identities from the initial normative authority-record population.

### Deliberately Not Added

- no 294-record `authority-registry.yaml` or equivalent serialization;
- no schema or validator;
- no generated registry/reverse index;
- no CI enforcement or code generation;
- no automatic applicability inference;
- no new L3 Pattern, third tranche, SEC-primary realization, M3/M4 or L4 work.

### Gate

- independently verify `R1-01` is fully closed;
- verify all three mandatory-field semantics are deterministic and non-authority-expanding;
- verify initial `relations` remain empty/omitted;
- verify rc01→rc02 frozen-upstream non-regression;
- verify no registry/schema/validator/CI/codegen or catalog-expansion scope was pulled into rc02;
- return an explicit `V0.0.4 AUTHORITY-MODEL DETERMINISM CLOSURE GATE` decision.

## v0.0.4rc01 — 2026-08-16

First post-v0.0.3 executable-governance development RC. This release defines the semantic authority model that must be reviewed before any machine-readable authority registry, schema, validator or CI enforcement is introduced.

### Added

- added `docs/executable-governance/README.md` as the controlled development scope/order/gate entry point;
- added `docs/executable-governance/00_SCAF_Machine_Readable_Authority_Model.md`;
- defined canonical-source precedence: frozen normative Markdown remains semantic authority and a machine-readable representation cannot override it;
- bounded the initial future registry population to the frozen v0.0.2 inventory of 294 requirement IDs / 218 Project-Applicable Obligations / 76 Framework Normative Invariants;
- defined stable record identity, initial authority classes, minimum semantic fields, representation lifecycle/staleness behavior, completeness criteria and fail-closed authority-resolution expectations;
- explicitly separated project-owned applicability/PDA/realization/verification/evidence/closure state from the framework authority registry;
- explicitly kept the twelve frozen v0.0.3 `SCAF-PAT-*` identities outside the initial normative authority-record population.

### Preserved

- frozen v0.0.2 L1/L2 normative semantics and 294 stable requirement identities;
- frozen v0.0.3 L3 catalog semantics, twelve Pattern identities, `Available / M2` states, trace relations and L3/L4 boundary;
- human semantic authority before executable representation;
- project Design Authority / Verification Authority / closure boundaries.

### Deliberately Not Added

- no `authority-registry.yaml` or other registry serialization;
- no JSON Schema or alternate schema language;
- no validator implementation or test fixture;
- no generated registry/reverse index;
- no CI enforcement or code generation;
- no automatic project applicability inference;
- no third-tranche Pattern, SEC-primary realization, M3/M4 or L4 expansion.

### Gate

- independently verify the new authority model does not create a competing normative authority source;
- verify the initial 294-record population boundary and 218/76 Target-class preservation are consistent with the frozen v0.0.2 baseline;
- verify project application/PDA/realization/verification/evidence/closure state remains outside the framework registry;
- verify L3 Pattern identities are not promoted into normative authority records;
- verify identity, completeness, conflict/staleness and fail-closed semantics are precise enough for a later serialization RC;
- return an explicit `V0.0.4 AUTHORITY-MODEL FOUNDATION GATE` decision without implementing the registry/schema/validator.

## v0.0.3 — 2026-08-16

Frozen L3 Pattern / Mechanism Catalog Baseline.

This release is created by explicit governance freeze decision after the independent `v0.0.3rc14` final-navigation closure review returned **`L3 V0.0.3 FREEZE-CANDIDATE CLOSURE GATE: YES`**, recorded upstream finding `R12-01` as **RESOLVED**, opened no Critical, Major, Minor or Trivial finding, confirmed the frozen v0.0.2 baseline, verified exactly twelve published Pattern identities, reproduced 12 / 12 rc13→rc14 Pattern-body non-regression checks, preserved the `FTL-001` trace closure, and found no separately gated scope expansion.

### Frozen

- L3 catalog-governance semantics;
- L3 Pattern metadata contract;
- L3 trace and project-selection semantics;
- twelve published Pattern identities;
- twelve `Available / M2 — Architecture Reviewed` lifecycle states;
- initial-seven `Introduced In v0.0.3rc03` history;
- second-five `Introduced In v0.0.3rc08` history;
- immutable primary-family identity and `Supersedes: None` state;
- reviewed Pattern architecture/trace/authority/L3-L4 boundaries.

### Semantic Change from v0.0.3rc14

- **None intended.**
- The freeze action changes release/freeze state and current release metadata only.
- Pattern bodies and trace relations remain semantically unchanged from the independently reviewed rc14 tree.
- The frozen v0.0.2 normative tree remains byte-stable at 294 / 218 / 76.

### Added

- `docs/l3/14_L3_v0.0.3_Freeze_Decision.md` as the formal freeze record.

### Not Included / Still Separately Gated

- third-tranche catalog expansion;
- deferred EVD export/transformation authoring;
- rejected/reframe PST configuration-activation authoring;
- SEC-primary realization;
- M3/M4;
- L4 implementation/verification guidance;
- schema, validator, generated registry/reverse index, CI, code generation or executable governance.

### Governance

- `v0.0.3` is frozen and shall not be modified in place.
- Later semantic work must continue on a new controlled RC development line.

## v0.0.3rc14 — 2026-08-16

Final freeze-candidate navigation cleanup after the independent v0.0.3rc13 focused closure review returned **`L3 V0.0.3 FREEZE-CANDIDATE CLOSURE GATE: YES, AFTER MINOR CLEANUP`**. The review confirmed the architecture/trace/lifecycle baseline, frozen normative integrity, 12 / 12 Pattern-body non-regression, `FTL-001` trace closure, and scope control; it opened no new/regression finding. The sole remaining residue of upstream `R12-01` was one stale active `Immediate Gate` paragraph in `docs/l3/03_L3_Pattern_Index.md`.

### Changed

- updated `docs/l3/03_L3_Pattern_Index.md` `## 5. Immediate Gate` from the stale rc12 review position to the rc14 final-navigation closure position;
- synchronized current release/navigation wording to v0.0.3rc14;
- added this rc14 release record as the final cleanup RC before any explicit freeze decision.

### Preserved

- exactly twelve published numeric `SCAF-PAT-*` identities;
- all twelve as `Available / M2 — Architecture Reviewed`;
- initial-seven `Introduced In: v0.0.3rc03`;
- second-five `Introduced In: v0.0.3rc08`;
- all immutable primary families, `Supersedes: None`, Pattern bodies and trace relations apart from current Development Release metadata;
- the rc09 `FTL-001` `SCAF-ROB-007` Constraint Input / `SCAF-ROB-015` Supporting closure;
- frozen v0.0.2 normative content and all 294 IDs / 218 Project-Applicable Obligations / 76 Framework Normative Invariants;
- many-to-many L2→L3 trace, bounded `Available` semantics, PDA/source-authority ownership and L3/L4 separation.

### Deliberately Not Added / Promoted

- v0.0.3 is **not frozen by rc14**;
- no thirteenth Pattern ID or third tranche;
- no deferred EVD Pattern, revived rejected/reframe PST Pattern or SEC-primary Pattern;
- no M3/M4, L4, schema, validator, generated registry/reverse index, CI, code generation or executable governance.

### Gate

- independently verify upstream `R12-01` is fully resolved;
- verify no stale active rc12/rc13 immediate-gate text remains in current navigation surfaces;
- verify rc13→rc14 12 / 12 Pattern-body non-regression with only Development Release metadata changes;
- verify the frozen v0.0.2 baseline remains byte-stable;
- return an explicit `L3 V0.0.3 FREEZE-CANDIDATE CLOSURE GATE` decision without performing the freeze.

## v0.0.3rc13 — 2026-08-16

Focused freeze-candidate release-record cleanup after the independent v0.0.3rc12 review returned **`FREEZE CANDIDATE NEEDS MINOR CLEANUP` / `L3 V0.0.3 FREEZE-CANDIDATE GATE: YES, AFTER MINOR CLEANUP`** with 0 Critical, 0 Major, 1 Minor (`R12-01`) and 0 Trivial findings.

### Changed

- updated root README current release/gate wording from the stale rc11 availability-acceptance position to the rc13 freeze-candidate closure position;
- added rc12 and rc13 to the root README current sequence;
- replaced stale `No CI is included in v0.0.3rc09` wording with release-stable `No CI is included in the v0.0.3 L3 baseline`;
- replaced `v0.0.3rc06 intentionally does not define:` in the living L3 metadata contract with `The v0.0.3 L3 baseline intentionally does not define:`;
- added `docs/l3/12_L3_v0.0.3_Freeze_Candidate_Release_Record_Cleanup.md`;
- synchronized current L3 README, governance, index and catalog navigation wording to the rc13 focused closure gate;
- corrected the rc12 CHANGELOG cleanup claim so the historical release record reflects the actual rc12 reviewed tree.

### Preserved

- exactly twelve published numeric `SCAF-PAT-*` identities;
- all twelve as `Available / M2 — Architecture Reviewed`;
- initial-seven `Introduced In: v0.0.3rc03`;
- second-five `Introduced In: v0.0.3rc08`;
- all immutable primary families, `Supersedes: None`, Pattern bodies and trace relations apart from current Development Release metadata;
- the rc09 `FTL-001` `SCAF-ROB-007` Constraint Input / `SCAF-ROB-015` Supporting closure;
- frozen v0.0.2 normative content and all 294 IDs / 218 Project-Applicable Obligations / 76 Framework Normative Invariants;
- many-to-many L2→L3 trace, bounded `Available` semantics, PDA/source-authority ownership and L3/L4 separation.

### Deliberately Not Added / Promoted

- v0.0.3 is **not frozen by rc13**;
- no thirteenth Pattern ID or third tranche;
- no deferred EVD Pattern, revived rejected/reframe PST Pattern or SEC-primary Pattern;
- no M3/M4, L4, schema, validator, generated registry/reverse index, CI, code generation or executable governance.

### Gate

- independently verify `R12-01` is fully resolved;
- verify root README, L3 navigation/contract surfaces and CHANGELOG tell one coherent rc13 freeze-candidate closure story;
- verify rc12→rc13 12 / 12 Pattern-body non-regression with only Development Release metadata changes;
- verify the frozen v0.0.2 baseline remains byte-stable;
- return an explicit `L3 V0.0.3 FREEZE-CANDIDATE CLOSURE GATE` decision without performing the freeze.

## v0.0.3rc12 — 2026-08-16

L3 milestone consolidation / freeze-candidate audit preparation after the independent v0.0.3rc11 availability-acceptance review returned **PASS / `L3 SECOND-TRANCHE PATTERN-AVAILABILITY ACCEPTANCE GATE: YES`**, confirmed all twelve entries as `Available / M2`, reproduced 12 / 12 Pattern-body non-regression hashes, preserved the frozen v0.0.2 baseline and opened no Critical, Major, Minor or Trivial finding.

### Added

- added `docs/l3/11_L3_v0.0.3_Milestone_Consolidation_and_Freeze_Candidate.md`;
- consolidated the complete v0.0.3 L3 review/lifecycle evidence from rc01 through rc11;
- defined explicit freeze-candidate criteria covering frozen-upstream integrity, twelve-ID stability, lifecycle semantics, Pattern-body non-regression, contract coherence, finding closure, authority preservation, bounded deferral and release-record consistency;
- defined the proposed v0.0.3 L3 frozen scope if a later explicit freeze decision is made.

### Changed

- updated current release/navigation/gate metadata to v0.0.3rc12;
- updated release-facing freeze-candidate wording and identified the remaining stale point-release metadata-contract wording for cleanup before freeze.
- normalized historical second-tranche decision-record `Development Release` labels so `07` / `08` / `09` / `10` identify their actual originating releases rc08 / rc09 / rc10 / rc11 instead of inheriting the current development release.

### Preserved

- exactly twelve published numeric `SCAF-PAT-*` identities;
- all twelve as `Available / M2 — Architecture Reviewed`;
- initial-seven `Introduced In: v0.0.3rc03` history;
- second-five `Introduced In: v0.0.3rc08` history;
- all immutable primary families and `Supersedes: None`;
- all Pattern architecture/trace bodies apart from current Development Release metadata;
- the rc09 `FTL-001` `SCAF-ROB-007` Constraint Input / `SCAF-ROB-015` Supporting closure;
- frozen v0.0.2 normative content and all 294 IDs / 218 Project-Applicable Obligations / 76 Framework Normative Invariants;
- many-to-many L2→L3 trace, PDA/source-authority, `Available` semantics and L3/L4 boundaries.

### Deliberately Not Added / Promoted

- v0.0.3 is **not frozen by rc12**;
- no thirteenth Pattern ID or third tranche;
- no deferred EVD Pattern;
- no revived rejected/reframe PST Pattern;
- no SEC-primary Pattern;
- no M3/M4, L4, schema, validator, generated registry/reverse index, CI, code generation or executable governance.

### Gate

- independently verify the complete v0.0.3 L3 milestone as a bounded freeze candidate;
- verify rc11→rc12 12 / 12 Pattern-body non-regression with only Development Release metadata changes;
- verify all review findings are closed and all release records are mutually consistent;
- determine whether deferred work is cleanly isolated future scope rather than an unresolved v0.0.3 baseline defect;
- return an explicit `L3 V0.0.3 FREEZE-CANDIDATE GATE` decision without performing the freeze.

## v0.0.3rc11 — 2026-08-16

Second-tranche catalog availability acceptance after the independent v0.0.3rc10 maturity / availability review returned **PASS / `L3 SECOND-TRANCHE PATTERN-LIFECYCLE GATE: YES`**, validated **5 / 5 `M2 VALID`**, judged **5 / 5 `READY FOR AVAILABLE`**, confirmed **12 / 12 Pattern-body non-regression PASS**, and opened no new Critical, Major, Minor or Trivial finding.

### Changed

- explicitly promoted `SCAF-PAT-FTL-001`, `SCAF-PAT-FTL-002`, `SCAF-PAT-TIM-001`, `SCAF-PAT-TIM-002`, and `SCAF-PAT-SYN-001` from `Catalog Status: Candidate` to `Catalog Status: Available`;
- retained `M2 — Architecture Reviewed` for all five; no M3/M4 maturity claim is made;
- retained each second-tranche Pattern ID, immutable primary family and `Introduced In: v0.0.3rc08` value;
- added `docs/l3/10_L3_Second_Tranche_Availability_Acceptance.md` as the release-scoped explicit catalog acceptance record;
- updated current README, L3 navigation/index, governance gate and Pattern release/status metadata for v0.0.3rc11.

### Availability Evidence Basis

- rc10 independently validated all five M2 states;
- rc10 independently judged all five entries `READY FOR AVAILABLE`;
- rc10 verified 12 / 12 controlled Pattern-body normalized hashes;
- rc10 opened no cleanup finding and preserved the rc09 `FTL-001` trace closure;
- the rc10 review performed no automatic Catalog Status transition, preserving the requirement for this later explicit repository lifecycle decision.

### Preserved

- all twelve published Pattern IDs and immutable primary families;
- the initial seven `Available / M2 / Introduced In: v0.0.3rc03` states;
- the second five `M2 — Architecture Reviewed / Introduced In: v0.0.3rc08` states;
- all Pattern architecture/trace bodies apart from current Development Release and the five intended Catalog Status metadata transitions;
- exactly twelve numeric `SCAF-PAT-*` identities and no `Supersedes` event;
- frozen v0.0.2 `docs/normative/` content and all 294 normative IDs / 218 Project-Applicable Obligations / 76 Framework Normative Invariants;
- many-to-many L2→L3 trace, PDA/source-authority and L3/L4 boundaries.

### Deliberately Not Added / Promoted

- no thirteenth Pattern ID or third tranche;
- no M3/M4 promotion;
- no deferred EVD export/transformation Pattern;
- no revived rejected/reframe PST configuration-activation Pattern;
- no SEC-primary Pattern;
- no L4, schema, validator, generated registry/reverse index, CI, code generation or executable governance.

### Gate

- independently verify all five rc10 readiness recommendations support the rc11 acceptance transitions;
- verify the transition is lifecycle-only with no mechanism/trace rewrite;
- verify all twelve IDs/families/history and frozen v0.0.2 baseline remain stable;
- verify `Available` retains its bounded catalog meaning and does not become project selection/compliance/satisfaction authority.

## v0.0.3rc10 — 2026-08-16

Second-tranche lifecycle decision after the independent v0.0.3rc09 focused review returned **PASS / `L3 SECOND-TRANCHE TRACE-CLOSURE GATE: YES`**, confirmed `R8-01` Resolved and found no new Critical, Major, Minor or Trivial finding.

### Changed

- added `docs/l3/09_L3_Second_Tranche_Lifecycle_Decision.md` as the release-scoped second-tranche maturity decision record;
- advanced `SCAF-PAT-FTL-001`, `SCAF-PAT-FTL-002`, `SCAF-PAT-TIM-001`, `SCAF-PAT-TIM-002`, and `SCAF-PAT-SYN-001` from `M1 — Structured` to `M2 — Architecture Reviewed`;
- retained `Catalog Status: Candidate` for all five so maturity and availability remain independent lifecycle axes;
- updated current release/navigation/gate wording for v0.0.3rc10.

### Evidence Basis

- rc08 independently reviewed all five second-tranche entries for family/mechanism fit, L2 trace, authority boundaries, non-duplication, PDA ownership and L3/L4 conformance;
- rc09 corrected the sole Minor `R8-01` in `FTL-001` and its focused review confirmed the finding fully Resolved with no regression;
- the frozen v0.0.2 baseline and twelve published Pattern identities remain stable.

### Preserved

- all five second-tranche IDs, immutable primary families, `Candidate` status and `Introduced In: v0.0.3rc08`;
- all seven initial-tranche `Available / M2 / Introduced In v0.0.3rc03` states;
- all Pattern architecture/trace bodies except current Development Release and the five intended Maturity metadata changes;
- exactly twelve numeric `SCAF-PAT-*` identities and no `Supersedes` event;
- frozen v0.0.2 `docs/normative/` content and all 294 normative IDs / 218 Project-Applicable Obligations / 76 Framework Normative Invariants;
- many-to-many trace, PDA/source-authority and L3/L4 boundaries.

### Deliberately Not Added / Promoted

- no `Candidate`→`Available` transition for the five second-tranche entries;
- no deferred EVD export/transformation Pattern;
- no revived PST configuration-activation Pattern;
- no SEC-primary Pattern;
- no third tranche, M3/M4, L4, schema, validator, generated registry/index, CI, code generation or executable governance.

### Gate

- independently validate M2 for each of the five second-tranche entries;
- independently assess `READY FOR AVAILABLE` entry by entry without changing status;
- reconfirm `FTL-001` `ROB-007` Constraint Input closure, twelve-ID inventory, initial-seven non-regression and frozen-baseline integrity.

## v0.0.3rc09 — 2026-08-16

Focused second-tranche trace cleanup after the independent v0.0.3rc08 Pattern review returned **PASS WITH MINOR CLEANUP / `L3 SECOND-TRANCHE PATTERN GATE: YES, AFTER MINOR CLEANUP`**, with **0 Critical, 0 Major and 1 Minor** finding.

### Changed

- added `docs/l3/08_L3_Second_Tranche_Trace_Cleanup.md` as the release-scoped `R8-01` closure record;
- corrected `SCAF-PAT-FTL-001` by moving `SCAF-ROB-007` from `Supporting L2 Trace` to `Constraint Inputs`;
- revised `FTL-001` detailed trace rationale so the project-identified material failure-propagation path is explicitly consumed as an upstream constraint on containment placement/configuration rather than represented as FTL-owned realization;
- retained `SCAF-ROB-015` as the Supporting Realization identified by the rc08 review;
- updated current release/gate/navigation metadata for v0.0.3rc09.

### Preserved

- `SCAF-PAT-FTL-001` ID, immutable `FTL` primary family, Candidate/M1 lifecycle state and `Introduced In: v0.0.3rc08`;
- the other four second-tranche Pattern architecture/trace bodies unchanged except current Development Release metadata;
- the initial seven Pattern architecture/trace bodies and `Available / M2` lifecycle states unchanged except current Development Release metadata;
- exactly twelve numeric `SCAF-PAT-*` identities; no thirteenth identity or `Supersedes` event;
- frozen v0.0.2 `docs/normative/` content and all 294 normative IDs / 218 Project-Applicable Obligations / 76 Framework Normative Invariants;
- many-to-many L2→L3 trace semantics, PDA/source-authority boundaries and the L3/L4 boundary.

### Deliberately Not Added / Promoted

- no M2 or `Available` promotion for the five second-tranche entries;
- no authoring of the deferred EVD export/transformation category;
- no Pattern ID for the rejected/reframe PST configuration-activation proposal;
- no SEC-primary Pattern;
- no third tranche, M3/M4, L4, schema, validator, generated registry/index, CI, code generation or executable governance.

### Gate

- independently verify `R8-01` is Resolved and `SCAF-ROB-007` is now a Constraint Input in `FTL-001`;
- verify `SCAF-ROB-015` remains Supporting Realization and `FTL-001` identity/lifecycle/family remain stable;
- verify the other eleven Pattern architecture bodies are non-regressed except Development Release metadata;
- reconfirm frozen v0.0.2 byte stability and the 294 / 218 / 76 inventory;
- do not auto-promote or open additional catalog scope from this cleanup RC alone.

## v0.0.3rc08 — 2026-08-16

Controlled second representative L3 Pattern tranche after the independent v0.0.3rc07 coverage / second-tranche planning review returned **PASS / `L3 SECOND-TRANCHE PLANNING GATE: YES`**, approved six later-authoring categories, rejected/reframed the PST configuration-activation proposal, preserved the SEC-primary hold, and opened no Critical, Major, Minor or Trivial release finding.

### Added

- added `docs/l3/07_L3_Second_Tranche_Authoring_Decision.md` recording the rc07 category dispositions and the deliberately limited rc08 authoring scope;
- published five new permanent Pattern identities as `Candidate / M1` entries:
  - `SCAF-PAT-FTL-001` — Failure-Domain Containment / Isolation;
  - `SCAF-PAT-FTL-002` — Controlled Failover with Graceful Degradation;
  - `SCAF-PAT-TIM-001` — Bounded Queue / Backpressure / Overload Protection;
  - `SCAF-PAT-TIM-002` — Timebase / Clock-Relationship / Epoch Validity;
  - `SCAF-PAT-SYN-001` — Generation/Epoch-Based Cross-Participant State Convergence;
- opened the previously empty `FTL`, `TIM` and `SYN` mechanism families with structured architecture-level entries;
- added explicit cross-family composition/boundary statements for FTL containment versus failover, TIM capacity versus ROB/INT authority, and SYN convergence versus existing COM reconnect semantics.

### Preserved

- the initial seven published Pattern identities as `Available / M2`, all still `Introduced In: v0.0.3rc03`;
- initial seven Pattern architecture/trace content unchanged except current Development Release metadata;
- frozen v0.0.2 `docs/normative/` content and all 294 normative IDs / 218 Project-Applicable Obligations / 76 Framework Normative Invariants;
- many-to-many L2→L3 trace semantics and the prohibition on generic L2→L3 `satisfies` shortcuts;
- Project Design Authority ownership of project mechanism selection/configuration and external source-authority ownership;
- L3/L4 boundary and separate later gates.

### Deliberately Deferred / Rejected

- the rc07-approved Evidence Retrieval / Export / Transformation Integrity (`EVD`) category is deferred to keep rc08 focused on the new FTL/TIM/SYN family stress test;
- no ID is allocated for Controlled Configuration Activation / Source Precedence (`PST`), which remains `REJECT / REFRAME` pending a stable principal mechanism/family basis;
- no SEC-primary Pattern is authored before the dedicated security-realization gate;
- no new Pattern is promoted beyond Candidate/M1;
- no M3/M4, L4, schema, validator, generated registry/index, CI, code generation or executable governance is introduced.

### Gate

- independently review all five new Candidate/M1 Patterns for family fit, trace classification, PDA/source-authority preservation, non-duplication, composition and L3/L4 conformance;
- verify `FTL-001` does not redefine ARCH Domains and `FTL-002` remains distinct from containment/retry/universal redundancy;
- verify TIM entries preserve TIME-owned measurable semantics while INT/ROB/RUN retain their downstream authorities;
- verify `SYN-001` complements rather than reclassifies/duplicates `SCAF-PAT-COM-001` and does not prescribe consensus/leader algorithms;
- reconfirm the initial seven Available/M2 entries and frozen v0.0.2 baseline are non-regressed;
- do not auto-promote the five new entries or open the deferred/rejected/security/L4/executable-governance scopes from this authoring RC alone.
## v0.0.3rc07 — 2026-08-16

L3 catalog trace-reference coverage and second-tranche planning after the independent v0.0.3rc06 availability-acceptance review returned **PASS / `INITIAL L3 PATTERN-AVAILABILITY ACCEPTANCE GATE: YES`**, validated **7 / 7 `AVAILABLE ACCEPTANCE VALID`**, confirmed **7 / 7 pattern-body non-regression**, and opened no Critical, Major, Minor or Trivial finding.

### Added

- added `docs/l3/06_L3_Catalog_Coverage_and_Second_Tranche_Planning.md` as a descriptive, human-readable coverage and expansion-planning artifact;
- established **trace-reference coverage** semantics that explicitly do not mean project applicability, compliance, obligation satisfaction or catalog completeness;
- recorded the current seven-pattern explicit trace surface: 60 distinct frozen Project-Applicable Obligations; two additional Framework Invariants appear only as provenance/mechanism-boundary references and are excluded from trace-coverage counts;
- added concern-level coverage counts and interpretations that distinguish expected low pattern coverage in AK/CTX/ARCH/RUN from actual reusable mechanism opportunities;
- added a controlled second-tranche prioritization model based on mechanism reuse, L2 leverage, taxonomy stress value, cross-concern value, technology neutrality, non-duplication and reviewability;
- proposed seven planning-only candidate categories across FTL, TIM, SYN, EVD and PST without allocating any Pattern ID;
- retained SEC realization behind a separate security-specific abstraction/review gate.

### Preserved

- exactly seven published Pattern IDs, all `Available / M2` and all introduced in v0.0.3rc03;
- existing Pattern mechanism bodies, L2 trace relations, immutable primary families and lifecycle states;
- frozen v0.0.2 `docs/normative/` content and all 294 normative IDs / 218 Project-Applicable Obligations / 76 Framework Normative Invariants;
- many-to-many L2→L3 trace semantics and the prohibition on generic L2→L3 `satisfies` shortcuts;
- Project Design Authority ownership of actual mechanism selection/configuration;
- L3/L4 boundary and later gates on M3/M4, L4 and executable governance.

### Deliberately Not Added / Promoted

- no eighth Pattern ID or second-tranche Pattern entry;
- no change to `Available / M2` lifecycle state of the initial seven patterns;
- no M3/M4 maturity claim;
- no SEC Pattern entry;
- no L4 implementation/verification guidance;
- no schema, validator, generated registry/index, CI, code generation or executable-governance machinery.

### Gate

- independently review whether trace-reference coverage is represented correctly and cannot be confused with satisfaction/compliance/completeness;
- verify concern-level low coverage is not automatically treated as a catalog defect;
- review each proposed second-tranche category for reusable mechanism intent, family fit, non-duplication and L3/L4 safety;
- decide which candidate categories, if any, may receive Pattern IDs in the next RC;
- keep security realization, M3/M4, L4 and executable-governance work separately gated.

# Changelog

## v0.0.3rc06 — 2026-08-16

Initial L3 pattern-tranche availability acceptance after the independent v0.0.3rc05 maturity / availability review returned **PASS / `INITIAL L3 PATTERN-LIFECYCLE GATE: YES`**, validated **7 / 7 `M2 VALID`**, judged **7 / 7 `READY FOR AVAILABLE`**, and opened no new Critical, Major, Minor or Trivial finding.

### Changed

- explicitly promoted all seven published initial-tranche entries from `Catalog Status: Candidate` to `Catalog Status: Available`;
- retained `M2 — Architecture Reviewed` for all seven entries; no M3/M4 maturity claim is made;
- retained every published Pattern ID, immutable primary family and `Introduced In: v0.0.3rc03` value;
- added `docs/l3/05_L3_Initial_Tranche_Availability_Acceptance.md` as the release-scoped catalog acceptance record;
- updated current README, L3 navigation/index, governance gate and pattern release/status metadata for v0.0.3rc06;
- kept Pattern architecture bodies, L2 trace semantics, PDA decisions, external-authority boundaries and L3/L4 boundaries unchanged apart from release/status lifecycle metadata.

### Availability Evidence Basis

- the rc05 independent review verified exact archive identity and frozen-baseline byte stability;
- all seven entries were independently assessed `M2 VALID`;
- all seven entries were independently assessed `READY FOR AVAILABLE`;
- no Critical/Major/Minor/Trivial cleanup item remained before explicit catalog acceptance;
- the review performed no automatic status transition, preserving the requirement for a later explicit repository lifecycle decision now recorded by rc06.

### Preserved

- exactly seven published Pattern IDs; no eighth identity;
- `M2 — Architecture Reviewed` for every entry;
- `Introduced In: v0.0.3rc03` for every entry;
- immutable primary families and `Supersedes: None` lifecycle state;
- frozen v0.0.2 `docs/normative/` content and all 294 normative IDs / 218 Project-Applicable Obligations / 76 Framework Normative Invariants;
- many-to-many L2→L3 trace semantics and the prohibition on generic L2→L3 `satisfies` shortcuts;
- Project Design Authority ownership of project mechanism selection/configuration and external source-authority ownership of external constraints;
- L3/L4 boundary and gates on schema, validator, CI, code generation and executable governance.

### Deliberately Not Added / Promoted

- no second pattern tranche or eighth Pattern ID;
- no M3/M4 maturity claim;
- no primary-family move, Pattern-ID replacement or `Supersedes` event;
- no L4 implementation / verification guidance;
- no schema, validator, generated registry/index, CI, code generation or executable-governance machinery.

### Gate

- independently confirm that the rc06 Candidate→Available transitions are supported by the rc05 entry-by-entry readiness evidence;
- confirm all seven identities remain Available/M2 with unchanged family and introduction history;
- confirm pattern architecture/trace content did not change to obtain availability;
- reconfirm frozen v0.0.2 integrity and accepted catalog-lifecycle semantics;
- only after a successful rc06 review may the initial seven-pattern availability milestone be considered closed; second-tranche, M3, L4 and executable-governance work remain separate decisions.

## v0.0.3rc05 — 2026-08-16

Initial L3 pattern-tranche maturity decision after the independent v0.0.3rc04 trace-closure review returned **PASS / `INITIAL L3 PATTERN-TRANCHE TRACE-CLOSURE GATE: YES`**, with `R3-01` through `R3-04` fully Resolved and no new Critical, Major, Minor or Trivial finding.

### Changed

- advanced all seven published initial-tranche patterns from `M1 — Structured` to `M2 — Architecture Reviewed`;
- retained `Catalog Status: Candidate` for all seven entries so maturity and catalog availability remain independent lifecycle axes;
- added a release-scoped initial-tranche lifecycle decision record documenting the M2 evidence basis and the separate `Available` acceptance gate;
- clarified catalog governance so M2 promotion requires completed independent architecture review/closure of material authority, trace and L3/L4 findings;
- clarified that Candidate→Available is a separate explicit catalog acceptance decision and does not follow automatically from M2;
- advanced current L3 development labels and release/gate wording to v0.0.3rc05.

### M2 Evidence Basis

- v0.0.3rc03 independently reviewed all seven entries for authority boundary, L2 trace, primary-family placement, PDA/external-authority separation and L3/L4 conformance;
- v0.0.3rc04 closed all four localized Minor trace findings from that review;
- the rc04 focused closure review confirmed all four findings Resolved and found no new Critical/Major/Minor/Trivial regression;
- the seven IDs, immutable primary families, index counts and frozen v0.0.2 baseline remain stable.

### Preserved

- the same seven published Pattern IDs and immutable primary families introduced in v0.0.3rc03;
- `Catalog Status: Candidate` for every current pattern;
- `Introduced In: v0.0.3rc03` for all seven identities;
- frozen v0.0.2 `docs/normative/` content and all 294 normative IDs / 218 Project-Applicable Obligations / 76 Framework Normative Invariants;
- many-to-many L2→L3 trace semantics and the prohibition on generic L2→L3 `satisfies` shortcuts;
- Project Design Authority ownership of project mechanism selection/configuration and external source-authority ownership of external constraints;
- L3/L4 boundary and gates on schema, validator, CI, code generation and executable governance.

### Deliberately Not Added / Promoted

- no Candidate→Available transition in this RC;
- no eighth Pattern ID, second tranche, primary-family move, `Supersedes` event or Pattern-ID replacement;
- no M3/M4 maturity claim;
- no L4 implementation / verification guidance;
- no schema, validator, CI or executable-governance machinery.

### Gate

- independently verify the M2 evidence basis for each of the seven entries;
- assess Candidate→Available readiness entry by entry using the catalog lifecycle criteria, without auto-promoting any entry;
- reconfirm Pattern identity/family, frozen-baseline integrity, L2 trace, PDA/external-authority and L3/L4 boundaries;
- only after a successful rc05 review may a later RC explicitly promote reviewed entries to `Available` and separately decide whether a small second tranche should begin.

## v0.0.3rc04 — 2026-08-16

Localized initial L3 pattern-tranche trace cleanup after the independent v0.0.3rc03 review returned **PASS WITH MINOR CLEANUP / `INITIAL L3 PATTERN-TRANCHE GATE: YES, AFTER MINOR CLEANUP`**, with no Critical or Major finding and four Minor trace-contract findings.

### Changed

- resolved `R3-01` in `SCAF-PAT-SUP-002` by removing `SCAF-ROB-032` from Primary Realization Candidate trace and removing `SCAF-LIFE-008` / `SCAF-LIFE-009` from Supporting Realization while retaining those LIFE obligations as reset-semantics Constraint Inputs;
- clarified that any downstream repeated recovery/escalation is where applicable `SCAF-ROB-032` termination semantics are evaluated, without giving the watchdog recovery authority;
- resolved `R3-02` in `SCAF-PAT-REC-001` by adding conditional `SCAF-INT-007` duplicate/order semantics for repeated/interleaved Interaction exchanges and conditional `SCAF-INT-010` session-incarnation semantics where retry continuity crosses/reuses connection sessions, while retaining `SCAF-INT-013` for negative/non-conforming Interaction outcomes;
- resolved `R3-03` in `SCAF-PAT-LCM-001` by adding `SCAF-RUN-009` as the explicit LIFE-to-RUN readiness-handoff Constraint Input and preserving separate LIFE update/activation and RUN readiness authorities;
- resolved `R3-04` in `SCAF-PAT-EVD-001` by adding `SCAF-OBS-009` as the causal/derived-inference claim-basis Constraint Input so recorder evidence cannot self-author root-cause claims;
- advanced current L3 development labels and release/gate wording to v0.0.3rc04.

### Preserved

- all seven published Pattern IDs and immutable primary families;
- `Catalog Status: Candidate` and `Maturity: M1 — Structured` for every current pattern;
- frozen v0.0.2 `docs/normative/` content and all 294 normative IDs / 218 Project-Applicable Obligations / 76 Framework Normative Invariants;
- many-to-many L2→L3 trace semantics and the prohibition on generic L2→L3 `satisfies` shortcuts;
- Project Design Authority ownership of project mechanism selection/configuration and external source-authority ownership of external constraints;
- L3/L4 boundary and gates on schema, validator, CI, code generation and executable governance.

### Deliberately Not Added / Promoted

- no eighth Pattern ID or second pattern tranche;
- no primary-family move, `Supersedes` lifecycle event or Pattern-ID replacement;
- no Candidate→Available promotion;
- no M1→M2 promotion;
- no L4 implementation / verification guidance;
- no schema, validator, CI or executable-governance machinery.

### Gate

- run a focused independent rc04 closure review of `R3-01` through `R3-04`;
- regress all seven published IDs, primary families, Candidate/M1 states, index counts and L3/L4 boundaries;
- reconfirm the frozen v0.0.2 normative tree byte-stable and the 294 / 218 / 76 inventory unchanged;
- only after successful closure, allow the next RC to make explicit entry-by-entry M2 / `Available` decisions and separately decide whether a second tranche should begin.

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
