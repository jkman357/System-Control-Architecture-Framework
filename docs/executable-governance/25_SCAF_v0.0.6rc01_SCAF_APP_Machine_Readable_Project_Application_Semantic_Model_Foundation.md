# SCAF v0.0.6rc01 — SCAF-APP Machine-Readable Project Application Semantic Model Foundation

**Development Release:** v0.0.6rc01
**Status:** Semantic Model Foundation / Review Candidate
**Date:** 2026-08-18
**Upstream Frozen Baselines:** v0.0.2 L1/L2; v0.0.3 L3; v0.0.4 Executable Governance; v0.0.5 L3 Machine-Readable Traceability

## 1. Decision Purpose

This RC opens the first controlled development line after the formal v0.0.5 freeze.

The next milestone is selected from the remaining architecture/governance gap rather than by automatically advancing to L4. The frozen framework already provides:

```text
v0.0.2  frozen L1/L2 normative authority
v0.0.3  frozen L3 Pattern / Mechanism Catalog
v0.0.4  frozen machine-readable authority + executable-governance baseline
v0.0.5  frozen machine-readable L2↔L3 traceability + validated read-only query boundary
```

What remains intentionally outside those frozen capabilities is project-specific applicability and disposition semantics. v0.0.5 explicitly preserves the boundary that absence of an L3 mechanism must not be treated as project failure without a controlled applicability basis, and that applicability, tailoring, Project Design Authority, rationale, evidence and closure remain separate project-governance concerns.

The existing frozen Authority Kernel already assigns this cross-cutting responsibility to `SCAF-APP`:

```text
SCAF-APP
Defines Framework Semantics / Obligation
for applicability / disposition / trace semantics.
```

v0.0.6rc01 therefore defines the first **machine-readable semantic model boundary for project application records**. It does not create a new framework plane and does not change frozen L1/L2, L3, registry, schema, validator, query or CI behavior.

## 2. Core Principle

The semantic model preserves the following engineering rule:

> **SCAF does not decide the engineering answer for the project. It ensures that material questions are surfaced, project judgments are attributable, and the basis for those judgments can be retained and revisited.**

Accordingly:

```text
machine-determinable fact
        ≠
engineering judgment
        ≠
project authority decision
        ≠
verification result
        ≠
closure
```

A future tool may determine representation facts that are objectively checkable. Where project-specific engineering judgment is required, the project record must preserve the judgment and its rationale/provenance rather than replacing that judgment with a generic framework default.

## 3. Scope of rc01

v0.0.6rc01 defines only:

1. the authority boundary of a machine-readable `SCAF-APP` Project Application Record;
2. the minimum semantic concepts that a future representation must preserve;
3. project-scope binding requirements;
4. applicability semantics, including a legitimate unresolved/undetermined state;
5. separation between applicability and project design/decision authority;
6. rationale/provenance semantics for project judgments;
7. distinction between representation invalidity and unresolved engineering work;
8. trace/reference expectations to frozen SCAF authority and project-side authoritative artifacts;
9. prohibited inferences that future schema/validator/query/AI consumers must not make;
10. bounded next-stage inputs for later serialization/schema/validation work.

This RC does **not** create a project-application YAML/JSON file, schema, validator, generated profile, CLI, AI resolver, CI gate or L4 content.

## 4. Frozen Semantic Basis

This model is subordinate to the accepted framework-side semantics already present in frozen SCAF authority.

The frozen Authority Kernel establishes that:

- a Project-Applicable Obligation applies when it is Applicable through SCAF Project Application / Framework Scan;
- `SCAF-APP` defines framework semantics/obligation for applicability/disposition/trace semantics;
- a project Framework Scan record dispositions/traces project state but is not SCAF normative authority, Project Design Authority, risk-acceptance authority, verification authority or closure authority;
- applicability, decision, deviation, risk, verification obligation, verification execution/result, evidence, closure and re-evaluation are distinguishable state dimensions;
- the authority that owns the underlying requirement/design/risk/deviation retains the corresponding closure authority.

The frozen v0.0.5 release additionally states that a validator is not authorized to equate absence of a mechanism with project failure without a controlled applicability basis.

This RC does not reopen or rewrite those frozen statements. It specifies how a later machine-readable project-application representation must preserve them.

## 5. Project Application Record — Semantic Role

A **Project Application Record** is a controlled project-side trace/disposition record governed by `SCAF-APP` semantics.

