# SCAF-CTX — System Context, Mission, Function & Service Obligations

**Release:** v0.0.2rc10  
**Concern:** `SCAF-CTX`  
**Layer:** L1 Concern Authority + L2 Required Project Decisions  
**Status:** Normative RC

## 1. Purpose

`SCAF-CTX` **Defines Framework Semantics / Obligation** needed to establish **what System is being reasoned about, what it must provide, who/what interacts with it, and what consequences follow when required functions/services are unavailable or degraded**.

`SCAF-CTX` is the primary framework semantic authority for logical mission/function/service context. Structural placement/topology belongs to `SCAF-ARCH`; interaction/data contract detail belongs to `SCAF-INT`; runtime resilience response belongs to `SCAF-ROB`.

## 2. L1 Authority Boundary

`SCAF-CTX` **Defines Framework Semantics / Obligation** for:

- System scope and boundary criteria;
- mission/objective/use-case framing;
- Function, Capability and Service semantics;
- provider/consumer and logical service dependency semantics;
- external actors and external-authority inputs;
- consequence-of-service-loss and required continuity/degradation outcome reasoning;
- assumptions that materially affect architecture decisions.

The **Project Design Authority Defines Project Instance / Decision** for the actual project boundary, mission/function/service model, provider/consumer relationships, logical dependencies, ordinary mission consequence/continuity/degraded-service architecture outcomes and applicable assumptions, subject to applicable external-authority constraints.

For safety-significant conditions, the applicable project safety/hazard authority remains the source authority for the safety objective/condition and risk-acceptance basis. The Project Design Authority integrates those controlled safety inputs into the project architecture; it does not replace their source authority.

`SCAF-CTX` does not define the project topology, structural allocation, runtime failover/recovery behavior, safety-significant safe condition or implementation mechanism.

## 3. Normative Obligations

### `SCAF-CTX-001` — System scope

**Target:** Project-Applicable Obligation

The project **SHALL** define the System scope to which the SCAF application applies.

The scope **SHALL** identify the System boundary sufficiently to distinguish in-scope architecture obligations from external actors, external Systems and external authorities.

### `SCAF-CTX-002` — Mission and objective framing

**Target:** Project-Applicable Obligation

The project **SHALL** identify the mission, objective, use case or equivalent purpose that justifies the System's required behavior.

### `SCAF-CTX-003` — Required Functions

**Target:** Project-Applicable Obligation

The project **SHALL** identify the Functions required to achieve applicable System objectives.

### `SCAF-CTX-004` — Capabilities

**Target:** Project-Applicable Obligation

Where the ability to perform a Function depends on stated conditions, resources or operating modes, the project **SHALL** identify the relevant Capability and its required conditions.

Capability semantics **SHALL NOT** be reduced to a technology label or implementation component.

### `SCAF-CTX-005` — Services and provider/consumer contract intent

**Target:** Project-Applicable Obligation

Where behavior or utility is exposed from a provider to one or more consumers, the project **SHALL** identify the Service and intended provider/consumer relationship.

At CTX level, this establishes logical service intent/dependency. Detailed interface, data and temporal contract semantics belong to applicable downstream concerns.

### `SCAF-CTX-006` — Logical service dependencies

**Target:** Project-Applicable Obligation

The project **SHALL** identify logical dependencies whose loss, degradation, staleness or unavailability can materially affect a required Function, Capability or Service.

The logical dependency model **SHALL** remain distinguishable from later structural realization dependencies defined by the Project Design Authority under `SCAF-ARCH` obligations.

### `SCAF-CTX-007` — Service-loss consequence

**Target:** Project-Applicable Obligation

For each Function or Service whose loss or degradation can materially affect mission or required operation, the project **SHALL** identify the relevant consequence.

### `SCAF-CTX-015` — Ordinary continuity / degraded-service outcome

**Target:** Project-Applicable Obligation

Where ordinary mission continuity or degraded-service behavior is required, the project **SHALL** identify the required context-level outcome and its authority provenance.

### `SCAF-CTX-016` — Safety-significant source-authority provenance

**Target:** Project-Applicable Obligation

Where a safety-significant safety objective/condition or risk-acceptance basis applies, the project **SHALL** preserve the applicable safety/hazard authority as the source authority.

The project **SHALL** trace how the Project Design Authority integrates that controlled safety input into the project architecture without replacing its source-authority provenance.

### `SCAF-CTX-008` — External actors and authorities

**Target:** Project-Applicable Obligation

