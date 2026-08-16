# SCAF L3 Pattern / Mechanism Catalog

**Development Release:** v0.0.3rc09  
**Upstream Baseline:** frozen v0.0.2 L1/L2  
**Framework Plane:** `SCAF-PROF`  
**Status:** focused second-tranche trace cleanup; initial seven remain Available/M2; five second-tranche entries remain Candidate/M1

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

## 2. v0.0.3rc09 Scope

The independent v0.0.3rc08 second-tranche Pattern review returned:

```text
L3 SECOND-TRANCHE PATTERN GATE: YES, AFTER MINOR CLEANUP
```

It found 0 Critical, 0 Major and one localized Minor finding, `R8-01`, in `SCAF-PAT-FTL-001`. The other four rc08 entries passed without finding.

v0.0.3rc09 performs only the required relation-classification cleanup:

- `SCAF-ROB-007` moves from `Supporting L2 Trace` to `Constraint Inputs` in `SCAF-PAT-FTL-001`;
- §5.2/§5.3 now make the project-identified failure-propagation path an upstream input that constrains containment placement/configuration;
- `SCAF-ROB-015` remains Supporting Realization.

All twelve published Pattern identities and immutable primary families remain unchanged. The initial seven remain `Available / M2`; all five second-tranche entries remain `Candidate / M1` and `Introduced In: v0.0.3rc08`.

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
| `08_L3_Second_Tranche_Trace_Cleanup.md` | rc09 localized `R8-01` trace-cleanup decision and focused closure boundary |
| `catalog/<FAMILY>/` | Published L3 pattern entries by immutable primary family |
| `templates/L3_Pattern_Template.md` | Controlled authoring template for later entries |

## 4. Frozen-Upstream Rule

The complete `docs/normative/` tree remains the frozen v0.0.2 L1/L2 baseline in this development repository. L3 work shall not modify those frozen files in place.

If L3 work exposes a genuine architecture-level contradiction in the frozen baseline, that issue must be raised explicitly as a separate governance event. It must not be repaired indirectly through L3 wording.

## 5. Current Gate / Closed Work

The immediate gate is an independent **rc09 focused trace-closure review**. The review must verify:

- `R8-01` is fully Resolved in `SCAF-PAT-FTL-001`;
- `SCAF-ROB-007` is a Constraint Input and no longer a Supporting Realization;
- `SCAF-ROB-015` remains the intended Supporting trace;
- the `FTL-001` ID/family/Candidate/M1/Introduced-In state remains stable;
- the other eleven Pattern architecture bodies are non-regressed except current Development Release metadata;
- the frozen v0.0.2 normative baseline remains byte-stable.

The following remain outside v0.0.3rc09:

- M2 or `Available` promotion of the five second-tranche entries;
- authoring of the rc07-approved but deferred EVD export/transformation category;
- the rejected/reframe PST configuration-activation candidate;
- SEC-primary Pattern authoring without the dedicated security-realization gate;
- third-tranche or bulk catalog expansion;
- M3/M4 maturity claims;
- L4 implementation or verification guidance;
- schema, authority registry, validator, generated reverse-trace index, CI, code generation or executable governance.
