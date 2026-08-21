# SCAF v0.2.0rc05 — Candidate Authority Downstream Consumption Dependency & Value Assessment

**Development Release:** v0.2.0rc05  
**Development Predecessor:** v0.2.0rc04 / Git `5df3a13003f69124fb56fb9605819068ed496b7a`  
**Formal Authority Release:** v0.1.0 / formal authority `294 / 218 / 76`  
**Validated Candidate Authority:** `299 / 223 / 76`, including `SCAF-OBS-041..045`  
**Layer:** executable-governance downstream dependency/value assessment  
**Status:** Independent-review candidate; no downstream consumer migration performed

## 1. Decision purpose

The v0.2.0rc04 independent review returned a clean finding-closure result:

```text
PASS
Critical: 0
Major:    0
Minor:    0
Trivial:  0
V0.2.0RC04 CANDIDATE AUTHORITY VALIDATOR FORMAL-PREREQUISITE FAIL-STOP HARDENING GATE: YES
```

The exact rc04 review report consumed by this assessment has SHA-256:

```text
22123e03915320ae8bfcd84ee95248f692228b820b275b10ee9353ec6656d6ea
```

That gate authorizes only the next dependency/value assessment. It does not itself authorize Project Application or later downstream consumption of candidate authority.

rc05 therefore asks one bounded question:

> Now that candidate authority is machine-readable, source-aware validated, and formal-prerequisite fail-stop, what is the smallest downstream migration that has real engineering-governance value without conflating formal and candidate authority?

No downstream schema, validator, generator, query, L3, L4, code-generation or generic runtime-instrumentation CI implementation is changed in rc05.

## 2. Executive decision

The assessment reaches this bounded result:

| Area | rc05 decision | Reason |
|---|---|---|
| Project Application ability to disposition candidate PAOs | **GO — real value exists** | `SCAF-OBS-041..045` are Project-Applicable Obligations. If they can never enter Project Application, their project-specific applicability / not-applicable / undetermined disposition cannot be exercised through SCAF's accepted governance model before formal promotion. |
| Directly switch the existing formal Project Application validator from `authority-registry.yaml` to `candidate-authority-registry.yaml` | **STOP** | That would silently change the accepted formal-only consumer boundary, make v0.1.0 Project Application behavior depend on development authority, and does not solve mixed source-release semantics. |
| Relax the existing Project Application schema in place so `scaf_source_release` simply accepts `v0.2.0rc01` | **STOP** | The candidate PAO domain is mixed: 218 PAOs retain `source_release: v0.0.2`, while five candidate PAOs have `source_release: v0.2.0rc01`. One release token cannot truthfully identify the complete candidate PAO set. |
| Candidate-only Project Application consumption path | **GO — but only after a semantic foundation** | A separately controlled candidate path can preserve the formal path while allowing candidate obligations to be dispositioned. It first needs an explicit authority-set binding model distinct from per-record semantic source release. |
| Candidate authority-set / representation identity semantics | **GO — next justified migration target** | Existing downstream logic uses one SCAF source release as the PAO-domain identity. The candidate registry is instead a validated composite authority set. The distinction must be made explicit before serialization/validator changes. |
| Existing Project Application applicability/disposition semantics | **PRESERVE** | `applicable / not_applicable / undetermined`, project scope, controlled disposition basis and project reference surfaces remain suitable. The gap is authority-set binding, not applicability meaning. |
| Effective Project Profile migration | **DEFER** | Existing profile semantics/generator derive a complete PAO domain from one `scaf_source_release`; this is incompatible with the mixed-source candidate authority set. Project Application semantics must be solved first. |
| Consumption Selection / Context Source Association / Controlled Context Package | **DEFER** | These are downstream of validated Effective Project Profile / Project Application state and gain no independent value from premature candidate support. |
| Project Application read/query views | **DEFER with Project Application implementation** | They are subordinate to the validator boundary and should not independently gain candidate authority. |
| L3 trace / new L3 Pattern | **STOP** | No new realization-mechanism gap is created by downstream applicability consumption. |
| L4 construction guidance | **STOP** | No construction mechanism is selected by this assessment. |
| Generic probe/log code generation or generic runtime-instrumentation CI | **STOP** | The new OBS obligations still contain project-specific engineering judgment not made machine-decidable by candidate consumption. |

Therefore, if rc05 passes independent review, the smallest justified next step is:

