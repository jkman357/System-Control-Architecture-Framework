# SCAF External Release-Integrity Pin Checker

This rc09 package verifies that the local canonical frozen-baseline manifest and local release-integrity checker match a trusted pin document supplied from **outside** the SCAF repository.

## Trust model

The rc07 local checker proves only source-vs-manifest consistency. A coordinated modification of source + local manifest can therefore pass local comparison. rc08 introduced a separate external comparison step; rc09 hardens local pinned-artifact symlink rejection:

```text
trusted external pin document
        ↓
pin local canonical manifest + release-integrity checker identities
        ↓
local release-integrity checker
        ↓
frozen docs/normative + docs/l3 bytes
```

The external pin document is the caller/environment trust input. SCAF rc09 does not decide how that document is distributed, signed, protected, or stored. CI enforcement, signing, protected release metadata and provenance services remain separately gated.

The pin checker itself is not self-authenticated by the pin document. Its trust comes from executing the reviewed rc09 source/package; a future CI/signing stage may independently pin the rc09 checker/package identity.

## External pin document contract

The JSON document must be stored outside the repository and contain exactly:

```json
{
  "pin_version": 1,
  "pin_scope": "scaf_frozen_baseline_release_integrity",
  "hash_algorithm": "sha256",
  "artifacts": [
    {
      "path": "release-integrity/frozen-baseline-manifest.json",
      "sha256": "<reviewed canonical manifest sha256>"
    },
    {
      "path": "tools/scaf_release_integrity/checker.py",
      "sha256": "<reviewed rc08 release-integrity checker sha256>"
    }
  ]
}
```

Artifact paths are fixed; the pin document cannot select arbitrary repository files or alternate algorithms. Duplicate JSON keys are rejected.

## Production command

```text
python -m tools.scaf_external_pin.checker --pin-file <outside-repository-pin.json>
```

The pin file must:

- be outside the SCAF repository;
- be a regular file;
- not be a symlink;
- contain exactly the two reviewed artifact pins above.

The production CLI exposes no repository-root, artifact-path, hash-algorithm or local-manifest override.

After a successful external-pin check, run the local frozen-byte check separately:

```text
python -m tools.scaf_release_integrity.checker
```

The two steps are intentionally separate so external provenance/pinning is not conflated with local byte-integrity checking.

## Tests

```text
python -m unittest discover -s tools/scaf_external_pin/tests -v
```


## rc09 local pinned-artifact symlink hardening

Production verification rejects either fixed repository artifact if the **artifact path itself** is a symlink, even when that symlink resolves to an in-repository regular file with identical bytes. The checker evaluates the lexical artifact path for symlink status before resolving it for repository confinement and hashing.

This closes upstream `R8-01` without changing the external pin document contract, fixed artifact identities, SHA-256 algorithm, or trust model. Symlinked parent-component policy is not expanded by rc09; the required closure is specifically the fixed artifact path itself.

Regression suite expectation for rc09:

```text
11 tests / OK
```
