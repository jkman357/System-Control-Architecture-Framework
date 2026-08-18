# SCAF L3 Deterministic Trace Views

`tools/scaf_trace_views` is the v0.0.5rc9 authority-validation and CLI-execution boundary closure for deterministic read-only consumption of the accepted L3 machine-readable trace.

It creates no authority/index file. Every supported Python or CLI query requires **both** the accepted rc6 source-aware trace validator and the frozen source-aware authority-registry validator to pass against the same resolved repository root before any trace view is projected.

## Supported Python API

```python
from tools.scaf_trace_views import query_l2, query_pattern

view = query_l2(repo_root, "SCAF-ROB-004")
view = query_pattern(repo_root, "SCAF-PAT-COM-001")
```

The public query functions own the validation sequence. A caller cannot supply prebuilt relation state, an authority classification set, or a caller-created context as a substitute for repository validation.

The package uses lazy re-exports so importing `tools.scaf_trace_views` does not preload the `tools.scaf_trace_views.query` CLI target.

## Validated-input boundary

```text
query_l2() / query_pattern()
        ↓
rc6 source-aware trace validation
        ↓ PASS only
frozen source-aware authority-registry validation
        ↓ PASS only
load validated repository state
        ↓
internal projection
        ↓
view
```

The authority validator is the existing frozen `tools.scaf_validator.validator.validate_registry()` implementation. rc9 reuses it unchanged against:

```text
<repo_root>/authority-registry.yaml
<repo_root>/schemas/authority-registry.schema.json
<repo_root>/docs/normative/
```

This ensures the Project-Applicable L2 query domain is not derived from unproved `authority_class` state.

## Run

From repository root:

```text
python -m tools.scaf_trace_views.query --l2 SCAF-ROB-004
python -m tools.scaf_trace_views.query --pattern SCAF-PAT-COM-001
```

Deterministic JSON:

```text
python -m tools.scaf_trace_views.query --l2 SCAF-ROB-004 --format json
python -m tools.scaf_trace_views.query --pattern SCAF-PAT-COM-001 --format json
```

Successful documented `python -m` execution produces the requested payload on stdout and no runtime-warning stderr. Validation failure produces no view payload, emits `ERROR:` and `RESULT: FAIL` to stderr, and exits non-zero.

## View semantics

All seven accepted serialized relation fields are preserved:

```text
pattern_id
relation_type
l2_id
pattern_source_path
pattern_source_field
source_release
qualifier
```

Relation classes remain:

```text
primary_realization_candidate
supporting_realization
constraint_input
```

L2 -> L3 ordering is relation type then `pattern_id`. L3 -> L2 ordering is relation type then `l2_id`.

A known, source-validated `Project-Applicable Obligation` with no accepted L3 trace is a valid zero-relation result. A Framework Normative Invariant, unknown authority, unknown Pattern, invalid trace state, or invalid authority-registry state returns no supported view.

## Boundary

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

The tool performs no project applicability inference, recommendation, Pattern auto-selection, resolver/context ranking, registry generation/rewrite, or CI/trust-chain enforcement.
