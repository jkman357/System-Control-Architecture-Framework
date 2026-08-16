# Read Coverage Audit

## 1. Coverage Definitions

This RC distinguishes **four levels**:

1. **Discovered** — file exists in the input archive and is listed.
2. **Machine-read** — file bytes/text were opened and inspected programmatically.
3. **Semantic role review** — the artifact's engineering/repository role and migration disposition were assessed.
4. **Deep normative audit** — detailed requirement-by-requirement reconciliation, contradiction review and wording migration.

The fourth level is intentionally incomplete because SCAF requires taxonomy and authority convergence before formal large-scale rewriting.

## 2. Gen1 Coverage

| Measure | Result |
|---|---:|
| Files discovered | 72 / 72 |
| Files machine-read | 72 / 72 |
| Files included in role/disposition inventory | 72 / 72 |
| Governed authority documents identified from `authority-registry.yaml` | 23 / 23 |
| Source-heading anchors added for core mapping concepts | Yes, partial/core concepts |
| Deep normative migration audit | Not complete |

### Files not read

**None.** All 72 Gen1 files were opened/read at machine-text level during the rc1–rc05 archaeology / authority-kernel work.

### Files not yet deeply audited requirement-by-requirement

The following classes remain intentionally deferred from complete line-by-line normative migration review:

- all protocol positive/negative YAML fixtures;
- `tests/test_security_regressions.py`;
- `tests/test_validate_protocol.py`;
- `tests/test_validate_repository.py`;
- `tests/test_verify_external_anchor.py`;
- `tools/validate_protocol.py`;
- `tools/validate_repository.py`;
- `tools/verify_external_anchor.py`;
- executable schema edge cases in `schema/protocol.schema.yaml`;
- executable schema edge cases in `schema/framework-conformance-claim.schema.yaml`;
- path/digest edge cases in legal-baseline and repository-protection tooling;
- full requirement-by-requirement reconciliation of Gen1 authorities marked `Draft for Review` or RC.

These artifacts were read and their roles were analyzed. Their individual executable assertions are **not** yet promoted into SCAF requirements.

## 3. Supplemental Crash Recorder Coverage

| Measure | Result |
|---|---:|
| Files discovered | 2 / 2 |
| Files machine-read | 2 / 2 |
| Primary specification structure reviewed | Yes |
| Major resilience/evidence concepts mapped | Yes |
| Section anchors added for major donor concepts | Yes |
| Recorder API/ABI/reference implementation promoted into SCAF core | No |

### Files not read

**None.** Both supplemental files were read at machine-text level.

### Deferred deep audit

The primary README contains both generic architecture and candidate implementation contracts. rc05 maps generic architecture concepts but does not adopt every API, record layout, ABI, memory budget, persistence layout or RC implementation recommendation as SCAF policy.

## 4. Independent Review Coverage

The v0.0.1rc1, v0.0.1rc02, v0.0.1rc03, v0.0.1rc04 and v0.0.1rc05 independent architecture reviews were read and used as correction / gate evidence.

Review findings incorporated through rc05 include:

- separation of authority planes;
- Node metamodel correction and Function/Service first-class model;
- framework normative authority vs Project Design Authority separation;
- non-linear plane relation;
- CTX logical-service dependency vs ARCH structural-realization dependency partition;
- ASSUR evidence/verification ownership without stealing source-concern thresholds;
- source-anchored migration evidence and per-donor maturity binding;
- robustness semantic restructuring and fault-tolerance/distributed-failure coverage;
- Safe State external authority boundary;
- Framework Scan multi-axis iterative lifecycle plus one worked project-start scan;
- composable implementation-profile axes;
- configuration/persistent-state authority;
- `SCAF-TIME` ownership of timebase/synchronization with OBS recording provenance;
- security architecture interface boundary to external/project security authority;
- source identity vs retrievability distinction;
- one canonical Concern -> Project Design -> Realization -> Assurance chain with APP cross-cutting;
- full authority-grammar usage in normative documents; historical analysis prose may still require lexical normalization;
- Service/Capability and subordinate System/Node clarification;
- ROB/LIFE/OBS/ASSUR boundary tightening;
- Security Authority vs Project Design Authority separation;
- complete Framework Scan state/closure proof on selected worked items.
- five-plane model clarified as SCAF framework planes with Project Design Authority kept project-side;
- Governance scope narrowed to SCAF authority/change semantics rather than project organizational governance;
- time epoch separated from boot incarnation, protocol/session identity and operational incarnation;
- Applicable Satisfaction Basis terminology introduced to preserve multi-authority acceptance provenance;
- migration rows realigned for capability semantics/allocation and incident time/incarnation provenance.

