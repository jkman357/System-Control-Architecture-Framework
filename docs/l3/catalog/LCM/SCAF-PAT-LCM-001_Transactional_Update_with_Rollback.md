# SCAF-PAT-LCM-001 — Transactional Update with Rollback

**Development Release:** v0.0.3rc04  
**Pattern Family:** `LCM` — Lifecycle Management  
**Pattern Kind:** Composite Pattern  
**Catalog Status:** Candidate  
**Maturity:** M1 — Structured  
**Introduced In:** v0.0.3rc03

## Metadata

| Field | Value |
|---|---|
| Pattern ID | `SCAF-PAT-LCM-001` |
| Pattern Name | Transactional Update with Rollback |
| Pattern Family | `LCM` |
| Pattern Kind | Composite Pattern |
| Catalog Status | Candidate |
| Maturity | M1 — Structured |
| Introduced In | v0.0.3rc03 |
| Primary L2 Trace | `SCAF-LIFE-015`, `SCAF-LIFE-017` |
| Supporting L2 Trace | `SCAF-LIFE-012`, `SCAF-LIFE-014`, `SCAF-LIFE-016`, `SCAF-LIFE-018`, `SCAF-LIFE-020`, `SCAF-LIFE-021`, `SCAF-CFG-021` |
| Constraint Inputs | `SCAF-CFG-008`, `SCAF-CFG-009`, `SCAF-CFG-010`, `SCAF-RUN-009`, applicable `SCAF-SEC-010`, `SCAF-SEC-022` |
| Profile Facets | Firmware/software/programmable-logic/configuration-bearing image; single or multi-participant lifecycle transaction |
| Provenance / Reference Basis | Frozen SCAF obligation-derived architecture synthesis; no A/B partition or bootloader implementation is mandated |

## 1. Intent

Treat update/activation as a controlled lifecycle transaction that either establishes a valid new lifecycle result or retains/restores an eligible prior result, with explicit interruption and rollback semantics.

## 2. Problem

A partially applied update can leave an unusable or internally inconsistent realization. Activation can fail after content transfer succeeds, and rollback can itself be unsafe or incompatible if eligibility is not controlled. Treating “image written” as “update successful” conflates transfer, commit, activation, readiness and rollback results.

## 3. Applicability

Consider this pattern where:

- partial update can materially damage lifecycle correctness or Service availability;
- a prior or alternate eligible realization can be retained/restored;
- update preconditions, commit, activation and rollback can be represented as distinct controlled results;
- interruption/power/reset/communication loss is a material lifecycle condition.

## 4. Non-Applicability / Cautions

Rollback may be impossible or prohibited when data/configuration migration is irreversible, security policy forbids older versions, hardware compatibility changes, or external authority requires forward-only transition. The pattern does not assume that every project must retain two complete images.

## 5. L2 Trace

### 5.1 Primary Realization Candidate

- `SCAF-LIFE-015` — structures update as a transaction with controlled atomicity/consistency, commit/completion and abort/interruption results.
- `SCAF-LIFE-017` — provides explicit rollback eligibility, completion/failure and consequence semantics.

### 5.2 Supporting Realization

- `SCAF-LIFE-012` — update scope and authoritative transaction/result responsibility remain project-defined.
- `SCAF-LIFE-014` — update proceeds only after controlled source preconditions are established.
- `SCAF-LIFE-016` — activation remains a distinct controlled result from transfer/commit.
- `SCAF-LIFE-018` — interruption/resume/restart uses controlled continuation eligibility.
- `SCAF-LIFE-020` — failed/incomplete lifecycle results hand off to ROB rather than embedding resilience policy inside the update transaction.
- `SCAF-LIFE-021` — material lifecycle result/identity can be observed for recovery/correlation.
- `SCAF-CFG-021` — configuration/version/migration inputs consumed by update retain CFG authority.

### 5.3 Constraint Inputs

- `SCAF-CFG-008` — version identity/compatibility constrains update eligibility.
- `SCAF-CFG-009` — migration semantics constrain whether update/rollback can establish a valid CFG result.
- `SCAF-CFG-010` — atomic persistent CFG changes may need coordination with lifecycle commit.
- `SCAF-RUN-009` — where lifecycle completion/activation does not itself establish operational readiness, the project-defined LIFE-to-RUN handoff condition constrains when the updated realization may enter the applicable RUN readiness/operational state; LIFE retains update/activation result authority and RUN retains readiness-state semantics.
- `SCAF-SEC-010` — where authenticity/integrity is required, the security result constrains lifecycle eligibility.
- `SCAF-SEC-022` — security authorization/trust/integrity inputs constrain security-sensitive lifecycle transactions without transferring LIFE authority.

