# SCAF-INT — Interfaces, Interaction & Data Contract Obligations

**Release:** v0.0.2rc14  
**Concern:** `SCAF-INT`  
**Layer:** L1 Concern Authority + L2 Required Project Decisions  
**Status:** Normative RC

## 1. Purpose

`SCAF-INT` **Defines Framework Semantics / Obligation** for how material interactions and interface/data contracts are identified, bounded and controlled without prescribing a transport, protocol stack, language, bus or implementation mechanism.

`SCAF-INT` is the primary framework semantic authority for Interface identity, Interaction semantics, data-contract semantics, validity/freshness/ordering/provenance contract meaning, targeting semantics, compatibility/evolution, and protocol/connection session identity where applicable.

Logical Function/Service need belongs to `SCAF-CTX`; structural placement/topology belongs to `SCAF-ARCH`; measurable temporal values and timebase semantics belong to `SCAF-TIME`; runtime failure/recovery behavior belongs to `SCAF-ROB`; adversarial/security constraints remain sourced from the applicable security authority and are applied through `SCAF-SEC`.

## 2. L1 Authority Boundary

`SCAF-INT` **Defines Framework Semantics / Obligation** for:

- Interface identity and controlled contract boundary;
- participating responsibility and interaction direction/intent;
- command/response/event/telemetry/stream/shared-state or equivalent interaction semantics where applicable;
- data meaning, representation and contract metadata needed for unambiguous exchange;
- validity, freshness-state, ordering and provenance contract semantics;
- addressing/routing/targeting semantics where applicable;
- protocol versus transport separation;
- protocol/connection session identity and generation semantics where material;
- compatibility/evolution semantics;
- negative/unsupported interaction-contract behavior;
- traceability from interaction/interface contracts to motivating CTX/ARCH decisions.

The **Project Design Authority Defines Project Instance / Decision** for the actual project Interfaces, Interactions, participants, directionality, data contracts, validity/freshness/ordering rules, addressing/targeting, session identity, compatibility policy and negative-contract outcomes.

`SCAF-INT` does not define project topology, measurable time thresholds/timebases, runtime failover/recovery, security risk acceptance, or concrete protocol/transport mechanisms.

## 3. Project-Applicable Obligations

### `SCAF-INT-001` — Material Interaction identification

**Target:** Project-Applicable Obligation

The project **SHALL** identify each material Interaction whose correctness, availability, data meaning or failure can affect an applicable Function, Capability, Service, architecture decision or verification obligation.

### `SCAF-INT-002` — Interaction-to-Interface boundary

**Target:** Project-Applicable Obligation

For each material Interaction, the project **SHALL** identify the applicable Interface boundary or boundaries through which the Interaction contract is exposed or realized.

This obligation preserves the frozen metamodel relation between a meaningful Interaction and its applicable Interface boundary without requiring every Interface boundary to have a separately controlled identity.

### `SCAF-INT-019` — Separately controlled Interface identity

**Target:** Project-Applicable Obligation

Where an Interface contract requires independently controlled identity, versioning, ownership, lifecycle or verification, the Project Design Authority **SHALL** define a stable Interface identity and the controlled contract boundary to which those project obligations apply.

### `SCAF-INT-003` — Participants, Roles and direction

**Target:** Project-Applicable Obligation

For each material Interaction, the project **SHALL** identify the participating Systems/Nodes and, where applicable, external Systems, external actors or other applicable external participants, together with applicable Roles and the direction or relationship needed to prevent sender/receiver, provider/consumer, initiator/responder or equivalent responsibility ambiguity.

An external participant **SHALL NOT** be modeled as a Node solely to satisfy this obligation.

### `SCAF-INT-004` — Interaction semantic class

**Target:** Project-Applicable Obligation

The project **SHALL** define the semantic form of each material Interaction sufficiently to distinguish the applicable contract behavior, such as command, response, event, telemetry, stream, shared-state access, request/reply or another project-defined form.

The semantic form **SHALL NOT** be inferred solely from transport or implementation technology.

### `SCAF-INT-005` — Data contract

