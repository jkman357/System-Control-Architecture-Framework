# SCAF L3 Pattern / Mechanism Catalog

**Development Release:** v0.0.3rc06  
**Upstream Baseline:** frozen v0.0.2 L1/L2  
**Framework Plane:** `SCAF-PROF`  
**Status:** Initial representative L3 pattern availability-acceptance RC; all seven entries Available / M2

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


## 2. v0.0.3rc06 Scope

The independent v0.0.3rc05 maturity / availability review returned `INITIAL L3 PATTERN-LIFECYCLE GATE: YES`, validated **7 / 7 `M2 VALID`**, independently judged **7 / 7 `READY FOR AVAILABLE`**, and opened no new Critical, Major, Minor or Trivial finding.

v0.0.3rc06 therefore records the explicit catalog-maintainer acceptance decision for the same seven published entries:

```text
Candidate -> Available
M2 — Architecture Reviewed remains unchanged
Introduced In: v0.0.3rc03 remains unchanged
```

The pattern mechanism bodies, authority boundaries and L2 trace semantics are not re-authored to obtain availability. This RC is intentionally limited to:

- recording the entry-by-entry availability acceptance decision and its review evidence basis;
- updating all seven pattern Catalog Status values from Candidate to Available;
- preserving M2 maturity, stable identity/family and original introduction history;
- updating current release/index/navigation/gate wording.

`Available` means accepted for project consideration under the current catalog release. It does not imply project applicability, recommendation, selection, compliance, verification, implementation correctness or L2 satisfaction.

## 3. Files

| File / Path | Purpose |
|---|---|
| `00_L3_Catalog_Governance.md` | L3 authority, taxonomy, ID, lifecycle and L3/L4 boundaries |
| `01_L3_Pattern_Metadata_Contract.md` | Required pattern-entry metadata and field semantics |
| `02_L3_Trace_and_Selection_Model.md` | L2→L3 trace relations, project selection states and satisfaction boundary |
| `03_L3_Pattern_Index.md` | Human-readable catalog index; not a trace authority |
| `04_L3_Initial_Tranche_Lifecycle_Decision.md` | Historical rc05 M2 decision record and availability-readiness gate |
| `05_L3_Initial_Tranche_Availability_Acceptance.md` | rc06 explicit entry-by-entry Candidate→Available catalog acceptance record |
| `catalog/<FAMILY>/` | Published L3 pattern entries by immutable primary family |
| `templates/L3_Pattern_Template.md` | Controlled authoring template for later entries |

## 4. Frozen-Upstream Rule

The complete `docs/normative/` tree remains the frozen v0.0.2 L1/L2 baseline in this development repository. L3 work shall not modify those frozen files in place.

If L3 work exposes a genuine architecture-level contradiction in the frozen baseline, that issue must be raised explicitly as a separate governance event. It must not be repaired indirectly through L3 wording.


## 5. Closed Gates

The following remain outside v0.0.3rc06:

- automatic project selection or L2 satisfaction inferred from `Available` status;
- uncontrolled/bulk second-tranche pattern expansion;
- M3 / M4 maturity claims without their separate evidence gates;
- L4 implementation guidance;
- L4 verification procedures or test cases;
- machine-readable pattern schema;
- authority registry;
- validator;
- generated reverse-trace index;
- CI enforcement;
- code generation;
- other executable-governance work.
