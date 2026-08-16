# SCAF-PAT-SYN-001 — Generation/Epoch-Based Cross-Participant State Convergence

**Development Release:** v0.0.3rc13  
**Pattern Family:** `SYN` — Distributed Consistency & Reconciliation  
**Pattern Kind:** Composite Pattern  
**Catalog Status:** Available  
**Maturity:** M2 — Architecture Reviewed  
**Introduced In:** v0.0.3rc08

## Metadata

| Field | Value |
|---|---|
| Pattern ID | `SCAF-PAT-SYN-001` |
| Pattern Name | Generation/Epoch-Based Cross-Participant State Convergence |
| Pattern Family | `SYN` |
| Pattern Kind | Composite Pattern |
| Catalog Status | Available |
| Maturity | M2 — Architecture Reviewed |
| Introduced In | v0.0.3rc08 |
| Primary L2 Trace | `SCAF-CFG-018`, `SCAF-RUN-010` |
| Supporting L2 Trace | `SCAF-CFG-019`, `SCAF-RUN-011`, `SCAF-ROB-012` |
| Constraint Inputs | `SCAF-INT-007`, `SCAF-INT-010`, `SCAF-RUN-021`; applicable `SCAF-TIME-007`, `SCAF-SEC-025` |
| Profile Facets | Multi-participant systems with replicated/cached configuration or operational state, intermittent connectivity, restartable participants or asynchronous update propagation |
| Provenance / Reference Basis | Frozen SCAF CFG/RUN/INT/ROB/TIME/SEC obligations plus rc07 second-tranche planning review approval; SCAF-new technology-neutral synthesis |

## 1. Intent

Drive related state held by multiple participants toward a project-defined consistent/eligible result using explicit generation/epoch/incarnation identity and controlled authority rules, without requiring reconnect as the trigger and without prescribing consensus, leader election or a replication product.

## 2. Problem

Participants may cache, replicate or independently observe related state. Updates can be delayed, duplicated or reordered; participants can restart; old replicas can reappear; two sources can disagree. Transport connectivity alone does not establish that the participants have converged on the state that is authoritative for current operation.

`SCAF-PAT-COM-001` addresses re-establishing a valid Interaction relationship after reconnect. A separate convergence mechanism is needed when state consistency is itself reusable and may be invoked after reconnect, startup, source change, delayed propagation, participant replacement or periodic reconciliation.

## 3. Applicability

Consider this pattern where:

- multiple participants depend on common or related configuration/operational state;
- state can become stale or divergent through delay, restart, partition or asynchronous update;
- a controlled authoritative source/result or conflict-resolution basis exists;
- generation/epoch/incarnation metadata can distinguish stale from current state;
- the project can define convergence eligibility/completion criteria.

## 4. Non-Applicability / Cautions

This pattern is not a consensus algorithm and does not establish a universal single leader. It is not needed where all consumers synchronously read one authoritative state and cannot retain divergent copies. Generation numbers alone are insufficient when multiple uncontrolled writers can create conflicting values within the same generation or when wrap/reuse is ambiguous.

Security-related state may require separate trust/authentication/authorization authority; this pattern does not become a SEC-primary mechanism merely because security decisions are distributed.

## 5. L2 Trace

### 5.1 Primary Realization Candidate

- `SCAF-CFG-018` — realizes a reusable mechanism for establishing the project-defined cross-participant configuration/persistent-state consistency relationship.
- `SCAF-RUN-010` — realizes convergence of material cross-participant operational state toward the project-defined authoritative current-state/consistency decision.

### 5.2 Supporting Realization

- `SCAF-CFG-019` — generation/epoch comparison can identify stale/divergent replicas and gate controlled reconciliation after delay/partition/reconnect.
- `SCAF-RUN-011` — operational incarnation/generation prevents state from an old runtime instance being accepted as current.
- `SCAF-ROB-012` — convergence result can provide controlled consistency/eligibility criteria before reintegration of a participant/state/resource.

### 5.3 Constraint Inputs

- `SCAF-INT-007` — duplicate, missing, reordered or superseded exchange semantics constrain update application and convergence.
- `SCAF-INT-010` — protocol/connection session identity constrains whether update exchanges belong to the current Interaction context.
- `SCAF-RUN-021` — measurable age/synchronization/capacity conditions used for RUN consistency remain traced to TIME/INT project decisions.
- `SCAF-TIME-007` — where state eligibility depends on age/freshness, TIME owns the measurable age/threshold/uncertainty basis.
- `SCAF-SEC-025` — where the converged state participates in related security decisions, SEC retains authoritative security-decision consistency and unknown/disagreement consequences.

