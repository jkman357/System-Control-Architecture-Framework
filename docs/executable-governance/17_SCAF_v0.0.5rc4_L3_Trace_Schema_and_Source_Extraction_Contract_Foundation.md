# SCAF v0.0.5rc4 — L3 Trace Schema & Source-Extraction Contract Foundation

**Development Release:** v0.0.5rc4  
**Status:** Schema / Source-Extraction Contract Foundation / Review Candidate  
**Upstream Accepted State:** v0.0.5rc3 L3 Machine-Readable Trace Serialization Foundation — clean review gate `YES`  
**Upstream Frozen Baselines:** v0.0.2 L1/L2; v0.0.3 L3; v0.0.4 Executable Governance

## 1. Decision Purpose

The accepted rc3 serialization proves that the current frozen L3 trace population can be represented exactly as 119 typed records in `l3-trace-registry.yaml`. The next dependency is not yet executable validation; it is first to define the representation schema and the deterministic interpretation contract that a later validator must implement.

Without a reviewed extraction contract, parser code could silently become a second semantic authority by deciding for itself how frozen Markdown qualifiers, grouped IDs and source fields are interpreted.

v0.0.5rc4 therefore defines two bounded contracts:

1. a Draft 2020-12 structural schema for the accepted rc3 trace serialization; and
2. a deterministic, fail-closed source-extraction contract for reconstructing the current frozen v0.0.3 trace population.

No trace validator/parser implementation is introduced in this RC.

## 2. Authority and Dependency Order

The accepted order remains:

```text
Frozen v0.0.3 Pattern Markdown metadata
        ↓ semantic trace authority
accepted rc1/rc2 trace representation model
        ↓ representation semantics
accepted rc3 l3-trace-registry.yaml
        ↓ concrete subordinate serialization
rc4 source-extraction contract
        ↓ deterministic interpretation rules
rc4 trace JSON Schema
        ↓ structural representation contract
future source-aware validator/parser
        ↓ executable proof / enforcement
future generated views / resolver consumers
```

The schema and extraction contract are subordinate to frozen Pattern metadata. Neither may redefine the frozen L3 semantic meaning.

If executable code later disagrees with this reviewed contract, the code is wrong. If `l3-trace-registry.yaml` disagrees with frozen Pattern metadata, the registry is wrong. Frozen source is not rewritten to make downstream artifacts pass.

## 3. Scope

v0.0.5rc4 adds:

- `schemas/l3-trace-registry.schema.json`;
- this source-extraction/schema governance record;
- current-state/navigation updates.

It defines:

- exact top-level serialization keys and current representation version binding;
- exact seven-field relation-record structure;
- required/unknown-field policy;
- controlled relation vocabulary and relation-type/source-field binding;
- current frozen Pattern identity/source-path binding;
- current frozen population cardinality constraints;
- qualifier null/string structural rule;
- the deterministic extraction source surface;
- normalization, grouping, qualifier-scope and fail-closed rules for the current frozen syntax;
- the boundary between schema-enforceable rules and future source-aware executable proof.

## 4. Explicit Non-Capabilities

rc4 does **not** add:

- a trace parser or validator executable;
- automatic regeneration of `l3-trace-registry.yaml`;
- a generated reverse/forward index;
- an authority/context resolver;
- formal qualifier grammar beyond the bounded current-source extraction contract;
- machine-evaluable project applicability;
- automatic Pattern selection;
- satisfaction, compliance, verification, evidence or closure inference;
- new L3 Patterns, M3/M4 or L4 guidance;
- code generation;
- CI/trust expansion.

The existing frozen v0.0.4 `tools/scaf_validator` continues to validate `authority-registry.yaml`; it does not become the trace validator in rc4.

## 5. Trace Schema Contract

Canonical schema path:

```text
schemas/l3-trace-registry.schema.json
```

Schema dialect:

```text
JSON Schema Draft 2020-12
```

The schema is intentionally bound to the currently accepted rc3 representation:

```text
trace_registry_version = 1
representation_release = v0.0.5rc3
source_release          = v0.0.3 for every relation
```

A later serialization change that requires different values must be separately reviewed rather than silently accepted by a permissive current schema.

### 5.1 Top-level object

Exactly these keys are allowed and required:

```text
trace_registry_version
representation_release
relations
```

Unknown top-level keys are rejected.

For the current frozen population, `relations` is structurally bounded to exactly 119 items.

### 5.2 Relation record

Every relation record requires exactly these seven keys:

```text
pattern_id
relation_type
l2_id
pattern_source_path
pattern_source_field
source_release
qualifier
```

Unknown relation-record keys are rejected.

Current controlled relation identifiers remain exactly:

```text
primary_realization_candidate
supporting_realization
constraint_input
```

The schema binds relation class to source field:

```text
primary_realization_candidate -> Primary L2 Trace
supporting_realization        -> Supporting L2 Trace
constraint_input              -> Constraint Inputs
```

The schema also binds each of the twelve accepted frozen `pattern_id` values to its current frozen repository-relative `pattern_source_path`.

`l2_id` is structurally restricted to the accepted SCAF L2-domain identity shape. Actual membership in frozen normative authority is a later source-aware validator obligation, not a JSON Schema claim.

`qualifier` is always present and is either:

```text
null
```

or a non-empty string.

The schema intentionally does not interpret qualifier text as a condition expression.

### 5.3 Current population constraints encoded structurally

The current schema binds the accepted rc3 population counts:

```text
119 total relation records
23 primary_realization_candidate
41 supporting_realization
55 constraint_input
15 non-null qualifier records
```

These counts are current frozen-population constraints. They do not replace source reconstruction.

### 5.4 Schema limitations are deliberate

Standard JSON Schema is not used as a substitute for source-aware semantic proof.

The rc4 schema does **not** claim to prove:

- uniqueness of the projected identity tuple `(pattern_id, relation_type, l2_id)` when two otherwise different objects could share that tuple;
- canonical cross-record sort order;
- that `l2_id` actually resolves in `authority-registry.yaml`;
- that a referenced Pattern file exists or still contains the claimed metadata;
- exact source membership / no omitted or invented relation;
- qualifier source fidelity or correct qualifier-to-ID association;
- source-order parsing correctness.

Those are future source-aware validator obligations.

`uniqueItems: true` rejects byte/data-equivalent duplicate relation objects, but it is **not** treated as proof of composite tuple uniqueness.

## 6. Authoritative Extraction Surface

Only the frozen Pattern metadata table is an extraction source for machine trace relations.

For each frozen Pattern file, a future parser shall locate exactly one metadata-table row for each of:

```text
Pattern ID
Primary L2 Trace
Supporting L2 Trace
Constraint Inputs
```

Machine relations are created only from these three trace fields:

```text
Primary L2 Trace
Supporting L2 Trace
Constraint Inputs
```

Narrative prose under `## 5. L2 Trace`, other headings, examples, tables or prose shall not create additional relations.

Missing or duplicate authoritative metadata rows are extraction errors. A future parser shall fail closed rather than guess which row is authoritative.

## 7. Field-to-Relation Extraction

Mapping is exact:

```text
Primary L2 Trace
    -> primary_realization_candidate

Supporting L2 Trace
    -> supporting_realization

Constraint Inputs
    -> constraint_input
```

### 7.1 Primary and supporting fields

For the frozen v0.0.3 population, `Primary L2 Trace` and `Supporting L2 Trace` are restricted to simple comma-separated Markdown code-span L2 IDs.

Accepted conceptual form:

```text
`SCAF-XXX-NNN`, `SCAF-YYY-NNN`, ...
```

A future parser shall:

1. read the metadata value cell only;
2. extract each backtick-delimited SCAF L2 identity in source order;
3. allow only comma separators and whitespace outside the ID code spans;
4. emit one relation per ID with `qualifier = null`;
5. reject unrecognized prose, semicolon clauses, qualifier keywords or malformed IDs in these two fields.

