# SCAF v0.0.9rc02 — Canonical Context Source Association Logical Model Foundation

**Development Release:** v0.0.9rc02  
**Status:** Canonical Context Source Association Logical Model Foundation / Review Candidate  
**Date:** 2026-08-19  
**Immediate Predecessor:** accepted v0.0.9rc01 (`9a71b25771793f1347b207beabb303a1b1abb201`)  
**Frozen Basis:** v0.0.2 L1/L2; v0.0.3 L3; v0.0.4 Executable Governance; v0.0.5 L3 Machine-Readable Traceability; v0.0.6 Project Application / Effective Project Profile; v0.0.7 Consumption Selection; v0.0.8 Lifecycle-Proportional Governance

## 1. Decision Purpose

The accepted rc01 semantic foundation established what Context Source Resolution means and preserved these separations:

```text
source relationship != source authority
source identity != exact source instance
discovery != controlled association
locator resolves != source is current / authoritative
source exists != obligation satisfied
source resolution != content loading / context inclusion
```

The rc01 independent review returned `PASS / GATE YES` with zero findings and no open blocking review-evidence limitation.

The post-review dependency/value assessment identified one material next-step ambiguity: a future machine-readable representation could encode materially different logical models unless the controlled source-association truth model is fixed before serialization.

The Current Decision Horizon for rc02 is therefore:

> **Define the canonical representation-neutral logical model for controlled Source Associations over one exact validated Consumption Selection, while keeping runtime resolution observations outside controlled association truth.**

rc02 does not define YAML/JSON, a schema, a resolver, content loading, ranking, token budgeting, or AI Context Assembly.

## 2. Why rc02 Is Required Now

Without a canonical logical model, two otherwise conforming implementations could reasonably choose incompatible structures such as:

```text
authority_id -> sources[]
```

versus:

```text
association =
  authority
  + relationship role
  + source identity
  + relationship scope
  + controlled basis/provenance
  + optional authority qualification
```

Those differences affect later validation, cardinality, provenance, duplicate handling, zero-association meaning, exact-source binding, and resolver behavior.

Applying frozen v0.0.8 proportional governance, this ambiguity is material before serialization because a premature representation would become an expensive downstream contract to change.

Therefore rc02 fixes the logical structure only.

## 3. Canonical Two-Plane Model

Context Source Resolution shall distinguish two logical planes:

```text
CONTROLLED ASSOCIATION TRUTH
        ↓
what source relationship has been deliberately recorded

RUNTIME RESOLUTION OBSERVATION
        ↓
what a resolver can observe about that source now
```

The governing invariant is:

> **Controlled association truth SHALL NOT be rewritten merely because a current resolver cannot resolve the source, finds the source missing, or observes that the source is stale/superseded.**

Accordingly:

```text
controlled association truth
!= runtime resolution observation
```

This separation prevents temporary repository/source conditions from silently changing engineering trace truth.

## 4. Canonical Controlled Association Aggregate

One canonical **Context Source Association Set** is bound to one exact validated Consumption Selection.

Conceptually:

```text
Context Source Association Set
│
├─ Upstream Selection Binding
│
├─ Source Unit Catalog
│    └─ 0..n Source Units
│
└─ Authority Source Entries
     └─ exactly one entry for every authority in validated I
          └─ 0..n Controlled Source Associations
```

The aggregate is representation-neutral. Names in this section identify logical responsibilities, not future serialized field names.

## 5. Upstream Selection Binding

The association set is subordinate to one exact Consumption Selection whose accepted source-aware validation has succeeded.

The logical binding shall identify the exact upstream selection instance strongly enough that a later validator can prove that the association set was constructed for the same selected authority domain.

The canonical logical dependency is:

```text
exact Consumption Selection bytes/instance
        ↓
accepted source-aware validation PASS
        ↓
validated included authority domain I
        ↓
Context Source Association Set
```

The association set shall not create a competing copy of upstream Project Application or Effective Project Profile truth.

It may retain the exact upstream selection identity/provenance needed for binding, while upstream applicability and rationale remain authoritative in their existing layers.

## 6. Coverage Domain and Zero-Association Meaning

The canonical association set covers exactly the validated included authority domain `I` of its bound Consumption Selection.

Every authority in `I` shall have exactly one logical **Authority Source Entry**, even when that entry currently has zero controlled Source Associations.

Therefore:

```text
missing Authority Source Entry
!= zero associations
```

and:

```text
zero controlled associations for authority A
= explicit state of the complete association-set model for A
```

This avoids treating serialization omission as controlled absence.

Authorities in `O` and `X` are outside the canonical rc02 association-set domain and retain their frozen Consumption Selection meanings.

