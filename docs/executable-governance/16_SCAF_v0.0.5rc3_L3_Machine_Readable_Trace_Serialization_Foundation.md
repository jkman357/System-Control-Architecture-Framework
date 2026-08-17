# SCAF v0.0.5rc3 — L3 Machine-Readable Trace Serialization Foundation

**Development Release:** v0.0.5rc3  
**Status:** Serialization Foundation / Review Candidate  
**Upstream Frozen Baselines:** v0.0.2 L1/L2; v0.0.3 L3; v0.0.4 Executable Governance  
**Accepted Model Basis:** v0.0.5rc1 model as amended by v0.0.5rc2

## 1. Decision Purpose

v0.0.5rc1 defined the machine-readable L3 trace representation model. The independent rc1 review returned `YES, AFTER MINOR CLEANUP`. v0.0.5rc2 closed both model findings and its independent review returned:

```text
R1-01: RESOLVED
R1-02: RESOLVED
V0.0.5 L3 TRACE MODEL DETERMINISM / QUALIFIER-FIDELITY CLEANUP GATE: YES
```

The next dependency is a concrete, reviewable serialization of the already-frozen 119 L2-to-L3 trace relations. Schema enforcement, source-aware validator implementation, generated views and resolver behavior all require a concrete representation first.

This RC therefore creates the initial machine-readable L3 trace serialization while keeping frozen Pattern Markdown metadata as semantic authority.

## 2. Scope

v0.0.5rc3 adds exactly one new machine-readable representation surface:

```text
l3-trace-registry.yaml
```

It also records the serialization contract and updates current-state navigation/history.

This RC does **not** add:

- a JSON Schema for the trace registry;
- a trace parser/validator tool;
- generated forward/reverse indexes;
- an authority/context resolver;
- formal machine-evaluable qualifier grammar;
- automatic project applicability or Pattern selection;
- satisfaction, compliance, verification, evidence or closure inference;
- non-empty relations in `authority-registry.yaml`;
- new L3 Patterns, M3/M4 work or L4 guidance;
- new CI/trust enforcement capability.

## 3. Semantic Authority Boundary

The frozen v0.0.3 Pattern Markdown metadata remains the semantic trace authority.

The authoritative fields remain exactly:

```text
Primary L2 Trace
Supporting L2 Trace
Constraint Inputs
```

`l3-trace-registry.yaml` is a subordinate representation. If it disagrees with frozen Pattern metadata, the serialization is wrong; the frozen source is not changed to make the serialization pass.

The representation does not become project design authority, verification authority or closure authority.

## 4. Concrete Serialization Surface

The canonical rc3 representation is repository-root:

```text
l3-trace-registry.yaml
```

The file is UTF-8 YAML and has exactly these top-level data keys:

```yaml
trace_registry_version: 1
representation_release: v0.0.5rc3
relations: [...]
```

`trace_registry_version` identifies the serialization-contract generation, not semantic requirement maturity.

`representation_release` identifies the SCAF development release that serialized the representation. It does not replace each relation's frozen semantic `source_release`.

No schema is introduced in rc3; the exact key/type constraints are a contract for a later schema gate.

## 5. Relation Record Shape

Every rc3 relation record contains all seven fields in this canonical presentation order:

```text
pattern_id
relation_type
l2_id
pattern_source_path
pattern_source_field
source_release
qualifier
```

Meanings remain those accepted by the rc1/rc2 model:

| Field | rc3 serialization rule |
|---|---|
| `pattern_id` | frozen `SCAF-PAT-*` identity owning the metadata relation |
| `relation_type` | exactly one accepted controlled relation identifier |
| `l2_id` | referenced frozen L2 authority identity |
| `pattern_source_path` | repository-relative frozen Pattern Markdown path |
| `pattern_source_field` | exact authoritative metadata field name |
| `source_release` | `v0.0.3` for every initial relation |
| `qualifier` | `null` when no material qualifier is associated; otherwise canonical source-fidelity text |

