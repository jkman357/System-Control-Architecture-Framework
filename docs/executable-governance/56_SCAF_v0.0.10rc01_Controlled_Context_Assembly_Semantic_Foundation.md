# SCAF v0.0.10rc01 — Controlled Context Assembly Semantic Foundation

**Development Release:** v0.0.10rc01  
**Status:** Controlled Context Assembly Semantic Foundation / Review Candidate  
**Date:** 2026-08-19  
**Immediate Predecessor:** formal frozen v0.0.9 (`cfa2839b8b7f5253c8ec8ea56068bf4229d45261`)  
**Frozen Basis:** v0.0.2 L1/L2; v0.0.3 L3; v0.0.4 Executable Governance; v0.0.5 L3 Machine-Readable Traceability; v0.0.6 Project Application / Effective Project Profile; v0.0.7 Consumption Selection; v0.0.8 Lifecycle-Proportional Governance; v0.0.9 Context Source Association / Source-Aware Validation

## 1. Decision Purpose

The frozen v0.0.9 baseline can deterministically establish a validated chain from one exact Consumption Selection through controlled Context Source Associations and source-aware consistency validation.

That chain can answer:

```text
which authorities are in validated I
which controlled Source Units are associated to those authorities
what relationship semantics those associations carry
whether the association representation is structurally valid
whether its deterministic repository/source bindings are source-consistent
```

It deliberately does **not** answer the downstream consumption question:

> **What controlled engineering context is presented to an engineer or AI for one bounded engineering objective, while preserving upstream authority, association and provenance truth?**

The Current Decision Horizon for v0.0.10rc01 is therefore limited to one semantic question:

> **What must Controlled Context Assembly mean before SCAF can responsibly define a machine-readable context package, deterministic builder, content materialization policy, or AI-facing consumer integration?**

The intended chain is:

```text
validated Consumption Selection
        ↓
validated Context Source Association set
        ↓
Controlled Context Assembly
        ↓
future Controlled Context Package
        ↓
engineer / AI consumer
```

v0.0.10rc01 establishes only the representation-neutral semantic boundary for Controlled Context Assembly.

It does **not** introduce a context-package serialization, schema, builder, content loader, chunker, ranking algorithm, token-budget policy, prompt format, model adapter, Source Resolver, CI gate or L4 implementation guidance.

## 2. Engineering Problem

Without an explicit Controlled Context Assembly boundary, future consumers could silently make materially different assumptions from the same validated upstream state, for example:

```text
source is associated
        = source content must be loaded

source content is omitted from one AI context
        = source is not applicable

context item is presented to an AI
        = AI gains engineering authority

context package appears complete
        = project / verification / compliance is complete

source summary is convenient
        = summary becomes authoritative source truth

an authority has zero source associations
        = authority may disappear from context

validated source association
        = source is current / latest / sufficient
```

Those equivalences are invalid.

v0.0.10rc01 therefore establishes semantic ownership before any context-package representation or executable assembly implementation is introduced.

## 3. Upstream Validated-Input Boundary

Controlled Context Assembly is downstream of the frozen v0.0.7 Consumption Selection and frozen v0.0.9 Context Source Association boundaries.

The governing input chain is:

```text
one exact Consumption Selection
        ↓
accepted source-aware Consumption Selection validation PASS
        ↓
one exact Context Source Association set bound to that selection
        ↓
accepted Context Source Association source-aware validation PASS
        ↓
Controlled Context Assembly reasoning
```

A future production assembler shall not treat an unvalidated or source-inconsistent Context Source Association artifact as controlled input.

The selected authority domain remains the validated included set `I` from Consumption Selection.

Controlled Context Assembly does not recalculate applicability and does not create a replacement authority-selection domain.

Accordingly:

```text
assembly input authority domain = validated I

assembly
!= Project Application
!= Effective Project Profile generation
!= Consumption Selection
!= Context Source Association validation
```

If a future use case requires a second authority-level sub-selection after `I`, that would require a separately justified semantic boundary. v0.0.10rc01 does not create one implicitly.

## 4. Controlled Context Assembly

**Controlled Context Assembly** is the governed construction of a bounded engineering-context view from validated upstream authority and source-association truth for one explicit engineering objective, while preserving the ownership and provenance of the underlying engineering sources.

Conceptually:

