# SCAF Machine-Readable Authority Model

**Development Release:** v0.0.4rc01  
**Status:** Foundation RC; machine-readable serialization not yet authorized  
**Upstream Baselines:** frozen v0.0.2 L1/L2; frozen v0.0.3 L3  
**Initial Registry Population:** frozen v0.0.2 L1/L2 normative requirement identities only

## 1. Purpose

This document defines the semantic contract that a later machine-readable SCAF authority registry must preserve.

The purpose of the registry is to make stable framework authority identities, classification and source location resolvable by tools without requiring every tool to reconstruct those facts from prose. The registry is a controlled machine-readable representation and index. It is **not** a second normative source and does not gain authority merely because a validator, generator, CI job or AI consumes it.

This RC establishes the model before serialization so that implementation convenience cannot silently redefine SCAF authority semantics.

## 2. Frozen Upstream Boundary

The initial registry population shall represent the frozen v0.0.2 L1/L2 normative inventory:

```text
294 unique normative requirement IDs
218 Project-Applicable Obligations
76 Framework Normative Invariants
```

The source semantics remain the frozen Markdown documents under `docs/normative/`.

The frozen v0.0.3 L3 catalog remains downstream architecture knowledge. Its twelve `SCAF-PAT-*` Pattern identities are **not** part of the initial authority-record population and shall not be reclassified as normative requirements by the registry.

A later separately gated extension may introduce machine-readable Pattern metadata or cross-layer reverse indexes, but those records must preserve the L2→L3 authority boundary and bounded `Available` semantics defined by the frozen L3 baseline.

## 3. Canonical Source-of-Truth Rule

For v0.0.4 development, the canonical direction is:

```text
frozen normative Markdown
        │
        │ defines semantic authority
        v
machine-readable authority representation
        │
        ├─ schema validation
        ├─ reference resolution
        ├─ generated indexes/views
        └─ later CI / tool consumption
```

A machine-readable record shall never override, amend, reinterpret or complete missing normative semantics in its source requirement.

If a record conflicts with its frozen normative source, the record is invalid. The correct response is to fail validation or block generation/enforcement based on the inconsistent representation; the tool shall not choose the registry value over the normative source.

If a source requirement cannot be represented without semantic invention, the representation shall remain incomplete/blocked and the issue shall be resolved through a separately controlled framework change. Tooling shall not guess.

## 4. Authority Record Identity

One initial authority record corresponds to exactly one frozen L1/L2 normative requirement ID.

The stable identity key is the existing requirement ID, for example:

```text
SCAF-AK-001
SCAF-CTX-001
SCAF-ROB-015
```

The registry shall not mint replacement IDs for existing frozen requirements.

Within one registry population:

- every represented authority ID shall be unique;
- duplicate records for one authority ID are invalid;
- aliases shall not create a second authority identity;
- a source-path move, generated index location or serializer key change shall not change requirement identity;
- a future supersession or retirement mechanism must be separately governed and shall not be inferred from file movement or absence.

## 5. Initial Authority Classes

The initial registry recognizes exactly the two normative Target classes already frozen by the Authority Kernel.

### 5.1 Project-Applicable Obligation

A record classified as `Project-Applicable Obligation` represents a frozen SCAF obligation that becomes project-applicable through SCAF Project Application / Framework Scan applicability semantics.

The registry records the framework classification. It does not decide that the obligation is Applicable to a particular project and does not become Project Design Authority, Project Verification / Assurance Authority or closure authority.

### 5.2 Framework Normative Invariant

A record classified as `Framework Normative Invariant` represents a frozen rule that constrains SCAF normative content, framework governance, migration/promotion behavior or authoring semantics.

It is not converted into a project architecture obligation by being present in a machine-readable registry.

### 5.3 Classification Preservation

A future registry shall reproduce each requirement's frozen `Target` classification exactly. Any mismatch between registry classification and the source requirement is a validation error.

No third authority class is introduced by v0.0.4rc01.

## 6. Required Semantic Fields for a Future Record

The following fields define the minimum semantic information that a later serialization must carry. The names below are conceptual field identifiers for the v0.0.4 line; concrete YAML/JSON syntax and schema mechanics are deferred to a later RC.

| Field | Cardinality | Semantic meaning |
|---|---:|---|
| `id` | exactly 1 | Existing stable frozen requirement ID |
| `record_kind` | exactly 1 | Initial value is `normative_requirement`; prevents Pattern/catalog records from being confused with normative authority |
| `layer` | exactly 1 | Source authority layer; initial population is L1/L2 normative authority |
| `authority_class` | exactly 1 | Frozen Target class: `Project-Applicable Obligation` or `Framework Normative Invariant` |
| `source_path` | exactly 1 | Repository-relative path to the canonical normative Markdown source |
| `source_anchor` | exactly 1 | Stable resolvable source locator based on the requirement identity/heading, not an invented semantic alias |
| `source_release` | exactly 1 | Frozen baseline that owns the represented semantics; initial population is `v0.0.2` |
| `representation_release` | exactly 1 | RC/release whose machine-readable representation contains the record; this does not change source authority |
| `status` | exactly 1 | Representation lifecycle state defined by executable-governance rules; it shall not silently redefine source requirement status |
| `relations` | 0..n | Typed references whose relation semantics are separately defined and validated; no generic `satisfies` shortcut |

