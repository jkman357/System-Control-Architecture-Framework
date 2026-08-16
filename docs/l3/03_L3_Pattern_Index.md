# SCAF L3 Pattern Index

**Development Release:** v0.0.3rc06  
**Status:** Navigation index; not trace authority

## 1. Current Catalog State

v0.0.3rc06 carries forward exactly the same **seven published pattern identities** and records the explicit catalog acceptance decision after the rc05 lifecycle review validated **7 / 7 M2** and judged **7 / 7 READY FOR AVAILABLE**. Every entry is now `Catalog Status: Available` and remains `M2 — Architecture Reviewed`.

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


## 4. rc06 Availability-Acceptance Position

The rc05 independent lifecycle review validated all seven M2 states and independently recommended all seven entries as `READY FOR AVAILABLE`. v0.0.3rc06 records the separate catalog-maintainer acceptance decision without changing maturity or pattern architecture.

`Available` means accepted for project consideration. It does not mean universally recommended, automatically applicable, selected by a project, compliant, verified, or sufficient for L2 satisfaction.

## 5. Expansion Gate

The initial seven-pattern availability transition is the only catalog expansion/lifecycle action in rc06. A second pattern tranche, M3/M4 maturity, L4 guidance, machine-readable schema, validator, generated registry/index, CI, code generation and executable governance remain separately gated.
