# SCAF v0.0.7 — Formal Freeze Decision

**Date:** 2026-08-19  
**Status:** Frozen Consumption Selection Baseline  
**Freeze Source:** `v0.0.7rc07`  
**Freeze Source Commit:** `353d056d76fad99b4da7928dec07a3aab9b944d7`  
**Freeze-Candidate Review:** `V0.0.7 CONSUMPTION SELECTION MILESTONE CONSOLIDATION / FREEZE-CANDIDATE GATE: YES`

## 1. Explicit Governance Decision

The independently reviewed `v0.0.7rc07` source state is formally frozen as:

```text
SCAF v0.0.7 — Frozen Consumption Selection Baseline
```

This governance decision is explicit and separate from the rc07 freeze-candidate review. The rc07 review established freeze eligibility; this record creates the formal immutable v0.0.7 baseline.

No semantic or executable capability is added by the freeze itself. Relative to committed rc07, the formal release changes only release-state/navigation documentation and adds this freeze-decision record.

## 2. Freeze-Candidate Evidence

The independent rc07 review reported:

```text
Critical: 0
Major:    0
Minor:    0
Trivial:  0

V0.0.7 CONSUMPTION SELECTION MILESTONE
CONSOLIDATION / FREEZE-CANDIDATE GATE: YES
```

The review independently confirmed:

```text
rc06 Consumption Selection builder:  34 / 34 PASS
rc05 Consumption Selection validator: 37 / 37 PASS
inherited accepted/frozen baseline:   191 / 191 PASS
current review execution inventory:   262 tests PASS
unexpected skips:                       0
```

The historical inherited/frozen baseline remains 191; 262 is the current v0.0.7 milestone review execution inventory, not a redefinition of that historical baseline.

The review also confirmed repository-owned production validation/integrity PASS, fixture-equivalent deterministic Consumption Selection generation and rc05 validation PASS, fresh frozen Effective Project Profile generation and rc12 validation PASS, exact package/Git lineage, and no accepted open findings.

## 3. Frozen Upstream Context

The v0.0.7 baseline remains subordinate to the already frozen baselines:

```text
v0.0.2 — L1/L2 normative authority
v0.0.3 — L3 Pattern / Mechanism Catalog
v0.0.4 — Executable Governance
v0.0.5 — L3 Machine-Readable Traceability
v0.0.6 — Machine-Readable Project Application / Effective Project Profile
```

The frozen source inventories remain:

```text
Authority records:                 294
Project-Applicable Obligations:    218
Framework Normative Invariants:     76
L3 Patterns:                        12
L3 Relations:                      119
```

v0.0.7 does not reopen or redefine those upstream frozen authorities.

## 4. Frozen Consumption Semantic Boundary

The accepted consumption distinctions are frozen unchanged:

```text
included in context != applicable
excluded from context != not_applicable
omitted != not_applicable
predicate excluded != bounded omitted
undetermined != no_current_disposition
```

The Effective Project Profile state vocabulary remains exactly:

```text
applicable
not_applicable
undetermined
no_current_disposition
```

No fifth state is introduced by inclusion, omission, predicate exclusion, validation, or complete/filtered classification.

Consumption Selection remains subordinate to validated Effective Project Profile and upstream Project Application truth. It does not create applicability, implementation, compliance, verification, risk, release, closure, or Project Design Authority truth.

## 5. Frozen Canonical Set Model

The accepted set model is frozen as:

```text
D = complete validated source-profile domain
E = predicate-eligible set
I = included set
O = predicate-eligible but bounded-omitted set
X = predicate-excluded set

E = I + O
D = I + O + X
```

`I`, `O`, and `X` remain mutually disjoint.

Eligibility remains exactly:

```text
entry.profile_state in state_selector
AND
entry.scaf_authority_id satisfies authority_selector
```

No arbitrary predicate language, semantic similarity, Pattern inference, file-presence inference, scope relation, ranking, token-budget rule, or AI classifier is part of the frozen eligibility model.

## 6. Frozen Representation and Schema

The accepted Consumption Selection serialized representation remains:

```text
selection_kind: consumption_selection
representation_release: v0.0.7rc03
```

The canonical top-level representation remains exactly nine members:

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

The accepted JSON Schema remains Draft 2020-12 with:

```text
$id = urn:scaf:schema:consumption-selection:v0.0.7rc04
```

The schema owns parsed-instance structure/state-shape constraints only. It does not by itself prove source validity, provenance correspondence, authority-domain membership, set reconstruction, selected-entry source fidelity, complete/filtered derivation, physical raw-YAML policy, or engineering correctness.

## 7. Frozen Source-Profile Provenance and Scope

Every supported Consumption Selection remains bound to one exact validated Effective Project Profile snapshot through:

```text
effective_project_profile_source_sha256
scaf_source_release
project_scope_ref
project_application_source_sha256
```

These values remain provenance facts only. They are not signer identity, trust approval, engineering correctness, compliance, verification, release readiness, or closure.

`project_scope_ref` remains an exact opaque non-empty string inherited from the validated source profile. v0.0.7 introduces no scope hierarchy, aliasing, inheritance, wildcard match, parent/child propagation, cross-scope carryover, scope resolver, scope-existence proof, or scope-correctness proof.

## 8. Frozen Source-Aware Validator Boundary

