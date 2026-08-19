# SCAF v0.0.9rc01 — Context Source Resolution Semantic Foundation

**Development Release:** v0.0.9rc01  
**Status:** Context Source Resolution Semantic Foundation / Review Candidate  
**Date:** 2026-08-19  
**Immediate Predecessor:** formal frozen v0.0.8 (`a18ed338d1f8c8b839e994fc4098ae3e98c6ac5f`)  
**Frozen Basis:** v0.0.2 L1/L2; v0.0.3 L3; v0.0.4 Executable Governance; v0.0.5 L3 Machine-Readable Traceability; v0.0.6 Project Application / Effective Project Profile; v0.0.7 Consumption Selection; v0.0.8 Lifecycle-Proportional Governance

## 1. Decision Purpose

The frozen v0.0.7 Consumption Selection baseline can deterministically answer which Project-Applicable Obligations are included in one validated selection. It deliberately does not answer where project/framework source material related to those selected authorities is located.

The frozen v0.0.8 baseline further requires SCAF to add only the governance depth needed for the next engineering action.

The Current Decision Horizon for v0.0.9rc01 is therefore limited to one question:

> **What must “source relationship” and “source resolution” mean before SCAF can responsibly define any machine-readable PAO-to-source model or resolver?**

The practical chain is:

```text
validated Consumption Selection
        ↓
included authority domain I
        ↓
controlled source associations
        ↓
future deterministic source resolution
```

v0.0.9rc01 establishes only the representation-neutral semantic boundary between the selected authority domain and source associations.

It does **not** load source content and does **not** decide what content enters an AI context.

## 2. Engineering Problem

Without an explicit source-resolution semantic boundary, future tools could silently make incompatible assumptions such as:

```text
file mentions authority ID
        = authoritative source

file exists
        = current source

source is related
        = source proves satisfaction

source was discovered
        = source must be loaded into AI context

no mapped source
        = obligation is not applicable
```

Those equivalences are invalid.

Different tools could otherwise produce materially different context reconstruction from the same validated Consumption Selection even while each tool appears internally deterministic.

The rc01 objective is to prevent that semantic divergence before representation or executable implementation begins.

## 3. Upstream Validation Boundary

Context Source Resolution is downstream of the frozen v0.0.7 Consumption Selection boundary.

The governing input model is:

```text
one exact Consumption Selection
        ↓
accepted source-aware Consumption Selection validation
        ↓
validated selected-entry domain I
        ↓
source-association reasoning
```

A future production resolver shall not consume selected authority state before the accepted Consumption Selection validation boundary has succeeded for the exact selection bytes it is using.

The rc01 semantic target is the **included authority domain `I`** from one validated Consumption Selection.

The frozen v0.0.7 meanings remain unchanged:

```text
D = complete validated source-profile domain
E = predicate-eligible set
I = included set
O = eligible bounded-omitted set
X = predicate-excluded set

E = I + O
D = I + O + X
```

For this rc01 target:

```text
source-resolution authority domain = I
```

This does not redefine `O` or `X`.

In particular:

```text
O != source does not exist
O != source is irrelevant
X != source does not exist
X != source is not authoritative
```

A future diagnostic or broader discovery mode over `O`/`X` would require a separately justified boundary. It is not created here.

## 4. Context Source Resolution Is Not Context Inclusion

The word **Context** in Context Source Resolution identifies the downstream purpose: locating controlled sources that may later support engineering-context reconstruction.

It does not mean that resolved source content is automatically inserted into an AI prompt or working context.

The governing distinction is:

```text
source association
!= content inclusion

source resolution
!= content loading

content loading
!= context selection

context selection
!= engineering applicability
```

Therefore a source resolver may identify multiple relevant sources while a later context-assembly stage legitimately chooses none, some, or all of them according to a separately governed policy.

No such policy is defined by rc01.

## 5. Source Unit

A **Source Unit** is a controlled engineering information unit that can be meaningfully referenced as a source for one or more selected SCAF authorities.

Examples may include:

- a SCAF normative authority document;
- a project architecture specification;
- an interface/protocol specification;
- a controlled decision record;
- source code or configuration source;
- a test definition;
- a verification result;
- retained engineering evidence;
- an applicable externally controlled constraint source;
- another controlled project artifact.

