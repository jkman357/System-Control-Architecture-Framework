# SCAF v0.0.6rc12 — Effective Project Profile Source-Aware Validator Foundation

**Development Release:** v0.0.6rc12  
**Status:** Source-Aware Profile Validator Foundation / Review Candidate  
**Date:** 2026-08-18  
**Upstream Frozen Baselines:** v0.0.2 L1/L2; v0.0.3 L3; v0.0.4 Executable Governance; v0.0.5 L3 Machine-Readable Traceability  
**Accepted Development Basis:** v0.0.6rc09 Effective Project Profile semantics; v0.0.6rc10 canonical profile representation; v0.0.6rc11 profile schema  
**Immediate Predecessor:** v0.0.6rc11

## 1. Decision Purpose

The independent v0.0.6rc11 review returned a clean gate with zero findings:

```text
Critical: 0
Major:    0
Minor:    0
Trivial:  0

V0.0.6RC11 EFFECTIVE PROJECT PROFILE SCHEMA FOUNDATION GATE: YES
```

rc11 formalized the parsed-instance portion of the accepted rc10 Effective Project Profile representation and explicitly left source-aware facts outside JSON Schema authority.

Those deferred facts include:

- raw-YAML representation policy;
- complete Project-Applicable Obligation domain coverage;
- cross-entry `scaf_authority_id` uniqueness;
- authority existence/class/source-release resolution;
- exact Project Application source SHA-256 correspondence;
- accepted Project Application source validation;
- recorded-state Project Application record correspondence;
- exact-pair absence proof for `no_current_disposition`;
- deterministic entry and mapping order.

rc12 adds the first executable validator that owns those machine-determinable representation/source checks without converting profile validity into project engineering authority.

The governing rule is:

> **The rc12 validator may prove that an Effective Project Profile is structurally valid and source-consistent with the selected validated Project Application snapshot and validated SCAF PAO domain. It shall not decide whether the underlying engineering applicability judgments are substantively correct.**

## 2. Scope of rc12

rc12 adds:

```text
tools/scaf_effective_project_profile_validator/
```

The production CLI is:

```text
python -m tools.scaf_effective_project_profile_validator.validator
```

A caller may select the two project-controlled source files:

```text
python -m tools.scaf_effective_project_profile_validator.validator \
  --profile <effective-project-profile.yaml> \
  --project-application <project-application.yaml>
```

The caller cannot select or substitute through the production CLI:

- another SCAF repository root;
- another Effective Project Profile schema;
- another Project Application schema;
- another authority registry;
- another authority-registry schema;
- another canonical normative source tree.

Those contract inputs remain owned by the reviewed repository containing the validator.

## 3. Validation Pipeline

The rc12 production validation path is:

```text
selected Effective Project Profile bytes
        ↓ private snapshot
accepted rc10 raw-YAML policy
        ↓
accepted rc11 JSON Schema
        ↓
canonical mapping / entry ordering checks

selected Project Application bytes
        ↓ same private snapshot bytes
exact SHA-256 comparison
        ↓
accepted rc07 Project Application validation
        ↓
validated current Project Application records

repository authority-registry bytes
        ↓ private validation boundary
frozen source-aware authority validation
        ↓
validated source-release-bound PAO domain

validated profile + validated PAO domain + validated Project Application
        ↓
complete-domain / identity proof
        ↓
recorded-state trace proof
        ↓
no_current_disposition exact-pair absence proof
        ↓
PROFILE REPRESENTATION/SOURCE RESULT: PASS/FAIL
```

The validator does not generate or modify a profile. It validates an existing selected profile against selected/current source snapshots.

## 4. Same-Snapshot Source Ownership

### 4.1 Effective Project Profile snapshot

The selected profile bytes are read before validation and consumed through a private temporary snapshot.

Raw-YAML and parsed-instance checks operate on that snapshot.

### 4.2 Project Application snapshot

The selected Project Application bytes are read once before validation.

The same byte population is used for:

- SHA-256 calculation;
- private snapshot creation;
- accepted rc07 validation;
- current-record indexing;
- exact authority/scope pair lookup;
- recorded-state trace proof;
- absence proof.

The source file selected by the caller is not re-read after those bytes have been captured.

Therefore a caller-side file change after snapshot capture cannot change the current validator result into a projection of unvalidated later bytes.

### 4.3 Frozen authority-registry snapshot

The repository-owned authority registry is likewise captured into the private validation boundary before source-aware proof and profile-domain construction.

The same validated snapshot defines the authority index and the Project-Applicable Obligation population consumed by rc12 profile checks.

The private boundary includes copied canonical normative Markdown and repository-owned schemas required by the accepted frozen authority validator and rc07 Project Application validator.

## 5. Raw-YAML Policy

Before profile schema validation, rc12 rejects:

```text
duplicate mapping keys
YAML anchors
YAML aliases
YAML merge keys
custom YAML tags
multi-document streams
non-string mapping keys
```

