# SCAF v0.0.6rc14 — Project Application / Effective Project Profile Milestone Consolidation and Freeze Candidate

**Development Release:** v0.0.6rc14  
**Status:** Milestone Consolidation / Freeze Candidate  
**Date:** 2026-08-18  
**Immediate Predecessor:** v0.0.6rc13 (`88b793c34c2090c9bd4d4b8053ded1ec6d892573`)  
**Upstream Frozen Baselines:** v0.0.2 L1/L2; v0.0.3 L3; v0.0.4 Executable Governance; v0.0.5 L3 Machine-Readable Traceability

## 1. Decision Purpose

v0.0.6rc14 consolidates the accepted v0.0.6 SCAF-APP Project Application and Effective Project Profile work into one reviewable milestone / freeze-candidate boundary.

It introduces no new Project Application state, profile state, representation, schema rule, validator behavior, query behavior, generator behavior, project authority, scope resolver, Pattern-selection capability, compliance result, or lifecycle-closure capability.

Its purpose is to verify that the accumulated rc01→rc13 chain is internally consistent, historical findings are closed, the machine-determinable boundary is complete for the intended v0.0.6 milestone, accepted regressions remain green, and deferred capabilities are explicit rather than silently implied.

A clean rc14 review establishes **freeze eligibility only**. Formal `v0.0.6` freeze requires a separate explicit governance decision.

## 2. Accepted Pre-Consolidation Review State

The independent v0.0.6rc13 review reported:

```text
Critical: 0
Major:    0
Minor:    0
Trivial:  0

V0.0.6RC13 EFFECTIVE PROJECT PROFILE DETERMINISTIC GENERATOR FOUNDATION GATE: YES
```

The review confirmed that the generator is validation-owning, deterministic, exact-scope, snapshot-based, non-persistent, and subordinate to accepted Project Application and SCAF authority sources. Generated output must pass the accepted rc12 representation/source validator before return or CLI emission.

The repository-external production trust bundle was not separately supplied to the rc13 review. Its actual production execution therefore remained **not independently verified**. This does not reopen the v0.0.6 source semantics because rc01→rc13 do not modify the frozen external-trust boundary.

## 3. Consolidated v0.0.6 Dependency Chain

The accepted milestone chain is:

```text
frozen v0.0.2 L1/L2 authority
    294 authority records
    218 Project-Applicable Obligations
    76 Framework Normative Invariants
        ↓
rc01 SCAF-APP Project Application semantic foundation
        ↓
rc02 canonical Project Application logical record model
        ↓
rc03 basis-role / state-compatibility hardening
        ↓
rc04 canonical Project Application YAML representation
        ↓
rc05 serialization fixture coverage hardening
        ↓
rc06 Project Application JSON Schema
        ↓
rc07 Project Application representation/source-aware validator
        ↓
rc08 validated deterministic Project Application read/query views
        ↓
rc09 Effective Project Profile semantic foundation
        ↓
rc10 canonical Effective Project Profile YAML representation
        ↓
rc11 Effective Project Profile JSON Schema
        ↓
rc12 Effective Project Profile representation/source-aware validator
        ↓
rc13 deterministic Effective Project Profile generator
        ↓
rc14 milestone consolidation / freeze candidate
```

Each downstream layer remains subordinate to the authority or project-side source above it. Machine-readable state, validation, query, profile projection, and generation do not create engineering decision authority.

## 4. Consolidated Project Application Contract

The accepted Project Application record model continues to represent project-side disposition of one SCAF Project-Applicable Obligation for one exact opaque project scope.

Accepted applicability tokens remain exactly:

```text
applicable
not_applicable
undetermined
```

`undetermined` remains a legitimate explicit engineering-unresolved state. It is not representation failure, project failure, non-compliance, or closure failure.

The accepted concrete representation remains `representation_release: v0.0.6rc04` and the accepted Project Application schema remains the rc06 Draft 2020-12 contract.

The accepted rc07 validator owns machine-determinable representation/source checks including raw-YAML policy, schema conformance, record identity, exact authority/scope uniqueness, canonical ordering, frozen authority proof, authority existence/class resolution, and source-release consistency.