A Source Unit is a semantic concept, not a file-only concept.

Accordingly:

```text
source unit
!= necessarily one filesystem file
!= necessarily Markdown
!= necessarily source code
```

A later representation may support files, fragments, records or other bounded units, but rc01 does not choose locator syntax or serialization.

## 6. Source Identity and Source Instance

SCAF shall distinguish a source's logical identity from the exact source instance consumed at a particular revision or snapshot.

```text
source identity
!= source instance / exact bytes
```

A repository-relative path can identify a logical source while the bytes at that path change over time.

For reproducible future resolution, an executable resolver may need to bind to a repository/source snapshot or exact content identity. rc01 establishes that semantic need but does not prescribe:

- Git commit fields;
- content hashes;
- fragment syntax;
- URI syntax;
- repository identifiers;
- cross-repository pinning format.

Those are representation/executable decisions for a later dependency/value gate.

## 7. Source Association

A **Source Association** is a controlled statement that one Source Unit has a defined relationship to one selected `scaf_authority_id` in the validated `I` domain.

Conceptually:

```text
selected scaf_authority_id
        ↕
source relationship
        ↕
Source Unit
```

A Source Association is a trace/relationship construct.

It does not create a new engineering authority merely because it records a relationship.

Therefore:

```text
source association
!= SCAF Concern Authority
!= Project Design Authority
!= Project Realization
!= Project Verification / Assurance Authority
!= risk acceptance authority
!= closure authority
```

Existing authority ownership remains defined by the frozen Authority Kernel and applicable project/external governance.

## 8. Relationship Role Is Separate From Authority Status

A source can be related to an obligation in materially different ways.

Semantic relationship roles may include, for example:

- framework definition / obligation source;
- project decision / authoritative-artifact source;
- realization / implementation source;
- verification-definition source;
- verification-result or evidence source;
- external-constraint source;
- supporting engineering-context source.

These are semantic role classes for rc01 reasoning. They are **not** a frozen machine-readable enum.

A later representation must preserve the distinction between why a source is related and whether that source is authoritative for a particular project decision/property.

The governing rule is:

```text
relationship role
!= authority status
```

For example:

```text
implementation source
!= Project Design Authority

evidence source
!= verification-sufficiency decision

supporting context source
!= authoritative artifact
```

A single Source Unit may legitimately have more than one relationship role.

## 9. Authority Is Property-Specific, Not File-Global

A source shall not be treated as universally authoritative merely because it is authoritative for one decision or property.

For example, one interface specification may authoritatively record a wire-format decision while containing an informative timing note that is not the authoritative timing decision.

Therefore:

```text
source is authoritative for property A
!= source is authoritative for every statement it contains
```

A future source-association model shall preserve authority scope sufficiently to avoid file-global authority promotion.

rc01 does not define the future field structure for that scope.

## 10. Framework, Project and External Source Ownership

Source ownership and source relationship are separate concerns.

A selected SCAF authority may relate to:

```text
framework-owned source
project-owned source
externally controlled source
```

Framework-owned source remains framework authority/guidance according to its existing SCAF role.

Project-owned source remains under project authority/governance.

Externally controlled source remains external authority/input and does not become SCAF-owned merely because SCAF records or resolves a reference to it.

The existence of a Source Association does not transfer ownership between these domains.

Repository-external trust expansion, external acquisition, signature validation, remote fetching and external pinning changes are outside rc01.

## 11. Discovery Is Not Controlled Association

Future tools may discover candidate relationships through mechanisms such as exact IDs, links, filenames, metadata, traces or content search.

Discovery is useful, but discovery alone shall not silently create authoritative project truth.

The governing distinction is:

```text
discovered candidate relationship
!= controlled source association
```

Similarly:

```text
semantic similarity
!= authority

text mention
!= source relationship proof
```

A future resolver may support deterministic framework-owned mappings, explicitly project-declared mappings, or candidate discovery, but the provenance of the association must remain distinguishable.

rc01 does not define a canonical provenance vocabulary or acceptance workflow.

## 12. Association Provenance

The source relationship itself has provenance independent of the source artifact's own authority.