```text
validated authority domain I
        +
validated controlled source associations
        +
explicit bounded assembly objective
        ↓
Controlled Context Assembly
        ↓
bounded consumer-facing engineering context
```

Controlled Context Assembly is a downstream consumption operation.

It does not rewrite upstream truth.

Therefore:

```text
assembly result
!= new authority truth
!= new applicability truth
!= new source-association truth
!= engineering approval
!= verification result
!= closure decision
```

## 5. Assembly Objective

A **Context Assembly Objective** is the bounded engineering purpose for which context is being assembled.

Examples may include:

- reviewing one interface contract;
- implementing one selected mechanism;
- investigating one runtime behavior;
- preparing one bounded verification activity;
- continuing one engineering task with another human or AI consumer.

The objective answers:

```text
what engineering subject is being supported?
what work is the consumer expected to perform?
what current decision horizon is relevant?
```

The objective is a consumption boundary only.

It does not confer Project Design Authority, Verification / Assurance Authority, release authority or closure authority.

The objective may influence which source content is materialized in a future package, but it shall not silently change:

```text
validated I
controlled source associations
source control domain
relationship semantics
authority qualification
applicability state
```

v0.0.10rc01 does not define a canonical objective serialization or controlled vocabulary.

## 6. Authority-Presence Invariant

The validated included authority domain `I` remains upstream controlled truth.

A future Controlled Context Package shall not silently erase an authority from that domain merely because:

```text
it has zero source associations
its associated source content is not materialized
its source content is unavailable to a particular consumer
its source is external
its source is large
its source is inconvenient to load
```

The semantic requirement is:

> **Every authority in the validated input domain `I` remains represented in the controlled context authority envelope, even when zero source content is materialized for that authority.**

This preserves the frozen v0.0.9 distinction:

```text
missing Authority Source Entry
!= explicit Authority Source Entry with zero associations
```

and extends the downstream consumption rule:

```text
zero materialized source content
!= authority omitted from validated I
```

This requirement is representation-neutral. v0.0.10rc01 does not define the future field shape used to represent the authority envelope.

## 7. Source Association Is Not Context Materialization

A controlled Source Association records that a Source Unit has a defined relationship to one selected authority.

It does not require that the Source Unit's bytes or human-readable content be inserted into every consumer context.

The governing distinction is:

```text
source association
!= context materialization
```

Accordingly:

```text
associated source
!= automatically loaded source

associated source
!= automatically quoted source

associated source
!= automatically summarized source
```

A future assembler may materialize none, some or all associated source content according to separately controlled assembly inputs/policy, while preserving the underlying association truth.

The association itself shall not disappear merely because its content is not materialized for one consumer package.

## 8. Context Materialization

**Context Materialization** is the downstream act of making bounded source-derived information available inside a particular consumer-facing context package.

Materialization may eventually take forms such as:

```text
source reference only
exact source bytes
bounded source fragment
structured source extract
controlled derived summary
other explicitly governed representation
```

These are possible future forms only. v0.0.10rc01 does not authorize or define any concrete materialization format.

The central semantic rule is:

```text
materialized context item
!= Source Unit identity itself
!= Source Association truth itself
!= source authority itself
```

Materialization is a consumption representation of controlled engineering information.

## 9. Context Inclusion Is Not Applicability

The frozen v0.0.7 rule remains:

```text
included in Consumption Selection != applicable
```

Controlled Context Assembly adds another distinct consumption layer:

```text
materialized in a context package
!= applicable
```

Likewise:

```text
not materialized
!= not_applicable
!= undetermined
!= no_current_disposition
```

Project applicability remains owned by Project Application / Effective Project Profile semantics.

Context assembly shall not infer or rewrite applicability from whether a source or context item is included for one task.

## 10. Context Omission

A **Context Omission** is the bounded non-materialization of otherwise available associated source content from one particular assembled context.

Context omission is scoped to the assembly objective/package and applies downstream to source-derived material for authorities already in validated `I`. It is not the frozen v0.0.7 bounded-omitted authority set `O`.

```text
context omission != v0.0.7 bounded omission O
```

It is not a framework/project engineering disposition.

Therefore:

```text
context omitted
!= source association removed
!= authority removed from I
!= not applicable
!= source invalid
!= source absent
!= obligation satisfied
!= waived
!= accepted risk
!= closed
```

