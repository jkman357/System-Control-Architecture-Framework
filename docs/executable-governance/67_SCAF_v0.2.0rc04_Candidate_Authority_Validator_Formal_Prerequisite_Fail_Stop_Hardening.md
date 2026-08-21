# SCAF v0.2.0rc04 — Candidate Authority Validator Formal-Prerequisite Fail-Stop Hardening

**Development Release:** v0.2.0rc04  
**Development Predecessor:** v0.2.0rc03 / Git `ea070585b7721ed3bf0411e2cd60d19d49e65500`  
**Formal Authority Release:** v0.1.0 using the frozen `294 / 218 / 76` authority representation  
**Candidate Representation:** v0.2.0rc03 `299 / 223 / 76` candidate authority registry  
**Status:** Finding-closure candidate; no downstream migration authorized

## 1. Why this RC exists

The independent v0.2.0rc03 review returned:

```text
PASS
Critical: 0
Major:    0
Minor:    1
Trivial:  0
V0.2.0RC03 CANDIDATE MACHINE-READABLE AUTHORITY REPRESENTATION FOUNDATION GATE: YES
```

The reviewed report has SHA-256:

```text
cdce0e7a44744377c300239bc57ddc025ee6a32240f1b42aa18e9aceb3535295
```

The single finding is `RC03-01 — Candidate validator does not stop processing after frozen-authority prerequisite failure`.

The rc03 implementation always returned an overall failure when frozen formal authority validation failed, so no false acceptance was demonstrated. However, it continued candidate projection, candidate-source and inventory reasoning after the formal prerequisite was already invalid. That behavior contradicted the declared validated-input ownership and validation order.

rc04 exists only to close that finding before any new dependency/value assessment.

## 2. Scope

rc04 changes only the candidate-validator fail-stop behavior, its regression coverage, and navigation/release records.

The functional change is:

```text
validate formal authority using frozen validator
        ↓
formal authority valid?
   NO ───────────────→ report frozen errors and return immediately
   YES
        ↓
continue candidate schema / binding / projection / source / inventory validation
```

No candidate authority semantics, registry records, schema constraints, formal authority, Project Application, L3 or L4 semantics are changed.

## 3. Formal prerequisite ownership

The frozen validator remains the sole validator for formal authority:

```text
authority-registry.yaml
schemas/authority-registry.schema.json
tools/scaf_validator/
```

The candidate validator must not reason from formal registry contents after the frozen validator has rejected those inputs.

Therefore `validate_candidate_data()` now:

1. invokes `frozen_validator.validate_registry(...)` first;
2. if `frozen_report.passed` is false, records the frozen errors;
3. returns immediately;
4. leaves candidate-derived counters and projection/source results at their uncomputed defaults;
5. proceeds to candidate structural/source-aware reasoning only after the formal prerequisite passes.

This is a control-flow hardening change. It does not alter the accepted rc03 candidate representation model.

## 4. Regression requirement

A new bounded regression test deliberately supplies a synthetic failed frozen-validation result.

The test requires:

```text
report.passed == False
report.frozen_input_valid == False
record_count == 0
unique_id_count == 0
frozen_projection_count == 0
candidate_record_count == 0
candidate_source_count == 0
project_applicable_count == 0
framework_invariant_count == 0
```

This demonstrates that candidate-specific processing does not occur after the formal prerequisite fails.

## 5. Preserved candidate representation

The following rc03 artifacts remain semantically unchanged:

```text
candidate-authority-registry.yaml
schemas/candidate-authority-registry.schema.json
```

The expected successful candidate result remains:

```text
299 total authority records
223 Project-Applicable Obligations
76 Framework Normative Invariants
294 exact frozen projections
5 candidate records: SCAF-OBS-041..045
```

Formal authority remains:

```text
294 / 218 / 76
```

## 6. Downstream boundary remains unchanged

rc04 does not authorize candidate consumption by:

- Project Application;
- Effective Project Profile;
- Consumption Selection;
- Context Source Association;
- Controlled Context Package;
- L3 trace/catalog;
- L4 construction guidance;
- generic code generation;
- generic runtime-instrumentation CI.

The existing distinction remains:

```text
candidate authority is source-aware validated
!=
candidate authority is formal authority
!=
candidate authority is already a downstream consumer input
```

## 7. Source-package hygiene

The committed rc03 parent on GitHub retains seven previously tracked Python bytecode/cache files. The reviewed rc03 source package had already treated their removal as non-semantic packaging hygiene.

rc04 re-applies those deletions against the actual committed rc03 parent while preserving the existing `.gitignore` rules. Review/test execution for this package should use `PYTHONDONTWRITEBYTECODE=1` so generated cache bytes do not reappear before the cleanup is committed.

This hygiene closure changes no Python source semantics.

## 8. Required validation

A valid rc04 candidate must demonstrate at least:

```text
formal authority validator:        294 / 218 / 76 PASS
candidate authority validator:     299 / 223 / 76 PASS
candidate frozen projection:       294 MATCH
candidate records:                 5
candidate validator regression:    all PASS, including fail-stop case
L3 trace validator:                12 patterns / 119 relations PASS
frozen release integrity:          docs/normative MATCH; docs/l3 MATCH
Project Application validator:     PASS against formal authority only
git diff --check HEAD:             PASS
```

## 9. Acceptance boundary

A clean rc04 review closes only `RC03-01` and establishes that the rc03 candidate representation has a trustworthy formal-prerequisite fail-stop boundary.

A clean rc04 review may authorize a **new dependency/value assessment** for whether any downstream candidate consumer migration is justified.

It does not itself authorize that migration.