A future controlled representation should be able to answer, as applicable:

```text
Who/what asserted this association?
Was it framework-owned, project-declared or tool-discovered?
What controlled basis allows the association to be relied upon?
```

Association provenance does not replace source authority.

Therefore:

```text
association provenance
!= source authority
!= engineering correctness
!= verification result
```

The exact representation of association provenance is deferred.

## 13. Resolvability, Currentness and Authority Are Orthogonal

A future tool may be able to deterministically resolve a locator to bytes. That is a machine-determinable fact.

It does not automatically establish that the resolved source is the current authoritative engineering artifact.

The governing distinctions are:

```text
locator resolves
!= source is current

source is current
!= source is authoritative

source is authoritative
!= source proves satisfaction
```

Likewise, a source may be stale/superseded yet still resolvable for historical trace.

A source may be authoritative in principle yet temporarily unresolvable because a repository/input is unavailable.

These conditions shall not be collapsed into one generic “valid source” status.

rc01 intentionally does not create canonical current/stale/missing status tokens.

## 14. Absence and Unresolved Mapping Semantics

A selected authority may currently have zero controlled Source Associations.

That condition shall not automatically mean:

```text
not applicable
satisfied
unsatisfied
waived
closed
no source exists anywhere
```

It may simply mean that source mapping has not yet been established for the Current Decision Horizon.

Similarly:

```text
no association recorded
!= source absent

locator unresolved
!= source never existed

stale source
!= missing source

missing source
!= obligation failure
```

Whether missing or unresolved source mapping blocks progression is governed by the frozen v0.0.8 Current Decision Horizon / Materiality Stop Rule and applicable external/project authority.

## 15. Cardinality

The semantic model permits:

```text
one selected authority -> zero, one or many Source Units
one Source Unit         -> one or many selected authorities
```

Multiple Source Associations do not imply ranking, priority or evidence weight.

One shared source related to many authorities does not require duplicated source content in a future AI context.

Content de-duplication and context assembly remain downstream concerns.

## 16. Source Existence Is Not Satisfaction

The presence of a related source is evidence only of a source relationship/existence fact within its proven boundary.

It does not prove the engineering obligation is satisfied.

Examples:

```text
architecture document exists
!= architecture decision is correct

implementation source exists
!= implementation satisfies obligation

test exists
!= test executed

test passed
!= evidence is sufficient for all applicable claims

evidence exists
!= closure granted
```

The frozen Authority Kernel / Applicable Satisfaction Basis / Verification / closure separations remain unchanged.

## 17. Framework Source Is Not Project Applicability

A selected authority will normally have a framework-owned definition source in SCAF.

That source relationship does not create or re-evaluate project applicability.

Project applicability remains upstream in Project Application / Effective Project Profile.

Therefore:

```text
framework definition source exists
!= project applicability

project source exists
!= applicability inference
```

Context Source Resolution shall remain downstream of validated project applicability/selection state rather than silently inferring it from artifact presence.

## 18. Project Scope Preservation

The validated Consumption Selection source binding includes the exact opaque `project_scope_ref` inherited from its Effective Project Profile.

Context Source Resolution shall preserve that upstream scope identity as context provenance.

rc01 introduces no:

- scope hierarchy;
- scope alias;
- parent/child propagation;
- wildcard scope matching;
- cross-scope inheritance;
- scope resolver;
- inference that a source belongs to a scope merely because of its path.

A future cross-scope source relation requires explicit semantics and a separate gate.

## 19. Content Semantics Are Deferred

Context Source Resolution identifies source relationships and future resolvable source units.

It does not define how source bytes are interpreted.

rc01 therefore does not define:

- text extraction;
- Markdown section parsing;
- code symbol extraction;
- PDF parsing;
- chunking;
- embeddings;
- semantic similarity;
- summarization;
- source-content normalization.

Those are materially different content-processing decisions.

## 20. Context Assembly Is Deferred

A future Context Assembly stage may decide what material actually enters an AI/engineering working context.

That stage may need policies for:

- purpose-specific inclusion;
- ordering;
- de-duplication;
- content windows/fragments;
- token/size budgets;
- truncation;
- priority;
- freshness policy;
- summarization.