Mapping remains exact:

```text
Primary L2 Trace    -> primary_realization_candidate
Supporting L2 Trace -> supporting_realization
Constraint Inputs   -> constraint_input
```

The generic `satisfies` relation remains prohibited.

## 6. Population and Identity Contract

The initial serialization contains exactly:

```text
Pattern identities:                  12
Primary relations:                   23
Supporting relations:                41
Constraint relations:                55
Total relation records:             119
Unique referenced frozen L2 IDs:     82
Unique relation triples:            119
Duplicate relation triples:           0
```

A relation identity remains:

```text
(pattern_id, relation_type, l2_id)
```

The same Pattern/L2 pair may therefore appear more than once under different relation types when the frozen source does so.

All 82 currently referenced L2 IDs resolve in the frozen v0.0.4 authority registry. That observed population fact does not authorize trace serialization to redefine authority-registry semantics.

## 7. Canonical Ordering

The accepted rc2 ordering rule is realized directly in `l3-trace-registry.yaml`.

Relations **shall** be ordered by:

1. `pattern_id` ascending;
2. relation type in this fixed order:
   1. `primary_realization_candidate`;
   2. `supporting_realization`;
   3. `constraint_input`;
3. `l2_id` ascending.

Mapping-key presentation order is also kept stable as listed in Section 5 for reviewability and byte-diff clarity, but mapping-key order does not create semantic precedence.

## 8. Qualifier Serialization Contract

### 8.1 Purpose

`qualifier` preserves material source context only. It is not an executable applicability expression.

Every relation record includes the key:

```yaml
qualifier: null
```

when no material source qualifier is associated.

Where material context exists, `qualifier` contains a canonical plain-text form derived from the frozen metadata association.

### 8.2 Canonicalization for the initial frozen population

For the current v0.0.3 metadata population:

- a leading `applicable` qualifier is serialized as `applicable` and applies to the L2 IDs it qualifies in the frozen metadata sequence;
- a leading `conditional` qualifier is preserved as `conditional` and combined with its associated trailing context where present;
- direct trailing source context after an L2 ID, such as `where ...` or `outcomes when ...`, is preserved in the relation's qualifier text;
- when a leading qualifier and trailing context both apply to one relation, the canonical qualifier is their source-order concatenation separated by one space;
- qualifier text is source-fidelity context, not a parsed predicate AST or normalized project condition.

The current initial serialization contains **15 non-null qualifiers**.

The exact qualified records are:

| Pattern | L2 ID | Canonical qualifier |
|---|---|---|
| `SCAF-PAT-COM-001` | `SCAF-TIME-007` | `applicable` |
| `SCAF-PAT-LCM-001` | `SCAF-SEC-010` | `applicable` |
| `SCAF-PAT-LCM-001` | `SCAF-SEC-022` | `applicable` |
| `SCAF-PAT-PST-001` | `SCAF-TIME-011` | `where storage/resource budget is material` |
| `SCAF-PAT-REC-001` | `SCAF-INT-007` | `conditional where retry repeats/interleaves Interaction exchanges` |
| `SCAF-PAT-REC-001` | `SCAF-INT-010` | `conditional where retry continuity crosses/reuses connection sessions` |
| `SCAF-PAT-REC-001` | `SCAF-INT-013` | `applicable outcomes when retry follows an Interaction failure` |
| `SCAF-PAT-SUP-001` | `SCAF-INT-010` | `where session identity is material` |
| `SCAF-PAT-SYN-001` | `SCAF-SEC-025` | `applicable` |
| `SCAF-PAT-SYN-001` | `SCAF-TIME-007` | `applicable` |
| `SCAF-PAT-TIM-001` | `SCAF-INT-007` | `applicable` |
| `SCAF-PAT-TIM-001` | `SCAF-INT-008` | `applicable` |
| `SCAF-PAT-TIM-002` | `SCAF-INT-008` | `applicable` |
| `SCAF-PAT-TIM-002` | `SCAF-ROB-004` | `applicable` |
| `SCAF-PAT-TIM-002` | `SCAF-RUN-021` | `applicable` |

