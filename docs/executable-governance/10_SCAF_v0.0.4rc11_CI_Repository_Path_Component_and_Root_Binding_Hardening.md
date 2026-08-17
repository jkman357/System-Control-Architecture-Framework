# SCAF v0.0.4rc11 — CI Repository Path-Component and Root-Binding Hardening

**Release:** v0.0.4rc11  
**Status:** Focused `R10-01` Closure RC  
**Date:** 2026-08-17

## 1. Upstream Review Basis

The independent v0.0.4rc10 review returned:

```text
V0.0.4 CI TRUST-INPUT / EXECUTABLE-GOVERNANCE GATE FOUNDATION GATE: NO
```

The sole blocking finding was:

```text
R10-01 — Major
Parent-directory symlink components can pivot gate.py or a downstream control
into a pristine nested shadow repository, permitting normal PASS while the
actual checkout-root content is modified or unvalidated.
```

The rc10 trust-input model, six fixed control-plane identities, fixed stage order, trusted-main/manual workflow scope, and authority/trust separation remain the accepted design basis. rc11 changes only repository/control path binding needed to close this fail-open path.

## 2. Closure Objective

A control result is acceptable only when the reviewed control executes from the intended checkout root through the intended non-symlinked repository path. Matching bytes in a shadow subtree are not sufficient.

The closure contract is:

```text
verified lexical checkout root
        ↓
component-by-component no-follow path validation
        ↓
fixed control artifact SHA-256 verification
        ↓
fixed downstream stage execution
        ↓
reported Repository root == verified checkout root
        ↓
PASS eligible
```

## 3. Production Repository-Root Binding

The production gate no longer discovers its repository root from:

```text
Path(__file__).resolve().parents[2]
```

because that operation can follow a symlinked parent before path topology is validated.

The production CLI instead requires execution from repository root and treats the lexical current working directory as the candidate checkout root. It then validates the canonical fixed path:

```text
tools/scaf_ci_gate/gate.py
```

component by component before accepting the current gate as the canonical gate for that root. The validated canonical gate must resolve to the currently executing file.

No production `--repo-root` override is introduced.

## 4. Component-by-Component No-Symlink Rule

For every fixed control-plane artifact, the gate shall inspect every repository-relative path component using no-follow filesystem metadata (`lstat` semantics) before accepting resolution or hashing.

For a path such as:

```text
tools/scaf_validator/validator.py
```

the required sequence is:

```text
repo root
  ↓
tools                 -> real directory, not symlink
  ↓
scaf_validator        -> real directory, not symlink
  ↓
validator.py          -> real regular file, not symlink
  ↓
resolve / confinement check
  ↓
SHA-256
```

The same rule applies to all six rc10/rc11 pinned control-plane artifact paths:

```text
tools/scaf_ci_gate/gate.py
tools/scaf_external_pin/checker.py
release-integrity/frozen-baseline-manifest.json
tools/scaf_release_integrity/checker.py
tools/scaf_validator/validator.py
schemas/authority-registry.schema.json
```

A symlink in a parent component or terminal component is a fail-closed control-path defect.

## 5. Pre-Stage Recheck

The downstream executable artifact path is checked again immediately before each stage execution. This reduces the gap between initial trust validation and stage launch and prevents a later path-topology change from silently reusing the earlier identity result.

The fixed stage order remains unchanged:

```text
scaf_external_pin
        ↓
scaf_release_integrity
        ↓
scaf_validator
```

## 6. Runtime Repository-Root Attestation

Each accepted downstream control already reports one line of the form:

```text
Repository: <path>
```

rc11 requires each successful stage to report exactly one repository root and requires that root to equal the same verified root used by the CI gate. A stage that returns exit code 0 but reports another nested/shadow repository is a gate failure.

This check is a control-orchestration/root-binding assertion. It does not make CI or the checker semantic authority.

## 7. Workflow Bootstrap Hardening

Before the GitHub Actions workflow computes the externally pinned `gate.py` SHA-256, its bootstrap code now:

1. confirms the working directory corresponds to `GITHUB_WORKSPACE`;
2. walks `tools/scaf_ci_gate/gate.py` component by component with `lstat`;
3. rejects any symlink component;
4. requires parent components to be directories;
5. requires the gate terminal path to be a regular file;
6. only then computes and compares the gate SHA-256;
7. executes repository gate code only after the bootstrap identity passes.

The workflow remains limited to trusted `main` pushes and `workflow_dispatch`.

## 8. Regression Contract

The rc11 CI-gate regression suite includes thirteen tests and retains the eight rc10 cases while adding focused R10-01 coverage:

1. all six fixed pinned artifact paths reject parent-component symlinks before stages;
2. production gate-root parent-directory symlink to a pristine nested shadow repository fails even when real frozen source is mutated;
3. production semantic-validator parent-directory symlink to a pristine nested shadow repository fails even when the real registry is invalid;
4. a successful stage that reports a different `Repository:` root is rejected;
5. workflow bootstrap component checks occur before the `sha256sum` gate identity comparison.

The accepted upstream suites remain:

```text
scaf_validator:          8 tests
scaf_release_integrity:  9 tests
scaf_external_pin:      11 tests
```

## 9. Authority and Trust Boundary

rc11 preserves:

```text
Frozen Markdown semantic authority
        !=
registry/schema conformance
        !=
frozen-byte identity
        !=
external identity trust input
        !=
CI executor/enforcement policy
```

Path topology and repository-root checks determine whether an executable control result is eligible for CI enforcement. They do not define SCAF requirement semantics, project applicability, compliance, verification, closure, Pattern selection, or L3 maturity.

## 10. Non-Regression Requirement

rc11 shall not change:

- `authority-registry.yaml`;
- `schemas/authority-registry.schema.json`;
- `tools/scaf_validator/validator.py` or its eight-test suite;
- `release-integrity/frozen-baseline-manifest.json`;
- `tools/scaf_release_integrity/checker.py` or its nine-test suite;
- `tools/scaf_external_pin/checker.py` or its eleven-test suite;
- executable-governance records `00_*` through `09_*`;
- frozen `docs/normative/`;
- frozen `docs/l3/`;
- the accepted 294 / 218 / 76 inventory;
- the twelve frozen `Available / M2 — Architecture Reviewed` L3 Pattern identities.

## 11. Deferred Scope

rc11 does not implement or authorize:

- fork-PR / `pull_request_target` execution of proposed code;
- branch-protection / merge-blocking administration;
- workflow self-authentication;
- signing, PKI, transparency logs, attestations, or provenance services;
- canonical external trust-bundle storage/distribution;
- generated indexes/views;
- authority-registry generation;
- code generation;
- automatic project applicability/compliance/closure inference;
- non-empty machine-readable L2→L3 relation semantics;
- new L3 Pattern work / third tranche / SEC-primary realization;
- M3/M4;
- L4.

## 12. Closure Gate

The independent rc11 review shall determine whether the two rc10 shadow-repository false-PASS reproductions are closed and whether all six fixed control-plane paths are protected from parent-component symlink redirection without reopening accepted semantics or deferred scope.

Expected gate label:

```text
V0.0.4 CI REPOSITORY PATH-COMPONENT / ROOT-BINDING HARDENING GATE
```
