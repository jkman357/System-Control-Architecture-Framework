# SCAF L3 Deterministic Trace Views

`tools/scaf_trace_views` is the v0.0.5rc7 read-only consumption foundation for the accepted L3 machine-readable trace.

It does **not** create another authority/index file. Every query first requires the repository to pass the accepted source-aware trace validator, then derives a view in memory from `l3-trace-registry.yaml` and writes the requested view to stdout only.

## Run

From repository root:

```text
python -m tools.scaf_trace_views.query --l2 SCAF-ROB-004
python -m tools.scaf_trace_views.query --pattern SCAF-PAT-COM-001
```

Deterministic JSON is available for AI/tool consumption:

```text
python -m tools.scaf_trace_views.query --l2 SCAF-ROB-004 --format json
python -m tools.scaf_trace_views.query --pattern SCAF-PAT-COM-001 --format json
```

## View semantics

The tool preserves the accepted typed trace relations and all seven serialized relation fields. It does not flatten relation classes and does not discard material qualifier context.

L2 -> L3 view order:

```text
relation type order
    primary_realization_candidate
    supporting_realization
    constraint_input
then pattern_id ascending
```

L3 -> L2 view order:

```text
relation type order
    primary_realization_candidate
    supporting_realization
    constraint_input
then l2_id ascending
```

A known frozen `Project-Applicable Obligation` with no current L3 trace is a valid zero-relation result. An unknown/non-project-applicable authority ID or unknown frozen Pattern ID fails closed.

## Boundary

A query result means only that the accepted catalog trace contains the displayed typed relation(s).

```text
Queried / Traced / Serialized / Source-validated
!= Applicable
!= Recommended
!= Selected
!= Satisfied
!= Compliant
!= Verified
!= Closed
```

The tool performs no project applicability inference, recommendation, Pattern auto-selection, resolver/context ranking, registry generation/rewrite, or CI/trust-chain enforcement.
