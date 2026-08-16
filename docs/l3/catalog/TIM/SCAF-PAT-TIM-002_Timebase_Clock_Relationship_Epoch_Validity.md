# SCAF-PAT-TIM-002 — Timebase / Clock-Relationship / Epoch Validity

**Development Release:** v0.0.3rc11  
**Pattern Family:** `TIM` — Timing & Capacity Realization  
**Pattern Kind:** Mechanism  
**Catalog Status:** Available  
**Maturity:** M2 — Architecture Reviewed  
**Introduced In:** v0.0.3rc08

## Metadata

| Field | Value |
|---|---|
| Pattern ID | `SCAF-PAT-TIM-002` |
| Pattern Name | Timebase / Clock-Relationship / Epoch Validity |
| Pattern Family | `TIM` |
| Pattern Kind | Mechanism |
| Catalog Status | Available |
| Maturity | M2 — Architecture Reviewed |
| Introduced In | v0.0.3rc08 |
| Primary L2 Trace | `SCAF-TIME-004`, `SCAF-TIME-020` |
| Supporting L2 Trace | `SCAF-TIME-002`, `SCAF-TIME-003`, `SCAF-TIME-005` |
| Constraint Inputs | applicable `SCAF-INT-008`, `SCAF-RUN-021`, `SCAF-ROB-004` |
| Profile Facets | Single-/multi-clock MCU/SoC/FPGA/PC/distributed systems; monotonic, wall-clock, synchronized and restartable epoch relationships |
| Provenance / Reference Basis | Frozen SCAF TIME/INT/RUN/ROB obligations plus rc07 second-tranche planning review approval; SCAF-new technology-neutral synthesis |

## 1. Intent

Represent and qualify whether a relied-upon relationship among clocks/timebases/time domains is currently usable, uncertain, invalid or newly established, so dependent temporal claims cannot silently survive clock drift, restart, epoch change or synchronization loss.

## 2. Problem

Systems often carry timestamps or elapsed-time values across multiple clocks and assume they remain comparable. A restart can reset a monotonic counter; wall-clock can jump; synchronization can be lost; offsets and uncertainty can exceed the bound required by freshness or ordering claims. Without an explicit relationship-validity mechanism, downstream logic can continue using numerically plausible but semantically incomparable time values.

## 3. Applicability

Consider this pattern where:

- correctness depends on comparing/ordering values from different clocks/timebases or time domains;
- synchronization/drift/offset uncertainty can become unusable;
- clock/timebase origin can restart or change;
- downstream freshness, readiness, consistency or health claims depend on the relationship;
- the project can define a relationship identity/epoch and usability criterion.

## 4. Non-Applicability / Cautions

This pattern may be unnecessary where all relevant temporal claims use one authoritative monotonic timebase and no relationship to another clock/domain is relied upon. It does not make wall-clock suitable for elapsed-time logic and does not make synchronized clocks perfectly simultaneous.

The mechanism qualifies a relationship; it does not own the downstream INT/RUN/ROB consequence when that relationship is unusable.

## 5. L2 Trace

### 5.1 Primary Realization Candidate

- `SCAF-TIME-004` — realizes a reusable way to track synchronization/drift/offset/uncertainty relationship and its usability state.
- `SCAF-TIME-020` — directly realizes explicit validity/degraded/re-evaluation state for temporal claims when a required clock relationship is lost or becomes unusable.

### 5.2 Supporting Realization

- `SCAF-TIME-002` — carries explicit timebase/clock identity and authority into relationship qualification.
- `SCAF-TIME-003` — prevents monotonic elapsed-time and wall-clock semantics from being substituted without an explicit controlled relationship.
- `SCAF-TIME-005` — uses Time Domain / Time Epoch identity to prevent values from incompatible origins/incarnations being compared as if continuous.

### 5.3 Constraint Inputs

- `SCAF-INT-008` — where an Interaction freshness state depends on the relationship, INT owns the current/stale/expired/invalid contract consequence.
- `SCAF-RUN-021` — where cross-participant RUN consistency depends on measurable synchronization/age, RUN traces to the applicable TIME decision rather than absorbing TIME authority.
- `SCAF-ROB-004` — where relationship loss is an input to health/failure classification, ROB owns the resulting health decision; TIM only supplies the controlled temporal validity result.

## 6. Required PDA Decisions

