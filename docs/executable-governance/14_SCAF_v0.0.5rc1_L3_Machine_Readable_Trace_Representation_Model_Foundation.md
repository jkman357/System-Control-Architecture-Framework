# SCAF v0.0.5rc1 — L3 Machine-Readable Trace Representation Model Foundation

**Development Release:** v0.0.5rc1  
**Status:** Model Foundation / Review Candidate  
**Upstream Frozen Baselines:** v0.0.2 L1/L2; v0.0.3 L3; v0.0.4 Executable Governance

## 1. Decision Purpose

This RC opens the next controlled development line after the formal v0.0.4 freeze.

The selected scope is based on a post-baseline gap/dependency assessment rather than on an assumption that the next release must advance to L4.

The highest-priority current gap is that the frozen v0.0.3 L3 catalog already contains accepted many-to-many L2-to-L3 trace semantics, but those relations remain available only in human-readable Pattern metadata. The frozen L3 trace model explicitly states that a reverse view such as:

```text
L2 obligation -> candidate L3 patterns
```

is derived navigation only and that, once executable governance exists, generated navigation is preferable to dual manual maintenance.

The v0.0.4 executable-governance foundation now exists and is frozen. This RC therefore defines the **machine-readable representation model** needed before serialization, schema/validation, generated reverse views, authority/context resolution or later L4 context consumption can be added safely.

## 2. Scope

v0.0.5rc1 defines only:

1. the semantic/authority boundary for machine-readable L3 trace representation;
2. the controlled relation vocabulary;
3. the conceptual relation-record model;
4. deterministic identity and ordering rules for a future serialization;
5. source-locator and source-fidelity rules;
6. handling of existing human-readable qualifiers without inventing applicability logic;
7. forward/reverse derived-view semantics;
8. non-equivalence with project applicability, Pattern selection, satisfaction, compliance, verification or closure;
9. the bounded inputs/outputs expected from later schema, validator and resolver stages.

This RC does **not** create the machine-readable registry itself.

## 3. Frozen Source of Truth

The semantic authority for current L2-to-L3 catalog trace remains the frozen v0.0.3 Pattern Markdown metadata.

The authoritative fields are exactly:

```text
Primary L2 Trace
Supporting L2 Trace
Constraint Inputs
```

The existing Pattern prose under `## 5. L2 Trace` explains/rationalizes those metadata relations, but narrative prose is not an additional machine-readable edge source.

A future machine-readable representation is subordinate to the frozen Pattern metadata and must not become an independent trace authority.

If a representation disagrees with the frozen Pattern metadata, the representation is invalid; the frozen source is not rewritten to make the representation pass.

## 4. Current Frozen Trace Inventory

The current frozen catalog contains:

```text
Pattern identities:                  12
Primary Realization Candidate:       23
Supporting Realization:              41
Constraint Input:                    55
Total relation instances:           119
Unique referenced frozen L2 IDs:     82
```

All 119 current relation triples are unique under:

```text
(pattern_id, relation_type, l2_id)
```

The model intentionally permits the same `(pattern_id, l2_id)` pair to carry more than one relation type when the frozen source does so. Current examples exist in `SCAF-PAT-COM-001`, so a future serializer/validator must not collapse relation types by Pattern/L2 pair alone.

The 82 currently referenced IDs resolve to Project-Applicable Obligation records in the frozen v0.0.4 authority registry. This is an observed current inventory property, not a new rule that silently changes the frozen L3 semantic contract.

## 5. Controlled Relation Vocabulary

The future machine-readable representation shall use exactly these semantic relation identifiers for the current frozen L3 trace model:

| Machine Identifier | Frozen Human-Readable Meaning |
|---|---|
| `primary_realization_candidate` | `Primary L2 Trace` / Primary Realization Candidate |
| `supporting_realization` | `Supporting L2 Trace` / Supporting Realization |
| `constraint_input` | `Constraint Inputs` / Constraint Input |

These identifiers are representation terms for already-frozen semantics; they do not create new relation meaning.

The generic relation:

```text
satisfies
```

is prohibited.

No generic machine relation such as `related_to`, `implements`, `complies_with`, `verifies`, `closes` or `applicable_to` may be substituted for the three controlled relation classes without a separately reviewed semantic change.

## 6. Conceptual Relation Record

A future serialized relation record shall minimally represent the following concepts:

