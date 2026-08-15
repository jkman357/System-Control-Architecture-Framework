# Read Coverage Audit

## 1. Coverage Definitions

This RC distinguishes three levels:

- **Discovered** — file exists in the input archive and is listed.
- **Machine-read** — file bytes/text were opened and inspected programmatically.
- **Semantic role review** — the artifact's engineering/repository role and Gen2 disposition were assessed.
- **Deep normative audit** — detailed requirement-by-requirement reconciliation, contradiction review and wording migration.

The last level is intentionally **not** complete in v0.0.1rc1 because the project explicitly requires taxonomy and mapping to converge before formal large-scale rewriting.

## 2. Gen1 Coverage

| Measure | Result |
|---|---:|
| Files discovered | 72 / 72 |
| Files machine-read | 72 / 72 |
| Files included in role/disposition inventory | 72 / 72 |
| Governed authority documents identified from `authority-registry.yaml` | 23 / 23 |
| Deep normative migration audit | Not yet performed |

### Files not read

**None.** All 72 Gen1 files were opened/read at machine-text level for v0.0.1rc1.

### Files not yet deeply audited requirement-by-requirement

The following classes are intentionally deferred from line-by-line normative migration review:

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
- path/digest edge cases in legal-baseline and repository-protection tooling.

These artifacts were read and their roles were analyzed, but their individual test assertions are not yet being promoted into Gen2 requirements.

## 3. Supplemental Crash Recorder Coverage

| Measure | Result |
|---|---:|
| Files discovered | 2 / 2 |
| Files machine-read | 2 / 2 |
| Primary specification structure reviewed | Yes |
| Major resilience/evidence concepts mapped | Yes |
| Recorder API/ABI/reference implementation promoted into Gen2 core | No |

### Files not read

**None.** Both files were read at machine-text level.

### Deferred deep audit

The primary README contains both generic architecture and detailed candidate implementation contracts. v0.0.1rc1 maps the generic architecture, but does not yet adjudicate every public API, record layout, ABI, memory budget or RC implementation recommendation as a Gen2 rule.

## 4. Why “Machine-read” Is Not “Fully Absorbed”

A repository can be fully opened without its entire normative meaning being reconciled. This RC therefore avoids the false claim that all 72 Gen1 files have already been semantically rewritten or conflict-resolved.

The next analysis increments should focus on **concept conflict and authority convergence**, especially:

1. master Framework vs specialized authority overlap;
2. application analysis vs conformance/evidence overlap;
3. protocol guide/template/schema semantic ownership;
4. Coordinator vs generic Node/system ownership;
5. runtime diagnostics vs incident evidence;
6. resilience lifecycle coverage;
7. verification obligations produced by Framework Scan.

## 5. Audit Conclusion

There are **no unread input files** in v0.0.1rc1. There are intentionally deferred **deep audits**, and those are listed above rather than hidden behind a blanket “fully analyzed” claim.
