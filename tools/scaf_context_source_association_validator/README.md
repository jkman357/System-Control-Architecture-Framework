# SCAF Context Source Association Validator

This package implements the v0.0.9rc05 source-aware validation boundary for the accepted v0.0.9rc03 Context Source Association representation and v0.0.9rc04 structural schema.

Run the repository-owned fixture:

```text
python -m tools.scaf_context_source_association_validator.validator
```

Optional project-side input selectors:

```text
--associations <path>
--selection <path>
--profile <path>
--project-application <path>
```

Repository-owned schema and validator sources are intentionally not overrideable through the production CLI.

A PASS proves only machine-determinable representation/source-association consistency under the validator's bounded input model. It does not discover sources, decide source currentness, infer authority, decide applicability, prove obligation satisfaction, decide verification sufficiency/compliance/risk/release/closure, or assemble AI context.
