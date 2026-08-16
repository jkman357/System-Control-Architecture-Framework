# SCAF L3 Pattern Index

**Development Release:** v0.0.3rc14  
**Status:** Navigation index; not trace authority

## 1. Current Catalog State

v0.0.3rc14 contains **twelve published Pattern identities**. The rc13 focused closure review confirmed the architecture/trace/lifecycle baseline and all mandatory non-regression checks, opened no new/regression finding, and returned `L3 V0.0.3 FREEZE-CANDIDATE CLOSURE GATE: YES, AFTER MINOR CLEANUP`. rc14 closes only the final stale navigation residue of upstream finding `R12-01`.

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

## 4. v0.0.3 Freeze-Candidate Closure Position

The five second-tranche entries completed independent architecture review in rc08, focused trace closure in rc09, M2 advancement/readiness review in rc10, explicit availability acceptance in rc11, and successful rc11 acceptance/non-regression review. The initial seven previously completed the same controlled lifecycle through rc06.

rc14 changes no catalog status or maturity. It performs only the final Pattern Index navigation cleanup required by the rc13 focused closure review. The twelve-entry `Available / M2` catalog and its L3 contracts are otherwise unchanged.

The EVD export/transformation category remains approved but deferred. The PST configuration-activation/source-precedence proposal remains rejected/reframe. SEC-primary authoring remains separately gated. M3/M4, L4 and executable governance also remain outside the proposed v0.0.3 frozen scope.

## 5. Immediate Gate

The rc14 closure review shall determine whether upstream finding `R12-01` is fully resolved and whether the rc14 tree is eligible for a **later explicit v0.0.3 freeze action**. It must verify current navigation consistency, frozen-baseline integrity, twelve-ID lifecycle/identity stability, Pattern-body non-regression, preservation of the `FTL-001` trace closure, and continued exclusion of separately gated future work.

**rc14 itself remains an RC and performs no freeze.**
