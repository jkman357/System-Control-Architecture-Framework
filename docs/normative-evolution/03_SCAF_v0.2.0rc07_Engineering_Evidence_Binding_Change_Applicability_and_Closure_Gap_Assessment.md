# SCAF v0.2.0rc07 — Engineering Evidence Binding, Change Applicability and Closure Gap Assessment

**Development Release:** v0.2.0rc07  
**Development Predecessor:** v0.2.0rc06 / Git `e5cece52a02fbf2eddd989ae4a26af3b3a54ca4f`  
**Formal Authority Release:** v0.1.0 / formal authority `294 / 218 / 76`  
**Validated Candidate Authority:** `299 / 223 / 76`, including `SCAF-OBS-041..045`  
**Layer:** L1/L2 normative-evolution gap assessment  
**Status:** Assessment-only candidate; no new L2 authority identity introduced

## 1. Why this RC exists

The v0.2.0rc06 independent review returned a clean result:

```text
PASS
Critical: 0
Major:    0
Minor:    0
Trivial:  0
V0.2.0RC06 CANDIDATE AUTHORITY-SET BINDING AND PROJECT APPLICATION CONSUMPTION SEMANTIC FOUNDATION GATE: YES
```

The exact rc06 review report consumed by this assessment has SHA-256:

```text
036994fd294e78b89b42d7ff10b279275ed14e0cfd55d11281ed26d5f668e401
```

That gate authorizes a dependency/value assessment for candidate downstream representation. However, before continuing that downstream migration, the active v0.2.0 line has exposed a more upstream engineering-evidence question through the accepted diagnostic-instrumentation work:

> Are the existing L2 authority obligations sufficient to bind runtime/diagnostic evidence to the source/build/target context that produced it, relate evidence to a controlled baseline and change set, and support before/after verification closure without making evidence itself the closure authority?

This assessment answers that question before adding another L2 candidate tranche or an L3 engineering pattern.

## 2. Assessment scope

rc07 evaluates only whether the current L1/L2 authority basis already covers three engineering-evidence relationships:

1. **Evidence Applicability Binding** — whether material evidence can be associated with the source/build/configuration/target/instrumentation context needed to interpret it;
2. **Baseline / Change Evidence Relationship** — whether a diagnosis, regression or verification claim that depends on change can identify the relevant baseline and change scope;
3. **Before / After Closure Evidence Relationship** — whether verification/closure evidence can distinguish the prior/baseline behavior from the changed/fixed behavior and remain attributable to the correct realization context.

The assessment also determines what remains deliberately outside L2 and should be deferred to a future L3 engineering pattern.

rc07 does **not**:

- add `SCAF-OBS-046` or any other new authority ID;
- modify the accepted `SCAF-OBS-041..045` candidate overlay;
- modify `candidate-authority-registry.yaml`;
- modify any formal normative source under `docs/normative/`;
- implement candidate Project Application authority-set binding;
- modify Effective Project Profile or later consumers;
- create an L3 Pattern;
- define an AI-specific authority role;
- prescribe Git, a logger API, a trace format, a storage medium or a test procedure.

## 3. Engineering method motivating the assessment

A reusable evidence-driven engineering workflow may consume four evidence classes:

```text
Source Evidence
Change Evidence
Runtime Evidence
Probe Evidence
```

and iterate through:

```text
Evidence
  ↓
Analysis / hypothesis
  ↓
Missing evidence?
  ↓ yes
Targeted development-scoped instrumentation
  ↓
New evidence
  ↓
Diagnosis / fix
  ↓
Verification
  ↓
Before / after evidence
  ↓
Engineering closure
```

This workflow is informative context for the assessment. L2 should define only the reusable engineering obligations required for trustworthy evidence interpretation. Analysis strategy such as first-behavioral-divergence search, hypothesis ranking, probe-point selection or AI-assisted source navigation belongs outside L2.

## 4. Existing authority basis reviewed