```text
v0.2.0rc06
Candidate Authority-Set Binding and Project Application Consumption
Semantic Foundation
```

rc06 should define semantics only. It should not yet modify the formal Project Application schema/validator, Effective Project Profile, later consumers, L3, L4, code generation, or generic instrumentation CI.

## 3. Inputs and preserved state

This assessment consumes the reviewed development chain:

```text
v0.2.0rc01
L2 diagnostic-instrumentation lifecycle semantic candidate
        ↓
v0.2.0rc02
post-semantic dependency/value assessment
        ↓
v0.2.0rc03
candidate machine-readable authority representation
        ↓
v0.2.0rc04
formal-prerequisite fail-stop hardening
        ↓
v0.2.0rc05
this downstream consumption dependency/value assessment
```

The accepted candidate authority remains:

```text
candidate-authority-registry.yaml
299 total authority records
223 Project-Applicable Obligations
76 Framework Normative Invariants
294 exact frozen projections
5 candidate PAOs: SCAF-OBS-041..045
```

The formal authority remains:

```text
authority-registry.yaml
294 total authority records
218 Project-Applicable Obligations
76 Framework Normative Invariants
```

No authority semantics or registry records are changed by rc05.

## 4. Why Project Application consumption has real value

`SCAF-OBS-041..045` were intentionally classified as Project-Applicable Obligations rather than Framework Normative Invariants.

That classification means their practical project meaning depends on Project Application / Framework Scan decisions such as:

```text
applicable
not_applicable
undetermined
```

with a controlled project scope and disposition basis.

If candidate authority remains machine-readable but Project Application can resolve only frozen v0.0.2 authority, then the development line has this split:

```text
candidate authority can validate OBS-041..045 as SCAF PAOs
        !=
projects can disposition OBS-041..045 through SCAF-APP
```

That split is acceptable while representation is under construction, but keeping it indefinitely would prevent SCAF from exercising the project-applicability semantics of the five new obligations before deciding whether they deserve formal promotion.

Therefore candidate Project Application consumption has material value.

The value is specifically **project applicability/disposition evaluation**. It is not a justification for per-probe inventories, runtime instrumentation APIs, logging implementations, evidence collectors, or automatic engineering decisions.

## 5. Existing Project Application boundary

The accepted formal Project Application representation is deliberately bound to the frozen authority model.

The current schema fixes:

```text
record_kind: project_application
representation_release: v0.0.6rc04
scaf_source_release: v0.0.2
```

The current production validator owns these repository-bound inputs:

```text
schemas/project-application.schema.json
authority-registry.yaml
schemas/authority-registry.schema.json
frozen authority-registry source-aware validator
```

It resolves every `scaf_authority_id` against validated formal authority and rejects unknown/candidate IDs.

That is correct for the frozen v0.1.0 path and must remain correct.

The accepted formal path therefore must not be changed in place merely because a development candidate exists.

## 6. The mixed source-release problem

The candidate authority representation exposes a fact the existing downstream model did not need to represent previously.

Among candidate Project-Applicable Obligations:

```text
218 PAOs have source_release: v0.0.2
5 PAOs have source_release:   v0.2.0rc01
```

The five candidate records are:

```text
SCAF-OBS-041
SCAF-OBS-042
SCAF-OBS-043
SCAF-OBS-044
SCAF-OBS-045
```

Each correctly retains the source release that owns its semantics rather than pretending to be a v0.0.2 obligation.

Therefore the candidate PAO domain is a **mixed-source validated authority set**.

This distinction is important:

```text
semantic source release of one authority record
!=
identity of the complete authority set being applied to a project
```

The frozen baseline did not expose this distinction because its accepted PAO domain was uniformly sourced from v0.0.2.

The candidate development line now requires the distinction to become explicit.

## 7. Why simply relaxing `scaf_source_release` is insufficient

One tempting migration would be:

```text
Project Application schema:
scaf_source_release = v0.0.2 OR v0.2.0rc01
```

That may be structurally capable of representing individual records, but it does not define the complete project authority domain.

A Project Application dataset is intentionally sparse: absence of a record does not mean the authority does not exist. Therefore the domain cannot be reconstructed by looking only at release tokens present in Project Application records.

For candidate authority, a project may legitimately have:

```text
an applicable disposition for one v0.0.2 PAO
an undetermined disposition for OBS-043 from v0.2.0rc01
no current disposition for many other PAOs
```

The dataset still needs one explicit answer to:

> Which validated SCAF authority set defines the universe of PAOs against which this project's dispositions are interpreted?

Per-record `scaf_source_release` alone does not answer that question.

Therefore direct schema relaxation is STOP.

## 8. Authority-set binding semantic requirement

The next semantic foundation should introduce an explicit concept of a **bound SCAF authority set** for candidate Project Application consumption.

The concept must preserve at least these facts:

1. the Project Application dataset is interpreted against exactly one validated framework authority set;
2. the authority set identity is distinct from each authority record's semantic `source_release`;
3. the candidate authority set is development-only and cannot be mistaken for formal v0.1.0 authority;
4. the bound set must resolve to a validated candidate authority representation before candidate IDs may be accepted;
5. the set's PAO population is the applicability domain even when Project Application contains only sparse disposition records;
6. formal Project Application behavior remains bound to formal authority unless a separately reviewed migration says otherwise;
7. no caller-selected arbitrary registry path becomes an alternate authority source simply because candidate consumption exists.

rc05 intentionally does not freeze final field names or serialization.

Possible later representation facts might include an authority-set kind, representation/development release, content identity, or controlled registry reference. The exact representation belongs to a later reviewed serialization step, not this assessment.

## 9. Per-record source provenance should be preserved

A future candidate Project Application path should not solve the mixed-source problem by rewriting all candidate authority records to one invented common `source_release`.

The source provenance remains meaningful:

```text
frozen PAO -> v0.0.2 semantic source
candidate OBS PAO -> v0.2.0rc01 semantic source
```

A candidate Project Application record should therefore remain capable of proving that its referenced authority ID resolves to the expected per-record source release within the bound authority set.

This preserves:

```text
authority-set identity
AND
per-authority semantic provenance
```

without conflating them.

## 10. Candidate-only Project Application path is preferred

The smallest safe future implementation shape is a **candidate-only Project Application path** rather than changing the accepted formal path in place.

The desired architectural separation is:

```text
Formal path
-----------
authority-registry.yaml
294 / 218 / 76
        ↓
accepted formal Project Application schema/validator
        ↓
formal v0.1.0 downstream behavior

Candidate path
--------------
candidate-authority-registry.yaml
299 / 223 / 76
        ↓
separately reviewed candidate Project Application contract/validator
        ↓
only later, if justified, candidate profile/consumption support
```

This separation has higher value than adding a mode switch to the existing production validator because it:

- keeps formal behavior stable;
- makes development authority explicit;
- permits bounded review of candidate semantics;
- avoids hidden caller-selected registry substitution;
- prevents a candidate feature from silently becoming a formal compatibility change.

Whether a later implementation reuses internal helper code is an implementation detail. The externally supported authority boundary must remain explicit.

## 11. Project Application semantics that do not need reinvention

The existing Project Application meaning remains useful for candidate obligations.

The next semantic foundation should preserve:

```text
one SCAF authority identity
+ one exact project_scope_ref
+ applicability = applicable / not_applicable / undetermined
+ controlled disposition_basis
+ decision_refs
+ authority_refs
+ supporting_refs
```

It should also preserve:

- Project Application is obligation/scope disposition, not implementation inventory;
- `not_applicable` requires controlled basis;
- `undetermined` remains distinct from resolved decisions;
- project reference presence does not prove engineering completion;
- Project Application does not mint replacement SCAF authority IDs;
- Framework Normative Invariants do not become Project Application records merely because they are in an authority set.

The new problem is authority-set binding, not applicability-state semantics.

## 12. Temporary probe inventory remains out of scope

`SCAF-OBS-041..045` do not justify converting SCAF-APP into a list of every probe, tracepoint, log statement, diagnostic counter, recorder hook, or temporary development edit.

The candidate Project Application concern remains at obligation/scope level, for example:

```text
SCAF-OBS-042 applicable to project scope X
with controlled project basis/evidence references
```

A project may separately maintain local instrumentation registers, change records, verification records, issue records, or evidence indices as appropriate.

Those project-local artifacts may be referenced by Project Application, but they are not framework authority records and are not SCAF-APP record identities.

## 13. Effective Project Profile incompatibility with mixed-source candidate authority

The existing Effective Project Profile semantics currently define the profile PAO domain as:

> the validated Project-Applicable Obligation population for the SCAF source release to which Project Application is bound.

The deterministic generator implements that rule by filtering authority records where:

```text
authority_class == Project-Applicable Obligation
AND
record.source_release == profile/project scaf_source_release
```