A later executable representation may need explicit omission basis/provenance so two deterministic builders can reproduce the same package. v0.0.10rc01 establishes the semantic need but does not define a machine-readable omission model.

## 11. Association Envelope vs Materialized Content

A future Controlled Context Package conceptually contains two different information planes:

```text
Controlled Context Package
│
├─ controlled authority / association envelope
│    ├─ validated authority domain I
│    └─ validated controlled Source Associations
│
└─ materialized consumer context
     └─ 0..n source-derived context items
```

The first plane preserves controlled upstream relationship truth.

The second plane is the bounded content actually made available to the consumer.

The governing distinction is:

```text
association-envelope presence
!= materialized-content presence
```

This separation prevents a token budget, content limit, model adapter or task-specific omission from silently rewriting controlled engineering relationships.

v0.0.10rc01 does not define whether a future serialization uses one file, multiple files, a manifest plus payloads, or another packaging structure.

## 12. Controlled Context Package

A **Controlled Context Package** is the future bounded output of Controlled Context Assembly.

Semantically, such a package must be capable of preserving enough information to determine, as applicable:

```text
which validated upstream selection/association state it was assembled from
which authority domain it represents
which controlled associations remain in its envelope
which source-derived items were materialized
which material was deliberately not materialized where omission is controlled
what bounded assembly objective the package serves
how materialized items trace back to controlled Source Units/associations
```

The package is a consumer artifact.

It is not an authoritative replacement for the underlying sources.

Therefore:

```text
Controlled Context Package
!= SCAF Concern Authority
!= Project Design Authority
!= Project Realization
!= Project Verification / Assurance Authority
!= external authority source
!= release / closure record
```

## 13. Source Truth vs Derived Context

A future context package may need to carry derived forms such as extracts or summaries for bounded consumption.

Any derived form must preserve the distinction:

```text
derived context representation
!= underlying source truth
```

A summary or extract may assist a consumer but shall not silently become the authoritative source solely because it appears in a controlled package.

Where a materialized item is transformed from a Source Unit, a future representation must retain sufficient provenance to trace the transformation back to its controlled source basis.

v0.0.10rc01 does not define summarization algorithms, model-generated transformation, extract syntax or fidelity metrics.

## 14. Provenance Preservation

Context Assembly shall preserve provenance across the downstream consumption boundary.

At minimum, future executable designs must be able to preserve the relationship between:

```text
materialized context item
        ↓
controlled Source Association
        ↓
Source Unit identity
        ↓
applicable exact-instance constraint / validated source binding where present
```

This does not require every package to duplicate every upstream field verbatim.

It requires that a consumer or validator can trace materialized context back to the controlled upstream basis without inventing a new source of truth.

Provenance preservation does not confer authority.

## 15. Exact Source Instance and Currentness Boundary

The frozen v0.0.9 distinction remains:

```text
Source Identity
!= expected / pinned Instance Constraint
!= actual runtime-resolved Source Instance
```

Controlled Context Assembly does not create a general Source Resolver and does not infer source currentness.

Therefore:

```text
assembled from a validated association
!= proof that a source is latest
!= proof that a source is current
!= proof that a source has not been superseded
```

Where an accepted upstream Instance Constraint already proves exact repository-local bytes, a future assembler may consume that validated fact.

Where currentness/resolution semantics do not exist upstream, the assembler shall not manufacture them.

## 16. Content-Availability Observation Is Not Association Truth

A future assembler may encounter a runtime situation where content cannot be loaded or materialized.

That runtime observation shall not rewrite the controlled association itself.

The accepted two-plane invariant therefore remains applicable downstream:

```text
controlled association truth
!= runtime resolution / materialization observation
```

Examples of future runtime observations may include:

```text
content unavailable
content load failed
fragment not found
materialization exceeded a configured bound
```

v0.0.10rc01 does not define a runtime observation schema or status vocabulary.

It only prohibits such observations from silently mutating applicability or controlled association truth.

## 17. Context Completeness Is Bounded

A Controlled Context Package may eventually be assessed as complete relative to its declared assembly objective and controlled assembly rules.

That bounded notion must remain separate from broader engineering completeness.

The governing distinction is:

```text
context-package completeness
!= project completeness
!= requirements completeness
!= source completeness
!= implementation completeness
!= verification completeness
!= compliance
!= release readiness
!= closure
```