| Concept | Meaning |
|---|---|
| `pattern_id` | Existing frozen `SCAF-PAT-*` identity owning the trace metadata |
| `relation_type` | One of the three controlled machine identifiers |
| `l2_id` | Frozen upstream requirement identity referenced by the Pattern metadata |
| `pattern_source_path` | Repository-relative frozen Pattern Markdown path |
| `pattern_source_field` | Exact authoritative metadata field corresponding to the relation type |
| `source_release` | Frozen semantic source release (`v0.0.3` for the initial population) |
| `qualifier` | Optional controlled source qualifier associated with the relation; no automatic applicability semantics in this model |

This RC intentionally does not mandate YAML versus JSON, top-level serialization keys, schema syntax or a concrete filename. Those belong to a later serialization/schema gate.

### 6.1 Deterministic relation identity

For the initial model, a relation instance is uniquely identified by:

```text
(pattern_id, relation_type, l2_id)
```

`qualifier` is not part of relation identity.

If a future accepted source would require multiple semantically distinct records with the same triple, the model must be explicitly revised rather than silently inventing duplicate identities.

### 6.2 Deterministic ordering

A future canonical serialization shall use stable ordering based on:

1. `pattern_id` ascending;
2. relation-type order:
   - `primary_realization_candidate`;
   - `supporting_realization`;
   - `constraint_input`;
3. `l2_id` ascending.

Ordering is representation determinism, not semantic precedence between requirements or Patterns.

## 7. Source Locator Contract

Machine-readable trace shall not depend on line numbers, renderer-specific Markdown anchors or search-result positions.

A future relation record resolves its source using:

```text
pattern_source_path
+ pattern_id
+ pattern_source_field
```

The source field mapping is deterministic:

```text
primary_realization_candidate -> Primary L2 Trace
supporting_realization        -> Supporting L2 Trace
constraint_input              -> Constraint Inputs
```

A later source-aware validator must prove that:

1. `pattern_source_path` resolves inside the frozen L3 catalog;
2. the file has exactly the expected `pattern_id` identity;
3. the mapped authoritative metadata field exists;
4. `l2_id` is actually present in that field under the declared relation class;
5. `l2_id` resolves to the accepted frozen normative authority population;
6. where frozen authoritative metadata associates material qualifier text/context with the relation, that qualifier association is preserved for the correct `l2_id` / relation record;
7. material qualifier text/context is not omitted, semantically altered, scope-expanded, scope-truncated or associated with a different `l2_id` / relation record;
8. no representation relation is invented from narrative text outside the three authoritative metadata fields;
9. no authoritative metadata relation is omitted from the representation.

Exact qualifier extraction, grouping and serialization syntax remain deferred to a later serialization/schema gate. The model-level fidelity obligation does not create a formal condition language or executable project-applicability predicate.

## 8. Qualifier Preservation Boundary

Some frozen `Constraint Inputs` contain controlled natural-language qualifiers, including forms such as:

```text
applicable <L2 ID>
conditional <L2 ID> where ...
<L2 ID> where ...
```

Examples already exist in frozen Patterns for timing, interaction/session, security and resource conditions.

v0.0.5rc1 does **not** promote those phrases into a formal condition language.

Where frozen authoritative metadata associates material qualifier text/context with a relation, a future serialization shall preserve that qualifier association as controlled source text/context on the correct relation record. The qualifier:

- preserves source meaning/context;
- may be displayed in generated navigation;
- shall not be silently discarded where material;
- shall not be semantically altered, scope-expanded, scope-truncated or associated with a different `l2_id` / relation record;
- must not be interpreted by rc1 as an executable project-applicability predicate;
- must not be converted into project selection or satisfaction state.

Formal machine-evaluable conditional semantics, if later needed, require a separate model/schema/review gate.

## 9. No Duplication into `authority-registry.yaml`

The frozen v0.0.4 `authority-registry.yaml` remains a 294-record representation of frozen normative authority.

This RC does not:

- add `SCAF-PAT-*` records to that registry;
- populate its currently empty `relations` fields;
- convert it into a mixed normative-authority + Pattern catalog registry;
- alter the frozen authority-registry schema or validator.

The future L3 trace representation should remain a separate subordinate representation surface so normative authority identity and L3 catalog trace do not become conflated.

A concrete filename such as `l3-trace-registry.yaml` is intentionally **not** frozen by rc1; naming/serialization belongs to the next implementation gate.

