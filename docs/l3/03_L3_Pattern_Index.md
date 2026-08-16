# SCAF L3 Pattern Index

**Development Release:** v0.0.3rc10  
**Status:** Navigation index; not trace authority

## 1. Current Catalog State

v0.0.3rc10 contains **twelve published Pattern identities** after the rc09 focused trace-closure review returned `YES`.

- **7 initial-tranche entries:** `Available / M2`, introduced in v0.0.3rc03.
- **5 second-tranche entries:** `Candidate / M2`, introduced in v0.0.3rc08 after completed architecture review and trace closure; availability remains separately gated.

The authoritative human-readable upstream trace remains inside each Pattern file. This index is navigation only.

## 2. Mechanism Families

| Family | Name | Current Pattern Count | Development Position |
|---|---|---:|---|
| `SUP` | Supervision & Detection | 2 | Initial tranche / Available M2 |
| `COM` | Interaction Resilience | 1 | Initial tranche / Available M2 |
| `REC` | Recovery & Reintegration | 1 | Initial tranche / Available M2 |
| `FTL` | Fault Tolerance & Isolation | 2 | Second tranche / Candidate M2 |
| `TIM` | Timing & Capacity Realization | 2 | Second tranche / Candidate M2 |
| `PST` | Persistent State Integrity | 1 | Initial tranche / Available M2 |
| `LCM` | Lifecycle Management | 1 | Initial tranche / Available M2 |
| `EVD` | Evidence & Incident Recording | 1 | Initial tranche / Available M2; approved export category deferred |
| `SYN` | Distributed Consistency & Reconciliation | 1 | Second tranche / Candidate M2 |
| `SEC` | Security Realization | 0 | Separate security-realization gate |
| **Total** |  | **12** | 7 Available/M2 + 5 Candidate/M2 |

## 3. Published Available / M2 Entries

| Pattern ID | Pattern Name | Family | Kind | Status | Maturity |
|---|---|---|---|---|---|
| `SCAF-PAT-SUP-001` | Heartbeat / Liveness Supervision | `SUP` | Mechanism | Available | M2 |
| `SCAF-PAT-SUP-002` | Independent Watchdog with Escalation | `SUP` | Mechanism | Available | M2 |
| `SCAF-PAT-REC-001` | Bounded Retry with Escalation | `REC` | Mechanism | Available | M2 |
| `SCAF-PAT-COM-001` | Reconnect plus State Reconciliation | `COM` | Composite Pattern | Available | M2 |
| `SCAF-PAT-PST-001` | Atomic Dual-Copy Persistent State | `PST` | Mechanism | Available | M2 |
| `SCAF-PAT-LCM-001` | Transactional Update with Rollback | `LCM` | Composite Pattern | Available | M2 |
| `SCAF-PAT-EVD-001` | Pre/Post-Trigger Retained Incident Evidence Ring | `EVD` | Composite Pattern | Available | M2 |

## 4. Published Second-Tranche Candidate / M2 Entries

| Pattern ID | Pattern Name | Family | Kind | Status | Maturity |
|---|---|---|---|---|---|
| `SCAF-PAT-FTL-001` | Failure-Domain Containment / Isolation | `FTL` | Mechanism | Candidate | M2 |
| `SCAF-PAT-FTL-002` | Controlled Failover with Graceful Degradation | `FTL` | Composite Pattern | Candidate | M2 |
| `SCAF-PAT-TIM-001` | Bounded Queue / Backpressure / Overload Protection | `TIM` | Mechanism | Candidate | M2 |
| `SCAF-PAT-TIM-002` | Timebase / Clock-Relationship / Epoch Validity | `TIM` | Mechanism | Candidate | M2 |
| `SCAF-PAT-SYN-001` | Generation/Epoch-Based Cross-Participant State Convergence | `SYN` | Composite Pattern | Candidate | M2 |

## 5. Second-Tranche Lifecycle Position

The five second-tranche entries completed independent architecture review in rc08 and focused trace closure in rc09. rc10 records them as `Candidate / M2` while preserving all IDs, primary families and `Introduced In: v0.0.3rc08` history.

The EVD export/transformation category remains approved but deferred. The PST configuration-activation/source-precedence proposal remains rejected/reframe. SEC-primary authoring remains separately gated.

## 6. Immediate Gate

The rc10 review shall validate M2 and availability readiness as separate axes for each of the five second-tranche entries. No status change occurs in rc10. A later RC may explicitly accept reviewed entries as `Available` only after this gate succeeds.
