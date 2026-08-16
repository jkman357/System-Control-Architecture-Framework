# SCAF L3 Second-Tranche Trace Cleanup Decision

**Development Release:** v0.0.3rc09  
**Upstream Pattern Release:** v0.0.3rc08  
**Scope:** localized closure of independent review finding `R8-01` only

## 1. Decision Basis

The independent v0.0.3rc08 second-tranche Pattern review returned:

```text
L3 SECOND-TRANCHE PATTERN GATE: YES, AFTER MINOR CLEANUP
```

The review reported **0 Critical, 0 Major, 1 Minor** finding. Four of the five new second-tranche entries passed without finding. The only cleanup item is `R8-01` in `SCAF-PAT-FTL-001`.

`R8-01` found that `SCAF-ROB-007` was classified as `Supporting L2 Trace` even though `FTL-001` consumes a project-identified failure-propagation path to constrain containment placement/configuration. Under the accepted L3 metadata contract, that relationship is a **Constraint Input**.

## 2. rc09 Localized Change

`SCAF-PAT-FTL-001` retains:

- Pattern ID `SCAF-PAT-FTL-001`;
- immutable primary family `FTL`;
- `Catalog Status: Candidate`;
- `Maturity: M1 — Structured`;
- `Introduced In: v0.0.3rc08`;
- `SCAF-ROB-008` as Primary L2 Trace;
- `SCAF-ROB-015` as Supporting L2 Trace;
- all existing ARCH/common-mode constraints and the existing L3/L4 boundary.

The localized correction is:

```text
SCAF-ROB-007
Supporting L2 Trace -> Constraint Input
```

The detailed trace rationale now states that the project-identified material failure-propagation path is an upstream controlled input that constrains containment placement, isolation action and propagation-blocking evaluation. The Pattern does not author or replace the ROB-owned propagation-path identification obligation.

## 3. Non-Change Boundary

This cleanup does **not**:

- change any other Pattern ID or primary family;
- change the mechanism intent of `FTL-001`;
- modify `FTL-002`, `TIM-001`, `TIM-002` or `SYN-001` architecture/trace content;
- modify the initial seven `Available / M2` Pattern architecture bodies;
- promote any second-tranche entry to M2 or `Available`;
- author the deferred EVD export/transformation category;
- allocate an ID for the rejected/reframe PST proposal;
- open SEC-primary authoring;
- modify frozen v0.0.2 normative content;
- introduce M3/M4, L4, schema, validator, generated registry/index, CI, code generation or executable governance.

## 4. Closure Gate

The rc09 independent review is a focused trace-closure review. It shall verify that:

1. `R8-01` is fully resolved by the relation reclassification and rationale;
2. `SCAF-ROB-007` is no longer represented as a Supporting Realization in `FTL-001`;
3. `SCAF-ROB-015` remains the Supporting trace identified by the rc08 review;
4. the `FTL-001` ID/family/Candidate/M1/Introduced-In state remains stable;
5. the other eleven published Pattern architecture bodies are non-regressed except current Development Release metadata;
6. the frozen v0.0.2 normative baseline remains byte-stable; and
7. no lifecycle promotion or new catalog scope is opened by the cleanup.

A successful closure review permits a later explicit maturity/readiness decision for the five second-tranche entries. It does not itself promote them or authorize additional Pattern authoring.
