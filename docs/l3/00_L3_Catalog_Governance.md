# SCAF L3 Catalog Governance

**Development Release:** v0.0.3rc05  
**Upstream Baseline:** frozen v0.0.2 L1/L2  
**Framework Plane:** `SCAF-PROF`  
**Status:** Development contract

## 1. Purpose

This document defines the architecture boundary and catalog-governance model for SCAF L3 Pattern / Mechanism content.

L3 is downstream of the frozen L1/L2 concern authorities. It exists to describe reusable candidate mechanisms without converting any single mechanism into a universal L2 implementation mandate.

This document introduces no new L1/L2 requirement IDs and does not alter the 294 frozen v0.0.2 normative requirement IDs.

## 2. L3 Authority Position

L3 belongs to framework-side `SCAF-PROF` realization/profile content.

L3 may:

- describe reusable candidate realization mechanisms;
- identify applicability conditions and non-applicability conditions;
- trace a mechanism to one or more frozen L2 obligations;
- describe legitimate variants, forces, tradeoffs, weaknesses and composition relations;
- identify project decisions that remain unresolved until a Project Design Authority acts;
- constrain or guide realization only where an applicable profile/catalog rule explicitly establishes such a constraint.

L3 does not:

- redefine an L1/L2 concern obligation;
- create a hidden L2 requirement through pattern prose;
- make a pattern universally mandatory merely because a traced L2 obligation is Applicable;
- define the actual project-specific architecture value, threshold, topology, allocation or selected implementation;
- act as Project Design Authority;
- act as Project Realization;
- act as project verification or evidence-sufficiency authority;
- imply that catalog membership establishes compliance or satisfaction.

## 3. Canonical Semantics

The governing interpretation is:

> **L2 defines the required architectural outcome or project decision. L3 describes reusable candidate realization mechanisms. Project Design Authority selects, rejects, combines or adapts mechanisms and records the actual project decision. Project Realization implements that decision.**

Accordingly:

```text
Applicable L2 obligation
        ≠
automatic L3 applicability
        ≠
automatic L3 selection
        ≠
L2 satisfaction
```

A project may use:

- one catalog pattern;
- multiple composed catalog patterns;
- an adapted catalog pattern;
- a project-specific mechanism not present in the catalog;
- no realization mechanism where the applicable obligation is satisfied by another valid architecture basis.

The project remains responsible for establishing the Applicable Satisfaction Basis defined by the frozen Authority Kernel.

## 4. Mechanism-Family Taxonomy

L3 uses a mechanism-family taxonomy rather than duplicating the frozen CTX / ARCH / INT / TIME / RUN / ROB / LIFE / OBS / CFG / SEC concern tree.

The initial families are:

| Code | Family | Scope |
|---|---|---|
| `SUP` | Supervision & Detection | liveness, progress, deadline, health and plausibility supervision mechanisms |
| `COM` | Interaction Resilience | freshness, sequencing, duplicate/reorder handling, bounded messaging and reconnect interaction mechanisms |
| `REC` | Recovery & Reintegration | retry, backoff, escalation, restart, resynchronization and reintegration mechanisms |
| `FTL` | Fault Tolerance & Isolation | containment, redundancy, failover, voting and isolation mechanisms |
| `TIM` | Timing & Capacity Realization | timer/timebase, synchronization, queue/backpressure and capacity-protection mechanisms |
| `PST` | Persistent State Integrity | atomic commit, redundant copy, journal, generation/version and corruption-recovery mechanisms |
| `LCM` | Lifecycle Management | boot, reset, update, activation, rollback and interrupted-lifecycle mechanisms |
| `EVD` | Evidence & Incident Recording | retained evidence, event rings, crash/incident recording, correlation and export mechanisms |
| `SYN` | Distributed Consistency & Reconciliation | generation/epoch, replica synchronization, partition reconciliation and distributed state convergence mechanisms |
| `SEC` | Security Realization | authentication, authorization, trust restoration, credential/key handling and control-path protection mechanisms |

These family codes are L3 catalog organization codes. They are **not new SCAF top-level concerns or authority homes**.

A pattern has one primary family for identity and navigation even when it traces across multiple frozen concerns.

## 5. Profile Facets Are Orthogonal to Pattern Families

