# SCAF L3 Pattern Index

**Development Release:** v0.0.3rc07  
**Status:** Navigation index; not trace authority

## 1. Current Catalog State

v0.0.3rc07 carries forward exactly the same **seven published pattern identities** as `Available / M2` after the independent rc06 availability-acceptance review returned `INITIAL L3 PATTERN-AVAILABILITY ACCEPTANCE GATE: YES` with 7 / 7 acceptance-valid and 7 / 7 pattern-body non-regression results.

rc07 performs no lifecycle change. It adds a descriptive trace-reference coverage audit and plans a small second tranche without allocating any new Pattern ID.

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


## 4. rc07 Coverage / Planning Position

The rc06 independent review closed the initial seven-pattern availability milestone. All seven current entries remain `Available / M2` with unchanged identity/family and architecture content.

The new planning authority for this RC is `06_L3_Catalog_Coverage_and_Second_Tranche_Planning.md`. Its numeric trace-reference coverage view is descriptive only and is not a compliance, satisfaction or completeness score.

## 5. Expansion Gate

No expansion occurs in rc07. A later RC may allocate a small second tranche only after the independent rc07 coverage/planning review passes. M3/M4 maturity, L4 guidance, machine-readable schema, validator, generated registry/index, CI, code generation and executable governance remain separately gated.