No narrative inference is permitted.

## 8. Constraint-Input Extraction State Contract

`Constraint Inputs` contains the only current frozen qualifier syntax. The rc4 contract defines only the forms actually present in frozen v0.0.3 source.

A future parser shall process the value left-to-right while preserving source association.

### 8.1 Hard scope delimiter

A semicolon (`;`) is a hard qualifier-scope boundary.

At every semicolon:

```text
active leading qualifier := none
```

A semicolon is not part of serialized qualifier text.

### 8.2 Comma behavior

A comma separates IDs/items but does **not** necessarily clear an active leading `applicable` qualifier.

This distinction is required by current frozen forms such as:

```text
applicable `SCAF-SEC-010`, `SCAF-SEC-022`
```

and:

```text
applicable `SCAF-INT-008`, `SCAF-RUN-021`, `SCAF-ROB-004`
```

### 8.3 Leading `applicable`

When the literal keyword `applicable` occurs immediately before an L2 ID, it starts an `applicable` qualifier scope at that point.

The qualifier:

- applies to that ID;
- continues across following comma-separated IDs;
- does not apply retroactively to IDs that appeared before the keyword;
- ends at a semicolon, end of field, or another explicitly recognized leading qualifier.

Each relation in that active group receives:

```text
qualifier: applicable
```

unless that individual ID also has an accepted trailing-context phrase, in which case Section 8.6 applies.

This rule covers current frozen forms where `applicable` begins at the start of the field, after a semicolon, or after earlier unqualified comma-separated IDs.

### 8.4 Leading `conditional`

The current frozen contract accepts `conditional` only in the current source form:

```text
conditional `<L2 ID>` where <free text>
```

For rc4 extraction:

- exactly one L2 ID shall follow `conditional` before its trailing `where ...` context;
- the canonical qualifier is `conditional` plus one ASCII space plus the trailing context;
- the clause ends at semicolon or end of field;
- any multi-ID conditional group or conditional clause without trailing context is unsupported and shall fail closed pending a separately reviewed contract change.

Current examples serialize as:

```text
conditional where retry repeats/interleaves Interaction exchanges
conditional where retry continuity crosses/reuses connection sessions
```

### 8.5 Unqualified trailing context

The current source permits an L2 ID with directly associated trailing context beginning with:

```text
where ...
```

The trailing context attaches only to the immediately preceding ID.

Examples include:

```text
`SCAF-TIME-011` where storage/resource budget is material
`SCAF-INT-010` where session identity is material
```

The canonical qualifier is the trimmed trailing text beginning with `where`.

### 8.6 Leading qualifier plus trailing context

The current source also contains a leading qualifier plus trailing context, for example:

```text
applicable `SCAF-INT-013` outcomes when retry follows an Interaction failure
```

Canonical qualifier construction is:

```text
<leading qualifier> + " " + <trailing context>
```

which yields:

```text
applicable outcomes when retry follows an Interaction failure
```

A trailing context applies only to the immediately preceding ID. Under the current rc4 contract, no further comma-separated ID may follow that trailing-context text before semicolon/end. Any such new form shall fail closed until separately specified.

### 8.7 Recognized trailing-context starts

For the frozen v0.0.3 source population, the recognized material trailing-context starts are exactly:

```text
where
outcomes when
```

The full trailing text from the recognized marker to the clause boundary is preserved after whitespace canonicalization.

New prose forms are not guessed. They require a separately reviewed extraction-contract change.

## 9. Canonical Text Normalization

For source qualifier fidelity, a future parser shall use the following bounded normalization:

1. Markdown backticks delimit L2 IDs and are not part of qualifier output;
2. separators (comma and semicolon) are not part of qualifier output;
3. leading/trailing whitespace is removed;
4. runs of whitespace inside qualifier text are canonicalized to one ASCII space;
5. source case, punctuation and words are otherwise preserved;
6. a leading qualifier and trailing context are joined with exactly one ASCII space;
7. when no material qualifier applies, serialized value is YAML/JSON null, not an empty string.