The primary authority basis is:

```text
SCAF-OBS-004  Evidence item identity
SCAF-OBS-005  Evidence provenance
SCAF-OBS-006  Observation time provenance / uncertainty
SCAF-OBS-008  Cross-participant evidence correlation
SCAF-OBS-009  Causal-correlation claim basis
SCAF-OBS-010  Evidence quality / completeness / missingness representation
SCAF-OBS-011  Observer / recorder self-health
SCAF-OBS-012  Loss-of-observation semantics
SCAF-OBS-013  Observer effect / low-coupling obligation
SCAF-OBS-015  Diagnostic evidence requirement
SCAF-OBS-023  Evidence copy / transformation consistency
SCAF-OBS-026  OBS traceability
SCAF-OBS-027  OBS change and re-evaluation
SCAF-OBS-035  OBS / ASSUR evidence-sufficiency boundary
SCAF-OBS-041  Diagnostic instrumentation lifecycle intent
SCAF-OBS-042  Development-scoped instrumentation purpose and removal criterion
SCAF-OBS-043  Development instrumentation closure disposition
SCAF-OBS-044  Instrumented-build evidence identity and cleanup re-evaluation
SCAF-OBS-045  Observation-path operational non-dependence and retained-cost acceptance
```

Cross-cutting authority relevant to verification/closure includes:

```text
SCAF-AK-005  Project verification separation from SCAF-ASSUR
SCAF-AK-006  Applicable Satisfaction Basis
SCAF-AK-007  Evidence sufficiency evaluation
SCAF-AK-012  Underlying closure authority
SCAF-AK-013  Closure/disposition trace
```

Other source concerns remain relevant where their identities/semantics are part of evidence applicability:

```text
SCAF-CFG   configuration / persistent-state identity and version semantics
SCAF-TIME  measurable timing / capacity / resource properties
SCAF-RUN   operational-state semantics
SCAF-LIFE  lifecycle / incarnation semantics
SCAF-ROB   health / failure / resilience semantics
SCAF-CTX / SCAF-ARCH  system and participant/target context
```

## 5. Assessment result summary

| Area | Coverage result | rc07 decision |
|---|---|---|
| Generic evidence item identity | **COVERED** | `SCAF-OBS-004` already requires evidence-item identity where confusion/replacement/correlation is material. |
| Generic evidence provenance | **COVERED but intentionally open-ended** | `SCAF-OBS-005` requires producer/source/context provenance, but does not explicitly establish realization/build applicability semantics. |
| Time/chronology/correlation | **COVERED** | `SCAF-OBS-006..009` already govern time provenance, correlation and causal-claim limitation. |
| Missingness / loss / recorder confidence | **COVERED** | `SCAF-OBS-010..012` already require visible quality/loss limitations. |
| Observer effect / non-interference | **COVERED** | `SCAF-OBS-013` plus candidate `SCAF-OBS-045` establish bounded observer effect and non-dependence. |
| Temporary versus retained instrumentation lifecycle | **COVERED** | Candidate `SCAF-OBS-041..044` establish lifecycle intent, bounded purpose, disposition and cleanup re-evaluation. |
| Instrumented-build identity | **COVERED for the temporary-instrumentation case** | `SCAF-OBS-044` prevents silent attribution of instrumented evidence to a materially different cleaned build. |
| Generic evidence-to-realization applicability | **PARTIALLY COVERED — REAL L2 GAP** | Existing generic provenance is broad, while `SCAF-OBS-044` is intentionally scoped to material temporary instrumentation effects. |
| Controlled baseline/change relationship for comparative diagnosis/regression | **PARTIALLY COVERED — REAL L2 GAP** | `SCAF-OBS-027` requires re-evaluation after material OBS change and `SCAF-OBS-009` limits causal claims, but neither requires the baseline/change relationship used by a comparative claim to be identifiable. |
| Before/after evidence relation supporting verification closure | **PARTIALLY COVERED — REAL L2 GAP** | `SCAF-AK-006/007/012/013` correctly own satisfaction basis, sufficiency and closure authority; what is missing is an OBS-side evidence relationship that keeps before/after evidence attributable to the correct realization contexts. |
| First behavioral divergence analysis | **NOT L2** | Analysis method; candidate future L3 pattern concept. |
| Evidence → hypothesis → probe iteration | **NOT L2** | Reusable engineering workflow/pattern, not normative source obligation. |
| AI source navigation / diff correlation / hypothesis generation | **NOT L2** | Consumer capability; no new L2 AI authority required. |
| AI root-cause / merge / safety authority | **NO NEW L2 GAP IDENTIFIED** | Existing authority kernel already keeps evidence evaluation, verification, design and closure authority separated. |

