# SCAF v0.0.4rc03 — Initial Authority Registry Serialization

**Development Release:** v0.0.4rc03  
**Status:** Initial 294-record authority-registry serialization RC  
**Upstream Baselines:** frozen v0.0.2 L1/L2; frozen v0.0.3 L3  
**Upstream Gate:** `V0.0.4 AUTHORITY-MODEL DETERMINISM CLOSURE GATE: YES`

## 1. Purpose

This RC performs the first machine-readable serialization authorized by the accepted v0.0.4 authority model and its rc02 determinism closure.

The RC serializes exactly the frozen v0.0.2 L1/L2 normative authority inventory into the repository-root `authority-registry.yaml` file. The registry is a subordinate controlled representation/index. It does not replace, override, amend, reinterpret, or complete the frozen normative Markdown under `docs/normative/`.

No schema, validator, generator, generated reverse index, CI enforcement, project applicability inference, L3 expansion, M3/M4, or L4 work is introduced here.

## 2. Serialization Artifact and Format Decision

The initial machine-readable artifact is:

```text
authority-registry.yaml
```

The concrete rc03 representation uses YAML with one top-level mapping key:

```yaml
records:
  - id: SCAF-AK-001
    record_kind: normative_requirement
    layer: l1_l2_normative_authority
    authority_class: Project-Applicable Obligation
    source_path: docs/normative/00_SCAF_Authority_Kernel.md
    source_anchor: SCAF-AK-001
    source_release: v0.0.2
    representation_release: v0.0.4rc03
    status: represented
    relations: []
```

This is a serialization choice, not a new normative authority layer. The first population deliberately uses only the ten fields already authorized by the accepted authority model. No title, concern, inferred layer, project state, derived cross-reference, Pattern selection, verification state, closure state, or convenience classification is added.

Record ordering is non-authoritative. Stable identity is the `id`, not sequence position.

## 3. Controlled Curated Representation Ownership

For rc03, `authority-registry.yaml` is a **controlled curated representation artifact** owned by the SCAF framework repository release state.

That means:

1. the canonical semantic source remains the frozen normative Markdown under `docs/normative/`;
2. the registry is reviewed and version-controlled with the SCAF release state;
3. a registry edit cannot create or change source authority semantics;
4. any source/registry mismatch is a representation defect and must not be resolved by preferring the registry;
5. no generator is claimed or included in rc03;
6. later generation or hybrid ownership requires a separately reviewed executable-governance change.

The registry must be reproducible in the audit sense: an independent reviewer can reconstruct the expected record population from the frozen source requirement headings, exact `Target` values, source file paths, and the deterministic constants defined by the rc02 authority model.

## 4. Initial Population Contract

The rc03 population shall contain exactly:

```text
294 unique authority records
218 Project-Applicable Obligations
76 Framework Normative Invariants
0 SCAF-PAT-* records
```

Every record shall use:

```text
record_kind            = normative_requirement
layer                  = l1_l2_normative_authority
source_anchor          = id
source_release         = v0.0.2
representation_release = v0.0.4rc03
status                 = represented
relations              = []
```

`authority_class` shall reproduce the exact frozen source `Target` value. `source_path` shall identify the canonical repository-relative normative Markdown file containing the requirement block.

For every record, `source_anchor == id` must resolve inside `source_path` to exactly one canonical requirement heading/block with that exact ID. Raw textual references elsewhere in prose are not authority anchors.

## 5. Completeness Claim Under Review

rc03 makes the controlled claim that the initial registry serialization is complete **subject to independent review**.

The review must establish all of the following before that claim is accepted:

1. exactly 294 records exist and all IDs are unique;
2. every frozen v0.0.2 normative requirement appears exactly once;
3. the exact 218 / 76 authority-class split is reproduced from source `Target` values;
4. every `source_path` exists and every `source_anchor` resolves exactly once as the canonical requirement heading/block;
5. every `source_anchor` equals its record `id`;
6. every record uses the accepted deterministic constants;
7. every `relations` value is empty;
8. no `SCAF-PAT-*` identity is serialized as normative authority;
9. no project-owned applicability, PDA, realization, verification, evidence, deviation, risk-acceptance, closure, or Pattern-selection state is introduced;
10. the frozen `docs/normative/` and `docs/l3/` trees remain unchanged.

## 6. Preserved Authority Boundaries

This serialization does not change:

- frozen v0.0.2 normative requirement semantics, identities, Target classes, or source precedence;
- frozen v0.0.3 L3 Pattern bodies, identities, lifecycle state, maturity, or trace semantics;
- the authority-model rule that Markdown is semantic authority and machine-readable data is subordinate representation;
- the two-class authority model;
- project Applicability / Project Design Authority / Project Realization / Project Verification / evidence / closure ownership;
- the exclusion of all `SCAF-PAT-*` identities from the L1/L2 normative authority population;
- the rule that non-empty machine-readable relations require a separate reviewed contract.

## 7. Deliberately Not Included

rc03 does not add or claim:

- JSON Schema or another machine-readable schema;
- validator implementation or fixtures;
- generator or hybrid registry ownership;
- generated reverse indexes;
- CI enforcement;
- code generation;
- automatic project applicability inference;
- machine-readable L2→L3 relations;
- new L3 Patterns / third tranche;
- SEC-primary realization;
- M3/M4;
- L4.

## 8. Serialization Gate

Independent review shall determine whether the initial 294-record serialization is complete, source-faithful, non-authority-expanding, and safe to use as the input for a later schema/structural-validator RC.

Expected decision:

```text
V0.0.4 INITIAL AUTHORITY-REGISTRY SERIALIZATION GATE: YES / YES, AFTER MINOR CLEANUP / NO
```

A `YES` authorizes only the next separately controlled executable-governance step. It does not automatically authorize CI, code generation, project applicability inference, L3 expansion, M3/M4, or L4.
