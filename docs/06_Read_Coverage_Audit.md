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

**None.** All 72 Gen1 files were opened/read at machine-text level during the rc1/rc03 archaeology work.

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

The primary README contains both generic architecture and candidate implementation contracts. rc03 maps generic architecture concepts but does not adopt every API, record layout, ABI, memory budget, persistence layout or RC implementation recommendation as SCAF policy.

## 4. Independent Review Coverage

The v0.0.1rc1 and v0.0.1rc02 independent architecture reviews were read and used as correction input.

Review findings incorporated through rc03 include:

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
- source identity vs retrievability distinction.

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

rc03 retains three non-normative architecture exercises:

1. single MCU system;
2. PC + multiple MCU system;
3. SoC + FPGA + DSP heterogeneous system.

At taxonomy level, all three remain representable without new ad-hoc top-level categories.

rc03 additionally runs a worked Framework Scan against the PC + multiple MCU archetype across eleven concerns. It exercises:

```text
Concern
 -> Applicability / Consequence
 -> Required Decision
 -> Project Design Authority output
 -> Verification / Evidence
 -> Re-evaluation Trigger
```

The exercise also exposes the greenfield bootstrap loop: provisional CTX/ARCH is refined by scan decisions and must then be re-scanned. This demonstrates an operating model beyond simple representability, but remains architecture evidence rather than project verification.

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
8. Framework Scan closure and re-evaluation semantics;
9. implementation-profile precedence/composition after profile axes stabilize.

## 9. Audit Conclusion

There are **no unread input files** among the two donor source archives used for the archaeology work.

However, there are intentionally deferred **deep normative audits**. v0.0.1rc03 should therefore be treated as:

> **an architecture/taxonomy convergence baseline with an explicit project-authority chain and worked application evidence, not a completed migration proof.**
