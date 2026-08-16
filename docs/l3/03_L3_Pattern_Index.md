# SCAF L3 Pattern Index

**Development Release:** v0.0.3rc04  
**Status:** Navigation index; not trace authority

## 1. Current Catalog State

v0.0.3rc04 carries forward the first representative tranche of **seven published pattern identities**. Every entry remains `Catalog Status: Candidate` and `Maturity: M1 — Structured` while the four localized rc03 review trace findings are closed and independently re-reviewed.

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

## 3. Published Candidate Entries

| Pattern ID | Pattern Name | Family | Kind | Status | Maturity |
|---|---|---|---|---|---|
| `SCAF-PAT-SUP-001` | Heartbeat / Liveness Supervision | `SUP` | Mechanism | Candidate | M1 |
| `SCAF-PAT-SUP-002` | Independent Watchdog with Escalation | `SUP` | Mechanism | Candidate | M1 |
| `SCAF-PAT-REC-001` | Bounded Retry with Escalation | `REC` | Mechanism | Candidate | M1 |
| `SCAF-PAT-COM-001` | Reconnect plus State Reconciliation | `COM` | Composite Pattern | Candidate | M1 |
| `SCAF-PAT-PST-001` | Atomic Dual-Copy Persistent State | `PST` | Mechanism | Candidate | M1 |
| `SCAF-PAT-LCM-001` | Transactional Update with Rollback | `LCM` | Composite Pattern | Candidate | M1 |
| `SCAF-PAT-EVD-001` | Pre/Post-Trigger Retained Incident Evidence Ring | `EVD` | Composite Pattern | Candidate | M1 |

## 4. Trace-Cleanup Review Purpose

The first tranche intentionally prioritizes architecture stress over coverage. The rc04 focused closure review should confirm the four localized trace fixes and regress the original architecture stress points:

- whether `SUP` patterns preserve the distinction between observation/supervision and project health/recovery authority;
- whether `REC` remains bounded and does not become an implementation retry policy;
- whether `SCAF-PAT-COM-001` can remain one COM identity while accurately cross-tracing ROB/CFG/RUN and later composing with SYN mechanisms;
- whether `PST` describes atomicity/authority without storage-layout creep;
- whether `LCM` separates transfer, commit, activation, rollback and RUN readiness;
- whether `EVD` preserves incident chronology/survivability without promoting recorder-specific donor implementation details.

## 5. Expansion Gate

Do not promote these entries to `Available`, advance them to M2, or add a broad second tranche until the focused rc04 closure review confirms `R3-01` through `R3-04` resolved, finds no blocking regression, and reconfirms the frozen v0.0.2 authority baseline.
