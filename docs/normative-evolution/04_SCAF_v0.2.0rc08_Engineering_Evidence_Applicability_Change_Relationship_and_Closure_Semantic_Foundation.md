# SCAF v0.2.0rc08 — Engineering Evidence Applicability, Change Relationship and Closure Semantic Foundation

**Development Release:** v0.2.0rc08  
**Development Predecessor:** v0.2.0rc07 / Git `510bdc1c936d870444da1052e0cd3159cc50b6af`  
**Formal Authority Release:** v0.1.0 / formal authority `294 / 218 / 76`  
**Currently Machine-Readable Candidate Authority:** `299 / 223 / 76`, representing `SCAF-OBS-041..045`  
**Affected Concern:** `SCAF-OBS`  
**Layer:** L2 candidate normative evolution  
**Status:** Independent-review semantic candidate; new rc08 IDs are not yet machine-readably represented

## 1. Why this RC exists

The v0.2.0rc07 independent review returned a clean result:

```text
PASS
Critical: 0
Major:    0
Minor:    0
Trivial:  0
V0.2.0RC07 ENGINEERING EVIDENCE BINDING CHANGE APPLICABILITY AND CLOSURE GAP ASSESSMENT GATE: YES
```

The exact rc07 review report supplied for this development step has SHA-256:

```text
93e6d3d73604415477633cfb664087b7fc4efe8491a0d097726628c55102c81b
```

That review independently confirmed that current SCAF already has substantial evidence authority for identity/provenance, time/correlation, causal-claim limitations, evidence quality/missingness/loss, observer effect, temporary-instrumentation lifecycle, verification evidence sufficiency and underlying closure separation. It also confirmed three remaining relationships as bounded real L2 gaps:

```text
1. Evidence Applicability Binding
2. Baseline / Change Evidence Relationship
3. Before / After Verification-Closure Evidence Relationship
```

rc08 addresses only those three gaps. It does not turn the later Evidence-Driven Engineering workflow into L2 authority.

## 2. Preserved authority and semantic boundaries

The new candidate semantics build on, rather than replace, existing authority:

```text
SCAF-OBS-004 / 005
  evidence identity and generic provenance

SCAF-OBS-009
  causal / derived-inference basis and limitations

SCAF-OBS-027
  change-triggered OBS re-evaluation

SCAF-OBS-041..045
  diagnostic-instrumentation lifecycle, temporary-probe disposition,
  instrumented-build identity and observation-path non-dependence

SCAF-AK-006
  Applicable Satisfaction Basis

SCAF-AK-007
  Project Verification / Assurance Authority decides evidence sufficiency

SCAF-AK-012
  underlying authority retains closure authority

SCAF-AK-013
  closure/disposition trace does not become closure authority
```

rc08 does not alter these ownership rules.

## 3. Candidate normative tranche

The rc08 OBS overlay proposes exactly three additional Project-Applicable Obligations:

- `SCAF-OBS-046` — Evidence realization applicability binding;
- `SCAF-OBS-047` — Baseline and change relationship for comparative evidence;
- `SCAF-OBS-048` — Before/after evidence relationship for verification and closure.

The complete proposed OBS replacement is:

`docs/normative-evolution/80_SCAF_OBS_Observability_Diagnostics_Incident_Evidence_Obligations_v0.2.0rc08.md`

The rc01 overlay remains unchanged and continues to be the source bound by the current candidate registry/validator. Existing candidate `SCAF-OBS-041..045` wording is reproduced unchanged in the rc08 overlay.

If the three new PAOs later pass review and are separately approved for machine-readable representation while the formal 294-record projection remains unchanged, the expected candidate inventory consequence would be:

```text
302 total
226 Project-Applicable Obligations
 76 Framework Normative Invariants
```

That inventory is a future representation consequence only. rc08 does not modify the current `299 / 223 / 76` candidate registry.

## 4. SCAF-OBS-046 — Evidence realization applicability binding

The first new semantic relationship answers:

> Does this evidence actually apply to the realization being analyzed or verified?

Generic provenance can identify producer, source object and observation context while still leaving a material mismatch ambiguous. Depending on the project, interpretation may depend on one or more of:

```text
source revision
build identity
configuration / feature profile
target or hardware revision
instrumentation configuration
operational / lifecycle identity
other source-owned realization identity
```

rc08 does not require all of these fields on every evidence item. It requires sufficient controlled identity/provenance only where the realization difference is material to interpretation, diagnosis, regression evaluation or verification applicability.

The source concerns remain authoritative for the meaning of these identities. OBS does not redefine CFG, ARCH, CTX, RUN, LIFE, TIME or other source semantics merely because evidence is associated with them.

## 5. SCAF-OBS-047 — Baseline and change relationship for comparative evidence

The second relationship answers:

> Which controlled baseline and which relevant change scope define the comparison being used?

The intended relation is:

```text
controlled baseline realization
        +
relevant change identity / scope
        +
applicable evidence from compared realization(s)
        ↓
controlled comparative evidence basis
```

This relation matters when diagnosis, regression evaluation or verification depends on a statement such as “known-good before this change” or “behavior changed across this controlled delta.”

The requirement deliberately does **not** mean:

```text
changed file == root cause
commit proximity == causality
newest change == responsible change
```

Causal claims remain governed by `SCAF-OBS-009`. Git history, patches, release manifests, change requests, controlled build records or another project mechanism may realize the relationship; none is mandated by L2.

## 6. SCAF-OBS-048 — Before/after evidence relationship for verification and closure

The third relationship answers:

> When verification or closure relies on a before/after behavioral comparison, are the two evidence sets correctly attributable to the prior and changed/corrected realizations?

