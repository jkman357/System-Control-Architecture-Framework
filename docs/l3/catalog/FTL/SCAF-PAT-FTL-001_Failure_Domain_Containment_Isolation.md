# SCAF-PAT-FTL-001 — Failure-Domain Containment / Isolation

**Development Release:** v0.0.3rc13  
**Pattern Family:** `FTL` — Fault Tolerance & Isolation  
**Pattern Kind:** Mechanism  
**Catalog Status:** Available  
**Maturity:** M2 — Architecture Reviewed  
**Introduced In:** v0.0.3rc08

## Metadata

| Field | Value |
|---|---|
| Pattern ID | `SCAF-PAT-FTL-001` |
| Pattern Name | Failure-Domain Containment / Isolation |
| Pattern Family | `FTL` |
| Pattern Kind | Mechanism |
| Catalog Status | Available |
| Maturity | M2 — Architecture Reviewed |
| Introduced In | v0.0.3rc08 |
| Primary L2 Trace | `SCAF-ROB-008` |
| Supporting L2 Trace | `SCAF-ROB-015` |
| Constraint Inputs | `SCAF-ARCH-007`, `SCAF-ARCH-008`, `SCAF-ARCH-015`, `SCAF-ROB-007`, `SCAF-ROB-014` |
| Profile Facets | MCU/SoC/FPGA/PC/distributed realizations with material fault, resource, power, clock, trust or responsibility domains |
| Provenance / Reference Basis | Frozen SCAF ARCH/ROB obligations plus rc07 second-tranche planning review approval; SCAF-new technology-neutral synthesis |

## 1. Intent

Bound the runtime propagation of an applicable fault/error/failure to project-defined structural or responsibility domains so unaffected responsibilities can retain controlled behavior and the project can determine whether containment succeeded.

## 2. Problem

A failure can escape its origin through shared resources, common providers, interfaces, power/clock dependencies, memory corruption, control authority or recovery actions. Without an explicit containment mechanism, a project may claim isolation merely because components are physically or logically separated even though the actual propagation path crosses those boundaries.

## 3. Applicability

Consider this pattern where:

- the project has identified a material failure propagation path;
- one or more project-defined Domains or responsibilities are intended to bound the effect;
- unaffected Functions/Services are expected to remain controlled after the initiating condition;
- the project can define observable behavior-level containment success/failure;
- shared dependencies and common-mode assumptions can be identified explicitly.

## 4. Non-Applicability / Cautions

Do not select this pattern merely because the architecture contains multiple Nodes, processes, partitions or hardware devices. A Node boundary is not automatically a containment boundary. The pattern is weak or inapplicable when material shared dependencies defeat the claimed isolation, when the project cannot define a meaningful contained outcome, or when complete shutdown is the required system response.

This pattern does not require redundancy and does not imply continued Service after containment.

## 5. L2 Trace

### 5.1 Primary Realization Candidate

- `SCAF-ROB-008` — provides a reusable runtime mechanism for establishing and preserving the project-defined containment outcome at controlled structural/Domain boundaries.

### 5.2 Supporting Realization

- `SCAF-ROB-015` — containment can bound cascading failure or recovery-storm propagation when peer/shared dependencies would otherwise amplify the initiating condition.

### 5.3 Constraint Inputs

- `SCAF-ARCH-007` — the actual Domain boundary is a Project Design Authority decision and is consumed by this pattern rather than redefined by FTL.
- `SCAF-ARCH-008` — identifies the controlled structural/Domain boundaries that are inputs to downstream containment reasoning.
- `SCAF-ARCH-015` — shared resources/providers/common infrastructure constrain whether an isolation claim is credible.
- `SCAF-ROB-007` — the project-identified material failure-propagation path is consumed as an upstream constraint that determines where containment placement, isolation action or propagation blocking must be evaluated; this Pattern does not author the propagation-path analysis.
- `SCAF-ROB-014` — common-mode/correlated failure assumptions constrain any claim that separated domains or recovery paths are independent.

## 6. Required PDA Decisions

- which failure propagation paths are material;
- the actual structural/Domain/responsibility boundaries used by the containment claim;
- which effects must be blocked, limited or made non-propagating;
- what behavior constitutes containment success, partial containment and failure;
- which shared dependencies remain inside or cross the boundary;
- what unaffected responsibilities may continue operating;
- whether containment changes readiness, degraded-Service or recovery eligibility;
- what evidence is required to determine containment outcome;
- the consequence when the boundary cannot be established or is itself compromised.

