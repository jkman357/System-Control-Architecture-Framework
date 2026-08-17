# SCAF v0.0.4rc10 — CI Trust-Input Model and Executable-Governance Gate Foundation

**Release:** v0.0.4rc10  
**Status:** CI Trust-Input / Executable-Governance Gate Foundation RC  
**Date:** 2026-08-17  
**Upstream Gate:** `V0.0.4 EXTERNAL-PIN LOCAL-ARTIFACT SYMLINK-HARDENING GATE: YES`

## 1. Purpose

rc10 establishes the first bounded CI execution/enforcement surface for the accepted SCAF executable-governance controls. It does not change SCAF semantic authority and does not reopen the frozen v0.0.2 L1/L2 or v0.0.3 L3 baselines.

The goal is to answer one bounded question:

> Can a trusted CI execution environment receive repository-external trust input, authenticate the reviewed control-plane identities, and then execute the three accepted controls in a fixed fail-closed order?

The three accepted controls remain distinct:

1. external identity pin verification;
2. frozen-baseline byte-integrity verification;
3. authority-registry/schema/canonical-source validation.

## 2. Authority and trust boundaries

The following meanings remain separate:

```text
Frozen Markdown semantic authority
        !=
authority-registry/schema representation conformance
        !=
local frozen-source byte identity
        !=
external identity trust input
        !=
CI execution/enforcement policy
```

GitHub Actions is an executor/enforcement surface only. It does not become semantic authority, framework authority, project design authority, requirement evidence, verification evidence, or release provenance by virtue of running the checks.

## 3. CI trust bundle

rc10 defines one external JSON trust-bundle contract with exactly these root members:

```text
trust_version
trust_scope
hash_algorithm
artifacts
external_pin
```

Fixed values:

```text
trust_version  = 1
trust_scope    = scaf_executable_governance_ci
hash_algorithm = sha256
```

The `artifacts` array pins exactly six repository control-plane artifacts:

```text
tools/scaf_ci_gate/gate.py
tools/scaf_external_pin/checker.py
release-integrity/frozen-baseline-manifest.json
tools/scaf_release_integrity/checker.py
tools/scaf_validator/validator.py
schemas/authority-registry.schema.json
```

Each artifact entry contains exactly:

```text
path
sha256
```

The nested `external_pin` object is the accepted rc08/rc09 external-pin contract and pins exactly:

```text
release-integrity/frozen-baseline-manifest.json
tools/scaf_release_integrity/checker.py
```

The nested hashes must equal the corresponding top-level CI trust pins. This prevents the CI trust bundle and the accepted external-pin meaning from silently disagreeing.

The trust bundle must be a regular non-symlink file outside the SCAF repository. Repository-resident files cannot claim to be the external trust root for this gate.

## 4. Bootstrap rule

`tools/scaf_ci_gate/gate.py` cannot simply declare itself trusted.

The GitHub Actions workflow therefore performs one minimal bootstrap before executing repository gate code:

1. obtain the external trust bundle from an Actions secret;
2. decode the bundle into `RUNNER_TEMP`, outside the checked-out repository;
3. parse only enough of the bundle to obtain the expected SHA-256 for `tools/scaf_ci_gate/gate.py`;
4. compute the checked-out `gate.py` SHA-256 using the runner's native hash utility;
5. fail before repository gate execution if the hashes differ;
6. only after that identity check, execute `gate.py`.

The production gate then revalidates the entire trust-bundle contract and all six pinned control-plane artifacts before executing any accepted SCAF control.

## 5. Fixed stage order and failure policy

The production gate executes exactly:

```text
external trust bundle valid + control identities MATCH
        ↓
scaf_external_pin
        ↓
scaf_release_integrity
        ↓
scaf_validator
        ↓
CI GATE PASS
```

Rules:

- missing trust input -> FAIL;
- malformed/unsupported trust bundle -> FAIL;
- bundle stored inside the repository -> FAIL;
- bundle symlink -> FAIL;
- any pinned control-plane artifact missing, symlinked, out of repository, or hash-mismatched -> FAIL before stages;
- external-pin stage non-zero -> FAIL and stop;
- frozen-baseline integrity stage non-zero -> FAIL and stop;
- semantic/representation validator stage non-zero -> FAIL;
- no stage may be skipped and still produce normal gate PASS.

Production CLI does not expose repository-root, artifact-set, schema, manifest, hash-algorithm, or stage-order overrides.

## 6. Python execution isolation

The CI gate and downstream SCAF control scripts are invoked with Python isolated mode (`-I`) to avoid using the checked-out repository current directory as an implicit Python import source. The semantic validator still uses its explicit external dependencies (`PyYAML` and `jsonschema`).