## 7. Authority Source Entry

An **Authority Source Entry** is the canonical container for source relationships associated with one selected `scaf_authority_id`.

Its logical responsibilities are:

```text
selected scaf_authority_id
association collection: 0..n
```

The authority identity must be a member of the validated `I` domain from the exact bound Consumption Selection.

The entry does not duplicate upstream applicability state, Project Application rationale, verification state, or closure state.

## 8. Source Unit Catalog

A Source Unit Catalog contains the logical Source Units referenced by controlled associations in the aggregate.

A Source Unit is identified once and may be referenced by associations from one or many selected authorities.

The logical model therefore preserves:

```text
one selected authority -> 0..n Source Units
one Source Unit         -> 1..n selected authorities
```

The catalog avoids duplicating source identity/ownership metadata in every association.

A Source Unit may represent a file, fragment, record, controlled artifact, external constraint source, or other bounded engineering information unit. rc02 still does not choose locator syntax.

## 9. Source Identity

Each Source Unit has a logical **Source Identity**.

Source Identity answers:

> Which controlled engineering information unit is this relationship referring to?

It does not by itself answer:

```text
which exact bytes are currently present?
is the source current?
is the source authoritative for this relationship/property?
does the source satisfy the obligation?
```

The frozen rc01 distinction remains:

```text
source identity != exact source instance
```

A future representation may use repository-relative identity, artifact identity, URI-like identity, or another controlled locator model, but rc02 does not select that syntax.

## 10. Source Control Domain

Each Source Unit shall preserve which governance/control domain owns or controls the source identity.

The logical distinction shall remain capable of separating at least:

```text
framework-controlled source
project-controlled source
externally controlled source
```

This is ownership/control metadata only.

It does not mean:

```text
framework-controlled = project-authoritative
project-controlled   = verified
external-controlled  = automatically applicable
```

Recording an association never transfers source ownership between domains.

## 11. Controlled Source Association

A **Controlled Source Association** is the atomic logical statement that:

```text
one selected authority
        ↕
one defined relationship semantic
        ↕
one Source Unit
```

Each association has one relationship semantic at the canonical logical level.

If the same Source Unit has multiple materially different roles for the same selected authority, those roles are represented as separate logical associations rather than one ambiguous multi-role assertion.

This permits each role to carry its own scope, basis/provenance, and optional authority qualification.

## 12. Relationship Semantic

Relationship Semantic answers:

> Why is this Source Unit related to this selected authority?

Examples remain semantic categories such as:

```text
framework obligation/definition source
project decision / authoritative-artifact source
realization / implementation source
verification-definition source
verification-result / evidence source
external-constraint source
supporting engineering-context source
```

rc02 does not freeze machine-readable tokens for those categories.

The invariant remains:

```text
relationship semantic != authority status
```

## 13. Relationship Scope

A relationship may concern all or only part of the engineering concern represented by a selected authority.

The canonical association therefore has a logical **Relationship Scope** responsibility.

Relationship Scope identifies the bounded property, decision, behavior, interface portion, evidence purpose, or equivalent subject to which the association applies when such narrowing is necessary.

It shall not be interpreted as a new project scope hierarchy.

In particular:

```text
relationship scope
!= project_scope_ref hierarchy
!= wildcard project scope
!= parent/child scope propagation
```

The exact opaque upstream `project_scope_ref` remains unchanged.

## 14. Association Basis / Provenance

A controlled association shall retain the basis/provenance by which the relationship became controlled truth.

The logical model shall be capable of answering, as applicable:

```text
what controlled basis asserts this relationship?
which framework/project controlled artifact or decision owns the assertion?
how can a reviewer distinguish accepted mapping from raw discovery?
```

This provenance belongs to the relationship assertion, not to the source artifact's engineering authority.

Therefore:

```text
association provenance
!= source authority
!= engineering correctness
!= verification result
```

A tool-discovered candidate is not a Controlled Source Association until an applicable controlled rule or project authority accepts/establishes that relationship.

## 15. Discovery Candidate Boundary

Candidate discovery remains outside the canonical controlled association truth set.

Conceptually:

```text
search / trace / metadata / semantic discovery
        ↓
Candidate Source Relationship
        ↓
controlled acceptance / deterministic framework rule
        ↓
Controlled Source Association
```

rc02 does not define the candidate-record format or acceptance workflow.

The important invariant is:

```text
discovered candidate
!= controlled association
```

This prevents future search or AI tooling from silently writing project trace truth.

## 16. Authority Qualification Is Optional and Bounded

A relationship role does not automatically establish authority status.