The existing `SCAF-PROF` realization/profile axes remain orthogonal applicability facets rather than the L3 pattern taxonomy.

Candidate facets include, where useful:

- compute / deployment;
- execution model;
- language / runtime;
- interaction / transport;
- persistence / storage;
- human-interface realization.

A heartbeat-supervision pattern, for example, remains a `SUP` pattern even when applicable variants exist for MCU, PC, RTOS, OS, UART, CAN, Ethernet or IPC contexts.

L3 shall not create separate top-level catalogs merely because the implementation technology is MCU, PC, SoC, FPGA or DSP.

## 6. Pattern ID Rule

Pattern IDs use:

```text
SCAF-PAT-<FAMILY>-<NNN>
```

Illustrative **format placeholders** (not allocated or reserved identities):

```text
SCAF-PAT-SUP-<NNN>
SCAF-PAT-REC-<NNN>
SCAF-PAT-PST-<NNN>
SCAF-PAT-EVD-<NNN>
```

Rules:

1. `<FAMILY>` must be a registered L3 mechanism-family code.
2. `<NNN>` is a three-digit monotonically assigned number within the family when an actual catalog entry is instantiated.
3. For pattern-identity lifecycle purposes, **published** means an ID has been assigned to an instantiated catalog entry and included in a repository release. Illustrative placeholders or examples do not allocate or reserve an ID.
4. Once an instantiated pattern ID has been published, the ID is not reused for another pattern.
5. Editorial clarification or compatible refinement retains the same ID.
6. A change that materially changes intent, architectural mechanism, selection contract, failure behavior or incompatible semantics requires a new pattern ID and an explicit `Supersedes` relation where lifecycle replacement applies.
7. The primary family is selected from the pattern's **principal reusable mechanism intent**, not from the frozen concern that contributes the greatest number of L2 traces.
8. The primary-family component of a published pattern ID is immutable. If later review determines that an instantiated pattern's genuine primary family must change, the reclassified pattern receives a new ID and records an explicit `Supersedes` relation to the prior identity; the prior identity is retained under the appropriate catalog lifecycle status.
9. Version numbers are not embedded in pattern IDs; repository release history carries version state.
10. Frozen L1/L2 concern IDs such as `SCAF-ROB-*` or `SCAF-CFG-*` are never reused as pattern IDs.

v0.0.3rc03 instantiates the seven Candidate/M1 Pattern IDs listed in Section 12. These published identities are now governed by the stable-ID and primary-family rules above.

## 7. Catalog Status

Pattern status describes catalog lifecycle, not engineering confidence:

| Status | Meaning |
|---|---|
| `Draft` | Pattern is being formed and may change materially |
| `Candidate` | Structure is complete enough for focused architecture review |
| `Available` | Accepted for project consideration under the current catalog release |
| `Deprecated` | Retained for compatibility/trace but discouraged for new selection |
| `Retired` | Historical only; not offered for new selection |

`Available` does not mean mandatory, compliant, verified for a project, or sufficient to satisfy an L2 obligation.

A `Candidate`→`Available` transition is a deliberate **catalog acceptance** decision. Unless a later governance rule explicitly establishes a stricter gate, an entry considered for `Available` shall have:

- maturity of at least `M2 — Architecture Reviewed`;
- no unresolved Critical, Major or Minor finding that materially affects pattern identity, authority boundary, L2 trace, applicability, PDA decision ownership, source-authority ownership or L3/L4 separation;
- sufficiently clear applicability, non-applicability/cautions, Required PDA Decisions, forces/tradeoffs, weakness modes and selection consequences for responsible project consideration;
- provenance/reference basis stated at its actual maturity without uncontrolled donor promotion;
- an explicit catalog lifecycle decision recording the acceptance.

`Available` does not require M3 or M4 evidence. M3/M4 describe additional engineering confidence, not the minimum catalog-availability state.

## 8. Pattern Maturity

Maturity is independent of status:

| Level | Name | Meaning |
|---|---|---|
| `M0` | Concept | Mechanism concept identified; evidence and structure incomplete |
| `M1` | Structured | Required metadata, trace, applicability and tradeoff structure completed |
| `M2` | Architecture Reviewed | Authority boundary, L2 trace and L3/L4 boundary independently reviewed |
| `M3` | Multi-Context Validated | Mechanism reasoning exercised across materially different system/realization contexts |
| `M4` | Reference / Field Backed | Supported by controlled reference implementation, project experience or retained field evidence |