The project **SHALL** identify external actors, Systems and authority sources that impose material architecture constraints or provide/consume required Services.

Applicable safety, security, regulatory, operational or risk authority decisions **SHALL** remain explicit and traceable as constraints/inputs rather than being collapsed into Project Design Authority provenance.

### `SCAF-CTX-009` — Assumptions and environmental conditions

**Target:** Project-Applicable Obligation

The project **SHALL** record assumptions and environmental/operational conditions that materially affect architecture applicability, Service availability, dependency reasoning or verification.

An assumption whose invalidation can change architecture decisions **SHALL** have a re-evaluation trigger in the project application trace.

### `SCAF-CTX-010` — Context trace-source readiness

**Target:** Project-Applicable Obligation

The project **SHALL** maintain the material CTX Functions, Capabilities, Services, dependencies, consequences, assumptions and external constraints with stable references or controlled identifiers sufficient for downstream architecture decisions to trace to their motivating context.

`SCAF-CTX-010` does not create a second context-to-architecture justification authority; `SCAF-ARCH` **Defines Framework Semantics / Obligation** for structural decisions to trace to applicable context.

### `SCAF-CTX-011` — Context changes require re-scan

**Target:** Project-Applicable Obligation

Changes to System scope, mission, required Service, provider/consumer relationship, logical dependency, material assumption or external-authority constraint **SHALL** trigger re-evaluation of affected SCAF concerns and project decisions.

### `SCAF-CTX-012` — Material operating modes

**Target:** Project-Applicable Obligation

Where operating modes materially change required behavior, dependencies, risk, continuity/degradation expectation or verification basis, the project **SHALL** identify those operating modes and their context significance.

### `SCAF-CTX-013` — Function traceability

**Target:** Project-Applicable Obligation

Each material Function **SHALL** trace to at least one applicable objective, requirement source or equivalent controlled mission input.

## 4. Framework Normative Invariants

### `SCAF-CTX-014` — CTX / ROB / safety-authority boundary

**Target:** Framework Normative Invariant

`SCAF-CTX` **SHALL NOT** define or select project runtime failover, recovery or containment behavior; those runtime resilience-response semantics belong to `SCAF-ROB`.

`SCAF-CTX` **SHALL NOT** become the source authority for a safety-significant safety objective/condition or its risk-acceptance basis; those remain owned by the applicable project safety/hazard authority.

## 5. Required Project Decisions / Records

The following table summarizes expected project outputs from the obligations above; it is informative and does not create additional normative requirements.

| Decision / record | Project-side authority / provenance |
|---|---|
| System scope and boundary | Project Design Authority |
| Mission / objectives | Project Design Authority / project requirements authority as assigned |
| Material operating modes | Project Design Authority / applicable project authority as assigned |
| Function / Capability / Service model | Project Design Authority |
| Provider / consumer relationships | Project Design Authority |
| Logical dependency model | Project Design Authority |
| Ordinary mission consequence / continuity / degraded-service outcome | Project Design Authority, constrained by applicable external authorities |
| Safety-significant safety objective/condition and risk-acceptance basis | Applicable safety/hazard authority; integrated into architecture by Project Design Authority |
| Material assumptions / external constraints | Applicable source authority; integrated into architecture by Project Design Authority |

The Framework Scan may **Disposition / Trace** these decisions but does not own them.

## 6. Concern Boundaries

- `SCAF-ARCH` **Defines Framework Semantics / Obligation** for structural allocation, topology, Nodes and Domains.
- `SCAF-INT` **Defines Framework Semantics / Obligation** for interface, interaction and data-contract semantics.
- `SCAF-TIME` **Defines Framework Semantics / Obligation** for measurable temporal semantics and budgets.
- `SCAF-ROB` **Defines Framework Semantics / Obligation** for failure/health/resilience response when Service dependencies fail or degrade.
- `SCAF-SEC` **Constrains** architecture using security-originated objectives/constraints from the applicable security authority.
- `SCAF-ASSUR` **Defines Framework Semantics / Obligation** for assurance/evidence rules; Project Verification / Assurance Authority **Verifies** applicable CTX obligations and project decisions.

## 7. Non-Normative Example

A project may identify a logical Service `Command Delivery` provided to an actuator-control Function. `SCAF-CTX` requires the logical need, provider/consumer relation, consequence of Service loss and any required continuity/degradation outcome to be understood. It does not decide whether that Service is realized through UART, CAN, shared memory or another mechanism, nor does it select the runtime failover behavior.
