# SCAF L3 Pattern / Mechanism Catalog

**Development Release:** v0.0.3rc13  
**Upstream Baseline:** frozen v0.0.2 L1/L2  
**Framework Plane:** `SCAF-PROF`  
**Status:** freeze-candidate release-record cleanup; twelve published entries Available/M2

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

## 2. v0.0.3rc13 Scope

The independent v0.0.3rc12 freeze-candidate review returned:

```text
L3 V0.0.3 FREEZE-CANDIDATE GATE: YES, AFTER MINOR CLEANUP
```

It found no architecture, trace, lifecycle or deferred-scope blocker. All twelve Pattern entries were judged valid for the proposed v0.0.3 freeze baseline. The only finding, `R12-01`, is a Minor release-record consistency defect.

v0.0.3rc13 performs the required release-record cleanup only. It synchronizes current release/navigation/gate wording, uses release-stable CI wording, and removes stale point-release wording from the living metadata contract. It adds no Pattern, changes no Pattern lifecycle state, changes no L2 trace relation, and does not modify frozen normative content.

A focused independent closure review shall determine whether `R12-01` is fully resolved and whether the current tree is eligible for a later explicit v0.0.3 freeze action. rc13 itself remains an RC.

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
| `catalog/<FAMILY>/` | Published L3 pattern entries by immutable primary family |
| `templates/L3_Pattern_Template.md` | Controlled authoring template for later entries |

## 4. Frozen-Upstream Rule

The complete `docs/normative/` tree remains the frozen v0.0.2 L1/L2 baseline in this development repository. L3 work shall not modify those frozen files in place.

If L3 work exposes a genuine architecture-level contradiction in the frozen baseline, that issue must be raised explicitly as a separate governance event. It must not be repaired indirectly through L3 wording.

## 5. Current Gate / Closed Work

The immediate gate is an independent **v0.0.3rc13 freeze-candidate release-record closure review**.

The review must verify at minimum:

- rc12 finding `R12-01` is fully resolved;
- root README current release/gate/sequence/CI wording is mutually consistent and release-stable;
- the living metadata contract no longer contains stale rc06 point-release wording for the intentionally deferred executable-governance items;
- frozen v0.0.2 remains byte-stable at 294 / 218 / 76;
- exactly twelve published Pattern identities exist and all remain `Available / M2`;
- all IDs, immutable primary families, `Introduced In` history and `Supersedes` state remain stable;
- rc12→rc13 Pattern bodies are non-regressed except current Development Release metadata;
- the rc09 `FTL-001` `SCAF-ROB-007` Constraint Input closure remains intact;
- no new architecture/trace/lifecycle scope is introduced.

A successful rc13 closure review may authorize a **later explicit freeze action** for v0.0.3. It does not itself freeze the release.

The following remain outside v0.0.3rc13:

- third-tranche/bulk catalog expansion;
- the approved-but-deferred EVD export/transformation Pattern;
- rejected/reframe PST configuration-activation authoring;
- SEC-primary Pattern authoring;
- M3/M4;
- L4;
- schema, validator, generated registry/reverse index, CI, code generation or executable governance.
