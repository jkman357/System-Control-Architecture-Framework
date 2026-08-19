# SCAF v0.0.7rc04 — Consumption Selection Schema Foundation

**Development Release:** v0.0.7rc04  
**Status:** Consumption Selection JSON Schema Foundation / Review Candidate  
**Date:** 2026-08-19  
**Immediate Predecessor:** v0.0.7rc03 (`be5a0ba3725002778ceb0f8c163b5d14f280336c`)  
**Accepted Development Basis:** v0.0.7rc01 consumption semantics; v0.0.7rc02 canonical logical model; v0.0.7rc03 canonical YAML representation  
**Frozen Basis:** v0.0.2 L1/L2; v0.0.3 L3; v0.0.4 Executable Governance; v0.0.5 L3 Machine-Readable Traceability; v0.0.6 Machine-Readable Project Application / Effective Project Profile

## 1. Decision Purpose

The independent v0.0.7rc03 review returned a clean gate with zero findings:

```text
Critical: 0
Major:    0
Minor:    0
Trivial:  0

V0.0.7RC03 CANONICAL CONSUMPTION / CONTEXT-SELECTION
MACHINE-READABLE REPRESENTATION FOUNDATION GATE: YES
```

rc03 established the accepted canonical YAML representation for one subordinate Consumption Selection over one validated Effective Project Profile snapshot.

v0.0.7rc04 takes the next bounded step: formalize the **parsed-instance structural/state-shape portion** of that accepted rc03 representation as JSON Schema Draft 2020-12.

The governing rule is:

> **The rc04 schema may determine whether a parsed Consumption Selection instance has the accepted rc03 structural/state shape. It shall not claim source-profile correspondence, authority/domain membership, selector/source set algebra, selected-entry source fidelity, or engineering authority.**

rc04 does not revise the rc03 serialization and therefore preserves:

```text
representation_release: v0.0.7rc03
```

## 2. Scope of rc04

rc04 adds:

```text
schemas/consumption-selection.schema.json
```

The schema formalizes only machine-determinable parsed-instance facts that can be checked without loading or proving the bound Effective Project Profile source.

rc04 does **not** add:

```text
raw-YAML policy enforcement
source-aware Consumption Selection validator
Consumption Selection builder/generator
Consumption Selection read/query API or CLI
persistent selection/context registry/cache/history
profile history/supersession
project-scope/reference resolver or hierarchy
PAO-to-file/document/context-source resolver
context-content record
AI context package/prompt/orchestration
arbitrary predicate language
semantic-similarity selection
priority/ranking/severity model
automatic applicability inference
Pattern recommendation/selection
AI approval / Project Design Authority automation
CI applicability-completion enforcement
implementation/compliance/verification/closure determination
profile-driven code generation
new L3 tranche / M3 / M4
L4 guidance
Development Context Recovery / .scaf/work-checkpoint.yaml
external-trust-model expansion
```

A later RC may separately consider a source-aware Consumption Selection validator after this schema boundary is independently reviewed.

## 3. Schema Identity

The schema uses JSON Schema Draft 2020-12:

```text
$schema: https://json-schema.org/draft/2020-12/schema
$id: urn:scaf:schema:consumption-selection:v0.0.7rc04
```

The schema targets the already accepted representation:

```text
selection_kind: consumption_selection
representation_release: v0.0.7rc03
```

rc04 does not create `representation_release: v0.0.7rc04`. The version of the schema and the version of the serialized representation are intentionally different concepts.

## 4. Root Parsed Representation

The parsed root must be an object containing exactly these nine accepted members:

```text
selection_kind
representation_release
source_profile_binding
selection_purpose
state_selector
authority_selector
bounded_omission
selected_entries
selection_class
```

All nine are required. Unknown root members are rejected.

The schema enforces exact discriminator/release values:

```text
selection_kind = consumption_selection
representation_release = v0.0.7rc03
```

The schema does not assign approval, project status, compliance, verification, release, closure, priority, severity, or engineering meaning to those contract identities.

## 5. Source Profile Binding Shape

`source_profile_binding` must be an object containing exactly:

```text
effective_project_profile_source_sha256
scaf_source_release
project_scope_ref
project_application_source_sha256
```

The schema requires:

- both SHA-256 fields to be exactly 64 lowercase hexadecimal characters;
- `scaf_source_release` to be a non-empty string;
- `project_scope_ref` to be a non-empty string;
- no unknown members.

The schema intentionally does **not** prove that:

```text
effective_project_profile_source_sha256
== SHA-256(actual selected profile bytes)
```

or that the other three provenance values equal the values inside that profile.

Those are source-aware proof obligations for a later validator.

