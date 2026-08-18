# System Control Architecture Framework (SCAF)

**Current Development Release:** v0.0.5rc10  
**Status:** L3 Machine-Readable Traceability Milestone Consolidation and Freeze Candidate  
**Date:** 2026-08-18

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
| `v0.0.5rc10` | Consolidation-only freeze candidate for the accepted v0.0.5 L3 machine-readable traceability chain; no new semantic or executable capability |

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

## Current v0.0.5rc10 Development Focus

The independent full-source rc9 re-review returned a clean gate `YES` with:

```text
RC7-01: REMAINS RESOLVED
RC8-01: REMAINS RESOLVED
RC8-02: REMAINS RESOLVED
RC9-01: NOT APPLICABLE UNDER CORRECTED CONTRACT

Critical: 0
Major:    0
Minor:    0
Trivial:  0
```

rc10 therefore introduces **no new semantic or executable capability**. It consolidates the accepted v0.0.5 machine-readable traceability milestone and establishes a freeze candidate for independent review.

The consolidated dependency chain is:

```text
frozen v0.0.2 L1/L2 semantic authority
        ↓
frozen v0.0.3 L3 Pattern semantic trace authority
        ↓
rc1/rc2 machine-readable trace representation model
        ↓
rc3 l3-trace-registry.yaml serialization
        ↓
rc4 trace schema + deterministic source-extraction contract
        ↓
rc6 source-aware trace validator
        ↓
rc7/rc8/rc9 validated deterministic read-only L2↔L3 query boundary
        ↓
rc10 milestone consolidation / freeze candidate
```

The supported Python API remains unchanged:

```python
from tools.scaf_trace_views import query_l2, query_pattern
```

Every supported query continues to require the accepted same-root trace-validation plus authority-validation proofs before projection. rc10 changes no validator, query implementation, registry, schema, workflow, frozen baseline, trust artifact, or regression code.

See [`docs/executable-governance/23_SCAF_v0.0.5rc10_L3_Machine_Readable_Traceability_Milestone_Consolidation_and_Freeze_Candidate.md`](docs/executable-governance/23_SCAF_v0.0.5rc10_L3_Machine_Readable_Traceability_Milestone_Consolidation_and_Freeze_Candidate.md).

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
rc10 consolidation record       -> freeze-candidate milestone boundary
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

The accepted trace-validator suite remains 24 tests. The accepted deterministic trace-view/query suite remains **28 tests**. rc10 changes neither test inventory nor executable behavior.

The production CI gate still requires the repository-external trust input defined by frozen v0.0.4. rc10 does not expand the six-artifact production trust set.

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
