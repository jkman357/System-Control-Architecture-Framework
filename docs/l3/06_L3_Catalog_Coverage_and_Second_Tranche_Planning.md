# SCAF L3 Catalog Coverage / Second-Tranche Planning

**Development Release:** v0.0.3rc07  
**Upstream Baseline:** frozen v0.0.2 L1/L2  
**Current Published Catalog:** seven `Available / M2` patterns  
**Decision Type:** descriptive trace-reference coverage audit and controlled second-tranche planning; no new Pattern ID allocation

## 1. Purpose

This document evaluates how the current seven-pattern L3 catalog references the frozen v0.0.2 L1/L2 obligation set and uses that evidence to plan, but **not yet author**, a second controlled L3 tranche.

The audit is intentionally descriptive. It does not reinterpret the frozen obligations and does not create a compliance, satisfaction or completeness score.

## 2. Coverage Semantics

This release uses **trace-reference coverage** only:

```text
Referenced
    = at least one current published L3 Pattern explicitly traces to the frozen ID
    ≠ obligation satisfied
    ≠ mechanism required
    ≠ project applicability established
    ≠ catalog completeness established

Unreferenced
    = no current published L3 Pattern explicitly traces to the frozen ID
    ≠ missing architecture
    ≠ missing project mechanism
    ≠ automatic L3 catalog gap
```

An unreferenced L2 obligation may legitimately remain unreferenced because it is primarily:

- a context, authority, state-model or architecture decision obligation rather than a reusable mechanism opportunity;
- already realized by a project-specific architecture basis;
- better represented by a future L3 pattern only when a reusable mechanism family is justified;
- outside the current tranche scope;
- intentionally reserved for a separately gated domain such as security realization.

The current catalog therefore must not optimize toward 100% numeric L2 reference coverage.

## 3. Current Trace-Reference Coverage Snapshot

The seven current `Available / M2` patterns carry explicit **Primary / Supporting / Constraint trace relations to 60 distinct frozen IDs**, and all 60 are `Project-Applicable Obligation` IDs.

Two additional Framework Normative Invariants (`SCAF-ROB-030` and `SCAF-CFG-038`) appear in provenance/mechanism-boundary context inside Pattern files, but they are **not** counted as L2 trace-reference coverage because they are not Primary / Supporting / Constraint trace targets.

Against the frozen v0.0.2 inventory, **60 of 218 Project-Applicable Obligations are currently trace-referenced by at least one L3 pattern**. The remaining **158** are unreferenced by the current seven-pattern catalog. That 158 count is a planning input only, not a defect count.

For this audit, a frozen ID is counted as trace-referenced only when it appears in one of the controlled Pattern metadata relations:

- `Primary L2 Trace`;
- `Supporting L2 Trace`;
- `Constraint Inputs`.

Incidental prose, provenance/reference-basis mentions, examples and mechanism-boundary citations are excluded from the trace-coverage count.

| Concern | Project-Applicable IDs | Currently Referenced | Unreferenced | Framework Invariants | Invariants Referenced | Planning Interpretation |
|---|---:|---:|---:|---:|---:|---|
| `AK` | 10 | 0 | 10 | 3 | 0 | Expected low direct pattern coverage; authority/application semantics are upstream governance, not a mechanism-catalog target. |
| `CTX` | 15 | 0 | 15 | 1 | 0 | Expected low direct pattern coverage; context/mission/service intent primarily constrains project architecture and pattern applicability. |
| `ARCH` | 16 | 0 | 16 | 1 | 0 | Expected low direct pattern coverage; structural decomposition and authority records are project architecture decisions, though later patterns may consume them as constraints. |
| `INT` | 16 | 4 | 12 | 3 | 0 | Partial coverage is expected. Current patterns consume session/order/contract semantics; future COM patterns may address reusable interaction-resilience mechanisms. |
| `TIME` | 16 | 5 | 11 | 4 | 0 | High-value expansion area. Current patterns consume timing budgets; dedicated TIM mechanisms for clock relationships and bounded demand are still absent. |
| `RUN` | 16 | 3 | 13 | 7 | 0 | Current traces mainly cover readiness/incarnation handoffs. Most RUN obligations remain state-model authority rather than automatic pattern gaps. |
| `ROB` | 23 | 11 | 12 | 10 | 0 | Strong current coverage but clear reusable FTL opportunities remain for containment, failover, degradation and common-mode handling. |
| `LIFE` | 23 | 11 | 12 | 10 | 0 | Update/reset/retained-state paths are represented; boot/power/brownout and multi-participant lifecycle mechanisms remain possible later candidates. |
| `OBS` | 27 | 13 | 14 | 13 | 0 | Incident capture is represented; retrieval/export/transformation and broader evidence-correlation mechanisms remain useful candidate areas. |
| `CFG` | 26 | 11 | 15 | 12 | 0 | Atomic persistent-state mechanisms are represented; activation, source precedence and provisioning remain possible reusable mechanism areas. |
| `SEC` | 30 | 2 | 28 | 12 | 0 | Intentionally sparse. Security realization remains a controlled later expansion area and should not be bulk-filled merely to raise coverage. |

