# SCAF-TIME — Timing, Concurrency, Capacity & Resource Margin Obligations

**Release:** v0.0.2rc07  
**Concern:** `SCAF-TIME`  
**Layer:** L1 Concern Authority + L2 Required Project Decisions  
**Status:** Normative RC

## 1. Purpose

`SCAF-TIME` **Defines Framework Semantics / Obligation** for measurable temporal properties, timebase/synchronization semantics, and execution/concurrency, capacity and resource-margin constraints only insofar as they establish an explicitly TIME-owned measurable property that can affect system correctness, availability or verifiability.

`SCAF-TIME` does not own logical Service intent (`SCAF-CTX`), structural allocation (`SCAF-ARCH`), Interface/data-contract meaning (`SCAF-INT`), operational-state semantics (`SCAF-RUN`), runtime resilience response (`SCAF-ROB`) or implementation scheduling mechanisms (`SCAF-PROF` / Project Realization).

## 2. L1 Authority Boundary

`SCAF-TIME` **Defines Framework Semantics / Obligation** for:

- clock/timebase identity and authority;
- monotonic versus wall-clock semantics;
- synchronization, drift and uncertainty semantics;
- Time Epoch and Time Domain semantics;
- deadline, period, latency, jitter and temporal-budget semantics;
- execution/concurrency assumptions or constraints where required to establish measurable temporal, capacity, resource-budget or margin properties;
- queueing/backpressure/capacity semantics;
- bandwidth/throughput requirements;
- CPU, memory, stack, storage, programmable-logic and channel/resource budgets where material;
- margin/headroom and measurable starvation/fairness/overload constraints that bound a TIME-owned property;
- long-duration accumulation horizon and measurable bounded-growth obligations.

The **Project Design Authority Defines Project Instance / Decision** for actual project timebases, clock relationships, temporal limits, synchronization tolerances, TIME-owned execution/concurrency constraints, capacity/resource budgets and margin values.

`SCAF-TIME` **Defines Framework Semantics / Obligation** for the temporal/resource property to be controlled; Project Realization implements the project decision using applicable mechanisms, and Project Verification / Assurance Authority verifies it against the Applicable Satisfaction Basis.

## 3. Project-Applicable Obligations

### `SCAF-TIME-001` — Material temporal/capacity property identification

**Target:** Project-Applicable Obligation

The project **SHALL** identify temporal, TIME-owned execution/concurrency, capacity or resource-margin properties whose violation can materially affect an applicable Function, Capability, Service, Interaction, architecture decision or verification claim.

### `SCAF-TIME-002` — Timebase identity and authority

**Target:** Project-Applicable Obligation

Where a project property depends on measuring, comparing or chronologically ordering temporal observations, the Project Design Authority **SHALL** define the applicable timebase/clock identity and the authority that establishes the project value or relationship.

### `SCAF-TIME-003` — Monotonic versus wall-clock semantics

**Target:** Project-Applicable Obligation

Where both elapsed-time/chronological-ordering semantics and calendar/wall-clock semantics are used, the project **SHALL** distinguish them and define any relied-upon relationship or conversion sufficiently to prevent one from being substituted for the other without an explicit decision.

### `SCAF-TIME-004` — Synchronization, drift and uncertainty

**Target:** Project-Applicable Obligation

Where timestamps, deadlines, freshness, chronological ordering or coordinated temporal behavior depend on more than one clock/timebase, the project **SHALL** define the required synchronization relationship, permitted drift/offset/uncertainty and the conditions under which the relationship is considered usable.

### `SCAF-TIME-020` — Dependent temporal-claim validity under clock-relationship loss

**Target:** Project-Applicable Obligation

Where a temporal claim depends on a synchronization or clock/timebase relationship, the project **SHALL** identify that dependency and define whether the claim remains valid, becomes invalid, or enters a controlled degraded/re-evaluation state when the required relationship is not usable.

The project **SHALL** trace any resulting contract, operational-state or resilience consequence to the applicable controlled `SCAF-INT`, `SCAF-RUN` or `SCAF-ROB` requirement, decision or obligation as available in the current project/framework stage. `SCAF-TIME` does not define the downstream runtime or resilience response.

### `SCAF-TIME-005` — Time Domain and Time Epoch

**Target:** Project-Applicable Obligation

Where multiple time domains or time origins can coexist, restart or change, the project **SHALL** define the applicable Time Domain / Time Epoch semantics and the relationships needed to interpret temporal values without ambiguity.

### `SCAF-TIME-006` — Deadlines, periods, latency and jitter

**Target:** Project-Applicable Obligation

Where deadline, period, latency or jitter materially affects correctness or required Service behavior, the Project Design Authority **SHALL** define the applicable measurable temporal requirement, reference points and project value/tolerance.

