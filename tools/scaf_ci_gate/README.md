# SCAF Executable-Governance CI Gate

This package is the v0.0.4rc11 bounded CI orchestration surface, focused on closing rc10 `R10-01`. It does not define SCAF semantic authority.

## Control order

The gate runs exactly:

1. external identity pin verification;
2. frozen-baseline byte-integrity verification;
3. authority-registry/schema/canonical-source validation.

A failed stage stops later stages and returns non-zero.

## External trust bundle

Production use requires `--trust-bundle <path>` where the JSON file:

- is outside the SCAF repository;
- is a regular non-symlink file;
- uses SHA-256;
- pins exactly the six accepted control-plane artifacts;
- embeds the accepted two-artifact external pin and requires those hashes to match the top-level CI pins.

The six pinned control-plane artifacts are:

```text
tools/scaf_ci_gate/gate.py
tools/scaf_external_pin/checker.py
release-integrity/frozen-baseline-manifest.json
tools/scaf_release_integrity/checker.py
tools/scaf_validator/validator.py
schemas/authority-registry.schema.json
```

The external trust bundle is an environment / CI trust input. It is not framework semantic authority.

## Production CLI

From repository root:

```text
python -I tools/scaf_ci_gate/gate.py --trust-bundle /outside/repository/scaf-ci-trust-bundle.json
```

The production CLI exposes no repository-root, artifact-set, schema, manifest, stage-order, or hash-algorithm override.

Production execution must start from repository root. The gate binds to that lexical checkout root, verifies that the canonical gate path is the running gate, and rejects any symlink in every repository-relative component of all six fixed control-plane artifact paths. Parent components must be real directories and terminal artifacts must be real regular files.

After every successful downstream stage, the gate also checks the stage-reported `Repository:` value. All three controls must report the same verified root; a PASS produced from a nested/shadow repository is rejected.

## GitHub Actions foundation

`.github/workflows/scaf-executable-governance.yml` is intentionally limited to trusted `main` pushes and manual dispatch in rc11. It expects one externally configured GitHub Actions secret:

```text
SCAF_CI_TRUST_BUNDLE_B64
```

The secret contains the external trust-bundle JSON encoded as base64. The workflow decodes it only into `RUNNER_TEMP`, checks every component of the canonical `tools/scaf_ci_gate/gate.py` path with no-follow `lstat` semantics, verifies the reviewed `gate.py` hash, and only then executes repository gate code.

rc11 deliberately does not claim a fork-PR / `pull_request_target` enforcement solution. It also does not self-authenticate the workflow definition, GitHub-hosted runner, action marketplace, Python package index, or external secret administration. Those are later trust/enforcement concerns.