Where a future consumer needs to know that a Source Unit is authoritative for a particular property/decision, the canonical logical model permits an optional **Authority Qualification** associated with the controlled relationship.

Authority Qualification must be grounded in existing authority ownership/basis and be bounded to the relevant property/decision scope.

It shall not be represented conceptually as an unqualified file-global boolean such as:

```text
authoritative: true
```

The required semantic is instead:

```text
existing authority basis
+ bounded property/decision scope
+ associated source relationship
```

Authority Qualification does not create new Project Design Authority, Verification Authority, risk-acceptance authority, or closure authority.

## 17. Exact Source Instance Constraint

A Source Identity may optionally have a controlled requirement that later resolution bind to a particular source instance or source snapshot.

This is an **Instance Constraint**, not the runtime observation itself.

Conceptually:

```text
controlled truth:
  source identity
  + optional expected/pinned instance constraint

runtime observation:
  actual resolved source instance
```

The exact future representation of a constraint may use a Git revision, digest, external pin, or another deterministic identity, but rc02 does not select a format.

## 18. Runtime Resolution Observation

A **Resolution Observation** is produced when a future resolver evaluates Source Units against a defined repository/source snapshot and resolver boundary.

It is not part of the controlled relationship assertion itself.

A Resolution Observation may establish machine-determinable facts such as:

```text
source identity resolved under this boundary
actual resolved source instance / exact bytes identity
source identity did not resolve deterministically
referenced source is absent in the evaluated source domain
resolved source is known stale/superseded under an applicable currentness rule
currentness is not established
instance constraint matches / does not match
```

rc02 defines these as logical outcome classes only. It does not define machine-readable status tokens.

## 19. Missing, Unresolvable and Stale Remain Distinct

The canonical logical model preserves the rc01 negative-condition distinction:

```text
missing
!= unresolvable
!= stale / superseded
```

For logical interpretation:

- **missing** means resolution reached the applicable source domain/snapshot and established that the referenced source unit/target is absent there;
- **unresolvable** means the resolver cannot deterministically complete resolution under the current resolver/source boundary, so existence/currentness may remain unknown;
- **stale/superseded** means a source resolved, but an applicable controlled currentness rule identifies it as no longer the current intended source/instance.

None of these observations automatically deletes the controlled association.

None automatically means:

```text
not applicable
waived
satisfied
verified
closed
```

Progression impact remains governed by frozen v0.0.8 Current Decision Horizon and applicable authority.

## 20. Currentness Is a Separate Evaluation

A source that resolves is not thereby current.

The logical model therefore preserves:

```text
resolvable
!= current
```

Currentness may depend on a controlled supersession rule, expected instance constraint, repository revision policy, external-source control, or another later-defined rule.

rc02 does not define a universal currentness algorithm.

## 21. Obligation Satisfaction Remains Upstream/Elsewhere

Neither controlled association truth nor runtime resolution observation determines obligation satisfaction.

The following remain invalid equivalences:

```text
associated source exists = obligation satisfied
implementation resolves  = implementation correct
test source resolves     = test executed
evidence resolves        = evidence sufficient
current authoritative source exists = closure
```

Satisfaction, verification sufficiency, compliance, risk acceptance, release readiness, and closure remain owned by their existing project/framework authorities.

## 22. Canonical Uniqueness and Duplicate Semantics

Within one Authority Source Entry, one semantic association shall not be duplicated merely because the same relationship was established by multiple controlled bases.

Conceptually, semantic association identity is determined by the combination of:

```text
selected authority
Source Unit
relationship semantic
relationship scope
optional Authority Qualification scope/basis
optional Instance Constraint
```

Multiple supporting assertion bases may be retained as provenance for that one semantic association rather than creating duplicate relationship truth.

A later representation may introduce an explicit `association_id`; rc02 does not prescribe its syntax.

## 23. Deterministic Ordering Is Representation-Level

The logical model is set/relationship oriented.

It requires deterministic semantic membership and uniqueness, but it does not yet prescribe serialized order for:

```text
Source Units
Authority Source Entries
Controlled Source Associations
provenance/basis references
```

A future canonical representation must define deterministic ordering if byte-stable output is required.

## 24. No New Applicability or Closure State

The association model adds no new applicability state and no new closure state.

The frozen upstream distinctions remain:

```text
applicable
not_applicable
undetermined
no_current_disposition
```

and:

```text
zero source associations
!= no_current_disposition
!= not_applicable
```

Similarly, runtime resolution outcomes do not become Project Application dispositions.

## 25. Exact Opaque Project Scope Preservation

