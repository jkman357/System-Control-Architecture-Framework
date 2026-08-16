# SCAF-PAT-COM-001 — Reconnect plus State Reconciliation

**Development Release:** v0.0.3rc04  
**Pattern Family:** `COM` — Interaction Resilience  
**Pattern Kind:** Composite Pattern  
**Catalog Status:** Candidate  
**Maturity:** M1 — Structured  
**Introduced In:** v0.0.3rc03

## Metadata

| Field | Value |
|---|---|
| Pattern ID | `SCAF-PAT-COM-001` |
| Pattern Name | Reconnect plus State Reconciliation |
| Pattern Family | `COM` |
| Pattern Kind | Composite Pattern |
| Catalog Status | Candidate |
| Maturity | M1 — Structured |
| Introduced In | v0.0.3rc03 |
| Primary L2 Trace | `SCAF-ROB-013`, `SCAF-INT-010` |
| Supporting L2 Trace | `SCAF-ROB-012`, `SCAF-CFG-019`, `SCAF-RUN-010` |
| Constraint Inputs | `SCAF-INT-007`, `SCAF-INT-008`, `SCAF-INT-010`, `SCAF-CFG-018`, `SCAF-CFG-019`, `SCAF-RUN-011`, applicable `SCAF-TIME-007` |
| Profile Facets | Distributed/multi-participant Interaction; reconnectable transport/session; replicated/cached operational or configuration state |
| Provenance / Reference Basis | Frozen SCAF obligation-derived architecture synthesis; intentionally used to stress COM/REC/SYN cross-family boundaries |

## 1. Intent

Restore coordinated operation after communication loss/reconnection without treating transport reconnection alone as proof that participants have mutually valid, current and consistent state.

## 2. Problem

During a partition or disconnect, participants may continue independently, restart, change configuration, queue commands, expire data or lose ownership assumptions. When connectivity returns, immediately resuming normal traffic can replay stale commands, overwrite newer state, combine incompatible incarnations or create ambiguous authority.

## 3. Applicability

Consider this pattern where:

- participants can disconnect and later reconnect;
- either side can change state, restart or accumulate stale/cached information while disconnected;
- normal coordinated operation depends on establishing compatible session/incarnation and authoritative state relationships;
- the project can define reconciliation eligibility and completion criteria.

## 4. Non-Applicability / Cautions

Simple reconnect may be sufficient where no material state/ownership can diverge and all post-connect information is independently authoritative/current. This pattern is not a consensus algorithm and does not define a universal distributed consistency model.

## 5. L2 Trace

### 5.1 Primary Realization Candidate

- `SCAF-ROB-013` — directly addresses resilience consequences of partition/reconnect before normal coordinated operation resumes.
- `SCAF-INT-010` — uses explicit protocol/connection session identity/generation to distinguish old and new exchange contexts.

### 5.2 Supporting Realization

- `SCAF-ROB-012` — provides a reusable reintegration/re-synchronization sequence with controlled eligibility criteria.
- `SCAF-CFG-019` — can reconcile stale/divergent configuration or persistent-state replicas after partition/reconnect.
- `SCAF-RUN-010` — can restore the project-defined cross-participant operational-state consistency relationship before coordinated operation resumes.

### 5.3 Constraint Inputs

- `SCAF-INT-007` — duplicate, missing, reordered or superseded information semantics constrain reconciliation.
- `SCAF-INT-008` — current/stale/expired/invalid contract states constrain what can be accepted after reconnect.
- `SCAF-INT-010` — session generation/identity determines whether retained exchanges belong to the current connection context.
- `SCAF-CFG-018` — authoritative source/result and permitted disagreement constrain configuration reconciliation.
- `SCAF-CFG-019` — stale-replica/reconnect consequences constrain acceptance of persisted/cached CFG state.
- `SCAF-RUN-011` — operational incarnation/generation constrains whether runtime state belongs to the current operational instance.
- `SCAF-TIME-007` — where freshness is time-based, project-defined age evaluation constrains reconciliation eligibility.

## 6. Required PDA Decisions