Its role is to connect a specific SCAF concern/obligation to a defined project scope and preserve the project's controlled disposition and supporting provenance.

Conceptually:

```text
frozen SCAF authority identity
        +
explicit project scope
        ↓
project applicability disposition
        ↓
required project judgment / decision trace, where applicable
        ↓
rationale / provenance
        ↓
links to project-side authoritative artifacts / authorities
```

A Project Application Record is **not**:

- a new SCAF normative requirement;
- the Project Design Authority;
- the Controlled Decision itself when that decision is owned elsewhere;
- the Authoritative Artifact that defines the project design unless project governance separately designates that artifact for that purpose;
- a Pattern-selection authority;
- a verification result;
- a risk-acceptance decision;
- a closure authority;
- evidence merely because it references evidence;
- a replacement for project architecture, interface, safety, security, risk or verification records.

## 6. Minimum Semantic Concepts

A future machine-readable Project Application Record must be able to preserve at least the following concepts without conflation. The initial applicability target domain is the frozen **Project-Applicable Obligation** population. Framework Normative Invariants are framework-governance constraints and are not silently converted into project-applicability records by this model.

| Concept | Required semantic meaning |
|---|---|
| SCAF target reference | Stable reference to the applicable frozen SCAF authority identity being considered |
| Project scope | The bounded project/system/Node/domain/interface/service/etc. context for which the disposition is asserted |
| Applicability disposition | Whether the referenced SCAF obligation is applicable, not applicable, or currently undetermined for that scope |
| Judgment / decision trace | Reference to the project-side decision/judgment responsibility when applicability or the obligation requires project-specific determination |
| Rationale / provenance | Controlled basis explaining or attributing a project judgment where such judgment cannot be derived solely from machine-verifiable representation facts |
| Authority provenance | Reference/identity of the project authority role or controlled source that owns the underlying project judgment/decision when required |
| Supporting references | Controlled links to authoritative project artifacts, external-authority inputs, or other sources used as the basis for the disposition |

These are semantic concepts, not frozen field names.

v0.0.6rc01 deliberately does **not** freeze:

- YAML versus JSON;
- repository filename;
- top-level keys;
- exact property names;
- identifier syntax for project-local records;
- serialization ordering;
- schema vocabulary;
- complete lifecycle state fields;
- exact enum token spelling.

Those are later representation/schema decisions.

## 7. Project Scope Binding

Applicability is meaningful only relative to explicit scope.

A future representation must not allow an applicability statement to be silently interpreted as project-global when the underlying judgment is Node-, domain-, interface-, service-, mode-, configuration- or lifecycle-specific.

For example, these are different assertions:

```text
SCAF obligation X is Applicable to the complete project.
SCAF obligation X is Applicable to Node N2.
SCAF obligation X is Not Applicable to a stateless utility Node.
SCAF obligation X is Undetermined for an interface whose ownership is not yet assigned.
```

A machine-readable representation must preserve enough scope identity to prevent one record from being reused outside the scope for which the project judgment was made.

This RC does not yet define a project-scope registry or canonical scope identity syntax.

## 8. Applicability Semantic Classes

The current semantic model carries three distinct applicability meanings, consistent with the already documented SCAF-APP conceptual taxonomy.

### 8.1 Applicable

The SCAF obligation is relevant to the declared project scope and enters the project authority/decision/realization/verification chain as required by the obligation and project governance.

`Applicable` does **not** mean:

```text
Pattern selected
implemented
satisfied
compliant
verified
closed
```

### 8.2 Not Applicable

The SCAF obligation has been considered for the declared project scope and a controlled project judgment concludes that it does not apply to that scope.

`Not Applicable` must not be treated as deletion of the SCAF obligation or modification of framework authority.

Because `Not Applicable` changes the project disposition of a Project-Applicable Obligation, a future representation must preserve a controlled basis sufficient to understand why the judgment was made and who/what owns that basis under project governance.

### 8.3 Undetermined

The project does not yet have a sufficient controlled basis to decide whether the SCAF obligation applies to the declared scope.

`Undetermined` is a legitimate engineering state and is intentionally distinct from:

```text
invalid data
schema error
project failure
verification failure
non-compliance
Not Applicable
```

