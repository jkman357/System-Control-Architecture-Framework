# SCAF Consumption Selection Validator

This package implements the v0.0.7rc05 source-aware validation boundary for the accepted v0.0.7rc03 Consumption Selection representation and v0.0.7rc04 schema.

Run the repository-owned fixture:

```text
python -m tools.scaf_consumption_selection_validator.validator
```

Optional project-side input selectors:

```text
--selection <path>
--profile <path>
--project-application <path>
```

Repository/schema/authority/normative overrides are intentionally not exposed by the production CLI.

A PASS proves only machine-determinable representation/source/selection consistency. It does not decide applicability correctness, Project Design Authority approval, Pattern selection, implementation, verification, compliance, risk acceptance, release readiness, or closure.
