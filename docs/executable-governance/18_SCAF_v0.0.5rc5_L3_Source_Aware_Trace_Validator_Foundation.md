# SCAF v0.0.5rc5 — L3 Source-Aware Trace Validator Foundation

**Development Release:** v0.0.5rc5  
**Status:** Source-Aware Trace Validator Foundation / Review Candidate  
**Upstream Accepted State:** v0.0.5rc4 L3 Trace Schema & Source-Extraction Contract Foundation — clean review gate `YES`  
**Upstream Frozen Baselines:** v0.0.2 L1/L2; v0.0.3 L3; v0.0.4 Executable Governance

## 1. Decision Purpose

The accepted rc4 gate established two reviewed contracts above the accepted rc3 trace serialization:

1. `schemas/l3-trace-registry.schema.json` defines the bounded structural representation contract; and
2. the rc4 source-extraction contract defines how the current frozen v0.0.3 Pattern metadata shall be interpreted deterministically and fail closed.

v0.0.5rc5 now implements those reviewed contracts as an executable development control.

The implementation is intentionally source-aware: it does not treat `l3-trace-registry.yaml` as its own authority. It reconstructs the relation population from frozen Pattern metadata, validates the serialized registry structurally, resolves referenced L2 identities in the frozen authority registry, and requires exact agreement.

## 2. Authority and Execution Order

The governing order is:

```text
Frozen v0.0.3 Pattern Markdown metadata
        ↓ semantic trace authority
accepted rc1/rc2 trace representation model
        ↓ representation semantics
accepted rc3 l3-trace-registry.yaml
        ↓ subordinate serialization under test
accepted rc4 source-extraction contract
        ↓ deterministic interpretation rules
accepted rc4 trace JSON Schema
        ↓ structural representation contract
rc5 source-aware trace validator
        ↓ executable conformance proof
future separately gated generated views / resolver / enforcement
```

The validator executes reviewed rules; it does not create new trace semantics.

If validator behavior disagrees with the accepted rc4 contract, the validator is wrong. If the serialized registry disagrees with frozen Pattern metadata, the serialized registry is wrong. Frozen source is not changed merely to satisfy downstream code.

## 3. Scope

v0.0.5rc5 adds the independent development tool:

```text
tools/scaf_trace_validator/
```

including:

- `validator.py`;
- `requirements.txt`;
- `README.md`;
- sixteen focused regression tests;
- this governance record and current-state/navigation updates.

The tool validates the existing accepted artifacts without modifying:

- `l3-trace-registry.yaml`;
- `schemas/l3-trace-registry.schema.json`;
- `authority-registry.yaml`;
- frozen Pattern/normative source;
- frozen v0.0.4 executable controls or CI workflow.

## 4. Explicit Non-Capabilities

rc5 does **not** add:

- automatic generation or rewriting of `l3-trace-registry.yaml`;
- generated forward/reverse indexes;
- an authority/context resolver;
- project applicability inference;
- automatic Pattern selection;
- satisfaction, compliance, verification, evidence or closure inference;
- a formal general-purpose qualifier language beyond the accepted bounded rc4 extraction contract;
- new L3 Pattern content, M3/M4 or L4 guidance;
- code generation;
- CI/trust-bundle expansion or merge enforcement.

The rc5 validator is a development control. It is not retroactively part of the frozen v0.0.4 six-artifact external trust set.

## 5. Canonical Tool Surface

Canonical module:

```text
tools/scaf_trace_validator/validator.py
```

Canonical local execution from repository root:

```text
python -m tools.scaf_trace_validator.validator
```

Dependencies:

```text
PyYAML>=6.0,<7
jsonschema>=4.18,<5
```

The validator supports an explicit repository-root argument for local testing/review copies, but the production/frozen v0.0.4 CI trust path is unchanged by rc5.

## 6. Structural Validation

The validator loads:

```text
l3-trace-registry.yaml
schemas/l3-trace-registry.schema.json
```

using:

