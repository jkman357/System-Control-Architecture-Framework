# SCAF-PAT-PST-001 — Atomic Dual-Copy Persistent State

**Development Release:** v0.0.3rc09  
**Pattern Family:** `PST` — Persistent State Integrity  
**Pattern Kind:** Mechanism  
**Catalog Status:** Available  
**Maturity:** M2 — Architecture Reviewed  
**Introduced In:** v0.0.3rc03

## Metadata

| Field | Value |
|---|---|
| Pattern ID | `SCAF-PAT-PST-001` |
| Pattern Name | Atomic Dual-Copy Persistent State |
| Pattern Family | `PST` |
| Pattern Kind | Mechanism |
| Catalog Status | Available |
| Maturity | M2 — Architecture Reviewed |
| Introduced In | v0.0.3rc03 |
| Primary L2 Trace | `SCAF-CFG-010`, `SCAF-CFG-013` |
| Supporting L2 Trace | `SCAF-CFG-003`, `SCAF-CFG-004`, `SCAF-CFG-006`, `SCAF-CFG-008`, `SCAF-CFG-012` |
| Constraint Inputs | `SCAF-LIFE-010`, `SCAF-TIME-011` where storage/resource budget is material |
| Profile Facets | NVM, filesystem, database-like persistence or other durable storage with distinguishable candidate copies/versions |
| Provenance / Reference Basis | Frozen SCAF obligation-derived architecture synthesis; dual-copy mechanism explicitly left to L3 by `SCAF-CFG-010`/`SCAF-CFG-038` |

## 1. Intent

Provide a technology-neutral persistent-state mechanism that preserves at least one previously valid authoritative state while a new candidate state is being written and establishes the new state only through a controlled commit/selection rule.

## 2. Problem

An interrupted or partially completed persistent write can leave a single stored state corrupt, ambiguous or internally inconsistent. If startup/load logic treats physical presence as authority, the system may consume an incomplete candidate or lose the last known valid state.

## 3. Applicability

Consider this pattern where:

- partial/interrupted persistent-state change can create a materially unusable result;
- storage can represent two distinguishable candidate copies/versions or equivalent isolated commit candidates;
- the project can define validity, generation/version and authoritative-selection semantics;
- preserving a prior valid state is useful for recovery or rollback.

## 4. Non-Applicability / Cautions

The pattern may be insufficient where both copies share a common destructive failure, corruption is systematic and identically reproduced, storage capacity/wear is unacceptable, or true multi-object transaction semantics require a broader journal/database mechanism.

Two physical copies do not by themselves establish semantic validity or authority.

## 5. L2 Trace

### 5.1 Primary Realization Candidate

- `SCAF-CFG-010` — provides a dual-candidate architecture for controlled atomic/consistent commit semantics without prescribing a storage technology.
- `SCAF-CFG-013` — provides a controlled basis to select/restorably retain a valid source state when one copy is incomplete, corrupt or unavailable.

### 5.2 Supporting Realization

- `SCAF-CFG-003` — requires the project to define the responsibility/rule that establishes the authoritative resulting value rather than treating an address as authority.
- `SCAF-CFG-004` — copy identity/generation/provenance prevents physical location alone from defining semantic identity.
- `SCAF-CFG-006` — each candidate must be evaluated against project-defined validity criteria.
- `SCAF-CFG-008` — version/compatibility identity can be carried with each candidate where interpretation depends on version.
- `SCAF-CFG-012` — retaining a prior valid copy can support project-defined CFG rollback eligibility/results.

### 5.3 Constraint Inputs

- `SCAF-LIFE-010` — after reset/boot/update, retained copies are consumed only if lifecycle-transition eligibility and source validity are established.
- `SCAF-TIME-011` — storage capacity, wear/endurance, write bandwidth or other finite resource budget may constrain use.

## 6. Required PDA Decisions

- semantic identity of the persistent state and authoritative source responsibility;
- validity/integrity criteria for each candidate copy;
- generation/version/commit-state representation and ordering semantics;
- authoritative selection rule when both, one or neither copy is valid;
- candidate-write and commit/promotion sequence at architecture level;
- behavior after interrupted commit, ambiguous generation or corruption of both copies;
- rollback/retention policy for the previous valid state;
- lifecycle consumption eligibility and migration/version compatibility;
- storage endurance/capacity/resource constraints.

## 7. Mechanism Summary

Two distinguishable persistent candidates are maintained for the same semantic state. A change is prepared in the non-authoritative/inactive candidate while the current authoritative candidate remains valid. The new candidate becomes eligible for authority only after the project-defined content validity and commit metadata/state are established. Load/recovery logic evaluates both candidates and applies the project-defined authority rule using validity, version/generation and commit state rather than storage location alone.

The mechanism preserves a recoverable prior state across an interrupted candidate write, subject to the project's common-mode and storage-failure assumptions.

## 8. Variants

- alternating A/B copies with monotonic generation identity;
- active/inactive candidate with explicit promotion marker;
- copy-on-write file/object replacement with two distinguishable durable candidates;
- dual records where commit metadata is separated from candidate content.

## 9. Forces / Tradeoffs

- stronger interrupted-write resilience versus doubled/extra storage;
- richer validity metadata versus complexity;
- more durable commit sequencing versus write latency/wear;
- retained rollback capability versus storage lifecycle management;
- simple two-copy selection versus multi-object consistency limitations.

## 10. Failure / Weakness Modes

- both copies corrupted by common-mode storage/power/software error;
- generation/version comparison becomes ambiguous;
- invalid candidate is promoted because validity check is incomplete;
- previous valid copy is overwritten too early;
- selection logic treats physical slot as authority;
- lifecycle/version migration changes semantics without updating eligibility;
- write endurance or resource limits invalidate assumed availability.

## 11. Selection Consequences

Selection requires explicit copy identity, validity, generation, commit and startup-selection semantics and consumes additional persistent storage/write budget. Recovery behavior must define what occurs when no valid authoritative candidate can be established.

## 12. Composition Relations

### Requires

- project-defined CFG source authority, validity and commit semantics.

### Commonly Composed With

- `SCAF-PAT-LCM-001` — Transactional Update with Rollback;
- `SCAF-PAT-COM-001` — Reconnect plus State Reconciliation where persistent replicas are exchanged;
- `SCAF-PAT-EVD-001` — incident evidence for commit/corruption failures where diagnostically material.

### Alternative To

- journaled/transactional storage, append-only log or database transaction mechanisms that establish the same required atomicity property.

### Conflicts With

- single-copy overwrite treated as atomic where the storage/transaction model does not establish that guarantee.

### Subsumes

- None.

### Supersedes

- None.

## 13. External Authority Considerations

Safety/security/regulatory sources may constrain persistence integrity, rollback eligibility, security authenticity, retention, auditability or failure consequence. Those source constraints are not created by this pattern.

## 14. Re-evaluation Triggers

Re-evaluate when storage technology/failure model, state size, update frequency, validity/version semantics, lifecycle transitions, migration policy, write endurance, atomic-write guarantees or authoritative-source decisions change.

## 15. Provenance / Reference Basis

SCAF-new synthesis from frozen CFG/LIFE/TIME obligations. The L2 baseline explicitly names dual-copy as an example of a realization that L1/L2 does not mandate; this entry supplies that mechanism at L3 without prescribing layout or API.

## 16. L3 / L4 Boundary Note

L3 does not define sector/page addresses, file names, binary record layout, checksum/CRC algorithm, generation bit width, flash erase sequence, database product, write API, power-fail timing procedure or test vectors.