## 6. Gap A — Generic Evidence Applicability Binding

### 6.1 What is already covered

`SCAF-OBS-005` requires the project to define provenance needed to interpret each material evidence class, including producing/observing responsibility, applicable source object/condition and observation context.

`SCAF-OBS-004` separately requires evidence-item identity where evidence may be confused, duplicated, replaced, merged, exported or correlated.

Candidate `SCAF-OBS-044` adds a strong special-case rule:

> where temporary instrumentation can materially affect behavior/timing/capacity/memory/scheduling/evidence production, evidence from that instrumented build must retain enough build/configuration/instrumentation identity to avoid silent attribution to a materially different cleaned build.

These obligations are sound and should be preserved.

### 6.2 What remains underspecified

The generic evidence-provenance obligation does not explicitly require a material runtime/diagnostic/verification evidence item to be associated with the realization identity needed to decide whether it applies to the source under analysis.

A project can therefore satisfy the literal generic provenance wording with observer/source/context information yet still leave ambiguous whether the evidence came from:

```text
source revision A or B
build/configuration X or Y
target/board revision H1 or H2
instrumentation configuration P1 or P2
feature/configuration profile C1 or C2
```

when those distinctions materially affect interpretation.

The problem is not that every evidence record must carry every possible identity field. The problem is that material applicability identity must be controlled where a mismatch could invalidate interpretation.

### 6.3 rc07 classification

```text
PARTIALLY COVERED
REAL L2 GAP
```

The gap belongs primarily to `SCAF-OBS` because it concerns evidence applicability/provenance. `SCAF-CFG`, CTX/ARCH, RUN/LIFE and other concerns continue to own the meaning of the identities being associated; OBS must not redefine them.

### 6.4 Candidate requirement direction

A later semantic RC should consider one new PAO with semantics equivalent to:

> Where evidence interpretation or verification applicability materially depends on the realized source/build/configuration/target/instrumentation context, the project SHALL preserve or associate sufficient controlled identity/provenance to determine that applicability and SHALL NOT silently attribute the evidence to a materially different realization context.

This must remain representation-neutral. It must not require Git hashes, a specific build-ID format, hardware serial numbers, file headers or universal metadata fields.

## 7. Gap B — Baseline / Change Evidence Relationship

### 7.1 What is already covered

`SCAF-OBS-027` requires OBS and dependent project decisions to be re-evaluated when evidence identity/provenance, source semantics, correlation, verification need or other material observation conditions change.

`SCAF-OBS-009` requires a controlled basis and limitations whenever evidence is used to make a causal or derived-inference claim.

`SCAF-AK-006` requires an Applicable Satisfaction Basis for each verification obligation.

These rules constrain interpretation and verification but do not fully define a comparative change-evidence relationship.

### 7.2 Missing relationship

When diagnosis/regression analysis relies on a statement such as:

```text
known-good behavior under baseline B
changed implementation C
observed failing behavior F
```

or:

```text
before change / after change
```

there is no direct L2 obligation requiring the relevant baseline and change scope to be identifiable as part of the evidence basis.

