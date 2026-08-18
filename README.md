# System Control Architecture Framework (SCAF)

**Current Formal Release:** v0.0.5  
**Active Development RC:** v0.0.6rc14
**Status:** Project Application / Effective Project Profile Milestone Consolidation / Freeze Candidate
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
| `v0.0.5` | Frozen L3 Machine-Readable Traceability baseline |

The formal v0.0.5 baseline remains frozen and immutable. `v0.0.6rc14` consolidates the accepted v0.0.6 SCAF-APP Project Application and Effective Project Profile chain as a documentation-only milestone / freeze candidate. A clean rc14 review establishes freeze eligibility only; formal v0.0.6 freeze still requires a separate explicit governance decision.

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

## Frozen v0.0.5 Milestone

The v0.0.5rc10 freeze-candidate review returned a clean gate `YES` with no findings:

```text
Critical: 0
Major:    0
Minor:    0
Trivial:  0

V0.0.5 L3 MACHINE-READABLE TRACEABILITY MILESTONE CONSOLIDATION / FREEZE-CANDIDATE GATE: YES
```

The explicit governance freeze decision therefore promotes the reviewed rc10 source state to formal **v0.0.5 — Frozen L3 Machine-Readable Traceability Baseline**. The frozen baseline introduces no new semantic or executable capability beyond the reviewed rc10 candidate.

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
v0.0.5 formal freeze decision
```

The supported Python API remains unchanged:

```python
from tools.scaf_trace_views import query_l2, query_pattern
```

Every supported query continues to require the accepted same-root trace-validation plus authority-validation proofs before projection. The formal freeze changes no validator, query implementation, registry, schema, workflow, trust artifact, or regression code.

See [`docs/executable-governance/24_SCAF_v0.0.5_Formal_Freeze_Decision.md`](docs/executable-governance/24_SCAF_v0.0.5_Formal_Freeze_Decision.md).

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
v0.0.5 freeze record            -> frozen milestone boundary
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

Frozen v0.0.5 validation / regression checks:

```text
python -m tools.scaf_validator.validator
python -m tools.scaf_trace_validator.validator
python -m unittest discover -s tools/scaf_trace_validator/tests -v
python -m unittest discover -s tools/scaf_trace_views/tests -v
```

The frozen trace-validator suite remains 24 tests. The frozen deterministic trace-view/query suite remains **28 tests**. Formal v0.0.5 freeze changes neither test inventory nor executable behavior.

The production CI gate still requires the repository-external trust input defined by frozen v0.0.4. Formal v0.0.5 does not expand the six-artifact production trust set. The rc10 freeze-candidate review did not independently execute the production external-trust gate because the required external trust bundle was unavailable; no production PASS is implied by this freeze.

## Repository Navigation

| Path | Purpose |
|---|---|
| `docs/normative/` | Frozen v0.0.2 L1/L2 semantic authority |
| `docs/l3/` | Frozen v0.0.3 L3 Pattern / Mechanism Catalog |
| `docs/executable-governance/` | Machine-readable/executable-governance contracts and controlled development records |
| `authority-registry.yaml` | Frozen v0.0.4 authority representation |
| `l3-trace-registry.yaml` | Frozen v0.0.5 subordinate serialization of frozen L3 typed trace relations |
| `examples/project-application.yaml` | rc04-conformant illustrative SCAF-APP YAML fixture; rc05 adds multi-item ordering/duplicate-free coverage only; not a real project disposition dataset |
| `examples/effective-project-profile.yaml` | v0.0.6rc10 canonical illustrative Effective Project Profile derived from the accepted example Project Application dataset for one exact scope |
| `schemas/` | Frozen authority/L3 trace schemas plus the accepted v0.0.6rc06 Project Application schema and v0.0.6rc11 Effective Project Profile schema foundations |
| `tools/scaf_validator/` | Frozen authority-registry semantic / structural / source-aware validator |
| `tools/scaf_trace_validator/` | Frozen v0.0.5 source-aware trace validator and regressions |
| `tools/scaf_trace_views/` | Frozen v0.0.5 deterministic validated read-only L2↔L3 trace views/query |
| `tools/scaf_project_application_validator/` | Accepted v0.0.6rc07 Project Application representation/source-aware validator foundation |
| `tools/scaf_project_application_views/` | Accepted v0.0.6rc08 validated deterministic read-only Project Application record/authority/scope queries |
| `tools/scaf_effective_project_profile_validator/` | Accepted v0.0.6rc12 Effective Project Profile representation/source-aware validator foundation |
| `tools/scaf_effective_project_profile_generator/` | Accepted v0.0.6rc13 deterministic validated Effective Project Profile generator foundation |
| `release-integrity/` | Frozen-baseline integrity manifest |
| `tools/scaf_release_integrity/` | Frozen-source byte-integrity checker |
| `tools/scaf_external_pin/` | External-pin verification |
| `tools/scaf_ci_gate/` | Executable-governance CI orchestration |
| `.github/workflows/` | Trusted-main/manual CI executor |
| `CHANGELOG.md` | Release / RC / review / finding history |

## Project Application

SCAF does not automatically decide project applicability or project architecture. A project remains responsible for controlled applicability, architecture/mechanism selection, adaptation, realization, verification/evidence, and closure decisions. Catalog availability and machine-readable trace are navigation/decision-support inputs, not automatic project authority.

`v0.0.6rc01` through `v0.0.6rc08` established the machine-readable Project Application semantics, canonical representation, schema, source-aware validator, and validated deterministic read/query views. `v0.0.6rc09` through `v0.0.6rc13` established Effective Project Profile semantics, canonical YAML, schema, source-aware validation, and deterministic validated generation. `v0.0.6rc14` now consolidates that complete chain without adding executable capability. It records the accepted milestone boundary, closed findings, regression inventory, authority separation, and explicitly deferred work as a freeze candidate. See [`docs/executable-governance/38_SCAF_v0.0.6rc14_Project_Application_Effective_Project_Profile_Milestone_Consolidation_and_Freeze_Candidate.md`](docs/executable-governance/38_SCAF_v0.0.6rc14_Project_Application_Effective_Project_Profile_Milestone_Consolidation_and_Freeze_Candidate.md).

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
