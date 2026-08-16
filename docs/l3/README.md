# SCAF L3 Pattern / Mechanism Catalog

**Development Release:** v0.0.3rc08  
**Upstream Baseline:** frozen v0.0.2 L1/L2  
**Framework Plane:** `SCAF-PROF`  
**Status:** controlled second representative Pattern tranche; initial seven remain Available/M2; five new entries are Candidate/M1

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

## 2. v0.0.3rc08 Scope

The independent v0.0.3rc07 coverage / second-tranche planning review returned:

```text
L3 SECOND-TRANCHE PLANNING GATE: YES
```

It found no Critical/Major/Minor/Trivial release finding and approved six candidate categories for later controlled authoring while rejecting/reframing the PST configuration-activation proposal.

v0.0.3rc08 deliberately authors **five** of the six approved categories to open the previously empty `FTL`, `TIM` and `SYN` families:

- `SCAF-PAT-FTL-001` — Failure-Domain Containment / Isolation;
- `SCAF-PAT-FTL-002` — Controlled Failover with Graceful Degradation;
- `SCAF-PAT-TIM-001` — Bounded Queue / Backpressure / Overload Protection;
- `SCAF-PAT-TIM-002` — Timebase / Clock-Relationship / Epoch Validity;
- `SCAF-PAT-SYN-001` — Generation/Epoch-Based Cross-Participant State Convergence.

All five are `Candidate / M1`. The first seven published entries remain `Available / M2` with unchanged architecture/trace content apart from the current Development Release field.

The rc07-approved EVD export/transformation category is intentionally deferred; no ID is allocated for the rejected/reframe PST candidate; SEC-primary realization remains separately gated.

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
| `07_L3_Second_Tranche_Authoring_Decision.md` | rc08 authoring scope, rc07 category dispositions and five new Pattern allocations |
| `catalog/<FAMILY>/` | Published L3 pattern entries by immutable primary family |
| `templates/L3_Pattern_Template.md` | Controlled authoring template for later entries |

## 4. Frozen-Upstream Rule

The complete `docs/normative/` tree remains the frozen v0.0.2 L1/L2 baseline in this development repository. L3 work shall not modify those frozen files in place.

If L3 work exposes a genuine architecture-level contradiction in the frozen baseline, that issue must be raised explicitly as a separate governance event. It must not be repaired indirectly through L3 wording.

## 5. Current Gate / Closed Work

The immediate gate is an independent review of the five new `Candidate / M1` entries. The review must preserve:

- the stable IDs/families/lifecycle states of the first seven `Available / M2` entries;
- the rc07 decision to keep FTL containment and failover as distinct Pattern intents;
- the TIM/ROB/INT authority partitions;
- the SYN/COM complementarity boundary;
- Project Design Authority and external-source authority;
- the L3/L4 boundary.

The following remain outside v0.0.3rc08:

- promotion of the five new entries to M2 or `Available` before review/closure;
- the deferred EVD export/transformation authoring unless separately opened later;
- the rejected/reframe PST configuration-activation candidate;
- SEC-primary Pattern authoring without the dedicated security-realization gate;
- uncontrolled/bulk catalog expansion;
- M3/M4 maturity claims;
- L4 implementation or verification guidance;
- schema, authority registry, validator, generated reverse-trace index, CI, code generation or executable governance.
