# SCAF v0.0.6rc04 — SCAF-APP Concrete Project Application Serialization Foundation

**Development Release:** v0.0.6rc04  
**Status:** Concrete Serialization Foundation / Review Candidate  
**Date:** 2026-08-18  
**Upstream Frozen Baselines:** v0.0.2 L1/L2; v0.0.3 L3; v0.0.4 Executable Governance; v0.0.5 L3 Machine-Readable Traceability  
**Accepted Development Basis:** v0.0.6rc01 semantic foundation; v0.0.6rc03 accepted canonical record model after rc02 finding closure  
**Immediate Predecessor:** v0.0.6rc03 Project Application Record Basis-Role and State-Compatibility Hardening

## 1. Decision Purpose

The independent v0.0.6rc03 review returned a clean gate:

```text
Critical: 0
Major:    0
Minor:    0
Trivial:  0

SCAF-RC02-001: CLOSED
SCAF-RC02-002: CLOSED

V0.0.6RC03 SCAF-APP PROJECT APPLICATION RECORD BASIS-ROLE AND
STATE-COMPATIBILITY HARDENING GATE: YES
```

The accepted v0.0.6 SCAF-APP development chain now provides:

```text
rc01  semantic / authority boundary
  ↓
rc02  canonical logical Project Application Record model
  ↓
rc03  deterministic direct-basis roles + current-state compatibility
  ↓
rc04  concrete YAML serialization foundation
```

rc04 performs the next bounded step: it maps the accepted logical record contract into one concrete YAML representation so later schema and validator work can implement an already reviewed representation instead of inventing serialization semantics.

The core rule remains:

> **SCAF does not decide the engineering answer for the project. It makes the project applicability disposition, its direct basis, and its controlled provenance representable without transferring project decision authority to the representation or to tooling.**

## 2. Scope of rc04

rc04 defines only:

1. YAML as the initial concrete Project Application serialization format;
2. the repository reference fixture path `examples/project-application.yaml`;
3. the top-level dataset container shape;
4. exact serialization of the accepted canonical logical record fields;
5. exact YAML representation of the three accepted applicability tokens;
6. exact YAML representation of `disposition_basis` current-state members;
7. omission/empty-list rules for optional and repeating fields;
8. reference-list representation and role preservation;
9. deterministic record/list ordering rules for controlled generation and review;
10. bounded YAML restrictions needed to prevent ambiguous representation;
11. a concrete three-record fixture covering `applicable`, `not_applicable`, and `undetermined`.

rc04 does **not** introduce:

- a JSON Schema or other formal schema;
- a Project Application validator;
- a project-scope registry or resolver;
- a reference-object locator grammar or reference resolver;
- source-aware reconstruction of project judgments;
- automatic applicability classification;
- AI approval of engineering rationale;
- Project Design Authority automation;
- Pattern recommendation or selection;
- decision/deviation/risk/verification/evidence/closure lifecycle serialization;
- history/supersession/re-evaluation serialization;
- tailoring taxonomy;
- Effective Project Profile generation;
- context resolver/packager;
- CI applicability-completion enforcement;
- code generation;
- new L3 Patterns;
- L4 guidance.

A later RC may add schema/validation only after this serialization contract passes review.

## 3. Representation Authority Boundary

The YAML representation is subordinate project-side representation governed by the accepted SCAF-APP semantics.

It does not become:

- SCAF normative authority;
- Project Design Authority;
- requirement/design/risk/deviation authority;
- verification authority;
- evidence authority;
- closure authority;
- Pattern-selection authority;
- project-completion PASS/FAIL authority.

The representation records project disposition state. It does not create the underlying engineering judgment merely because a field contains text or references.

The framework-side normative target remains the frozen Project-Applicable Obligation identified by `scaf_authority_id`.

## 4. Concrete Format and Reference Fixture

The initial concrete format is **YAML**.

The repository reference fixture is:

```text
examples/project-application.yaml
```

That file is an illustrative serialization fixture for the SCAF representation contract. It is **not** a Project Application dataset for the SCAF repository itself and does not assert real project applicability decisions.

A real project adopting this contract may use a project-controlled path and filename. rc04 does not make `examples/project-application.yaml` a mandatory project repository path.

The fixture exists so reviewers and later executable-governance work can inspect one concrete representation of all three applicability states.

## 5. Top-Level Dataset Shape

The concrete YAML document shall contain exactly one top-level mapping with exactly one top-level member:

```yaml
records:
  - ...
```

`records` is a YAML sequence of zero or more Project Application Record mappings.

The top-level container does not create a new project-governance semantic dimension. It is only the serialization container for the accepted record population.

rc04 deliberately does not add top-level project metadata, project identity, scope registry, author, timestamp, completion status, approval state, or generation metadata.

