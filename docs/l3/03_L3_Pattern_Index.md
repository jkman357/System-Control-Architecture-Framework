# SCAF L3 Pattern Index

**Development Release:** v0.0.3rc01  
**Status:** Navigation / planning index; not trace authority

## 1. Current Catalog State

v0.0.3rc01 intentionally contains **zero instantiated `SCAF-PAT-*` patterns**.

The purpose of this RC is to stabilize the catalog architecture, metadata, trace and selection semantics before bulk content is authored.

## 2. Mechanism Families

| Family | Name | Current Pattern Count | Development Priority |
|---|---|---:|---|
| `SUP` | Supervision & Detection | 0 | First tranche |
| `COM` | Interaction Resilience | 0 | First tranche |
| `REC` | Recovery & Reintegration | 0 | First tranche |
| `FTL` | Fault Tolerance & Isolation | 0 | Later |
| `TIM` | Timing & Capacity Realization | 0 | Later |
| `PST` | Persistent State Integrity | 0 | First tranche |
| `LCM` | Lifecycle Management | 0 | First tranche |
| `EVD` | Evidence & Incident Recording | 0 | First tranche |
| `SYN` | Distributed Consistency & Reconciliation | 0 | Later |
| `SEC` | Security Realization | 0 | Later / controlled expansion |

## 3. Representative First-Tranche Candidates

The following are planning candidates only. They are **not pattern IDs, not accepted pattern names and not catalog entries in this release**.

- heartbeat / liveness supervision;
- independent watchdog escalation;
- bounded retry with escalation;
- reconnect plus state reconciliation;
- atomic dual-copy persistent state;
- transactional update plus rollback;
- retained incident evidence;
- pre/post-trigger evidence ring.

These candidates should be used first to stress-test the L3 contract because they cross ROB/TIME/OBS/INT/LIFE/CFG boundaries and expose whether the model preserves multiple valid mechanisms.

## 4. Expansion Gate

Do not allocate the first `SCAF-PAT-*` IDs until independent review confirms that:

- the family taxonomy is stable enough for initial use;
- metadata fields are sufficient without creating implementation overreach;
- L2 trace is many-to-many and does not imply satisfaction;
- Project Design Authority remains the project selection authority;
- pattern alternatives and project-specific mechanisms remain permitted;
- L3/L4 separation is clear.