The review itself is not treated as a normative SCAF source.

## 5. Mapping Confidence vs Audit Completion

A `High` mapping confidence means the source concept and intended SCAF home are clear enough for architecture planning. It does **not** mean all normative wording or source conflicts have been reconciled.

Current mapping states intentionally distinguish:

```text
High confidence + Partial audit
Medium confidence + Deferred audit
New SCAF concept
```

This prevents a broad archaeology pass from being presented as completed normative migration.

## 6. Tabletop Architecture / Application Coverage

v0.0.1 retains three non-normative architecture exercises:

1. single MCU system;
2. PC + multiple MCU system;
3. SoC + FPGA + DSP heterogeneous system.

At taxonomy level, all three remain representable without new ad-hoc top-level categories.

v0.0.1 retains complete-state worked Framework Scan traces against the PC + multiple MCU archetype for selected concerns. Each worked item instantiates:

```text
Concern / Obligation
 -> Applicability State
 -> Failure Consequence
 -> Decision State
 -> Risk State
 -> Project Design Authority Output
 -> Realization Responsibility
 -> Applicable Satisfaction Basis
 -> Verification State / Method
 -> Evidence State / Item
 -> Closure / Deviation + Acceptance Authority
 -> Re-evaluation Trigger
```

The exercise also exposes the greenfield bootstrap loop: provisional CTX/ARCH is refined by scan decisions and then re-scanned. It demonstrates closure semantics without making `SCAF-ASSUR` or `SCAF-APP` the project design/closure authority.

## 7. Why “Machine-read” Is Not “Fully Absorbed”

A repository can be fully opened without its entire normative meaning being reconciled. SCAF therefore does not claim that all Gen1 tests/schema/tool semantics are already migrated merely because every file was opened.

In particular, executable artifacts may encode invariants not fully repeated in Markdown authorities. Those invariants must be mined before any final claim that “all durable Gen1 concepts have a SCAF home.”

## 8. Remaining Audit Priorities

1. master Framework vs specialized authority overlap;
2. Application Analysis vs conformance/evidence overlap;
3. protocol guide/template/schema semantic ownership;
4. Draft/RC donor semantics before normative promotion;
5. executable invariants hidden in test fixtures/validators;
6. Coordinator/software-specific mechanisms vs system-level properties;
7. runtime diagnostics vs incident evidence vs assurance evidence;
8. donor retrievability and requirement-level source-semantic reproducibility;
9. implementation-profile precedence/composition after profile axes stabilize;
10. Draft/RC donor and executable-invariant audit before broad normative promotion or migration-completion claims.

## 9. Audit Conclusion

There are **no unread input files** among the two donor source archives used for the archaeology work.

However, there are intentionally deferred **deep normative audits**. The frozen v0.0.1 release should therefore be treated as:

> **a frozen architecture-convergence / authority-kernel baseline that permits the next development line to perform controlled normative rewrite, with explicit donor-promotion and migration-completion gates; it is not a completed migration proof.**

## 10. v0.0.2rc05 Normative Rewrite Coverage

This release retains the reviewed Authority Kernel / `SCAF-CTX` / `SCAF-ARCH` baseline and the rc04 `SCAF-INT` / `SCAF-TIME` tranche, then applies targeted corrections from the rc04 independent normative architecture review. The corrections close TIME concurrency ownership, TIME/ROB detection and long-run boundaries, synchronization-loss dependent-claim validity, and minor INT Interface/participant/validity-contract gaps.

The INT/TIME normative text remains derived from the frozen SCAF architecture authority homes and controlled mapping evidence. It does **not** bulk-promote donor-specific Draft/RC wording, schema-only invariants, validator-only invariants or test-fixture-only semantics. Those remain subject to donor-specific promotion/deep-audit gates.

Review focus for this closure RC is whether INT semantic ordering, RUN operational-state consistency, TIME measurable temporal/capacity/resource properties and ROB detection/recovery authority remain non-overlapping; whether synchronization-loss claims close cleanly; and whether INT/TIME Project-Applicable Obligations are Framework-Scan scannable before `SCAF-RUN` begins.


## 11. v0.0.2rc06 Normative Rewrite Coverage

This release begins the controlled `SCAF-RUN` L1/L2 normative tranche after the rc05 independent closure review accepted INT as Stable, TIME as Stable after minor cleanup, and confirmed a clean authority space for RUN. The Authority Kernel / CTX / ARCH / INT baselines remain substantively unchanged.