The loader is based on `yaml.SafeLoader` with strict mapping construction.

Comments remain permitted and non-authoritative.

This executes the accepted rc10 YAML policy that rc11 correctly left outside JSON Schema proof.

## 6. rc11 Schema Chaining

After raw-YAML policy checks, the validator applies:

```text
schemas/effective-project-profile.schema.json
```

The accepted rc11 schema remains the owner of parsed-instance shape/state rules including:

- exact six-member root structure;
- profile kind and representation-release constants;
- non-empty source-release/scope strings;
- lowercase 64-hex source-digest syntax;
- four profile-state tokens;
- recorded-state `project_application_record_id` requirement;
- absence-state record-ID prohibition;
- unknown member rejection;
- parsed null/type constraints;
- exact duplicate complete-entry rejection.

If schema validation fails, later source-aware checks do not reinterpret the malformed profile as an engineering-state issue.

## 7. Project Application Source SHA-256 Proof

The profile field:

```text
project_application_source_sha256
```

is compared to SHA-256 computed over the exact selected Project Application bytes captured by the validator.

A lexical 64-hex value that does not match those exact bytes is source-invalid even though it is rc11 schema-valid.

The digest remains exact source-snapshot provenance only. It does not establish:

```text
signer identity
project approval
trust authority
engineering correctness
compliance evidence
semantic equivalence across different serializations
```

## 8. Accepted Project Application Proof

The same selected Project Application snapshot is validated through the accepted rc07 Project Application representation/source-aware validator.

If the selected Project Application snapshot fails rc07 validation, no supported profile source-consistency result may PASS.

This preserves:

- accepted Project Application raw-YAML policy;
- rc06 Project Application schema;
- record-ID uniqueness;
- current authority/scope pair uniqueness;
- deterministic collection ordering;
- frozen SCAF authority target existence/class/source-release resolution;
- valid `undetermined` as legitimate engineering-unresolved state.

rc12 does not create a second Project Application interpretation.

## 9. Validated PAO Domain Proof

The frozen authority-registry snapshot must first pass the existing source-aware authority validator.

For the profile's exact:

```text
scaf_source_release
```

rc12 derives the domain from validated authority records satisfying:

```text
authority_class: Project-Applicable Obligation
source_release: <profile scaf_source_release>
```

For the current accepted v0.0.2 source release this population is 218 PAOs, but rc12 derives the actual domain from the validated source snapshot rather than encoding `218` as the profile-validator semantic rule.

Framework Normative Invariants and unknown authority identities are outside the domain.

## 10. Complete-Domain and Identity Proof

For one validated profile:

- every entry `scaf_authority_id` must resolve in the validated authority snapshot;
- every entry must resolve to `Project-Applicable Obligation`;
- every entry's authority source release must equal profile `scaf_source_release`;
- each `scaf_authority_id` may occur at most once;
- the profile entry-ID set must exactly equal the validated PAO domain for that source release;
- entry count must equal the validated domain population.

This closes the rc11 limitations for:

```text
missing PAO entry
non-identical duplicate authority entry
FNI entry
unknown authority entry
wrong source-release domain
```

without adding any engineering applicability inference.

## 11. Deterministic Ordering Proof

rc12 enforces the accepted rc10 deterministic representation ordering:

### Root mapping

```text
profile_kind
representation_release
scaf_source_release
project_scope_ref
project_application_source_sha256
entries
```

### Recorded entry mapping

```text
scaf_authority_id
profile_state
project_application_record_id
```

### Absence entry mapping

```text
scaf_authority_id
profile_state
```

### Entry sequence

Entries must be ordered by exact serialized `scaf_authority_id` ascending.

These ordering rules support deterministic serialization/review/diffing only. They do not define engineering priority, authority precedence, Pattern preference or lifecycle order.

## 12. Recorded-State Trace Proof

For each profile entry whose state is:

```text
applicable
not_applicable
undetermined
```

its `project_application_record_id` must resolve in the same validated Project Application snapshot.

The resolved current record must match all of:

```text
record.scaf_authority_id == entry.scaf_authority_id
record.project_scope_ref == profile.project_scope_ref
record.applicability == entry.profile_state
record.scaf_source_release == profile.scaf_source_release
```

Because accepted rc07 already proves unique current authority/scope pairs, the exact pair must resolve to the same record identity referenced by the profile entry.

A profile cannot point to an existing but unrelated record merely because the record ID is syntactically valid.

## 13. `no_current_disposition` Absence Proof

This is the most important new rc12 source-aware rule.

For an entry with:

```text
profile_state: no_current_disposition
```

rc12 proves that the same validated Project Application snapshot contains **no current record** for the exact pair:

```text
(entry.scaf_authority_id, profile.project_scope_ref)
```

Therefore rc12 turns a profile token from an unverified assertion into a machine-proven dataset-relative fact:

```text
no current exact-pair record exists
in this selected validated Project Application snapshot
```

