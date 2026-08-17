# SCAF Authority-Registry Validator

**Development Release:** v0.0.4rc05  
**Scope:** structural + canonical-source fidelity validation for the accepted rc03 authority registry

This validator is a subordinate executable-governance check. It does **not** become semantic authority and does not replace the frozen Markdown under `docs/normative/`.

## Install dependencies

From the repository root:

```text
python -m pip install -r tools/scaf_validator/requirements.txt
```

Dependencies are intentionally limited to:

- PyYAML — parse the accepted YAML representation;
- jsonschema — validate the local Draft 2020-12 structural schema.

## Run validation

```text
python -m tools.scaf_validator.validator
```

Expected successful summary:

```text
Records:    294
Unique IDs: 294
Source IDs: 294
Project-Applicable Obligations: 218
Framework Normative Invariants: 76
Errors:      0
RESULT: PASS
```

## Run regression tests

```text
python -m unittest discover -s tools/scaf_validator/tests -v
```

The tests exercise the accepted registry plus controlled mutations for duplicate identity, anchor mismatch, source-path mismatch, Target/class mismatch, non-empty relations and unsupported Pattern identity.

## Validation boundary

The JSON Schema enforces the accepted rc03 ten-field representation shape and deterministic constants. Source-aware validation additionally checks facts that JSON Schema alone cannot prove:

- authority-ID uniqueness by `id`;
- bidirectional 294-record source coverage;
- repository-relative canonical `source_path` existence;
- `source_anchor == id`;
- exactly one canonical requirement heading/block in the declared source file;
- exact frozen source `Target` ↔ `authority_class` fidelity.

Raw textual occurrences of an ID are not authority anchors. The validator recognizes only the frozen canonical requirement heading form.

The validator intentionally does not infer project applicability, compliance, realization, verification, closure, L3 Pattern selection, L2→L3 relations or any other project/architecture state.
