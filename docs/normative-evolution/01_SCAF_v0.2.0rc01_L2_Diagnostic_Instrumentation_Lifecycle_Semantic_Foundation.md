# SCAF v0.2.0rc01 — L2 Diagnostic Instrumentation Lifecycle Semantic Foundation

**Development Release:** v0.2.0rc01  
**Formal Predecessor:** v0.1.0  
**Affected Concern:** `SCAF-OBS`  
**Layer:** L2 candidate normative evolution  
**Status:** Independent-review candidate; not yet promoted into frozen canonical authority

## 1. Why this RC exists

The frozen SCAF observability baseline already requires evidence purpose, evidence quality, observer self-health, loss-of-observation semantics and bounded observer effect. It does not yet make one engineering lifecycle distinction explicit enough:

```text
observation intentionally retained beyond development
!=
temporary instrumentation added to answer a bounded engineering question
```

Without that distinction, temporary diagnostic code can accumulate by inertia, while useful long-term health/incident monitoring can be removed merely because it originated during debugging.

This RC therefore proposes a small L2 semantic extension rather than prescribing a logging implementation.

## 2. Candidate concepts

### 2.1 Retained diagnostic instrumentation

Observation/diagnostic instrumentation intentionally kept beyond the development activity because it has continuing operational, service, diagnostic, verification or incident-evidence value.

Retention does not imply continuous physical logging and does not select RAM, Flash, SD, USB, telemetry, database or another storage/export mechanism.

### 2.2 Development-scoped instrumentation

Temporary observation/diagnostic instrumentation added to answer a bounded engineering question during feature implementation, defect investigation, refactoring, timing/performance study or verification.

A project may use different local terms such as probe, trace point, breadcrumb, debug counter or instrumentation marker. SCAF governs lifecycle intent, not the project naming convention.

### 2.3 Remove-or-retain disposition

Development-scoped instrumentation reaches closure only through an explicit disposition:

```text
REMOVE
or
RETAIN / PROMOTE as retained diagnostic instrumentation
```

A disabled compile switch by itself is not equivalent to lifecycle disposition if stale instrumentation remains unintentionally in the source baseline.

## 3. Candidate normative delta

The candidate OBS overlay reserves five new Project-Applicable Obligation IDs:

- `SCAF-OBS-041` — Diagnostic instrumentation lifecycle intent;
- `SCAF-OBS-042` — Development-scoped instrumentation purpose and removal criterion;
- `SCAF-OBS-043` — Development instrumentation closure disposition;
- `SCAF-OBS-044` — Instrumented-build evidence identity and cleanup re-evaluation;
- `SCAF-OBS-045` — Observation-path operational non-dependence and retained-cost acceptance.

The full proposed replacement text is in:

`docs/normative-evolution/80_SCAF_OBS_Observability_Diagnostics_Incident_Evidence_Obligations_v0.2.0rc01.md`

Frozen IDs `SCAF-OBS-001` through `SCAF-OBS-040` are preserved unchanged in meaning and identity.

## 4. Intended engineering behavior

The candidate semantics support a controlled development loop such as:

```text
define expected behavior
    ↓
add only evidence-producing development instrumentation needed for the question
    ↓
implement / run / collect evidence
    ↓
verify expected behavior and material regression constraints
    ↓
REMOVE or RETAIN each development-scoped observation site
    ↓
rebuild / perform cleanup-sensitive regression or timing confirmation
    ↓
close the change baseline
```

This is a governance shape, not a mandatory process template. Project lifecycle/proportional-governance rules still determine how much evidence is required for a particular change.

## 5. Runtime non-interference boundary

This RC intentionally strengthens the connection between instrumentation lifecycle and the existing observer-effect rule.

A retained observer may consume CPU, memory, storage capacity, bandwidth or service time only within project-defined and accepted bounds. Where diagnostic persistence/export is not itself required source functionality, loss or slowness of that evidence path must not silently become a prerequisite for the source Function/Service to continue.

The candidate does **not** impose an impossible universal zero-overhead requirement. Measurable limits remain project decisions governed by `SCAF-TIME`; failure/degradation consequences remain governed by `SCAF-ROB`; evidence loss remains governed by `SCAF-OBS`.

## 6. Mechanism boundary

This RC does not prescribe:

- retained RAM;
- ring buffers;
- internal/external Flash;
- SD card logging;
- USB streaming;
- background writer tasks;
- DMA;
- specific RTOS priorities;
- file formats;
- log APIs;
- compile-time macro names;
- recorder/probe wrappers.

Those are realization/Pattern/Construction Guidance questions. A future L3 or L4 change is justified only if the accepted L2 semantics expose a real reusable mechanism/construction dependency.

## 7. Controlled supplemental input

The user-supplied supplemental donor considered for this RC is:

```text
Embedded-Incident-Crash-Recorder-Framework-main.zip
SHA-256: b96da3ba5baa8b946ed916d9dbb76b9f7a51552b39d8a11f7d27d3adf78a392b
Donor version observed in README: v1.0.0rc05
License observed in donor: MIT
```

The donor is used only as a controlled reference for generic concepts including temporary-vs-retained diagnostic instrumentation, cleanup/promotion lifecycle, observer-effect measurement and decoupling of evidence acquisition from slower persistence/export work.

SCAF does not copy or promote donor code, API names, record layouts, memory budgets, storage profiles, implementation constants or project-specific examples. The candidate wording is independently synthesized under SCAF authority semantics.

The older supplemental-source record already frozen in SCAF input-baseline history remains unchanged; this RC records a new development input rather than rewriting historical provenance.

## 8. Frozen-state preservation

`v0.2.0rc01` deliberately does **not** modify:

- `docs/normative/` frozen canonical files;
- the frozen `294 / 218 / 76` authority inventory;
- `authority-registry.yaml`;
- authority-registry schema/validator;
- L3 catalog or machine-readable trace;
- Project Application / Effective Project Profile machinery;
- Consumption Selection / Context Source Association / Controlled Context Package machinery;
- frozen L4 guidance.

This means the existing executable-governance chain remains valid for the formal v0.1.0 baseline while the candidate L2 delta is reviewed independently.

## 9. Review gate

Independent review should determine whether:

1. the retained-vs-development instrumentation distinction belongs in L2 OBS authority;
2. the five proposed obligations are non-duplicative and mechanism-neutral;
3. cleanup/promotion semantics preserve Project Design Authority and proportional governance;
4. the non-interference language is strong enough without claiming universal zero overhead;
5. build/evidence identity semantics avoid silently transferring evidence from an instrumented build to a materially different cleaned build;
6. no frozen baseline is modified in place;
7. the supplemental donor is used as concept input without uncontrolled source promotion.

A clean review authorizes only a new dependency/value assessment. It does not automatically authorize authority-registry migration, L3/L4 expansion or executable tooling work.