A later source-aware validator must reconstruct and verify this association against frozen metadata. rc3 does not implement that validator.

### 8.3 Explicit non-semantics

A non-null qualifier does **not** mean that the referenced obligation is automatically applicable to a project.

```text
qualifier fidelity
!= executable applicability inference
!= project Pattern selection
!= satisfaction
!= compliance
!= verification
!= closure
```

## 9. Source Locator and Fidelity

Each relation points back to frozen source using:

```text
pattern_source_path
+ pattern_id
+ pattern_source_field
```

No line number, rendered Markdown slug or search-result position is used.

A later source-aware validator is expected to prove the accepted rc2 obligations, including:

- source path and Pattern identity resolution;
- field/relation-class fidelity;
- exact relation membership and no omission/invention;
- L2 identity resolution;
- material qualifier fidelity and correct relation association;
- canonical ordering and duplicate-triple rejection.

Those checks are future executable work, not a capability claim of rc3.

## 10. Separation from `authority-registry.yaml`

The frozen v0.0.4 authority registry remains unchanged:

```text
294 records
218 Project-Applicable Obligations
76 Framework Normative Invariants
0 SCAF-PAT-* records
294 / 294 relations = []
```

`l3-trace-registry.yaml` does not replace, extend or mutate that frozen normative-authority representation.

The two registries answer different questions:

```text
authority-registry.yaml
-> what frozen normative authority identities exist and where they resolve

l3-trace-registry.yaml
-> what frozen L3 catalog trace relations already exist in Pattern metadata
```

## 11. Derived Views and Future Consumers

A future validated trace registry may support deterministic generated views such as:

```text
Pattern -> typed L2 trace
L2 obligation -> typed candidate/supporting/constraint Pattern relations
```

Those views remain derived navigation. They must preserve relation type and material qualifier context.

A later resolver may consume the validated trace registry, but a resolver result remains navigation/context reconstruction rather than project authority.

## 12. Non-Regression Boundary

rc3 must preserve byte identities of the frozen v0.0.2/v0.0.3/v0.0.4 surfaces, including:

- `docs/normative/`;
- `docs/l3/`;
- `authority-registry.yaml`;
- `schemas/authority-registry.schema.json`;
- all accepted v0.0.4 executable controls, tests and workflow;
- the v0.0.4 frozen-baseline manifest.

The accepted 41 executable-governance regressions and production external-trust CI gate remain the non-regression baseline.

## 13. Deferred Scope

After rc3 review, later work may evaluate whether the next highest-priority need is a trace schema, source-aware trace validator, generated navigation, resolver/context packaging or another gap.

rc3 does not pre-commit the next RC to any one of those directions.

Still deferred:

- trace JSON Schema;
- executable trace validator/generator;
- generated reverse index;
- authority/context resolver;
- project applicability inference;
- automatic Pattern selection;
- new L3 work;
- M3/M4;
- L4 guidance;
- code generation;
- additional CI/trust capability.

## 14. Acceptance Target

The rc3 serialization is acceptable only if independent review confirms that:

1. all 119 records are reconstructible from frozen authoritative metadata;
2. relation classes and source fields are exact;
3. all relation triples are unique and canonically ordered;
4. all 82 L2 IDs resolve to accepted frozen authority identities;
5. all material qualifier associations are preserved correctly;
6. no relation is invented from narrative prose;
7. no frozen authoritative relation is omitted;
8. `authority-registry.yaml` remains separate and unchanged;
9. serialization does not imply applicability, selection, satisfaction, compliance, verification or closure;
10. frozen/control identities and existing executable regressions remain intact.
