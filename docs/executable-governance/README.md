# SCAF Executable Governance Baseline

**Release:** v0.0.4  
**Status:** Frozen Executable Governance Baseline  
**Upstream Baselines:** frozen v0.0.2 L1/L2; frozen v0.0.3 L3

## Current Development Line

`v0.0.5rc9 — L3 Trace Views Authority Validation and CLI Execution Boundary Closure` follows the rc8 independent review. That review confirmed `RC7-01: RESOLVED` and identified one new Major (`RC8-01`) plus one Minor (`RC8-02`).

rc9 is narrowly scoped to those findings:

- supported `query_l2(repo_root, l2_id)` and `query_pattern(repo_root, pattern_id)` now require both rc6 trace validation and the existing frozen authority-registry validator against the same repository root before context loading/projection;
- `tools.scaf_trace_views` uses lazy package re-exports so documented `python -m tools.scaf_trace_views.query` execution does not preload the target module;
- real subprocess regressions cover successful and invalid-repository documented CLI execution;
- frozen validators, frozen L1/L2/L3 sources, registries/schemas, release-integrity controls, CI controls and the production six-artifact trust set are not modified.

Current v0.0.5 records:

- `14_SCAF_v0.0.5rc1_L3_Machine_Readable_Trace_Representation_Model_Foundation.md` — accepted model foundation as amended by rc2;
- `15_SCAF_v0.0.5rc2_L3_Trace_Model_Determinism_and_Qualifier_Fidelity_Cleanup.md` — accepted `R1-01` / `R1-02` closure;
- `16_SCAF_v0.0.5rc3_L3_Machine_Readable_Trace_Serialization_Foundation.md` — accepted concrete serialization contract;
- `17_SCAF_v0.0.5rc4_L3_Trace_Schema_and_Source_Extraction_Contract_Foundation.md` — accepted schema/extraction contract;
- `18_SCAF_v0.0.5rc5_L3_Source_Aware_Trace_Validator_Foundation.md` — historical rc5 validator foundation reviewed with gate `NO` / `R5-01` + `R5-02`;
- `19_SCAF_v0.0.5rc6_L3_Trace_Validator_Fail_Closed_Source_Boundary_Hardening.md` — accepted `R5-01` / `R5-02` closure;
- `20_SCAF_v0.0.5rc7_L3_Deterministic_Trace_Views_and_Query_Foundation.md` — trace-consumption foundation reviewed with gate `NO` / `RC7-01`;
- `21_SCAF_v0.0.5rc8_L3_Trace_Views_Validated_Programmatic_API_Boundary_Hardening.md` — `RC7-01` closure candidate; review confirmed closure but opened `RC8-01` / `RC8-02`;
- `22_SCAF_v0.0.5rc9_L3_Trace_Views_Authority_Validation_and_CLI_Execution_Boundary_Closure.md` — current focused rc8 finding-closure candidate.

Detailed version/review history remains in repository-root `CHANGELOG.md`.

## Frozen v0.0.4 Position

The v0.0.4 baseline remains frozen. Its semantic validator, release-integrity checker, external-pin checker, CI gate, manifest, schema and workflow trust model are not changed by rc9.

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
current rc9 same-root authority/trace proof closure + clean CLI execution
```

No later enforcement, applicability inference, recommendation, selection, generated index, code generation, signing/provenance, or L4 scope is implied by rc9.