Maturity does not make a pattern universally applicable or mandatory.

Promotion to `M2 — Architecture Reviewed` requires independent review evidence covering, at minimum, the pattern's authority boundary, L2 trace and L3/L4 boundary. Critical/Major findings and any Minor finding materially affecting those M2 dimensions shall be resolved or explicitly dispositioned through the controlled review process before M2 promotion is recorded.

## 9. Composition Relations

Patterns may explicitly relate through:

- `Requires` — another pattern/mechanism capability is structurally required for the described mechanism to operate as claimed;
- `Commonly Composed With` — composition is common but not mandatory;
- `Alternative To` — mechanisms commonly address substantially overlapping realization intent through different tradeoffs;
- `Conflicts With` — simultaneous selection may create incompatible semantics or assumptions;
- `Subsumes` — one pattern intentionally includes the architecture intent of another in a defined scope;
- `Supersedes` — lifecycle replacement relation between published pattern identities.

Composition relations are catalog guidance. They are not project dependency truth until adopted in a controlled project decision.

## 10. L3 / L4 Boundary

L3 may describe mechanism architecture, such as:

- participants/responsibilities involved;
- conceptual state and information flow;
- validity/generation/selection semantics;
- failure and fallback behavior;
- architectural variants;
- required project decisions;
- forces and tradeoffs.

L3 shall not, in this development stage, prescribe:

- source code or language-specific APIs;
- concrete register/flash address/layout values;
- product-specific file paths or database tables;
- exact scheduler APIs or OS calls;
- concrete protocol packet layouts unless the pattern itself is explicitly a protocol-architecture pattern at the permitted abstraction;
- device-specific initialization sequences;
- step-by-step verification procedures or executable test cases.

Those belong to later L4 implementation / verification guidance or project-specific controlled artifacts.

## 11. Initial Development Priority

The catalog-contract gate has passed and the first deliberately small representative tranche published in v0.0.3rc03 remains the active seven-pattern tranche in v0.0.3rc05 across:

1. `SUP` — supervision / liveness / progress detection;
2. `REC` — bounded retry / escalation;
3. `COM` — reconnect / interaction reconciliation;
4. `PST` — persistent-state integrity / atomicity;
5. `LCM` — update / activation / rollback lifecycle;
6. `EVD` — retained incident evidence / pre-post event recording.

`FTL`, `TIM`, `SYN` and especially technology-sensitive `SEC` remain later expansion areas. The first seven entries have now demonstrated stable metadata, trace, primary-family, composition and L3/L4 semantics through independent review and closure. Broad second-tranche authoring remains separately gated while rc05 validates their M2 lifecycle decision and assesses `Available` readiness.


## 12. v0.0.3rc03 Initial Pattern-Tranche Gate

The v0.0.3rc02 focused closure review returned:

```text
L3 CATALOG-CONTRACT CLOSURE GATE: YES
```

v0.0.3rc03 therefore allocates the first seven permanent pattern identities as **Candidate / M1** entries solely to stress-test the accepted catalog contract:

- `SCAF-PAT-SUP-001` — Heartbeat / Liveness Supervision;
- `SCAF-PAT-SUP-002` — Independent Watchdog with Escalation;
- `SCAF-PAT-REC-001` — Bounded Retry with Escalation;
- `SCAF-PAT-COM-001` — Reconnect plus State Reconciliation;
- `SCAF-PAT-PST-001` — Atomic Dual-Copy Persistent State;
- `SCAF-PAT-LCM-001` — Transactional Update with Rollback;
- `SCAF-PAT-EVD-001` — Pre/Post-Trigger Retained Incident Evidence Ring.

These identities are now published and therefore subject to the stable-ID and primary-family immutability rules in this document. Their `Candidate` status does not imply universal recommendation, project selection or L2 satisfaction.

Before any entry is promoted to `Available` or the catalog expands materially, independent review shall determine whether:

- each pattern remains subordinate to the frozen L2 authority and does not redefine its traced obligations;
- the L2 trace relations are accurate, many-to-many and free of generic `satisfies` shortcuts;
- the primary family reflects principal reusable mechanism intent, especially for cross-cutting `SCAF-PAT-COM-001`;
- required PDA decisions preserve actual project selection/configuration authority;
- external source-authority constraints remain external inputs rather than catalog/PDA-owned objectives;
- the patterns remain L3 architecture mechanisms and do not leak numeric/device/API/code/test-procedure L4 detail;
- composition relations are guidance rather than automatic project dependency truth;
- provenance, including the supplemental incident-recorder RC donor, does not imply uncontrolled donor promotion;
- all seven IDs are unique, stable and consistent with the catalog index;
- the frozen v0.0.2 normative tree remains byte-stable.


## 13. v0.0.3rc04 Initial-Tranche Trace-Closure Gate

The independent v0.0.3rc03 tranche review returned:

```text
INITIAL L3 PATTERN-TRANCHE GATE: YES, AFTER MINOR CLEANUP
```

It found no Critical or Major issue, cleared the `SCAF-PAT-COM-001` COM/REC/SYN identity stress case, and identified four localized Minor trace-contract defects (`R3-01` through `R3-04`). v0.0.3rc04 therefore preserves all seven published identities, families, Candidate status and M1 maturity while correcting only those trace classifications/inputs.

The rc04 focused closure review shall confirm:

- `R3-01`: `SCAF-PAT-SUP-002` no longer overstates `SCAF-ROB-032` as watchdog Primary realization and LIFE reset semantics remain consumed Constraint Inputs rather than watchdog-owned reset realization;
- `R3-02`: `SCAF-PAT-REC-001` consumes applicable `SCAF-INT-007` duplicate/order semantics for repeated/interleaved Interaction exchanges and, where relevant, `SCAF-INT-010` session-incarnation semantics without transferring INT authority into REC;
- `R3-03`: `SCAF-PAT-LCM-001` explicitly consumes `SCAF-RUN-009` for LIFE-to-RUN readiness handoff without conflating lifecycle activation with operational readiness;
- `R3-04`: `SCAF-PAT-EVD-001` explicitly consumes `SCAF-OBS-009` for causal/derived-inference claim basis and does not turn recorder chronology into root-cause authority;
- all seven published IDs, primary families, Candidate/M1 states and index counts remain stable;
- no generic L2→L3 `satisfies` shortcut, authority inversion, L4 detail, schema/validator/CI/code-generation/executable-governance work or frozen normative edit is introduced.

A successful rc04 closure review may permit the **next RC** to record successful architecture review and make explicit, entry-by-entry decisions about M2 advancement and/or `Available` status. This gate does not itself auto-promote any pattern and does not authorize uncontrolled bulk catalog expansion.


## 14. v0.0.3rc05 Initial-Tranche Maturity / Availability Gate

The focused independent v0.0.3rc04 closure review returned:

```text
INITIAL L3 PATTERN-TRANCHE TRACE-CLOSURE GATE: YES
```

It confirmed `R3-01` through `R3-04` fully Resolved, found no new Critical/Major/Minor/Trivial regression, preserved the same seven published identities/families and reconfirmed the frozen v0.0.2 baseline.

v0.0.3rc05 therefore records an explicit **M1→M2 maturity advancement for all seven initial-tranche entries**. The basis is the completed rc03 independent architecture review plus rc04 focused closure review, which together cover authority boundary, L2 trace and L3/L4 conformance for every entry.

All seven entries remain `Catalog Status: Candidate`. M2 maturity is an engineering-review state; it is not the catalog acceptance decision represented by `Available`.

The rc05 independent review shall therefore answer two separate questions for every pattern:

1. **M2 validation:** is the recorded `M2 — Architecture Reviewed` state justified by the available review/closure evidence and current pattern content?
2. **Availability readiness:** is the entry sufficiently clear and controlled for a later explicit `Candidate`→`Available` lifecycle transition under Section 7, without implying recommendation, project applicability, compliance or L2 satisfaction?

A successful rc05 review may permit a later RC to promote all, some or none of the seven entries to `Available`. Such status changes must be explicit and entry-specific. The same later RC may separately decide whether to open a small second pattern tranche. Neither action is automatic.
