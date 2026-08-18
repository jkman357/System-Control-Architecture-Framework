# SCAF v0.0.5 — Formal Freeze Decision

**Date:** 2026-08-18  
**Status:** Frozen L3 Machine-Readable Traceability Baseline  
**Freeze Source:** `v0.0.5rc10`  
**Freeze-Candidate Review:** `V0.0.5 L3 MACHINE-READABLE TRACEABILITY MILESTONE CONSOLIDATION / FREEZE-CANDIDATE GATE: YES`

## 1. Explicit Governance Decision

The reviewed `v0.0.5rc10` source state is formally frozen as:

```text
SCAF v0.0.5 — Frozen L3 Machine-Readable Traceability Baseline
```

This decision is explicit and separate from the rc10 freeze-candidate review. rc10 established freeze eligibility; this record creates the formal immutable baseline.

No semantic or executable capability is added by the freeze itself. Relative to rc10, the formal release changes only release-state/navigation documentation and adds this freeze-decision record.

## 2. Freeze-Candidate Evidence

The independent rc10 review reported:

```text
Critical: 0
Major:    0
Minor:    0
Trivial:  0

V0.0.5 L3 MACHINE-READABLE TRACEABILITY MILESTONE CONSOLIDATION / FREEZE-CANDIDATE GATE: YES
```

The review independently confirmed the rc9→rc10 delta was consolidation-only (`1 Added / 3 Changed / 0 Removed`), frozen upstream identities remained exact, required validators passed, development regressions remained green, and no deferred capability was introduced.

## 3. Frozen Machine-Readable Traceability Inventory

The formal baseline freezes exactly:

```text
Patterns:                  12
Relations:                119
Primary:                   23
Supporting:                41
Constraint:                55
Unique referenced L2 IDs:  82
Qualifier-bearing:         15
```

The controlled relation vocabulary remains exactly:

```text
primary_realization_candidate
supporting_realization
constraint_input
```

Every accepted relation preserves the seven-field representation:

```text
pattern_id
relation_type
l2_id
pattern_source_path
pattern_source_field
source_release
qualifier
```

## 4. Frozen Authority and Upstream Source Boundaries

The frozen v0.0.2 L1/L2 authority inventory remains:

```text
294 total authority records
218 Project-Applicable Obligations
76 Framework Normative Invariants
```

Protected source identities remain:

```text
docs/normative/
11 files
aggregate SHA-256:
86ca06dbb586b8e0f47c8efbe731635633484bf58de2ddd3e90639a42090775f
```

```text
docs/l3/
30 files
aggregate SHA-256:
eddb26826ce83d7a9aae028cf3c4f7f630b304c41e3bcbbfe8f00e51d3248eeb
```

The v0.0.5 freeze does not reopen or redefine the frozen v0.0.2, v0.0.3, or v0.0.4 baselines.

## 5. Frozen Validation and Query Boundary

The source-aware trace proof remains owned by:

```text
tools.scaf_trace_validator.validator.validate_repository(repo_root)
```

The supported public trace-query API remains:

```python
from tools.scaf_trace_views import query_l2, query_pattern
```

Every supported query preserves the same-root validation-owning sequence:

```text
resolve repository root
        ↓
source-aware trace validation
        ↓ PASS only
frozen authority-registry validation
        ↓ PASS only
load validated repository state
        ↓
deterministic in-memory projection
        ↓
view return
```

No caller-supplied validated context, public direct builder, alternate authority root, or weaker CLI-only path is authorized by the frozen baseline.

## 6. Frozen Projection Semantics

The baseline freezes:

- deterministic L2 → L3 trace views for known Project-Applicable authority identities;
- deterministic L3 Pattern → L2 trace views for known frozen Pattern identities;
- exact 119-relation coverage in both directions;
- relation-type and qualifier fidelity;
- deterministic ordering and JSON;
- valid zero-relation results for accepted Project-Applicable identities with no current L3 relation;
- Framework Normative Invariants outside the current Project-Applicable L2 query domain;
- read-only in-memory projection with no persisted generated index.

The frozen non-equivalence is:

```text
Queried / Traced / Serialized / Trace-source-validated / Authority-source-validated
!= Applicable
!= Recommended
!= Selected
!= Satisfied
!= Compliant
!= Verified
!= Closed
```

## 7. Frozen Regression Baseline

The accepted development regressions at freeze are:

```text
source-aware trace-validator suite: 24 / 24 PASS
trace-view/query suite:             28 / 28 PASS
```

The inherited frozen v0.0.4 executable-governance inventory remains:

```text
scaf_validator           8 / 8 PASS
scaf_release_integrity   9 / 9 PASS
scaf_external_pin       11 / 11 PASS
scaf_ci_gate            13 / 13 PASS
----------------------------------
Total                   41 / 41 PASS
```

A later change that reduces these inventories, introduces unexpected skips, or changes accepted behavior belongs to a new controlled development line and does not modify v0.0.5 in place.

## 8. Production Trust Boundary

The frozen v0.0.4 six-artifact production trust set and repository-external trust-input model remain unchanged. v0.0.5 does not add trace-view or trace-validator artifacts to that trust set.

The rc10 independent review did not execute the production external-trust gate because the required repository-external trust bundle was unavailable. Therefore:

```text
Production external-trust gate execution: NOT INDEPENDENTLY VERIFIED
```

The formal v0.0.5 freeze does not convert that limitation into a production PASS and does not treat the missing external input as a source defect.

## 9. Explicitly Deferred / Not Authorized by v0.0.5

The freeze does not claim completion or authorization of:

- L4 implementation / verification guidance;
- new L3 Pattern work, M3, or M4;
- project-applicability inference;
- Pattern recommendation or automatic selection;
- requirement satisfaction/compliance/verification/closure inference;
- persisted/generated forward or reverse indexes;
- automatic trace-registry generation or rewrite;
- generated authority indexes/views;
- code generation;
- architecture/dependency enforcement beyond accepted existing controls;
- requirements-to-test traceability beyond the frozen L2↔L3 trace milestone;
- fork/privileged-PR enforcement;
- signing, PKI, provenance, attestation, or trust-bundle distribution expansion.

In particular, v0.0.5 does not authorize a validator to equate absence of a mechanism with project failure without a controlled applicability basis. Applicability, tailoring, project design authority, rationale, evidence, and closure remain separate project-governance concerns.

## 10. Post-Freeze Governance

`v0.0.5` is immutable as a formal frozen baseline and shall not be modified or respun in place.

Future capability work must start on a new controlled RC/version line, preserve traceability to the frozen v0.0.2 / v0.0.3 / v0.0.4 / v0.0.5 baselines, and explicitly justify any later evolution of authority, applicability, traceability, validation, project-decision, or implementation-guidance behavior.
