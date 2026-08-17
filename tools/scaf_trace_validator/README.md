# SCAF L3 Source-Aware Trace Validator

This development control implements the reviewed v0.0.5rc4 L3 trace schema and frozen-source extraction contract.

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
- deterministic reconstruction from the three frozen authoritative Pattern metadata rows;
- exact 119-record source/serialization equality;
- exact 23 / 41 / 55 relation split;
- 119 unique `(pattern_id, relation_type, l2_id)` tuples;
- 15 source-faithful qualifier associations;
- canonical cross-record ordering;
- resolution of all 82 referenced L2 IDs in `authority-registry.yaml`;
- fail-closed rejection of unsupported frozen-source syntax.

The tool is a v0.0.5 development control and is not retroactively part of the frozen v0.0.4 six-artifact CI trust bundle.