**Target:** Project-Applicable Obligation

For each material exchanged data item or controlled shared-state element, the project **SHALL** define the data meaning and representation properties necessary for producer and consumer to interpret the contract consistently.

Where material, the contract **SHALL** include applicable units, domains/ranges, encoding/serialization meaning, version/discriminator information, or equivalent interpretation metadata.

### `SCAF-INT-006` — Validity and provenance semantics

**Target:** Project-Applicable Obligation

Where data can be valid, invalid, unavailable, unknown, substituted, derived or otherwise qualified, the project **SHALL** define the applicable validity states, the criteria or conditions used to assign those states, and the provenance semantics needed for a consumer to interpret the data consistently.

Where a validity state changes the contract outcome, the project **SHALL** define the applicable consumer-visible contract consequence or trace to the controlled requirement that defines that consequence.

### `SCAF-INT-007` — Ordering semantics

**Target:** Project-Applicable Obligation

Where semantic ordering can affect correctness or interpretation, the project **SHALL** define the required Interaction/data-contract ordering semantics, including the meaning of duplicate, missing, reordered or superseded information where applicable.

### `SCAF-INT-008` — Freshness-state contract

**Target:** Project-Applicable Obligation

Where age or staleness can affect correctness, the project **SHALL** define the Interface/Interaction contract meaning of current, stale, expired, invalid or equivalent freshness states and the consumer-visible consequence of those states at the contract level.

Measurable age limits, timebase selection, clock relationship and temporal uncertainty used to evaluate those states are defined through applicable `SCAF-TIME` project decisions.

### `SCAF-INT-009` — Addressing, routing and targeting

**Target:** Project-Applicable Obligation

Where an Interaction may reach more than one possible participant, instance, Service, channel or destination, the project **SHALL** define the applicable addressing, routing or targeting semantics sufficiently to prevent ambiguous destination ownership.

### `SCAF-INT-010` — Protocol / connection session identity

**Target:** Project-Applicable Obligation

Where restart, reconnection, replacement or reuse of an Interaction context can make old and new exchanges ambiguous, the project **SHALL** define protocol/connection session identity or generation semantics sufficient to distinguish the applicable session incarnations.

### `SCAF-INT-011` — Protocol versus transport separation

**Target:** Project-Applicable Obligation

The project **SHALL** keep the semantic Interaction/data contract distinguishable from the transport or realization mechanism that carries it whenever either may change independently.

### `SCAF-INT-012` — Compatibility and evolution

**Target:** Project-Applicable Obligation

Where Interface or data-contract evolution can affect independently developed, deployed, updated or replaced participants, the project **SHALL** define the compatibility/evolution policy and the conditions under which an Interaction is accepted, rejected, degraded or requires coordinated change.

### `SCAF-INT-013` — Negative / unsupported contract behavior

**Target:** Project-Applicable Obligation

Where malformed, unsupported, unknown, duplicate, out-of-order, stale, unauthorized or otherwise non-conforming Interaction input can occur and is material, the project **SHALL** define the contract-level handling outcome and authority provenance.

**Boundary note (informative):** this obligation defines the contract outcome; runtime resilience/recovery behavior after an Interaction failure or violation remains under applicable `SCAF-ROB` obligations.

### `SCAF-INT-014` — Contract trace to context and architecture

**Target:** Project-Applicable Obligation

Each material Interface/Interaction contract **SHALL** trace to the applicable CTX Service/Function/dependency need and to the ARCH participant/responsibility relationship that motivates the contract.

### `SCAF-INT-015` — Interaction change and re-evaluation

**Target:** Project-Applicable Obligation

Changes to Interface identity, participants, contract meaning, validity/freshness/order semantics, targeting, session identity, compatibility policy or negative-contract outcome **SHALL** trigger re-evaluation of affected timing, runtime, robustness, lifecycle, observability, security and verification obligations.

## 4. Framework Normative Invariants

### `SCAF-INT-016` — INT / TIME freshness authority boundary

**Target:** Framework Normative Invariant