None of those policies is authorized by rc01.

The governing boundary is:

```text
Context Source Resolution
        ↓
identifies source relationships / resolvable units

Context Assembly
        ↓
separately decides content inclusion and packaging
```

## 21. Machine-Determinable Facts vs Engineering Judgment

The frozen authority separation remains applicable.

Potential machine-determinable facts include, in a future executable boundary:

- selection validation result;
- exact selected authority membership;
- whether a locator resolves within a bound snapshot;
- exact source bytes/hash where applicable;
- explicit association membership;
- deterministic ordering.

Those facts remain distinct from:

```text
source is the correct authoritative artifact
engineering decision is correct
implementation is correct
verification evidence is sufficient
compliance is achieved
risk is accepted
release is ready
work is closed
```

Future automation shall not cross that boundary without separately defined authority semantics.

## 22. Current Decision Horizon / Progression Sufficiency for rc01

Applying frozen v0.0.8 proportional governance, rc01 needs only enough semantic precision to allow a later dependency/value decision about machine-readable source associations.

Progression Sufficiency for rc01 requires that reviewers can consistently distinguish:

```text
selection membership vs source relationship
source identity vs exact source instance
relationship role vs authority status
source ownership vs association provenance
discovery vs controlled association
resolvability vs currentness vs authority
source existence vs obligation satisfaction
source resolution vs content loading/context inclusion
unresolved mapping vs not-applicable/waived/closed
```

If these distinctions are coherent and no material current ambiguity remains, theoretical completeness alone shall not require immediate serialization, schema or resolver implementation.

## 23. Deliberately Deferred Scope

v0.0.9rc01 deliberately does **not** add:

```text
YAML / JSON source-association representation
source-association schema
source-aware source resolver
filesystem scanning
Git-history traversal
remote repository acquisition
external trust-model expansion
canonical source-role enum
canonical source-status enum
canonical association-provenance enum
automatic semantic-similarity mapping
automatic authority inference
scope hierarchy / scope resolver
content extraction / parsing / chunking
ranking / priority / severity policy
token-budget calculation
AI prompt / context package
AI orchestration / model selection
automatic applicability inference
Pattern recommendation / selection
implementation/compliance/verification/closure determination
CI enforcement of source mapping
L4 guidance expansion
Development Context Recovery / work-checkpoint mechanism
```

These are not defects in rc01. They require later dependency/value decisions.

## 24. Frozen Baselines Preserved

v0.0.9rc01 does not modify:

- the `294 / 218 / 76` authority inventory;
- `authority-registry.yaml`;
- frozen L1/L2 normative source;
- frozen L3 Pattern catalog or `12 / 119` trace inventory;
- Project Application semantics/representation/schema/validator/query;
- Effective Project Profile semantics/representation/schema/validator/generator;
- Consumption Selection semantics/representation/schema/validator/builder;
- frozen v0.0.8 Lifecycle-Proportional Governance semantics;
- release-integrity, external-pin, CI/trust implementation;
- existing executable regression implementations.

No new `SCAF-AK-*`, PAO or FNI identity is created.

## 25. Review Guidance

Review should focus on whether rc01 establishes a coherent source-resolution semantic boundary without silently transferring engineering authority or pre-authorizing context assembly.

A reviewer should treat as material any ambiguity that could cause future conforming implementations to disagree about:

- which authority domain may be resolved;
- whether discovery creates controlled association truth;
- whether source relationship implies authority/currentness/satisfaction;
- whether source resolution implies context inclusion;
- whether missing/unresolved mapping changes applicability/closure;
- whether scope or authority can be inferred from path/content presence.

Purely stylistic, taxonomic or future serialization preferences should not block rc01 when the semantic distinctions above are already progression-sufficient.

## 26. Post-Review Dependency / Value Gate

A clean rc01 review authorizes only a dependency/value assessment.

It does **not** automatically authorize rc02, a machine-readable model, schema, validator or resolver.

After review, SCAF shall ask whether a concrete representation/executable source-association model is actually required for the next engineering action.

If the answer is no, the v0.0.8 Materiality Stop Rule applies and the development line may STOP or defer further formalization.