Project-controlled references remain opaque/unresolved at this milestone unless a separately accepted source contract owns them.

The accepted rc08 supported public query API remains:

```python
query_record(repo_root, record_id, project_application_path=None)
query_authority(repo_root, scaf_authority_id, project_application_path=None)
query_scope(repo_root, project_scope_ref, project_application_path=None)
```

These APIs own validation before projection and do not accept caller-supplied parsed records or caller-created validated contexts as substitutes.

## 5. Consolidated Effective Project Profile Contract

An Effective Project Profile remains a subordinate derived current-state projection for exactly one selected non-empty opaque `project_scope_ref` over the complete validated Project-Applicable Obligation domain for the bound SCAF source release.

Accepted profile states remain exactly:

```text
applicable
not_applicable
undetermined
no_current_disposition
```

The distinction remains mandatory:

```text
undetermined
!=
no_current_disposition
```

`undetermined` means a validated current Project Application record exists and explicitly records an unresolved engineering applicability judgment.

`no_current_disposition` means only that no current Project Application record exists for the exact `(scaf_authority_id, project_scope_ref)` pair in the selected validated Project Application snapshot. It is profile-only derived absence and is not a fourth Project Application applicability token.

The complete-domain partition remains:

```text
D = A + N + U + M
```

where `D` is the validated PAO population for the bound source release, not a permanent literal 218 rule.

For the current frozen v0.0.2 authority source:

```text
D = 218
```

but later source releases may have a different validated PAO population.

## 6. Accepted Profile Representation / Validation / Generation Boundary

The accepted rc10 profile representation remains exactly six top-level members:

```text
profile_kind
representation_release
scaf_source_release
project_scope_ref
project_application_source_sha256
entries
```

The accepted profile representation release remains:

```text
representation_release: v0.0.6rc10
```

rc11 formalizes parsed-instance structure/state compatibility without claiming source-aware proof.

rc12 owns the remaining source-aware validation boundary:

```text
profile raw bytes
    ↓ private snapshot
raw-YAML policy
    ↓
rc11 schema
    ↓
canonical ordering

selected Project Application bytes
    ↓ private snapshot
exact SHA-256 comparison
    ↓
accepted rc07 Project Application proof

repository authority + normative sources
    ↓ private validation boundary
frozen source-aware authority proof
    ↓
source-release-bound PAO domain

validated profile + validated Project Application + validated PAO domain
    ↓
complete domain / identity
    ↓
recorded-state exact trace proof
    ↓
no_current_disposition exact-pair absence proof
```

The accepted success wording remains:

```text
PROFILE REPRESENTATION/SOURCE RESULT: PASS
```

It is not an engineering, compliance, verification, release, or closure verdict.

rc13 deterministically generates the accepted rc10 representation from validated Project Application and authority snapshots for one exact scope, then requires the generated bytes to pass rc12 before return/emission.

Generation rule remains exactly:

```text
validated exact-pair current Project Application record exists
    -> copy record.applicability + record.record_id

validated exact pair absent
    -> no_current_disposition
```

No other source may set a generated profile state.

## 7. Source Snapshot / Provenance Boundary

The accepted v0.0.6 executable path uses private captured source boundaries so validation/generation consumes the same source population that was validated.

The profile field:

```text
project_application_source_sha256
```

remains SHA-256 of the exact selected Project Application raw bytes used for derivation/validation.

Its meaning is exact source-snapshot provenance only. It does not establish:

```text
signer identity
project approval
trust authority
engineering correctness
compliance evidence
semantic equivalence across different serializations
```

## 8. Exact-Scope / No-Inference Boundary

At v0.0.6 the project scope remains an opaque exact string.

No accepted v0.0.6 capability provides:

```text
scope registry
scope hierarchy
scope aliasing
scope inheritance
wildcards
parent/child propagation
scope existence proof
scope correctness proof
```

No Project Application or Effective Project Profile state may be inferred from:

```text
L3 trace presence or relation type
Pattern availability
another project scope
scope or reference naming
implementation artifacts
verification/evidence presence
compliance artifacts
previously generated profiles
AI recommendation
```