Those concepts shall not be inferred from file location, Git authorship, repository identity, or YAML comments.

## 6. Canonical Record Serialization

Each `records` item shall be a YAML mapping using the accepted rc02/rc03 logical field names.

The canonical field order for controlled generation and review is:

```text
record_id
record_kind
representation_release
scaf_authority_id
scaf_source_release
project_scope_ref
applicability
disposition_basis
decision_refs
authority_refs
supporting_refs
```

Semantic consumers shall use field identity rather than physical mapping position. The ordering rule exists to make controlled generation, diff review, and deterministic projection stable; reordering a valid mapping does not change the underlying project judgment.

### 6.1 Scalar fields

The following fields serialize as YAML strings:

```text
record_id
record_kind
representation_release
scaf_authority_id
scaf_source_release
project_scope_ref
applicability
```

The initial constant/value contracts are:

```text
record_kind:            project_application
representation_release: v0.0.6rc04
scaf_source_release:     v0.0.2   # initial frozen target population
```

`scaf_authority_id` shall identify a frozen Project-Applicable Obligation. rc04 does not change the frozen authority population.

`project_scope_ref` is serialized as an opaque non-empty YAML string. rc04 does not infer parent/child scope, scope kind, or containment from punctuation or textual appearance.

### 6.2 Applicability tokens

The exact serialized token vocabulary is:

```text
applicable
not_applicable
undetermined
```

No aliases such as `yes`, `no`, `n/a`, `pending`, `open`, `pass`, or `fail` are part of the rc04 representation contract.

The tokens retain only the accepted applicability meaning and do not imply downstream state.

## 7. `disposition_basis` Serialization

`disposition_basis` shall serialize as a YAML mapping.

Its accepted members remain:

```text
summary
basis_refs
unresolved_reason
awaiting_refs
```

The canonical member order for controlled generation and review is:

```text
summary
basis_refs
unresolved_reason
awaiting_refs
```

State compatibility remains exactly the accepted rc03 contract:

| Member | `applicable` | `not_applicable` | `undetermined` |
|---|---|---|---|
| `summary` | allowed; may satisfy direct basis | allowed; may satisfy direct basis | allowed; supplementary only |
| `basis_refs` | allowed; may satisfy direct basis | allowed; may satisfy direct basis | allowed; may explain why unresolved |
| `unresolved_reason` | prohibited | prohibited | required exactly once |
| `awaiting_refs` | prohibited | prohibited | allowed 0..n |

### 7.1 Direct applicability-basis sufficiency

For `applicable` and `not_applicable`, at least one of the following shall be meaningfully populated:

```text
disposition_basis.summary
disposition_basis.basis_refs
```

The mere presence of:

```text
decision_refs
authority_refs
supporting_refs
```

shall not satisfy direct applicability-basis sufficiency.

rc04 serializes this accepted distinction; it does not change it.

### 7.2 `summary`

When present, `summary` serializes as a non-empty YAML string.

When absent, the member is omitted. It shall not be serialized as `null`, an empty string, or a placeholder such as `TBD` merely to satisfy field presence.

For `undetermined`, `summary` remains supplementary and cannot replace `unresolved_reason`.

### 7.3 `basis_refs`

`basis_refs` serializes as a YAML sequence of zero or more non-empty opaque reference strings.

The semantic role remains direct applicability basis: each target listed here shall directly establish, justify, or substantively support the current applicability disposition for the declared scope.

`basis_refs` may be empty when `summary` alone supplies direct basis for `applicable` / `not_applicable`, or when an `undetermined` state has no currently available controlled basis reference beyond its required unresolved explanation.

### 7.4 `unresolved_reason`

For `undetermined`, `unresolved_reason` shall be present exactly once and serialize as a non-empty YAML string.

For `applicable` and `not_applicable`, the member shall be omitted entirely.

It shall not be retained as `null`, an empty string, a historical note, or an ignored field after the current disposition resolves.

### 7.5 `awaiting_refs`

For `undetermined`, `awaiting_refs` serializes as a YAML sequence of zero or more non-empty opaque reference strings.

For `applicable` and `not_applicable`, the member shall be omitted entirely.

Historical unresolved inputs remain outside the current-state record after resolution unless a future separately reviewed history/re-evaluation model defines them.

## 8. Top-Level Reference Surfaces

The accepted role separation remains:

```text
basis_refs      -> direct applicability basis
decision_refs   -> controlled project decision/judgment trace
authority_refs  -> project authority / approval provenance
supporting_refs -> related controlled context
```

`decision_refs`, `authority_refs`, and `supporting_refs` each serialize as YAML sequences of zero or more opaque non-empty strings.