- duplicate-key-rejecting YAML loading;
- JSON Schema Draft 2020-12 meta-validation;
- validation of the serialized registry against the canonical rc4 trace schema.

Structural schema success is reported separately from source-aware proof.

Schema failure is fail closed and contributes to a non-zero validator result.

## 7. Frozen Pattern Source Reconstruction

The validator discovers the frozen Pattern catalog surface under:

```text
docs/l3/catalog/*/SCAF-PAT-*.md
```

For each Pattern it requires exactly one metadata row for:

```text
Pattern ID
Primary L2 Trace
Supporting L2 Trace
Constraint Inputs
```

Only the three trace rows create machine relations.

Narrative prose, including narrative sections that happen to mention valid or invalid `SCAF-*` identities, does not create additional relation records.

The current Pattern inventory is required to remain exactly twelve files/identities.

## 8. rc4 Extraction Contract Implementation

### 8.1 Primary and Supporting

`Primary L2 Trace` and `Supporting L2 Trace` are accepted only as comma-separated Markdown code-span L2 IDs under the reviewed rc4 syntax.

The validator rejects prose, semicolon clauses, malformed IDs, qualifier syntax, or otherwise unsupported tokens in these fields.

Each extracted relation receives `qualifier = null`.

### 8.2 Constraint Inputs

The implementation follows the accepted left-to-right source-association contract:

- semicolon is a hard qualifier-scope reset;
- comma is an item separator but does not clear active `applicable` scope;
- `applicable` can begin after earlier unqualified IDs and is non-retroactive;
- active `applicable` continues over following comma-separated IDs;
- `conditional` is accepted only for the reviewed one-ID `conditional <ID> where ...` form;
- direct `where ...` applies only to the immediately preceding ID;
- `outcomes when ...` is accepted only as the reviewed trailing-context marker;
- trailing context cannot be followed by another comma-separated ID before clause end;
- unsupported/ambiguous syntax fails closed.

### 8.3 Qualifier normalization

The executable implementation preserves the accepted rc4 bounded normalization:

- ID backticks are excluded;
- comma/semicolon separators are excluded;
- outer whitespace is removed;
- internal whitespace is canonicalized to one ASCII space;
- source words, case and punctuation are otherwise preserved;
- leading qualifier + trailing context is joined by one ASCII space;
- no material qualifier is represented as null.

The validator does not interpret qualifier prose as executable applicability logic.

## 9. Exact Source / Serialization Equality

After extraction resolves source-order qualifier scope, the validator applies the accepted canonical order:

1. `pattern_id` ascending;
2. relation type in fixed order:
   - `primary_realization_candidate`;
   - `supporting_realization`;
   - `constraint_input`;
3. `l2_id` ascending.

The reconstructed seven-field records must then be exactly equal to the serialized `relations` list.

This exact equality detects, among other failures:

- omitted relation;
- invented relation;
- wrong relation class;
- wrong source path;
- wrong source field;
- wrong source release;
- qualifier omission;
- qualifier alteration;
- qualifier reassociation;
- non-canonical record population/order.

## 10. Composite Identity and Ordering Proof

The validator independently proves uniqueness of:

```text
(pattern_id, relation_type, l2_id)
```

It does not rely on JSON Schema `uniqueItems` as proof of projected tuple uniqueness.

It separately proves the serialized list already uses the accepted canonical cross-record ordering.

## 11. L2 Authority Resolution

The validator loads frozen:

```text
authority-registry.yaml
```

with duplicate-key rejection and requires every serialized trace `l2_id` to resolve to an authority-registry record identity.

For the current accepted population this proves resolution of all 82 unique referenced L2 IDs.

This resolution proves identity existence only. It does not mean project applicability, Pattern selection, satisfaction, compliance, verification or closure.

## 12. Accepted Current Population

A successful current rc5 run shall report:

```text
Patterns:        12
Relations:       119
Primary:          23
Supporting:       41
Constraint:       55
Unique tuples:   119
Unique L2 IDs:    82
Qualifiers:       15
```

and:

```text
Schema validation:      PASS
Source reconstruction:  PASS
Authority resolution:   PASS
Canonical ordering:     PASS
Errors: 0
RESULT: PASS
```

These population checks are concise diagnostics in addition to, not replacements for, schema validation and exact source reconstruction.

## 13. Regression Foundation

rc5 adds sixteen focused regressions covering:

1. accepted repository PASS;
2. omitted relation rejection;
3. invented relation rejection;
4. projected tuple duplicate rejection even when object contents differ;
5. canonical-order shuffle rejection;
6. qualifier omission rejection;
7. qualifier reassociation rejection;
8. unresolved but well-formed L2 identity rejection;
9. wrong source path rejection;
10. wrong source field rejection;
11. Primary/Supporting prose rejection;
12. unknown Constraint leading qualifier rejection;
13. multi-ID `conditional` rejection;
14. trailing context followed by another ID rejection;
15. duplicate authoritative metadata-row rejection;
16. narrative-prose L2 mentions confirmed non-authoritative for machine edges.

Canonical test command:

```text
python -m unittest discover -s tools/scaf_trace_validator/tests -v
```

The existing frozen executable-governance test inventory remains separately unchanged at 41 tests. rc5 adds sixteen development-control regressions, so a local full test run contains 57 tests when both inventories are counted; this does **not** redefine the frozen v0.0.4 regression inventory.

## 14. Fail-Closed Behavior

The rc5 tool shall return non-zero when any governed proof fails, including:

- registry/schema load or schema conformance failure;
- duplicate YAML mapping key;
- missing/duplicate authoritative metadata row;
- unsupported extraction syntax;
- source/serialization mismatch;
- duplicate typed trace identity;
- canonical-order mismatch;
- unresolved L2 identity;
- accepted population inconsistency.

Diagnostics may continue after some failures when safe to provide useful review information, but an error can never produce `RESULT: PASS`.

## 15. Semantic Boundary

The validator proves:

```text
structurally valid
+ source-faithful
+ identity-resolved
+ canonically ordered
```

It does **not** prove:

```text
Applicable
Selected
Satisfied
Compliant
Verified
Closed
```

Nor does it prove that a Pattern is the best design choice for any project.

## 16. Frozen / Executable Non-Regression Boundary

rc5 must preserve byte-unchanged:

- frozen `docs/normative/` and `docs/l3/` trees;
- frozen `authority-registry.yaml` and `schemas/authority-registry.schema.json`;
- accepted rc3 `l3-trace-registry.yaml`;
- accepted rc4 `schemas/l3-trace-registry.schema.json`;
- frozen v0.0.4 manifest, validator, release-integrity, external-pin, CI-gate and workflow artifacts;
- existing 41 frozen executable-governance regressions;
- production external-trust CI-gate behavior.

No rc5 trace-validator artifact is inserted retroactively into the frozen v0.0.4 trust bundle.

## 17. Acceptance Target

rc5 is acceptable only if independent review confirms:

1. accepted rc4 schema/extraction semantics are implemented without semantic expansion;
2. accepted repository returns zero-error PASS with the expected 12 / 23 / 41 / 55 / 119 / 82 / 15 inventory;
3. independent source reconstruction equals the accepted registry exactly;
4. tuple uniqueness, canonical ordering and L2 resolution are executable checks rather than documentation claims;
5. representative source/registry mutations fail closed, including qualifier and unsupported-syntax cases;
6. narrative prose remains non-authoritative for relation creation;
7. all sixteen rc5 regressions pass with no unexpected skip;
8. all 41 frozen executable-governance regressions remain unchanged and pass;
9. production frozen v0.0.4 external-trust CI gate remains unchanged and passes;
10. no auto-generation, generated views, resolver, project inference, new L3/L4 or CI/trust expansion is falsely introduced;
11. no unresolved Critical, Major or Minor finding remains in rc5 scope.

## 18. Deferred Next Decisions

After rc5 review, the next scope shall be selected again by dependency/value analysis. Candidate later work may include generated forward/reverse trace views or additional enforcement integration, but rc5 does not pre-commit a later RC.