The L2↔L3 traceability baseline remains navigation/decision support, not project applicability authority.

## 9. Engineering / Authority Separation

The consolidated milestone preserves:

```text
machine-determinable fact
!= engineering judgment
!= Project Design Authority decision
!= implementation result
!= verification result
!= compliance result
!= risk acceptance
!= release readiness
!= closure
```

SCAF may validate representation/source consistency and deterministically project recorded project-side dispositions. It does not determine whether the engineering applicability judgment itself is substantively correct.

## 10. Accepted v0.0.6 Review / Finding Consolidation

The controlled history is consolidated as follows:

```text
rc01  Project Application semantic foundation
      review: PASS / GATE YES
      findings: none

rc02  canonical Project Application logical record model
      review: FAIL / GATE NO
      SCAF-RC02-001 Major opened
      SCAF-RC02-002 Minor opened

rc03  basis-role / state-compatibility hardening
      closes SCAF-RC02-001 / SCAF-RC02-002
      review: PASS / GATE YES

rc04  concrete Project Application YAML representation
      review: PASS with SCAF-RC04-001 Minor fixture-coverage finding

rc05  serialization fixture coverage hardening
      closes SCAF-RC04-001
      review: PASS / GATE YES

rc06  Project Application schema foundation
      review: PASS / GATE YES

rc07  Project Application source-aware validator
      review: PASS / GATE YES

rc08  validated Project Application read/query views
      review: PASS / GATE YES

rc09  Effective Project Profile semantic foundation
      review: PASS / GATE YES

rc10  canonical Effective Project Profile representation
      review: PASS / GATE YES

rc11  Effective Project Profile schema foundation
      review: PASS / GATE YES

rc12  Effective Project Profile source-aware validator
      review: PASS / GATE YES

rc13  deterministic Effective Project Profile generator
      review: PASS / GATE YES
```

No accepted Critical, Major, Minor, or Trivial finding remains open at the rc14 entry point.

## 11. Regression Baseline

The accepted v0.0.6 executable regression inventory is:

```text
Project Application validator suite:          21
Project Application validated views suite:    22
Effective Project Profile validator suite:    30
Effective Project Profile generator suite:    25
                                              ---
v0.0.6 executable development suites:         98
```

The frozen v0.0.4 / v0.0.5 regression inventory remains:

```text
frozen executable-governance suites:          41
frozen trace-validator suite:                  24
frozen trace-view/query suite:                 28
                                              ---
frozen executable regression suites:          93
```

Combined current repository regression inventory covered by the rc14 milestone review:

```text
98 + 93 = 191 tests
```

In addition, the accepted production validation commands must remain green:

```text
python -m tools.scaf_validator.validator
python -m tools.scaf_trace_validator.validator
python -m tools.scaf_release_integrity.checker
python -m tools.scaf_project_application_validator.validator
python -m tools.scaf_effective_project_profile_validator.validator
```

and deterministic profile generation for the accepted illustrative source must continue to produce rc12-valid canonical output.

A regression-count reduction, unexpected skip, or changed accepted behavior is not authorized by rc14.

## 12. Freeze-Candidate Non-Regression Rule

rc14 is consolidation-only. Relative to committed rc13 it shall change only milestone/navigation documentation.

It shall not change:

- frozen v0.0.2 normative source;
- frozen v0.0.3 L3 source;
- frozen v0.0.4 executable-governance implementation/trust artifacts;
- frozen v0.0.5 machine-readable traceability artifacts;
- `authority-registry.yaml` or its schema;
- `l3-trace-registry.yaml` or its schema;
- Project Application fixture/schema/validator/views;
- Effective Project Profile fixture/schema/validator/generator;
- release-integrity, external-pin, or CI-gate implementation;
- GitHub Actions workflow behavior;
- accepted regression test source/inventory;
- historical controlled records rc01→rc13.

Expected rc13→rc14 source delta:

```text
Added:   1
Changed: 3
Removed: 0
```

Expected added file:

```text
docs/executable-governance/38_SCAF_v0.0.6rc14_Project_Application_Effective_Project_Profile_Milestone_Consolidation_and_Freeze_Candidate.md
```