The Context Source Association Set inherits the exact opaque `project_scope_ref` through its bound Consumption Selection provenance.

rc02 introduces no:

```text
scope hierarchy
scope alias
scope wildcard
path-derived scope
parent/child propagation
cross-scope inheritance
scope resolver
```

A future representation/resolver must preserve this boundary unless a separately reviewed scope capability is explicitly introduced.

## 26. Validation Ownership Direction

Although rc02 adds no validator, it establishes what a future source-aware validator would need to prove before accepting a machine-readable association set.

At minimum, future executable validation would need to establish:

```text
exact upstream Consumption Selection binding
upstream source-aware validation success
coverage exactly equals validated I
one Authority Source Entry per selected authority
all referenced Source Units exist in the association catalog
association semantic uniqueness
controlled provenance/basis presence according to future representation rules
no candidate-discovery record silently promoted as controlled truth
no runtime resolution observation substituted for controlled association truth
```

This list is an ownership direction, not authorization to implement the validator in rc02.

## 27. Context Assembly Boundary Remains Closed

The output of future Context Source Resolution remains a source relationship/resolution result, not an AI context package.

The downstream chain remains:

```text
validated Consumption Selection
        ↓
controlled Context Source Association Set
        ↓
future deterministic Resolution Observations
        ↓
future separately governed Context Assembly
```

rc02 does not define:

```text
content extraction
fragment loading
chunking
summarization
ranking / priority
semantic similarity inclusion
token budget
truncation
prompt structure
model selection
conversation injection
```

## 28. Representation / Executable Boundary

v0.0.9rc02 deliberately adds no:

```text
YAML / JSON source-association file
JSON Schema
validator
builder
generator
resolver
filesystem scanner
Git-history scanner
remote fetcher
content parser
context package
CI gate
authority-registry field
Project Application field
Effective Project Profile field
Consumption Selection field
```

The canonical logical model exists so those later decisions, if justified, are not forced to invent incompatible semantics.

## 29. Progression Sufficiency for rc02

rc02 is progression-sufficient when an independent reviewer can conclude that a future representation designer can answer consistently:

```text
What is the complete association-set domain?
How is zero association represented logically?
What is a Source Unit versus an exact source instance?
What is the atomic controlled relationship?
How are role, scope, provenance and authority qualification separated?
How is controlled truth separated from resolver observation?
How do missing, unresolvable and stale differ?
What remains upstream authority/applicability/closure truth?
What remains downstream Context Assembly?
```

Progression sufficiency does not require choosing serialization or resolver technology now.

## 30. Dependency / Value Gate After Review

A clean rc02 review shall authorize only a new dependency/value assessment.

The next question is expected to be:

> **Is a canonical machine-readable Context Source Association representation now required to enable a concrete next engineering action?**

Possible outcomes are:

```text
STOP / freeze logical model
or
CONTINUE to one separately justified representation RC
```

A clean rc02 review does not automatically authorize rc03.

## 31. Deliberately Deferred Scope

The following remain explicitly deferred:

```text
machine-readable source-association representation
schema
source-aware validator
deterministic resolver / builder
repository / filesystem / Git scanning
remote/external source retrieval
locator syntax
fragment syntax
content extraction / chunking
semantic search / embeddings
ranking / priority / severity automation
token-budget or truncation policy
AI Context Assembly / prompt packaging / orchestration
scope resolver / hierarchy / aliases / propagation
automatic authority inference
automatic applicability inference
verification/compliance/closure determination
CI source-mapping completion enforcement
L4 implementation/verification guidance expansion
Development Context Recovery / .scaf/work-checkpoint.yaml
external trust-model expansion
```

These are not rc02 defects.

## 32. rc02 Acceptance Boundary

The intended review gate is clean only if:

1. rc01 accepted semantics remain unchanged;
2. the aggregate binds to one exact validated Consumption Selection and exactly its `I` domain;
3. zero association is explicit and cannot be confused with omitted/incomplete data;
4. Source Identity remains separate from exact Source Instance;
5. controlled association truth remains separate from runtime resolution observation;
6. one semantic relationship is atomic enough to carry independent role/scope/basis;
7. discovery candidates cannot silently become controlled association truth;
8. property-specific authority is not collapsed into file-global authority;
9. missing, unresolvable and stale/superseded remain distinct;
10. source existence/resolution does not prove satisfaction, verification, compliance or closure;
11. exact opaque project scope and existing authority ownership remain unchanged;
12. no machine-readable/executable/Context Assembly capability is introduced;
13. frozen v0.0.8 and earlier protected surfaces remain unchanged.

If these conditions hold, rc02 is sufficient for the next dependency/value decision.
