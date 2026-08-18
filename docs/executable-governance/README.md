# SCAF Executable Governance Baseline

**Release:** v0.0.4  
**Status:** Frozen Executable Governance Baseline  
**Upstream Baselines:** frozen v0.0.2 L1/L2; frozen v0.0.3 L3

## Active v0.0.6 Development

`v0.0.6rc06 — Project Application Schema Foundation` continues the controlled line after the independent rc05 review returned a clean `GATE: YES`, closed `SCAF-RC04-001`, and reported zero new findings.

rc06 adds `schemas/project-application.schema.json` as the first formal JSON Schema Draft 2020-12 encoding of the accepted rc04 Project Application representation contract. The concrete representation remains identified by `representation_release: v0.0.6rc04`; rc06 is a schema release, not a new serialization-contract revision.

The schema encodes machine-determinable parsed-instance facts such as required fields/types, exact applicability tokens, state-dependent `disposition_basis` presence/prohibition, direct-basis structural sufficiency for resolved states, null/type constraints, and exact-duplicate rejection within role-specific reference lists.

Schema-only validation intentionally does not claim proof of raw-YAML duplicate-key/anchor restrictions, lexical list/record ordering, cross-record `record_id` or authority/scope uniqueness, authority/reference existence, engineering rationale correctness, Project Design Authority sufficiency, verification, compliance, or closure. Those remain separate loader/validator/source-aware/engineering boundaries.

No Project Application validator, resolver, automatic applicability decision, Pattern selector, Effective Project Profile, CI completion gate or L4 content is introduced.

Controlled records:

- `25_SCAF_v0.0.6rc01_SCAF_APP_Machine_Readable_Project_Application_Semantic_Model_Foundation.md` — accepted machine-readable SCAF-APP Project Application semantic-model foundation;
- `26_SCAF_v0.0.6rc02_SCAF_APP_Canonical_Project_Application_Record_Model.md` — canonical logical record model whose independent review opened `SCAF-RC02-001` / `SCAF-RC02-002`;
- `27_SCAF_v0.0.6rc03_SCAF_APP_Project_Application_Record_Basis_Role_and_State_Compatibility_Hardening.md` — accepted closure of the rc02 basis-role and state-compatibility findings;
- `28_SCAF_v0.0.6rc04_SCAF_APP_Concrete_Project_Application_Serialization_Foundation.md` — accepted concrete YAML serialization foundation; independent review opened `SCAF-RC04-001` (Minor fixture coverage);
- `29_SCAF_v0.0.6rc05_Project_Application_Serialization_Fixture_Coverage_Hardening.md` — accepted closure of `SCAF-RC04-001`;
- `30_SCAF_v0.0.6rc06_Project_Application_Schema_Foundation.md` — formal Project Application schema foundation review candidate.

## Frozen v0.0.5 Milestone

`v0.0.5 — Frozen L3 Machine-Readable Traceability Baseline` is the formal baseline promoted from the cleanly reviewed `v0.0.5rc10` freeze candidate by explicit governance decision on 2026-08-18.

Accepted freeze-candidate review state:

```text
Critical / Major / Minor / Trivial: 0 / 0 / 0 / 0
V0.0.5 L3 MACHINE-READABLE TRACEABILITY MILESTONE CONSOLIDATION / FREEZE-CANDIDATE GATE: YES
```

The formal freeze is release-state/documentation-only relative to rc10. It adds no semantic or executable capability and changes no registry, schema, validator, trace-view/query code, workflow, trust-set artifact, frozen source, or regression implementation.

v0.0.5 controlled records:

- `14_SCAF_v0.0.5rc1_L3_Machine_Readable_Trace_Representation_Model_Foundation.md` — trace representation model foundation;
- `15_SCAF_v0.0.5rc2_L3_Trace_Model_Determinism_and_Qualifier_Fidelity_Cleanup.md` — `R1-01` / `R1-02` closure;
- `16_SCAF_v0.0.5rc3_L3_Machine_Readable_Trace_Serialization_Foundation.md` — accepted 119-relation concrete serialization;
- `17_SCAF_v0.0.5rc4_L3_Trace_Schema_and_Source_Extraction_Contract_Foundation.md` — accepted schema/extraction contract;
- `18_SCAF_v0.0.5rc5_L3_Source_Aware_Trace_Validator_Foundation.md` — historical validator foundation review with `R5-01` / `R5-02`;
- `19_SCAF_v0.0.5rc6_L3_Trace_Validator_Fail_Closed_Source_Boundary_Hardening.md` — accepted `R5-01` / `R5-02` closure;
- `20_SCAF_v0.0.5rc7_L3_Deterministic_Trace_Views_and_Query_Foundation.md` — deterministic read-only consumption foundation; review opened `RC7-01`;
- `21_SCAF_v0.0.5rc8_L3_Trace_Views_Validated_Programmatic_API_Boundary_Hardening.md` — `RC7-01` closure; review opened `RC8-01` / `RC8-02`;
- `22_SCAF_v0.0.5rc9_L3_Trace_Views_Authority_Validation_and_CLI_Execution_Boundary_Closure.md` — accepted `RC8-01` / `RC8-02` closure after clean full-source re-review;
- `23_SCAF_v0.0.5rc10_L3_Machine_Readable_Traceability_Milestone_Consolidation_and_Freeze_Candidate.md` — reviewed consolidation-only freeze candidate;
- `24_SCAF_v0.0.5_Formal_Freeze_Decision.md` — formal explicit freeze decision and immutable baseline boundary.

Detailed version/review history remains in repository-root `CHANGELOG.md`.

## Frozen v0.0.4 Position

The v0.0.4 baseline remains frozen. Its semantic validator, release-integrity checker, external-pin checker, CI gate, manifest, schema and workflow trust model are not changed by v0.0.5 formal freeze.

The accepted frozen regression inventory remains 41 tests:

```text
scaf_validator           8
scaf_release_integrity   9
scaf_external_pin       11
scaf_ci_gate            13
Total                   41
```

Semantic validation, frozen-byte integrity and repository-external identity pinning remain separate controls.

## Development Order

```text
frozen semantic authority
        ↓
accepted machine-readable authority representation + frozen validator
        ↓
accepted L3 machine-readable trace representation
        ↓
accepted trace schema + source extraction contract
        ↓
accepted source-aware trace validator
        ↓
validated deterministic read-only trace consumption
        ↓
accepted rc9 same-root authority/trace proof closure + clean CLI execution
        ↓
frozen v0.0.5 machine-readable traceability baseline
        ↓
v0.0.6rc01 SCAF-APP machine-readable Project Application semantic foundation
        ↓
v0.0.6rc02 canonical Project Application logical record model
        ↓
v0.0.6rc03 applicability-basis role + state-compatibility finding closure
        ↓
v0.0.6rc04 concrete Project Application YAML serialization foundation
        ↓
v0.0.6rc05 serialization fixture multi-item coverage hardening
        ↓
v0.0.6rc06 Project Application JSON Schema foundation
```

No automatic applicability inference, recommendation, selection, Project Application validator, generated index, code generation, signing/provenance, CI completion enforcement, or L4 scope is implied by rc06. Validator/source-resolution work remains separately gated and review-driven.
