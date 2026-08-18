# SCAF v0.0.6rc02 — SCAF-APP Canonical Project Application Record Model

**Development Release:** v0.0.6rc02  
**Status:** Canonical Record Model / Review Candidate  
**Date:** 2026-08-18  
**Upstream Frozen Baselines:** v0.0.2 L1/L2; v0.0.3 L3; v0.0.4 Executable Governance; v0.0.5 L3 Machine-Readable Traceability  
**Accepted Development Basis:** v0.0.6rc01 SCAF-APP Machine-Readable Project Application Semantic Model Foundation

## 1. Decision Purpose

The independent v0.0.6rc01 review returned a clean gate:

```text
Critical: 0
Major:    0
Minor:    0
Trivial:  0

V0.0.6RC01 SCAF-APP MACHINE-READABLE PROJECT APPLICATION SEMANTIC MODEL FOUNDATION GATE: YES
```

rc01 established what a future machine-readable Project Application Record means and what authority it must not acquire. The next dependency is a deterministic record contract that can later be serialized and schema-validated without allowing implementation convenience to redefine those semantics.

v0.0.6rc02 therefore defines the **canonical logical record model** for one SCAF-APP Project Application disposition. It freezes canonical concept names, cardinalities, applicability tokens, state-dependent basis requirements, identity rules and prohibited cross-field inferences.

This RC still does **not** create a repository-root project-application registry, YAML/JSON instance population, JSON Schema, validator, project-scope registry, generated Effective Project Profile, automatic applicability classifier, CI completion gate or L4 content.

## 2. Governing Principle

The rc02 record model implements the rc01 principle:

> **SCAF does not decide the engineering answer for the project. It ensures that material questions are surfaced, project judgments are attributable, and the basis for those judgments can be retained and revisited.**

The record therefore distinguishes:

```text
framework authority identity
        !=
project scope
        !=
applicability disposition
        !=
underlying project decision authority
        !=
verification result
        !=
closure
```

A serialized record may make a project disposition machine-readable. It does not become the authority that made the disposition.

## 3. rc02 Scope

rc02 defines:

1. one-record identity semantics;
2. the canonical logical field set for the initial Project Application Record;
3. controlled applicability tokens;
4. deterministic project-scope reference semantics;
5. state-dependent disposition-basis requirements;
6. controlled trace/reference surfaces for project authority and supporting sources;
7. explicit unresolved-basis semantics for `undetermined`;
8. representation-level consistency rules that a later schema/validator may enforce;
9. fields and lifecycle dimensions deliberately excluded from the initial record model;
10. the boundary between record validity and project engineering completion.

rc02 does not claim that all project application lifecycle concerns fit into one record. In particular, decision state, deviation state, risk state, verification state, evidence state, closure state and re-evaluation state remain distinct project-governance dimensions and are not collapsed into a single rc02 status field.

## 4. Target Domain

The initial rc02 record domain is exactly the frozen **Project-Applicable Obligation** population represented in the frozen authority registry:

```text
Project-Applicable Obligations: 218
Framework Normative Invariants:   76
Total authority records:         294
```

A Project Application Record shall target one existing frozen Project-Applicable Obligation identity.

A Framework Normative Invariant shall not be converted into a Project Application Record merely because it is machine-readable in `authority-registry.yaml`.

The canonical framework-side target remains the frozen authority identity. Project application does not mint replacement SCAF authority IDs.

## 5. Canonical Logical Record Shape

The initial logical record contains the following canonical concepts. These names are now the accepted **logical field names** for the v0.0.6 line. rc02 does not yet freeze YAML/JSON syntax or mapping order.

| Field | Cardinality | Initial semantic contract |
|---|---:|---|
| `record_id` | exactly 1 | Stable project-local identity for this Project Application Record |
| `record_kind` | exactly 1 | Constant logical value `project_application` |
| `representation_release` | exactly 1 | SCAF RC/release whose representation contract is used; initial rc02 value is `v0.0.6rc02` when a later rc02-conformant example/fixture is produced |
| `scaf_authority_id` | exactly 1 | Existing frozen Project-Applicable Obligation identity |
| `scaf_source_release` | exactly 1 | Frozen SCAF release owning the referenced obligation semantics; initial population is `v0.0.2` |
| `project_scope_ref` | exactly 1 | Project-controlled reference identifying the exact scope for which applicability is asserted |
| `applicability` | exactly 1 | Controlled token: `applicable`, `not_applicable`, or `undetermined` |
| `disposition_basis` | exactly 1 | Structured basis container preserving why/how the applicability disposition is supportable or still unresolved |
| `decision_refs` | 0..n | References to project-side controlled decisions/judgments relevant to the disposition; references do not transfer decision authority |
| `authority_refs` | 0..n | References to project authority roles/artifacts that own or approve relevant project judgment under project governance |
| `supporting_refs` | 0..n | References to controlled project/external sources used to support the disposition |

