# SCAF Candidate Authority Validator

This tool validates the **v0.2.0rc03 development candidate** machine-readable L1/L2 authority representation. v0.2.0rc04 hardens its formal-prerequisite control flow without changing that representation.

It is intentionally separate from `tools/scaf_validator/`, which remains the validator for the frozen formal authority registry.

The candidate validator checks that:

- the frozen `authority-registry.yaml` first passes its existing source-aware validator; if it fails, validation stops before candidate-specific reasoning;
- the candidate registry contains exactly `299 / 223 / 76` records;
- all 294 frozen records are reproduced exactly, field-for-field;
- the only candidate-only IDs are `SCAF-OBS-041..045`;
- those five IDs resolve against the accepted rc01 OBS candidate overlay;
- candidate authority class and source anchors match the candidate Markdown;
- the frozen-registry and candidate-source SHA-256 bindings match the repository bytes;
- candidate/frozen release state is explicit.

The validator does **not**:

- promote candidate authority into formal v0.1.0 authority;
- modify or replace the frozen validator;
- make `candidate-authority-registry.yaml` a SCAF-APP input;
- validate Project Application, Effective Project Profile, Consumption Selection, L3 or L4 against candidate authority;
- decide engineering applicability, adequacy, verification sufficiency or project closure.

Run from repository root:

```text
python -m tools.scaf_candidate_authority_validator.validator
```

A successful result is representation/source-fidelity evidence for this candidate only. It is not a formal freeze/promotion decision.