The parser shall not paraphrase, lowercase, reorder, synonym-normalize or interpret qualifier prose.

## 10. Source Order versus Canonical Registry Order

Extraction first reconstructs relations in frozen source order so qualifier scope can be evaluated correctly.

Only after all source associations are resolved shall the output population be sorted into the accepted canonical registry order:

1. `pattern_id` ascending;
2. relation type:
   - `primary_realization_candidate`;
   - `supporting_realization`;
   - `constraint_input`;
3. `l2_id` ascending.

Canonical output ordering is representation determinism. It is not requirement or Pattern precedence.

## 11. Fail-Closed Rule for New Source Syntax

The extraction contract is deliberately bounded to the frozen v0.0.3 forms reviewed in rc4.

A future parser shall fail rather than infer meaning when it encounters, for example:

- an unknown leading qualifier keyword;
- an unknown trailing-context construction;
- malformed or non-code-span L2 identity syntax;
- multiple IDs in a `conditional` clause;
- trailing context followed by another comma-separated ID in the same clause;
- ambiguous Markdown structure;
- missing/duplicate authoritative metadata rows;
- prose in Primary/Supporting fields;
- a source form whose qualifier scope cannot be determined by Sections 7–9.

New syntax must first be added to the controlled extraction contract and reviewed. Parser implementation is not allowed to silently expand the language.

## 12. Expected Reconstructed Population

Applying this contract to the current frozen source shall reconstruct exactly:

```text
12 Pattern identities
23 primary_realization_candidate
41 supporting_realization
55 constraint_input
119 total relation records
82 unique referenced frozen L2 IDs
119 unique (pattern_id, relation_type, l2_id) tuples
15 non-null qualifier associations
```

The accepted qualifier associations remain those reviewed in rc3. rc4 does not change `l3-trace-registry.yaml`; its `representation_release` therefore remains `v0.0.5rc3`.

## 13. Future Source-Aware Validator Proof Obligations

A later executable validator may implement this contract only after separate review. At minimum it shall eventually prove:

- trace registry validates against the canonical rc4 schema;
- exactly one authoritative source metadata row exists for each required field;
- source extraction reproduces exactly the serialized relation set;
- relation-type/source-field mapping is exact;
- each `pattern_source_path` and `pattern_id` resolve together;
- all `l2_id` values resolve in accepted frozen normative authority;
- no source relation is omitted and no relation is invented;
- `(pattern_id, relation_type, l2_id)` tuples are unique;
- qualifier association and canonical qualifier text are source-faithful;
- canonical cross-record ordering is exact;
- unsupported source syntax fails closed.

This section is a future executable-proof target, not a claim that rc4 already implements it.

## 14. Non-Regression Boundary

rc4 must preserve unchanged:

- frozen `docs/normative/` and `docs/l3/` bytes;
- frozen `authority-registry.yaml` and its schema;
- frozen v0.0.4 executable controls, tests, manifest and workflow;
- accepted rc3 `l3-trace-registry.yaml` bytes;
- accepted 41 executable-governance regression tests;
- production external-trust CI-gate behavior.

The current trace schema is an added development artifact and is not retroactively part of the frozen v0.0.4 six-artifact external trust set.

## 15. Acceptance Target

rc4 is acceptable only if independent review confirms that:

1. the schema validates the accepted rc3 trace registry and rejects structurally invalid variants within its documented responsibility;
2. schema responsibility is not confused with future source-aware proof;
3. the extraction contract deterministically reconstructs the current 119-record / 15-qualifier population without narrative inference;
4. qualifier scope for all current `applicable`, `conditional`, `where ...`, and `outcomes when ...` forms is unambiguous;
5. unsupported syntax is explicitly fail-closed;
6. the accepted rc1/rc2/rc3 semantic, serialization and authority boundaries remain intact;
7. no parser/validator/generator capability is falsely claimed as implemented;
8. frozen/control identities, 41 regressions and production CI-gate behavior remain intact.
