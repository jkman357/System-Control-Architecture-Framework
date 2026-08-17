# SCAF v0.0.4rc12 — Executable Governance Milestone Consolidation and Freeze Candidate

**Release:** v0.0.4rc12  
**Status:** Milestone Consolidation / Freeze Candidate RC  
**Date:** 2026-08-17

## 1. Purpose

v0.0.4rc12 is a **consolidation-only freeze candidate** for the v0.0.4 executable-governance milestone.

It adds no new executable-governance capability. Its purpose is to make the accepted rc01→rc11 development sequence, current executable control chain, frozen/non-frozen boundary, accepted review history, regression inventory, trust limitations, and deferred scope auditable from one current-state record before any formal v0.0.4 freeze decision.

Formal freeze is **not** performed by this RC. A formal `v0.0.4` baseline may be created only after an independent freeze-candidate review returns an acceptable gate and an explicit governance freeze decision is made.

## 2. Upstream Acceptance Basis

The independent v0.0.4rc11 review returned:

```text
R10-01: RESOLVED
V0.0.4 CI REPOSITORY PATH-COMPONENT / ROOT-BINDING HARDENING GATE: YES
```

It opened no Critical, Major, Minor, or Trivial findings and independently reproduced closure of both rc10 shadow-repository false-PASS paths.

The v0.0.4 milestone therefore enters rc12 with no open accepted review finding from rc01→rc11.

## 3. Milestone Evolution

| RC | Controlled milestone step | Independent review disposition |
|---|---|---|
| rc01 | Machine-readable authority-model foundation | `YES, AFTER MINOR CLEANUP`; opened `R1-01` Minor |
| rc02 | Authority-model determinism cleanup | `YES`; `R1-01` resolved |
| rc03 | Initial 294-record authority-registry serialization | `YES, AFTER MINOR CLEANUP`; opened `R3-01` Minor |
| rc04 | Authority-registry release-state documentation cleanup | `YES`; `R3-01` resolved |
| rc05 | Authority-registry schema and structural/source-aware validator foundation | `YES, AFTER MINOR CLEANUP`; opened `R5-01` Minor |
| rc06 | Canonical-schema binding and validator CLI hardening | `YES`; `R5-01` resolved |
| rc07 | Frozen-baseline release-integrity foundation | `YES`; opened only non-blocking `R7-01` / `R7-02` Trivial findings |
| rc08 | Release-integrity diagnostic cleanup and external-pinning foundation | `YES, AFTER MINOR CLEANUP`; `R7-01` / `R7-02` resolved; opened `R8-01` Minor |
| rc09 | External-pin local-artifact symlink hardening | `YES`; `R8-01` resolved |
| rc10 | CI trust-input model and executable-governance gate foundation | `NO`; opened `R10-01` Major |
| rc11 | CI repository path-component and root-binding hardening | `YES`; `R10-01` resolved |
| rc12 | Milestone consolidation / freeze candidate | current review target |

The rc10 `NO` result is retained explicitly as part of the release history. rc12 does not rewrite or hide failed intermediate review state; it records the rc11 closure that made the current candidate eligible for final consolidation review.

## 4. Current Executable-Governance Control Chain

The current v0.0.4 candidate control chain is:

```text
Frozen v0.0.2 normative Markdown semantic authority
        ↓
authority-registry.yaml
        ↓
canonical authority-registry JSON Schema
        ↓
semantic / structural / source-aware validator
        ↓
frozen v0.0.2 + v0.0.3 byte-integrity manifest
        ↓
standalone release-integrity checker
        ↓
external identity pin verification
        ↓
external CI trust bundle
        ↓
CI gate bootstrap / six-artifact identity validation
        ↓
fixed three-stage executable-governance gate
        ↓
path-component + repository-root binding / stage-root attestation
```

The three executable control domains remain separate:

```text
tools.scaf_validator.validator
    -> semantic / representation / canonical-source consistency

tools.scaf_release_integrity.checker
    -> frozen source byte identity against the canonical local manifest

tools.scaf_external_pin.checker
    -> local manifest / release-integrity-checker identity against external trust input
```

`tools.scaf_ci_gate.gate` is an enforcement orchestrator over those accepted controls. It is not semantic authority.

## 5. Frozen Semantic Baselines Carried Into v0.0.4

### 5.1 Frozen v0.0.2 L1/L2 baseline

The candidate preserves:

```text
294 normative requirement IDs
218 Project-Applicable Obligations
76 Framework Normative Invariants
```