No initial field is named `status`, `pass`, `fail`, `compliant`, `verified`, `closed`, `selected`, or `implemented`.

Those concepts would collapse independent state dimensions or imply authority that the Project Application Record does not own.

## 6. Record Identity

### 6.1 `record_id`

`record_id` identifies the project-side application record, not the SCAF authority itself.

Within one project application dataset:

- every `record_id` shall be unique;
- one `record_id` shall identify one Project Application Record;
- a `record_id` shall not be reused for a different `(scaf_authority_id, project_scope_ref)` binding;
- moving or reformatting the serialized file shall not silently change record identity;
- rc02 does not freeze the project-local identifier syntax.

The following are different identities:

```text
SCAF-ROB-015 applied to Project scope A
SCAF-ROB-015 applied to Node N2
SCAF-ROB-015 applied to Interface IF-3
```

Even though they share the same SCAF authority ID, they are different project application assertions because their scope differs.

### 6.2 Target/scope uniqueness

A later serialization/validator shall reject ambiguous duplicate active records that assert more than one applicability disposition for the same canonical `(scaf_authority_id, project_scope_ref)` pair in one dataset unless a separately reviewed versioning/supersession model explicitly permits them.

rc02 does not yet define record supersession/history serialization.

## 7. Framework Authority Reference

`scaf_authority_id` shall resolve to exactly one frozen Project-Applicable Obligation in the accepted framework authority representation/source chain.

For the initial population:

```text
scaf_source_release: v0.0.2
```

means that the referenced normative semantics are owned by the frozen v0.0.2 L1/L2 source baseline. It does not mean the project application judgment was made in v0.0.2.

The Project Application Record shall not copy normative prose and treat the copy as a new authority source.

The directional boundary remains:

```text
frozen normative source
        ↓
validated authority identity
        ↓
project application record references that identity
```

not:

```text
project application record
        ↓
redefines or overrides frozen SCAF authority
```

## 8. Project Scope Reference

`project_scope_ref` is a required project-controlled reference.

Its purpose is to prevent an applicability assertion from being silently interpreted outside the scope for which it was made.

The initial contract requires that a future concrete representation treat `project_scope_ref` as an opaque controlled reference whose meaning is owned by project governance. SCAF may validate its presence and, once a project-scope resolution contract exists, its resolvability. SCAF shall not infer a broader scope from naming conventions.

Examples of scope concepts that a project may control include:

```text
project
system
Node
subsystem/domain
interface
service
mode/configuration/lifecycle context
```

rc02 does not freeze a `scope_kind` enum, hierarchy syntax, path grammar, project-scope registry filename, or inheritance model.

Until such a model is separately reviewed, consumers shall not infer that one scope includes another merely because the text of one reference appears hierarchical.

## 9. Canonical Applicability Tokens

rc02 freezes the initial serialization-neutral applicability token vocabulary:

```text
applicable
not_applicable
undetermined
```

These tokens carry only applicability semantics.

### 9.1 `applicable`

The referenced Project-Applicable Obligation is relevant to the declared `project_scope_ref`.

It does not imply:

```text
Pattern selected
implementation complete
satisfied
compliant
verified
closed
```

### 9.2 `not_applicable`

The obligation was considered for the declared scope and the project has a controlled basis for concluding that it does not apply to that scope.

It does not delete, weaken or modify the framework obligation.

It is not a generic substitute for tailoring, deviation, exception, risk acceptance, implementation choice or verification waiver.

### 9.3 `undetermined`

The project does not yet possess a sufficient controlled basis to decide applicability for the declared scope.

`undetermined` is a valid engineering disposition token and shall not be interpreted as:

```text
malformed representation
schema failure
project failure
non-compliance
verification failure
not_applicable
```

A later consumer may report it as unresolved/open work, but shall keep that report distinct from representation-invalid diagnostics.