- what state/ownership/commands may diverge while disconnected;
- session and operational incarnation identities used during reconnect;
- authoritative source/responsibility for each reconciled state class;
- stale/duplicate/reordered data treatment;
- permitted divergence and reconciliation eligibility criteria;
- conflict resolution/precedence where both sides changed materially;
- whether queued operations are replayed, discarded, revalidated or transformed;
- completion criterion before normal coordinated operation resumes;
- behavior when reconciliation cannot establish a valid result;
- evidence needed to diagnose reconnect/reconciliation failure.

## 7. Mechanism Summary

The reconnect sequence establishes a **new or explicitly validated session context**, exchanges the identities/versions/state summaries needed to evaluate compatibility, classifies retained/queued information against the current session/incarnation and source authority, then executes a controlled reconciliation step. Normal coordinated operation resumes only after the project-defined reconciliation completion/eligibility criteria are established.

Transport connectivity is therefore treated as a prerequisite, not the final proof of coordinated readiness.

The primary family is `COM` because the reusable mechanism intent is the controlled re-establishment of a valid Interaction relationship after reconnection. The pattern cross-traces ROB/CFG/RUN obligations rather than duplicating separate REC or SYN identities.

## 8. Variants

- authoritative-side resync where one participant is the clear source of current state;
- version/generation comparison followed by selective transfer;
- discard-and-rebuild of non-authoritative caches;
- explicit conflict resolution when multiple sources can change;
- staged reconciliation where safety/security-critical state is established before lower-priority state.

## 9. Forces / Tradeoffs

- fast reconnect versus stronger validation/reconciliation;
- retained offline autonomy versus conflict complexity;
- bandwidth/startup latency versus full state comparison;
- source authority simplicity versus multi-writer flexibility;
- availability during partition versus risk of divergent decisions.

## 10. Failure / Weakness Modes

- old queued command is replayed into a new session/incarnation;
- reconnect transport success is mistaken for synchronized state;
- both peers claim authority without controlled conflict resolution;
- state version/generation wraps or is reused ambiguously;
- time-based freshness is trusted after clock relationship loss;
- reconciliation partially completes but normal operation resumes prematurely;
- repeated disconnect/reconnect creates a reconciliation storm.

## 11. Selection Consequences

Selection requires explicit session/incarnation identities, state-authority rules, reconciliation states and a normal-operation eligibility gate. It can also require additional bandwidth, retained metadata and project evidence for unresolved reconciliation.

## 12. Composition Relations

### Requires

- controlled session identity and authoritative state semantics for the reconciled information.

### Commonly Composed With

- `SCAF-PAT-REC-001` — Bounded Retry with Escalation;
- `SCAF-PAT-PST-001` — Atomic Dual-Copy Persistent State where locally persisted state participates;
- `SCAF-PAT-EVD-001` — Pre/Post-Trigger Retained Incident Evidence Ring.

### Alternative To

- project architectures that deliberately discard all disconnected-session state and reconstruct from a single authoritative source after reconnect.

### Conflicts With

- transparent reconnect that preserves stale queues/state without session/incarnation validation.

### Subsumes

- None.

### Supersedes

- None.

## 13. External Authority Considerations

Applicable safety/security/regulatory/risk authority may constrain offline autonomy, command replay, freshness, security re-authentication, permissible degraded operation or reconciliation completion before Service resumes.

## 14. Re-evaluation Triggers

Re-evaluate when session semantics, transport behavior, participant restart model, state-authority ownership, multi-writer policy, offline capability, freshness rules, configuration replication or operational-state consistency requirements change.

## 15. Provenance / Reference Basis

SCAF-new synthesis of frozen INT/ROB/CFG/RUN/TIME obligations. The entry intentionally demonstrates that a cross-cutting mechanism can retain one primary family/identity while tracing several frozen concern authorities.

## 16. L3 / L4 Boundary Note

This pattern does not prescribe a consensus protocol, leader election, two-phase commit, message schema, database replication product, retransmission algorithm, reconnect timeout, sequence-number width or verification sequence.