The digest remains exact-byte provenance only. Schema conformance does not establish signer identity, trust, approval, semantic equivalence, engineering correctness, compliance, verification, release readiness, or closure.

## 6. Selection Purpose

`selection_purpose` must be a non-empty parsed string.

The schema only validates its representation shape. It does not interpret or approve its meaning.

A valid purpose string cannot change:

```text
profile state
Project Application state
PAO authority
Pattern selection
implementation state
verification/compliance state
risk acceptance
release/closure state
```

## 7. State Selector

`state_selector` must be an array containing zero to four unique items drawn only from:

```text
applicable
not_applicable
undetermined
no_current_disposition
```

This preserves the frozen four-state vocabulary and permits the accepted empty selector.

`uniqueItems: true` rejects duplicate state tokens.

The schema does not prove the rc03 canonical physical order of state tokens. Parsed JSON data does not carry the raw-YAML ordering/format policy needed for that proof. A later representation/source-aware validator may enforce canonical sequence order where required.

No fifth profile state is introduced by selection, inclusion, omission, exclusion, or classification.

## 8. Authority Selector Shapes

The schema accepts exactly one of two shapes.

### 8.1 All-domain selector

```yaml
authority_selector:
  mode: "all_domain"
```

No `scaf_authority_ids` member is allowed in this shape.

### 8.2 Explicit-set selector

```yaml
authority_selector:
  mode: "explicit_set"
  scaf_authority_ids:
    - "SCAF-AK-001"
```

The ID array:

- is required for `explicit_set`;
- may be empty;
- contains non-empty strings;
- rejects exact duplicate strings through `uniqueItems: true`.

Schema validation does not prove that an explicit ID exists, is a PAO, belongs to the bound source-release domain, or is in canonical lexical order.

Those remain source-aware and representation-order proof obligations.

## 9. Bounded Omission Shapes

The schema accepts exactly one of two shapes.

### 9.1 No bounded omission

```yaml
bounded_omission:
  applied: false
```

`basis` is prohibited by the exact object shape.

### 9.2 Bounded omission applied

```yaml
bounded_omission:
  applied: true
  basis: "non-empty descriptive basis"
```

A non-empty `basis` is required when `applied` is true.

The schema checks only this state-compatible representation shape.

It does not prove:

```text
applied: false -> I = E
applied: true  -> I subset-or-equal E and O = E - I
```

because those relations require the validated source profile plus selector evaluation.

`basis` remains non-authoritative descriptive metadata and is not a ranking, priority, severity, applicability, compliance, or closure decision.

## 10. Selected Entry Shapes

Every `selected_entries` item must match exactly one of two accepted shapes.

### 10.1 Recorded-state selected entry

For:

```text
applicable
not_applicable
undetermined
```

the parsed object must contain exactly:

```text
scaf_authority_id
profile_state
project_application_record_id
```

All identity strings must be non-empty.

### 10.2 Absence-state selected entry

For:

```text
no_current_disposition
```

the parsed object must contain exactly:

```text
scaf_authority_id
profile_state
```

`project_application_record_id` is prohibited by the exact absence-state object shape.

This preserves:

```text
no_current_disposition
!= synthetic Project Application record
```

The schema rejects exact duplicate complete selected-entry objects through `uniqueItems: true`.

It does **not** prove cross-entry uniqueness of `scaf_authority_id` when two non-identical entry objects reuse the same ID.

## 11. Selection Class Shape

`selection_class` accepts exactly:

```text
complete
filtered
```

This is parsed representation validation only.

The schema cannot prove the accepted derivation:

```text
complete
iff I = D and O = empty and X = empty

filtered
otherwise
```

A caller-supplied `selection_class` token that has a valid lexical value but contradicts the actual source-derived set relations therefore requires rejection by a later source-aware validator, not by schema-only validation.

## 12. Parsed-Instance Facts Enforced by rc04

Within its intended scope, the rc04 schema can enforce:

- root is an object;
- exact nine root member names and all are required;
- exact `selection_kind` and rc03 `representation_release` tokens;
- exact source-binding member names;
- lowercase 64-hex lexical digest forms;
- non-empty source release, scope and purpose strings;
- four-token state selector vocabulary;
- state-selector duplicate rejection and maximum four items;
- exact all-domain versus explicit-set authority-selector shapes;
- explicit-set duplicate-string rejection;
- exact bounded-omission `applied:false` / `applied:true + basis` shapes;
- selected entries are an array;
- exact duplicate complete selected-entry rejection;
- exact recorded-state versus absence-state selected-entry shapes;
- Project Application record ID required for recorded states;
- Project Application record ID prohibited for `no_current_disposition`;
- exact `complete` / `filtered` selection-class vocabulary;
- unknown members rejected at every schema-owned object boundary;
- parsed null/type mismatches rejected where the representation requires object, array, string, or boolean values.