Additional fields may be added only when their semantics are explicit and do not duplicate project-owned applicability, decision, realization, evidence or closure state.

## 7. Fields the Initial Authority Registry Shall Not Own

The initial framework authority registry shall not contain project-specific values that would cause it to become a project governance database.

In particular it shall not own:

- project Applicability decisions;
- project consequence/risk disposition;
- Project Design Authority assignment for a concrete project decision;
- project design values;
- implementation/realization state;
- verification result or evidence sufficiency decision;
- project closure, deviation or risk-acceptance state;
- project selection of an L3 Pattern.

A later project-side application model may reference SCAF authority IDs, but that is a separate record/authority domain.

## 8. Relation Semantics Boundary

A future machine-readable registry may represent explicit framework relations only when their semantics are defined by SCAF and can be reproduced without inference.

The initial implementation shall prefer omission over invention. A relation shall not be synthesized merely because two requirements mention similar terms.

Where cross-layer L2→L3 trace is later represented, it must preserve the frozen L3 relation meanings such as Primary Realization Candidate, Supporting and Constraint Input. It shall not collapse those relations into `satisfies`, `implements`, `complies_with` or another stronger claim.

## 9. Representation Lifecycle and Staleness

Machine-readable authority data has a representation lifecycle distinct from the source authority lifecycle.

At minimum a future implementation must be able to distinguish:

- a source requirement that validly exists but is missing from the representation;
- a representation record whose source no longer resolves;
- a record whose classification or source locator conflicts with the source;
- a duplicate representation of one stable authority ID;
- a representation generated/curated for an older source baseline.

These states are representation defects. They do not silently delete, retire or change the underlying normative requirement.

## 10. Completeness Rule for the Initial Registry

When a later RC claims the **initial frozen L1/L2 authority registry is complete**, completeness means all of the following:

1. exactly 294 unique authority records resolve to the frozen v0.0.2 normative source tree;
2. exactly 218 are classified as `Project-Applicable Obligation`;
3. exactly 76 are classified as `Framework Normative Invariant`;
4. every record ID matches its source requirement ID;
5. every source requirement appears exactly once;
6. no `SCAF-PAT-*` identity is counted as one of the 294 authority records;
7. no machine-readable record changes the frozen source semantics.

Until a later RC both serializes and validates that population, v0.0.4rc01 makes no claim that such a registry exists.

## 11. Failure Policy

A future validator or consumer shall fail closed for authority-identity and source-consistency defects that make authority resolution ambiguous or incorrect.

Examples include:

- duplicate authority ID;
- unresolved canonical source;
- ID/source mismatch;
- authority-class/source mismatch;
- unsupported record kind presented as normative authority;
- incompatible registry/schema version where semantics cannot be safely interpreted.

Warnings may later be defined for non-authority metadata quality issues, but v0.0.4rc01 does not define validator severities.

## 12. Serialization Neutrality

v0.0.4rc01 does not authorize a normative YAML or JSON representation and does not choose a schema language.

The next serialization RC may choose a concrete format only if it can preserve this model without changing its authority semantics. Serializer convenience is subordinate to the model.

Likewise, the future registry may be curated, generated or hybrid only after the ownership and reproducibility rules for that mechanism are explicitly defined.

## 13. AI / Tool Consumption Boundary

An AI agent, validator, generator or CI job may use the future registry to determine what authority identities exist and where their canonical sources reside.

It shall not infer from registry presence alone that:

- every obligation is Applicable to the current project;
- an L3 Pattern must be selected;
- project evidence is sufficient;
- a project decision is closed;
- a requirement is satisfied;
- a machine-readable field overrides contradictory normative text.

The registry is intended to reduce context reconstruction ambiguity, not to erase authority boundaries.

## 14. v0.0.4rc01 Review Gate

Independent review shall answer whether this model is safe and precise enough to authorize a later RC to serialize the initial 294-record frozen L1/L2 registry.

The review shall specifically verify:

1. frozen v0.0.2 and v0.0.3 semantics are not reopened;
2. registry/representation authority is subordinate to canonical normative source semantics;
3. the two frozen Target classes are preserved without creating a third hidden authority class;
4. project applicability/PDA/realization/verification/evidence/closure state is not absorbed into the framework registry;
5. L3 Pattern identities remain downstream catalog identities, not normative authority records;
6. identity, completeness, stale/conflict and fail-closed rules are sufficient for later structural validation;
7. no schema, validator, CI, codegen or bulk catalog expansion is silently claimed by rc01.

Expected decision:

```text
V0.0.4 AUTHORITY-MODEL FOUNDATION GATE: YES / YES, AFTER MINOR CLEANUP / NO
```
