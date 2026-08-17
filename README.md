# System Control Architecture Framework (SCAF)

**Current Development Release:** v0.0.5rc5  
**Status:** L3 Source-Aware Trace Validator Foundation  
**Date:** 2026-08-17

System Control Architecture Framework (**SCAF**) is a system-level architecture and engineering-governance framework for making responsibilities, interfaces, runtime behavior, failure handling, lifecycle behavior, observability, evidence, and project decisions explicit and reviewable.

SCAF is the successor to the Gen1 `host-device-control-framework`. `Gen2` is retained only as lineage / migration context.

## Meaning of “Control”

In SCAF, **Control** does not mean control theory and does not mean only host-to-device control.

It refers to system-level architectural control concerns such as:

- responsibility and authority;
- functions, services and dependencies;
- runtime state and interaction contracts;
- timing, concurrency, capacity and resources;
- robustness, resilience and recovery;
- boot, power, reset and update lifecycle;
- configuration and persistent operational state;
- observability, diagnostics and incident evidence;
- security architecture interfaces and robustness;
- verification, evidence and project application.

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
| `v0.0.5rc5` | Executable source-aware validation of the accepted L3 trace serialization |

Frozen releases are not modified in place. New semantic or executable capability proceeds on a later controlled RC/version line.

Detailed release history, review gates and finding closure are maintained in [`CHANGELOG.md`](CHANGELOG.md), not in this README.

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

The frozen L1/L2 and L3 layers remain canonical for their accepted scope. The current v0.0.5 development line does not reopen them.

## Current v0.0.5rc5 Development Focus

The accepted rc4 gate fixed both the structural trace schema and the deterministic fail-closed extraction contract. rc5 implements those reviewed rules as an independent executable development control:

[`tools/scaf_trace_validator/`](tools/scaf_trace_validator/README.md)

Canonical run:

```text
python -m tools.scaf_trace_validator.validator
```

The validator independently performs:

```text
trace JSON Schema validation
        +
frozen Pattern metadata reconstruction
        +
exact 119-record source/serialization comparison
        +
119 typed-relation tuple uniqueness
        +
canonical cross-record ordering proof
        +
82 L2 authority-identity resolutions
        +
15 qualifier-fidelity associations
```

Current accepted trace population remains:

```text
12 Pattern identities
23 primary_realization_candidate
41 supporting_realization
55 constraint_input
119 total relation records
82 unique referenced frozen L2 IDs
15 records with material source qualifiers
```

The authority chain remains:

```text
Frozen L3 Markdown         -> semantic trace authority
Source-extraction contract -> deterministic interpretation
Trace JSON Schema          -> structural representation constraints
l3-trace-registry.yaml     -> subordinate serialized data
rc5 trace validator        -> executable source-aware conformance proof
```

The validator is fail closed for unsupported extraction syntax and source/serialization disagreement. It does not generate or rewrite the registry and does not infer applicability, Pattern selection, satisfaction, compliance, verification or closure.

rc5 adds sixteen trace-validator regressions. The frozen v0.0.4 executable-governance inventory remains separately unchanged at 41 tests; the rc5 development tool is not retroactively added to the frozen six-artifact CI trust bundle.

See [`docs/executable-governance/18_SCAF_v0.0.5rc5_L3_Source_Aware_Trace_Validator_Foundation.md`](docs/executable-governance/18_SCAF_v0.0.5rc5_L3_Source_Aware_Trace_Validator_Foundation.md).

## Authority and Trace Boundaries

SCAF keeps these meanings distinct:

```text
Frozen Markdown semantic authority
        !=
authority-registry / schema conformance
        !=
L3 machine-readable trace representation
        !=
frozen-source byte identity
        !=
external identity trust input
        !=
CI executor / enforcement policy
```

For L2-to-L3 catalog trace, the accepted relation classes are:

- `primary_realization_candidate`;
- `supporting_realization`;
- `constraint_input`.

The generic relation `satisfies` is prohibited.

A trace or resolver result does not by itself mean:

```text
Applicable
Selected
Satisfied
Compliant
Verified
Closed
```

Those meanings remain governed by the frozen authority, project decision, realization, verification/evidence and closure semantics.