The accepted validation-owning public API remains:

```python
validate_consumption_selection(
    repo_root,
    selection_path=None,
    profile_path=None,
    project_application_path=None,
)
```

The supported production CLI remains limited to project-side source selection:

```text
--selection
--profile
--project-application
```

The validator owns the source-aware proof chain:

```text
Consumption Selection bytes
        ↓
raw-YAML / canonical policy
        ↓
accepted rc04 schema
        ↓
exact bound Effective Project Profile bytes
        ↓
frozen v0.0.6 source-aware profile validation
        ↓
exact SHA / provenance proof
        ↓
selector/domain resolution
        ↓
selected-entry source fidelity
        ↓
D/E/I/O/X reconstruction
        ↓
bounded-omission consistency
        ↓
complete/filtered derivation proof
```

The accepted success wording remains:

```text
CONSUMPTION SELECTION REPRESENTATION/SOURCE RESULT: PASS
```

That PASS is machine-determinable representation/source/selection consistency only.

## 9. Frozen Deterministic Builder Boundary

The accepted builder API remains:

```python
build_consumption_selection(
    repo_root,
    selection_purpose,
    state_selector=(),
    *,
    authority_mode="all_domain",
    authority_ids=(),
    omitted_authority_ids=(),
    omission_basis=None,
    profile_path=None,
    project_application_path=None,
) -> bytes
```

The builder remains validation-first and deterministic. It consumes source-profile state only after accepted frozen source-aware Effective Project Profile validation. It constructs only the accepted rc03 representation and requires accepted rc05 self-validation before successful return or CLI emission.

Bounded omission remains exact caller-declared eligible authority IDs. The builder introduces no ranking, priority, severity, token-budget calculation, semantic matching, Pattern inference, scope inference, or AI selection algorithm.

The accepted equality case remains valid:

```text
bounded_omission.applied = true
O = empty
```

## 10. Project Application Truth and Engineering Authority Separation

Selected recorded entries remain a trace projection only:

```text
scaf_authority_id
profile_state
project_application_record_id
```

For `no_current_disposition`, `project_application_record_id` remains absent.

Authoritative Project Application rationale/provenance remains upstream and is not duplicated into Consumption Selection as competing truth.

The frozen authority separation remains:

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

## 11. Frozen Deterministic Evidence

The accepted fixture-equivalent Consumption Selection deterministic output remains:

```text
SHA-256:
e23531f2e8b3ae8052cf5cbf5b3e80115ef53837a0831afbc2fe160a982dbdc2
```

It is byte-identical to the accepted rc03 fixture after removing only leading non-authoritative comments/blanks and passes accepted rc05 validation with:

```text
D = 218
E = 3
I = 2
O = 1
X = 215
O = { SCAF-AK-003 }
Errors = 0
```

The inherited frozen Effective Project Profile deterministic output remains:

```text
SHA-256:
6f6485077022f3686064876b0891ff45c6f4e4f69a81ab4bb557d6b7a09c3433

representation_release: v0.0.6rc10
entries: 218
applicable: 1
not_applicable: 0
undetermined: 0
no_current_disposition: 217
```

and remains accepted by the frozen rc12 source-aware profile validator.

These fixture counts are current accepted source observations; they are not permanent cross-release domain-size representation rules.

## 12. Frozen Regression Position

The v0.0.7 milestone executable regression inventory at freeze is:

```text
Consumption Selection builder:    34 / 34 PASS
Consumption Selection validator:  37 / 37 PASS
inherited accepted/frozen:       191 / 191 PASS
                                  ---------------
current milestone inventory:      262 tests PASS
```

The historical inherited/frozen 191-test baseline remains separately identified and unchanged.

## 13. Explicitly Deferred Capabilities

The following remain outside formal v0.0.7 and require a new separately reviewed version line if pursued:

```text
PAO-to-file/document/context-source resolution
context-content records
AI context package
AI prompt format
AI orchestration / model selection
semantic-similarity context selection
ranking / priority / severity policy
token-budget calculation or automated truncation policy
scope/reference resolver
scope hierarchy / aliases / inheritance
profile history / supersession
Consumption Selection history / persistent registry / cache
automatic applicability inference
Pattern recommendation / selection
AI approval / Project Design Authority automation
CI applicability-completion enforcement
implementation/compliance/verification/closure determination
profile-driven code generation
new L3 tranche / M3 / M4
L4 implementation / verification guidance
Development Context Recovery / .scaf/work-checkpoint.yaml
external-trust-model expansion
```

Their absence is intentional and is not a gap in the frozen v0.0.7 scope.

## 14. Immutability Rule

Formal `v0.0.7` is immutable. Future work shall not modify or respin the frozen v0.0.7 baseline in place.

Any later change to Consumption Selection semantics, representation, schema, source-aware validation, deterministic construction, or any deferred context-source/AI capability requires a new controlled version line with its own dependency/value decision and independent review.

## 15. Formal Freeze Effect

The formal release action is deliberately narrow:

```text
reviewed rc07 source state
        +
explicit governance freeze decision
        ↓
SCAF v0.0.7 — Frozen Consumption Selection Baseline
```

No semantic, executable, authority, representation, schema, validator, builder, workflow, trust-boundary, or frozen-source behavior is changed by the freeze itself.
