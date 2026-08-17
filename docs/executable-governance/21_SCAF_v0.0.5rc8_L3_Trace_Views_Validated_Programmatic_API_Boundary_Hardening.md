# SCAF v0.0.5rc8 — L3 Trace Views Validated Programmatic API Boundary Hardening

## 1. Purpose

v0.0.5rc8 is a focused closure release for the single blocking rc7 review finding:

```text
RC7-01 — Public view-builder path can return trace views from an unvalidated caller-constructed TraceContext
Severity: Major
```

The rc7 canonical CLI path correctly required rc6 source-aware validation, but the module also exposed directly callable public symbols that accepted a caller-created context and returned normal trace-view objects without owning the validation proof.

rc8 closes that alternate supported programmatic path without changing trace semantics, serialized data, source-aware validation rules, generated artifacts, project authority, or the frozen production trust chain.

## 2. Upstream Review Basis

The independent rc7 review reported:

```text
Critical: 0
Major:    1
Minor:    0
Trivial:  0

RC7-01 — Public view-builder path can return trace views from an unvalidated caller-constructed TraceContext

V0.0.5 L3 DETERMINISTIC TRACE VIEWS / QUERY FOUNDATION GATE: NO
```

All other reviewed rc7 behaviors passed, including:

- direct rc6→rc7 repository delta;
- normal CLI validated-source gating;
- exact two-direction 119-relation projections;
- typed relation and qualifier fidelity;
- zero-relation semantics;
- deterministic JSON;
- read-only behavior;
- rc6 24/24 regressions;
- rc7 17/17 regressions;
- frozen 41/41 regressions; and
- unchanged production six-artifact external-trust gate.

Therefore rc8 is intentionally bounded to the supported programmatic API trust boundary.

## 3. Supported Public API Contract

The supported Python query API is now exactly:

```python
from tools.scaf_trace_views import query_l2, query_pattern

view = query_l2(repo_root, l2_id)
view = query_pattern(repo_root, pattern_id)
```

Each supported query API **shall own** repository validation:

```text
query_l2(repo_root, l2_id)
        ↓
_load_validated_context(repo_root)
        ↓
rc6 validate_repository(repo_root)
        ↓ PASS only
internal projection
        ↓
view return
```

and:

```text
query_pattern(repo_root, pattern_id)
        ↓
_load_validated_context(repo_root)
        ↓
rc6 validate_repository(repo_root)
        ↓ PASS only
internal projection
        ↓
view return
```

A supported caller cannot supply prebuilt relation state or a caller-created trace context in place of the repository root validation proof.

## 4. Removed Public Trust Objects

The rc7 public symbols:

```text
TraceContext
build_l2_view()
build_pattern_view()
```

are removed from the supported/module public API surface.

Their responsibilities are replaced by internal implementation details:

```text
_ValidatedTraceContext
_build_l2_view()
_build_pattern_view()
```

Python underscore privacy is not treated as a cryptographic or hostile-code security boundary. It defines the supported engineering API surface. To make accidental caller construction fail closed as well, `_ValidatedTraceContext` additionally requires a module-internal validation seal and rejects ordinary caller construction without that seal.

The package and query module explicitly define `__all__` so supported public symbols are bounded and reviewable.

## 5. CLI / Programmatic Path Unification

The CLI no longer performs an independently assembled context/build sequence. `main()` calls the same supported public API used by Python consumers:

```text
CLI --l2
   ↓
query_l2()
   ↓
rc6 validation
   ↓
view

CLI --pattern
   ↓
query_pattern()
   ↓
rc6 validation
   ↓
view
```

This removes the possibility of one validation policy for CLI use and a weaker supported policy for programmatic use.

## 6. Failure Contract

For every supported public query path:

```text
rc6 validation FAIL
        ↓
no returned trace view
```

For CLI use:

```text
rc6 validation FAIL
        ↓
stdout view payload: none
stderr: ERROR + RESULT: FAIL
exit code: non-zero
```

Internal projection helpers do not constitute supported public query APIs and shall not be documented or exported as caller-supplied trust surfaces.

## 7. Preserved Trace Semantics

rc8 does not change the accepted rc7 view semantics.

Every returned relation still preserves:

```text
pattern_id
relation_type
l2_id
pattern_source_path
pattern_source_field
source_release
qualifier
```

The accepted relation classes remain:

```text
primary_realization_candidate
supporting_realization
constraint_input
```

The accepted query-domain and ordering rules remain unchanged.

Known Project-Applicable Obligations with no accepted L3 trace still return:

```text
relation_count: 0
relations: []
```

Framework Normative Invariants and unknown identities remain outside/fail-closed for the current L2 query surface.

## 8. Regression Expansion

The rc7 trace-view/query development suite contained 17 tests.

rc8 expands the suite to **23 tests** and specifically adds/strengthens regression coverage for:

- supported public L2 query owns `validate_repository()`;
- supported public Pattern query owns `validate_repository()`;
- invalid serialized repository state fails through the public L2 API;
- invalid frozen-source state fails through the public Pattern API;
- `_ValidatedTraceContext` rejects caller construction without the internal validation seal;
- legacy public `TraceContext`, `build_l2_view`, and `build_pattern_view` symbols are absent;
- package `__all__` exports only validation-owning supported query APIs plus the public error type;
- CLI routes through the same public `query_l2()` entry point.

Existing projection, fidelity, deterministic-output, zero-result, domain-boundary and read-only regressions remain preserved.

## 9. Preserved Upstream State

rc8 does not modify:

- frozen v0.0.2 normative authority;
- frozen v0.0.3 L3 Pattern sources;
- frozen v0.0.4 executable-governance controls/trust bundle;
- `authority-registry.yaml`;
- `l3-trace-registry.yaml`;
- `schemas/l3-trace-registry.schema.json`;
- `tools/scaf_trace_validator/`;
- `.github/workflows/scaf-executable-governance.yml`.

The rc6 source-aware validator remains the validation authority for trace consumption. rc8 only changes how the trace-view module exposes and routes supported consumers to that proof.

## 10. Semantic / Authority Boundary

The accepted non-equivalence remains unchanged:

```text
Queried / Traced / Serialized / Schema-valid / Source-validated / Resolved
!= Applicable
!= Recommended
!= Selected
!= Satisfied
!= Compliant
!= Verified
!= Closed
```

No programmatic API result gains project-decision authority merely because the validation boundary is hardened.

## 11. Explicit Non-Goals

rc8 does not implement:

- persisted/generated forward or reverse indexes;
- trace-registry generation or rewriting;
- authority/context resolver selection logic;
- semantic relevance/ranking;
- project applicability inference;
- Pattern recommendation or automatic selection;
- satisfaction/compliance/verification/evidence/closure inference;
- new L3 Patterns, M3/M4, or L4 guidance;
- code generation;
- trace-view CI/merge enforcement;
- expansion of the frozen v0.0.4 six-artifact trust chain.

## 12. rc8 Gate Intent

The rc8 review should independently reproduce the rc7 programmatic bypass attempt and establish that the supported public API surface no longer allows a caller-created trace context or direct public builder to return a view without successful rc6 validation.

A clean gate requires at least:

```text
RC7-01: RESOLVED
Critical: 0
Major:    0
Minor:    0
Trivial:  0

V0.0.5 L3 TRACE VIEWS VALIDATED PROGRAMMATIC API BOUNDARY HARDENING GATE: YES
```
