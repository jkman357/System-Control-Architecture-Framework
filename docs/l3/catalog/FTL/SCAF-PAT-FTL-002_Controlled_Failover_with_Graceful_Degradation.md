# SCAF-PAT-FTL-002 — Controlled Failover with Graceful Degradation

**Development Release:** v0.0.3rc12  
**Pattern Family:** `FTL` — Fault Tolerance & Isolation  
**Pattern Kind:** Composite Pattern  
**Catalog Status:** Available  
**Maturity:** M2 — Architecture Reviewed  
**Introduced In:** v0.0.3rc08

## Metadata

| Field | Value |
|---|---|
| Pattern ID | `SCAF-PAT-FTL-002` |
| Pattern Name | Controlled Failover with Graceful Degradation |
| Pattern Family | `FTL` |
| Pattern Kind | Composite Pattern |
| Catalog Status | Available |
| Maturity | M2 — Architecture Reviewed |
| Introduced In | v0.0.3rc08 |
| Primary L2 Trace | `SCAF-ROB-009`, `SCAF-ROB-010` |
| Supporting L2 Trace | `SCAF-ROB-011`, `SCAF-ROB-015` |
| Constraint Inputs | `SCAF-CTX-007`, `SCAF-CTX-015`, `SCAF-ARCH-006`, `SCAF-ARCH-015`, `SCAF-ROB-014`, `SCAF-RUN-006`, `SCAF-RUN-020` |
| Profile Facets | Multi-path, redundant, alternate-provider or degradable-service realizations across embedded, host, SoC/FPGA and distributed systems |
| Provenance / Reference Basis | Frozen SCAF CTX/ARCH/RUN/ROB obligations plus rc07 second-tranche planning review approval; SCAF-new technology-neutral synthesis |

## 1. Intent

Continue a controlled required Service or a deliberately reduced Service after a material failure by selecting an eligible alternate realization or degraded outcome without making redundancy topology, voting or failover policy universal.

## 2. Problem

A system may have an alternate provider, redundant resource or reduced-capability mode, yet still fail unsafely if it cannot determine when the alternate is eligible, whether the failed path has been isolated, what state must transfer, what Service remains valid or when repeated failover must stop. Conversely, forcing failover everywhere can add common-mode complexity and hide cases where shutdown is the correct outcome.

## 3. Applicability

Consider this pattern where:

- continued or degraded Service after a failure is project-applicable;
- at least one alternate realization, resource, participant or reduced-function path can provide a controlled outcome;
- project-defined eligibility and completion criteria can be established;
- Service-loss/degradation consequences and operational readiness states are controlled;
- common-mode/shared dependencies can be assessed.

## 4. Non-Applicability / Cautions

Do not select this pattern when no acceptable alternate/degraded outcome exists, when switching could violate a stronger external authority, when alternate paths share the same unmitigated failure source, or when the safest required outcome is controlled shutdown.

Failover does not imply full capability restoration. Graceful degradation does not mean arbitrary feature loss; the permitted degraded outcome comes from project context and applicable external authorities.

## 5. L2 Trace

### 5.1 Primary Realization Candidate

- `SCAF-ROB-009` — realizes one reusable mechanism family for an Applicable failover/reconfiguration/tolerance outcome while leaving topology and selection policy project-specific.
- `SCAF-ROB-010` — realizes a controlled transition to a project-defined degraded Service outcome when full Service cannot be maintained.

### 5.2 Supporting Realization

- `SCAF-ROB-011` — requires an explicit success/failed-completion criterion for the failover/degradation transition.
- `SCAF-ROB-015` — can bound oscillating failover, repeated recovery or peer-dependency cascades when the project defines appropriate inhibit/escalation conditions.

### 5.3 Constraint Inputs

- `SCAF-CTX-007` — the consequence of Service loss/degradation constrains whether failover/degradation is necessary or acceptable.
- `SCAF-CTX-015` — context-level continuity/degraded-Service outcome is externally/project controlled and is not authored by this pattern.
- `SCAF-ARCH-006` — actual alternate providers/resources and realization dependencies are architecture decisions consumed by FTL.
- `SCAF-ARCH-015` — shared dependencies constrain claims that alternate paths provide meaningful independence.
- `SCAF-ROB-014` — common-mode/correlated failure assumptions constrain eligibility and confidence in failover paths.
- `SCAF-RUN-006` — readiness/availability states constrain when an alternate or degraded path may be represented as operationally usable.
- `SCAF-RUN-020` — readiness/degraded-state consequences remain traced to controlled CTX/external authority.

