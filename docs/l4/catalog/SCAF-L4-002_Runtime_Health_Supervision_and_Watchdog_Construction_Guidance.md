# SCAF-L4-002 — Runtime Health Supervision and Watchdog Construction Guidance

**Development Release:** v0.1.0rc03  
**Guidance Identity:** `SCAF-L4-002`  
**Status:** Candidate allocation; becomes accepted only if the rc03 candidate is accepted and committed  
**Primary L3 Trace:** `SCAF-PAT-SUP-001`, `SCAF-PAT-SUP-002`  
**Construction Position:** Platform-neutral runtime supervision / watchdog guidance; not Project Design Authority

## 1. Purpose

Provide a construction-ready, platform-neutral realization shape for projects that combine recurring/progress-coupled liveness evidence with a sufficiently independent watchdog or supervisory escalation mechanism.

The guidance is intended to help an engineer or AI consumer begin implementation without silently inventing:

- what counts as progress or health;
- who evaluates health;
- who may service or preserve the watchdog;
- timing values;
- startup / maintenance / degraded-mode behavior;
- reset/recovery scope;
- evidence-retention policy;
- platform APIs or watchdog hardware.

The governing separation remains:

```text
liveness evidence != complete health proof
watchdog expiry != root-cause proof
L4 guidance != Project Design Authority
L4 Verification Intent != verification result
Construction Ready != buildable / correct / verified / compliant / closed
```

## 2. Trace and Authority Boundary

### 2.1 Primary L3 trace

```text
SCAF-PAT-SUP-001 — Heartbeat / Liveness Supervision ─┐
                                                     ├─> SCAF-L4-002
SCAF-PAT-SUP-002 — Independent Watchdog with Escalation ┘
```

This intentionally exercises the accepted rc01 many-to-many trace model. The L4 guidance composes two accepted L3 mechanisms without merging their authority ownership.

### 2.2 Frozen L2 basis inherited from the two L3 Patterns

From `SCAF-PAT-SUP-001`:

- Primary: `SCAF-ROB-004`, `SCAF-ROB-005`;
- Supporting: `SCAF-ROB-031`, `SCAF-OBS-014`, `SCAF-OBS-015`;
- Constraint inputs: `SCAF-TIME-002`, `SCAF-TIME-006`, and `SCAF-INT-010` where session/incarnation identity is material.

From `SCAF-PAT-SUP-002`:

- Primary: `SCAF-ROB-006`;
- Supporting: `SCAF-ROB-005`, `SCAF-ROB-011`;
- Constraint inputs: `SCAF-TIME-006`, `SCAF-LIFE-008`, `SCAF-LIFE-009`.

Where repeated recovery/escalation is separately selected, applicable retry/escalation termination semantics remain owned by the applicable ROB/RUN project decision rather than by this L4 guidance.

### 2.3 What the trace does not mean

```text
L3 Pattern available != project adopts SCAF-L4-002
L3 Pattern selected != SCAF-L4-002 automatically selected
SCAF-L4-002 used != watchdog reset automatically required
heartbeat observed != complete system healthy
watchdog expiry != causal diagnosis
```

Concrete project health classifications, progress criteria, escalation target, reset semantics and verification acceptance remain Project Design Authority / Project Verification / Assurance responsibilities.

## 3. Construction Preconditions and Not-Suitable Conditions

### 3.1 Construction preconditions

Use this guidance when the project has, or intends to establish:

- one or more runtime responsibilities whose continued progress/liveness is material;
- a project-defined observation that can represent that progress/liveness with controlled identity and timing;
- a supervising responsibility that evaluates the observation;
- a watchdog/supervisory escalation path with project-defined independence from the supervised execution context;
- a controlled consequence when required progress cannot be established;
- lifecycle semantics for startup, restart/reset, intentional suspension/maintenance and recovery where those states are material.

These are L4 construction preconditions, not Project Application dispositions.

### 3.2 Not suitable when

This guidance is weak or unsuitable when:

- silence/absence cannot be distinguished from valid normal behavior and no alternate progress evidence exists;
- the chosen heartbeat/progress indication can continue while the material Function/Service is stalled and the limitation is not otherwise controlled;
- the supervisor/watchdog shares all material failure dependencies with the supervised context and no useful independence claim can be established;
- watchdog expiry has no controlled project consequence;
- restart/reset/session changes can make stale progress evidence appear current and no identity mechanism exists;
- the project intentionally relies on a different supervision mechanism that owns the same construction concern.

Absence of this L4 guidance does not make upstream ROB/TIME/LIFE/OBS/INT concerns non-applicable.

## 4. Recommended Implementation Shape

A generic construction shape is:

```text
Monitored responsibility / Service / execution context
        ↓
Progress / liveness evidence
  - identity / incarnation / session as needed
  - progress token / heartbeat / milestone / useful traffic evidence
        ↓
Supervision Evaluation Responsibility
  - timebase / age / progress evaluation
  - project health/liveness classification input
  - supervisor self-validity / observation validity
        ↓
Watchdog Service Eligibility Decision
  - may service / preserve watchdog only when project-defined conditions allow
        ↓
Independent Watchdog / Supervisory Expiry Mechanism
        ↓ expiry / invalid supervision result
Project-owned Escalation / Recovery Path
  - restart / reset / isolation / failover / degradation / other controlled response
        ↓
Lifecycle consequence + retained/diagnostic evidence as applicable
```

The construction boundary is not a specific heartbeat packet, timer peripheral or RTOS task. The project must be able to answer:

```text
What property proves required progress?
Who decides whether the evidence is current and sufficient?
Who can authorize watchdog servicing?
What happens when evidence is missing / stale / invalid / indeterminate?
What happens when the supervisor itself is unavailable or invalid?
What timing relationship keeps healthy operation alive while still bounding failed progress?
What evidence survives or remains observable when escalation occurs?
```

## 5. Construction Constraints

A realization claiming this guidance shall preserve the following within its declared scope:

1. **Progress evidence is semantically controlled.** The supervised indication represents the project-defined liveness/progress property rather than merely proving that some task, scheduler, interrupt or transport path is active.
2. **Watchdog service cannot silently bypass health evaluation.** A supervised component shall not independently preserve the final supervision/watchdog healthy outcome in a way that can mask loss of required project health/progress.
3. **Service eligibility is explicit.** The project defines the conditions under which watchdog servicing/preservation is allowed, including required participant coverage and supervisor/observation validity.
4. **Missing/invalid evidence is not automatically healthy.** Unknown, unavailable, stale, session-mismatched or indeterminate supervision input follows a project-defined consequence and shall not silently preserve an unqualified healthy state.
5. **Supervisor failure semantics are controlled.** Failure, unavailability, disagreement or invalid output of the supervision responsibility cannot silently become proof of healthy operation.
6. **Timing relationships are project-controlled.** Progress interval/deadline, evaluation cadence/tolerance, watchdog service/expiry bound and escalation timing are explicit project values/relationships where material.
7. **Lifecycle mode is explicit.** Startup, partial initialization, maintenance, intentional suspension, update, degraded operation and recovery cannot rely on an indefinite implicit grace state that defeats the supervision claim.
8. **Incarnation/session freshness is preserved.** Where restart/reconnection/reuse can make old evidence ambiguous, stale evidence cannot satisfy current supervision merely because its value appears syntactically valid.
9. **Independence is analyzed, not assumed.** Supervisor/watchdog separation is stated in terms of project-relevant shared scheduler/process/reset/power/clock/communication/resource dependencies.
10. **Escalation does not erase authority boundaries.** Watchdog expiry may trigger or authorize a project-selected response but does not itself define the root cause, reset class, reset domain, safety consequence or final recovery outcome.
11. **Evidence needed for the claimed behavior is not silently destroyed.** Where evidence around expiry/escalation is material and reasonably producible, the project defines capture/retention ordering sufficient to support diagnosis without pretending that evidence is root-cause proof.
12. **Repeated escalation is bounded by separately owned policy.** If reset/restart/recovery can repeat, the applicable project recovery/termination policy controls reset-loop or retry-loop behavior; this L4 guidance does not create unbounded repeated recovery authority.