They shall always be present in the canonical rc04 record serialization, using `[]` when no references exist.

Their presence does not transfer authority and does not satisfy direct applicability-basis requirements.

The same controlled target may appear in more than one role-specific list only when it genuinely fulfills each represented role. Consumers shall not infer one role from presence in another list.

## 9. Omission, Empty and Null Rules

The concrete rc04 representation uses the following rules:

### 9.1 Required record fields

All eleven canonical top-level record fields shall be present exactly once:

```text
record_id
record_kind
representation_release
scaf_authority_id
scaf_source_release
project_scope_ref
applicability
disposition_basis
decision_refs
authority_refs
supporting_refs
```

### 9.2 Repeating reference fields

The following list-valued record fields shall always be present and use `[]` when empty:

```text
decision_refs
authority_refs
supporting_refs
```

Within `disposition_basis`, `basis_refs` shall also always be present and use `[]` when empty.

For `undetermined`, `awaiting_refs` shall be present even when empty, using `[]`.

For resolved states, `awaiting_refs` is prohibited and therefore omitted rather than serialized empty.

### 9.3 Optional scalar fields

Absent optional scalar fields are omitted, not serialized as `null` or empty strings.

This applies to:

```text
summary
```

and to `unresolved_reason` only outside its required `undetermined` state, where it is prohibited and omitted.

### 9.4 Null values

YAML `null` values are not part of the rc04 Project Application representation contract.

A missing value shall not be represented with `null`, `~`, or an empty scalar.

This keeps absence, prohibited state, empty reference population, and actual string content distinct.

## 10. Reference Scalar Contract

All rc04 reference values serialize as opaque non-empty YAML strings.

Examples include values resembling:

```text
project:scope:system
project:decision:D-17
project:authority:system-architect
project:artifact:ARCH-004
external:req:EXT-12
```

These examples do **not** freeze a locator grammar.

A consumer shall not infer:

- reference type from prefix syntax;
- scope hierarchy from delimiters;
- authority from a path-like string;
- artifact existence merely because a string is present;
- applicability correctness from successful string parsing.

Reference resolution and accepted locator grammar remain separately gated future work.

## 11. Deterministic Collection Ordering

For controlled generation, review fixtures, and future deterministic views, rc04 defines the following ordering rules.

### 11.1 Record ordering

`records` shall be ordered by exact `record_id` ascending.

Record order is serialization determinism, not project authority or priority.

### 11.2 Reference-list ordering

Within each of the following lists, reference strings shall be ordered by exact serialized string ascending:

```text
basis_refs
awaiting_refs
decision_refs
authority_refs
supporting_refs
```

Within one list, the same exact serialized reference string shall not appear more than once.

The same target may still appear across different role-specific lists when it genuinely fulfills each role, as accepted by rc03.

### 11.3 Mapping order

The canonical mapping order defined in Sections 6 and 7 shall be used by controlled generators and fixtures for stable human review.

No semantic precedence shall be inferred from mapping order.

## 12. Bounded YAML Restrictions

To keep the representation reviewable and avoid YAML features that could obscure the accepted logical contract, rc04 representation shall not use:

- duplicate mapping keys;
- YAML anchors or aliases;
- YAML merge keys;
- custom YAML tags;
- multi-document streams;
- non-string keys;
- null placeholders for absent values.

The Project Application document is one YAML document with one top-level `records` mapping.

Comments may be present for human explanation but are not Project Application data and shall not carry required engineering rationale, authority, or applicability semantics.

The concrete fixture uses quoted string values to make string typing visually explicit. A later schema/validator RC may define parser/profile details more formally, but shall not alter the accepted rc04 logical types or state semantics without a separately reviewed semantic change.

## 13. Concrete Fixture Coverage

`examples/project-application.yaml` contains three illustrative records solely to exercise the serialization contract:

```text
EXAMPLE-PA-001 -> applicable
EXAMPLE-PA-002 -> not_applicable
EXAMPLE-PA-003 -> undetermined
```

The fixture intentionally demonstrates:

- one applicable record with direct basis and downstream/supporting references;
- one not-applicable record with direct basis plus authority provenance;
- one undetermined record with required `unresolved_reason` and `awaiting_refs`;
- explicit empty lists where the contract requires a repeating field;
- omission of unresolved-only members from resolved records;
- opaque project-controlled scope/reference strings;
- deterministic record and reference ordering.

Fixture identifiers, project scopes, decisions, authorities and supporting artifacts are illustrative and carry no real project authority.

## 14. Representation-Invalid Versus Engineering-Unresolved

rc04 continues the accepted distinction.

A later representation validator may reject conditions such as:

- missing required record fields;
- unsupported applicability token;
- duplicate mapping keys;
- duplicate `record_id`;
- ambiguous duplicate active target/scope assertion under the accepted record model;
- null where a string/list contract requires another representation;
- `applicable` / `not_applicable` with neither meaningful `summary` nor non-empty `basis_refs`;
- `undetermined` without non-empty `unresolved_reason`;
- unresolved-only members on resolved current states;
- unordered/duplicate list items when deterministic serialization is required;
- unsupported YAML aliases/tags/merge behavior;
- unresolved framework target or scope/reference values once separately reviewed resolution contracts exist.

Engineering-unresolved work remains different.

For example, this can be a structurally valid Project Application record:

```yaml
applicability: "undetermined"
disposition_basis:
  basis_refs: []
  unresolved_reason: "Interface ownership is not yet assigned."
  awaiting_refs:
    - "project:decision:interface-owner"
```

The engineering question remains open. The representation is not invalid merely because the disposition is `undetermined`.

## 15. Prohibited Inferences

Neither the YAML representation nor later consumers are authorized to infer:

```text
record exists                    -> obligation applicable
applicable                       -> Pattern selected
applicable                       -> implemented
applicable                       -> satisfied / compliant
applicable                       -> verified / closed
not_applicable                   -> SCAF obligation deleted / weakened
not_applicable                   -> tailoring / deviation / waiver
undetermined                     -> project failure
undetermined                     -> malformed representation
basis reference exists           -> engineering rationale is correct
decision reference exists        -> direct applicability basis exists
authority reference exists       -> direct applicability basis exists
supporting reference exists      -> direct applicability basis exists
reference string parses          -> referenced authority/artifact exists
L3 Pattern exists                -> project applicability
No L3 Pattern                    -> project failure
primary realization candidate    -> Pattern selected
```

Machine-readable representation is not machine-owned engineering judgment.

## 16. Relationship to Frozen Framework Data

The rc04 Project Application representation remains separate from:

```text
authority-registry.yaml
l3-trace-registry.yaml
```

`authority-registry.yaml` remains frozen framework truth representation and shall not acquire project-specific applicability, scope, rationale, PDA identity, project design value, verification, evidence, or closure state.

`l3-trace-registry.yaml` remains frozen L2↔L3 catalog trace and shall not acquire Project Application disposition or Pattern-selection state.

The concrete Project Application representation references framework authority; it does not rewrite framework authority.

## 17. Schema / Validator Deferral Boundary

rc04 intentionally stops before schema and validator implementation.

A later schema/validator RC may encode or verify the accepted rc04 facts, including:

- required top-level `records` container;
- required field/type/cardinality rules;
- token vocabulary;
- state-dependent member rules;
- empty/omission/null rules;
- deterministic collection ordering;
- duplicate rejection;
- bounded YAML representation restrictions where supported by the loader/validation boundary;
- SCAF authority resolution against the accepted frozen authority representation;
- project-scope/reference resolution only after a separately reviewed resolution contract exists.

A later schema/validator shall not invent new engineering semantics merely because they are convenient to validate.

In particular it shall not:

- determine applicability from L3 Pattern presence;
- judge substantive engineering correctness of `summary` or referenced sources;
- auto-approve `not_applicable`;
- convert `undetermined` into project failure;
- infer PDA ownership from path/author/tool metadata;
- treat schema validity as satisfaction, verification, compliance, or closure.

## 18. Frozen / Non-Target Preservation

rc04 changes no frozen:

- v0.0.2 normative source;
- v0.0.3 L3 Pattern source;
- `authority-registry.yaml`;
- `l3-trace-registry.yaml`;
- existing schemas;
- authority validator;
- trace validator;
- trace views/query;
- release-integrity checker/manifest;
- external-pin checker;
- CI gate/workflow;
- production trust-set artifact.

The accepted regression inventories remain unchanged.

## 19. Review Gate

rc04 is ready for acceptance only if independent review confirms that:

1. the YAML representation is a faithful serialization of accepted rc01/rc03 semantics;
2. no field role or applicability meaning was silently changed;
3. direct basis remains limited to `summary` / `basis_refs`;
4. state-dependent current-state rules remain deterministic;
5. omission/empty/null behavior is unambiguous;
6. top-level and record serialization are sufficiently deterministic for later schema work;
7. reference strings remain opaque and do not create an unreviewed resolver grammar;
8. the fixture covers the three applicability states without asserting real project decisions;
9. representation validity remains distinct from engineering completion;
10. no schema/validator/AI applicability decision/Pattern selection/L4 capability is smuggled into the RC;
11. all frozen validation/regression/integrity checks remain clean.

A clean gate may permit consideration of a later Project Application schema foundation RC. It does not pre-authorize the specific schema or validator design.
