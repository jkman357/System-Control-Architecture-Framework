# SCAF L3 Pattern / Mechanism Catalog

**Development Release:** v0.0.3  
**Upstream Baseline:** frozen v0.0.2 L1/L2  
**Framework Plane:** `SCAF-PROF`  
**Status:** Frozen v0.0.3 L3 baseline; twelve published entries Available/M2

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

## 2. v0.0.3 Frozen Scope

The independent v0.0.3rc14 final-navigation closure review returned:

```text
L3 V0.0.3 FREEZE-CANDIDATE CLOSURE GATE: YES
```

It confirmed `R12-01` resolved, zero Critical/Major/Minor/Trivial findings, byte-stable frozen v0.0.2 upstream content, exactly twelve `Available / M2` Pattern identities, 12 / 12 Pattern-body non-regression, preservation of the `FTL-001` trace closure, mutually consistent current navigation, and no separately gated scope expansion.

By explicit governance decision, v0.0.3 is now the **Frozen L3 Pattern / Mechanism Catalog Baseline**. The freeze changes release/freeze state and current-release metadata only; it introduces no intended Pattern architecture, trace, authority or lifecycle semantic change from the reviewed rc14 tree.

Frozen catalog state:

- twelve published Pattern identities;
- all twelve `Available / M2 — Architecture Reviewed`;
- initial seven retain `Introduced In: v0.0.3rc03`;
- second five retain `Introduced In: v0.0.3rc08`;
- all primary families remain immutable and all `Supersedes` relations remain `None`.

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
| `11_L3_v0.0.3_Milestone_Consolidation_and_Freeze_Candidate.md` | rc12 milestone evidence consolidation, proposed freeze scope and freeze-candidate criteria |
| `12_L3_v0.0.3_Freeze_Candidate_Release_Record_Cleanup.md` | rc13 focused `R12-01` release-record cleanup and closure-gate record |
| `13_L3_v0.0.3_Freeze_Candidate_Final_Navigation_Cleanup.md` | rc14 final Pattern Index navigation cleanup and focused freeze-candidate closure record |
| `14_L3_v0.0.3_Freeze_Decision.md` | Formal v0.0.3 L3 freeze decision, frozen scope and post-freeze governance boundary |
| `catalog/<FAMILY>/` | Published L3 pattern entries by immutable primary family |
| `templates/L3_Pattern_Template.md` | Controlled authoring template for later entries |

## 4. Frozen-Upstream Rule

The complete `docs/normative/` tree remains the frozen v0.0.2 L1/L2 baseline in this development repository. L3 work shall not modify those frozen files in place.

If L3 work exposes a genuine architecture-level contradiction in the frozen baseline, that issue must be raised explicitly as a separate governance event. It must not be repaired indirectly through L3 wording.

## 5. Frozen Governance State

The v0.0.3 L3 freeze-candidate gate is closed. The reviewed rc14 tree was explicitly frozen as v0.0.3 after the independent closure review returned `L3 V0.0.3 FREEZE-CANDIDATE CLOSURE GATE: YES` with `R12-01` resolved and no new/regression findings.

The frozen v0.0.3 baseline shall not be modified in place.

The following remain outside this frozen baseline and require a later separately controlled development line:

- third-tranche/bulk catalog expansion;
- the approved-but-deferred EVD export/transformation Pattern;
- rejected/reframe PST configuration-activation authoring;
- SEC-primary Pattern authoring;
- M3/M4;
- L4;
- schema, validator, generated registry/reverse index, CI, code generation or executable governance.