- relevant timebase/clock identities and authorities;
- monotonic versus wall-clock usage rules;
- Time Domain / Time Epoch identity and restart/change semantics;
- required offset/drift/uncertainty relationship and usable/unusable criteria;
- how relationship quality is measured or established;
- dependent temporal claims and whether each becomes invalid, degraded or requires re-evaluation;
- downstream INT/RUN/ROB consequence for unusable relationship;
- re-establishment criteria after restart, resynchronization or source change;
- evidence needed to diagnose clock-relationship loss or ambiguity.

## 7. Mechanism Summary

The mechanism maintains a controlled **clock-relationship state** that binds:

- the participating timebase identities;
- their applicable time-domain/epoch/incarnation identity;
- measured or established offset/drift/uncertainty information;
- a project-defined usability classification.

A temporal consumer does not rely only on a numeric timestamp. It also requires the applicable relationship state/epoch to be valid for the claim being made. When synchronization is lost, uncertainty exceeds the permitted basis, or an epoch changes, dependent claims are invalidated, degraded or marked for controlled re-evaluation according to the project decision.

Re-establishment creates or validates a new relationship/epoch rather than silently continuing the old one.

## 8. Variants

- one authoritative clock with qualified offset mappings for participant clocks;
- peer clock relationship with explicit uncertainty bound;
- monotonic local time plus separately qualified wall-clock mapping;
- generation/epoch-tagged timestamp sets after restart;
- holdover/degraded relationship state with increased uncertainty until resynchronization.

## 9. Forces / Tradeoffs

- tighter temporal confidence versus synchronization traffic/measurement cost;
- availability during clock loss versus conservative invalidation of dependent claims;
- high-resolution timestamps versus wrap/epoch/uncertainty management complexity;
- centralized time authority versus dependency on a common source;
- holdover continuity versus growing uncertainty.

## 10. Failure / Weakness Modes

- different time domains share the same numeric value but are treated as comparable;
- monotonic counter restart is mistaken for continuation;
- wall-clock adjustment corrupts elapsed-time assumptions;
- synchronization quality degrades without invalidating dependent freshness/order claims;
- stale relationship metadata survives a participant/session restart;
- uncertainty is omitted from a claim that relies on clock agreement;
- the time authority becomes a common-mode dependency without controlled consequence.

## 11. Selection Consequences

Selection requires explicit clock/timebase/epoch identities, relationship-quality state and dependency tracing from temporal claims to that state. It may require downstream contract/readiness/health states for unusable time relationships, but those semantics remain owned by INT/RUN/ROB.

## 12. Composition Relations

### Requires

- controlled timebase identities and project-defined relationship usability criteria.

### Commonly Composed With

- `SCAF-PAT-SUP-001` where liveness/freshness evidence depends on time;
- `SCAF-PAT-COM-001` where reconnect reconciliation uses age or chronological ordering;
- `SCAF-PAT-SYN-001` where convergence eligibility depends on freshness or epoch;
- `SCAF-PAT-EVD-001` where incident evidence spans multiple clocks/time domains.

### Alternative To

- designs that constrain all relevant temporal claims to one authoritative monotonic timebase and require no cross-clock relationship.

### Conflicts With

- implicit timestamp comparability without timebase/epoch identity or relationship validity.

### Subsumes

- None.

### Supersedes

- None.

## 13. External Authority Considerations

Safety/security/regulatory/risk authorities may constrain maximum acceptable timestamp uncertainty, freshness confidence, audit-time requirements, trusted time sources or permitted operation when time relationship is unavailable.

## 14. Re-evaluation Triggers

Re-evaluate when clock source, synchronization architecture, oscillator/time service, restart model, wall-clock adjustment behavior, timestamp representation, freshness/ordering requirements or cross-participant consistency requirements change.

## 15. Provenance / Reference Basis

SCAF-new synthesis of frozen TIME/INT/RUN/ROB obligations. The rc07 independent planning review approved the category specifically as a **clock-relationship qualification/validity mechanism**, not a restatement of TIME obligations or prescription of a synchronization protocol.

## 16. L3 / L4 Boundary Note

This pattern does not prescribe PTP/NTP/GPS/RTC technology, synchronization packet format, oscillator type, PLL, timestamp counter width, clock API, drift estimator, servo algorithm, poll interval, exact uncertainty value or verification procedure.