`docs/normative/` contains exactly 11 protected files with accepted aggregate SHA-256:

```text
86ca06dbb586b8e0f47c8efbe731635633484bf58de2ddd3e90639a42090775f
```

### 5.2 Frozen v0.0.3 L3 baseline

The candidate preserves:

```text
12 published SCAF-PAT-* identities
12 / 12 Catalog Status = Available
12 / 12 Maturity = M2 — Architecture Reviewed
```

`docs/l3/` contains exactly 30 protected files with accepted aggregate SHA-256:

```text
eddb26826ce83d7a9aae028cf3c4f7f630b304c41e3bcbbfe8f00e51d3248eeb
```

`Available / M2` remains catalog lifecycle state only. It does not imply project applicability, recommendation, automatic selection, satisfaction, compliance, verification, evidence sufficiency, or closure.

## 6. Machine-Readable Authority Candidate State

`authority-registry.yaml` remains the accepted rc03 controlled-curated representation of the frozen v0.0.2 L1/L2 authority population.

Candidate invariants:

```text
records:                              294
unique IDs:                           294
Project-Applicable Obligations:       218
Framework Normative Invariants:        76
SCAF-PAT-* records:                     0
relations fields:                     294
non-empty relations:                    0
```

Frozen Markdown remains canonical semantic authority. The registry does not become an alternate normative authority source.

Machine-readable L2→L3 relation semantics remain deferred; empty `relations` values are intentional candidate state, not missing freeze work.

## 7. Current Control-Plane Identity Set

The CI trust model pins exactly these six repository artifacts by SHA-256:

```text
tools/scaf_ci_gate/gate.py
    2b553ff5e74089c0d1a535998291ea8fedb494b643cde2d42887ecf12b094f43

tools/scaf_external_pin/checker.py
    fc2f44fdcef05194e0614e375063a37316af678243dbc1e8b64e5d9cf155142b

release-integrity/frozen-baseline-manifest.json
    bdf56105e0becdb66c2e53f9adde6fe49a640fd0a50cf06215ef34a8156e1e2b

tools/scaf_release_integrity/checker.py
    03bcc9e3308f73a97bf02537e286589589122cce13f3ddf0fc13c61e46a7fead

tools/scaf_validator/validator.py
    8c8ec9b16567112004d8eb3e65755f6bc2b446670f084aefd7e70a635a76d92f

schemas/authority-registry.schema.json
    560e89b9385bc5696f2401f01a56c8928ccea01be7bad1e8b00f0e51c3993965
```

The external CI trust bundle remains repository-external caller/environment trust input. It is not committed as the repository's own trust root.

## 8. CI Gate Candidate State

The accepted candidate sequence remains:

```text
external trust input available and structurally valid
        ↓
six fixed control-plane paths pass component-by-component no-symlink validation
        ↓
six externally pinned SHA-256 identities MATCH
        ↓
external-pin verification
        ↓
frozen-baseline release integrity
        ↓
authority-registry semantic / structural / source validation
        ↓
each successful stage reports the same verified Repository root
        ↓
CI gate RESULT: PASS
```

Any failed identity, topology, root-attestation, or control stage prevents an overall PASS.

The GitHub Actions workflow remains a **trusted-main/manual executor foundation** only:

```text
push: main
workflow_dispatch
```

It does not implement fork-PR or privileged `pull_request_target` execution.

## 9. Regression Inventory

The v0.0.4 freeze candidate requires these accepted regression suites to remain green:

```text
scaf_validator:          8 tests / OK
scaf_release_integrity:  9 tests / OK
scaf_external_pin:      11 tests / OK
scaf_ci_gate:           13 tests / OK
```

Total current shipped regressions across the four control suites:

```text
41 tests
```

A freeze-candidate review shall treat a regression-count reduction, unexpected skip, or normal PASS through a reproduced accepted fail-closed case as a blocking inconsistency unless explicitly justified by a separately reviewed semantic change. rc12 authorizes no such semantic change.

## 10. Authority / Trust Separation

The freeze candidate preserves the following non-equivalence:

```text
Frozen Markdown semantic authority
        !=
authority-registry / schema conformance
        !=
frozen-source byte identity
        !=
external identity trust input
        !=
CI executor / enforcement policy
```

Neither schema, validator, manifest, external pin, trust bundle, workflow, nor CI gate may create or redefine requirement semantics, project applicability, PDA decisions, compliance, verification, evidence, closure, Pattern selection, or L3 maturity merely because it validates or enforces a representation/control state.

