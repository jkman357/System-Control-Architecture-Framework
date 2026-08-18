# SCAF Project Application Validator

**Development Release:** v0.0.6rc07  
**Status:** Project Application Validator Foundation / Review Candidate

This tool validates **Project Application representation conformance** for the accepted `v0.0.6rc04` Project Application representation and the `v0.0.6rc06` JSON Schema foundation.

It is not a project-design, applicability, compliance, verification, or closure authority.

## Install dependencies

From the repository root:

```text
python -m pip install -r tools/scaf_project_application_validator/requirements.txt
```

Dependencies are intentionally limited to:

- PyYAML — YAML event/loader-policy processing;
- jsonschema — Draft 2020-12 parsed-instance validation.

## Validate the repository fixture

```text
python -m tools.scaf_project_application_validator.validator
```

The default input is:

```text
examples/project-application.yaml
```

## Validate another Project Application YAML

```text
python -m tools.scaf_project_application_validator.validator --project-application <path>
```

The caller may select the Project Application dataset, but the production CLI does **not** accept caller-selected repository roots, schemas, or authority registries. The validator is bound to the canonical schema and frozen authority registry in the SCAF repository containing the tool.

## Validator pipeline

```text
Project Application YAML
        ↓
raw-YAML policy checks
        ↓
strict safe load
        ↓
rc06 JSON Schema validation
        ↓
cross-record identity checks
        ↓
deterministic record/reference ordering checks
        ↓
frozen authority-registry validation
        ↓
scaf_authority_id existence/class/source-release resolution
```

The raw-YAML policy rejects:

- duplicate mapping keys;
- anchors;
- aliases;
- merge keys;
- custom YAML tags;
- multi-document streams;
- non-string mapping keys.

The post-schema checks enforce:

- `record_id` uniqueness across records;
- unique active `(scaf_authority_id, project_scope_ref)` pairs;
- exact ascending `record_id` ordering;
- exact ascending ordering for `basis_refs`, `awaiting_refs`, `decision_refs`, `authority_refs`, and `supporting_refs` when present;
- `scaf_authority_id` existence in the frozen authority registry;
- target class = `Project-Applicable Obligation`;
- target `source_release` consistency with the record.

## What PASS means

`REPRESENTATION RESULT: PASS` means the input satisfied the reviewed machine-determinable representation contract checked by this tool.

It does **not** mean:

- the applicability judgment is technically correct;
- the rationale is adequate;
- a referenced decision or authority is sufficient;
- a project reference exists or resolves;
- a Pattern is selected or appropriate;
- implementation, verification, compliance, evidence, or closure is complete.

Project-controlled reference existence/resolution remains deferred. Engineering judgment remains owned by the applicable project authority.

## Tests

```text
python -m unittest discover -s tools/scaf_project_application_validator/tests -v
```

The rc07 suite covers the accepted fixture plus bounded invalid-condition cases for raw-YAML policy, schema chaining, cross-record uniqueness, deterministic ordering, and frozen authority target resolution.