## 10. Derived Forward and Reverse Views

Once a validated machine-readable trace representation exists, tools may generate views such as:

```text
Pattern -> traced L2 relations
```

and:

```text
L2 ID -> traced L3 Patterns
```

Generated views are derived navigation only.

A reverse view must preserve at least:

- `pattern_id`;
- `relation_type`;
- any material controlled qualifier.

It must not flatten all relation classes into an undifferentiated list labelled `candidate patterns`, because `constraint_input` is semantically different from a realization candidate.

The generated view is reproducible output, not independently edited trace authority.

## 11. Resolver Boundary

This model is a prerequisite for a later Authority / Engineering Context Resolver, but rc1 does not implement one.

A later resolver may use the representation to answer bounded navigation questions such as:

```text
Which frozen L3 Patterns trace to this frozen L2 ID?
Which frozen L2 IDs trace from this Pattern, and under what relation class?
Which canonical source artifacts should be loaded to inspect that trace?
```

A resolver result remains navigation/context output.

The following inference remains invalid:

```text
Resolved / Traced
        => Applicable
        => Selected
        => Satisfied
        => Compliant
        => Verified
        => Closed
```

No such implication is authorized by this model.

## 12. Project Authority Boundary

Project-side Pattern decisions remain under Project Design Authority and project application governance.

Machine-readable catalog trace does not decide:

- whether an L2 obligation is applicable to a project;
- whether a Pattern should be considered or selected;
- whether a Pattern requires adaptation;
- whether another non-catalog mechanism is preferable;
- whether implementation is correct;
- whether verification/evidence is sufficient;
- whether an obligation may be closed.

The frozen L3 project-selection states (`Not Evaluated`, `Considered`, `Selected`, `Selected with Adaptation`, `Rejected`, `Superseded`) are not stored or inferred by the rc1 trace model.

## 13. L4 Boundary

This RC is not an L4 release.

It does not introduce implementation or verification guidance and does not assume that L4 must be the next development step.

The trace representation is useful to later L4 work because it can provide deterministic navigation from frozen obligations to frozen Pattern context. Whether, when and how L4 guidance is introduced remains demand/dependency driven and separately gated.

## 14. Expected Later Stages

Subject to separate review gates, a likely dependency progression is:

```text
rc1 — trace representation model
        ↓
concrete serialization contract / initial 119-relation representation
        ↓
schema + source-aware trace validator
        ↓
generated forward/reverse views
        ↓
authority / engineering-context resolver
        ↓
project-application and/or L4 context consumption as justified by need
```

This sequence is a dependency model, not a commitment to exact RC numbering or mandatory future scope.

## 15. rc1 Acceptance Criteria

v0.0.5rc1 is acceptable only if independent review confirms all of the following:

1. frozen v0.0.2/v0.0.3/v0.0.4 baselines are not reopened;
2. the three machine relation identifiers faithfully represent the frozen L3 relation classes;
3. the generic `satisfies` shortcut remains prohibited;
4. the relation-record identity model permits current multi-type Pattern/L2 pairs;
5. qualifier handling preserves controlled source text without inventing applicability semantics;
6. `authority-registry.yaml` remains separate and unchanged;
7. generated reverse views are derived and relation-type preserving;
8. no project applicability/selection/satisfaction/compliance/verification/closure authority is inferred;
9. current inventory is correctly stated as 12 Patterns / 119 relations / 82 unique L2 IDs with 23 / 41 / 55 relation counts;
10. the frozen v0.0.4 executable controls and 41 regressions remain unchanged and passing;
11. README presents current state/navigation while detailed release history remains in CHANGELOG;
12. no L4, new L3 Pattern, project inference, serialization/schema/validator, generated index or code-generation capability is falsely claimed by rc1.

## 16. Explicitly Deferred

Not implemented by v0.0.5rc1:

- concrete L3 trace YAML/JSON serialization;
- trace schema;
- trace parser/source-aware validator;
- generated forward or reverse index;
- authority/context resolver;
- project applicability inference;
- Pattern selection automation;
- satisfaction/compliance/verification/evidence/closure inference;
- project-side Pattern selection records;
- non-empty `authority-registry.yaml` relations;
- new L3 Patterns / third tranche / SEC-primary work;
- M3/M4 maturity;
- L4 implementation/verification guidance;
- code generation;
- additional CI/trust/signing/provenance capability.