These constraints preserve the claimed construction realization. They do not create new universal L1/L2 obligations.

## 6. Construction Invariants

Valid realization variations shall preserve, as applicable:

- each required monitored responsibility has an unambiguous supervision identity and current-incarnation/session interpretation;
- progress/liveness evidence used for a health decision is attributable to the responsibility/property being supervised;
- one participant's healthy evidence cannot silently substitute for another required participant's missing or invalid evidence;
- watchdog servicing/preservation follows a controlled eligibility decision rather than unconditional activity in the supervised context;
- supervisor/observation invalidity cannot silently produce an unqualified healthy result;
- timing used for age/deadline/expiry evaluation uses a project-controlled timebase and defined reference points;
- intentional lifecycle exceptions are bounded and transition back to normal supervision through explicit project conditions;
- escalation cause/effect is distinguishable from root-cause diagnosis;
- reset/restart consequences preserve project reset-domain and retained-state/evidence semantics;
- instrumentation used to claim supervision behavior is sufficient to distinguish progress evidence, supervisor decision, watchdog service/expiry and resulting escalation at the resolution required by the project.

A materially different realization may adapt an invariant only through Project Design Authority with rationale proportional to the resulting behavior/verification impact.

## 7. Construction Assumptions

This guidance does not turn these assumptions into project facts. Confirm, replace or reject each material assumption relied upon:

- heartbeat/progress generation itself does not materially disturb the property being observed;
- the selected progress evidence stops or becomes detectably invalid when the material responsibility stops progressing;
- supervisor execution has enough scheduling/resource opportunity to evaluate health within the project timing model;
- the watchdog/supervisory mechanism continues operating under the failure conditions for which independence is claimed;
- any shared clock, power, reset, memory, interrupt, communication or scheduler dependency is included in the independence argument;
- intentional suspension/maintenance/update states are observable before ordinary progress evidence is intentionally absent;
- a restart/reset creates or updates any required boot/operational/session/incarnation identity before stale evidence can be consumed as current;
- evidence intended to survive escalation is captured/retained before the relevant reset/restart invalidates it;
- the escalation target can actually produce the recovery/containment outcome claimed elsewhere by the project.

```text
L4 assumption != project fact
```

## 8. Required Project Decisions

L4 identifies the decision categories; Project Design Authority supplies the project values and policies.

### 8.1 Monitored set and progress semantics

Define:

- monitored participant / Service / execution responsibility;
- exact material property that must demonstrate progress or presence;
- whether evidence means liveness, useful progress, milestone completion, service availability or another controlled property;
- required participant set and whether any participant is optional, degraded-mode-only or mode-dependent;
- meaning of healthy, late, missing, stale, invalid, unknown and indeterminate observation as applicable.

### 8.2 Progress / heartbeat representation

Define:

- evidence source and owner;
- push heartbeat, poll/read token, monotonic progress counter, milestone/event, useful-traffic evidence or another representation;
- counter/token width and rollover semantics if material;
- identity / session / incarnation correlation;
- whether duplicate evidence or unchanged progress values count as progress;
- whether useful traffic proves the material service property or only transport activity.

No representation listed here is the SCAF default.

### 8.3 Supervision ownership and independence

Define:

- responsibility that evaluates progress/age;
- owner of the authoritative supervision result used by this realization;
- responsibility authorized to service/preserve the watchdog;
- required separation from supervised scheduler/process/reset/power/clock/resource domains;
- behavior if the supervisor itself stalls, disagrees with another monitor, loses its observation source or reports invalid data.

### 8.4 Timing relationship

Define where materially applicable:

- supervision timebase;
- heartbeat/progress production expectation;
- age/deadline/tolerance and jitter basis;
- maximum acceptable detection latency;
- supervisor evaluation cadence and worst credible evaluation delay;
- watchdog service window / expiry bound;
- maximum allowed detection + escalation response bound;
- timing behavior under startup, intentional suspension, degraded mode, maintenance and recovery.

No numeric timing value is supplied by this guidance.

### 8.5 Watchdog mode / service eligibility

Define:

- when the watchdog is armed/enabled;
- whether an early-boot watchdog is active before the full supervisor is ready;
- bounded bootstrap servicing behavior, if any;
- conditions that make watchdog service eligible;
- whether all required monitored responsibilities must be healthy, or whether mode-dependent health sets exist;
- behavior when observation/supervisor validity is unknown or indeterminate;
- behavior if the watchdog itself is unavailable, already expired, window-violated or otherwise invalid.

### 8.6 Lifecycle / mode behavior

Define treatment of:

- cold boot / partial initialization;
- restart/reset/reconnect/replacement;
- intentional task/process suspension;
- maintenance/service modes;
- update/activation where supervision coverage changes;
- degraded operation with a changed monitored set;
- shutdown/power transition;
- recovery/reintegration into normal supervision.

A grace period or temporary bypass is a project decision and shall be bounded by explicit entry/exit conditions where it affects the supervision claim.

### 8.7 Escalation / recovery / reset consequence

Define:

- expiry/invalid-supervision consequence;
- restart, reset, isolation, failover, degradation or another project response;
- target/reset scope and coordinated participant consequence;
- conditions for successful recovery/re-entry;
- behavior after repeated expiry/recovery;
- reset-loop/recovery-loop termination or escalation policy where repeated recovery is applicable.

This L4 guidance does not make reset the universal watchdog outcome.

### 8.8 Evidence and observability

Define what is needed to determine:

- last accepted progress/liveness evidence per required participant;
- evidence age / generation / incarnation / session;
- current supervision classification and reason;
- supervisor validity/degradation state;
- watchdog armed/service-eligible/service/expiry state or equivalent observable evidence;
- escalation reason and target;
- reset class/cause/scope where applicable;
- prior expiry/recovery count or history where repeated events matter;
- retained pre-reset/pre-restart evidence where reasonably producible and needed for diagnosis.

### 8.9 Verification thresholds / evidence

Define measurable criteria for the applicable project cases, including:

- acceptable normal observation/evaluation jitter;
- maximum detection/response latency;
- stale/session-mismatch rejection behavior;
- supervisor-failure behavior;
- startup/maintenance/degraded-mode transitions;
- expiry/escalation/reset evidence;
- repeated-recovery containment where applicable;
- independence claim evidence appropriate to the current engineering stage.

## 9. Interface and State Considerations

The implementation should keep these concepts distinguishable even if they share one physical API or task:

```text
progress/liveness evidence
!= supervision classification
!= watchdog service eligibility
!= watchdog service/expiry observation
!= escalation/recovery result
```

The project may represent supervision state using names such as disarmed, qualifying, supervising, degraded/indeterminate, expiry-pending or escalating, but this guidance does not require those names or a universal state machine.

Where multiple participants are supervised, define how per-participant state combines into the system/service supervision result. A boolean AND, quorum, weighted vote, mode-dependent set or another rule is a Project Design Decision; no combination rule is the SCAF default.

Where progress evidence crosses an Interaction boundary, session/incarnation semantics shall prevent old-session evidence from satisfying a current-session liveness decision when `SCAF-INT-010` is applicable.

## 10. Timing Considerations

Timing must be reasoned as a relationship, not copied from an example.

Useful project quantities may include:

```text
T_progress_expectation
T_progress_deadline
T_supervisor_evaluation
T_supervisor_jitter
T_watchdog_service_window
T_watchdog_expiry
T_escalation_effect
T_required_response
```

These names are analytical placeholders only.

A project commonly needs to establish both:

```text
healthy worst-credible supervision/service path
    remains within the configured watchdog service/expiry relationship
```

and

```text
loss of required progress
    becomes detectable and reaches the project-selected consequence
    within the applicable response bound
```

Where the project uses a direct watchdog expiry as the escalation trigger, a useful analysis relation may be expressed as:

```text
expected healthy evaluation/service delay < watchdog expiry bound
```

with sufficient tolerance for controlled jitter, while the resulting failure-detection/escalation latency remains within the applicable project requirement.

This is an analysis aid, not a universal formula. Projects with windowed watchdogs, staged supervisors, pre-expiry escalation, external supervisors or different timing semantics may require a different relationship.

## 11. Concurrency / Reentrancy Considerations

Consider, as materially applicable:

- progress evidence updated in ISR/task/thread/process contexts;
- races between progress update and supervisor sampling;
- atomicity/consistency of counters, timestamps, generations and classification state;
- multiple supervisors or redundant monitors and disagreement semantics;
- watchdog service calls from more than one context;
- priority inversion/starvation that delays supervision but not the monitored task, or vice versa;
- scheduler suspension/critical sections that can create apparent heartbeat loss;
- reset/escalation occurring concurrently with evidence capture or state transition.

A thread-safe watchdog API or atomic heartbeat variable does not by itself prove the project supervision semantics are correct.

## 12. Capacity / Resource Considerations

Supervision should not create an unexamined resource path that undermines its own claim. Consider:

- bounded storage for heartbeat/event history if history is retained;
- counters/timestamps/participant tables for the maximum supervised set;
- logging/telemetry rate during repeated late/missing events;
- retained evidence budget across reset/recovery;
- watchdog/service overhead and observer effect;
- communication bandwidth where heartbeat is transported.

If supervision introduces a materially bounded queue/backlog/overload concern, `SCAF-L4-001` may be a useful composing guidance. Its adoption is not automatic.

## 13. Lifecycle Construction

### 13.1 Startup / partial initialization

The project must define when supervision begins and when watchdog service becomes eligible. Common safe shapes include:

- watchdog disabled until a controlled readiness point, if permitted;
- watchdog active from early boot with a bounded bootstrap servicing path;
- staged monitored-set qualification as responsibilities become ready.

No shape is universal. An indefinite startup grace/bypass that can remain active after required supervision should begin is inconsistent with the claimed bounded supervision behavior.

### 13.2 Intentional suspension / maintenance / update

Intentional absence of progress shall be represented by a controlled mode/condition rather than being indistinguishable from an unintended stall. The project defines whether the participant is removed from the required monitored set, uses an alternate progress condition, changes timing, or requires a different controlled response.

### 13.3 Reset / restart / recovery

After restart/reset:

- required lifecycle/session/incarnation identity is re-established before stale evidence is reused;
- reset cause/class/scope is interpreted under project LIFE semantics;
- retained evidence is consumed only when its validity is established;
- the supervisor re-enters normal operation through controlled qualification criteria;
- repeated reset/recovery behavior follows separately owned bounded policy.

## 14. Failure / Recovery Considerations

The project should explicitly address at least the applicable cases:

- monitored code continues heartbeat while material work is stalled;
- progress evidence stops because the observer/transport path failed rather than the monitored responsibility;
- supervisor stalls or loses scheduling/resource access;
- watchdog hardware/service mechanism fails unavailable or fails to expire;
- shared clock/power/reset/resource defeats both supervisor and supervised context;
- stale heartbeat survives restart/reconnection;
- timing jitter/overload causes nuisance expiry;
- escalation destroys evidence required for diagnosis;
- reset scope leaves peers/retained state inconsistent;
- reset/restart repeats without removing the initiating condition.

The project may decide that some conditions are indistinguishable at runtime. In that case the limitation and controlled consequence should be explicit rather than replaced by false root-cause certainty.

## 15. Diagnostics / Observability

Construction should make enough of the supervision chain observable to support the project claim without forcing one telemetry implementation.

Candidate observations include:

- last progress token/counter/milestone per participant;
- progress age and timebase identity;
- participant incarnation/session/generation;
- late/missing/stale/invalid classification and reason;
- supervisor self-validity / degraded status;
- current required monitored set / supervision mode;
- watchdog armed/service-eligible/service/expiry evidence;
- escalation invocation and target;
- reset cause/class/scope after reboot;
- retained incident evidence around expiry;
- repeated expiry/recovery count/history where material.

Observation itself shall not be confused with the authoritative health/failure decision. Instrumentation that materially changes scheduling/timing must be considered under the applicable observer-effect/timing assumptions.

## 16. Verification Intent

These intents state properties to verify. Project Test Procedures own concrete stimuli, values, instrumentation, execution and pass/fail decisions.

### VI-01 — Healthy bounded supervision

**Property:** valid required progress remains recognized without nuisance escalation under the project's normal and worst-credible healthy timing assumptions.  
**Condition:** all required participants progress and supervisor/watchdog dependencies are valid.  
**Expected observable:** progress evidence is accepted with correct identity; service eligibility remains controlled; no unintended expiry/escalation occurs.

### VI-02 — Required participant progress stall

**Property:** loss of required progress cannot be hidden by continued execution elsewhere.  
**Condition:** one required monitored responsibility stops producing the project-defined progress property.  
**Expected observable:** its evidence becomes late/missing/invalid according to project semantics; watchdog service eligibility/response changes as designed; controlled consequence occurs within the project bound.

### VI-03 — Activity without material progress

**Property:** mere task/interrupt/transport activity does not falsely prove the material progress property where the design claims stronger progress supervision.  
**Condition:** heartbeat-producing infrastructure remains active while the material Function/Service stops progressing.  
**Expected observable:** the chosen evidence either detects the lack of material progress or the project explicitly demonstrates/document its detection limitation and controlled consequence.

### VI-04 — Stale / wrong-incarnation evidence

**Property:** old evidence cannot satisfy current supervision when session/incarnation identity is material.  
**Condition:** participant/session restarts or reconnects and stale evidence from the prior instance is presented/retained.  
**Expected observable:** stale/mismatched evidence is rejected or classified according to project semantics and does not silently preserve current healthy status.

### VI-05 — Supervisor / observation failure

**Property:** failure of the monitor/supervision path cannot silently become an unqualified healthy result.  
**Condition:** supervisor execution, observation source or required supervision dependency becomes unavailable/invalid.  
**Expected observable:** supervisor/observation invalidity is represented and the project-defined consequence occurs.

### VI-06 — Startup / partial initialization

**Property:** startup grace/bootstrap servicing is bounded and transitions to normal supervision under explicit conditions.  
**Condition:** system remains in partial initialization near or beyond the project-defined qualification boundary.  
**Expected observable:** watchdog/supervision mode and service eligibility follow the controlled bootstrap policy; indefinite silent bypass does not occur.

### VI-07 — Intentional suspension / maintenance / degraded mode

**Property:** intentional loss/change of progress evidence is distinguishable from unintended stall.  
**Condition:** enter and exit each materially applicable maintenance/suspend/degraded mode.  
**Expected observable:** required monitored set/timing/response changes according to project policy and returns through controlled requalification.

### VI-08 — Timing / jitter boundary

**Property:** normal worst-credible jitter does not cause nuisance expiry while true loss of progress still reaches detection/escalation within the required bound.  
**Condition:** exercise project-defined timing extremes and interference assumptions.  
**Expected observable:** measured detection/evaluation/service/expiry behavior remains within the project timing criteria.

### VI-09 — Watchdog expiry / escalation evidence

**Property:** expiry/escalation produces the project-selected consequence without being misreported as root cause.  
**Condition:** make watchdog servicing ineligible or otherwise satisfy the project expiry condition.  
**Expected observable:** expiry/escalation is observable; reset/restart/isolation/etc. occurs as selected; reset cause/scope and required evidence are preserved/interpretable as applicable.