## 4. Current Pattern-to-L2 Reference Surface

The table below is navigation evidence only. The authoritative trace relation and rationale remain inside each Pattern entry.

| Pattern | Primary Family | Distinct Frozen IDs Referenced | Main Cross-Concern Surface |
|---|---|---:|---|
| `SCAF-PAT-SUP-001` | `SUP` | 8 | ROB / OBS / TIME / INT |
| `SCAF-PAT-SUP-002` | `SUP` | 6 | ROB / TIME / LIFE |
| `SCAF-PAT-REC-001` | `REC` | 11 | ROB / TIME / INT |
| `SCAF-PAT-COM-001` | `COM` | 10 | ROB / INT / CFG / RUN / TIME |
| `SCAF-PAT-PST-001` | `PST` | 9 | CFG / LIFE / TIME |
| `SCAF-PAT-LCM-001` | `LCM` | 15 | LIFE / CFG / RUN / SEC |
| `SCAF-PAT-EVD-001` | `EVD` | 14 | OBS / TIME / LIFE |

Cross-pattern overlap is expected because L2→L3 trace is many-to-many. Summing the per-pattern counts therefore exceeds the 60 distinct traced Project-Applicable IDs.

## 5. Gap-Analysis Rule

A **catalog gap** may be proposed only when all of the following are true:

1. a recurring project realization problem can be described as a reusable architecture-level mechanism rather than merely restating an L2 obligation;
2. the mechanism can preserve multiple valid implementation choices and unresolved PDA decisions;
3. the candidate adds meaningful cross-project reuse beyond the seven existing patterns;
4. its principal reusable mechanism intent supports a stable primary L3 family;
5. it can remain inside the accepted L3/L4 boundary;
6. it does not require reopening the frozen L1/L2 authority home or semantics;
7. it is not better deferred to a separately gated domain such as security-specific realization.

Therefore an unreferenced obligation is **not** by itself sufficient reason to create a Pattern.

## 6. Second-Tranche Prioritization Criteria

Candidate categories are ranked using these planning criteria:

- **mechanism reuse value** — likely to recur across MCU, PC, SoC, FPGA or distributed-node systems;
- **frozen-L2 leverage** — addresses a meaningful cluster of existing obligations without rewriting them;
- **catalog stress value** — exercises currently empty or weakly represented mechanism families;
- **cross-concern value** — tests whether authority can remain clean across multiple concern traces;
- **technology neutrality** — can be expressed without choosing a concrete product/API/protocol/algorithm;
- **non-duplication** — adds a new reusable mechanism intent rather than rephrasing an existing Pattern;
- **reviewability** — can be independently reviewed at L3 without requiring L4 or project-specific evidence.

## 7. Recommended Second-Tranche Candidate Categories

No Pattern ID is allocated in rc07. The categories below are planning candidates only.

| Priority | Candidate Category | Likely Primary Family | Frozen L2 Anchors to Examine | Why It Is Valuable | Key Boundary to Stress-Test |
|---:|---|---|---|---|---|
| 1 | Failure-Domain Containment / Isolation | `FTL` | `SCAF-ROB-007`, `SCAF-ROB-008`, `SCAF-ROB-014`; architecture inputs such as containment/shared-dependency structure | Opens the currently empty FTL family with a broadly reusable resilience mechanism | FTL mechanism must consume architecture/failure-domain decisions without redefining ARCH topology |
| 2 | Controlled Failover with Graceful Degradation | `FTL` | `SCAF-ROB-009`, `SCAF-ROB-010`, `SCAF-ROB-011`, `SCAF-ROB-015`; CTX service-loss/degraded-service inputs where applicable | Exercises redundancy/failover/degradation semantics while preserving project-specific service objectives | Failover must not imply universal redundancy topology, voting rule or recovery policy |
| 3 | Bounded Queue / Backpressure / Overload Protection | `TIM` | `SCAF-TIME-009`, `SCAF-TIME-010`, `SCAF-TIME-012`, `SCAF-TIME-013`, `SCAF-TIME-011` | Opens TIM with a common cross-platform capacity mechanism; complements but does not duplicate bounded retry | TIME owns capacity/deadline semantics; mechanism must not prescribe queue depth, scheduler or transport API |
| 4 | Timebase / Clock-Relationship / Epoch Validity | `TIM` | `SCAF-TIME-002`, `SCAF-TIME-003`, `SCAF-TIME-004`, `SCAF-TIME-005`, `SCAF-TIME-020` | Provides reusable handling for monotonic time, wall-clock separation, synchronization uncertainty and clock-relationship loss | Must distinguish time authority/uncertainty semantics from concrete synchronization protocol or oscillator implementation |
| 5 | Generation/Epoch-Based Cross-Participant State Convergence | `SYN` | `SCAF-CFG-018`, `SCAF-CFG-019`, `SCAF-RUN-010`, `SCAF-RUN-011`, `SCAF-INT-010`; `SCAF-SEC-025` only where separately applicable | Opens SYN and deliberately tests complementarity with `COM-001` rather than reclassifying or duplicating it | SYN owns reusable convergence mechanism intent; COM continues to own reconnect Interaction re-establishment |
| 6 | Evidence Retrieval / Export / Transformation Integrity | `EVD` | `SCAF-OBS-022`, `SCAF-OBS-023`, `SCAF-OBS-024`, `SCAF-OBS-025`; SEC constraints where applicable | Extends evidence architecture beyond capture into controlled extraction/transfer without becoming an application/file-format cookbook | OBS evidence identity/provenance must survive copies/transforms while export medium/API remains L4/project-specific |
| 7 | Controlled Configuration Activation / Source Precedence | `PST` | `SCAF-CFG-005`, `SCAF-CFG-007`, `SCAF-CFG-011`, `SCAF-CFG-016`, `SCAF-CFG-017`, `SCAF-CFG-020`, `SCAF-CFG-022` | Complements atomic storage with reusable selection/activation semantics for multiple configuration sources | Physical persistence mechanism must remain distinct from CFG source authority, precedence and RUN application state |

