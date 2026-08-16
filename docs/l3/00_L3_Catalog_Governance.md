# SCAF L3 Catalog Governance

**Development Release:** v0.0.3rc01  
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

Examples of valid future identities:

```text
SCAF-PAT-SUP-001
SCAF-PAT-REC-001
SCAF-PAT-PST-001
SCAF-PAT-EVD-001
```

Rules:

1. `<FAMILY>` must be a registered L3 mechanism-family code.
2. `<NNN>` is a three-digit monotonically assigned number within the family.
3. Once an ID has been published in a repository release, the ID is not reused for another pattern.
4. Editorial clarification or compatible refinement retains the same ID.
5. A change that materially changes intent, architectural mechanism, selection contract, failure behavior or incompatible semantics requires a new pattern ID and an explicit supersession relation.
6. Version numbers are not embedded in pattern IDs; repository release history carries version state.
7. Frozen L1/L2 concern IDs such as `SCAF-ROB-*` or `SCAF-CFG-*` are never reused as pattern IDs.

No `SCAF-PAT-*` ID is instantiated in v0.0.3rc01.

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

The recommended first pattern tranche, after this catalog contract passes review, is intentionally small and representative:

1. `SUP` — supervision / liveness / progress detection;
2. `REC` — bounded retry / escalation / reconciliation;
3. `PST` — persistent-state integrity / atomicity;
4. `LCM` — update / activation / rollback lifecycle;
5. `EVD` — retained incident evidence / pre-post event recording;
6. `COM` — freshness / sequence / reconnect interaction resilience.

`FTL`, `TIM`, `SYN` and especially technology-sensitive `SEC` patterns should expand after the first representative set proves the metadata, trace and selection model.

## 12. v0.0.3rc01 Gate

Before bulk pattern authoring begins, independent review should determine whether:

- the L3 taxonomy is mechanism-oriented rather than a duplicate concern taxonomy;
- the catalog remains subordinate to frozen L1/L2 authority;
- pattern selection cannot be misread as requirement satisfaction;
- valid alternate/project-specific mechanisms remain permitted;
- L2→L3 trace supports many-to-many relations;
- status and maturity are semantically separate;
- the metadata contract captures unresolved PDA decisions;
- the L3/L4 boundary prevents implementation-rule creep;
- no v0.0.2 normative file was modified.