Without that relationship, a technically correct runtime sequence can be compared against the wrong baseline, or a difference can be attributed to an unrelated set of changes.

### 7.3 rc07 classification

```text
PARTIALLY COVERED
REAL L2 GAP
```

This is not a requirement to use Git. `git diff`, commit ranges and patch history are useful implementation examples only.

The L2 concern is the controlled relationship:

```text
baseline identity
+
material change identity/scope
+
resulting evidence applicability
```

### 7.4 Candidate requirement direction

A later semantic RC should consider one new PAO with semantics equivalent to:

> Where diagnosis, regression evaluation or verification materially depends on comparison to a prior/known-good realization, the project SHALL identify the controlled baseline and the relevant change scope sufficiently to establish which realization states are being compared. Change proximity alone SHALL NOT establish causality; causal claims remain subject to `SCAF-OBS-009`.

The requirement should allow source-control history, release manifests, controlled build records, change requests or another project mechanism.

## 8. Gap C — Before / After Verification and Closure Evidence Relationship

### 8.1 Existing authority is already correct

SCAF already has strong authority separation:

- `SCAF-AK-006` defines the Applicable Satisfaction Basis;
- `SCAF-AK-007` assigns evidence-sufficiency evaluation to Project Verification / Assurance Authority;
- `SCAF-AK-012` retains underlying closure authority with the owner of the requirement/design/risk/deviation;
- `SCAF-AK-013` requires closure/disposition trace without turning the trace record into closure authority;
- `SCAF-OBS-035` prevents OBS evidence availability from being interpreted as verification sufficiency or closure.

No new AI-specific closure authority is required.

### 8.2 What remains missing

The current L2 OBS set does not directly require before/after evidence used for a behavioral verification or defect/change closure claim to remain attributable to the correct before and after realization contexts.

Candidate `SCAF-OBS-044` handles one important special case: after temporary instrumentation cleanup, determine and perform the required regression/timing/resource re-evaluation. It does not define the general evidence relation for any corrected/changed realization.

A meaningful closure comparison may need to demonstrate, as applicable:

```text
identified abnormal/divergent behavior is no longer present
intended behavior is present
material existing behavior/regression constraints remain satisfied
resulting evidence belongs to the corrected build/configuration/target
```

Whether this evidence is sufficient remains a Project Verification / Assurance Authority decision under `SCAF-AK-007`; whether the underlying issue can close remains with the applicable closure authority under `SCAF-AK-012`.

### 8.3 rc07 classification

```text
PARTIALLY COVERED
REAL L2 GAP
```

The new L2 content should define evidence applicability/comparison semantics, not universal test depth and not a universal requirement for runtime logs.

### 8.4 Candidate requirement direction

A later semantic RC should consider one new PAO with semantics equivalent to:

> Where verification or closure relies materially on comparison of behavior before and after a change/fix, the project SHALL preserve the controlled relationship and realization applicability of the compared evidence sufficiently to distinguish the baseline/prior condition from the changed/fixed condition and to evaluate the applicable intended and regression properties. The existence of before/after evidence SHALL NOT by itself establish evidence sufficiency or underlying closure.

## 9. Evidence classes versus normative identities

The four engineering evidence classes are useful pattern vocabulary:

```text
Source Evidence
Change Evidence
Runtime Evidence
Probe Evidence
```

rc07 does **not** recommend turning these four labels into four mandatory L2 authority classes.

Reason:

- Source evidence may be architecture/source/configuration authorities rather than an OBS evidence class.
- Change evidence may be represented by source-control history, controlled change records, build manifests or other project mechanisms.
- Runtime evidence is already broadly covered by OBS observation/diagnostic/incident-evidence semantics.
- Probe evidence is a lifecycle/use characterization of development-scoped instrumentation already covered by `SCAF-OBS-041..044`.

The reusable four-part composition belongs more naturally to a later L3 Pattern after the required L2 evidence relationships are complete.

