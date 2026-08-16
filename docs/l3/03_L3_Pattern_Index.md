# SCAF L3 Pattern Index

**Development Release:** v0.0.3rc09  
**Status:** Navigation index; not trace authority

## 1. Current Catalog State

v0.0.3rc09 contains **twelve published Pattern identities**. The independent rc08 second-tranche review returned `YES, AFTER MINOR CLEANUP`; rc09 performs only the localized `FTL-001` trace-relation correction before focused closure.

- **7 initial-tranche entries:** `Available / M2`, introduced in v0.0.3rc03 and unchanged in architecture/trace content except current Development Release metadata.
- **5 second-tranche entries:** `Candidate / M1`, introduced in v0.0.3rc08; rc09 changes only the `FTL-001` `SCAF-ROB-007` relation classification and awaits focused closure.

The authoritative human-readable upstream trace remains inside each Pattern file. This index is navigation only.

## 2. Mechanism Families

| Family | Name | Current Pattern Count | Development Position |
|---|---|---:|---|
| `SUP` | Supervision & Detection | 2 | Initial tranche / Available M2 |
| `COM` | Interaction Resilience | 1 | Initial tranche / Available M2 |
| `REC` | Recovery & Reintegration | 1 | Initial tranche / Available M2 |
| `FTL` | Fault Tolerance & Isolation | 2 | Second tranche / Candidate M1 |
| `TIM` | Timing & Capacity Realization | 2 | Second tranche / Candidate M1 |
| `PST` | Persistent State Integrity | 1 | Initial tranche / Available M2 |
| `LCM` | Lifecycle Management | 1 | Initial tranche / Available M2 |
| `EVD` | Evidence & Incident Recording | 1 | Initial tranche / Available M2; approved export category deferred |
| `SYN` | Distributed Consistency & Reconciliation | 1 | Second tranche / Candidate M1 |
| `SEC` | Security Realization | 0 | Separate security-realization gate |
| **Total** |  | **12** | 7 Available/M2 + 5 Candidate/M1 |

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

## 4. Published Second-Tranche Candidate / M1 Entries

| Pattern ID | Pattern Name | Family | Kind | Status | Maturity |
|---|---|---|---|---|---|
| `SCAF-PAT-FTL-001` | Failure-Domain Containment / Isolation | `FTL` | Mechanism | Candidate | M1 |
| `SCAF-PAT-FTL-002` | Controlled Failover with Graceful Degradation | `FTL` | Composite Pattern | Candidate | M1 |
| `SCAF-PAT-TIM-001` | Bounded Queue / Backpressure / Overload Protection | `TIM` | Mechanism | Candidate | M1 |
| `SCAF-PAT-TIM-002` | Timebase / Clock-Relationship / Epoch Validity | `TIM` | Mechanism | Candidate | M1 |
| `SCAF-PAT-SYN-001` | Generation/Epoch-Based Cross-Participant State Convergence | `SYN` | Composite Pattern | Candidate | M1 |

## 5. rc08 Authoring Position

The rc07 review approved six categories for later authoring. rc08 chooses five to keep the review focused on opening the previously empty FTL/TIM/SYN families. The EVD export/transformation category remains approved but deferred. The PST configuration-activation/source-precedence proposal remains rejected/reframe and has no ID. SEC-primary authoring remains separately gated.

## 6. Immediate Gate

The next review shall independently assess all five new Candidate/M1 entries for identity/family fit, L2 trace relations, authority boundaries, non-duplication, composition semantics and L3/L4 conformance. M2/Available promotion, further tranche expansion, M3/M4, L4 and executable governance remain separately gated.