`SCAF-INT` **Defines Framework Semantics / Obligation** for the semantic meaning of valid/current/stale/expired Interaction data and for semantic ordering within an Interface/Interaction contract.

`SCAF-INT` **SHALL NOT** own measurable timebase, synchronization, age-limit, deadline or temporal-uncertainty semantics; those belong to `SCAF-TIME`.

### `SCAF-INT-017` — INT / ROB / SEC authority boundary

**Target:** Framework Normative Invariant

`SCAF-INT` **Defines Framework Semantics / Obligation** for the Interaction/data-contract result of a negative or invalid exchange.

`SCAF-INT` **SHALL NOT** redefine runtime resilience/recovery behavior for which `SCAF-ROB` **Defines Framework Semantics / Obligation**, or security objectives/risk acceptance for which the applicable Security Authority remains source authority. `SCAF-SEC` **Defines Framework Semantics / Obligation** for applying controlled security constraints to INT contracts without replacing either authority.

### `SCAF-INT-018` — Session-identity partition

**Target:** Framework Normative Invariant

Protocol/connection session identity and generation semantics belong to `SCAF-INT`.

Time Epoch / Time Domain belongs to `SCAF-TIME`; Boot Incarnation belongs to `SCAF-LIFE`; Operational Incarnation belongs to `SCAF-RUN`; `SCAF-OBS` records these identities and their provenance/correlation without redefining their primary semantics.

## 5. Required Project Decisions / Records

The following table is informative and does not create additional normative requirements.

| Decision / record | Project-side authority / provenance |
|---|---|
| Material Interaction inventory | Project Design Authority |
| Interaction-to-Interface boundary mapping | Project Design Authority |
| Separately controlled Interface identity / contract boundary, when Applicable | Project Design Authority |
| Participants / Roles / direction | Project Design Authority |
| Interaction semantic form | Project Design Authority |
| Data meaning / representation contract | Project Design Authority, constrained by applicable source authorities |
| Validity / ordering / freshness-state semantics | Project Design Authority; temporal values constrained by `SCAF-TIME` decisions |
| Addressing / routing / targeting | Project Design Authority |
| Protocol / connection session identity | Project Design Authority |
| Compatibility / evolution policy | Project Design Authority, constrained by lifecycle/security/project authorities where applicable |
| Negative / unsupported contract outcome | Project Design Authority, constrained by applicable ROB/SEC/external-authority obligations |

`SCAF-APP` may Disposition / Trace these decisions but does not own them.

## 6. Concern Boundaries

- `SCAF-CTX` **Defines Framework Semantics / Obligation** for logical Function/Service/dependency intent.
- `SCAF-ARCH` **Defines Framework Semantics / Obligation** for structural participants, topology and allocation.
- `SCAF-INT` **Defines Framework Semantics / Obligation** for Interface, Interaction and data-contract meaning.
- `SCAF-TIME` **Defines Framework Semantics / Obligation** for measurable temporal values, timebase/synchronization and temporal uncertainty.
- `SCAF-RUN` **Defines Framework Semantics / Obligation** for service/operational-state behavior outside the Interaction contract itself.
- `SCAF-ROB` **Defines Framework Semantics / Obligation** for failure/health/containment/recovery response.
- `SCAF-LIFE` **Defines Framework Semantics / Obligation** for boot/reset/power/update lifecycle semantics that may constrain compatibility or session behavior.
- `SCAF-OBS` **Observes** and records Interaction/session/timing provenance without becoming source authority.
- `SCAF-SEC` **Constrains** Interface/Interaction semantics using applicable security-authority inputs.
- `SCAF-ASSUR` **Defines Framework Semantics / Obligation** for assurance/evidence semantics; Project Verification / Assurance Authority **Verifies** the project contract against its Applicable Satisfaction Basis.

## 7. Non-Normative Example

A logical telemetry Service may be realized through a serial bus, shared memory, IPC or a network transport. `SCAF-INT` requires the project to define what the telemetry means, who produces/consumes it, how validity/order/freshness states are interpreted, and how session/version changes are recognized. It does not require a specific bus, packet format, retry algorithm or time threshold.