## 6. Required PDA Decisions

- which Functions/Services require continuity, degradation or shutdown after each material failure class;
- alternate resource/provider/path candidates and their eligibility criteria;
- required isolation/containment before an alternate can be trusted;
- authoritative state/ownership transfer semantics;
- full-Service versus degraded-Service completion criteria;
- operational readiness/availability state mapping;
- failback policy, if any;
- repeated failover/oscillation termination or escalation criteria;
- common-mode assumptions and residual-risk treatment;
- evidence needed to establish transition outcome and diagnose failure.

## 7. Mechanism Summary

The mechanism separates three decisions that are often incorrectly collapsed:

1. **eligibility** — determine whether an alternate or degraded path is permitted and sufficiently independent/ready;
2. **transition** — transfer or establish the required authority/state/resource relationship without accepting stale or conflicting ownership;
3. **completion** — assert full, degraded or failed outcome using project-defined Service/readiness criteria.

If the preferred path is unavailable or invalid, the mechanism chooses an eligible alternate outcome only under the controlled project decision basis. If no acceptable alternate exists, it enters the defined failed/degraded/escalated outcome instead of cycling indefinitely.

The primary family is `FTL` because the reusable mechanism intent is tolerance through alternate/degraded service realization, not generic recovery retry.

## 8. Variants

- active/standby provider switch;
- N-of-M eligible resource selection without prescribing a voting algorithm;
- degraded-function mode that removes a nonessential capability while preserving a required Service;
- alternate communication/control path selection;
- manual-authority failover where automatic transition is not permitted.

## 9. Forces / Tradeoffs

- availability versus redundancy cost and common-mode exposure;
- transition speed versus validation/state-transfer confidence;
- automatic failover versus operator/authority oversight;
- capability preservation versus simpler degraded modes;
- failback convenience versus oscillation risk;
- alternate-path independence versus resource sharing efficiency.

## 10. Failure / Weakness Modes

- alternate path shares the same hidden failure source;
- failed path remains active and creates conflicting authority;
- stale state/ownership transfers to the alternate;
- transition is declared complete before readiness is established;
- repeated failover/failback oscillates under marginal conditions;
- degraded mode violates a CTX/external-authority consequence;
- failure of the failover selector/supervisor itself is not controlled;
- resource depletion makes all alternates simultaneously unusable.

## 11. Selection Consequences

Selection creates project obligations to identify alternate/degraded outcomes, eligibility and completion criteria, state/authority transfer semantics, readiness mapping and common-mode assumptions. It may require containment, synchronization, supervision or evidence mechanisms, but it does not mandate any particular redundancy topology.

## 12. Composition Relations

### Requires

- project-defined alternate/degraded Service outcome and eligibility basis.

### Commonly Composed With

- `SCAF-PAT-FTL-001` — Failure-Domain Containment / Isolation;
- `SCAF-PAT-SUP-001` / `SCAF-PAT-SUP-002` for failure/liveness evidence;
- `SCAF-PAT-COM-001` where alternate participants must establish a valid Interaction relationship;
- `SCAF-PAT-SYN-001` where cross-participant state must converge before readiness;
- `SCAF-PAT-EVD-001` for retained transition evidence.

### Alternative To

- controlled shutdown where continuity/degraded Service is not required or is not safely achievable.

### Conflicts With

- unconditional failover to an alternate whose eligibility, state authority or independence has not been established.

### Subsumes

- None.

### Supersedes

- None.

## 13. External Authority Considerations

Safety/security/regulatory/risk authorities may constrain required continuity, prohibited degraded states, independence, switchover authority, operator involvement, failover timing and residual risk.

## 14. Re-evaluation Triggers

Re-evaluate when Service-loss consequences, alternate topology, shared dependencies, state ownership, readiness semantics, common-mode assumptions, operating modes, resource budgets or external failover constraints change.

## 15. Provenance / Reference Basis

SCAF-new synthesis of frozen CTX/ARCH/RUN/ROB obligations. The rc07 independent planning review explicitly approved this as distinct from containment: containment answers where/how propagation is bounded, while this pattern answers whether/how Service continues or degrades.

## 16. L3 / L4 Boundary Note

This pattern does not prescribe active-active versus active-passive topology, voting quorum, leader election, hot/cold standby implementation, switchover timeout, specific redundancy hardware, health algorithm, failover API, state-transfer protocol or verification sequence.
