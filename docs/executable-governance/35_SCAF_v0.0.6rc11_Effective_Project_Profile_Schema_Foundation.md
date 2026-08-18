# SCAF v0.0.6rc11 — Effective Project Profile Schema Foundation

**Development Release:** v0.0.6rc11  
**Status:** Effective Project Profile Schema Foundation / Review Candidate  
**Date:** 2026-08-18  
**Upstream Frozen Baselines:** v0.0.2 L1/L2; v0.0.3 L3; v0.0.4 Executable Governance; v0.0.5 L3 Machine-Readable Traceability  
**Accepted Development Basis:** v0.0.6rc09 Effective Project Profile semantics; v0.0.6rc10 canonical representation  
**Immediate Predecessor:** v0.0.6rc10

## 1. Decision Purpose

The independent v0.0.6rc10 review returned a clean gate with zero findings:

```text
Critical: 0
Major:    0
Minor:    0
Trivial:  0

V0.0.6RC10 EFFECTIVE PROJECT PROFILE CANONICAL REPRESENTATION FOUNDATION GATE: YES
```

rc10 established the first canonical machine-readable YAML representation for the accepted rc09 Effective Project Profile semantics. The representation is intentionally subordinate derived current-state information: it does not create, approve, replace, or strengthen a Project Application judgment.

rc11 takes the next bounded step: encode the **machine-determinable parsed-instance portion** of the accepted rc10 representation as a formal JSON Schema Draft 2020-12 schema foundation.

The governing rule is:

> **The rc11 schema may decide whether a parsed profile instance has the accepted rc10 structural/state shape. It shall not claim facts that require framework-source resolution, Project Application source comparison, raw-YAML inspection, or engineering judgment.**

## 2. Scope of rc11

rc11 adds:

```text
schemas/effective-project-profile.schema.json
```

The schema formalizes only the accepted rc10 representation facts that JSON Schema can determine from a parsed instance without external source reconstruction.

rc11 does **not** add:

- an Effective Project Profile generator/builder;
- a profile representation/source-aware validator;
- profile query API or CLI;
- persistent/generated profile registry or cache;
- raw-YAML loader-policy enforcement;
- PAO-domain resolution against `authority-registry.yaml`;
- Project Application record resolution;
- verification that `project_application_source_sha256` matches actual source bytes;
- project-scope registry or resolver;
- automatic applicability inference;
- AI approval of engineering rationale;
- Project Design Authority automation;
- Pattern recommendation or selection;
- implementation/satisfaction/compliance determination;
- verification/evidence/closure determination;
- project completion PASS/FAIL;
- AI context packaging;
- CI applicability-completion enforcement;
- code generation;
- new L3 Pattern content;
- L4 guidance;
- Development Context Recovery / `.scaf/work-checkpoint.yaml` state.

A later RC may separately consider a representation/source-aware profile validator only after this schema boundary is independently reviewed.

## 3. Schema Identity

The schema is JSON Schema Draft 2020-12:

```text
$schema: https://json-schema.org/draft/2020-12/schema
$id: urn:scaf:schema:effective-project-profile:v0.0.6rc11
```

The schema targets the already accepted profile representation release:

```text
representation_release: v0.0.6rc10
```

rc11 does **not** create a new profile representation release. It formalizes the parsed-instance portion of the accepted rc10 representation contract.

## 4. Root Representation Contract

The parsed profile root shall be an object containing exactly the six accepted rc10 members:

```text
profile_kind
representation_release
scaf_source_release
project_scope_ref
project_application_source_sha256
entries
```

All six are required and unknown root members are rejected.

The schema enforces:

```text
profile_kind = effective_project_profile
representation_release = v0.0.6rc10
```

`scaf_source_release` remains a non-empty string rather than a schema constant. This preserves the rc10 representation rule that the profile domain is bound to the validated PAO population of the selected source release and that a later source release may have a different PAO population while still using the same representation contract.

`project_scope_ref` remains a non-empty opaque string. Schema validity does not prove project-scope existence, hierarchy, aliasing, inheritance, ownership, or engineering correctness.

## 5. Source SHA-256 Field

The schema enforces only the lexical representation of:

```text
project_application_source_sha256
```

as exactly 64 lowercase hexadecimal characters:

```text
^[0-9a-f]{64}$
```

This is a parsed-instance representation fact only.

The schema cannot prove that the digest actually equals SHA-256 over the exact raw bytes of the selected Project Application source. That source-aware comparison remains deferred to a later validator boundary.

The digest continues to mean only exact source-snapshot provenance. Schema conformance does not make it signer identity, project approval, trust evidence, compliance evidence, or semantic-equivalence identity.

## 6. Entry Structural Model

Each `entries` item must match exactly one of two accepted shapes.

### 6.1 Recorded-state entry

For:

```text
applicable
not_applicable
undetermined
```

the schema requires exactly:

```text
scaf_authority_id
profile_state
project_application_record_id
```