A context package can be sufficient for one implementation/review task while the project remains intentionally incomplete.

Conversely, a package can be incomplete for its stated objective even when the underlying project sources are valid.

v0.0.10rc01 does not create canonical `complete/incomplete` machine tokens.

## 18. Context Sufficiency and Engineering Judgment

Whether a particular package is useful or sufficient for a complex engineering task may require engineering judgment.

SCAF shall not collapse that judgment into deterministic context-assembly facts.

The distinction is:

```text
machine-determinable assembly conformance
!= engineering-context sufficiency judgment
```

Examples of machine-determinable facts may later include:

```text
exact upstream binding
required authority-envelope coverage
traceability of materialized items
bounded omission representation
byte/fragment identity where explicitly defined
```

Examples that may require engineering judgment include:

```text
whether the selected supporting material is enough to make a design decision
whether a summary preserves the engineering nuance needed for the task
whether another source should be consulted before committing an architecture decision
```

A future validator shall not represent mechanical package conformance as proof of engineering sufficiency.

## 19. Consumer-Neutral Semantics

Controlled Context Assembly is consumer-neutral at this semantic layer.

A consumer may be:

```text
human engineer
reviewer
coding agent
analysis model
other engineering tool
```

Presentation to a consumer does not change authority ownership.

In particular:

```text
context presented to AI
!= authority granted to AI

AI received authoritative source
!= AI becomes Project Design Authority
```

Project Design Authority, Verification / Assurance Authority and applicable external authority remain where the frozen Authority Kernel and project governance place them.

## 20. Model / Prompt Separation

v0.0.10rc01 does not define prompts, chat messages, model-specific system instructions, agent roles or orchestration.

The semantic chain is intentionally:

```text
controlled engineering context
        ↓
future consumer adapter
        ↓
AI / human interaction
```

not:

```text
Controlled Context Package
= prompt
```

Therefore:

```text
context package
!= prompt template
!= model configuration
!= conversation state
!= agent persona
```

Model-specific optimization may be useful later, but it is a downstream consumer concern and requires a separate dependency/value decision.

## 21. Token Budget and Ranking Are Deferred Policies

A future consumer may have bounded context capacity.

That does not authorize v0.0.10rc01 to invent ranking or token-budget semantics prematurely.

The current rule is only:

```text
capacity-driven materialization decision
shall not rewrite upstream authority / applicability / association truth
```

Future policies may need to define deterministic or explicit criteria for:

```text
priority
bounded omission
content granularity
ordering
capacity budget
consumer capability
```

Those are separately gated executable-policy questions.

No ranking/priority/token-budget algorithm is introduced here.

## 22. No Implicit Relevance Inference

A future assembler shall not treat incidental textual similarity, file co-location, search ranking or model preference as a controlled Source Association.

The frozen v0.0.9 rule remains:

```text
discovered candidate
!= controlled association
```

Controlled Context Assembly consumes accepted controlled relationships.

If future assembly uses discovery to suggest additional candidate material, that suggestion remains outside controlled association truth until separately governed and accepted.

v0.0.10rc01 does not introduce candidate discovery.

## 23. External Source and Content-Use Boundary

A controlled association to an external Source Unit records an engineering relationship.

It does not by itself grant permission to copy, redistribute, transform or embed external content into a context package.

Therefore:

```text
external source association
!= content-use authorization
!= redistribution permission
!= license grant
```

A future content materializer must respect applicable license, copyright, confidentiality, data-handling and other source-use constraints independently of the engineering association semantics.

This is a framework boundary statement, not a legal conclusion about any specific source.

## 24. Security / Privacy / Sensitive-Content Boundary

Controlled Context Assembly may eventually handle project-controlled or externally controlled information.

A valid engineering association does not imply that every consumer is authorized to receive the source content.

Accordingly:

```text
source is relevant
!= consumer is authorized to receive source content
```

Future implementations may require project-specific access, confidentiality, privacy, export, regulatory or other information-handling constraints.

v0.0.10rc01 does not define an access-control system, secret manager, credential mechanism or data-classification model.

It only preserves the requirement that content materialization not silently override applicable information-handling authority.

## 25. Determinism Target

A future executable Controlled Context Assembly capability should be deterministic for every machine-determinable input under its declared policy.

The target is:

```text
same validated upstream inputs
+ same explicit assembly objective
+ same explicit deterministic assembly inputs/policy
        ↓
same controlled package semantics
```

This does not mean SCAF must automate every engineering-context choice.

Where a choice requires engineering judgment, the judgment should be explicit controlled input/provenance rather than hidden inference inside the assembler.

The semantic rule is:

```text
machine-readable != machine-decided
```

## 26. Invalid vs Unresolved

The frozen distinction remains:

```text
Invalid
= machine-verifiable representation/source inconsistency

Unresolved
= legitimate engineering question not yet decided
```

Controlled Context Assembly shall not treat legitimate unresolved engineering content as invalid merely because the engineering answer is not yet known.

Likewise, a machine-verifiable assembly-contract violation shall not be reclassified as a legitimate engineering uncertainty merely to allow progression.

A future executable layer must keep those categories separate.

## 27. Interaction With Lifecycle-Proportional Governance

The frozen v0.0.8 Current Decision Horizon applies directly to context assembly.

A package should contain the controlled context needed for the current bounded engineering objective, not theoretical maximum repository content.

Therefore:

```text
right context for current decision horizon
!= all available project information
```

The Materiality Stop Rule also applies to future assembly rules. SCAF should not add ranking, chunking, model-specific adaptation or resolver capabilities unless omission of those capabilities creates a material current ambiguity, inconsistent implementation, blocked consumer capability or difficult-to-reverse commitment.

## 28. Relationship to L4

v0.0.10rc01 does not introduce L4 implementation guidance.

Future L4 material may itself become controlled Source Units or materialized context when independently justified and governed.

The dependency direction remains:

```text
L4 content, if/when created
        ↓
controlled source relationship
        ↓
Controlled Context Assembly
```

Controlled Context Assembly does not create implementation guidance simply by assembling existing sources.

## 29. Representation-Neutral Logical Shape

At this semantic stage, a future Controlled Context Package can be reasoned about conceptually as:

```text
Controlled Context Package
│
├─ upstream provenance / validated-input binding
│
├─ assembly objective
│
├─ authority envelope
│    └─ every authority in validated I
│         └─ validated controlled Source Associations
│
└─ materialized context items
     └─ each traceable to controlled source basis
```

This is a logical explanation only.

It does not freeze:

- field names;
- YAML/JSON shape;
- identifiers;
- schema vocabulary;
- content payload format;
- fragment syntax;
- ordering rules;
- omission tokens;
- completion tokens;
- builder API.

Those require later dependency/value decisions.

## 30. Invariants Established by rc01

v0.0.10rc01 establishes the following semantic invariants:

### CCA-01 — Validated Upstream Ownership

```text
Controlled Context Assembly
consumes validated upstream selection + association truth
and does not independently recreate those truths
```

### CCA-02 — Authority-Presence Preservation

```text
every authority in validated I
remains represented in the controlled context authority envelope
```

### CCA-03 — Association / Materialization Separation

```text
source association
!= context materialization
```

### CCA-04 — Inclusion / Applicability Separation

```text
context materialized
!= applicable
context omitted
!= not_applicable
```

### CCA-05 — Omission / Relationship Separation

```text
context omission
!= source association removal
```

### CCA-06 — Package / Authority Separation

```text
Controlled Context Package
!= engineering authority
```

### CCA-07 — Derived Context / Source Truth Separation

```text
derived context representation
!= authoritative source truth
```

### CCA-08 — Bounded Completeness

```text
context-package completeness
!= project / verification / compliance / release / closure completeness
```

### CCA-09 — Consumer / Authority Separation

```text
context presented to AI or human
!= authority granted to that consumer
```

### CCA-10 — Association / Runtime Observation Separation

```text
controlled association truth
!= runtime resolution / materialization observation
```

### CCA-11 — Consumer-Neutral Context

```text
Controlled Context Package
!= prompt / model / conversation / agent persona
```

### CCA-12 — Machine-Readable / Machine-Decided Separation

```text
machine-readable context policy
!= machine-owned engineering judgment
```

### CCA-13 — Association / Content-Use Authorization Separation

```text
source association
!= permission to copy / expose / redistribute source content
```

## 31. Deliberately Deferred Capability

v0.0.10rc01 does **not** introduce:

```text
context-package YAML / JSON
context-package schema
context-package validator
context builder / generator
source-content loader
fragment locator
chunking
summarization
semantic extraction
ranking / priority
context budget / token budget
model tokenizer dependency
prompt construction
model-specific adapter
conversation orchestration
agent role/persona framework
automatic source discovery
general Source Resolver
Git history traversal
currentness / supersession model
runtime materialization-observation schema
CI context gate
new authority-registry record
new PAO / FNI
L4 implementation guidance
```

These remain separately gated.

## 32. Authority Boundary

v0.0.10rc01 adds no new SCAF Concern Authority, PAO, FNI, Project Design Authority, Verification / Assurance Authority, risk-acceptance authority, release authority or closure authority.

It changes no frozen authority record.

The existing authority chain remains:

```text
SCAF Concern Authority
        ↓
Project Design Authority
        ↓
Project Realization
        ↓
Project Verification / Assurance Authority
```

Controlled Context Assembly is a governed consumption mechanism around those authorities; it does not sit above or replace them.

## 33. Dependency / Value Gate After rc01

A clean rc01 review shall not automatically authorize rc02.

After review, SCAF shall reassess what executable ambiguity remains.

Potential next questions may include:

```text
Is a canonical representation-neutral Context Package logical model now required?
Is an explicit context-materialization decision model required?
Is the authority envelope / materialized-content split sufficient as currently defined?
Is a machine-readable representation needed before any builder can be responsibly written?
```

The frozen v0.0.8 rule still applies:

> **No next RC exists merely because another refinement is imaginable.**

If no material ambiguity or executable dependency remains at the next Current Decision Horizon, SCAF shall stop rather than extend the RC line for theoretical completeness.

## 34. Progression Criteria

v0.0.10rc01 is progression-sufficient only if independent review confirms that:

1. the semantic boundary is downstream of validated Consumption Selection and Context Source Association truth;
2. `I` authority presence is preserved without creating a second implicit applicability/authority filter;
3. Source Association is clearly separate from content materialization;
4. context inclusion/omission cannot silently rewrite applicability or source-association truth;
5. the authority/association envelope is semantically distinct from materialized consumer content;
6. derived extracts/summaries cannot silently become authoritative source truth;
7. provenance requirements are sufficient to support future traceable materialization without prematurely fixing serialization;
8. context completeness remains bounded to one assembly objective and does not imply engineering/verification/closure completeness;
9. consumer presentation does not transfer engineering authority;
10. currentness/runtime materialization observations remain separate from controlled association truth;
11. external source association does not imply content-use authorization;
12. deterministic future assembly is separated from engineering judgment;
13. no context package representation, schema, builder, loader, ranking/token budget, prompt/model integration, general resolver, CI gate, authority expansion or L4 capability is introduced;
14. frozen v0.0.2–v0.0.9 authority and executable surfaces remain unchanged;
15. the result supports only the next dependency/value assessment, not automatic rc02 progression.

## 35. Review Posture

Review should focus on specification conformance and bounded semantic consistency.

The reviewer should identify:

- contradictions with frozen upstream semantics;
- authority transfer or applicability inference accidentally introduced by context language;
- ambiguity between controlled association truth and materialized content;
- ambiguity between context omission and engineering disposition;
- ambiguity between context-package completeness and engineering completion;
- provenance gaps that would permit transformed context to become an untraceable source of truth;
- premature representation/executable commitments;
- deferred capability that has been implicitly introduced despite the stated boundary.

Review should not require implementation, token-budget experiments, model benchmarks, source-loader evidence or L4 realization evidence that v0.0.10rc01 intentionally does not and cannot yet produce.

## 36. Summary

v0.0.10rc01 establishes the representation-neutral semantic boundary for Controlled Context Assembly.

The governing chain is:

```text
validated Consumption Selection
        ↓
validated Context Source Associations
        ↓
controlled authority / association envelope
        ↓
bounded context materialization
        ↓
future Controlled Context Package
        ↓
engineer / AI consumer
```

The central separation is:

```text
validated engineering truth
!= materialized consumer context
```

while preserving:

```text
source association != context materialization
context inclusion != applicability
context omission != not_applicable / waiver / closure
context package != engineering authority
context completeness != engineering completion
context presented to AI != authority granted to AI
controlled association truth != runtime materialization observation
machine-readable != machine-decided
```

No machine-readable Context Package or executable Context Assembly capability is introduced by this RC.