## 10. `disposition_basis` Contract

Every record contains exactly one `disposition_basis` logical container.

The container exists so the record can preserve the basis of the applicability disposition without requiring every project to manufacture narrative prose when controlled references already provide the basis.

The container has the following canonical logical members:

| Member | Cardinality | Meaning |
|---|---:|---|
| `summary` | 0..1 | Concise project-controlled rationale text; may be omitted when controlled references fully carry the basis |
| `basis_refs` | 0..n | References to controlled facts, decisions, analyses, architecture records, external-authority inputs or other authoritative project sources that support the disposition |
| `unresolved_reason` | 0..1 | Required semantic explanation when `applicability == undetermined` |
| `awaiting_refs` | 0..n | Controlled references to missing/pending inputs, decisions or authority assignments expected to resolve an `undetermined` disposition |

At least one meaningful basis element shall be present according to the state-dependent rules below.

### 10.1 Basis rule for `applicable`

For `applicable`, the record shall preserve enough basis to make the assertion attributable and reviewable.

At least one of the following shall be present:

```text
disposition_basis.summary
disposition_basis.basis_refs
decision_refs
authority_refs
supporting_refs
```

The model does not require redundant prose when a controlled project artifact unambiguously provides the basis.

### 10.2 Basis rule for `not_applicable`

For `not_applicable`, a controlled basis is mandatory because the project is explicitly disposing a Project-Applicable Obligation as outside the declared scope.

At least one of:

```text
disposition_basis.summary
disposition_basis.basis_refs
decision_refs
```

shall be present, and the overall record shall retain sufficient provenance to identify the project-controlled source/authority of that judgment through `authority_refs`, `decision_refs`, or controlled basis references.

A bare record containing only:

```text
scaf_authority_id
project_scope_ref
applicability: not_applicable
```

is semantically incomplete under rc02.

### 10.3 Basis rule for `undetermined`

For `undetermined`:

- `disposition_basis.unresolved_reason` is required;
- at least one of `disposition_basis.awaiting_refs`, `disposition_basis.basis_refs`, `decision_refs`, `authority_refs`, or `supporting_refs` should identify the missing/dependent controlled context when such a reference exists;
- the record shall not invent a project decision merely to eliminate the unresolved state.

The purpose is to retain **why the question remains open** and, where possible, **what controlled input is expected to resolve it**.

## 11. Project Judgment / Authority Trace References

### 11.1 `decision_refs`

`decision_refs` point to project-controlled decision/judgment artifacts relevant to applicability or to a required downstream project determination.

A reference does not mean the Project Application Record owns the decision.

### 11.2 `authority_refs`

`authority_refs` identify project authority roles/artifacts that own or approve the relevant project judgment under project governance.

The record shall not synthesize authority ownership from repository path, author name, AI generation metadata or tool output unless project governance separately designates those as controlled authority identifiers.

### 11.3 `supporting_refs`

`supporting_refs` identify supporting controlled sources. They may include project architecture, interface, verification planning, safety/security/risk analysis, external requirements, system context or other controlled inputs.

A supporting reference is not automatically evidence of satisfaction and does not imply verification or closure.

## 12. Representation Validity Rules Authorized by rc02

rc02 authorizes later schema/validator work to treat the following as representation-invalid or contract-invalid conditions, once the concrete serialization is reviewed:

- missing any exactly-one required field;
- unsupported `record_kind`;
- unsupported applicability token;
- unknown/unresolvable `scaf_authority_id`;
- target authority is not a Project-Applicable Obligation;
- source-release mismatch against the accepted target authority contract;
- empty/unresolvable `project_scope_ref` once scope resolution is part of the accepted validation contract;
- duplicate `record_id`;
- ambiguous duplicate `(scaf_authority_id, project_scope_ref)` assertion;
- `not_applicable` without the required controlled basis/provenance;
- `undetermined` without `unresolved_reason`;
- state-incompatible basis content when a later schema contract defines it precisely;
- malformed controlled references under a separately accepted reference grammar.

These are representation/contract consistency questions.

They remain distinct from whether the project has completed the underlying engineering work.

## 13. Engineering-Unresolved Conditions That Are Not Representation Invalidity

The following may be legitimate engineering-unresolved states even when the record is structurally valid:

- `applicability: undetermined` with a valid unresolved basis;
- a referenced Project Design Authority decision is pending;
- a needed architecture boundary is not yet decided;
- a project authority assignment is pending;
- a controlled external input is not yet available;
- supporting evidence or verification work is not yet complete where those lifecycle dimensions are owned elsewhere.

A future validator may report these as separate open/unresolved findings or query views. It shall not reclassify them as malformed representation merely to produce binary PASS/FAIL project completion output.

## 14. Explicitly Deferred Lifecycle Dimensions

The rc02 record intentionally does not add canonical fields for:

```text
decision_state
deviation_state
risk_state
verification_obligation_state
verification_execution_state
verification_result
evidence_state
closure_state
re_evaluation_state
Pattern selection
tailoring classification
implementation/realization state
```

Those dimensions remain real and important. They are deferred because their ownership and lifecycle semantics must be modeled without turning the initial applicability record into an all-purpose ALM database row.

Later extensions may reference or compose these dimensions, but they must preserve the frozen `SCAF-AK-003` separation and must not overload `applicability` or `record_id` with their meaning.

## 15. Framework Truth vs Project Truth

The following separation remains mandatory:

```text
authority-registry.yaml
    -> framework authority identities/classes/source resolution

future project-application representation
    -> project-specific applicability disposition + provenance
```

Project-specific fields defined by rc02 shall not be added to frozen `authority-registry.yaml` merely because it is already machine-readable.

Similarly, `l3-trace-registry.yaml` remains a representation of frozen L2↔L3 trace and shall not store project applicability or Pattern selection.

## 16. L3 Trace Boundary

No rc02 field or token changes the frozen v0.0.5 relation semantics.

The following remain invalid inferences:

```text
No L3 Pattern trace
    -> project failure

L3 Pattern trace exists
    -> obligation is applicable

primary_realization_candidate
    -> Pattern selected

applicable
    -> Pattern selected / satisfied / verified / closed
```

A future project application consumer may combine validated authority identity, validated trace views and project disposition for navigation/context assembly, but combining those inputs does not transfer project authority to the tool.

## 17. AI / Tool Consumption Boundary

A future AI/tool may use an rc02-conformant representation to answer bounded questions such as:

```text
Which SCAF obligations have an applicability disposition for scope X?
Which are undetermined?
What controlled basis is attached to a not-applicable disposition?
Which project decision/authority references are associated?
```

It shall not infer or auto-approve:

```text
not_applicable
engineering rationale
Project Design Authority approval
Pattern selection
satisfaction
compliance
verification
closure
```

from absence/presence of fields or from generated text alone.

AI-generated rationale may be proposed as draft project input, but it is not a controlled project judgment until accepted under project governance.

## 18. rc02 Non-Claims

v0.0.6rc02 does **not** introduce or claim:

- a concrete `project-application.yaml` / JSON dataset;
- a JSON Schema;
- executable project-application validation;
- automatic registry generation;
- a project-scope registry or scope-inheritance engine;
- automatic applicability inference;
- automatic `not_applicable` approval;
- tailoring/deviation taxonomy;
- Pattern recommendation/selection;
- Effective Project Profile generation;
- context packaging/resolver behavior;
- CI enforcement of applicability completion;
- code generation;
- new L3 Pattern content;
- L4 implementation/verification guidance;
- production trust-set expansion.

## 19. Candidate Next Dependency

If rc02 is independently accepted, the next dependency may be a **concrete initial Project Application serialization foundation** that realizes this canonical record contract in a reviewable machine-readable file before schema/validator implementation.

That later RC should be review-driven and is not pre-authorized merely by this document.

## 20. rc02 Review Questions

Independent review should determine whether:

1. the record model preserves the accepted rc01 semantic/authority boundary;
2. canonical field names and applicability tokens are deterministic enough for later serialization;
3. record identity and target/scope binding prevent ambiguous project assertions;
4. `disposition_basis` is sufficiently expressive without forcing artificial narrative prose;
5. `not_applicable` has a sufficiently controlled basis/provenance rule;
6. `undetermined` remains legitimate engineering state while still requiring explainable unresolved basis;
7. representation-invalid and engineering-unresolved conditions remain distinct;
8. Project Design Authority, verification, risk, deviation, evidence and closure authority are not absorbed into this record;
9. framework truth remains separate from project truth;
10. no L3 trace, automatic applicability, Pattern selection, compliance, closure, CI enforcement or L4 capability is silently introduced.