All required string identities must be non-empty.

The schema therefore rejects a recorded state whose `project_application_record_id` is omitted, empty, null, or accompanied by unknown extra members.

### 6.2 Absence-state entry

For:

```text
no_current_disposition
```

the schema requires exactly:

```text
scaf_authority_id
profile_state
```

and rejects `project_application_record_id` because the absence-state object has `additionalProperties: false` and does not define that field.

This preserves the rc09/rc10 rule:

```text
no_current_disposition
!= synthetic Project Application record
```

## 7. Profile-State Vocabulary

The schema accepts exactly:

```text
applicable
not_applicable
undetermined
no_current_disposition
```

The first three are recorded-state profile tokens and require a Project Application record trace field.

The fourth is the profile-only absence token and prohibits that trace field.

This schema does not change the Project Application applicability vocabulary, which remains:

```text
applicable
not_applicable
undetermined
```

A Project Application record containing:

```text
applicability: no_current_disposition
```

remains invalid under the accepted Project Application schema/validator.

## 8. Parsed-Instance Facts Enforced by rc11

Within its intended scope, the rc11 schema can deterministically enforce:

- root parsed type is an object;
- exactly the six accepted root member names;
- all six root members are present;
- exact `profile_kind` token;
- exact `representation_release` token;
- non-empty `scaf_source_release`;
- non-empty opaque `project_scope_ref`;
- lowercase 64-hex lexical SHA-256 shape;
- `entries` is an array;
- exact duplicate complete entry objects are rejected by `uniqueItems`;
- every entry matches one accepted state-specific object shape;
- non-empty `scaf_authority_id`;
- exact four-token profile-state vocabulary;
- `project_application_record_id` required for recorded states;
- `project_application_record_id` prohibited for `no_current_disposition`;
- non-empty record identity when present;
- unknown entry members rejected;
- parsed null/type mismatches rejected where the contract requires string/array/object values.

A successful schema check means only that these parsed representation facts conform.

## 9. Explicit Schema-Only Limitations

The following rc10 contract rules remain outside schema-only proof and are **not weakened or removed** by rc11.

### 9.1 Complete PAO-domain coverage

The schema cannot determine the validated PAO population for `scaf_source_release`.

Therefore it cannot prove:

```text
entry count = D
all PAO IDs occur exactly once
no PAO is omitted
```

For the current frozen v0.0.2 source, `D = 218` remains an observed validated source inventory, not a schema magic number.

### 9.2 Cross-entry `scaf_authority_id` uniqueness

`uniqueItems: true` rejects exact duplicate complete entry objects only.

It does **not** prove that two non-identical entries cannot share the same `scaf_authority_id`.

A later validator must enforce one entry per validated PAO identity.

### 9.3 Authority existence and class

The schema treats `scaf_authority_id` as a non-empty string.

It cannot prove that an ID:

- exists in the validated authority source;
- belongs to the profile's `scaf_source_release`;
- is a Project-Applicable Obligation;
- is not a Framework Normative Invariant.

### 9.4 Project Application record trace correctness

For recorded states, schema requires a non-empty `project_application_record_id`, but cannot prove that the record:

- exists in the selected validated Project Application source;
- is current under the accepted representation;
- has the same exact `scaf_authority_id`;
- has the same exact `project_scope_ref`;
- has `applicability` equal to `profile_state`.

### 9.5 Absence correctness

Schema can enforce the **shape** of `no_current_disposition`, including prohibition of a record ID.

It cannot prove the semantic absence fact that no current Project Application record exists for the exact PAO/scope pair in the selected source snapshot.

### 9.6 SHA-256 source correspondence

Schema validates only lowercase 64-hex syntax.

It cannot recompute or compare the digest with actual source bytes.

### 9.7 Entry ordering

JSON Schema does not establish the rc10 exact-string ascending `scaf_authority_id` ordering contract.

A parsed instance may be schema-valid while its entries are not in canonical physical order.

### 9.8 Raw YAML representation policy

Parsed-instance JSON Schema cannot reliably establish raw-YAML conditions including:

```text
duplicate mapping keys
anchors
aliases
merge keys
custom tags
multi-document streams
physical mapping-member order
```

These remain representation/source-aware validation concerns.

### 9.9 Engineering and project authority

Schema validity cannot determine:

```text
applicability correctness
rationale adequacy
Project Design Authority approval
scope correctness/existence
Pattern suitability or selection
implementation satisfaction
verification/evidence sufficiency
compliance
risk acceptance
project completion
release readiness
closure
```

## 10. Canonical Fixture Compatibility

The accepted rc10 fixture remains unchanged:

```text
examples/effective-project-profile.yaml
```

It must validate against:

```text
schemas/effective-project-profile.schema.json
```

The fixture remains faithfully derived for:

```text
project_scope_ref: example:scope:system
```

with the accepted current partition:

```text
D = 218
A = 1
N = 0
U = 0
M = 217
```

