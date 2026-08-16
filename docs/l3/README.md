# SCAF L3 Pattern / Mechanism Catalog

**Development Release:** v0.0.3rc03  
**Upstream Baseline:** frozen v0.0.2 L1/L2  
**Framework Plane:** `SCAF-PROF`  
**Status:** Initial representative L3 pattern tranche; all entries Candidate / M1

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

## 2. v0.0.3rc03 Scope

The v0.0.3rc02 focused closure review returned `L3 CATALOG-CONTRACT CLOSURE GATE: YES`. v0.0.3rc03 therefore begins the first deliberately small representative pattern tranche.

This RC introduces seven permanent pattern identities, all with `Catalog Status: Candidate` and `Maturity: M1 — Structured`:

- `SCAF-PAT-SUP-001` — Heartbeat / Liveness Supervision;
- `SCAF-PAT-SUP-002` — Independent Watchdog with Escalation;
- `SCAF-PAT-REC-001` — Bounded Retry with Escalation;
- `SCAF-PAT-COM-001` — Reconnect plus State Reconciliation;
- `SCAF-PAT-PST-001` — Atomic Dual-Copy Persistent State;
- `SCAF-PAT-LCM-001` — Transactional Update with Rollback;
- `SCAF-PAT-EVD-001` — Pre/Post-Trigger Retained Incident Evidence Ring.

These entries are not yet `Available`. The tranche exists to stress-test the accepted taxonomy, metadata, trace, primary-family, composition, provenance and L3/L4 boundary rules before catalog expansion.

## 3. Files

| File / Path | Purpose |
|---|---|
| `00_L3_Catalog_Governance.md` | L3 authority, taxonomy, ID, lifecycle and L3/L4 boundaries |
| `01_L3_Pattern_Metadata_Contract.md` | Required pattern-entry metadata and field semantics |
| `02_L3_Trace_and_Selection_Model.md` | L2→L3 trace relations, project selection states and satisfaction boundary |
| `03_L3_Pattern_Index.md` | Human-readable catalog index; not a trace authority |
| `catalog/<FAMILY>/` | Published L3 pattern entries by immutable primary family |
| `templates/L3_Pattern_Template.md` | Controlled authoring template for later entries |

## 4. Frozen-Upstream Rule

The complete `docs/normative/` tree remains the frozen v0.0.2 L1/L2 baseline in this development repository. L3 work shall not modify those frozen files in place.

If L3 work exposes a genuine architecture-level contradiction in the frozen baseline, that issue must be raised explicitly as a separate governance event. It must not be repaired indirectly through L3 wording.

## 5. Closed Gates

The following remain outside v0.0.3rc03:

- promotion of Candidate patterns to `Available` before independent tranche review;
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
