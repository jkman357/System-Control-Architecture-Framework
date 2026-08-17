# SCAF L3 Source-Aware Trace Validator

This development control implements the reviewed v0.0.5rc4 L3 trace schema and frozen-source extraction contract. v0.0.5rc6 hardens the first rc5 implementation after independent review identified two fail-open source-boundary defects.

Frozen v0.0.3 Pattern Markdown metadata remains semantic trace authority. `l3-trace-registry.yaml` is a subordinate representation. The validator proves representation/source conformance only; it does not decide project applicability, Pattern selection, satisfaction, compliance, verification, evidence sufficiency, or closure.

## Install dependencies

```text
python -m pip install -r tools/scaf_trace_validator/requirements.txt
```

## Run

From repository root:

```text
python -m tools.scaf_trace_validator.validator
```

A successful run proves, for the current reviewed population:

- Draft 2020-12 trace-schema conformance;
- deterministic reconstruction only from the required rows in the single authoritative `## Metadata` table;
- exact 119-record source/serialization equality;
- exact 23 / 41 / 55 relation split;
- 119 unique `(pattern_id, relation_type, l2_id)` tuples;
- 15 source-faithful qualifier associations;
- canonical cross-record ordering;
- resolution of all 82 referenced L2 IDs in `authority-registry.yaml`;
- strict comma-delimited Constraint Inputs item transitions, including rejection of leading/missing comma separators;
- fail-closed rejection of unsupported frozen-source syntax and same-key narrative-table authority substitution.

The tool is a v0.0.5 development control and is not retroactively part of the frozen v0.0.4 six-artifact CI trust bundle.


## rc6 source-boundary hardening

The validator treats source location and delimiters as reviewed syntax, not as advisory formatting:

- exactly one `## Metadata` section is required per frozen Pattern source;
- exactly one `| Field | Value |` metadata table must appear inside that section;
- `Pattern ID`, `Primary L2 Trace`, `Supporting L2 Trace`, and `Constraint Inputs` are machine-authoritative only when present exactly once in that table;
- same-key rows under later narrative headings/tables do not create or replace machine authority;
- a Constraint Inputs clause may not begin with a comma;
- every later ID/item transition requires an explicit comma;
- reviewed `applicable` / `conditional` markers do not waive the comma requirement.

These rules close rc5 review findings `R5-01` and `R5-02` without adding a new qualifier grammar or source-authority surface.