## Executable Governance

The frozen v0.0.4 baseline provides four executable controls:

```text
scaf_validator
scaf_release_integrity
scaf_external_pin
scaf_ci_gate
```

Canonical local checks:

```text
python -m tools.scaf_validator.validator
python -m tools.scaf_release_integrity.checker
python -m unittest discover -s tools/scaf_validator/tests -v
python -m unittest discover -s tools/scaf_release_integrity/tests -v
python -m unittest discover -s tools/scaf_external_pin/tests -v
python -m unittest discover -s tools/scaf_ci_gate/tests -v
```

Accepted regression inventory remains:

```text
8 validator tests
9 release-integrity tests
11 external-pin tests
13 CI-gate tests
41 total
```

Current v0.0.5 development control:

```text
python -m tools.scaf_trace_validator.validator
python -m unittest discover -s tools/scaf_trace_validator/tests -v
```

The trace-validator suite adds 16 development regressions while the frozen v0.0.4 inventory remains 41.

The production CI gate additionally requires the reviewed repository-external trust input defined by the frozen v0.0.4 executable-governance baseline.

## Repository Navigation

| Path | Purpose |
|---|---|
| `docs/normative/` | Frozen v0.0.2 L1/L2 semantic authority |
| `docs/l3/` | Frozen v0.0.3 L3 Pattern / Mechanism Catalog |
| `docs/executable-governance/` | Machine-readable/executable-governance contracts, decisions and freeze records |
| `authority-registry.yaml` | Frozen v0.0.4 294-record authority representation |
| `l3-trace-registry.yaml` | Accepted v0.0.5rc3 subordinate serialization of frozen L3 typed trace relations |
| `schemas/l3-trace-registry.schema.json` | Accepted rc4 structural contract for the L3 trace registry |
| `tools/scaf_trace_validator/` | rc5 source-aware trace validation development control and regressions |
| `schemas/` | Frozen v0.0.4 authority-registry schema plus v0.0.5rc4 L3 trace structural schema |
| `release-integrity/` | Frozen-baseline integrity manifest |
| `tools/scaf_validator/` | Frozen v0.0.4 authority-registry semantic / structural / source-aware validator; not the rc4 trace validator |
| `tools/scaf_release_integrity/` | Frozen-source byte-integrity checker |
| `tools/scaf_external_pin/` | External identity-pin verification |
| `tools/scaf_ci_gate/` | Executable-governance CI orchestration |
| `.github/workflows/` | Trusted-main/manual CI executor |
| `CHANGELOG.md` | Release / RC / review / finding history |

## Source Position

SCAF keeps source classes distinct:

1. Gen1 formal baseline — `host-device-control-framework`;
2. supplemental resilience source — `Embedded_Incident_Crash_Recorder_Framework`;
3. independent architecture reviews — correction evidence, not normative source;
4. SCAF-new architecture decisions — controlled additions where donor material is insufficient.

Source provenance and source maturity are preserved rather than silently merged.

## Project Application

SCAF does not automatically decide project applicability or project architecture.

A project remains responsible for controlled decisions such as:

- which Project-Applicable Obligations are applicable;
- what architecture/mechanism is selected;
- what adaptation is required;
- how realization is performed;
- what verification/evidence establishes the required property;
- who has closure authority.

Catalog availability and machine-readable trace are navigation/decision-support inputs, not automatic project authority.

## Documentation Policy

- `README.md` describes the **current framework state and navigation**.
- `CHANGELOG.md` contains **version/RC evolution, review gates and finding history**.
- detailed controlled decisions and evidence remain under `docs/`.

This separation is intentional so the repository entry point does not become a duplicate release-history document.

## Release Policy

- RC work uses controlled `vX.Y.ZrcN` development releases.
- A formal baseline is created only after its required review gates and an explicit governance freeze decision.
- Frozen baselines are immutable; later work starts on a new controlled line.

## License / Disclaimer

See [`LICENSE`](LICENSE).

The framework and accompanying materials are provided **AS IS**, without warranty. Unless explicitly granted by the repository license terms, no additional license, certification, compliance claim, safety approval, or fitness-for-purpose representation is implied.