Expected changed files:

```text
README.md
CHANGELOG.md
docs/executable-governance/README.md
```

## 13. Explicitly Deferred Beyond This Freeze Candidate

The v0.0.6 milestone does not claim completion of:

- project-scope registry, hierarchy, aliasing, inheritance, or resolver;
- project-controlled reference resolution;
- Project Application history, supersession, or re-evaluation serialization;
- persistent/generated Effective Project Profile registry/cache/history;
- automatic applicability inference;
- AI approval of engineering rationale;
- Project Design Authority automation;
- Pattern recommendation or automatic selection;
- AI context packaging / context assembly from the Effective Project Profile;
- CI applicability-completion enforcement;
- implementation/satisfaction/compliance determination;
- verification/evidence/closure determination;
- requirements-to-test closure beyond existing accepted traceability boundaries;
- profile-driven code generation;
- architecture/dependency enforcement beyond accepted frozen controls;
- new L3 Pattern tranche, M3/M4, or L4 guidance;
- Development Context Recovery / `.scaf/work-checkpoint.yaml`;
- expansion of the frozen repository-external trust model.

Deferred work is not an rc14 defect merely because it is not implemented.

## 14. Milestone Acceptance Criteria

Independent rc14 review shall confirm at least:

1. rc01→rc13 history and finding disposition are accurately consolidated.
2. No accepted Critical/Major/Minor/Trivial finding remains open.
3. committed predecessor is exactly rc13 `88b793c34c2090c9bd4d4b8053ded1ec6d892573`.
4. rc13→rc14 source delta is exactly 1 Added / 3 Changed / 0 Removed.
5. rc14 is documentation/navigation-only and introduces no semantic or executable capability.
6. frozen v0.0.2/v0.0.3/v0.0.4/v0.0.5 protected inputs remain unchanged.
7. Project Application representation/schema/validator/views remain unchanged.
8. Effective Project Profile representation/schema/validator/generator remain unchanged.
9. authority inventory remains 294 / 218 / 76.
10. L3 trace inventory remains 12 Patterns / 119 relations.
11. Project Application validator suite remains 21/21 with no unexpected skips.
12. Project Application views suite remains 22/22 with no unexpected skips.
13. Effective Project Profile validator suite remains 30/30 with no unexpected skips.
14. Effective Project Profile generator suite remains 25/25 with no unexpected skips.
15. frozen v0.0.4 executable-governance suites remain 41/41.
16. frozen trace-validator suite remains 24/24.
17. frozen trace-view/query suite remains 28/28.
18. accepted production validators/integrity checks remain PASS.
19. deterministic generator output remains accepted rc10 representation and passes accepted rc12 validation.
20. `undetermined` remains distinct from `no_current_disposition`.
21. `no_current_disposition` remains exact-pair dataset-relative absence only.
22. exact-scope resolution neutrality and no-inference boundaries remain intact.
23. Project Design Authority / engineering / compliance / verification / closure authority remains outside machine-generated profile state.
24. README, CHANGELOG, executable-governance navigation, and rc14 record consistently identify rc14 as a **freeze candidate**, not a formal frozen release.
25. deferred work is clearly bounded and not falsely represented as complete.

## 15. Formal Freeze Rule

A clean independent rc14 gate establishes **freeze-candidate eligibility only**.

It does not by itself authorize:

- changing the formal release from v0.0.5 to v0.0.6;
- marking v0.0.6 as frozen;
- modifying the reviewed rc14 candidate in place after review;
- treating deferred context/CI/L4 work as accepted milestone content;
- advancing to a new capability line without a separate development decision.

Formal freeze requires a separate explicit governance decision after the independent review.

The intended formal milestone name, if that explicit decision is made, is:

```text
SCAF v0.0.6 — Frozen Machine-Readable Project Application and Effective Project Profile Baseline
```

## 16. Freeze-Candidate Gate

Expected independent review label:

```text
V0.0.6 PROJECT APPLICATION / EFFECTIVE PROJECT PROFILE MILESTONE CONSOLIDATION / FREEZE-CANDIDATE GATE
```
