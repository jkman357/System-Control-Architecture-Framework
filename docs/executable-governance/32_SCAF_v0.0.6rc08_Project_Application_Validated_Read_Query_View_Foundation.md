# SCAF v0.0.6rc08 — Project Application Validated Read/Query View Foundation

**Development Release:** v0.0.6rc08  
**Status:** Validated Read/Query View Foundation / Review Candidate  
**Date:** 2026-08-18  
**Upstream Frozen Baselines:** v0.0.2 L1/L2; v0.0.3 L3; v0.0.4 Executable Governance; v0.0.5 L3 Machine-Readable Traceability  
**Accepted Development Basis:** v0.0.6rc04 Project Application representation; v0.0.6rc06 schema; v0.0.6rc07 representation/source-aware validator  
**Immediate Predecessor:** v0.0.6rc07

## 1. Decision Purpose

The independent v0.0.6rc07 review returned a clean gate:

```text
Critical: 0
Major:    0
Minor:    0
Trivial:  0

V0.0.6RC07 PROJECT APPLICATION VALIDATOR FOUNDATION GATE: YES
```

rc07 established that a selected Project Application dataset can be checked for the accepted raw-YAML policy, rc06 schema conformance, cross-record identity uniqueness, deterministic collection ordering, frozen authority-registry proof, and `scaf_authority_id` existence/class/source-release resolution without converting representation conformance into project engineering authority.

rc08 takes the next bounded step: allow humans, automation, and AI tooling to consume that validated current-state Project Application dataset through deterministic read-only query views.

The governing rule is:

> **A supported rc08 query may project only data that passes the rc07 validation boundary. Query results are validated read-only observations of recorded project dispositions, not new applicability decisions or project authority.**

## 2. Scope of rc08

rc08 adds:

```text
tools/scaf_project_application_views/
```

Supported programmatic entry points are:

```text
query_record(repo_root, record_id, project_application_path=None)
query_authority(repo_root, scaf_authority_id, project_application_path=None)
query_scope(repo_root, project_scope_ref, project_application_path=None)
```

The selected Project Application path remains caller-selectable because rc07 already permits validation of a project-controlled dataset. The repository root continues to own the canonical schema and frozen authority-registry proof boundary.

rc08 does not add a mutable project index, generated registry, cache, resolver, recommendation engine, or completion state.

## 3. Validation-Owning Public API Boundary

The supported public query functions own the validation sequence. They do not accept:

```text
pre-parsed Project Application records
caller-built record indices
caller-created validation reports
caller-created validated context
caller-selected schema objects
caller-selected authority registries
```

The public flow is:

```text
selected Project Application YAML
        ↓
private immutable snapshot
        ↓
rc07 Project Application validator
        ↓ PASS only
internal sealed validated context
        ↓
deterministic projection
        ↓
read-only query result
```

This is deliberate. A caller cannot obtain a supported result by constructing a parsed mapping that never passed rc07 validation.

The internal validated context uses a private seal and is not part of the supported package API.

## 4. Same-Snapshot Validation and Consumption

rc08 validates and projects from the same private snapshot of the selected Project Application bytes.

This prevents a file selected by the caller from being validated in one state and then re-read for projection after it has changed.

For the `query_authority()` query domain, the frozen `authority-registry.yaml` is likewise copied to a private snapshot, source-aware validated against the repository-owned frozen authority schema/normative sources, and consumed from that same snapshot.

This snapshot behavior does not create a new persistent artifact and does not alter the source repository.

## 5. Query Model

Every result includes:

```text
project_application_view_version
query_kind
query_id
record_count
applicability_counts
records
```

`applicability_counts` contains the accepted current-state tokens in stable order:

```text
applicable
not_applicable
undetermined
```

Projected records preserve the accepted Project Application record content. Record and `disposition_basis` mappings are emitted in the accepted rc04 canonical field/member order so deterministic JSON does not depend on non-semantic physical mapping order in a valid input. rc08 does not rewrite rationale, normalize references into a new grammar, or introduce derived engineering fields.

## 6. `query_record` Semantics

`query_record()` selects one exact validated current-state `record_id`.

Rules:

- the selected Project Application dataset must pass rc07 validation;
- `record_id` must be a non-empty string;
- the requested identity must occur in the validated dataset;
- rc07 already proves current dataset `record_id` uniqueness;
- an unknown record identity returns no supported view and raises a query error.

A successful record query means only that the returned record is part of the validated selected dataset.

## 7. `query_authority` Semantics

`query_authority()` selects all validated current-state Project Application records for one frozen Project-Applicable Obligation identity.

The authority query domain is not inferred from the Project Application dataset alone. The frozen authority registry is source-aware validated and the requested ID must belong to:

```text
Project-Applicable Obligation
```

A Framework Normative Invariant or unknown frozen authority ID is not a valid Project Application authority query identity.

A known frozen Project-Applicable Obligation may legitimately have zero current records in the selected Project Application dataset. That is a valid zero-record view and means only:

> no validated current Project Application record in the selected dataset uses this exact authority identity.

It does not mean `Not Applicable`, omitted by decision, satisfied, compliant, or closed.

Authority-query records are ordered by:

```text
project_scope_ref ascending
then record_id ascending
```

This is deterministic serialization/view order only and has no priority meaning.

## 8. `query_scope` Semantics

`query_scope()` filters validated current records by exact `project_scope_ref` string.

rc08 still has no project-scope registry or resolver. Therefore every scope view explicitly includes:

```text
scope_resolution: not_performed
```

A zero-record result for an arbitrary non-empty scope string is valid and means only:

> no validated current record in the selected dataset has that exact serialized `project_scope_ref` value.

It does not prove that the project scope exists, does not exist, is authorized, is current, or is correctly defined.

Scope-query records are ordered by:

```text
scaf_authority_id ascending
then record_id ascending
```

Again, ordering is deterministic projection only.

## 9. Read-Only Projection Boundary

rc08 query results are detached copies of validated record content. Modifying a returned Python dictionary does not modify the source dataset or internal validated context.

The package creates no persistent index and performs no write-back.

The supported relationship is:

```text
Validated
    ↓
Queried
    ↓
Projected
```

It is explicitly not:

```text
Validated
    ↓
Automatically Approved / Selected / Closed
```

## 10. CLI Boundary

The production CLI is:

```text
python -m tools.scaf_project_application_views.query --record <record_id>
python -m tools.scaf_project_application_views.query --authority <scaf_authority_id>
python -m tools.scaf_project_application_views.query --scope <project_scope_ref>
```

The caller may select a Project Application dataset:

```text
--project-application <path>
```

The production CLI does not expose caller-selected:

```text
repository root
Project Application schema
authority registry
authority-registry schema
```

Text and JSON output are read-only projections. Validation/query failure emits `ERROR:` and `RESULT: FAIL` to stderr, exits non-zero, and emits no view payload.

## 11. Invalid Versus Unresolved

rc08 preserves the accepted distinction:

```text
representation invalidity
!=
legitimate engineering-unresolved state
```

A structurally/source-valid `undetermined` Project Application record remains queryable and contributes to the `undetermined` applicability count.

Querying such a record does not resolve its engineering question and does not convert `undetermined` into project failure or closure failure.

## 12. Engineering and Authority Boundary

A successful rc08 query proves only that:

- the selected dataset passed rc07 representation/source-aware validation;
- the requested supported query was applied deterministically to that validated data;
- returned records are read-only projections of the validated dataset.

A successful query does not prove:

```text
applicability correctness
rationale adequacy
Project Design Authority approval
project scope existence/validity
project-controlled reference existence/authority
Pattern suitability or selection
implementation/satisfaction
verification/evidence sufficiency
compliance
closure
```

Machine-readable and machine-queryable remain distinct from machine-decided.

## 13. Deferred Scope

rc08 deliberately does not introduce:

- project-scope registry/resolution;
- project-controlled reference locator/resolution;
- automatic applicability inference;
- AI approval of engineering rationale;
- Project Design Authority automation;
- Pattern recommendation or selection;
- Effective Project Profile generation;
- AI context packaging;
- project applicability-completion CI enforcement;
- implementation/satisfaction/compliance determination;
- verification/evidence/closure determination;
- history/supersession/re-evaluation serialization;
- tailoring taxonomy;
- code generation;
- new L3 Pattern content;
- L4 guidance;
- Development Context Recovery / `.scaf/work-checkpoint.yaml` workflow capability.

The Development Context Recovery idea remains a separate workflow concern and is intentionally not mixed into this Project Application query RC.

## 14. Regression / Verification Expectations

The rc08 candidate shall demonstrate:

```text
accepted Project Application record query              PASS
accepted authority query                               PASS
accepted scope query                                   PASS
known PAO with no current record -> zero view          PASS
unknown / FNI authority query rejection                PASS
unknown record query rejection                         PASS
scope zero-record resolution-neutral behavior          PASS
selected external Project Application validation       PASS
schema-invalid selected dataset rejection              PASS
ordering-invalid selected dataset rejection            PASS
frozen authority proof failure rejection               PASS
public API validated-input boundary                     PASS
internal context seal                                  PASS
read-only detached projection                          PASS
deterministic JSON independent of mapping member order PASS
CLI JSON/text execution                                PASS
CLI invalid-input no-payload behavior                  PASS
```

The new rc08 Project Application view suite is development-line coverage and does not change the frozen v0.0.4/v0.0.5 regression inventories.

## 15. Frozen Baseline Preservation

rc08 shall not modify:

```text
docs/normative/
docs/l3/
authority-registry.yaml
l3-trace-registry.yaml
schemas/authority-registry.schema.json
schemas/l3-trace-registry.schema.json
schemas/project-application.schema.json
examples/project-application.yaml
tools/scaf_validator/
tools/scaf_trace_validator/
tools/scaf_trace_views/
tools/scaf_project_application_validator/
tools/scaf_release_integrity/
tools/scaf_external_pin/
tools/scaf_ci_gate/
.github/workflows/
release-integrity/
```

The new query package is additive and consumes accepted validator/schema/authority surfaces without modifying them.

## 16. Acceptance Boundary

rc08 is acceptable only if independent review confirms that:

1. every supported public query owns the rc07 validation boundary;
2. no supported programmatic API can substitute caller-built parsed/context state for validation;
3. selected Project Application data is projected from the same immutable snapshot that was validated;
4. record/authority/scope query semantics are deterministic and accurately bounded;
5. authority queries use a source-validated frozen PAO query domain;
6. scope queries explicitly remain resolution-neutral;
7. zero-record results are not reinterpreted as applicability/completion decisions;
8. returned records are detached read-only projections;
9. invalid and legitimate `undetermined` states remain distinct;
10. Project Design Authority and engineering judgment remain outside tooling authority;
11. all frozen validators, integrity checks, and regression inventories remain passing;
12. no resolver/inference/Pattern/Profile/context-package/CI/L4 expansion is introduced.

A later RC may consider higher-level project profile or context-consumption capabilities only after this query boundary is independently accepted. rc08 itself does not pre-authorize that work.
