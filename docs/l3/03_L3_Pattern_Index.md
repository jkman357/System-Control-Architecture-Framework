# SCAF L3 Pattern Index

**Development Release:** v0.0.3  
**Status:** Frozen v0.0.3 navigation index; not trace authority

## 1. Frozen Catalog State

v0.0.3 contains **twelve published Pattern identities**, all `Available / M2 — Architecture Reviewed`. The independent rc14 final-navigation closure review returned `L3 V0.0.3 FREEZE-CANDIDATE CLOSURE GATE: YES`, resolved upstream finding `R12-01`, and opened no new/regression findings. The explicit governance freeze therefore establishes the reviewed twelve-entry catalog as the frozen v0.0.3 L3 baseline.

- **7 initial-tranche entries:** `Available / M2`, introduced in v0.0.3rc03.
- **5 second-tranche entries:** `Available / M2`, introduced in v0.0.3rc08 after completed architecture review, trace closure, M2 validation and independent availability-readiness assessment.

The authoritative human-readable upstream trace remains inside each Pattern file. This index is navigation only.

## 2. Mechanism Families

| Family | Name | Current Pattern Count | Development Position |
|---|---|---:|---|
| `SUP` | Supervision & Detection | 2 | Initial tranche / Available M2 |
| `COM` | Interaction Resilience | 1 | Initial tranche / Available M2 |
| `REC` | Recovery & Reintegration | 1 | Initial tranche / Available M2 |
| `FTL` | Fault Tolerance & Isolation | 2 | Second tranche / Available M2 |
| `TIM` | Timing & Capacity Realization | 2 | Second tranche / Available M2 |
| `PST` | Persistent State Integrity | 1 | Initial tranche / Available M2 |
| `LCM` | Lifecycle Management | 1 | Initial tranche / Available M2 |
| `EVD` | Evidence & Incident Recording | 1 | Initial tranche / Available M2; approved export category deferred |
| `SYN` | Distributed Consistency & Reconciliation | 1 | Second tranche / Available M2 |
| `SEC` | Security Realization | 0 | Separate security-realization gate |
| **Total** |  | **12** | 12 Available/M2 |

## 3. Published Available / M2 Entries

| Pattern ID | Pattern Name | Family | Kind | Status | Maturity | Introduced In |
|---|---|---|---|---|---|---|
| `SCAF-PAT-SUP-001` | Heartbeat / Liveness Supervision | `SUP` | Mechanism | Available | M2 | v0.0.3rc03 |
| `SCAF-PAT-SUP-002` | Independent Watchdog with Escalation | `SUP` | Mechanism | Available | M2 | v0.0.3rc03 |
| `SCAF-PAT-REC-001` | Bounded Retry with Escalation | `REC` | Mechanism | Available | M2 | v0.0.3rc03 |
| `SCAF-PAT-COM-001` | Reconnect plus State Reconciliation | `COM` | Composite Pattern | Available | M2 | v0.0.3rc03 |
| `SCAF-PAT-PST-001` | Atomic Dual-Copy Persistent State | `PST` | Mechanism | Available | M2 | v0.0.3rc03 |
| `SCAF-PAT-LCM-001` | Transactional Update with Rollback | `LCM` | Composite Pattern | Available | M2 | v0.0.3rc03 |
| `SCAF-PAT-EVD-001` | Pre/Post-Trigger Retained Incident Evidence Ring | `EVD` | Composite Pattern | Available | M2 | v0.0.3rc03 |
| `SCAF-PAT-FTL-001` | Failure-Domain Containment / Isolation | `FTL` | Mechanism | Available | M2 | v0.0.3rc08 |
| `SCAF-PAT-FTL-002` | Controlled Failover with Graceful Degradation | `FTL` | Composite Pattern | Available | M2 | v0.0.3rc08 |
| `SCAF-PAT-TIM-001` | Bounded Queue / Backpressure / Overload Protection | `TIM` | Mechanism | Available | M2 | v0.0.3rc08 |
| `SCAF-PAT-TIM-002` | Timebase / Clock-Relationship / Epoch Validity | `TIM` | Mechanism | Available | M2 | v0.0.3rc08 |
| `SCAF-PAT-SYN-001` | Generation/Epoch-Based Cross-Participant State Convergence | `SYN` | Composite Pattern | Available | M2 | v0.0.3rc08 |

## 4. v0.0.3 Frozen Baseline Position

The first and second Pattern tranches completed the controlled Candidate/M1 → independent review/closure → M2 → availability-readiness → explicit Available lifecycle. rc12–rc14 then consolidated the milestone, closed release-record residues and passed the final independent freeze-candidate closure review.

The v0.0.3 freeze changes no catalog status or maturity and introduces no new Pattern ID. It freezes the reviewed twelve-entry `Available / M2` catalog and its L3 governance/metadata/trace contracts as the current L3 baseline.

The EVD export/transformation category remains approved but deferred. The PST configuration-activation/source-precedence proposal remains rejected/reframe. SEC-primary authoring remains separately gated. M3/M4, L4 and executable governance remain outside the frozen v0.0.3 scope.

## 5. Governance State

v0.0.3 is formally frozen by explicit governance decision following the rc14 closure result:

```text
L3 V0.0.3 FREEZE-CANDIDATE CLOSURE GATE: YES
```

This index and the frozen Pattern catalog shall not be modified in place for semantic evolution. Later work must use a new controlled RC development line.
