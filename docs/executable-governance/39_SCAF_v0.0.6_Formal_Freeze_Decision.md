# SCAF v0.0.6 — Formal Freeze Decision

**Date:** 2026-08-18  
**Status:** Frozen Machine-Readable Project Application and Effective Project Profile Baseline  
**Freeze Source:** `v0.0.6rc14`  
**Freeze Source Commit:** `9484d4dd771606a4277a326eb7a7ec961feb5ea1`  
**Freeze-Candidate Review:** `V0.0.6 PROJECT APPLICATION / EFFECTIVE PROJECT PROFILE MILESTONE CONSOLIDATION / FREEZE-CANDIDATE GATE: YES`

## 1. Explicit Governance Decision

The reviewed `v0.0.6rc14` source state is formally frozen as:

```text
SCAF v0.0.6 — Frozen Machine-Readable Project Application and Effective Project Profile Baseline
```

This decision is explicit and separate from the rc14 freeze-candidate review. rc14 established freeze eligibility; this record creates the formal immutable baseline.

No semantic or executable capability is added by the freeze itself. Relative to committed rc14, the formal release changes only release-state/navigation documentation and adds this freeze-decision record.

## 2. Freeze-Candidate Evidence

The independent rc14 review reported:

```text
Critical: 0
Major:    0
Minor:    0
Trivial:  0

V0.0.6 PROJECT APPLICATION / EFFECTIVE PROJECT PROFILE
MILESTONE CONSOLIDATION / FREEZE-CANDIDATE GATE: YES
```

The review independently confirmed:

```text
v0.0.6 executable-development suites: 98 / 98 PASS
frozen regression suites:             93 / 93 PASS
combined review-covered inventory:    191 / 191 PASS
```

It also confirmed that rc14 was documentation/navigation-only, all accepted findings were closed, the Project Application and Effective Project Profile boundaries remained unchanged, required production validators/integrity checks passed, and deterministic rc13 generation remained accepted by rc12 source-aware validation.

## 3. Frozen Upstream Authority Context

The formal v0.0.6 baseline remains subordinate to the already frozen upstream baselines:

```text
v0.0.2 — L1/L2 normative authority
v0.0.3 — L3 Pattern / Mechanism Catalog
v0.0.4 — Executable Governance
v0.0.5 — L3 Machine-Readable Traceability
```

The frozen authority inventory remains:

```text
Authority records:                 294
Project-Applicable Obligations:    218
Framework Normative Invariants:     76
```

The frozen L3 machine-readable traceability inventory remains:

```text
Patterns:    12
Relations:  119
```

v0.0.6 does not reopen or redefine those frozen upstream baselines.

## 4. Frozen Project Application Contract

The v0.0.6 baseline freezes machine-readable project-side disposition for one exact SCAF Project-Applicable Obligation and one exact opaque project scope.

Accepted Project Application applicability tokens remain exactly:

```text
applicable
not_applicable
undetermined
```

`undetermined` remains a legitimate explicit engineering-unresolved state. It is not representation failure, project failure, non-compliance, verification failure, or closure failure.

The accepted concrete Project Application representation remains:

```text
representation_release: v0.0.6rc04
```

The accepted parsed-instance schema remains the rc06 Draft 2020-12 contract.

The accepted rc07 representation/source-aware validator remains responsible for machine-determinable Project Application checks, including raw-YAML policy, schema conformance, current-record identity, exact authority/scope uniqueness, canonical ordering, frozen authority proof, authority target resolution, and source-release consistency.

Project-controlled references remain opaque unless a separately accepted source contract owns their resolution.

## 5. Frozen Project Application Query Boundary

The supported validation-owning rc08 Project Application query API remains:

```python
query_record(repo_root, record_id, project_application_path=None)
query_authority(repo_root, scaf_authority_id, project_application_path=None)
query_scope(repo_root, project_scope_ref, project_application_path=None)
```

Supported queries validate before projection and do not accept caller-supplied parsed records, caller-built indexes, caller-created validation reports, or caller-created validated contexts as substitutes for accepted validation.

Query results remain read-only deterministic project-state views. They do not create or replace engineering applicability authority.

## 6. Frozen Effective Project Profile Semantics

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

`undetermined` means a validated current Project Application record exists and explicitly records an unresolved engineering applicability state.

`no_current_disposition` means only that no current Project Application record exists for the exact `(scaf_authority_id, project_scope_ref)` pair in the selected validated Project Application snapshot.

`no_current_disposition` is profile-only derived absence. It is not a fourth Project Application applicability token and does not mean `not_applicable`, scope nonexistence, failure, non-compliance, or closure.

The complete-domain partition remains:

```text
D = A + N + U + M
```

where `D` is the validated source-release-bound PAO population. The current frozen v0.0.2 population is 218 PAOs, but 218 is not a permanent cross-release representation rule.

## 7. Frozen Profile Representation and Source-Aware Validation

The accepted rc10 Effective Project Profile representation remains exactly six top-level members:

```text
profile_kind
representation_release
scaf_source_release
project_scope_ref
project_application_source_sha256
entries
```

The accepted representation release remains:

```text
representation_release: v0.0.6rc10
```

The accepted rc11 Draft 2020-12 schema owns parsed-instance structure and state compatibility.