## 11. Frozen / Candidate / Deferred Boundary

### Frozen upstream inputs

- v0.0.2 L1/L2 normative baseline under `docs/normative/`;
- v0.0.3 L3 Pattern / Mechanism Catalog baseline under `docs/l3/`.

These baselines shall not be modified in place.

### v0.0.4 freeze-candidate content

- machine-readable authority model;
- deterministic authority-record contract;
- 294-record authority registry;
- canonical registry schema;
- semantic / structural / source-aware validator;
- validator CLI binding/hardening;
- frozen-baseline manifest;
- release-integrity checker;
- external-pin verification foundation and symlink hardening;
- external CI trust-input contract;
- executable-governance CI gate;
- repository path-component and root-binding hardening;
- regression suites and current trusted-main/manual workflow executor.

### Explicitly deferred beyond v0.0.4

- fork-PR / privileged PR execution policy;
- branch-protection / merge-blocking administration;
- workflow/package self-authentication;
- signing, PKI, transparency logs, attestations, or provenance services;
- canonical external pin / CI trust-bundle storage and distribution policy;
- generated authority indexes/views and reverse indexes;
- authority-registry generation or hybrid generated/curated ownership;
- code generation;
- automatic project applicability/compliance/verification/evidence/closure inference;
- machine-readable non-empty L2→L3 relation semantics;
- third-tranche/new L3 Pattern work or SEC-primary realization;
- M3/M4;
- L4 implementation / verification guidance.

Deferred items are not acceptance defects for v0.0.4 merely because they are not implemented.

## 12. Freeze-Candidate Non-Regression Rule

rc12 is consolidation-only. Relative to accepted rc11, it shall change only current release/navigation/consolidation documentation needed to represent the freeze candidate.

It shall not change executable control behavior, workflow behavior, registry/schema semantics, frozen manifest/checker identities, external-pin behavior, CI-gate behavior, regression code, frozen normative content, frozen L3 content, or accepted historical governance records `00_*` through `10_*`.

Expected rc11→rc12 repository delta:

```text
Added:   1
Changed: 3
Removed: 0
```

Expected added file:

```text
docs/executable-governance/11_SCAF_v0.0.4rc12_Executable_Governance_Milestone_Consolidation_and_Freeze_Candidate.md
```

Expected changed files:

```text
README.md
CHANGELOG.md
docs/executable-governance/README.md
```

## 13. Freeze-Candidate Acceptance Criteria

The independent rc12 review shall confirm all of the following before recommending formal freeze eligibility:

1. rc01→rc11 review history is accurately consolidated, including the rc10 `NO` and rc11 closure.
2. No accepted finding remains open.
3. The 294 / 218 / 76 authority inventory remains unchanged.
4. All 294 registry `relations` values remain empty and no `SCAF-PAT-*` identity enters the authority registry.
5. The 11-file normative and 30-file L3 protected trees match the accepted fingerprints.
6. The six current CI control-plane artifact identities match the accepted SHA-256 values.
7. The four shipped regression suites remain 8 / 9 / 11 / 13 tests and pass.
8. The canonical executable-governance gate passes with a valid outside-repository trust bundle.
9. The gate retains fixed stage order, path-component hardening, repository-root binding, and stage-root attestation.
10. The workflow remains trusted-main/manual only and does not silently expand into privileged PR enforcement.
11. Authority, representation, byte-integrity, trust-input, and CI-enforcement meanings remain distinct.
12. rc12 introduces no new semantic or executable capability beyond consolidation/navigation.
13. Deferred work is clearly identified and not falsely presented as complete.
14. rc12 is clearly identified as a **freeze candidate**, not as an already frozen `v0.0.4` release.

## 14. Formal Freeze Rule

An independent rc12 gate of `YES` establishes **freeze-candidate eligibility only**.

It does not by itself rename the release to `v0.0.4`, rewrite current-release metadata, or authorize in-place mutation of candidate artifacts.

Formal freeze requires a separate explicit governance decision after review. The intended formal milestone name, if that decision is made, is:

```text
SCAF v0.0.4 — Frozen Executable Governance Baseline
```

## 15. Freeze-Candidate Gate

Expected independent review label:

```text
V0.0.4 EXECUTABLE-GOVERNANCE MILESTONE CONSOLIDATION / FREEZE-CANDIDATE GATE
```
