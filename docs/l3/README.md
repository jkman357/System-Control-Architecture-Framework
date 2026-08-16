# SCAF L3 Pattern / Mechanism Catalog

**Development Release:** v0.0.3rc04  
**Upstream Baseline:** frozen v0.0.2 L1/L2  
**Framework Plane:** `SCAF-PROF`  
**Status:** Initial representative L3 pattern tranche trace-cleanup RC; all entries remain Candidate / M1

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

## 2. v0.0.3rc04 Scope

The independent v0.0.3rc03 initial-pattern-tranche review returned `INITIAL L3 PATTERN-TRANCHE GATE: YES, AFTER MINOR CLEANUP`, with no Critical or Major finding and four localized Minor trace-contract findings (`R3-01` through `R3-04`).

v0.0.3rc04 is therefore a narrow trace-cleanup RC. It keeps the same seven published permanent identities and keeps every entry at `Catalog Status: Candidate` and `Maturity: M1 — Structured`. It does **not** add a second tranche or promote any pattern.

Localized cleanup is limited to:

- `SCAF-PAT-SUP-002` — remove the overstated `SCAF-ROB-032` Primary trace and keep LIFE reset semantics as Constraint Inputs rather than Supporting Realization;
- `SCAF-PAT-REC-001` — add the applicable INT-owned duplicate/order and conditional session-incarnation constraints for Interaction retries;
- `SCAF-PAT-LCM-001` — add the explicit `SCAF-RUN-009` LIFE-to-RUN readiness handoff constraint;
- `SCAF-PAT-EVD-001` — add the explicit `SCAF-OBS-009` causal-inference claim-basis constraint.

The other three patterns remain semantically unchanged apart from current-development-release labeling. The next gate is a focused independent closure review of `R3-01` through `R3-04` plus regression checks across all seven published identities.

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

The following remain outside v0.0.3rc04:

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
