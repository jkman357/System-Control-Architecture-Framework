# SCAF v0.0.5rc9 — L3 Trace Views Authority Validation and CLI Execution Boundary Closure

## 1. Purpose

v0.0.5rc9 is a bounded finding-closure release for the independent rc8 review:

```text
RC8-01 — Supported public queries consume authority-registry classification state that is not covered by the rc6 validation proof
Severity: Major

RC8-02 — Eager package re-export of query causes documented python -m execution to preload/re-execute the target module
Severity: Minor
```

The same review confirmed:

```text
RC7-01: RESOLVED
```

rc9 does not reopen the accepted rc8 public-API shape. It completes the validated-input boundary for repository state used by the query contract and removes the documented CLI module-preload defect.

## 2. RC8-01 Closure Principle

A validation-owning API must validate every repository input whose semantics affect its returned contract.

The L2 trace-query domain depends on `authority-registry.yaml` classification state. Therefore source-aware trace validation alone is insufficient even when every trace relation resolves to an authority ID.

rc9 requires two independent existing proofs before projection:

```text
trace representation/source proof
AND
authority representation/source/classification proof
```

No new authority validator is introduced.

## 3. Same-Root Dual Validation Contract

For both supported public entry points:

```text
query_l2(repo_root, l2_id)
query_pattern(repo_root, pattern_id)
```

rc9 resolves the supplied repository root once and requires:

```text
validate_repository(repo_root)
        ↓ PASS only
validate_registry(
    repo_root,
    repo_root / authority-registry.yaml,
    repo_root / schemas/authority-registry.schema.json)
        ↓ PASS only
load registry state
        ↓
internal deterministic projection
        ↓
return view
```

The second validator is the frozen v0.0.4 implementation:

```text
tools.scaf_validator.validator.validate_registry()
```

It remains unchanged. The accepted rc6 trace validator also remains unchanged.

The same-root binding is intentional: a supported query may not validate authority state from one repository and project trace state from another.

## 4. Authority Query-Domain Negative Conditions

Before rc9, a fabricated record or classification drift could remain outside the rc6 trace proof while changing the public L2 query domain.

rc9 adds regression coverage requiring supported queries to return no view when, in a disposable repository copy:

1. `SCAF-AK-009` is changed from `Framework Normative Invariant` to `Project-Applicable Obligation`;
2. a fabricated `SCAF-ROB-999` Project-Applicable record is appended to the authority registry;
3. an invalid authority registry is supplied while querying a valid frozen Pattern.

The authority validator must reject those states before projection. A normal zero-relation view is not an acceptable response to an invalid authority-registry state.

## 5. RC8-02 Closure Principle

The documented command remains:

```text
python -m tools.scaf_trace_views.query ...
```

The package must not eagerly import the `query` submodule merely to expose the supported Python API. rc9 therefore replaces eager package re-export with lazy attribute loading.

The supported package surface remains exactly:

```text
TraceViewError
query_l2
query_pattern
```

while normal parent-package import no longer preloads the `-m` target module.

## 6. Documented CLI Execution Regression

rc9 adds subprocess tests that execute the documented command rather than calling imported `main()` only.

Successful command requirement:

```text
exit code: 0
stdout: deterministic requested payload
stderr: empty
RuntimeWarning: absent
```

Invalid authority-registry requirement:

```text
exit code: non-zero
stdout: empty
stderr: contains ERROR and RESULT: FAIL
RuntimeWarning: absent
```

The regression invokes Python with `-Werror::RuntimeWarning` so the rc8 duplicate-module condition cannot pass unnoticed.

## 7. Preserved Public API and Projection Semantics

rc9 does not add a new public builder, caller-provided context, prevalidated token, authority set, relation set, or caller-selectable schema.

Returned relation records preserve exactly:

```text
pattern_id
relation_type
l2_id
pattern_source_path
pattern_source_field
source_release
qualifier
```

Accepted relation classes, multi-type pairs, qualifier fidelity, deterministic ordering, deterministic JSON, the two 119-relation projection proofs, and zero-relation semantics for a valid source-validated Project-Applicable identity remain unchanged.

## 8. Regression Expansion

The rc8 trace-view/query suite contained 23 tests.

rc9 expands it to **28 tests** by adding exactly five focused regressions:

```text
authority-class drift -> public L2 query rejects
fabricated Project-Applicable authority -> public L2 query rejects
invalid authority registry -> public Pattern query rejects
documented python -m success -> payload / empty stderr / no RuntimeWarning
documented python -m invalid-authority failure -> no stdout / non-zero / ERROR + RESULT: FAIL
```

Existing public validation-ownership tests are strengthened to establish that both public query directions invoke both validators using the same resolved repository root.

## 9. Preserved Upstream / Frozen State

rc9 does not modify:

```text
docs/normative/
docs/l3/
authority-registry.yaml
schemas/authority-registry.schema.json
l3-trace-registry.yaml
schemas/l3-trace-registry.schema.json
tools/scaf_validator/
tools/scaf_trace_validator/
release-integrity/frozen-baseline-manifest.json
tools/scaf_release_integrity/
tools/scaf_external_pin/
tools/scaf_ci_gate/
.github/workflows/scaf-executable-governance.yml
```

The frozen v0.0.4 six-artifact production external-trust set is unchanged.

## 10. Semantic / Authority Boundary

```text
Queried / Traced / Serialized / Trace-source-validated / Authority-source-validated
!= Applicable
!= Recommended
!= Selected
!= Satisfied
!= Compliant
!= Verified
!= Closed
```

Authority validation proves representation/source/classification conformance. It does not turn a trace-view query into a project applicability engine or architecture-selection authority.

## 11. Explicit Non-Goals

rc9 does not implement:

- registry generation or rewriting;
- persisted/generated forward or reverse indexes;
- project applicability inference;
- Pattern recommendation or automatic selection;
- resolver/context ranking;
- satisfaction/compliance/verification/evidence/closure inference;
- new L3 Patterns, M3/M4 or L4 guidance;
- code generation;
- new CI/merge enforcement;
- expansion or replacement of frozen validators;
- expansion of the frozen production trust chain.

## 12. rc9 Gate Intent

A clean independent review should reproduce the rc8 authority-classification/query-domain defect using disposable repository copies and establish that both supported public query directions now fail before view return unless both same-root validation proofs pass.

It should also execute the documented `python -m` command itself and establish that successful execution has no duplicate-module runtime warning and invalid authority state returns no view payload.

Expected clean-gate shape:

```text
RC8-01: RESOLVED
RC8-02: RESOLVED
Critical: 0
Major:    0
Minor:    0
Trivial:  0

V0.0.5 L3 TRACE VIEWS AUTHORITY VALIDATION AND CLI EXECUTION BOUNDARY CLOSURE GATE: YES
```