## 7. Mechanism Summary

The mechanism places a controlled **propagation boundary** between an affected origin/responsibility and the responsibilities that must remain protected. Inputs or effects crossing that boundary are admitted, blocked, isolated, invalidated or placed into a controlled safe/indeterminate condition according to project-defined semantics. The mechanism also exposes a containment-result state sufficient for downstream ROB/RUN/recovery decisions.

The mechanism does not invent the boundary. ARCH defines the actual structural/Domain relationship; FTL uses it to realize runtime containment behavior.

Containment can be implemented at different realization layers, including responsibility gating, resource partitioning, communication isolation, controlled ownership transfer, fault-domain reset separation or another project mechanism, but no specific technology is required by this L3 entry.

## 8. Variants

- fail-stop isolation of the affected responsibility while peers continue;
- communication/interaction isolation at a defined domain boundary;
- resource partition/quarantine that prevents corrupted or exhausted resources from affecting peers;
- selective functional isolation where only affected capability paths are blocked;
- containment combined with a later reintegration/recovery gate.

## 9. Forces / Tradeoffs

- stronger isolation versus resource duplication and implementation cost;
- fast containment versus risk of false isolation or incomplete diagnosis;
- coarse domains versus availability loss from unnecessarily large containment scope;
- fine-grained domains versus architectural complexity and cross-domain dependencies;
- local autonomy versus coordination required to avoid inconsistent peer decisions;
- shared infrastructure efficiency versus common-mode exposure.

## 10. Failure / Weakness Modes

- the claimed domain boundary does not match the actual propagation path;
- a shared clock, power source, memory, bus, provider or control path defeats isolation;
- containment action itself propagates disruption to unaffected responsibilities;
- partial isolation is treated as successful without evidence;
- stale/queued cross-domain interactions reintroduce the fault after isolation;
- recovery/reintegration occurs before the boundary and affected state are valid;
- overly broad containment causes unnecessary Service loss.

## 11. Selection Consequences

Selection requires controlled Domain/propagation-path records, explicit success/failure semantics, shared-dependency analysis and a defined downstream consequence for contained versus uncontained outcomes. It may create new operational states, recovery gates, observability needs or architecture constraints, but those project decisions remain under their applicable authorities.

## 12. Composition Relations

### Requires

- project-defined structural/Domain boundaries and failure propagation assumptions.

### Commonly Composed With

- `SCAF-PAT-FTL-002` — Controlled Failover with Graceful Degradation;
- `SCAF-PAT-SUP-001` / `SCAF-PAT-SUP-002` where supervision triggers containment;
- `SCAF-PAT-REC-001` where recovery is attempted after containment;
- `SCAF-PAT-EVD-001` where containment evidence must be retained.

### Alternative To

- project architectures that intentionally stop the whole affected System instead of preserving an unaffected domain.

### Conflicts With

- architectures that claim containment solely from Node/process/device separation while retaining uncontrolled shared dependencies across the claimed boundary.

### Subsumes

- None.

### Supersedes

- None.

## 13. External Authority Considerations

Applicable safety, security, regulatory or risk authorities may constrain which effects must be contained, required independence, acceptable residual common-mode risk, permitted continued operation and evidence needed to justify the containment claim.

## 14. Re-evaluation Triggers

Re-evaluate when Domain boundaries, shared infrastructure, resource ownership, power/clock topology, communication paths, recovery paths, redundancy assumptions, Service allocation or failure-propagation analysis changes.

## 15. Provenance / Reference Basis

SCAF-new synthesis of frozen ARCH/ROB obligations. The category was explicitly approved for second-tranche authoring by the v0.0.3rc07 independent coverage/planning review, which required the mechanism to consume architecture/failure-domain decisions without redefining ARCH topology.

## 16. L3 / L4 Boundary Note

This pattern does not prescribe an MPU/MMU scheme, process/container technology, bus firewall, power switch, reset controller, FPGA partition, watchdog IC, IPC mechanism, memory map, API, isolation timeout, fault-injection procedure or verification test sequence.
