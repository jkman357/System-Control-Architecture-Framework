# Effective Project Profile Source-Aware Validator

This package is the `v0.0.6rc12` executable validation boundary for the
accepted Effective Project Profile semantics (`rc09`), canonical YAML
representation (`rc10`), and parsed-instance schema (`rc11`).

Run the repository illustrative sources:

```text
python -m tools.scaf_effective_project_profile_validator.validator
```

Or select both project-controlled inputs:

```text
python -m tools.scaf_effective_project_profile_validator.validator \
  --profile <effective-project-profile.yaml> \
  --project-application <project-application.yaml>
```

The caller may select only those two project-side source files. The repository
root, profile schema, Project Application schema, frozen authority registry and
schema, and canonical normative sources are derived from this reviewed SCAF
repository and are not CLI-selectable.

The validator checks:

- accepted rc10 raw-YAML restrictions;
- accepted rc11 Draft 2020-12 schema conformance;
- exact SHA-256 binding to the selected Project Application source bytes;
- frozen authority-registry source-aware proof;
- accepted rc07 validation of the selected Project Application snapshot;
- complete source-release-bound Project-Applicable Obligation coverage;
- cross-entry authority-ID uniqueness and PAO-only domain membership;
- canonical root/entry mapping order and entry ordering;
- recorded-state record-ID existence and exact authority/scope/state/source-release correspondence;
- exact-pair absence for every `no_current_disposition` entry.

A successful result is reported only as:

```text
PROFILE REPRESENTATION/SOURCE RESULT: PASS
```

It does **not** mean project applicability is substantively correct, rationale
is adequate, Project Design Authority approved the judgment, a Pattern is
selected, implementation or verification is complete, compliance is achieved,
risk is acceptable, the project is complete, release is ready, or closure has
occurred.