## 6. Required PDA Decisions

- state classes that require cross-participant convergence;
- authoritative source/result responsibility and permitted writer model;
- generation/epoch/incarnation identity semantics and rollover/reuse behavior;
- comparison rule for current, stale, conflicting and unknown states;
- update ordering/idempotency and duplicate/superseded handling;
- conflict-resolution/precedence basis where multiple legitimate sources can change;
- convergence eligibility/completion criteria and permitted temporary divergence;
- consequence when convergence cannot establish a controlled result;
- whether convergence is triggered by reconnect, startup, periodic check, source change or another project condition;
- evidence needed to diagnose divergence/convergence failure.

## 7. Mechanism Summary

Each participant associates relevant state with controlled identity metadata such as source, generation, epoch and operational/session incarnation as applicable. A convergence step compares the participant's state against the authoritative source/result basis, rejects information belonging to incompatible old generations/incarnations, resolves or escalates conflicts according to project decisions, and establishes an explicit **convergence status**.

Normal use of the shared state is gated where the project requires convergence before coordinated operation. The mechanism can operate after reconnect, but reconnect is not intrinsic to the pattern: convergence may also occur while connectivity remains continuous.

The primary family is `SYN` because the reusable intent is distributed state convergence. `COM-001` retains ownership of reconnect Interaction/session re-establishment and may compose with this pattern when reconnection is the trigger.

## 8. Variants

- authoritative-source generation comparison and selective update;
- full snapshot replacement of non-authoritative replicas;
- per-object generation/vector of controlled source generations without prescribing vector-clock algorithms;
- staged convergence where critical state is established before optional state;
- periodic divergence detection and repair while continuously connected.

## 9. Forces / Tradeoffs

- faster convergence versus transfer/comparison cost;
- simple single-source authority versus multi-writer flexibility;
- retained offline autonomy versus conflict complexity;
- fine-grained generations versus metadata/storage overhead;
- temporary divergence tolerance versus stricter readiness gating;
- centralized source dependency versus distributed resilience.

## 10. Failure / Weakness Modes

- generation/epoch wraps or is reused without disambiguation;
- stale participant writes current-looking state after restart;
- two authorities issue conflicting state with no controlled resolution basis;
- reordered/duplicate updates regress a participant;
- convergence is declared complete with unvalidated subsets;
- freshness depends on a clock relationship that is no longer usable;
- security-sensitive state converges structurally but trust/authorization relationship is not valid;
- convergence storms repeatedly transfer large state after transient divergence.

## 11. Selection Consequences

Selection requires explicit distributed-state authority, generation/incarnation semantics, convergence states and failure consequences. It may impose metadata, storage, bandwidth and readiness-gating costs. It does not make all replicated state strongly consistent and does not prescribe a distributed consensus model.

## 12. Composition Relations

### Requires

- controlled authoritative source/result and generation/incarnation semantics for the converged state.

### Commonly Composed With

- `SCAF-PAT-COM-001` — Reconnect plus State Reconciliation when reconnect initiates convergence;
- `SCAF-PAT-TIM-002` where freshness/epoch validity depends on time relationships;
- `SCAF-PAT-PST-001` where local replicas are persisted;
- `SCAF-PAT-FTL-002` where alternate participants must converge before failover readiness;
- `SCAF-PAT-EVD-001` for divergence/convergence evidence.

### Alternative To

- project architectures that avoid replicated/cached state and always read synchronously from one authoritative source.

### Conflicts With

- accepting any highest numeric generation without controlled source/incarnation semantics;
- treating transport reconnect alone as convergence completion.

### Subsumes

- None.

### Supersedes

- None.

## 13. External Authority Considerations

Safety/security/regulatory/risk authorities may constrain maximum permitted divergence, source authority, update authorization, unknown/conflict behavior, auditability and whether coordinated operation may continue before convergence.

## 14. Re-evaluation Triggers

Re-evaluate when writer/source authority, replica topology, restart/session model, generation representation, state partitioning, freshness rules, security-decision coupling, convergence trigger or permitted divergence changes.

## 15. Provenance / Reference Basis

SCAF-new synthesis of frozen CFG/RUN/INT/ROB/TIME/SEC obligations. The rc07 independent planning review explicitly approved this as complementary to `SCAF-PAT-COM-001`: SYN owns reusable convergence mechanics, while COM retains reconnect Interaction/session establishment.

## 16. L3 / L4 Boundary Note

This pattern does not prescribe Raft/Paxos, leader election, quorum size, CRDT, vector-clock implementation, database replication product, message schema, generation width, transport, serialization, retry interval or verification sequence.
