# SCAF L3 Pattern / Mechanism Catalog

**Development Release:** v0.0.3rc11  
**Upstream Baseline:** frozen v0.0.2 L1/L2  
**Framework Plane:** `SCAF-PROF`  
**Status:** second-tranche availability acceptance; all twelve published entries Available/M2

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

Pattern publication, availability or project selection by itself does not satisfy an L2 obligation.

## 2. v0.0.3rc11 Scope

The independent v0.0.3rc10 maturity / availability review returned:

```text
L3 SECOND-TRANCHE PATTERN-LIFECYCLE GATE: YES
```

It validated **5 / 5 M2**, judged **5 / 5 READY FOR AVAILABLE**, confirmed 12 / 12 controlled Pattern-body non-regression checks and found no new Critical/Major/Minor/Trivial issue.

v0.0.3rc11 therefore records the explicit `Candidate`→`Available` catalog acceptance for the five second-tranche entries. M2 maturity, IDs, primary families and `Introduced In: v0.0.3rc08` remain unchanged. The initial seven remain `Available / M2`.

No Pattern mechanism/trace body is re-authored for this lifecycle move. `Available` means accepted for project consideration under the current catalog release; it does not imply project applicability, recommendation, selection, compliance, verification, implementation correctness or L2 satisfaction.

## 3. Files

| File / Path | Purpose |
|---|---|
| `00_L3_Catalog_Governance.md` | L3 authority, taxonomy, ID, lifecycle and L3/L4 boundaries |
| `01_L3_Pattern_Metadata_Contract.md` | Required pattern-entry metadata and field semantics |
| `02_L3_Trace_and_Selection_Model.md` | L2→L3 trace relations, project selection states and satisfaction boundary |
| `03_L3_Pattern_Index.md` | Human-readable catalog index; not a trace authority |
| `04_L3_Initial_Tranche_Lifecycle_Decision.md` | Historical rc05 M2 decision record and availability-readiness gate |
| `05_L3_Initial_Tranche_Availability_Acceptance.md` | Historical rc06 Candidate→Available acceptance record |
| `06_L3_Catalog_Coverage_and_Second_Tranche_Planning.md` | Historical rc07 trace-reference coverage audit / second-tranche planning artifact |
| `07_L3_Second_Tranche_Authoring_Decision.md` | Historical rc08 authoring scope, rc07 category dispositions and five new Pattern allocations |
| `08_L3_Second_Tranche_Trace_Cleanup.md` | Historical rc09 localized `R8-01` trace-cleanup decision and focused closure boundary |
| `09_L3_Second_Tranche_Lifecycle_Decision.md` | Historical rc10 M2 maturity decision and availability-readiness gate |
| `10_L3_Second_Tranche_Availability_Acceptance.md` | rc11 explicit second-tranche Candidate→Available acceptance record |
| `catalog/<FAMILY>/` | Published L3 pattern entries by immutable primary family |
| `templates/L3_Pattern_Template.md` | Controlled authoring template for later entries |

## 4. Frozen-Upstream Rule

The complete `docs/normative/` tree remains the frozen v0.0.2 L1/L2 baseline in this development repository. L3 work shall not modify those frozen files in place.

If L3 work exposes a genuine architecture-level contradiction in the frozen baseline, that issue must be raised explicitly as a separate governance event. It must not be repaired indirectly through L3 wording.

## 5. Current Gate / Closed Work

The immediate gate is an independent **rc11 second-tranche availability-acceptance review**.

The review must reconfirm:

- all twelve published Patterns are `Available / M2` with stable IDs/families/history;
- the five second-tranche status transitions are directly supported by rc10 `READY FOR AVAILABLE` evidence;
- the transition did not rewrite mechanism architecture or L2 trace semantics;
- `FTL-001` retains `SCAF-ROB-007` as Constraint Input and `SCAF-ROB-015` as Supporting;
- the frozen v0.0.2 normative baseline remains byte-stable;
- `Available` does not imply project selection, recommendation, compliance, verification or L2 satisfaction.

The following remain outside v0.0.3rc11:

- the approved-but-deferred EVD export/transformation Pattern;
- rejected/reframe PST configuration-activation authoring;
- SEC-primary Pattern authoring;
- third-tranche/bulk expansion;
- M3/M4;
- L4;
- schema, validator, generated registry/reverse index, CI, code generation or executable governance.
