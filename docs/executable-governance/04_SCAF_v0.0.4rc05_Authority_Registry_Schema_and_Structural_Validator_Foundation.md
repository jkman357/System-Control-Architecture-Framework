# SCAF v0.0.4rc05 — Authority Registry Schema and Structural Validator Foundation

**Development Release:** v0.0.4rc05  
**Status:** Schema + structural/source-aware validator foundation RC  
**Upstream Baselines:** frozen v0.0.2 L1/L2; frozen v0.0.3 L3  
**Accepted Registry Basis:** v0.0.4rc03 294-record controlled curated representation  
**Upstream Gate:** `V0.0.4 AUTHORITY-REGISTRY RELEASE-STATE CLEANUP GATE: YES`

## 1. Purpose

This RC makes the accepted rc03 authority-registry contract executable at the first validation layer.

It adds:

- a local JSON Schema for the accepted ten-field 294-record representation;
- an executable structural and canonical-source fidelity validator;
- focused regression tests against accepted and intentionally mutated registry states.

The validator and schema are subordinate checks. They do **not** become semantic authority. Frozen normative Markdown under `docs/normative/` remains the semantic authority, and the unchanged `authority-registry.yaml` remains the accepted rc03 controlled curated representation.

## 2. Artifacts

The rc05 validation foundation consists of:

```text
schemas/authority-registry.schema.json
tools/scaf_validator/validator.py
tools/scaf_validator/requirements.txt
tools/scaf_validator/README.md
tools/scaf_validator/tests/test_validator.py
```

The registry itself is intentionally unchanged from rc03/rc04:

```text
authority-registry.yaml
representation_release = v0.0.4rc03 for all 294 records
```

## 3. Schema Boundary

`schemas/authority-registry.schema.json` uses JSON Schema Draft 2020-12 to express only the accepted rc03 structural contract.

It enforces:

- exactly one top-level `records` member and no additional top-level properties;
- exactly 294 records;
- exactly the accepted ten fields per record and no additional record fields;
- record ID format limited to the frozen L1/L2 authority-prefix population;
- `record_kind = normative_requirement`;
- `layer = l1_l2_normative_authority`;
- exactly the two accepted authority classes;
- source paths limited to the eleven frozen normative Markdown files;
- `source_release = v0.0.2`;
- `representation_release = v0.0.4rc03` for the accepted serialization under validation;
- `status = represented`;
- empty `relations`.

The schema does not infer project state, Pattern state, compliance, verification, closure, relation semantics, or source authority.

JSON Schema alone cannot prove every cross-record/source property. In particular, authority-ID uniqueness by `id`, source-heading resolution, source-path fidelity, and source `Target` fidelity are enforced by the source-aware validator.

## 4. Validator Boundary

The executable validator is invoked from repository root with:

```text
python -m tools.scaf_validator.validator
```

Its validation order is:

```text
YAML parse with duplicate mapping-key rejection
        ↓
local JSON Schema validation
        ↓
canonical frozen-source inventory parse
        ↓
registry ID uniqueness and bidirectional source coverage
        ↓
source_path existence / canonical-file fidelity
        ↓
source_anchor == id
        ↓
exactly-one canonical requirement-heading resolution
        ↓
source Target == authority_class
        ↓
PASS / FAIL
```

The canonical requirement heading form is the frozen form:

```text
### `SCAF-<CONCERN>-NNN` — <title>
```

Raw textual cross-references are not authority anchors. A requirement ID must resolve exactly once as a canonical heading/block inside its declared `source_path`.

The validator fails closed on structural/source consistency defects. It does not repair, reinterpret, auto-complete, or prefer registry data over canonical Markdown.

## 5. Dependency Boundary

The validator requires:

```text
PyYAML >= 6.0, < 7
jsonschema >= 4.18, < 5
```

Installation command:

```text
python -m pip install -r tools/scaf_validator/requirements.txt
```

These dependencies provide representation parsing and local schema validation only. They do not define SCAF semantics.

## 6. Regression Test Contract

Run:

```text
python -m unittest discover -s tools/scaf_validator/tests -v
```

The rc05 regression suite includes:

1. accepted registry passes;
2. duplicate authority identity fails;
3. `source_anchor != id` fails;
4. canonical source-path mismatch fails;
5. source `Target` / `authority_class` mismatch fails;
6. non-empty `relations` fails schema validation;
7. `SCAF-PAT-*` identity inserted into the normative authority registry fails.

These are representation-contract regressions only. They are not project conformance tests and do not validate product architecture.

## 7. rc05 Self-Validation Result

Before packaging, the rc05 validator was executed against the unchanged accepted registry and frozen source tree.

Observed result:

```text
Records:    294
Unique IDs: 294
Source IDs: 294
Project-Applicable Obligations: 218
Framework Normative Invariants: 76
Errors:      0
RESULT: PASS
```

The seven regression tests also passed.

This is build/review evidence for rc05, not a replacement for independent review.

## 8. Non-Regression Requirements

rc05 shall preserve byte-for-byte from rc04:

- `authority-registry.yaml`;
- `docs/executable-governance/00_SCAF_Machine_Readable_Authority_Model.md`;
- `docs/executable-governance/01_SCAF_v0.0.4rc02_Authority_Model_Determinism_Cleanup.md`;
- `docs/executable-governance/02_SCAF_v0.0.4rc03_Initial_Authority_Registry_Serialization.md`;
- `docs/executable-governance/03_SCAF_v0.0.4rc04_Authority_Registry_Release_State_Documentation_Cleanup.md`;
- frozen `docs/normative/`;
- frozen `docs/l3/`.

The schema and validator may encode the accepted representation contract, but they shall not change it.

## 9. Deliberately Not Included

rc05 does not add or authorize:

- CI enforcement or merge blocking;
- registry generation or hybrid ownership;
- generated reverse indexes/views;
- code generation;
- automatic project applicability inference;
- project compliance/verification/closure evaluation;
- non-empty machine-readable relation semantics;
- machine-readable L2→L3 relations;
- new L3 Pattern / third tranche;
- SEC-primary realization;
- M3/M4;
- L4.

## 10. Independent Review Gate

Independent review shall determine whether the rc05 schema and validator faithfully execute the accepted rc03 registry contract without becoming a competing authority source or expanding semantics.

The review shall verify at minimum:

1. rc04→rc05 non-regression for the accepted registry, authority-model/serialization records, frozen normative tree, and frozen L3 tree;
2. schema validity and exact accepted ten-field structural constraints;
3. validator pass on the accepted 294-record registry;
4. exact 294 / 218 / 76 source-aware reconstruction;
5. duplicate-ID, source-path, source-anchor and Target/class mismatch failure behavior;
6. empty-relations and L3 Pattern exclusion enforcement;
7. regression tests execute and pass;
8. canonical Markdown precedence and fail-closed behavior remain explicit;
9. no CI/codegen/generated-view/project-inference/L3/M3/M4/L4 scope is introduced.

Expected decision:

```text
V0.0.4 AUTHORITY-REGISTRY SCHEMA-VALIDATOR FOUNDATION GATE: YES / YES, AFTER MINOR CLEANUP / NO
```

A `YES` accepts only this validation foundation and authorizes planning a later separately reviewed executable-governance step. It does not automatically authorize CI enforcement, generation, project applicability inference, cross-layer relation semantics, Pattern expansion, M3/M4, or L4.