This is a bounded hardening measure and is not a general Python package-provenance solution.

## 7. GitHub Actions foundation

The repository adds:

```text
.github/workflows/scaf-executable-governance.yml
```

rc10 intentionally limits this workflow to:

```text
push to main
workflow_dispatch
```

It does **not** claim fork-PR or `pull_request_target` enforcement.

The workflow:

- uses read-only repository contents permission;
- disables persisted checkout credentials;
- pins GitHub-maintained checkout/setup-python actions to reviewed full commit SHAs;
- expects the external trust bundle through the Actions secret `SCAF_CI_TRUST_BUNDLE_B64`;
- fails if that trust input is unavailable;
- materializes the bundle only under `RUNNER_TEMP`;
- bootstraps `gate.py` identity before executing repository gate code;
- installs exact direct semantic-validator dependency versions for this RC;
- executes the bounded CI gate.

## 8. Why PR/fork enforcement is deferred

rc10 does not use normal `pull_request` as the trusted-pin gate because fork pull-request workflows do not receive normal Actions secrets. It also does not introduce `pull_request_target` with checkout/execution of pull-request code because that event runs with elevated base-repository trust and GitHub explicitly warns that executing untrusted checked-out PR code in that context creates a privileged-code execution risk.

A future PR enforcement stage must define a separate trust/execution model rather than silently reusing the trusted-branch workflow.

## 9. GitHub action dependency posture

The two GitHub-maintained actions used by the workflow are pinned to full commit SHAs rather than mutable tags:

```text
actions/checkout  v7.0.1  3d3c42e5aac5ba805825da76410c181273ba90b1
actions/setup-python v7.0.0 5fda3b95a4ea91299a34e894583c3862153e4b97
```

This follows GitHub's documented secure-use recommendation that a full-length commit SHA is the immutable action reference form.

## 10. Regression contract

`tools/scaf_ci_gate/tests/test_gate.py` covers at least:

1. accepted external bundle runs all three stages in fixed order;
2. repository-resident bundle fails;
3. top-level control-plane hash mismatch fails before stages;
4. nested external-pin hash inconsistent with top-level trust pin fails;
5. modified pinned semantic validator in a repository copy fails before execution;
6. production CLI rejects repository-root and stage-order overrides;
7. workflow is trusted-branch/manual only and requires external trust input;
8. workflow uses read-only contents, disabled credential persistence, and full-SHA action pins.

The accepted upstream suites remain separate and must also continue to pass:

```text
scaf_validator:          8 tests
scaf_release_integrity:  9 tests
scaf_external_pin:      11 tests
```

## 11. Explicit limitations

rc10 does **not** claim that the repository-contained workflow self-authenticates itself. A user with authority to change the trusted default branch/workflow may alter the executor definition unless separate repository/organization policy protects it.

rc10 also does not authenticate:

- GitHub-hosted runner images;
- GitHub service operation;
- Actions-secret administration;
- PyPI package provenance beyond the exact direct dependency versions requested by the workflow;
- the external trust-bundle creator/distribution channel.

Those are future trust-maturity concerns, not hidden properties of this foundation.

## 12. Deferred scope

rc10 does not add or authorize:

- fork-PR / `pull_request_target` execution of proposed repository code;
- merge blocking / branch-protection configuration as a repository-owned semantic decision;
- signing, PKI, transparency logs, attestations, or provenance services;
- canonical external trust-bundle storage/distribution policy;
- reusable workflow hosted in a separate trust repository;
- generated indexes/views;
- authority-registry generation;
- code generation;
- automatic project applicability/compliance/closure inference;
- non-empty machine-readable L2→L3 relation semantics;
- new L3 Patterns / third tranche / SEC-primary realization;
- M3/M4;
- L4.

## 13. Gate question

The independent rc10 review shall determine whether:

- the external CI trust-bundle contract is deterministic and bounded;
- `gate.py` is externally bootstrapped before repository gate execution in the workflow;
- all six control-plane identities are checked fail-closed;
- the nested accepted external pin cannot disagree with the top-level CI trust bundle;
- the three accepted controls execute in fixed order with stop-on-failure behavior;
- trusted-branch GitHub Actions execution is correctly scoped and fail-closed on missing external trust input;
- accepted upstream artifacts and frozen baselines remain non-regressed;
- rc10 does not overclaim PR/fork, signing/provenance, generated-view, L3, M3/M4, or L4 scope.

Expected gate label:

```text
V0.0.4 CI TRUST-INPUT / EXECUTABLE-GOVERNANCE GATE FOUNDATION GATE
```
