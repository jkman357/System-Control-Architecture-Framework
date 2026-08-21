# SCAF v0.2.0rc06 — Candidate Authority-Set Binding and Project Application Consumption Semantic Foundation

**Development Release:** v0.2.0rc06  
**Development Predecessor:** v0.2.0rc05 / Git `0868bb911b9c1f71463ca195498d6cf1fbe45381`  
**Formal Authority Release:** v0.1.0 / formal authority `294 / 218 / 76`  
**Validated Candidate Authority:** `299 / 223 / 76`, including `SCAF-OBS-041..045`  
**Layer:** executable-governance semantic foundation  
**Status:** Independent-review candidate; no Project Application representation/tool migration performed

## 1. Why this RC exists

The v0.2.0rc05 independent review returned a clean result:

```text
PASS
Critical: 0
Major:    0
Minor:    0
Trivial:  0
V0.2.0RC05 CANDIDATE AUTHORITY DOWNSTREAM CONSUMPTION DEPENDENCY AND VALUE ASSESSMENT GATE: YES
```

The exact rc05 review report consumed by this semantic foundation has SHA-256:

```text
b04f661f1aab468fb66250c8a08675e97c4680b3a5594a3d574fbdd18c2ba2fb
```

That review independently confirmed the blocking semantic fact:

```text
candidate Project-Applicable Obligation domain

218 PAOs  semantic source_release: v0.0.2
  5 PAOs  semantic source_release: v0.2.0rc01
--------------------------------------------
223 PAOs  in one validated candidate authority set
```

It also confirmed that the accepted Project Application model is sparse, that an empty Project Application record set is valid, and that the current Effective Project Profile generator derives the PAO universe from one `scaf_source_release`. Therefore record-level source provenance cannot truthfully identify the complete candidate authority universe.

rc06 defines the missing semantic boundary before any candidate Project Application serialization/schema/validator work.

## 2. Scope

rc06 defines semantics only for:

1. **Authority Set Identity**;
2. **Authority Set Binding**;
3. **Authority Record Semantic Provenance**;
4. **Project Application Consumption Context**;
5. membership and validation preconditions for candidate Project Application consumption;
6. sparse/empty Project Application behavior relative to a bound authority set;
7. the future downstream domain-derivation consequence for Effective Project Profile.

rc06 does **not** add or modify:

- `examples/project-application.yaml`;
- `schemas/project-application.schema.json`;
- `tools/scaf_project_application_validator/`;
- `tools/scaf_project_application_views/`;
- Effective Project Profile schema/generator/validator;
- Consumption Selection;
- Context Source Association;
- Controlled Context Package;
- L3 Pattern or trace data;
- L4 construction guidance;
- generic probe/log APIs;
- code generation;
- generic runtime-instrumentation CI.

The formal v0.1.0 consumer path remains unchanged.

## 3. Core semantic distinction

The central rc06 distinction is:

```text
Authority Set Identity
!=
Authority Record Semantic Provenance
```

These answer different questions.

### 3.1 Authority Set Identity

**Authority Set Identity** identifies the complete validated authority universe against which a consumer operates.

For Project Application, the relevant domain is the Project-Applicable Obligation subset of that complete set.

Authority Set Identity answers:

> Which complete validated SCAF authority set defines the authority membership and applicability universe for this Project Application snapshot/context?

It does **not** answer:

> In which historical/source release was each individual authority semantic introduced or last sourced?

An authority set may legitimately contain inherited authority records whose semantic source releases differ from newer records in the same set.

### 3.2 Authority Record Semantic Provenance

**Authority Record Semantic Provenance** identifies the controlled semantic source of one authority record.

In the current candidate representation:

```text
inherited candidate-set records retain source_release: v0.0.2
SCAF-OBS-041..045 retain source_release: v0.2.0rc01
```

Those values must not be rewritten merely to make every member of the candidate set share one release token.

Per-record source provenance answers:

> From which accepted semantic source/release is this authority record reconstructed?

It does not identify the complete consumer authority universe.

### 3.3 Why one field cannot safely mean both

In the formal v0.1.0 Project Application baseline, the complete PAO set happens to be source-homogeneous:

```text
218 formal PAOs
source_release: v0.0.2
```

That historical coincidence allowed one record-level release value to serve as a practical domain cue.

The candidate set exposes the latent distinction:

```text
218 × v0.0.2
+ 5 × v0.2.0rc01
= 223 PAOs in one validated authority set
```

Therefore future candidate consumption must not infer complete-set identity from record-level source release values.

## 4. Authority Set Binding

**Authority Set Binding** is the controlled association between a Project Application consumption context and exactly one complete validated authority set.

The binding means:

```text
this Project Application snapshot/context
is interpreted against
this complete validated authority set
```

The binding is not an applicability disposition and is not a project design decision about how an obligation is realized.

