# SCAF L3 Pattern / Mechanism Catalog

**Development Release:** v0.0.3rc05  
**Upstream Baseline:** frozen v0.0.2 L1/L2  
**Framework Plane:** `SCAF-PROF`  
**Status:** Initial representative L3 pattern maturity-decision RC; all entries Candidate / M2

## 1. Purpose

This directory contains the controlled L3 Pattern / Mechanism Catalog development line for System Control Architecture Framework (SCAF).

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

## 2. v0.0.3rc05 Scope

The independent v0.0.3rc04 focused trace-closure review returned `INITIAL L3 PATTERN-TRANCHE TRACE-CLOSURE GATE: YES`, confirmed `R3-01` through `R3-04` Resolved and found no new Critical, Major, Minor or Trivial finding.

v0.0.3rc05 therefore records the deliberate maturity decision that the same seven published entries now satisfy the catalog definition of `M2 — Architecture Reviewed`. All seven remain `Catalog Status: Candidate` while a separate availability-readiness review is performed.

No pattern body is re-authored merely to claim maturity. The rc05 content changes are limited to:

- recording the M2 lifecycle decision and its independent-review evidence basis;
- updating the seven pattern metadata maturity values from M1 to M2;
- defining the separate Candidate→Available acceptance gate;
- updating current release/index/navigation wording.

The rc05 review must validate M2 promotion independently and assess, entry by entry, whether later `Available` promotion would be justified. It must not infer project suitability, recommendation, compliance or L2 satisfaction from either M2 or future `Available` status.

## 3. Files

| File / Path | Purpose |
|---|---|
| `00_L3_Catalog_Governance.md` | L3 authority, taxonomy, ID, lifecycle and L3/L4 boundaries |
| `01_L3_Pattern_Metadata_Contract.md` | Required pattern-entry metadata and field semantics |
| `02_L3_Trace_and_Selection_Model.md` | L2→L3 trace relations, project selection states and satisfaction boundary |
| `03_L3_Pattern_Index.md` | Human-readable catalog index; not a trace authority |
| `04_L3_Initial_Tranche_Lifecycle_Decision.md` | Release-scoped M2 decision record and `Available` readiness gate |
| `catalog/<FAMILY>/` | Published L3 pattern entries by immutable primary family |
| `templates/L3_Pattern_Template.md` | Controlled authoring template for later entries |

## 4. Frozen-Upstream Rule

The complete `docs/normative/` tree remains the frozen v0.0.2 L1/L2 baseline in this development repository. L3 work shall not modify those frozen files in place.

If L3 work exposes a genuine architecture-level contradiction in the frozen baseline, that issue must be raised explicitly as a separate governance event. It must not be repaired indirectly through L3 wording.

## 5. Closed Gates

The following remain outside v0.0.3rc05:

- Candidate→`Available` promotion before the rc05 maturity / availability-readiness review is accepted;
- bulk pattern expansion;
- L4 implementation guidance;
- L4 verification procedures or test cases;
- machine-readable pattern schema;
- authority registry;
- validator;
- generated reverse-trace index;
- CI enforcement;
- code generation;
- other executable-governance work.
