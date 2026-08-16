# SCAF L3 Pattern / Mechanism Catalog

**Development Release:** v0.0.3rc07  
**Upstream Baseline:** frozen v0.0.2 L1/L2  
**Framework Plane:** `SCAF-PROF`  
**Status:** L3 catalog coverage / second-tranche planning RC; seven existing entries remain Available / M2

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


## 2. v0.0.3rc07 Scope

The independent v0.0.3rc06 availability-acceptance review returned:

```text
INITIAL L3 PATTERN-AVAILABILITY ACCEPTANCE GATE: YES
```

It validated **7 / 7 `AVAILABLE ACCEPTANCE VALID`**, confirmed 7 / 7 pattern-body non-regression, and opened no Critical, Major, Minor or Trivial finding. The initial seven-pattern availability milestone is therefore closed.

v0.0.3rc07 does not author new patterns. It adds a controlled **trace-reference coverage audit and second-tranche planning decision surface** while preserving the current seven entries as `Available / M2`.

The audit distinguishes numeric trace-reference coverage from obligation satisfaction or catalog completeness and identifies a small set of candidate mechanism categories for independent review before any new Pattern ID is allocated.

## 3. Files

| File / Path | Purpose |
|---|---|
| `00_L3_Catalog_Governance.md` | L3 authority, taxonomy, ID, lifecycle and L3/L4 boundaries |
| `01_L3_Pattern_Metadata_Contract.md` | Required pattern-entry metadata and field semantics |
| `02_L3_Trace_and_Selection_Model.md` | L2→L3 trace relations, project selection states and satisfaction boundary |
| `03_L3_Pattern_Index.md` | Human-readable catalog index; not a trace authority |
| `04_L3_Initial_Tranche_Lifecycle_Decision.md` | Historical rc05 M2 decision record and availability-readiness gate |
| `05_L3_Initial_Tranche_Availability_Acceptance.md` | Historical rc06 explicit entry-by-entry Candidate→Available catalog acceptance record |
| `06_L3_Catalog_Coverage_and_Second_Tranche_Planning.md` | rc07 descriptive trace-reference coverage audit and controlled second-tranche candidate planning |
| `catalog/<FAMILY>/` | Published L3 pattern entries by immutable primary family |
| `templates/L3_Pattern_Template.md` | Controlled authoring template for later entries |

## 4. Frozen-Upstream Rule

The complete `docs/normative/` tree remains the frozen v0.0.2 L1/L2 baseline in this development repository. L3 work shall not modify those frozen files in place.

If L3 work exposes a genuine architecture-level contradiction in the frozen baseline, that issue must be raised explicitly as a separate governance event. It must not be repaired indirectly through L3 wording.


## 5. Closed Gates

The following remain outside v0.0.3rc07:

- automatic project selection or L2 satisfaction inferred from `Available` status;
- any second-tranche Pattern ID allocation before the rc07 planning gate passes;
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
