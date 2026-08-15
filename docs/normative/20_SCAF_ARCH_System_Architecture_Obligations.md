# SCAF-ARCH — System / Node / Role / Domain Architecture Obligations

**Release:** v0.0.2rc05  
**Concern:** `SCAF-ARCH`  
**Layer:** L1 Concern Authority + L2 Required Project Decisions  
**Status:** Normative RC

## 1. Purpose

`SCAF-ARCH` **Defines Framework Semantics / Obligation** for structuring the System, allocating System/Node responsibilities, defining structural topology/reasoning Domains, and making structural realization dependencies explicit.

`SCAF-ARCH` does not own logical mission/Service semantics (`SCAF-CTX`), detailed interaction/data contracts (`SCAF-INT`) or runtime fault/containment/recovery behavior (`SCAF-ROB`).

## 2. L1 Authority Boundary

`SCAF-ARCH` **Defines Framework Semantics / Obligation** for:

- Node-decomposition applicability and Node-boundary criteria;
- contextual Role semantics;
- allocation of Capability/Service responsibility to applicable System/Node responsibilities;
- topology and structural realization-dependency semantics;
- cross-cutting Domain semantics;
- subordinate System / subordinate Node representation;
- trace of structural decisions to motivating context and project decision authority.

The **Project Design Authority Defines Project Instance / Decision** for actual Node-decomposition use, Node boundaries, Role assignments, capability/service allocation, topology, structural dependency graph and Domain boundaries.

## 3. Normative Obligations

### `SCAF-ARCH-001` — Architecture realizes applicable context

**Target:** Project-Applicable Obligation

The project **SHALL** define a structural architecture sufficient to realize applicable `SCAF-CTX` Functions, Capabilities, Services and logical dependency needs.

### `SCAF-ARCH-002` — Node-decomposition applicability

**Target:** Project-Applicable Obligation

The project **SHALL** determine whether Node decomposition is Applicable for representing independently meaningful architecture responsibilities, lifecycle/interaction identities, controlled obligations or subordinate-System abstractions at the current reasoning scope.

### `SCAF-ARCH-016` — Node-boundary decision, when Applicable

**Target:** Project-Applicable Obligation

Where Node decomposition is Applicable, the Project Design Authority **SHALL** define and justify Node boundaries using architecture criteria rather than automatically mapping Nodes to chips, boards, processes, threads, FPGA blocks or network endpoints.

A physical boundary or verification task alone **SHALL NOT** justify a Node boundary.

### `SCAF-ARCH-003` — Avoid gratuitous Nodes

**Target:** Project-Applicable Obligation

Where Node decomposition is Applicable, the project **SHALL NOT** create Nodes that add no distinct architecture decision, lifecycle/interaction identity, responsibility or controlled obligation.

Implementation entities that do not change architecture reasoning or authority may remain internal implementation details; this sentence is guidance, not an additional SHALL-level obligation.

### `SCAF-ARCH-004` — Role is contextual

**Target:** Project-Applicable Obligation

The project **SHALL** treat Role as a contextual responsibility relation rather than a mandatory containment child of Node.

Where one participant plays multiple Roles and the distinction is material, the project **SHALL** identify the relevant context sufficiently to prevent responsibility, authority or interaction ambiguity.

### `SCAF-ARCH-005` — Capability and Service responsibility allocation

**Target:** Project-Applicable Obligation

The project **SHALL** allocate required Capabilities and Service provider/consumer responsibilities to the applicable System and/or Node responsibilities represented by the frozen core metamodel, using Role to qualify contextual responsibility where needed.

The allocation **SHALL** remain distinguishable from the implementation technology used to realize it.

### `SCAF-ARCH-006` — Structural topology and realization dependencies

**Target:** Project-Applicable Obligation

Where structural realization dependencies exist, the Project Design Authority **SHALL** define the topology and dependencies necessary to realize the applicable CTX logical needs.

### `SCAF-ARCH-007` — Domain boundaries

**Target:** Project-Applicable Obligation

Where a fault, reset, power, security/trust, resource, clock/time or other justified Domain is material to architecture behavior, the Project Design Authority **SHALL** define that Domain boundary and its relation to relevant Systems, Nodes and Services.

A Domain **MAY** align with, subdivide or cross Node boundaries.

The project **SHALL NOT** assume Node boundary and Domain boundary are equivalent without an explicit architecture rationale.

### `SCAF-ARCH-008` — Containment-structure input to robustness analysis

**Target:** Project-Applicable Obligation

Where containment reasoning is Applicable, the Project Design Authority **SHALL** identify the actual structural/Domain boundaries that are inputs to downstream `SCAF-ROB` containment analysis.

### `SCAF-ARCH-009` — Subordinate System versus subordinate Node

**Target:** Project-Applicable Obligation

When an element has its own bounded System scope and its own SCAF application, the project **SHALL** treat it as a subordinate System for that scope.

When an element remains inside the current System's architecture authority and does not create a separately bounded SCAF application, it **MAY** be modeled as a subordinate Node when Node decomposition is Applicable.