### 4.1 Exactly one complete set per consumption context

A Project Application consumption context must bind to exactly one complete authority set identity.

It must not silently operate against:

- an inferred union of multiple registries;
- a caller-selected arbitrary registry path;
- whichever authority files happen to be present;
- a set reconstructed from only the Project Application records that happen to exist;
- a mix of formal and candidate authorities without a validated set contract.

### 4.2 Binding is explicit, not inferred from sparse records

Project Application is a sparse disposition dataset. It is not required to contain one record for every PAO.

Therefore authority-set binding cannot be inferred from:

- the set of authority IDs present in Project Application records;
- the set of `scaf_source_release` values present in those records;
- the first record;
- the highest observed source release;
- the absence of records.

A future machine-readable candidate Project Application representation must preserve the authority-set binding independently of record population.

### 4.3 Empty Project Application remains meaningful

An empty Project Application record list can still have a valid authority-set binding.

Conceptually:

```text
bound authority set: candidate 299 / 223 / 76
Project Application records: 0
```

means:

> The complete candidate PAO universe is known, but no current project applicability disposition records have been supplied for this snapshot/context.

It must not mean:

```text
no authority set
zero applicable obligations
all obligations not applicable
formal authority by default
```

This is required so downstream derivation can distinguish **no current disposition** from **not applicable**.

## 5. Project Application Consumption Context

A **Project Application Consumption Context** is the semantic context in which Project Application records are interpreted against one validated authority set.

At minimum, the future representation must preserve enough controlled identity to determine:

- which authority set is bound;
- whether that set is formal or candidate under the accepted development/release lifecycle;
- that the set has passed its owning validator boundary;
- which Project-Applicable Obligations are members of the bound set;
- which individual authority record each Project Application record references;
- the project scope for each applicability disposition.

Exact field names, token syntax, hashing strategy, file layout, schema vocabulary and whether the binding is stored directly in the Project Application file or in a separately controlled companion representation remain deferred.

## 6. Candidate authority-set semantics

The accepted development candidate authority set currently has these machine-reconstructed facts:

```text
299 total authority records
223 Project-Applicable Obligations
76 Framework Normative Invariants
294 exact inherited/frozen projections
5 candidate-only PAOs: SCAF-OBS-041..045
```

Its semantic status remains:

```text
validated candidate authority set
!= formal v0.1.0 authority
```

A future candidate Project Application path may consume this set only after the candidate authority validator has passed.

The candidate authority validator itself retains the rc04 prerequisite chain:

```text
formal authority valid?
   NO -> stop candidate reasoning
   YES
      -> candidate schema/binding/projection/source/inventory validation
```

Project Application candidate consumption must not become a second, weaker path for accepting an invalid candidate authority set.

## 7. Authority membership contract

For a Project Application record interpreted within a bound authority set:

1. the referenced SCAF authority ID must be a member of that bound set;
2. the referenced authority must be a **Project-Applicable Obligation** for Project Application applicability disposition;
3. a Framework Normative Invariant must not be silently converted into a Project Application record target;
4. the authority record's semantic provenance remains whatever the validated bound set records for that authority;
5. Project Application must not rewrite that provenance;
6. an authority ID outside the bound set is unresolved for that consumption context even if the ID exists in some other repository artifact or another authority set.

For the current candidate set this means inherited formal PAOs and `SCAF-OBS-041..045` can all be members of the same candidate applicability universe while retaining different semantic source releases.

## 8. Project Application record semantics remain unchanged

rc06 changes no accepted applicability meanings.

A Project Application record still represents:

```text
one SCAF Project-Applicable Obligation
+ one exact project scope
+ one applicability disposition
+ controlled disposition basis/provenance
+ controlled project references
```

The accepted applicability states remain conceptually:

- `Applicable`;
- `Not Applicable`;
- `Undetermined`.

They still do not mean:

```text
implemented
satisfied
compliant
verified
closed
```

Authority-set binding supplies the authority universe. It does not replace Project Application judgment.

## 9. No per-probe / per-log inventory expansion

Candidate authority-set binding does not change SCAF-APP granularity.

SCAF-APP remains an obligation/scope applicability-disposition model. It is not converted into an inventory of:

- probe statements;
- tracepoints;
- log calls;
- diagnostic counters;
- recorder hooks;
- RAM buffers;
- Flash/SD/USB records;
- temporary debug edits;
- test-only instrumentation instances.

Project-local instrumentation/evidence inventories may be referenced by controlled project artifacts, but those items do not become SCAF authority identities merely because `SCAF-OBS-041..045` exist.

## 10. Sparse disposition semantics

A Project Application dataset need not enumerate all PAOs in the bound authority set.

For a bound candidate set with 223 PAOs:

```text
223 PAOs in bound authority set
3 Project Application records for scope X
```