### VI-10 — Repeated recovery / reset-loop containment

**Property:** repeated expiry/recovery cannot continue without the separately defined project termination/escalation behavior where repeated recovery is applicable.  
**Condition:** initiating condition persists across recovery/reset.  
**Expected observable:** repetition count/time/resource boundary or other termination criterion is reached and the project-defined next consequence occurs.

### VI-11 — Independence claim

**Property:** the claimed supervisor/watchdog independence is supported to the depth reasonably available at the current engineering stage.  
**Condition:** examine or exercise the material shared dependencies/failure contexts on which independence is claimed.  
**Expected observable/evidence:** architecture analysis, bench evidence, fault-condition verification or later empirical evidence demonstrates the controlled independence claim or exposes a bounded limitation requiring reassessment.

The Evidence Availability Rule remains applicable: empirical evidence that cannot reasonably be produced at the current stage is not an automatic current blocker, but the future evidence property/trigger shall remain explicit where material.

## 17. Invalid / Incomplete Construction Conditions

For a project claiming this L4 guidance, the realization is deterministically incomplete/invalid for the claimed scope when, as applicable:

- required monitored responsibility/progress property is not identified;
- progress evidence has no controlled owner/identity or can be stale across an applicable incarnation/session boundary without detection;
- watchdog servicing can bypass the claimed supervision decision and thereby mask required health loss;
- missing/invalid supervisor evidence is silently treated as healthy;
- no project-owned timing/deadline/expiry relationship exists where timing is material;
- startup/maintenance bypass can remain indefinitely active without controlled exit while normal supervision is required;
- watchdog/supervisor independence is claimed without identifying material shared dependencies;
- expiry has no defined controlled consequence;
- reset/restart is used without required reset-domain/lifecycle consequence decisions;
- repeated recovery is possible but no applicable termination/escalation policy exists where continued repetition is not acceptable;
- verification is claimed without evidence capable of observing the relevant progress/supervision/expiry behavior.

Legitimate not-yet-decided project values or not-yet-producible empirical evidence are not automatically `Invalid`; they remain unresolved until the current decision horizon requires resolution.

## 18. Recommended Practices

Recommended, not mandatory:

- prefer progress evidence tied to useful work rather than an unconditional periodic toggle when practical;
- keep watchdog-service authority narrow and reviewable;
- expose per-participant last-progress/age and supervision reason rather than only one final boolean where diagnosis matters;
- use monotonic/progress generations or session identities when restart/reconnection can make stale evidence plausible;
- analyze watchdog independence in terms of actual shared dependencies rather than the label “hardware watchdog” or “independent task”;
- preserve enough pre-expiry evidence to distinguish a supervision condition from likely initiating hypotheses when the project needs diagnosis;
- make temporary supervision bypass/grace states explicit and bounded;
- verify repeated-recovery behavior before treating a reset as sufficient recovery.

A project may choose another approach with appropriate material rationale.

## 19. Example Realization — Non-Canonical

> This example illustrates one conforming shape. It is not a canonical implementation and contains no SCAF default values.

```text
Required monitored set
    = <Project Design Decision by operating mode>

For each required participant P:
    PROGRESS_EVIDENCE[P]
        = <Project Design Decision>
    PROGRESS_DEADLINE[P]
        = <Project Design Decision>
    INCARNATION / SESSION RULE[P]
        = <Project Design Decision if applicable>

SUPERVISOR_OWNER
    = <Project Design Decision>

WATCHDOG_OWNER
    = <Project Design Decision>

WATCHDOG_EXPIRY_BOUND
    = <Project Design Decision>

STARTUP / MAINTENANCE / DEGRADED SUPERVISION POLICY
    = <Project Design Decision>

Conceptual decision:
    evaluate required progress + evidence identity + supervisor validity
        ↓
    project health/liveness input
        ↓
    watchdog service eligible OR not eligible
        ↓
    expiry / project-selected escalation when required
```

The example does not select:

- heartbeat period;
- missed-heartbeat count;
- watchdog timeout;
- timer/watchdog peripheral;
- RTOS/task/thread priority;
- API/register sequence;
- reset scope;
- recovery strategy;
- pass/fail threshold.

## 20. Variations / Trade-offs

Potential realization variations include:

- explicit push heartbeat versus supervisor polling;
- progress counter versus milestone/event supervision;
- local supervisor task versus separate process/service/domain;
- internal hardware watchdog versus external supervisor;
- one aggregate watchdog versus hierarchical/layered supervision;
- direct expiry-triggered reset versus expiry/invalid-supervision feeding a separate escalation controller;
- always-on supervision versus mode-dependent monitored sets.

Trade-offs include:

- faster detection versus nuisance escalation under jitter/overload;
- stronger independence versus cost/complexity;
- richer progress evidence versus coupling/observer effect;
- narrower recovery scope versus incomplete clearing of shared corruption;
- more retained evidence versus storage/time/resource cost;
- service continuity versus stronger clearing/reset action.

## 21. Material Deviation / Composition Boundary

A project need not create waiver bureaucracy for local implementation differences. Retain material rationale where a deviation changes, for example:

- what property counts as progress;
- which participants are required;
- supervisor/watchdog ownership or independence;
- service-eligibility semantics;
- timing/detection/expiry relationship;
- unknown/invalid supervision handling;
- reset/recovery scope;
- observability/verification capability.

Common composition candidates include:

- `SCAF-PAT-REC-001` / future corresponding L4 guidance for bounded retry/recovery escalation;
- `SCAF-PAT-EVD-001` / future corresponding L4 guidance for retained incident evidence;
- `SCAF-L4-001` where the supervision transport/history itself has bounded queue/overload concerns.

Composition does not imply automatic adoption. Material conflicts are resolved by Project Design Authority and shall not be silently merged.

## 22. Construction Readiness Checklist

A competent engineer or AI consumer should be able to begin a coherent project implementation when the project can answer, or explicitly track as current unresolved decisions:

- What responsibilities/properties are supervised?
- What evidence proves liveness/useful progress and what does it not prove?
- How is evidence associated with the correct participant/incarnation/session?
- Who evaluates supervision and who is allowed to service/preserve the watchdog?
- What supervisor/watchdog independence is required and from which failure dependencies?
- What timing relationship governs progress/deadline/evaluation/watchdog expiry/escalation?
- How are startup, intentional suspension, maintenance, degraded operation and recovery handled?
- What happens when evidence is missing/stale/invalid/indeterminate?
- What happens when the supervisor/watchdog itself is unavailable or invalid?
- What escalation/recovery/reset consequence is project-owned?
- What evidence/observability is needed before and after expiry/reset?
- What Verification Intent becomes concrete project Test Procedures later?

Passing this checklist means locally Construction Ready for the declared scope. It does not prove code buildability, implementation correctness, verification PASS, compliance, release readiness or closure.

## 23. rc03 / Guidance Non-Goals

This guidance does not introduce:

- a universal health taxonomy;
- a universal watchdog timeout or heartbeat period;
- a required missed-heartbeat count;
- a specific MCU/SoC/OS/RTOS/watchdog device;
- watchdog registers/APIs/ISR/task priorities;
- a mandatory reset response;
- a reference implementation or code template;
- a project Test Procedure;
- a new L1/L2 authority obligation;
- a new L3 Pattern or modified L3 trace;
- an L4 registry/schema/validator;
- executable L3↔L4 trace;
- project L4 adoption/pinning machinery;
- CI enforcement;
- Controlled Context Package builder/materialization policy.

## 24. Provenance / Reference Basis

This entry is SCAF-original construction elaboration derived from the frozen `SCAF-PAT-SUP-001`, `SCAF-PAT-SUP-002` and their frozen SCAF authority traces. It does not directly incorporate third-party source code, prompt text, schema bodies, documentation passages or vendor implementation examples.