rc11 does not fabricate not-applicable or undetermined entries simply to exercise schema branches. Those branches are verified through bounded disposable test instances.

## 11. Required Bounded Schema Checks

Review and local validation should materially exercise both positive and negative conditions.

At minimum verify:

```text
accepted rc10 fixture                                -> schema valid
unknown root member                                  -> schema invalid
wrong profile_kind                                   -> schema invalid
wrong representation_release                         -> schema invalid
empty scaf_source_release                            -> schema invalid
empty project_scope_ref                              -> schema invalid
uppercase / wrong-length source digest               -> schema invalid
unsupported profile_state                            -> schema invalid
recorded state without project_application_record_id -> schema invalid
recorded state with empty record ID                  -> schema invalid
no_current_disposition with record ID                -> schema invalid
unknown entry member                                 -> schema invalid
parsed null where string/array required              -> schema invalid
exact duplicate complete entry                       -> schema invalid
```

Also verify the documented schema-only limitations remain limitations rather than accidental positive claims:

```text
omit one otherwise-valid PAO entry
-> may remain schema-valid; later complete-domain validator concern

duplicate scaf_authority_id using two different valid entry objects
-> may remain schema-valid; later cross-entry identity concern

non-empty FNI/unknown-looking scaf_authority_id
-> may remain schema-valid; later authority-resolution concern

lexically valid but incorrect 64-hex source digest
-> may remain schema-valid; later source-aware comparison concern

recorded non-empty record ID pointing to wrong/nonexistent source record
-> may remain schema-valid; later trace-resolution concern

non-canonical entry order
-> may remain schema-valid; later deterministic representation validator concern
```

These limitation cases are expected. They are not rc11 defects if the schema and documentation do not claim otherwise.

## 12. Invalid Versus Unresolved

A conformant `undetermined` entry remains representation-valid when it has the required non-empty Project Application record trace field.

That means only the profile shape records an explicit unresolved engineering disposition.

It is not:

```text
schema failure
project failure
non-compliance
verification failure
closure failure
```

`no_current_disposition` remains distinct: it represents dataset-relative current-record absence and does not carry a synthetic record ID.

## 13. Authority Boundary

The schema is subordinate to the accepted framework and Project Application sources.

It may decide parsed structural/state-shape facts only.

The enduring separation remains:

```text
machine-determinable representation fact
!= engineering judgment
!= project authority decision
!= verification result
!= compliance result
!= closure
```

A successful schema validation must never be rendered as:

```text
PROJECT PASS
COMPLIANCE PASS
ENGINEERING PASS
PROFILE APPROVED
```

## 14. Preservation Requirements

rc11 shall not modify:

```text
authority-registry.yaml
l3-trace-registry.yaml
examples/project-application.yaml
examples/effective-project-profile.yaml
schemas/authority-registry.schema.json
schemas/l3-trace-registry.schema.json
schemas/project-application.schema.json
tools/scaf_project_application_validator/
tools/scaf_project_application_views/
docs/normative/
docs/l3/
release-integrity/
.github/workflows/
```

Frozen and accepted regression behavior remains unchanged.

## 15. Future Review Boundary

After rc11 is independently accepted, a later RC may consider a source-aware Effective Project Profile validator.

That later boundary would be responsible for machine-determinable facts schema alone cannot prove, such as:

- raw-YAML policy;
- canonical physical entry ordering;
- validated complete PAO-domain coverage;
- cross-entry authority-ID uniqueness;
- authority existence/class/source-release proof;
- exact Project Application source SHA-256 correspondence;
- recorded entry/source-record authority/scope/state consistency;
- actual current-record absence for `no_current_disposition`.

That later validator still must not decide engineering applicability correctness or Project Design Authority approval.

No such executable validator is introduced by rc11.

## 16. Acceptance Conditions

rc11 is acceptable only if independent review confirms:

1. schema is valid JSON Schema Draft 2020-12;
2. accepted rc10 fixture validates;
3. schema faithfully encodes the parsed-instance portion of rc10 without inventing new semantics;
4. four-state entry shape compatibility is deterministic;
5. `no_current_disposition` remains profile-only and trace-free;
6. `undetermined` remains valid unresolved engineering state when structurally conformant;
7. complete-domain/source-resolution/trace-resolution/order/raw-YAML limitations are explicit and not falsely claimed as schema proof;
8. rc10 fixture and accepted/frozen inputs remain byte-identical;
9. rc07/rc08 and all frozen regression suites remain passing;
10. no generator, validator, resolver, context-package, CI, Pattern-selection, L4, or work-checkpoint capability is introduced.

## 17. Boundary Statement

v0.0.6rc11 establishes only the formal parsed-instance schema foundation for the accepted rc10 Effective Project Profile representation.

It does not turn the profile into project authority and does not prove complete-domain/source-aware correctness.

The next executable profile step, if any, remains separately review-gated.
