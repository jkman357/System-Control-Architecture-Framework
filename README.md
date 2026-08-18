# System Control Architecture Framework (SCAF)

**Current Development Release:** v0.0.5rc9  
**Status:** L3 Trace Views Authority Validation and CLI Execution Boundary Closure  
**Date:** 2026-08-17

System Control Architecture Framework (**SCAF**) is a system-level architecture and engineering-governance framework for making responsibilities, interfaces, runtime behavior, failure handling, lifecycle behavior, observability, evidence, and project decisions explicit and reviewable.

SCAF is the successor to the Gen1 `host-device-control-framework`. `Gen2` is retained only as lineage / migration context.

## Meaning of “Control”

In SCAF, **Control** does not mean control theory and does not mean only host-to-device control. It refers to system-level architectural control concerns including responsibility and authority, functions/services/dependencies, runtime state, interaction contracts, timing/capacity/resources, robustness/resilience/recovery, boot/power/reset/update, configuration/persistent operational state, observability/diagnostics/incident evidence, security architecture interfaces, verification/evidence, and controlled project application.

## Current Baselines

Formal frozen baselines:

| Release | Frozen Baseline |
|---|---|
| `v0.0.1` | Architecture-convergence baseline |
| `v0.0.2` | L1/L2 normative authority baseline |
| `v0.0.3` | L3 Pattern / Mechanism Catalog baseline |
| `v0.0.4` | Executable Governance baseline |

Current development line:

| Release | Development Scope |
|---|---|
| `v0.0.5rc9` | Same-root trace + authority validation for deterministic read-only L2↔L3 query APIs, plus clean documented `python -m` CLI execution |

Frozen releases are not modified in place. Detailed release history, review gates and finding closure are maintained in [`CHANGELOG.md`](CHANGELOG.md).

## Framework Layers

```text
L1/L2 — Normative Authority
  What system/project concerns must be addressed and who owns the decision?
        ↓
L3 — Pattern / Mechanism Catalog
  What reusable architecture mechanisms may be considered?
        ↓
L4 — Implementation / Verification Guidance
  Future demand-driven guidance; not automatically implied by the current RC.
```

The frozen L1/L2 and L3 layers remain canonical for their accepted scope. v0.0.5 does not reopen them.

## Current v0.0.5rc9 Development Focus

The independent rc8 review confirmed `RC7-01: RESOLVED` but found two bounded issues in the validated trace-query boundary:

- `RC8-01` (Major): the public query path consumed `authority-registry.yaml` classification state without owning the frozen authority-registry validation proof for that same repository root;
- `RC8-02` (Minor): eager package re-export preloaded the documented `python -m tools.scaf_trace_views.query` target module, allowing CPython `runpy` to emit a duplicate-module `RuntimeWarning` and execute a second module instance.

rc9 closes only those findings. The supported Python API remains:

```python
from tools.scaf_trace_views import query_l2, query_pattern

view = query_l2(repo_root, "SCAF-ROB-004")
view = query_pattern(repo_root, "SCAF-PAT-COM-001")
```

Every supported query now requires both validation proofs on the same resolved repository root before repository data can be projected:

```text
query_l2() / query_pattern()
        ↓
rc6 trace validate_repository(repo_root)
        ↓ PASS only
frozen authority validate_registry(
    repo_root,
    repo_root / authority-registry.yaml,
    repo_root / schemas/authority-registry.schema.json)
        ↓ PASS only
load validated trace + authority state
        ↓
internal deterministic projection
        ↓
view return
```

The frozen authority validator itself is reused unchanged. rc9 does not create a second authority validator and does not modify the accepted rc6 trace validator.

The package now lazily re-exports `TraceViewError`, `query_l2`, and `query_pattern`; importing `tools.scaf_trace_views` no longer eagerly imports the `query` CLI target. The documented CLI therefore exercises one normal module execution path:

```text
python -m tools.scaf_trace_views.query --l2 SCAF-ROB-004
python -m tools.scaf_trace_views.query --pattern SCAF-PAT-COM-001
```

The rc9 suite includes actual subprocess coverage of these documented commands, including clean successful stderr and fail-closed invalid-authority behavior.