The remaining TIME cleanup is limited to splitting synchronization relationship semantics from dependent temporal-claim validity and making staged INT/RUN/ROB forward references precise. The new RUN text is derived from the frozen SCAF authority home for Runtime Behavior, State & Operational Lifecycle and does not bulk-promote donor-specific state-machine, RTOS, task/thread or recovery mechanisms.

Review focus for this RC is whether RUN cleanly owns operational-state meaning and transition consistency without re-owning INT semantic contracts, TIME measurable temporal/capacity properties, LIFE boot/reset/power/update lifecycle, ROB fault/degradation/recovery semantics, CFG persistent-state authority or OBS evidence representation; and whether RUN Project-Applicable Obligations remain Framework-Scan scannable before ROB authoring begins.

## 12. v0.0.2rc07 Normative Rewrite Coverage

This release begins the controlled `SCAF-ROB` L1/L2 normative tranche after the rc06 independent RUN review found no Critical or Major issues, accepted RUN as Stable after minor cleanup, and confirmed a clean RUN/ROB authority boundary. The Authority Kernel / CTX / ARCH / INT / TIME baselines remain substantively unchanged.

The localized RUN cleanup distinguishes Project Design Authority from runtime authoritative-current-state responsibility, normalizes framework-boundary relation grammar and improves requirement atomicity without changing the RUN authority home. Supporting Evidence-state terminology is completed using evidence-sufficiency language.

The ROB text is derived from the frozen SCAF robustness/resilience authority home and controlled mapping evidence. It does **not** bulk-promote donor-specific watchdog, heartbeat, retry, failover, reset, crash-recorder, RTOS or other mechanism wording; Draft/RC/mixed-maturity and executable-only donor semantics remain subject to donor-specific promotion/deep-audit gates.

Review focus for this RC is whether ROB cleanly owns fault/error/failure meaning, health/failure determination and resilience outcomes without re-owning RUN operational-state representation, LIFE lifecycle transactions, INT contract/session semantics, TIME measurable bounds, ARCH structural/Domain boundaries, CFG persistent-state authority, OBS evidence semantics or external safety/security/risk source authority; and whether ROB Project-Applicable Obligations remain Framework-Scan scannable before LIFE authoring begins.


## 13. v0.0.2rc08 Normative Rewrite Coverage

This release begins the controlled `SCAF-LIFE` L1/L2 normative tranche after the rc07 independent ROB review found no Critical or Major issues, accepted ROB as Stable after minor cleanup, and confirmed clean ROB/RUN, ROB/LIFE, ROB/INT, ROB/TIME, ROB/ARCH, ROB/CFG, ROB/OBS and external-authority boundaries. The Authority Kernel / CTX / ARCH / INT / TIME / RUN baselines remain substantively unchanged.

The localized ROB cleanup separates detectability from diagnostic coverage, separates recovery/repair outcome from retry/escalation termination, clarifies risk-authority provenance, separates ROB/OBS from ROB/ASSUR invariants and normalizes health/authority vocabulary without changing the ROB authority home.

The LIFE text is derived from the frozen SCAF Boot, Power, Reset & Update Lifecycle authority home and controlled donor mapping evidence. It does **not** bulk-promote donor-specific bootloader, firmware-slot, flash-write, reset-register, update-protocol, power-sequencing, RTOS or other implementation wording; Draft/RC/mixed-maturity and executable-only donor semantics remain subject to donor-specific promotion/deep-audit gates.

Review focus for this RC is whether LIFE cleanly owns lifecycle transaction/state/result, atomicity, activation/rollback and Boot Incarnation semantics without re-owning RUN readiness/current-state, ROB failure-response, INT contract/session, TIME measurable properties, ARCH structural boundaries, CFG persistent-state authority, OBS evidence semantics or external safety/security/risk source authority; and whether LIFE Project-Applicable Obligations remain Framework-Scan scannable before OBS authoring begins.

## 14. v0.0.2rc09 Normative Rewrite Coverage

This release begins the controlled `SCAF-OBS` L1/L2 normative tranche after the rc08 independent LIFE review found no Critical or Major issues, accepted LIFE as Stable after minor cleanup, and confirmed clean LIFE/RUN, LIFE/ROB, LIFE/INT, LIFE/TIME, LIFE/ARCH, LIFE/CFG, LIFE/OBS, external-authority and four-way-identity boundaries. The Authority Kernel / CTX / ARCH / INT / TIME / RUN / ROB baselines remain substantively unchanged.

