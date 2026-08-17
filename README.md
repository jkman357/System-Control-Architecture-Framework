# System Control Architecture Framework (SCAF)

**Current Development Release:** v0.0.5rc2  
**Status:** L3 Trace Model Determinism & Qualifier-Fidelity Cleanup  
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
| `v0.0.5rc2` | Focused determinism / qualifier-fidelity cleanup of the L3 trace representation model |

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

## Current v0.0.5rc2 Development Focus

The frozen v0.0.3 L3 catalog already contains authoritative human-readable L2-to-L3 trace metadata for twelve published Patterns.

Current frozen trace inventory:

```text
12 Pattern identities
23 Primary Realization Candidate references
41 Supporting Realization references
55 Constraint Input references
119 total trace relations
82 unique referenced frozen L2 IDs
```

`v0.0.5rc1` defined how those existing trace semantics may later be represented machine-readably without creating a second semantic authority. The independent rc1 review returned `YES, AFTER MINOR CLEANUP`; `v0.0.5rc2` is the bounded cleanup for material qualifier fidelity and canonical deterministic ordering.

The intended boundary is:

```text
Frozen L3 Pattern Markdown metadata
        ↓ semantic trace authority
Machine-readable L3 trace representation
        ↓ subordinate representation
Generated forward/reverse navigation views
        ↓ derived only
Future resolver/context consumption
```

The current RC does **not** serialize the 119 relations, introduce a trace schema/validator implementation, generate a reverse index, infer project applicability, select Patterns, claim satisfaction/compliance, add L4 guidance, or modify the existing `authority-registry.yaml` relation state. It only makes qualifier preservation enforceable at the future model/validator-contract level and makes canonical ordering mandatory.

See [`docs/executable-governance/14_SCAF_v0.0.5rc1_L3_Machine_Readable_Trace_Representation_Model_Foundation.md`](docs/executable-governance/14_SCAF_v0.0.5rc1_L3_Machine_Readable_Trace_Representation_Model_Foundation.md) and [`docs/executable-governance/15_SCAF_v0.0.5rc2_L3_Trace_Model_Determinism_and_Qualifier_Fidelity_Cleanup.md`](docs/executable-governance/15_SCAF_v0.0.5rc2_L3_Trace_Model_Determinism_and_Qualifier_Fidelity_Cleanup.md).

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

The production CI gate additionally requires the reviewed repository-external trust input defined by the frozen v0.0.4 executable-governance baseline.

## Repository Navigation

| Path | Purpose |
|---|---|
| `docs/normative/` | Frozen v0.0.2 L1/L2 semantic authority |
| `docs/l3/` | Frozen v0.0.3 L3 Pattern / Mechanism Catalog |
| `docs/executable-governance/` | Machine-readable/executable-governance contracts, decisions and freeze records |
| `authority-registry.yaml` | Frozen v0.0.4 294-record authority representation |
| `schemas/` | Frozen v0.0.4 authority-registry schema |
| `release-integrity/` | Frozen-baseline integrity manifest |
| `tools/scaf_validator/` | Semantic / structural / source-aware validator |
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
