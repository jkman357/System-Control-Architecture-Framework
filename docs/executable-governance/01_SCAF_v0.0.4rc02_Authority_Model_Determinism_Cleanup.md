# SCAF v0.0.4rc02 — Authority Model Determinism Cleanup

**Development Release:** v0.0.4rc02  
**Status:** Focused closure RC  
**Upstream Baselines:** frozen v0.0.2 L1/L2; frozen v0.0.3 L3  
**Upstream Review:** v0.0.4rc01 Authority-Model Foundation Review  
**Blocking Finding Addressed:** `R1-01` — Minor

## 1. Purpose

This RC closes the single blocking semantic-determinism finding from the independent v0.0.4rc01 authority-model foundation review before any bulk machine-readable registry serialization is attempted.

The upstream review accepted the authority/source precedence, identity model, two-class authority boundary, project-authority boundary, L3 boundary, completeness model and fail-closed direction. It required only deterministic initial semantics for three mandatory future-record fields: `status`, `layer` and `source_anchor`.

This RC does not serialize the 294 records.

## 2. R1-01 Closure Decisions

### 2.1 `layer`

The first 294 records shall all use exactly:

```text
l1_l2_normative_authority
```

The value is a representation-domain label for the combined frozen L1/L2 normative authority population. No tool may infer per-record `L1`/`L2` classification from source location, prose or heuristics.

### 2.2 `source_anchor`

For each initial record:

```text
source_anchor == id
```

The resolver must locate exactly one requirement heading/block carrying that exact requirement ID inside the declared canonical `source_path`. Zero matches or multiple matches are fail-closed defects. Renderer-generated Markdown slugs, line numbers and generated index positions are not canonical anchors.

### 2.3 `status`

The only initial record status is:

```text
represented
```

This is representation-only state: the record exists in the machine-readable representation. It carries no source lifecycle, project applicability, compliance, realization, verification, closure, maturity, availability or Pattern-selection meaning.

### 2.4 `relations`

The rc01 review also recommended keeping initial `relations` empty/omitted unless a separately reviewed relation vocabulary exists. rc02 makes that population rule explicit. No new relation semantics are introduced.

## 3. Preserved Authority Boundaries

This cleanup does not change:

- frozen v0.0.2 normative requirement semantics or identities;
- the 294 / 218 / 76 frozen inventory;
- frozen v0.0.3 L3 Pattern bodies, identities, `Available / M2` states or trace meanings;
- canonical normative Markdown precedence over machine-readable representation;
- the two frozen authority classes;
- project Applicability / PDA / realization / verification / evidence / closure ownership;
- the exclusion of all `SCAF-PAT-*` identities from the initial normative authority-record population.

## 4. Deliberately Not Included

rc02 does not add or claim:

- `authority-registry.yaml` or another 294-record serialization;
- JSON Schema or another schema language;
- validator implementation or fixtures;
- generated registry/reverse index;
- CI enforcement;
- code generation;
- automatic project applicability inference;
- new L3 Patterns or third-tranche expansion;
- SEC-primary realization;
- M3/M4;
- L4.

## 5. Closure Gate

Independent review shall verify that `R1-01` is fully resolved without reopening frozen upstream semantics or pulling deferred executable-governance work into rc02.

Expected decision:

```text
V0.0.4 AUTHORITY-MODEL DETERMINISM CLOSURE GATE: YES / YES, AFTER MINOR CLEANUP / NO
```

A `YES` permits only the next controlled step: serialization of the initial 294-record frozen L1/L2 authority registry under the accepted authority model.