An `Undetermined` state must remain visible and revisitable. A future representation must preserve enough unresolved-basis/dependency provenance to understand why the applicability decision is still open and what controlled input is missing or expected; detailed re-evaluation-state serialization remains deferred. Future project tooling may report the state as open/pending engineering work, but must not automatically convert it into `Not Applicable`, `Applicable`, or project failure.

The serialization tokens for these semantic classes are deferred.

## 9. Applicability Is Not a Single Project Status

The frozen Authority Kernel requires multiple project dimensions to remain distinguishable. Therefore a future Project Application representation must not collapse project state into a single value such as:

```text
PASS
FAIL
DONE
OPEN
```

or any other status that implicitly merges:

```text
applicability
+ decision
+ deviation
+ risk
+ verification
+ evidence
+ closure
```

v0.0.6rc01 focuses on the front of this chain. Later RCs may serialize additional state dimensions, but they must preserve the frozen separation rather than replacing it with one checklist outcome.

## 10. Engineering Judgment and Rationale

A future tool may directly determine facts whose truth is bounded by an accepted machine-readable contract, for example:

```text
Does a referenced SCAF ID exist?
Is a referenced source path valid?
Does a record contain a structurally valid scope reference?
Is a machine representation internally consistent?
```

Those facts are not equivalent to project engineering judgment.

Examples of project judgment include:

```text
Is this obligation applicable to this architecture scope?
Is an externally supervised Node's recovery arrangement sufficient for this project?
Is a specific resource/timing/freshness consequence material?
What project design decision satisfies an Applicable obligation?
```

Where a disposition depends on engineering judgment, the future project record must preserve a **controlled rationale/provenance basis** rather than presenting the tool as the decision owner. Where an applicability result is a direct consequence of accepted machine-verifiable scope facts, provenance may reference those controlled facts instead of requiring redundant narrative prose.

The rationale may reference a controlled authoritative artifact rather than duplicating its full prose, provided the record retains enough provenance to reconstruct why the disposition exists.

A generated or AI-suggested rationale is not by itself an approved project judgment. Approval/ownership remains with the project authority responsible for the underlying decision.

## 11. Decision and Authority Separation

Applicability answers:

> Does this SCAF obligation apply to this declared project scope?

It does not answer:

> What exact project architecture/design value or mechanism shall be used?

When an Applicable obligation requires a project-specific decision, the Project Design Authority remains responsible for that Controlled Decision.

A future Project Application Record may trace the decision state, owner and artifact, but must not acquire that authority merely because it stores the references.

Likewise, a future record that says `Not Applicable` must not imply that SCAF itself made that project decision. It records the project disposition and its provenance.

## 12. Tailoring / Deviation Boundary

Tailoring is intentionally **not** collapsed into applicability in this RC.

The following are semantically different:

```text
Not Applicable
Applicable, realized as defined
Applicable, with a controlled project-specific adaptation
Applicable, with a deviation/exception under project governance
```

The frozen Authority Kernel already requires deviation to remain a separate state dimension. v0.0.6rc01 therefore does not define a canonical tailoring enum and does not authorize a future consumer to interpret `Not Applicable` as a tailoring mechanism.

A later RC may define machine-readable tailoring/adaptation semantics after the applicability/authority boundary is accepted.

## 13. Representation Invalidity vs Engineering Unresolved State

Future executable controls must distinguish two fundamentally different classes of condition.

### 13.1 Representation-invalid conditions

Examples include:

```text
unknown SCAF authority identity
illegal serialized value
broken reference
missing required structural concept
duplicate project-record identity under a later accepted identity rule
scope reference that cannot resolve under a later accepted scope model
machine-detectable contradiction prohibited by the accepted representation contract
```

These conditions may validly fail structural/semantic validation.

### 13.2 Engineering-unresolved conditions

Examples include:

```text
applicability remains Undetermined
project judgment is pending
required Project Design Authority decision has not yet been made
rationale/evidence is awaiting an upstream architecture decision
```

These conditions may be reportable as open/pending/unresolved project work, but their existence is not equivalent to malformed representation.

A future validator must not convert engineering incompleteness into representation invalidity merely to produce a binary PASS/FAIL checklist.

## 14. Framework Truth vs Project Truth

Machine-readable framework authority and project application state remain separate data/authority surfaces.

Conceptually:

```text
authority-registry.yaml
  framework-side authority representation
        │
        │ reference by stable SCAF identity
        ▼
future project-application representation
  project-side applicability/disposition/provenance
```