This is correct for the uniform frozen v0.0.2 domain.

It is not sufficient for the candidate authority set.

If a future profile used:

```text
scaf_source_release: v0.0.2
```

it would derive only the 218 frozen PAOs and omit `OBS-041..045`.

If it used:

```text
scaf_source_release: v0.2.0rc01
```

it would derive only the five candidate PAOs and omit the 218 inherited frozen PAOs.

Either result would be an incomplete candidate PAO domain.

Therefore Effective Project Profile migration is DEFER until authority-set semantics exist.

A later profile migration, if justified, should derive the complete PAO domain from the **validated bound authority set**, while preserving per-authority source provenance separately.

rc05 does not implement or authorize that change.

## 14. Why later consumers remain deferred

The accepted downstream chain is intentionally layered:

```text
validated Project Application
        ↓
Effective Project Profile
        ↓
Consumption Selection
        ↓
Context Source Association
        ↓
Controlled Context Package
```

Candidate authority has no independent reason to jump directly into the later stages.

Until a candidate Project Application contract exists and a complete candidate profile domain can be derived truthfully, later consumers would have no validated project-applicability state to consume.

Therefore:

```text
Effective Project Profile            DEFER
Consumption Selection                DEFER
Context Source Association           DEFER
Controlled Context Package           DEFER
```

No hidden assumption is made that these layers must eventually migrate. Each remains subject to a later dependency/value check.

## 15. Project Application query views remain subordinate

The existing Project Application query/view layer explicitly owns validation of its input and separately validates the frozen authority query domain.

It should not be modified ahead of the Project Application validator/contract itself.

A candidate query for `SCAF-OBS-041` would only become meaningful after a candidate Project Application path can validate that ID against a controlled candidate authority set.

Therefore query/view migration is DEFER with the Project Application implementation step.

## 16. Formal promotion is not a substitute for this distinction

One option would be to avoid candidate Project Application support entirely and wait until a future formal v0.2.0 promotion.

That would reduce development machinery, but it has two costs:

1. the five candidate PAOs could not be exercised through SCAF's own project-applicability model before formal promotion;
2. even a future formal registry may legitimately preserve mixed semantic source provenance for inherited versus newly introduced authority.

Therefore the authority-set versus per-record source-release distinction has value beyond this one candidate RC line.

The distinction should still be introduced conservatively and only at semantic level first.

## 17. Executability classification

rc05 separates facts that can later be machine-validated from engineering judgments that remain project-owned.

| Concern | Potential machine role | Boundary |
|---|---|---|
| Authority-set identity/binding | Structurally/source-aware executable | Validator can prove the Project Application dataset is bound to the intended validated authority set. |
| Authority ID membership in bound set | Executable | Validator can resolve one ID in the bound authority representation. |
| Authority class | Executable | Validator can require Project-Applicable Obligation. |
| Per-record source release | Executable | Validator can compare Project Application provenance with resolved authority record provenance. |
| Project Application record uniqueness/order/state compatibility | Executable | Existing representation rules can remain machine-checked. |
| Whether OBS-041..045 are applicable to a specific project scope | Engineering/project governance judgment | SCAF must not infer this from authority presence alone. |
| Adequacy of a temporary probe purpose/removal criterion | Engineering judgment | Not machine-decided by authority-set binding. |
| Whether cleanup/regression evidence is sufficient | Engineering/verification judgment | May be supported by project evidence contracts but not generically decided here. |
| Whether observer effect/resource cost is acceptable | Engineering judgment | Requires project timing/resource/evidence analysis. |
| Whether operational non-dependence is actually satisfied | Project-specific evidence/judgment | Repository structure alone is insufficient. |

## 18. Applicability examples are informative only

Candidate consumption does not mean every project must create dispositions for the five obligations in the same way.

Possible project outcomes include:

```text
OBS-041 applicable
OBS-042 applicable
OBS-043 applicable
OBS-044 undetermined pending verification strategy
OBS-045 applicable
```

or, under a different project scope and controlled basis:

```text
OBS-042 not_applicable
```

The framework does not infer these states from project type, MCU/PC/SoC platform, logging mechanism, storage presence, safety classification, lifecycle label, or use of a specific diagnostic framework.

The examples demonstrate why Project Application support has value; they are not defaults.

## 19. L3 / L4 / code-generation decisions remain STOP

Nothing in the downstream-consumption assessment changes the earlier conclusions:

```text
new L3 Pattern                                STOP
immediate L3 trace migration                 STOP
L4 diagnostic instrumentation guidance       STOP
generic probe/log API                        STOP
generic storage/export topology              STOP
generic instrumentation code generation      STOP
generic CI proof of cleanup/non-dependence    STOP
```

Project Application consumption determines whether a framework obligation is in scope for a project. It does not select or implement the mechanism used to satisfy it.

## 20. Source-package hygiene note

The reviewed rc04 source package carried deletion of seven generated Python `__pycache__` / `.pyc` artifacts as non-semantic hygiene. The subsequently committed rc04 Git tree on `main` retained those seven tracked cache objects.

rc05 is based on the actual committed rc04 Git predecessor, not on an alternate reviewed-package tree.

The rc05 source package again leaves those generated cache files deleted in the working tree and preserves `.gitignore` rules. This is non-semantic hygiene only and does not change the dependency/value decision.

Review/test execution should use:

```text
PYTHONDONTWRITEBYTECODE=1
```

so generated cache bytes do not reappear during review.

The rc05 reviewer should verify the Git predecessor identity separately from this non-semantic working-tree cleanup.

## 21. Bounded negative / over-expansion conditions

The assessment is considered incorrect if it implies or authorizes any of the following:

1. candidate authority is already formal v0.1.0 authority;
2. existing formal Project Application silently accepts candidate IDs;
3. caller-selected arbitrary authority registry paths become supported production input;
4. changing `scaf_source_release` to a two-value enum fully solves candidate consumption;
5. a single source release can truthfully identify the complete mixed candidate PAO domain;
6. inherited frozen authority source releases are rewritten merely to make candidate consumption easier;
7. Project Application becomes a per-probe/per-log-item inventory;
8. Effective Project Profile migration occurs before an authority-set binding contract exists;
9. later consumption/context layers are changed merely because Project Application may later support candidate authority;
10. candidate support automatically requires L3/L4 changes;
11. candidate support implies generic probe/log code generation;
12. candidate support implies generic machine decision of applicability, cleanup sufficiency, observer-effect acceptance, or operational non-dependence;
13. a formal/candidate mode switch is added to the existing production validator before the semantic authority-set boundary is reviewed;
14. all projects are presumed to require the five candidate obligations without Project Application judgment.

## 22. Required validation of preserved state

rc05 changes assessment/navigation records only. The preserved executable state must continue to demonstrate:

```text
formal authority validator:        294 / 218 / 76 PASS
candidate authority validator:     299 / 223 / 76 PASS
candidate frozen projection:       294 MATCH
candidate records:                 5
L3 trace validator:                12 patterns / 119 relations PASS
frozen release integrity:          docs/normative MATCH; docs/l3 MATCH
Project Application validator:     PASS against formal authority only
```

A disposable Project Application probe using `SCAF-OBS-041` should continue to fail under the existing formal-only validator. That rejection is expected evidence that rc05 performed assessment rather than migration.

## 23. Recommended next RC if rc05 passes

A clean rc05 review may authorize only:

```text
v0.2.0rc06 — Candidate Authority-Set Binding and Project Application
Consumption Semantic Foundation
```

The rc06 semantic foundation should define at least:

1. meaning and ownership of a bound framework authority set;
2. formal versus candidate authority-set distinction;
3. authority-set identity versus per-record semantic source release;
4. candidate Project Application domain membership semantics;
5. preservation of sparse Project Application disposition records over a complete bound PAO domain;
6. per-record source-provenance consistency;
7. no caller-selected arbitrary registry substitution;
8. formal Project Application compatibility preservation;
9. the boundary that Effective Project Profile and later consumers remain deferred.

rc06 should **not** yet introduce:

- a candidate Project Application YAML serialization;
- a candidate Project Application schema;
- a candidate Project Application validator;
- Effective Project Profile changes;
- consumption/context changes;
- L3/L4 changes;
- code generation;
- generic runtime-instrumentation CI.

A later dependency/value gate should decide which representation/tooling step, if any, follows the semantic foundation.

## 24. Acceptance boundary

A clean rc05 review means only:

> Candidate Project Application consumption has material value, but the smallest justified next migration is an authority-set binding / Project Application consumption semantic foundation. Direct implementation against the existing formal consumer chain is not yet justified.

It does not promote/freeze `SCAF-OBS-041..045` and does not authorize downstream implementation.