See [`docs/executable-governance/22_SCAF_v0.0.5rc9_L3_Trace_Views_Authority_Validation_and_CLI_Execution_Boundary_Closure.md`](docs/executable-governance/22_SCAF_v0.0.5rc9_L3_Trace_Views_Authority_Validation_and_CLI_Execution_Boundary_Closure.md).

## Authority and Trace Boundaries

```text
Frozen L1/L2 Markdown          -> semantic authority for authority identities/classes
frozen authority schema        -> structural representation constraints
frozen authority validator     -> source-aware authority-registry conformance proof
Frozen L3 Markdown             -> semantic trace authority
rc4 source-extraction contract -> deterministic trace interpretation
rc4 trace JSON Schema          -> trace structural representation constraints
l3-trace-registry.yaml         -> subordinate serialized trace data
rc6 trace validator            -> source-aware trace conformance proof
rc9 public query API / CLI     -> validated deterministic read-only consumption
```

The accepted L2↔L3 trace relation classes remain:

- `primary_realization_candidate`;
- `supporting_realization`;
- `constraint_input`.

A trace-view result does not by itself mean Applicable, Recommended, Selected, Satisfied, Compliant, Verified, or Closed.

## Executable Governance

The frozen v0.0.4 baseline provides:

```text
scaf_validator
scaf_release_integrity
scaf_external_pin
scaf_ci_gate
```

Canonical frozen regression inventory remains:

```text
8 validator tests
9 release-integrity tests
11 external-pin tests
13 CI-gate tests
41 total
```

Current v0.0.5 development checks:

```text
python -m tools.scaf_validator.validator
python -m tools.scaf_trace_validator.validator
python -m unittest discover -s tools/scaf_trace_validator/tests -v
python -m unittest discover -s tools/scaf_trace_views/tests -v
```

The accepted trace-validator suite remains 24 tests. rc9 expands the deterministic trace-view/query development suite from 23 to **28 tests**, adding three authority-registry negative-condition regressions and two documented `python -m` subprocess regressions.

The production CI gate still requires the repository-external trust input defined by frozen v0.0.4. rc9 does not expand the six-artifact production trust set.

## Repository Navigation

| Path | Purpose |
|---|---|
| `docs/normative/` | Frozen v0.0.2 L1/L2 semantic authority |
| `docs/l3/` | Frozen v0.0.3 L3 Pattern / Mechanism Catalog |
| `docs/executable-governance/` | Machine-readable/executable-governance contracts and controlled development records |
| `authority-registry.yaml` | Frozen v0.0.4 authority representation |
| `l3-trace-registry.yaml` | Accepted v0.0.5 subordinate serialization of frozen L3 typed trace relations |
| `schemas/` | Frozen authority-registry schema plus accepted L3 trace schema |
| `tools/scaf_validator/` | Frozen authority-registry semantic / structural / source-aware validator |
| `tools/scaf_trace_validator/` | Accepted source-aware trace validator and regressions |
| `tools/scaf_trace_views/` | Deterministic validated read-only L2↔L3 trace views/query |
| `release-integrity/` | Frozen-baseline integrity manifest |
| `tools/scaf_release_integrity/` | Frozen-source byte-integrity checker |
| `tools/scaf_external_pin/` | External-pin verification |
| `tools/scaf_ci_gate/` | Executable-governance CI orchestration |
| `.github/workflows/` | Trusted-main/manual CI executor |
| `CHANGELOG.md` | Release / RC / review / finding history |

## Project Application

SCAF does not automatically decide project applicability or project architecture. A project remains responsible for controlled applicability, architecture/mechanism selection, adaptation, realization, verification/evidence, and closure decisions. Catalog availability and machine-readable trace are navigation/decision-support inputs, not automatic project authority.

## Documentation Policy

- `README.md` describes the current framework state and navigation.
- `CHANGELOG.md` contains version/RC evolution, review gates and finding history.
- detailed controlled decisions and evidence remain under `docs/`.

## Release Policy

- RC work uses controlled `vX.Y.ZrcN` development releases.
- A formal baseline is created only after required review gates and an explicit governance freeze decision.
- Frozen baselines are immutable; later work starts on a new controlled line.

## License / Disclaimer

See [`LICENSE`](LICENSE). The framework and accompanying materials are provided **AS IS**, without warranty. No certification, compliance, safety approval, or fitness-for-purpose representation is implied.