The localized LIFE cleanup removes a framework self-rule from the `SCAF-LIFE-014` Project-Applicable target, narrows Boot Incarnation triggers to LIFE-controlled lifecycle instances, separates lifecycle-transition consumption eligibility from source validity, normalizes lifecycle authoritative-result responsibility/handoff vocabulary, distinguishes activation from RUN readiness/availability and replaces bare safety wording with controlled source criteria.

The OBS text is derived from the frozen SCAF Observability, Diagnostics & Incident Evidence authority home and controlled donor mapping evidence. It does **not** bulk-promote recorder APIs, retained-RAM layouts, ring buffers, flash/file/database storage, telemetry protocols, crash-recorder mechanisms or other L3/L4 realization wording; Draft/RC/mixed-maturity and executable-only donor semantics remain subject to donor-specific promotion/deep-audit gates.

Review focus for this RC is whether OBS cleanly owns observation/evidence identity, provenance, correlation, quality/availability, preservation/survivability/accessibility/export and observer-effect/self-health semantics without re-owning RUN state, ROB health/failure meaning, LIFE lifecycle result/Boot Incarnation, INT contract/session, TIME time semantics, CFG persistent-state authority, ASSUR evidence sufficiency or external safety/security/risk authority; and whether OBS Project-Applicable Obligations remain Framework-Scan scannable before CFG authoring begins.



## 15. v0.0.2rc10 Normative Rewrite Coverage

This release begins the controlled `SCAF-CFG` L1/L2 normative tranche after the rc09 independent OBS review found no Critical or Major issues, accepted OBS as Stable after minor cleanup, and confirmed clean OBS/source, OBS/RUN, OBS/ROB, OBS/LIFE, OBS/INT, OBS/TIME, OBS/CFG, OBS/ASSUR, OBS/ARCH, external-authority, four-way-identity and causal/evidence-sufficiency boundaries. The Authority Kernel / CTX / ARCH / INT / TIME / RUN / ROB / LIFE baselines remain substantively unchanged.

The localized OBS cleanup removes a framework-self rule from `SCAF-OBS-006` Project-Applicable target, normalizes Project-Applicable boundary prose as informative notes, separates causal/derived-inference claims from first-observed abnormal evidence, narrows retention/accessibility from lifecycle survivability, and fixes stale README/editorial residue without changing the OBS authority home.

The CFG text is derived from the frozen SCAF Configuration & Persistent Operational State authority home and controlled donor mapping evidence. It does **not** bulk-promote configuration file formats, schemas, validators, EEPROM/FRAM/flash layouts, databases, registries, migration engines, journaling, CRC/checksum, synchronization protocols or other L3/L4 realization wording; Draft/RC/mixed-maturity and executable-only donor semantics remain subject to donor-specific promotion/deep-audit gates.

Review focus for this RC is whether CFG cleanly owns configuration/persistent-operational-state source/classification/identity/provenance/default/validity/version/migration/commit/rollback/calibration/synchronization semantics without re-owning OBS evidence, LIFE lifecycle transaction/rollback, RUN current operational state, INT exchange/session, TIME measurable properties, ROB resilience response, ARCH structural boundaries, ASSUR evidence sufficiency or external safety/security/risk authority; and whether CFG Project-Applicable Obligations remain Framework-Scan scannable before the integrated L1/L2 consolidation gate.


## 16. v0.0.2rc11 Integrated L1/L2 Consolidation Coverage

This release adds no new concern tranche and does not reopen taxonomy. It performs the targeted pre-SEC consolidation requested by the independent rc10 CFG review after CFG was judged Stable after minor cleanup and the integrated backbone was judged Stable after targeted consolidation.

The consolidation narrows CFG/ROB corruption-versus-recovery terminology, completes derived-value provenance, normalizes CFG Project-Applicable boundary notes, hardens CFG semantic identity against physical storage locators, tightens CFG-to-OBS observability handoff semantics, adds explicit INT-valid/delivered versus CFG-accepted/committed/activated separation, and normalizes older CFG forward references across RUN/ROB/LIFE/OBS.

No new donor class is promoted by these edits. The release continues to exclude schema, validator, CI, L3 mechanism catalogs, L4 implementation guidance and `SCAF-SEC` normative authoring. Review focus is whether the existing CTX -> ARCH -> INT -> TIME -> RUN -> ROB -> LIFE -> OBS -> CFG L1/L2 backbone is integrated-clean enough to open the SEC tranche without taxonomy reopen.

## 17. v0.0.2rc12 SEC Normative Rewrite Coverage