## 10. Observability non-interference status

No new L2 gap is identified for the high-level non-interference principle.

Current coverage is sufficient at the authority level:

```text
SCAF-OBS-013
observer effect / low-coupling obligation

SCAF-OBS-045
observation-path operational non-dependence
+ retained observer-effect/resource acceptance

SCAF-TIME
measurable timing/capacity/resource limits

SCAF-ROB
resilience consequence after relevant failure/overload
```

A future L3 pattern may recommend mechanisms such as bounded in-memory capture, deferred export or controlled overflow policies, but L2 should not mandate ring buffers, background flush tasks, DMA, SD, USB, trace transport, priority values or logging APIs.

## 11. AI / human authority assessment

No new AI-specific L2 authority is justified by this workflow.

Existing SCAF authority separation already establishes that:

```text
analysis/evidence consumer
!=
Project Design Authority
!=
Project Verification / Assurance Authority
!=
underlying closure authority
```

An AI consumer may navigate source, compare changes, analyze runtime sequences, form hypotheses, recommend evidence collection locations or generate review findings. None of those activities automatically grant authority to:

- define project design decisions;
- determine actual evidence sufficiency;
- accept residual risk;
- close the underlying requirement/defect/deviation;
- authorize merge/release merely because a diagnostic inference is persuasive.

A later L3 pattern should state this consumer/authority boundary explicitly by reference to the existing Authority Kernel rather than creating duplicate AI-only L2 authority rules.

## 12. Candidate next L2 tranche

If rc07 passes independent review, the smallest justified next normative step is a semantic candidate tranche addressing the three confirmed gaps only.

Recommended provisional scope:

```text
Evidence Applicability Binding
Baseline / Change Evidence Relationship
Before / After Verification-Closure Evidence Relationship
```

The next RC may reserve candidate identities such as `SCAF-OBS-046..048`, but the exact titles/text/numbering are **not** accepted by rc07 merely because this assessment identifies three gaps.

The semantic RC must preserve:

- `SCAF-OBS-004/005/009/010/012/013/027`;
- candidate `SCAF-OBS-041..045`;
- `SCAF-AK-006/007/012/013` verification and closure authority;
- per-source concern authority for configuration, timing, lifecycle, runtime, robustness and system context;
- representation neutrality;
- project-specific evidence sufficiency and closure judgment.

## 13. Downstream executable-governance state

The rc06 Authority-Set Binding semantic foundation remains accepted development-line work, but candidate Project Application implementation should remain parked while the L2 authority set is still expanding.

Reason:

```text
candidate authority set is still under active semantic evolution
        ↓
adding another L2 tranche would change candidate membership/domain
        ↓
premature downstream consumer migration would immediately require another migration
```

Therefore rc07 records:

```text
PARK   candidate Project Application authority-set representation/tooling
PARK   Effective Project Profile candidate migration
PARK   Consumption / Context downstream migration
```

This is not a reversal of rc06. rc06 solved the semantic binding problem. rc07 simply defers implementation until the upstream L2 evidence foundation stabilizes enough to justify downstream migration.

## 14. L3 decision

A new L3 Pattern is **DEFERRED**, not rejected.

The candidate future Pattern may be named along the lines of:

```text
Evidence-Driven AI-Assisted Engineering
```

and may compose:

```text
Source Evidence
Change Evidence
Runtime Evidence
Probe Evidence

Evidence → Hypothesis → Targeted Probe → Evidence → Verification → Closure
```

However, the following remain L3/pattern-level method concepts rather than new L2 obligations:

- first behavioral divergence search;
- hypothesis ranking;
- highest-information-gain probe selection;
- iterative probe placement;
- source/diff/runtime correlation workflow;
- AI-assisted analysis roles;
- mechanism recommendations for RAM/Flash/SD/USB/streaming/export.

A separate dependency/value review must determine whether a new L3 Pattern is justified after the L2 evidence tranche stabilizes. Existing frozen L3 is not modified in place.

