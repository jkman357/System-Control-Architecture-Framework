# Overlap, Obsolescence and Gap Analysis

## 1. Purpose

This document identifies structural problems that must be resolved before or during controlled SCAF normative rewriting.

## 2. Primary Structural Finding

Gen1 contains substantial reusable engineering content. The main migration risk is not missing documents; it is **duplicate or ambiguous authority created by Gen1 role/document boundaries and by rc1's mixed taxonomy dimensions**.

The frozen v0.0.1 baseline treats the authority kernel as closed enough for controlled normative rewrite while preserving explicit promotion/migration gates.

## 3. Resolved / Substantially Improved through rc05

### 3.1 Mixed taxonomy planes

rc1 placed system concerns, project application, assurance, implementation, tooling and engineering process as peer branches.

**rc05 retained/closure decision:** separate five authority planes and make tooling/AI supporting mechanisms rather than peer system concerns.

### 3.2 Node-centric replacement risk

Replacing Host/Device with Node alone is insufficient.

**rc05 retained/closure decision:** add Function/Service/Capability, Interface, Interaction and cross-cutting Domains as first-class metamodel concepts; define Node boundary criteria.

### 3.3 Migration action vocabulary

rc1 mixed `Keep/Move/Merge/Rewrite/Retire/New` with `Elevate/Generalize/Rebuild`.

**rc05 retained/closure decision:** separate **Disposition** from **Transformation**.

### 3.4 Framework Scan state mixing

Applicability, risk, decision, verification and evidence are different state axes.

**rc05 retained/closure decision:** model them as independent dimensions in a single decision/evidence lifecycle.

### 3.5 Linear fault lifecycle

`Prevention -> Detection -> Containment -> Recovery` mixes design-time assurance with runtime behavior.

**rc05 retained/closure decision:** separate fault/error/failure semantics, runtime resilience response and assurance.

## 4. Remaining Authority-Overlap Risks

### 4.1 Freshness

Potential donors/consumers: Interface, Timing, Robustness and Security.

Resolution rule:

- `SCAF-INT` **Defines Framework Semantics / Obligation** for data validity, age and ordering; the Project Design Authority defines the project-specific contract;
- `SCAF-TIME` constrains the project contract with measurable temporal semantics and budgets;
- `SCAF-ROB` **Defines Framework Semantics / Obligation** for behavior after freshness loss;
- `SCAF-SEC` constrains hostile/replay freshness requirements based on applicable security authority inputs;
- `SCAF-ASSUR` **Defines Framework Semantics / Obligation** for assurance/evidence rules; the Project Verification / Assurance Authority **Verifies**.

### 4.2 Containment

Potential donors/consumers: Architecture, Robustness and Security.

Resolution rule:

- `SCAF-ARCH` **Defines Framework Semantics / Obligation** for Domain-boundary semantics; the Project Design Authority defines project-specific boundaries;
- `SCAF-ROB` **Defines Framework Semantics / Obligation** for runtime fault-containment behavior;
- `SCAF-SEC` constrains adversarial containment requirements;
- `SCAF-PROF` may guide/constrain realization mechanisms; Project Realization implements them;
- `SCAF-ASSUR` **Defines Framework Semantics / Obligation** for assurance/evidence rules; Project Verification / Assurance Authority **Verifies**.

### 4.3 Lifecycle

Lifecycle currently appears in Node behavior, session/connection behavior, boot/update and credentials.

Resolution rule:

- `SCAF-RUN` **Defines Framework Semantics / Obligation** for service/operational-state lifecycle;
- `SCAF-LIFE` **Defines Framework Semantics / Obligation** for boot/power/reset/update lifecycle;
- `SCAF-INT` **Defines Framework Semantics / Obligation** for interface/session lifecycle contracts;
- `SCAF-CFG` **Defines Framework Semantics / Obligation** for configuration lifecycle;
- `SCAF-SEC` defines/constrains credential/security lifecycle architecture obligations based on applicable security authority inputs.

Each must state its relation rather than claiming generic lifecycle authority.

### 4.4 Evidence

Runtime incident evidence and verification evidence are related but not identical.

Resolution rule:

- `SCAF-OBS` **Defines Framework Semantics / Obligation** for operational, diagnostic and incident evidence;
- `SCAF-ASSUR` **Defines Framework Semantics / Obligation** for verification/evidence-sufficiency criteria; Project Verification / Assurance Authority evaluates project evidence against the Applicable Satisfaction Basis; underlying requirement/design/risk/deviation authorities retain their applicable closure roles;
- runtime evidence may become assurance evidence only when provenance, identity, reproducibility/interpretability and acceptance conditions are satisfied.

## 5. Outdated or Too-Narrow Gen1 Framing

| Gen1 framing | SCAF treatment |
|---|---|
| Host / Device as primary architecture | Retire as top-level taxonomy; preserve only where project roles truly match |
| Coordinator / Node as parallel document domains | Replace with System/Service/Node/Role/Interaction/Domain model |
| Embedded system as framework boundary | Move embedded constraints to realization profiles |
| Protocol as dominant interface form | Generalize to broader interface/interaction contracts |
| Coordinator UI/concurrency/logging as general architecture | Split system properties from desktop/HMI realization mechanisms |
| Validation checklist mirroring document folders | Regenerate only after concern authorities stabilize |
| Repository paths as governance authority | Preserve governance intent; rebuild path-specific enforcement later |
| Secure session as primary security model | Keep as profile; broaden to system security robustness |

## 6. Robustness / Resilience Coverage Requiring Normative Elaboration

### 6.1 Fault / Error / Failure semantics

SCAF now has an explicit semantic home and separation:

```text
Fault source / condition
  -> activation
  -> erroneous state
  -> propagation
  -> service failure
  -> system consequence
```

This is now an explicit `SCAF-ROB` concern and must precede detailed normative rules.

### 6.2 Fault-tolerance mechanisms

Gen1 and the Crash Recorder contain detection, watchdog, degradation, recovery and evidence ideas. `SCAF-ROB` now provides the authority home; controlled normative elaboration must cover:

- redundancy;
- failover;
- masking/tolerance;
- reconfiguration;
- repair;
- state resynchronization;
- reintegration;
- recovery after prolonged degraded operation.

### 6.3 Diagnostic coverage and latent faults

Controlled normative elaboration must ask:

- which faults are detectable;
- maximum detection latency;
- which faults remain latent;
- health-monitor failure behavior;
- diagnostic coverage evidence;
- whether a degraded monitor can falsely indicate health.

### 6.4 Distributed failure semantics

`SCAF-ROB` is the primary framework semantic authority for these heterogeneous/multi-node failure concerns; normative elaboration must cover:

- network partition;
- split brain / stale ownership;
- reconnect reconciliation;
- replay after reconnect;
- correlated/common-mode failures;
- cascading recovery;
- recovery storms;
- peer recovery dependencies.

### 6.5 Safe State authority boundary

`Safe State` cannot be universally invented by SCAF.

For safety-relevant projects, project safety/hazard authority must define the safety-significant condition/strategy. SCAF may define:

- which project authority owns entry/exit decisions;
- state-transition behavior;
- interaction requirements;
- observability;
- verification/evidence obligations.

### 6.6 Long-run robustness

Requires first-class normative coverage within `SCAF-ROB`:

- counter wrap;
- timestamp wrap;
- queue/backlog accumulation;
- storage/log growth;
- fragmentation where applicable;
- retry escalation;
- leaked state/resources;
- persistent-state drift;
- clock drift / resynchronization;
- wear / endurance;
- repeated recovery stress.

## 7. Function / Service / Dependency Coverage Requiring Normative Elaboration

A Node-health model alone is insufficient. System consequence is expressed through service/function loss or degradation.

`SCAF-CTX` now provides the authority home; controlled normative elaboration must cover:

- required System Function / Service;
- provider(s);
- consumer(s);
- dependencies;
- criticality / mission impact;
- degraded service level;
- availability/recovery priority;
- alternative/redundant providers where applicable.

This is essential for meaningful graceful degradation, failover and safe behavior.

## 8. Configuration / Persistent Operational State Coverage Requiring Normative Elaboration

Gen1 explicitly contains configuration and persistence, but rc1 did not provide a clear authority home.

`SCAF-CFG` is the primary framework semantic authority for:

- configuration ownership;
- defaults;
- provisioning;
- validation;
- version/migration;
- atomic update/commit;
- persistence;
- rollback/recovery after corruption;
- calibration/parameter state;
- synchronization across nodes;
- distinction between configuration persistence and incident-evidence persistence.

## 9. Distributed Incident Evidence Coverage Requiring Normative Elaboration

Single-node timestamps are not enough for system-level incident reconstruction.

SCAF now has authority homes for these concepts; controlled normative elaboration must preserve:

- timestamp provenance;
- clock source;
- synchronization state/quality;
- uncertainty bounds where available;
- time epoch/time-domain provenance (`SCAF-TIME`), boot incarnation (`SCAF-LIFE`), protocol/session identity (`SCAF-INT`) and operational incarnation where applicable (`SCAF-RUN`), recorded/correlated by `SCAF-OBS`;
- local ordering;
- cross-node correlation ID;
- causal correlation when synchronized wall time is unavailable.

## 10. Implementation Profile Composition Risk

rc1 mixed platform, execution model, language, HMI, transport, storage and reference architecture in one profile list.

v0.0.1 retains profiles as composable axes:

```text
Compute / deployment technology
Execution model
Language / runtime
Interaction / transport realization
Persistence / storage realization
Human-interface realization
Optional reference architecture / subsystem pattern
```

A project may select several axes simultaneously. Profiles do not own or realize the project requirement; they guide/constrain Project Realization.

## 11. Machine-Verifiable Tooling Gap

Gen1 has schemas, validators, fixtures and CI. Their concepts are valuable, but their executable form is coupled to Gen1 structure.

Current decision:

```text
Do not copy CI.
Do not freeze schema.
Do not migrate validators yet.
Do not lose their semantic invariants.
```

Before SCAF tooling is rebuilt, the deep audit must mine invariants that exist only in tests/schema/validators.

## 12. Initial Controlled Rewrite Priorities

Initial controlled L1/L2 rewrite priorities before broad normative expansion / donor promotion / freeze:

1. begin controlled L1/L2 normative elaboration using the closed authority kernel;
2. preserve the canonical concern -> Project Design -> Realization -> Assurance chain and APP cross-cut trace in every rewritten concern;
3. confirm individual source/maturity/anchor evidence before promoting donor-derived normative statements, especially Draft/RC and mixed-donor concepts;
4. extract schema/test/validator executable invariants before claiming migration completeness or promoting rules that depend on them;
5. keep top-level taxonomy closed unless a real project application demonstrates an authority-home failure that cannot be resolved within the current model.

The current task is **controlled normative elaboration with authority preservation**, not taxonomy expansion or document-count growth.


## v0.0.1 Frozen Authority-Kernel Baseline Note

rc05 retains the separation of SCAF normative concern authority from Project Design Authority and makes the canonical chain explicit: SCAF defines framework semantics/obligations; Project Design Authority defines project-specific architecture values; Project Realization implements them; `SCAF-ASSUR` defines assurance semantics while the Project Verification / Assurance Authority verifies/evaluates project evidence; `SCAF-APP` cross-cuts by dispositioning/tracing state and closure. Framework Scan and assurance artifacts therefore do not become duplicate design authorities.

Additional closure rules:

- `SCAF-LIFE` is primary framework semantic authority for lifecycle transaction/state semantics; `SCAF-ROB` is primary framework semantic authority for failure-response properties when those lifecycle operations fail.
- `SCAF-ROB` is primary framework semantic authority for health/failure decision and resilience response; `SCAF-OBS` is primary framework semantic authority for observation/representation/preservation/export of health and incident evidence.
- external/project Security Authority retains threat assumptions, security objectives and risk acceptance in its scope; Project Design Authority Defines Project Instance / Decision for the actual integrated architecture decisions.
- controlled normative rewrite is now permitted, but Draft/RC donor promotion, executable-invariant migration and final migration proof remain gated.
- the five authority planes are SCAF framework planes; Project Design Authority remains a project-side bridge, not a sixth SCAF plane.
- time epoch, boot incarnation, protocol/session identity and operational incarnation are distinct semantics; `SCAF-OBS` records their provenance rather than re-owning them.
- Framework Scan uses an **Applicable Satisfaction Basis** trace rather than implying that one source concern alone owns every project acceptance condition.