It still does **not** mean:

```text
not_applicable
undetermined
intentional omission
scope nonexistence
project failure
non-compliance
project incompleteness
```

The absence proof is relative only to the selected validated source snapshot and exact opaque scope string.

## 14. Exact-Scope / Resolver Boundary

`project_scope_ref` remains an opaque non-empty project-controlled string.

rc12 performs exact serialized string equality only.

It does not add:

- a project-scope registry;
- scope existence proof;
- hierarchy or containment;
- aliasing;
- inheritance;
- wildcard resolution;
- parent/child carryover.

A disposition from another scope cannot satisfy or contradict the selected exact scope unless the serialized scope strings are exactly equal.

## 15. Invalid Versus Unresolved

A profile with a valid recorded `undetermined` state remains validator-valid when its referenced Project Application record is itself valid and matches the same authority/scope/source/state.

Therefore:

```text
engineering unresolved
!= representation invalid
```

By contrast, a malformed profile, invalid source digest, invalid Project Application snapshot, wrong trace, incomplete PAO domain, or contradicted absence state is representation/source invalid.

## 16. Production CLI Authority Boundary

The production CLI accepts only:

```text
--profile
--project-application
```

It does not expose caller substitution of repository/schema/authority/normative boundaries.

The function-level API:

```text
validate_effective_project_profile(repo_root, profile_path=None, project_application_path=None)
```

accepts `repo_root` for isolated controlled tests. That testability surface is not a production CLI repository override.

## 17. PASS Meaning

The success line is exactly:

```text
PROFILE REPRESENTATION/SOURCE RESULT: PASS
```

PASS means only that the selected profile passed the implemented representation/source-consistency checks.

It does not mean:

```text
PROJECT PASS
ENGINEERING PASS
COMPLIANCE PASS
VERIFICATION PASS
RELEASE PASS
CLOSURE PASS
```

It does not approve the substantive engineering applicability decision recorded by Project Application.

## 18. Deliberate Non-Expansion

rc12 does not add:

- an Effective Project Profile generator/builder;
- a profile query/view API beyond validation;
- a persistent/generated profile registry or cache;
- project-scope/reference resolution;
- automatic applicability inference;
- AI approval of engineering rationale;
- Project Design Authority automation;
- Pattern recommendation or selection;
- implementation/satisfaction determination;
- verification/evidence sufficiency determination;
- compliance determination;
- risk acceptance;
- project completion determination;
- release/closure determination;
- AI context packaging;
- CI applicability-completion enforcement;
- code generation;
- new L3 Pattern content;
- L4 guidance;
- Development Context Recovery / `.scaf/work-checkpoint.yaml` workflow state.

## 19. Regression Boundary

The accepted/frozen regressions remain required:

```text
rc07 Project Application validator suite     21
rc08 Project Application view/query suite    22
frozen executable-governance suites          41
frozen trace-validator suite                 24
frozen trace-view/query suite                 28
```

The frozen authority inventory remains:

```text
294 total authority records
218 Project-Applicable Obligations
76 Framework Normative Invariants
```

The frozen L3 trace inventory remains:

```text
12 Patterns
119 relations
```

## 20. Acceptance Criteria

rc12 is acceptable only if independent review confirms all of the following:

1. package/Git lineage is exactly on the committed rc11 predecessor;
2. the source delta is limited to the intended rc12 validator/documentation surface;
3. accepted rc10 fixture and rc11 schema remain unchanged;
4. profile raw-YAML restrictions execute before parsed-instance schema consumption;
5. the accepted rc11 schema is reused rather than redefined;
6. selected Project Application exact-byte SHA-256 is actually compared;
7. the selected Project Application snapshot passes accepted rc07 validation;
8. the frozen authority-registry snapshot passes source-aware proof before PAO-domain use;
9. complete source-release-bound PAO domain and cross-entry identity are checked;
10. FNI/unknown/wrong-source-release entries are rejected;
11. canonical root/entry/sequence ordering is checked;
12. recorded-state record IDs resolve to the exact authority/scope/state/source release;
13. `no_current_disposition` is accepted only when exact-pair absence is proven in the same validated Project Application snapshot;
14. valid `undetermined` remains valid unresolved engineering state;
15. production CLI does not permit repository/schema/authority substitution;
16. success wording remains profile representation/source conformance only;
17. no generator/resolver/inference/Pattern/CI/L4 scope expansion occurs;
18. rc12 regression tests and all accepted/frozen regressions pass.

## 21. Plain-Language Meaning

rc11 could answer:

> "Does this profile have the right structural shape?"

rc12 adds:

> "Does this profile actually agree with the SCAF obligation domain and the exact Project Application source snapshot it claims to describe?"

For `no_current_disposition`, that specifically means the tool now checks the source data and proves the exact record is absent from the selected validated dataset. It still does not decide whether that absence is acceptable or whether the project is complete.