## 15. Mechanism and platform neutrality

The confirmed L2 gaps must remain valid across MCU, RTOS, SoC and host/service environments.

No candidate L2 requirement should mandate:

```text
Git
RAM ring buffer
retained RAM
Flash incident record
SD card
USB stream
DAT format
printf/log macro
background logging task
DMA
specific scheduler priority
specific build system
specific CI provider
AI model/provider
```

Those may be project realizations or future L3/L4 examples only.

## 16. Required validation for rc07

Because rc07 is assessment-only, a valid candidate must demonstrate:

```text
formal authority validator:        294 / 218 / 76 PASS
candidate authority validator:     299 / 223 / 76 PASS
candidate frozen projection:       294 MATCH
candidate records:                 5
L3 trace validator:                12 patterns / 119 relations PASS
frozen release integrity:          docs/normative MATCH; docs/l3 MATCH
formal Project Application:        PASS against formal authority only
git diff --check HEAD:             PASS
```

The working-tree semantic delta should be limited to this assessment and navigation/release records. No authority registry, schema, validator, L3/L4 source or downstream consumer implementation should change.

## 17. Bounded invalid / over-expansion conditions

The review should confirm at least that rc07 prevents the following:

1. treating generic `SCAF-OBS-005` provenance as already equivalent to explicit source/build/target applicability binding;
2. treating `SCAF-OBS-044` instrumented-build identity as a universal evidence-applicability rule for every evidence class;
3. requiring all evidence to carry every possible build/board/configuration identity regardless of materiality;
4. requiring Git or a particular source-control system;
5. treating change proximity or diff membership as proof of causality;
6. treating before/after evidence existence as evidence sufficiency;
7. treating verification evidence sufficiency as underlying closure authority;
8. interpreting missing Project Application evidence references as automatic Not Applicable or closure;
9. turning SCAF-APP into a per-log/per-probe inventory;
10. creating an AI-specific Project Design/Verification/Closure authority;
11. adding a new L3 Pattern before the L2 evidence gaps are semantically resolved;
12. modifying frozen `docs/normative/` or `docs/l3/` in place;
13. expanding L4/code generation/generic instrumentation CI as a consequence of this assessment;
14. resuming candidate downstream consumer implementation before the active L2 authority tranche is stabilized and separately assessed.

## 18. rc07 decision

The assessment concludes:

```text
COVERED
- generic evidence identity/provenance foundation
- time/correlation/causal limitation
- evidence quality/missingness/loss
- observer effect/non-dependence
- temporary instrumentation lifecycle
- verification sufficiency / closure authority separation

REAL L2 GAPS
1. generic Evidence Applicability Binding
2. Baseline / Change Evidence Relationship
3. Before / After Verification-Closure Evidence Relationship

NOT L2
- first behavioral divergence method
- Evidence → Hypothesis → Probe workflow
- AI source/diff/runtime analysis workflow
- concrete logging/storage/export mechanisms
```

Therefore, after a clean rc07 independent review, the smallest justified next step is:

```text
v0.2.0rc08
Engineering Evidence Applicability, Change Relationship and Closure
Semantic Candidate
```

That next RC should add only the minimum L2 candidate semantics required by the three confirmed gaps. It should not simultaneously create the L3 Pattern or resume downstream candidate Project Application implementation.

## 19. Acceptance boundary

A clean rc07 review establishes only that three L2 engineering-evidence relationships are materially under-specified and justify a bounded semantic candidate tranche.

It does not:

- accept any exact `SCAF-OBS-046..048` wording or numbering;
- change formal or candidate authority inventories;
- promote candidate authority;
- authorize candidate Project Application serialization/schema/validator;
- authorize Effective Project Profile or later-consumer migration;
- create an L3 Pattern;
- create L4 guidance;
- authorize code generation;
- authorize generic runtime-instrumentation CI.