As applicable, the controlled comparison may support evaluation of:

```text
previously abnormal/divergent behavior no longer present
intended behavior present
material existing/regression properties still satisfied
observed result attributable to the changed/corrected realization
```

The relation does not itself decide whether the evidence is sufficient and does not close the underlying issue. Those authorities remain separated:

```text
Applicable Satisfaction Basis       -> SCAF-AK-006
Evidence sufficiency                -> SCAF-AK-007
Underlying closure                  -> SCAF-AK-012
Closure / disposition trace         -> SCAF-AK-013
```

A project need not produce runtime logs or a universal before/after test for every change. The obligation applies when verification/closure materially relies on such a comparison.

## 7. Relationship to temporary Probe and retained Diagnostic lifecycle

The accepted `SCAF-OBS-041..045` semantics remain unchanged. rc08 does not introduce a new mandatory Probe class.

The combined L2 foundation now supports, without prescribing a workflow:

```text
development-scoped instrumentation has bounded purpose
        ↓
instrumented evidence has appropriate identity
        ↓
evidence remains applicable to the realization under analysis
        ↓
baseline/change comparison can be controlled where material
        ↓
before/after evidence can support verification/closure evaluation
        ↓
temporary instrumentation is removed or intentionally retained/promoted
```

The reusable engineering method that composes Probe exploration, retained Diagnostic observability and iterative evidence collection remains a future L3 Pattern question.

## 8. Materiality and proportionality boundary

rc08 does not create a universal metadata burden.

A project does not have to attach source revision, build ID, hardware revision, configuration ID and instrumentation profile to every observation when those distinctions cannot materially affect interpretation. The project must control the identity/provenance necessary for the applicable evidence purpose and risk.

Likewise:

- not every diagnosis requires a known-good baseline;
- not every change requires a before/after runtime comparison;
- not every closure requires retained runtime logs;
- not every evidence item needs direct linkage to a source-control commit.

Existing lifecycle-proportional governance and project verification authority remain applicable.

## 9. Mechanism and platform neutrality

The candidate requirements do not mandate:

```text
Git or another source-control system
commit hashes or patch files
specific build-ID syntax
hardware serial-number format
RAM ring buffer / retained RAM
Flash / SD / USB / DAT
logging macro or event-record layout
background writer / DMA / RTOS priority
specific build system or CI provider
AI model/provider
```

Those are project realization or later Pattern/Construction Guidance examples.

## 10. L2 / L3 boundary

rc08 deliberately does **not** make the following L2 obligations:

```text
Source Evidence + Change Evidence + Runtime Evidence + Probe Evidence
first behavioral divergence search
Evidence -> Hypothesis -> Probe -> Evidence iteration
hypothesis ranking
highest-information-gain probe selection
AI source navigation / change correlation / runtime analysis
AI probe-point recommendation
```

These describe a reusable engineering method/consumer capability rather than source authority. After the L2 evidence foundation stabilizes, a separate dependency/value review may determine whether an Evidence-Driven Engineering L3 Pattern is justified.

## 11. AI / human authority boundary

No AI-specific authority is created by rc08. Analysis of evidence does not grant an AI, tool or other consumer Project Design Authority, Project Verification / Assurance Authority, risk-acceptance authority, merge/release authority or underlying closure authority.

The existing Authority Kernel remains sufficient. Future L3 text may reference that boundary but should not duplicate it as a new AI-only authority regime.

## 12. Executable-governance state

rc08 is semantic-only. It does not modify:

- `authority-registry.yaml`;
- `candidate-authority-registry.yaml`;
- formal or candidate authority schema/validator;
- Project Application schema/validator/views;
- Effective Project Profile;
- Consumption Selection;
- Context Source Association;
- Controlled Context Package;
- L3 catalog/trace;
- L4 guidance;
- code generation or generic runtime-instrumentation CI.

Candidate Project Application / Effective Project Profile downstream implementation remains **PARKED** while this upstream L2 tranche is under review.

## 13. Required semantic non-equivalences

Independent review should preserve these distinctions:

```text
generic provenance != proof of evidence applicability to every realization
evidence applicability != source identity authority
baseline/change relationship != causality
change membership/proximity != root-cause proof
before/after evidence existence != evidence sufficiency
evidence sufficiency != underlying closure authority
OBS evidence relationship != universal test procedure
semantic candidate acceptance != machine-readable representation migration
L2 evidence foundation != L3 engineering workflow
AI evidence analysis != engineering authority
```

## 14. Review gate

A clean rc08 review should determine whether:

1. `SCAF-OBS-046..048` each close one confirmed rc07 gap without duplicating existing authority;
2. the three obligations remain Project-Applicable Obligations and preserve source-authority ownership;
3. `SCAF-OBS-046` is materiality-bounded and does not require universal identity fields;
4. `SCAF-OBS-047` controls baseline/change comparison without treating change membership as causality;
5. `SCAF-OBS-048` controls before/after evidence attribution without taking evidence-sufficiency or closure authority;
6. `SCAF-OBS-041..045` remain textually unchanged in the new complete overlay;
7. the current machine-readable candidate registry remains `299 / 223 / 76`;
8. frozen formal authority, L3 and downstream consumers remain unchanged;
9. no L3 Pattern, L4 guidance, code generation or generic instrumentation CI is introduced.

A clean YES gate authorizes only a new dependency/value assessment. It does not automatically authorize candidate-registry migration to `302 / 226 / 76`, Project Application/EPP migration, L3 Pattern creation, L4 guidance, code generation or CI enforcement.