means only three explicit dispositions currently exist for that scope in that snapshot.

The other 220 obligations are not automatically:

```text
not_applicable
undetermined
satisfied
ignored
```

They are simply absent from the Project Application disposition dataset.

A later Effective Project Profile may materialize a complete domain and represent absence as `no_current_disposition`, consistent with the accepted frozen profile semantics. That downstream behavior remains deferred in rc06.

## 11. Formal-path compatibility

rc06 does not retroactively invalidate or modify the frozen formal Project Application baseline.

The accepted formal path remains:

```text
formal authority-registry.yaml
294 / 218 / 76
        ↓
existing Project Application schema / validator
formal-only authority resolution
```

The existing formal Project Application representation may continue using its accepted `scaf_source_release: v0.0.2` contract because the formal PAO universe is source-homogeneous and frozen.

The new semantic distinction is required for composite/mixed-source authority sets. It does not require an in-place modification of the frozen formal schema or validator.

## 12. Candidate-path separation

A future candidate Project Application capability should be separately controlled from the existing formal path unless a later dependency/value assessment justifies a different migration.

rc06 therefore preserves these boundaries:

```text
formal Project Application path
!= candidate Project Application path

candidate authority-set binding
!= caller-selected arbitrary registry

candidate support
!= relaxation of formal authority ownership
```

This RC does not choose the future implementation structure. Candidate support could later be represented by a separately controlled schema/validator, a bounded wrapper, or another reviewed model. That is a later representation decision.

## 13. Authority-set identity is not necessarily a release token

rc06 intentionally does not define Authority Set Identity as merely a release string.

A useful future authority-set binding must be able to deterministically identify the exact validated set, including cases where:

- one set contains records from multiple semantic source releases;
- candidate state evolves without rewriting inherited provenance;
- a later formal release contains authority inherited from older source releases.

A future machine-readable representation may use a controlled identity plus immutable content/provenance binding, but exact mechanics are deferred.

Therefore rc06 freezes the semantic need for **set identity**, not a specific token such as:

```text
v0.2.0rc06
candidate
latest
```

and not any specific hash field, filename or URI.

## 14. Authority-set lifecycle/state

Authority-set identity and authority-set lifecycle/state are related but distinct.

The current development candidate set is candidate state. The frozen v0.1.0 authority set is formal state.

A future consumer must not infer formal authority merely because:

- the set validates structurally;
- all member IDs resolve;
- a Project Application binds to it;
- the candidate set is newer than the formal set.

Formal promotion/freeze remains an explicit SCAF lifecycle decision.

Likewise, candidate Project Application consumption is permitted only within a future accepted candidate consumer path; it does not promote the candidate authority set.

## 15. Machine-readable facts versus engineering judgment

Future tooling may determine bounded representation facts such as:

- the bound authority-set identity is recognized by the candidate consumer contract;
- the owning authority-set validator passed;
- a referenced authority ID is a member of the bound set;
- the authority class is Project-Applicable Obligation;
- the authority record's semantic source provenance matches the validated bound set;
- Project Application structural/state rules are satisfied.

Future tooling must not infer or decide engineering judgments such as:

- whether `SCAF-OBS-041..045` apply to a particular project scope;
- whether temporary instrumentation purpose/removal criteria are adequate;
- whether cleanup/re-evaluation evidence is sufficient;
- whether retained diagnostic observer effect/resource cost is acceptable;
- whether an observation path is operationally independent enough for the project;
- whether a project design or verification activity has satisfied an Applicable obligation.

Those remain controlled project engineering judgments/decisions.

## 16. Effective Project Profile downstream consequence

The accepted Effective Project Profile generator currently derives the PAO universe using one source-release value.

That remains correct for the frozen source-homogeneous formal baseline, but it is insufficient for the mixed-source candidate authority set.

The semantic consequence established by rc06 is:

> A future candidate Effective Project Profile must derive its complete PAO universe from the validated **bound authority set**, not by filtering the authority registry to one record-level semantic source release.

For the current candidate set, that future domain is:

```text
223 Project-Applicable Obligations
```

not:

```text
218 only
5 only
```

rc06 does not modify the Effective Project Profile generator, schema or validator. Their migration remains deferred until candidate Project Application representation and validation exist.

## 17. Later consumer boundary

No independent value is created by migrating later consumers before the Project Application authority-set binding is represented and validated.

Therefore rc06 keeps deferred:

```text
Effective Project Profile
        ↓
Consumption Selection
        ↓
Context Source Association
        ↓
Controlled Context Package
```

Each layer must later receive its own dependency/value assessment rather than inheriting candidate support automatically.

## 18. Query/view boundary

Project Application read/query views remain subordinate to their validator boundary.

A future candidate query/view must not accept unvalidated candidate Project Application data merely because candidate authority exists.