This release begins the controlled `SCAF-SEC` L1/L2 normative tranche after the rc11 independent integrated consolidation review found no Critical/Major issues, judged the CTX -> ARCH -> INT -> TIME -> RUN -> ROB -> LIFE -> OBS -> CFG backbone Stable after minor cleanup, and cleared SEC authoring to begin with parallel lexical/target-purity cleanup.

The SEC text is derived from the frozen `SCAF-SEC — Security Architecture Interface & Robustness` authority home and the already-stabilized cross-concern boundaries. It explicitly preserves the applicable external/project Security Authority as source authority for threat assumptions/model, security objectives/requirements, security risk evaluation/acceptance, regulatory/certification security acceptance and externally imposed security constraints. SCAF-SEC defines architecture obligations and required project decisions; the Project Design Authority defines actual project trust/security architecture decisions.

The tranche remains technology-neutral and does **not** bulk-promote donor-specific cryptographic algorithms, credential formats, secure-boot mechanisms, secure elements, access-control implementations, firewalls, protocol security mechanisms, schema-only invariants, validator-only rules or test-fixture-only semantics. Those remain gated for later L3/L4 or donor-specific promotion review.

Review focus for rc12 is whether SEC cleanly defines the security architecture interface without re-owning ARCH structure, INT contract/session semantics, TIME measurable properties, RUN current state, ROB general resilience response, LIFE transaction results, OBS evidence authority, CFG source authority, ASSUR evidence-sufficiency semantics or external Security/Risk/Regulatory acceptance authority; and whether SEC Project-Applicable Obligations are Framework-Scan scannable.

After SEC reaches a stable L1/L2 baseline, one final integrated L1/L2 consolidation review is expected before L3 Pattern / Mechanism Catalog authoring begins.

## 18. v0.0.2rc13 Final Integrated L1/L2 Consolidation Coverage

This release adds no new concern tranche and does not reopen taxonomy. It performs the final integrated L1/L2 consolidation after the independent rc12 SCAF-SEC review found no Critical/Major issues, judged SEC Stable after minor cleanup, confirmed SEC integration with the existing CTX -> ARCH -> INT -> TIME -> RUN -> ROB -> LIFE -> OBS -> CFG backbone as Pass, and cleared final consolidation to begin.

The consolidation closes the rc12 SEC cross-reference and authority-precision findings, including the SEC/OBS invariant reference, robustness-significant qualification for resource-abuse handoff to ROB, and authorization-related CFG input wording. It also normalizes the specifically reviewed residual CTX/ROB authority-role grammar without changing concern authority homes.

No donor class is newly promoted by these edits. Schema, validator, CI, L3 pattern/mechanism catalogs and L4 implementation guidance remain excluded. Review focus for rc13 is whether the complete CTX -> ARCH -> INT -> TIME -> RUN -> ROB -> LIFE -> OBS -> CFG -> SEC L1/L2 backbone is integrated-clean, Framework-Scan compatible, source/evidence/closure disciplined, identity-consistent and suitable to become an explicit L1/L2 freeze candidate before L3 authoring.

## 19. v0.0.2rc14 Final Editorial Closure / Freeze-Candidate Coverage

This release adds no concern tranche, changes no requirement ID or Target class, and introduces no intended normative semantic change. It closes only the four editorial findings identified by the independent rc13 final integrated L1/L2 review: Authority Kernel normative-keyword scan hygiene, `SCAF-OBS-020` normative-keyword typography, `docs/00_Input_Baseline.md` section numbering, and `docs/03_Gen1_to_Gen2_Concept_Mapping.md` duplicate section numbering.

The complete CTX -> ARCH -> INT -> TIME -> RUN -> ROB -> LIFE -> OBS -> CFG -> SEC L1/L2 backbone is carried forward unchanged for a narrow freeze-candidate audit. L3/L4, schema, validator, CI and generated conformance tooling remain closed pending an explicit L1/L2 freeze decision.

## 20. v0.0.2rc15 Freeze-Candidate Release-Hygiene Closure Coverage

This release adds no concern tranche, changes no requirement ID or Target class, and introduces no intended normative semantic change. It closes the sole trivial issue identified by the independent rc14 freeze-candidate audit: a stale README sentence that described the next gate as another final integrated L1/L2 review after that integrated review had already completed.

The complete CTX -> ARCH -> INT -> TIME -> RUN -> ROB -> LIFE -> OBS -> CFG -> SEC L1/L2 backbone and all rc14 editorial closures are carried forward unchanged for a narrow rc15 freeze-candidate audit. L3/L4, schema, validator, CI and generated conformance tooling remain closed pending an explicit L1/L2 freeze decision.