Project-specific applicability, rationale, PDA identity, project design values, verification state, evidence state and closure state must not be written into `authority-registry.yaml` merely because that registry is already machine-readable.

The frozen authority registry remains subordinate representation of frozen framework authority, not a project-instance database.

## 15. Relationship to Frozen L3 Traceability

The frozen v0.0.5 L2↔L3 trace surface is a navigation/decision-support input.

A trace result such as:

```text
L2 obligation -> candidate L3 Pattern relations
```

must not by itself create project applicability or Pattern selection.

The order remains conceptually:

```text
SCAF authority
    ↓
project applicability / disposition
    ↓
project decision context
    ↓
L3 candidate-pattern navigation, where useful
    ↓
Project Design Authority selection/adaptation decision
```

A future resolver may combine validated framework trace data with controlled project application state for read-only context assembly, but only after the project-application representation has its own accepted contract and validation boundary.

## 16. Prohibited Inferences

v0.0.6rc01 explicitly prohibits a future implementation from inferring any of the following solely from the presence/absence of framework or L3 data:

```text
No L3 Pattern exists -> project failure
L3 Pattern exists -> obligation Applicable
L3 primary realization candidate -> Pattern selected
Applicability = Applicable -> obligation satisfied
Applicability = Not Applicable -> SCAF obligation deleted
Applicability = Undetermined -> invalid record
Rationale text exists -> project authority approved the judgment
Evidence reference exists -> verification passed
Verification passed -> underlying design/risk/deviation closed
Project Application Record -> Project Design Authority
```

Any later executable inference beyond machine-verifiable representation facts requires an explicit semantic contract and review gate.

## 17. Intended Future Machine-Readable Flow

This RC establishes only the semantic foundation for a later sequence such as:

```text
frozen SCAF authority
        ↓
accepted Project Application semantic model       <- rc01
        ↓
future canonical serialization
        ↓
future schema / structural validation
        ↓
future source/reference-aware validation
        ↓
future deterministic project-application views
        ↓
future effective project-context assembly
```

The sequence is dependency-oriented, not a pre-committed RC count.

Each later capability is selected from review results and remaining gaps.

## 18. Explicit Deferrals

v0.0.6rc01 intentionally defers:

- concrete `project-application.yaml` or JSON serialization;
- schema and exact property names;
- project-scope registry/model;
- complete Decision / Deviation / Risk / Verification / Evidence / Closure serialization;
- canonical tailoring/adaptation states;
- automatic rationale generation/approval;
- automatic applicability classification;
- AI authority to approve project engineering decisions;
- Pattern recommendation or auto-selection;
- generated Effective Project Profile;
- project-context resolver/packager;
- CI enforcement of project applicability completion;
- code generation;
- new L3 Patterns;
- L4 implementation/verification guidance;
- expansion of the frozen v0.0.4 production trust set.

None of these is implied by acceptance of rc01.

## 19. Acceptance Criteria for This RC

This semantic foundation is ready to support a later serialization RC only if review confirms that:

1. it preserves frozen SCAF-APP authority semantics without modifying the frozen L1/L2 or L3 baseline;
2. it does not create a new framework plane or duplicate Project Design Authority;
3. it keeps framework authority separate from project-specific disposition and does not silently convert Framework Normative Invariants into project-applicability targets;
4. it gives `Undetermined` a legitimate semantic meaning distinct from invalidity/failure;
5. it keeps applicability distinct from Decision, Deviation, Risk, Verification, Evidence and Closure;
6. it requires project scope to bound applicability assertions;
7. it preserves rationale/provenance for engineering judgment without making the record/tool the decision owner;
8. it does not turn absence/presence of an L3 mechanism into project applicability, selection, satisfaction or failure;
9. it leaves serialization/schema/validator mechanics sufficiently deferred that the semantic contract can be reviewed independently;
10. it does not implicitly advance SCAF to L4.

## 20. rc01 Boundary Summary

```text
v0.0.5 frozen baseline
        ↓
SCAF-APP already owns framework applicability/disposition/trace semantics
        ↓
v0.0.6rc01 defines the machine-readable Project Application semantic boundary
        ↓
NO concrete registry yet
NO schema yet
NO validator yet
NO automatic applicability decision
NO checklist-style mechanism-presence gate
NO L4 advancement
```

The intended outcome is not a machine that chooses project architecture. It is a controlled semantic basis from which future tools can reliably distinguish what they can determine from what the project must judge and record.
