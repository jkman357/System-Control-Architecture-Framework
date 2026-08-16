# SCAF L3 Pattern Index

**Development Release:** v0.0.3rc05  
**Status:** Navigation index; not trace authority

## 1. Current Catalog State

v0.0.3rc05 carries forward exactly the same **seven published pattern identities** and records their deliberate maturity advancement to `M2 — Architecture Reviewed` after the successful rc04 trace-closure review. Every entry remains `Catalog Status: Candidate` pending a separate availability-readiness review.

The authoritative human-readable upstream trace remains inside each pattern file. This index is navigation only.

## 2. Mechanism Families

| Family | Name | Current Pattern Count | Development Position |
|---|---|---:|---|
| `SUP` | Supervision & Detection | 2 | Initial tranche |
| `COM` | Interaction Resilience | 1 | Initial tranche / cross-family stress case |
| `REC` | Recovery & Reintegration | 1 | Initial tranche |
| `FTL` | Fault Tolerance & Isolation | 0 | Later |
| `TIM` | Timing & Capacity Realization | 0 | Later |
| `PST` | Persistent State Integrity | 1 | Initial tranche |
| `LCM` | Lifecycle Management | 1 | Initial tranche |
| `EVD` | Evidence & Incident Recording | 1 | Initial tranche |
| `SYN` | Distributed Consistency & Reconciliation | 0 | Later |
| `SEC` | Security Realization | 0 | Later / controlled expansion |

## 3. Published Candidate / M2 Entries

| Pattern ID | Pattern Name | Family | Kind | Status | Maturity |
|---|---|---|---|---|---|
| `SCAF-PAT-SUP-001` | Heartbeat / Liveness Supervision | `SUP` | Mechanism | Candidate | M2 |
| `SCAF-PAT-SUP-002` | Independent Watchdog with Escalation | `SUP` | Mechanism | Candidate | M2 |
| `SCAF-PAT-REC-001` | Bounded Retry with Escalation | `REC` | Mechanism | Candidate | M2 |
| `SCAF-PAT-COM-001` | Reconnect plus State Reconciliation | `COM` | Composite Pattern | Candidate | M2 |
| `SCAF-PAT-PST-001` | Atomic Dual-Copy Persistent State | `PST` | Mechanism | Candidate | M2 |
| `SCAF-PAT-LCM-001` | Transactional Update with Rollback | `LCM` | Composite Pattern | Candidate | M2 |
| `SCAF-PAT-EVD-001` | Pre/Post-Trigger Retained Incident Evidence Ring | `EVD` | Composite Pattern | Candidate | M2 |

## 4. rc05 Lifecycle Review Purpose

The initial seven patterns have passed independent architecture review and focused trace closure. The rc05 review now stress-tests the **catalog lifecycle model**, not the mechanism-family taxonomy.

Review shall distinguish:

- `M2 — Architecture Reviewed`: evidence that authority boundary, L2 trace and L3/L4 boundary have been independently reviewed and material findings closed;
- `Available`: a separate catalog acceptance state indicating that the pattern is accepted for project consideration under the current catalog release.

The review shall assess each entry independently. A pattern may validly be `Candidate / M2` if architecture review is complete but catalog availability acceptance is not yet granted.

## 5. Expansion Gate

Do not change any entry from `Candidate` to `Available` and do not add a second tranche inside rc05. The independent rc05 lifecycle review must first validate the M2 evidence basis and issue an entry-by-entry availability-readiness recommendation while reconfirming the frozen v0.0.2 baseline and accepted L3 contract.