If a subordinate System is abstracted as a participant/Node at a parent-System level, the abstraction and trace relation **SHALL** be explicit.

### `SCAF-ARCH-010` — Architecture decision authority trace

**Target:** Project-Applicable Obligation

Material `SCAF-ARCH` project decisions **SHALL** trace to the Project Design Authority designated under the SCAF Authority Kernel or to an explicit coordinated decision rule permitted by that kernel.

This requirement applies the kernel to `SCAF-ARCH`; it does not redefine Project Design Authority semantics.

### `SCAF-ARCH-011` — Architecture decision records

**Target:** Project-Applicable Obligation

Authoritative architecture artifacts **SHALL** record applicable `SCAF-ARCH` Controlled Decisions and authority provenance at a level sufficient for realization and verification trace.

This requirement does not make the artifact itself an authority role.

### `SCAF-ARCH-012` — Architecture change and re-evaluation

**Target:** Project-Applicable Obligation

Changes to Node decomposition/boundaries, responsibility allocation, topology, Domain boundaries, structural dependencies or subordinate-System abstraction **SHALL** trigger re-evaluation of affected interaction, timing, robustness, lifecycle, observability, configuration, security and verification obligations.

### `SCAF-ARCH-013` — Structural decision trace to motivating context

**Target:** Project-Applicable Obligation

Each material structural allocation, topology, Node/Domain boundary or subordinate-System abstraction decision **SHALL** trace to one or more applicable CTX Functions, Capabilities, Services, logical dependencies, consequences, assumptions or external constraints that motivate the decision.

### `SCAF-ARCH-014` — Logical versus structural dependency distinction

**Target:** Project-Applicable Obligation

The project **SHALL** keep `SCAF-CTX` logical Service dependencies distinguishable from `SCAF-ARCH` structural realization dependencies so that one logical dependency may be realized by one or more structural paths without changing its logical meaning.

### `SCAF-ARCH-015` — Shared dependency exposure

**Target:** Project-Applicable Obligation

Where a shared resource, shared provider or common infrastructure creates a material coupled-failure or capacity dependency, the project **SHALL** represent the affected structural dependency, participating System/Node responsibilities and shared dependency source so that downstream `SCAF-ROB` and `SCAF-TIME` obligations can reference the same controlled architecture relationship.

## 4. Framework Normative Invariants

### `SCAF-ARCH-017` — ARCH / ROB containment authority boundary

**Target:** Framework Normative Invariant

`SCAF-ARCH` **Defines Framework Semantics / Obligation** for structural and Domain-boundary representation used by containment reasoning.

`SCAF-ARCH` **SHALL NOT** define project runtime fault-containment response; runtime failure, containment and recovery-response semantics remain under `SCAF-ROB`.

## 5. Required Project Decisions / Records

The following table summarizes expected project outputs from the obligations above; it is informative and does not create additional normative requirements.

| Decision / record | Project-side authority / provenance |
|---|---|
| Node-decomposition applicability | Project Design Authority |
| Node boundaries and rationale, where applicable | Project Design Authority |
| Role assignments in context | Project Design Authority |
| Capability / Service responsibility allocation | Project Design Authority |
| Structural topology / dependencies | Project Design Authority |
| Domain boundaries and relation to System/Node/Service | Project Design Authority, constrained by applicable concern/external authorities |
| Subordinate System vs subordinate Node treatment | Project Design Authority |
| Controlled architecture artifact(s) | Records Project Design Authority decisions; artifact is not the authority role |

## 6. Concern Boundaries

- `SCAF-CTX` **Defines Framework Semantics / Obligation** for logical mission/function/service context and logical dependency semantics.
- `SCAF-INT` **Defines Framework Semantics / Obligation** for interface, interaction and data-contract semantics.
- `SCAF-TIME` **Defines Framework Semantics / Obligation** for timing, clock/timebase, synchronization, concurrency and capacity semantics.
- `SCAF-ROB` **Defines Framework Semantics / Obligation** for runtime failure/health/containment/recovery behavior using project ARCH structure/Domains.
- `SCAF-LIFE` **Defines Framework Semantics / Obligation** for boot/power/reset/update transaction and lifecycle semantics.
- `SCAF-SEC` **Constrains** architecture based on applicable project/external security-authority inputs.
- `SCAF-PROF` may **Constrain / Guide Realization**; **Project Realization** performs actual realization.
- `SCAF-ASSUR` **Defines Framework Semantics / Obligation** for assurance/evidence rules; **Project Verification / Assurance Authority Verifies** the project realization/decision against the Applicable Satisfaction Basis.

## 7. Non-Normative Example

A SoC, FPGA and DSP may be one Node, several Nodes, or a subordinate System plus Nodes depending on responsibility, lifecycle, interaction and authority boundaries. SCAF does not decide the count from technology names and does not require Node decomposition when it adds no independently meaningful architecture reasoning. The project makes the applicable structural decisions and then applies interaction, timing, robustness, lifecycle and assurance obligations to the resulting structure.
