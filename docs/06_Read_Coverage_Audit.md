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

## 10. v0.0.2rc03 Normative Rewrite Coverage

This release closes the remaining target-class and authority-source precision defects in the controlled Authority Kernel, `SCAF-CTX` and `SCAF-ARCH` tranche after rc02 review. Donor-specific deep audit remains a separate promotion gate; no Draft/RC or executable-only donor invariant is silently promoted by these documents.