A schema PASS means only that these parsed representation facts conform.

## 13. Explicit Schema-Only Limitations

The following accepted rc01/rc02/rc03 obligations remain outside schema-only proof and are **not weakened** by rc04.

### 13.1 Bound source-profile validity

The schema cannot execute the frozen v0.0.6 Effective Project Profile validator and cannot establish that the selected source profile is valid.

### 13.2 Exact profile-byte SHA-256 correspondence

The schema validates lowercase digest syntax only. It cannot compare the serialized digest to the exact selected profile bytes.

### 13.3 Provenance equality

The schema cannot prove that:

```text
scaf_source_release
project_scope_ref
project_application_source_sha256
```

match the values inside the bound source profile.

### 13.4 Authority existence and domain membership

The schema cannot resolve explicit IDs against the validated source-release-bound PAO domain and cannot reject a syntactically non-empty but unknown authority ID for source reasons.

### 13.5 Eligibility set `E`

The schema cannot evaluate the accepted predicate over the bound source profile:

```text
profile_state in state_selector
AND
authority satisfies authority_selector
```

### 13.6 Selected-entry source fidelity

The schema cannot prove that every selected entry exists in the source profile with the same exact authority ID, profile state, and conditional Project Application record trace.

### 13.7 Set algebra

The schema cannot prove:

```text
E = I + O
D = I + O + X
I / O / X mutually disjoint
predicate excluded != bounded omitted
```

### 13.8 Bounded omission consistency

The schema cannot prove `I == E` when omission is not applied or reconstruct `O = E - I` when it is applied.

### 13.9 Complete/filtered derivation

The schema cannot prove that the serialized `selection_class` matches actual source-derived set relations.

### 13.10 Cross-entry authority uniqueness

`uniqueItems` rejects duplicate complete objects only; it does not prove unique `scaf_authority_id` across non-identical selected entries.

### 13.11 Canonical physical YAML policy

JSON Schema operates on parsed instances. It does not prove:

```text
single YAML document
raw duplicate-key absence
anchors/aliases/merge/custom-tag absence
physical mapping-member order
canonical state-selector order
canonical authority-ID order
canonical selected-entry order
quoted-string style
comment policy
```

### 13.12 Engineering authority

Schema validity does not prove or decide:

```text
applicability correctness
scope correctness
Pattern selection
implementation status
verification sufficiency
compliance
risk acceptance
release readiness
closure
AI approval
Project Design Authority approval
```

## 14. Authority Separation Preserved

The accepted boundaries remain:

```text
included in context != applicable
excluded from context != not_applicable
omitted != not_applicable
predicate excluded != bounded omitted
undetermined != no_current_disposition
```

and:

```text
machine-determinable representation fact
!= engineering judgment
!= Project Design Authority decision
!= verification result
!= compliance result
!= risk acceptance
!= release readiness
!= closure
```

A valid Consumption Selection schema instance is a structurally/state-shape-conformant subordinate selection record only.

## 15. Frozen v0.0.6 Preservation

rc04 does not modify:

```text
authority-registry.yaml
l3-trace-registry.yaml
examples/project-application.yaml
examples/effective-project-profile.yaml
examples/consumption-selection.yaml
schemas/project-application.schema.json
schemas/effective-project-profile.schema.json
accepted/frozen validators, views, generator, integrity/trust tooling
docs/normative/
docs/l3/
release-integrity/
.github/workflows/
```

Formal v0.0.6 remains immutable.

## 16. Intended Progression

A possible later progression is:

```text
rc01 consumption semantics
        ↓
rc02 canonical logical model
        ↓
rc03 canonical YAML representation
        ↓
rc04 parsed-instance JSON Schema
        ↓
later source-aware Consumption Selection validator
        ↓
later deterministic selection builder/generator
        ↓
later separately reviewed context-source resolution / context assembly
```

This progression is explanatory only. rc04 does not pre-authorize any later stage.

## 17. Acceptance Boundary

rc04 is acceptable only if independent review confirms that:

1. the rc03 representation remains unchanged;
2. the schema validates the accepted fixture;
3. the schema rejects malformed structural/state-shape cases it claims to own;
4. state/selector/omission/selected-entry shape constraints match accepted rc03 semantics;
5. schema-only limitations are explicit and accurate;
6. no source-aware or engineering conclusion is claimed from schema PASS;
7. frozen v0.0.6 and accepted rc01-rc03 behavior remain unchanged;
8. no deferred validator/builder/context-source/AI/CI/L4 capability is introduced.

A clean rc04 review authorizes only continuation of the controlled v0.0.7 development line.
