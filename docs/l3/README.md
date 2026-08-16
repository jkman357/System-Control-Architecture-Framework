# SCAF L3 Pattern / Mechanism Catalog

**Development Release:** v0.0.3rc12  
**Upstream Baseline:** frozen v0.0.2 L1/L2  
**Framework Plane:** `SCAF-PROF`  
**Status:** milestone consolidation / freeze-candidate audit; twelve published entries Available/M2

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

## 2. v0.0.3rc12 Scope

The independent v0.0.3rc11 availability-acceptance review returned:

```text
L3 SECOND-TRANCHE PATTERN-AVAILABILITY ACCEPTANCE GATE: YES
```

It verified all twelve published entries as `Available / M2`, reproduced all twelve controlled non-regression hashes, preserved the frozen v0.0.2 baseline and opened no finding.

v0.0.3rc12 does not add or promote any Pattern. It consolidates the evidence from the complete v0.0.3 L3 development line and prepares an explicit freeze-candidate audit. The audit is intended to answer whether the current L3 contracts and twelve-entry catalog may be frozen as a stable baseline in a later explicit governance action.

The proposed freeze scope is deliberately bounded to the L3 catalog governance/metadata/trace contracts and the twelve current `Available / M2` Pattern entries. It does not include M3/M4, L4 implementation/verification guidance, future Pattern categories or executable governance.

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
| `catalog/<FAMILY>/` | Published L3 pattern entries by immutable primary family |
| `templates/L3_Pattern_Template.md` | Controlled authoring template for later entries |

## 4. Frozen-Upstream Rule

The complete `docs/normative/` tree remains the frozen v0.0.2 L1/L2 baseline in this development repository. L3 work shall not modify those frozen files in place.

If L3 work exposes a genuine architecture-level contradiction in the frozen baseline, that issue must be raised explicitly as a separate governance event. It must not be repaired indirectly through L3 wording.

## 5. Current Gate / Closed Work

The immediate gate is an independent **v0.0.3 L3 milestone-consolidation / freeze-candidate audit**.

The review must verify at minimum:

- frozen v0.0.2 remains byte-stable at 294 / 218 / 76;
- exactly twelve published Pattern identities exist and all remain `Available / M2`;
- all IDs, immutable primary families, `Introduced In` history and `Supersedes` state remain stable;
- rc11→rc12 Pattern bodies are non-regressed except current Development Release metadata;
- the governance, metadata and trace/selection contracts are internally consistent and have been exercised successfully by both tranches;
- all material findings from the v0.0.3 line are closed;
- `Available` and M2 retain their bounded meanings and do not become project selection/compliance/satisfaction authority;
- deferred EVD, PST reframe, SEC-primary, M3/M4, L4 and executable-governance work are cleanly outside the proposed frozen scope rather than unresolved baseline contradictions;
- no release-record inconsistency or hidden scope expansion prevents a freeze candidate.

A successful rc12 review may authorize a **later explicit freeze action** for v0.0.3. It does not itself freeze the release.

The following remain outside v0.0.3rc12:

- third-tranche/bulk catalog expansion;
- the approved-but-deferred EVD export/transformation Pattern;
- rejected/reframe PST configuration-activation authoring;
- SEC-primary Pattern authoring;
- M3/M4;
- L4;
- schema, validator, generated registry/reverse index, CI, code generation or executable governance.