rc06 therefore makes no query/view change.

## 19. Formal promotion does not erase the distinction

Even if `SCAF-OBS-041..045` are later formally promoted, Authority Set Identity and per-record Semantic Provenance remain conceptually distinct.

A later formal set may contain:

```text
older inherited authority semantics
+ newer promoted authority semantics
```

within one formal validated set.

Rewriting every member's provenance to the newest release would destroy useful semantic history and source traceability.

Therefore Authority Set Binding is not temporary candidate-only terminology; candidate consumption is the first case that makes the distinction operationally unavoidable.

## 20. Semantic invariants established by rc06

The rc06 candidate semantic foundation requires the following invariants for any later candidate Project Application representation/tooling:

### ASB-01 — One bound authority set

One Project Application consumption context binds to exactly one complete validated authority set.

### ASB-02 — Explicit set identity

Complete authority-set identity is preserved independently of record population and must not be inferred solely from per-record semantic source release.

### ASB-03 — Validated-set prerequisite

Candidate Project Application consumption may proceed only after the owning candidate authority validator passes.

### ASB-04 — Membership-bounded target resolution

Every Project Application SCAF target resolves within the bound authority set and must be a Project-Applicable Obligation.

### ASB-05 — Provenance preservation

Per-authority semantic source provenance is preserved from the validated bound set and is not rewritten to create artificial source homogeneity.

### ASB-06 — Sparse dataset preservation

Project Application records may remain sparse. Missing records do not acquire an applicability disposition by inference.

### ASB-07 — Empty dataset preservation

An empty Project Application record population may still bind to a complete authority set; empty records do not mean no authority universe.

### ASB-08 — Candidate/formal state separation

Binding a Project Application context to candidate authority does not make that authority formal.

### ASB-09 — No arbitrary consumer registry selection

Candidate support must not become a generic caller-selected registry path that bypasses repository-owned validation and authority-set ownership.

### ASB-10 — Applicability judgment ownership preserved

Authority-set membership and validation do not decide project applicability, sufficiency, observer-effect acceptance, verification or closure.

### ASB-11 — No per-probe inventory expansion

Authority-set binding does not turn SCAF-APP into an inventory of implementation-level instrumentation instances.

### ASB-12 — Downstream domain derives from set

A future complete PAO-domain consumer derives its domain from the validated bound authority set, not from one per-record semantic source-release token.

These are semantic invariants for the development candidate. rc06 creates no new L1/L2 normative SCAF IDs.

## 21. Representation decisions explicitly deferred

rc06 intentionally does not choose:

- a canonical authority-set identity string;
- a new Project Application top-level key;
- whether binding is embedded or companion-file based;
- a content-hash field;
- a candidate Project Application representation release token;
- YAML versus another representation;
- schema structure;
- validator API;
- CLI arguments;
- candidate query/view API;
- formal/candidate migration strategy;
- Effective Project Profile representation changes.

Those decisions require a post-semantic dependency/value assessment.

## 22. L3 / L4 / tooling STOP boundary

Authority-set binding is a governance/consumer semantic concern. It does not establish a new runtime realization mechanism.

Therefore rc06 does not justify:

- a new L3 Pattern identity;
- L3 trace changes;
- new L4 diagnostic-instrumentation construction guidance;
- probe/log APIs;
- storage/export topology;
- code generation;
- generic runtime-instrumentation CI proof.

All remain STOP / out of scope.

## 23. Required validation preservation

A valid rc06 candidate must preserve at least:

```text
formal authority validator:        294 / 218 / 76 PASS
candidate authority validator:     299 / 223 / 76 PASS
candidate frozen projection:       294 MATCH
candidate records:                 5
L3 trace validator:                12 patterns / 119 relations PASS
frozen release integrity:          docs/normative MATCH; docs/l3 MATCH
Project Application validator:     PASS against formal authority only
required existing test suites:     PASS
git diff --check HEAD:             PASS
```

The existing formal Project Application validator must continue rejecting `SCAF-OBS-041` as unresolved frozen authority.

## 24. Acceptance boundary

A clean rc06 review establishes only the semantic contract for candidate Authority-Set Binding and Project Application Consumption.

A clean rc06 review may authorize a **new dependency/value assessment** for the smallest machine-readable representation and validation path that can preserve these semantics.

It does **not** authorize:

- candidate Project Application serialization;
- a candidate Project Application schema;
- a candidate Project Application validator;
- an in-place modification of the frozen formal Project Application schema/validator;
- Effective Project Profile migration;
- later consumer migration;
- L3/L4 expansion;
- code generation;
- generic runtime-instrumentation CI.

The intended next question after a clean review is:

> What is the minimum representation/validation boundary needed to bind a candidate Project Application context to an exact validated authority set without weakening the frozen formal path or over-expanding downstream consumers?
