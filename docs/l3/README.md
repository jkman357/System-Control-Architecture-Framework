# SCAF L3 Pattern / Mechanism Catalog

**Development Release:** v0.0.3rc10  
**Upstream Baseline:** frozen v0.0.2 L1/L2  
**Framework Plane:** `SCAF-PROF`  
**Status:** second-tranche lifecycle decision; initial seven Available/M2; five second-tranche entries Candidate/M2

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

## 2. v0.0.3rc10 Scope

The independent v0.0.3rc09 focused trace-closure review returned:

```text
L3 SECOND-TRANCHE TRACE-CLOSURE GATE: YES
```

It confirmed `R8-01` Resolved, found no new regression finding and permitted a later maturity/readiness review for the five second-tranche entries.

v0.0.3rc10 therefore records their deliberate advancement to `M2 — Architecture Reviewed` while retaining `Catalog Status: Candidate`. The initial seven remain `Available / M2`.

No Pattern mechanism/trace body is re-authored for this lifecycle move. The rc10 review must separately validate M2 and availability readiness entry by entry.

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
| `09_L3_Second_Tranche_Lifecycle_Decision.md` | rc10 M2 maturity decision and separate availability-readiness gate |
| `catalog/<FAMILY>/` | Published L3 pattern entries by immutable primary family |
| `templates/L3_Pattern_Template.md` | Controlled authoring template for later entries |

## 4. Frozen-Upstream Rule

The complete `docs/normative/` tree remains the frozen v0.0.2 L1/L2 baseline in this development repository. L3 work shall not modify those frozen files in place.

If L3 work exposes a genuine architecture-level contradiction in the frozen baseline, that issue must be raised explicitly as a separate governance event. It must not be repaired indirectly through L3 wording.

## 5. Current Gate / Closed Work

The immediate gate is an independent **rc10 second-tranche maturity / availability-readiness review**. For each of `FTL-001`, `FTL-002`, `TIM-001`, `TIM-002` and `SYN-001`, review must separately determine M2 validity and later availability readiness.

The review must also reconfirm:

- the initial seven remain `Available / M2` and non-regressed;
- exactly twelve published IDs remain;
- `FTL-001` continues to treat `SCAF-ROB-007` as a Constraint Input;
- the frozen v0.0.2 normative baseline remains byte-stable;
- M2 does not imply `Available`, project selection, recommendation, compliance or L2 satisfaction.

The following remain outside v0.0.3rc10:

- Candidate→Available transition for the five second-tranche entries;
- deferred EVD export/transformation authoring;
- rejected/reframe PST configuration-activation authoring;
- SEC-primary Pattern authoring;
- third-tranche/bulk expansion;
- M3/M4, L4, schema, validator, generated registry/index, CI, code generation or executable governance.