### `SCAF-TIME-007` — Freshness temporal evaluation

**Target:** Project-Applicable Obligation

Where an applicable `SCAF-INT` contract uses age/freshness to distinguish current, stale, expired or invalid information, the Project Design Authority **SHALL** define the measurable age reference, timebase, threshold/tolerance and uncertainty needed to evaluate that contract.

This requirement supplies temporal evaluation semantics; `SCAF-INT` retains authority for the contract meaning of the freshness state.

### `SCAF-TIME-008` — TIME-owned concurrency and interference constraints

**Target:** Project-Applicable Obligation

Where concurrent execution, access or scheduling can materially affect a measurable temporal, capacity, resource-budget, margin or other explicitly `SCAF-TIME`-owned property, the project **SHALL** define the architecture-level concurrency assumption or constraint needed to establish that property.

**Boundary note (informative):** The obligation may constrain simultaneous activity, interference, serialization/parallelism assumptions, service capacity or priority relationships at architecture level. Framework authority for Interface semantic ordering, runtime state/transition consistency and resilience/recovery behavior is defined by `SCAF-TIME-019`.

### `SCAF-TIME-009` — Queueing / backpressure / bounded demand

**Target:** Project-Applicable Obligation

Where produced demand can exceed service capacity or buffering can grow, the project **SHALL** define the applicable boundedness, queue/capacity and backpressure/admission requirement needed to prevent uncontrolled accumulation or hidden loss of timing/capacity assumptions.

### `SCAF-TIME-010` — Bandwidth and throughput

**Target:** Project-Applicable Obligation

Where bandwidth or throughput is material, the Project Design Authority **SHALL** define the required capacity, expected demand basis and applicable margin/tolerance.

### `SCAF-TIME-011` — Resource budgets and margin

**Target:** Project-Applicable Obligation

Where CPU, memory, stack, storage, programmable-logic, channel or another finite resource can constrain an applicable architecture property, the project **SHALL** define a controlled budget and required margin/headroom or an explicit rationale that no separate margin is required.

### `SCAF-TIME-012` — Starvation, fairness and overload bounds

**Target:** Project-Applicable Obligation

Where starvation, unfair service, scheduling interference or overload can materially violate a required temporal/capacity property, the project **SHALL** define the measurable unacceptable condition, applicable limit/bound and architecture-level constraint needed to prevent or bound loss of that TIME-owned property.

**Boundary note (informative):** This obligation defines the measurable condition and bound. Framework authority for detection/health classification, containment, degradation and recovery after violation is preserved by `SCAF-TIME-018`.

### `SCAF-TIME-013` — Long-duration accumulation / measurable bounded growth

**Target:** Project-Applicable Obligation

Where counters, queues, retained data, resource consumption, drift, error accumulation or another long-duration quantity can grow with operation time and affect a TIME-owned property, the project **SHALL** define the applicable accumulation model or basis, intended operating horizon, measurable bound/capacity and required margin needed to preserve that property.

**Boundary note (informative):** This requirement defines measurable boundedness only. Detection of exhaustion/violation and rollover, renewal, degradation, containment or recovery behavior are governed by the applicable concern according to the behavior being controlled; `SCAF-TIME-018` preserves the ROB-side detection/recovery boundary.

### `SCAF-TIME-014` — Timing/capacity traceability

**Target:** Project-Applicable Obligation

Each material temporal, TIME-owned execution/concurrency, capacity or resource-budget decision **SHALL** trace to the applicable CTX need, ARCH dependency/resource relationship, INT contract, RUN state requirement or other controlled source that motivates the decision.

### `SCAF-TIME-015` — Change and re-evaluation

**Target:** Project-Applicable Obligation

Changes to timebase, synchronization, clock relationship, temporal threshold, TIME-owned execution/concurrency constraint, workload/demand, capacity, resource budget or margin **SHALL** trigger re-evaluation of affected Interface, runtime, robustness, lifecycle, observability, security and verification obligations.

## 4. Framework Normative Invariants

### `SCAF-TIME-016` — INT / TIME temporal-contract boundary

**Target:** Framework Normative Invariant

`SCAF-INT` **Defines Framework Semantics / Obligation** for the semantic meaning of validity/freshness states and semantic ordering in an Interface/Interaction contract.

`SCAF-TIME` **Defines Framework Semantics / Obligation** for measurable age, deadline, period, latency, jitter, timebase, synchronization, chronological relationships and temporal-uncertainty semantics used to evaluate applicable temporal properties.

Neither concern **SHALL** silently absorb the other's project-instance decision authority.

### `SCAF-TIME-017` — Time / incarnation identity partition

**Target:** Framework Normative Invariant

Time Epoch / Time Domain semantics belong to `SCAF-TIME`.

