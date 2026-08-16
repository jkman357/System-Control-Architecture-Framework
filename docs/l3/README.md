# SCAF L3 Pattern / Mechanism Catalog

**Development Release:** v0.0.3rc02  
**Upstream Baseline:** frozen v0.0.2 L1/L2  
**Framework Plane:** `SCAF-PROF`  
**Status:** L3 architecture / catalog-contract RC; no pattern instances yet

## 1. Purpose

This directory begins the controlled L3 Pattern / Mechanism Catalog development line for System Control Architecture Framework (SCAF).

L3 provides reusable **candidate realization mechanisms** that may help a project realize one or more applicable frozen L2 obligations. L3 does not reopen the frozen v0.0.2 taxonomy, core metamodel, authority homes, requirement IDs or requirement semantics.

The canonical relationship is:

```text
Frozen L1/L2 concern obligations
        ↓
L3 candidate Pattern / Mechanism Catalog (`SCAF-PROF`)
        ↓
Project Design Authority evaluates / selects / adapts / rejects
        ↓
Controlled project decision
        ↓
Project Realization implements
        ↓
Project Verification / Assurance evaluates project evidence
```

Pattern selection by itself does not satisfy an L2 obligation.

## 2. v0.0.3rc02 Scope

v0.0.3rc02 is a localized contract-cleanup release responding to the independent rc01 review. It does not allocate pattern identities or expand catalog content.

This RC establishes only the L3 architecture and catalog contract:

- L3 scope and authority boundary;
- mechanism-family taxonomy;
- stable pattern-ID rule;
- pattern metadata contract;
- many-to-many L2-to-L3 trace semantics;
- project selection semantics;
- catalog status and maturity semantics;
- composition / alternative / conflict relations;
- L3 / L4 boundary;
- initial pattern-family priority.

This RC intentionally contains **no `SCAF-PAT-*` pattern instances**. Representative patterns are deferred until this contract passes independent architecture review.

## 3. Files

| File | Purpose |
|---|---|
| `00_L3_Catalog_Governance.md` | L3 authority, taxonomy, ID, lifecycle and L3/L4 boundaries |
| `01_L3_Pattern_Metadata_Contract.md` | Required pattern-entry metadata and field semantics |
| `02_L3_Trace_and_Selection_Model.md` | L2→L3 trace relations, project selection states and satisfaction boundary |
| `03_L3_Pattern_Index.md` | Human-readable catalog index and initial family backlog; not a trace authority |
| `catalog/README.md` | Mechanism-family definitions and future placement rules |
| `templates/L3_Pattern_Template.md` | Controlled authoring template for later `SCAF-PAT-*` entries |

## 4. Frozen-Upstream Rule

The complete `docs/normative/` tree remains the frozen v0.0.2 L1/L2 baseline in this development repository. L3 work shall not modify those frozen files in place.

If future L3 work exposes a genuine architecture-level contradiction in the frozen baseline, that issue must be raised explicitly as a separate governance event. It must not be repaired indirectly through L3 wording.

## 5. Closed Gates

The following remain outside v0.0.3rc02:

- L4 implementation guidance;
- L4 verification procedures or test cases;
- machine-readable pattern schema;
- authority registry;
- validator;
- generated reverse-trace index;
- CI enforcement;
- code generation;
- bulk pattern authoring.