### Alternate / follow-on candidate

A **Power / Brownout Lifecycle Continuity** pattern under `LCM` is a strong follow-on candidate around `SCAF-LIFE-011`, lifecycle transaction/completion semantics and applicable CFG/ROB consequences. It is not placed in the first recommended seven second-tranche categories because the tranche should stay small and should first exercise the currently empty `FTL`, `TIM` and `SYN` families.

## 8. Security Expansion Position

`SEC` has only sparse current L3 trace-reference coverage. That is intentional and **shall not** be treated as a reason to bulk-author security patterns.

Potential security realization areas include trust establishment, authentication/authorization, anti-replay, credential/key lifecycle, security-sensitive control paths, compromise containment and trust re-establishment. However, these mechanisms are particularly prone to technology-specific prescription and to importing external security authority incorrectly.

Accordingly, rc07 recommends:

> **Do not include a SEC pattern in the immediate second tranche unless a dedicated security-realization review gate first confirms the intended abstraction, external-authority inputs and L3/L4 boundary.**

This is a planning hold, not a judgment that SEC obligations lack implementation needs.

## 9. Concern Areas That Should Not Be Filled for Numeric Coverage

The following areas should not receive patterns merely because their direct current reference count is low:

- `AK` — framework/project authority and satisfaction/evidence governance;
- `CTX` — scope, mission, functions, services, external actors and context assumptions;
- `ARCH` — decomposition, topology, structural authority and architecture-decision records;
- much of `RUN` — operational state-model semantics and transition authority.

Patterns may consume these obligations as constraints when a reusable mechanism genuinely needs them, but SCAF should not manufacture mechanism entries simply to make the coverage matrix look complete.

## 10. Recommended Second-Tranche Size and Gate

If the rc07 coverage/planning review passes, the next authoring RC should remain deliberately small:

- target **4–7 new Candidate / M1 patterns**;
- prioritize at least one `FTL`, one `TIM` and one `SYN` entry;
- prefer categories from Section 7 that pass independent review;
- do not allocate a Pattern ID for a category rejected or deferred by the planning review;
- keep all seven current first-tranche entries `Available / M2` unchanged;
- do not combine second-tranche authoring with M3, L4 or executable-governance work.

## 11. Machine-Readable / Executable Governance Boundary

This rc07 audit is a **static human-readable Markdown planning artifact**. Its counts were produced from the current controlled repository state, but the repository does not introduce a schema, validator, generated registry/index, CI check or executable coverage gate.

Future automation may compute these views after a separate executable-governance gate. Until then:

- Pattern entries remain the trace authority;
- this document is descriptive planning/navigation evidence;
- the numeric coverage matrix is not a conformance metric;
- no CI or validator shall infer required Pattern coverage from it.

## 12. rc07 Decision Boundary

v0.0.3rc07 does **not**:

- allocate an eighth Pattern ID;
- modify any existing Pattern mechanism body or lifecycle state;
- promote any Pattern beyond `Available / M2`;
- open M3/M4;
- create a SEC realization pattern;
- start L4 implementation/verification guidance;
- introduce schema, validator, generated reverse index, CI, code generation or executable governance;
- modify the frozen v0.0.2 normative tree.

The immediate gate is an independent **L3 catalog coverage / second-tranche planning review**. Only after that review may a later RC allocate a small second tranche.
