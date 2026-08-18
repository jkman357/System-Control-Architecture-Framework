# SCAF Project Application Validated Read/Query Views

**Development Release:** v0.0.6rc08  
**Status:** Validated Read/Query View Foundation / Review Candidate

This package provides deterministic **read-only** views over Project Application data only after the selected dataset passes the accepted v0.0.6rc07 representation/source-aware validator.

It does not infer applicability, resolve project-controlled scope/reference targets, recommend or select Patterns, or determine implementation, verification, compliance, evidence sufficiency, or closure.

## Supported Python API

```python
from tools.scaf_project_application_views import (
    query_record,
    query_authority,
    query_scope,
)

record_view = query_record(repo_root, "EXAMPLE-PA-001")
authority_view = query_authority(repo_root, "SCAF-AK-001")
scope_view = query_scope(repo_root, "example:scope:system")
```

A caller may also select another Project Application dataset as the third argument / `project_application_path`, but the query function still owns validation of that selected input.

The supported API does **not** accept pre-parsed records, caller-built indices, or caller-created validation context.

## Validated-input boundary

```text
query_record() / query_authority() / query_scope()
        ↓
immutable snapshot of selected Project Application YAML
        ↓
rc07 Project Application validator
        ↓ PASS only
internal validated context
        ↓
deterministic read-only projection
        ↓
view
```

For `query_authority()`, the frozen authority-registry query domain is separately source-validated so a known Project-Applicable Obligation with zero current Project Application records can return a valid zero-record view, while unknown and Framework Normative Invariant IDs are rejected.

## Query semantics

### `query_record`

Returns exactly one validated current Project Application record by `record_id`. Unknown record IDs are rejected.

### `query_authority`

Returns all validated current records whose `scaf_authority_id` equals one frozen Project-Applicable Obligation ID. Records are ordered by exact `project_scope_ref`, then `record_id`.

A known frozen Project-Applicable Obligation with no current Project Application record is a valid zero-record result.

### `query_scope`

Filters validated current records by exact opaque `project_scope_ref` string. Records are ordered by exact `scaf_authority_id`, then `record_id`.

Because rc08 introduces no project-scope resolver, every scope view explicitly contains:

```text
scope_resolution: not_performed
```

A zero-record scope query does not prove that the scope exists or does not exist. It only means no validated current record in the selected dataset has that exact string.

## Deterministic projection

Record mappings and `disposition_basis` mappings are emitted in the accepted rc04 canonical field/member order. This keeps JSON output deterministic even when a schema-valid input uses a different physical YAML mapping-key order, which is non-semantic under the accepted representation contract.

## CLI

From repository root:

```text
python -m tools.scaf_project_application_views.query --record EXAMPLE-PA-001
python -m tools.scaf_project_application_views.query --authority SCAF-AK-001
python -m tools.scaf_project_application_views.query --scope example:scope:system
```

Deterministic JSON:

```text
python -m tools.scaf_project_application_views.query --record EXAMPLE-PA-001 --format json
```

Another Project Application dataset may be selected:

```text
python -m tools.scaf_project_application_views.query \
  --project-application <path> \
  --scope <project_scope_ref>
```

The production CLI does not expose caller-selected repository/schema/authority-registry overrides.

## View boundary

```text
Validated / Queried / Projected
!= Applicability Correctness
!= Approved
!= Recommended
!= Pattern Selected
!= Implemented
!= Verified
!= Compliant
!= Closed
```

Project-controlled reference existence/resolution and engineering judgment remain outside rc08.