Boot Incarnation / Boot Generation belongs to `SCAF-LIFE`; Protocol/Connection Session Identity belongs to `SCAF-INT`; Operational Incarnation belongs to `SCAF-RUN`; `SCAF-OBS` records these identities, time provenance and correlation metadata without redefining their primary semantics.

### `SCAF-TIME-018` — TIME / ROB / PROF realization boundary

**Target:** Framework Normative Invariant

`SCAF-TIME` **Defines Framework Semantics / Obligation** for temporal/capacity/resource bounds, budgets, thresholds, horizons and required margins.

`SCAF-TIME` **SHALL NOT** define detection/health classification, containment, degradation, recovery or reintegration after timing/capacity/resource violation (`SCAF-ROB`), nor define rollover/renewal or other response behavior solely because a measurable bound is reached; those behaviors remain with the applicable lifecycle, interaction, runtime or robustness authority. `SCAF-TIME` also **SHALL NOT** prescribe technology/runtime-specific realization mechanisms (`SCAF-PROF` guidance / Project Realization).

### `SCAF-TIME-019` — TIME / INT / RUN concurrency and ordering boundary

**Target:** Framework Normative Invariant

`SCAF-TIME` **Defines Framework Semantics / Obligation** for architecture-level execution/concurrency assumptions or constraints only where they are required to establish an explicitly TIME-owned measurable temporal, capacity, resource-budget or margin property.

`SCAF-INT` retains primary framework semantic authority for Interface/Interaction semantic ordering. `SCAF-RUN` retains primary framework semantic authority for operational-state and state-transition consistency. `SCAF-ROB` retains primary framework semantic authority for resilience/recovery behavior after concurrency-related property violation.

`SCAF-TIME` **SHALL NOT** use generic concurrency correctness or generic ordering as a basis to absorb those authorities.

## 5. Required Project Decisions / Records

The following table is informative and does not create additional normative requirements.

| Decision / record | Project-side authority / provenance |
|---|---|
| Material timing/capacity property inventory | Project Design Authority |
| Timebase / clock identity and authority | Project Design Authority |
| Synchronization / drift / uncertainty model | Project Design Authority |
| Dependent temporal-claim validity / re-evaluation on clock-relationship loss | Project Design Authority, traced to applicable INT/RUN/ROB controlled requirement or decision |
| Time Domain / Time Epoch model | Project Design Authority |
| Deadline / period / latency / jitter values | Project Design Authority |
| Freshness age/timebase/threshold values | Project Design Authority, constrained by `SCAF-INT` contract semantics |
| Concurrency architecture constraints for explicitly TIME-owned measurable properties | Project Design Authority |
| Queue/capacity/backpressure requirements | Project Design Authority |
| Bandwidth / throughput budget | Project Design Authority |
| Resource budgets / margins | Project Design Authority |
| Long-duration accumulation horizon / measurable bound / margin | Project Design Authority, constrained by applicable concern/external authorities |

`SCAF-APP` may Disposition / Trace these decisions but does not own them.

## 6. Concern Boundaries

- `SCAF-CTX` **Defines Framework Semantics / Obligation** for mission/Service need and consequence context.
- `SCAF-ARCH` **Defines Framework Semantics / Obligation** for structural resource/dependency relationships.
- `SCAF-INT` **Defines Framework Semantics / Obligation** for Interface/Interaction validity, freshness-state and ordering contract meaning.
- `SCAF-RUN` **Defines Framework Semantics / Obligation** for service/operational state and operational-incarnation semantics.
- `SCAF-TIME` **Defines Framework Semantics / Obligation** for measurable temporal, synchronization, TIME-owned execution/concurrency, capacity and margin properties.
- `SCAF-ROB` **Defines Framework Semantics / Obligation** for resilience/containment/recovery behavior when timing/capacity/resource assumptions fail.
- `SCAF-LIFE` **Defines Framework Semantics / Obligation** for boot/reset/power/update lifecycle identities and sequencing.
- `SCAF-OBS` **Observes** and records time/session/incarnation provenance and synchronization quality as evidence.
- `SCAF-PROF` may **Constrain / Guide Realization**; Project Realization implements scheduling, synchronization, buffering and resource mechanisms.
- `SCAF-ASSUR` **Defines Framework Semantics / Obligation** for assurance/evidence semantics; Project Verification / Assurance Authority **Verifies** applicable TIME obligations against the Applicable Satisfaction Basis.

## 7. Non-Normative Example

A telemetry contract may define that data becomes stale after a project-defined age. `SCAF-INT` defines the framework semantic distinction between current and stale data; `SCAF-TIME` requires the project to define the timebase, age reference, threshold and uncertainty used to evaluate the distinction. Whether the project realizes that timing using an RTOS timer, FPGA counter, operating-system clock or another mechanism is outside L1/L2 normative scope.