## 6. Required PDA Decisions

- update transaction scope and lifecycle result authority;
- update source/version/compatibility/security eligibility;
- staging/preparation boundary and authoritative commit point;
- activation criteria and relationship to RUN readiness;
- interruption resume/restart policy and continuation basis;
- rollback eligibility, target version/state and completion criteria;
- migration/configuration coordination and whether rollback remains semantically possible;
- behavior if neither new nor prior realization can establish a valid lifecycle result;
- multi-participant coordination where applicable;
- evidence/identity required to diagnose interrupted update, activation or rollback.

## 7. Mechanism Summary

The update is represented as a sequence of controlled lifecycle phases: establish preconditions and source eligibility; prepare/stage the candidate realization; establish transaction commit/completion according to the project atomicity basis; activate the candidate when its activation criteria are met; evaluate resulting lifecycle state; and invoke rollback only when rollback is explicitly eligible.

Interruption is a first-class transaction condition. On restart/resume, lifecycle logic determines whether the prepared candidate, prior result or another controlled recovery path is eligible. Update success is not inferred solely from transfer completion, and lifecycle activation is not automatically equivalent to RUN readiness.

## 8. Variants

- retained previous realization with staged candidate;
- copy-on-write/replacement transaction over update artifact;
- update transaction coordinated with configuration migration checkpoint;
- multi-participant staged update with controlled activation barrier;
- forward-recovery variant where rollback is prohibited but an alternate recovery realization exists.

## 9. Forces / Tradeoffs

- rollback availability versus storage/resource cost;
- strong transaction consistency versus update duration/complexity;
- independent activation versus faster deployment;
- compatibility/migration flexibility versus rollback complexity;
- multi-participant atomicity versus availability during rollout.

## 10. Failure / Weakness Modes

- candidate is activated before transaction/validity criteria are established;
- rollback target is incompatible with migrated configuration/state;
- authenticity/security eligibility is confused with lifecycle completion;
- repeated failed activation causes boot/update loop;
- interrupted update loses which candidate/result is authoritative;
- partial multi-participant update resumes coordinated Service prematurely;
- rollback succeeds at image level but required RUN readiness cannot be established.

## 11. Selection Consequences

Selection requires persistent lifecycle transaction identity/state, explicit commit/activation/rollback semantics and coordination with configuration/security/ROB/RUN authorities. It may require retained prior realization capacity and incident evidence across reset/boot.

## 12. Composition Relations

### Requires

- controlled update eligibility, lifecycle transaction/result authority and version/compatibility basis.

### Commonly Composed With

- `SCAF-PAT-PST-001` — Atomic Dual-Copy Persistent State for transaction/configuration metadata where appropriate;
- `SCAF-PAT-REC-001` — Bounded Retry with Escalation for bounded update/recovery attempts;
- `SCAF-PAT-EVD-001` — Pre/Post-Trigger Retained Incident Evidence Ring for interrupted/failed lifecycle evidence.

### Alternative To

- forward-only transactional update mechanisms where rollback is intentionally inapplicable but an equivalent controlled failure/recovery basis exists.

### Conflicts With

- update flows that treat successful data transfer or file write as automatic activation/readiness.

### Subsumes

- None.

### Supersedes

- None.

## 13. External Authority Considerations

Security Authority may constrain update authenticity, anti-rollback, authorization or version eligibility. Safety/regulatory/risk authority may constrain update availability, rollback permissibility, controlled maintenance states or evidence retention. Those constraints remain source-authority inputs.

## 14. Re-evaluation Triggers

Re-evaluate when updateable component scope, storage model, version/migration policy, security eligibility, boot/activation architecture, rollback permissibility, multi-participant coordination or RUN readiness relationship changes.

## 15. Provenance / Reference Basis

SCAF-new synthesis of frozen LIFE/CFG/SEC/ROB obligations. The pattern deliberately remains above A/B slot, bootloader, package, signature algorithm or vendor updater implementation.

## 16. L3 / L4 Boundary Note

L3 does not prescribe image-slot count, partition map, bootloader commands, package format, signature algorithm, flash write sequence, update protocol, rollback counter implementation, code or verification test steps.