The accepted rc12 validator owns the remaining machine-determinable representation/source boundary, including:

```text
raw-YAML policy
profile schema validation
canonical ordering
exact Project Application source SHA-256 correspondence
accepted rc07 Project Application proof
frozen authority/source proof
source-release-bound complete PAO domain
cross-entry authority identity
recorded-state exact trace correspondence
no_current_disposition exact-pair absence proof
```

The accepted success wording remains:

```text
PROFILE REPRESENTATION/SOURCE RESULT: PASS
```

That result is not an engineering, Project Design Authority, compliance, verification, risk, release, or closure verdict.

## 8. Frozen Deterministic Generation Boundary

The accepted rc13 generator deterministically constructs the accepted rc10 profile representation from validated Project Application and validated authority snapshots for one exact project scope.

Generation remains exactly:

```text
validated exact-pair current Project Application record exists
    -> copy record.applicability + record.record_id

validated exact pair absent
    -> no_current_disposition
```

No L3 trace, Pattern availability, other scope, implementation artifact, evidence artifact, compliance artifact, previous profile, naming convention, or AI recommendation may set a generated profile state.

The generator remains validation-owning, source-snapshot-bound, deterministic, non-persistent, and read-only toward controlled sources.

Every supported generated profile must pass accepted rc12 source-aware validation before successful return or CLI emission.

## 9. Exact-Scope and No-Inference Boundary

The v0.0.6 baseline freezes `project_scope_ref` as an exact opaque non-empty string for Project Application query/profile semantics.

v0.0.6 introduces no:

```text
scope registry
scope hierarchy
scope aliasing
scope inheritance
wildcard scope matching
parent/child carryover
scope existence proof
scope correctness proof
```

Likewise, Project Application or Effective Project Profile state is not inferred from:

```text
L3 trace presence or relation type
Pattern availability
another project scope
implementation artifacts
verification/evidence artifacts
compliance artifacts
scope/reference naming
AI recommendation
```

## 10. Frozen Regression Baseline

The accepted v0.0.6 executable-development regression inventory at freeze is:

```text
Project Application validator tests:       21 / 21 PASS
Project Application view/query tests:      22 / 22 PASS
Effective Project Profile validator tests: 30 / 30 PASS
Effective Project Profile generator tests: 25 / 25 PASS
-----------------------------------------
Total:                                     98 / 98 PASS
```

The inherited frozen regression inventory remains:

```text
v0.0.4 executable-governance suites: 41 / 41 PASS
v0.0.5 trace-validator suite:         24 / 24 PASS
v0.0.5 trace-view/query suite:        28 / 28 PASS
------------------------------------
Frozen total:                         93 / 93 PASS
```

Combined review-covered inventory at freeze:

```text
191 / 191 PASS
```

A later change that reduces these inventories, introduces unexpected skips, or changes accepted behavior belongs to a new controlled development line and does not modify v0.0.6 in place.

## 11. Production Validation State

At freeze-candidate review, the required repository production checks remained green:

```text
Authority validation:                 PASS
L3 trace validation:                  PASS
Frozen release integrity:             PASS
Project Application validation:       PASS
Effective Project Profile validation: PASS
rc13 generation -> rc12 validation:   PASS
```

The repository-external production trust bundle was not separately supplied to the rc14 independent review. Therefore:

```text
Actual production external-trust execution: NOT INDEPENDENTLY VERIFIED
```

The formal v0.0.6 freeze does not convert that limitation into a production PASS and does not treat the unavailable external input as a v0.0.6 source defect.

## 12. Engineering / Authority Separation

The frozen baseline preserves:

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

Machine-readable Project Application, deterministic query, Effective Project Profile projection, source-aware validation, and deterministic generation remain subordinate engineering-governance mechanisms.

They do not decide whether an applicability rationale is substantively correct, whether a project design is adequate, whether verification evidence is sufficient, or whether a project is complete or ready for release.

## 13. Explicitly Deferred / Not Authorized by v0.0.6

The formal v0.0.6 baseline does not claim completion or authorization of:

- project-scope/reference resolution;
- Project Application history, supersession, or re-evaluation models;
- persistent Effective Project Profile registry/cache/history;
- automatic applicability inference;
- AI approval of engineering rationale;
- Project Design Authority automation;
- Pattern recommendation or automatic selection;
- AI context packaging / context assembly;
- CI applicability-completion enforcement;
- implementation/compliance/verification/closure determination;
- profile-driven code generation;
- new L3 tranche work, M3, or M4;
- L4 implementation / verification guidance;
- Development Context Recovery / `.scaf/work-checkpoint.yaml`;
- expansion of the frozen external-trust model.

These are future-version concerns and are not defects merely because they are absent from v0.0.6.

## 14. Post-Freeze Governance

`v0.0.6` is immutable as a formal frozen baseline and shall not be modified or respun in place.

Future capability work must begin on a new controlled RC/version line and preserve traceability to the frozen v0.0.2 / v0.0.3 / v0.0.4 / v0.0.5 / v0.0.6 baselines.

Any later evolution of applicability, project-scope semantics, Project Application records, Effective Project Profile semantics, validation, generation, context consumption, project authority, compliance, verification, or implementation guidance must be introduced explicitly and reviewed as new controlled work.
