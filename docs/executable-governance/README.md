# SCAF Executable Governance Baseline

**Release:** v0.0.4  
**Status:** Frozen Executable Governance Baseline  
**Upstream Baselines:** frozen v0.0.2 L1/L2; frozen v0.0.3 L3

## v0.0.7 Development

The v0.0.7 line starts from formal frozen `v0.0.6` and does not modify the frozen Project Application / Effective Project Profile baseline.

Current controlled records:

- `40_SCAF_v0.0.7rc01_Effective_Project_Profile_Consumption_Semantic_Foundation.md` — accepted semantic boundary for downstream consumption, filtering, reporting, and future context-selection use of validated Effective Project Profile state without transferring engineering authority.
- `41_SCAF_v0.0.7rc02_Canonical_Consumption_Context_Selection_Model_Foundation.md` — accepted canonical representation-neutral logical model for source-bound consumption selection, deterministic eligibility, included entries, predicate exclusion, bounded omission, and complete/filtered classification.
- `42_SCAF_v0.0.7rc03_Canonical_Consumption_Context_Selection_Machine_Readable_Representation_Foundation.md` — accepted canonical YAML representation of the logical model, with exact source-profile binding, bounded selectors/omission, selected-entry fidelity, deterministic ordering, and no redundant E/O/X truth lists.
- `43_SCAF_v0.0.7rc04_Consumption_Selection_Schema_Foundation.md` — accepted JSON Schema Draft 2020-12 foundation for the rc03 parsed representation shape.
- `44_SCAF_v0.0.7rc05_Consumption_Selection_Source_Aware_Validator_Foundation.md` — accepted source-aware executable validator for raw-YAML/canonical order, rc04 schema, frozen bound-profile proof, exact provenance, selector/domain membership, selected-entry fidelity, D/E/I/O/X, omission consistency, and complete/filtered derivation.
- `45_SCAF_v0.0.7rc06_Deterministic_Consumption_Selection_Builder_Foundation.md` — accepted deterministic builder over one validated profile plus explicit bounded selection/omission inputs, with mandatory rc05 self-validation.
- `46_SCAF_v0.0.7rc07_Consumption_Selection_Milestone_Consolidation_and_Freeze_Candidate.md` — consolidation-only freeze candidate for the accepted rc01→rc06 Consumption Selection chain, clean review history, regression inventory, authority boundary, and deferred scope.

rc07 adds no executable capability. It consolidates the accepted Consumption Selection milestone and keeps ranking/token-budget policy, context-source resolution, AI context package/orchestration, CI completion enforcement, L4 guidance, and Development Context Recovery separately gated. A clean rc07 review establishes freeze eligibility only.

## Frozen v0.0.6 Milestone

`v0.0.6 — Frozen Machine-Readable Project Application and Effective Project Profile Baseline` is the formal baseline promoted from the cleanly reviewed `v0.0.6rc14` freeze candidate by explicit governance decision on 2026-08-18.

Accepted freeze-candidate review state:

```text
Critical / Major / Minor / Trivial: 0 / 0 / 0 / 0
V0.0.6 PROJECT APPLICATION / EFFECTIVE PROJECT PROFILE
MILESTONE CONSOLIDATION / FREEZE-CANDIDATE GATE: YES
```

The formal freeze is release-state/documentation-only relative to committed rc14. It adds no semantic or executable capability and changes no accepted representation, schema, validator, query, generator, frozen source, workflow, trust boundary, or regression implementation.

v0.0.6 controlled records:

- `25_SCAF_v0.0.6rc01_SCAF_APP_Machine_Readable_Project_Application_Semantic_Model_Foundation.md` — accepted machine-readable SCAF-APP Project Application semantic-model foundation;
- `26_SCAF_v0.0.6rc02_SCAF_APP_Canonical_Project_Application_Record_Model.md` — canonical logical record model whose independent review opened `SCAF-RC02-001` / `SCAF-RC02-002`;
- `27_SCAF_v0.0.6rc03_SCAF_APP_Project_Application_Record_Basis_Role_and_State_Compatibility_Hardening.md` — accepted closure of the rc02 findings;
- `28_SCAF_v0.0.6rc04_SCAF_APP_Concrete_Project_Application_Serialization_Foundation.md` — accepted YAML serialization; review opened `SCAF-RC04-001`;
- `29_SCAF_v0.0.6rc05_Project_Application_Serialization_Fixture_Coverage_Hardening.md` — accepted closure of `SCAF-RC04-001`;
- `30_SCAF_v0.0.6rc06_Project_Application_Schema_Foundation.md` — accepted Project Application schema;
- `31_SCAF_v0.0.6rc07_Project_Application_Validator_Foundation.md` — accepted Project Application representation/source-aware validator;
- `32_SCAF_v0.0.6rc08_Project_Application_Validated_Read_Query_View_Foundation.md` — accepted validation-owning Project Application query views;
- `33_SCAF_v0.0.6rc09_Effective_Project_Profile_Semantic_Foundation.md` — accepted Effective Project Profile semantics;
- `34_SCAF_v0.0.6rc10_Effective_Project_Profile_Canonical_Representation_Foundation.md` — accepted canonical Effective Project Profile representation;
- `35_SCAF_v0.0.6rc11_Effective_Project_Profile_Schema_Foundation.md` — accepted Effective Project Profile schema;
- `36_SCAF_v0.0.6rc12_Effective_Project_Profile_Source_Aware_Validator_Foundation.md` — accepted Effective Project Profile source-aware validator;
- `37_SCAF_v0.0.6rc13_Effective_Project_Profile_Deterministic_Generator_Foundation.md` — accepted deterministic validated Effective Project Profile generator;
- `38_SCAF_v0.0.6rc14_Project_Application_Effective_Project_Profile_Milestone_Consolidation_and_Freeze_Candidate.md` — reviewed consolidation-only freeze candidate;
- `39_SCAF_v0.0.6_Formal_Freeze_Decision.md` — formal explicit freeze decision and immutable baseline boundary.

The accepted review-covered regression inventory is:

```text
v0.0.6 development suites: 98 / 98 PASS
inherited frozen suites:    93 / 93 PASS
combined:                  191 / 191 PASS
```

Detailed version/review history remains in repository-root `CHANGELOG.md`.

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
        ↓
v0.0.6rc07 Project Application representation/source-aware validator foundation
        ↓
v0.0.6rc08 validated Project Application read/query views
        ↓
v0.0.6rc09 Effective Project Profile semantic foundation
        ↓
v0.0.6rc10 Effective Project Profile canonical representation foundation
        ↓
v0.0.6rc11 Effective Project Profile JSON Schema foundation
        ↓
v0.0.6rc12 Effective Project Profile source-aware validator foundation
        ↓
v0.0.6rc13 Effective Project Profile deterministic generator foundation
        ↓
frozen v0.0.6 machine-readable Project Application / Effective Project Profile baseline
        ↓
v0.0.7rc01 Effective Project Profile consumption semantic foundation
        ↓
v0.0.7rc02 canonical consumption / context-selection logical model
        ↓
v0.0.7rc03 canonical consumption / context-selection YAML representation
        ↓
v0.0.7rc04 Consumption Selection JSON Schema foundation
        ↓
v0.0.7rc05 Consumption Selection source-aware validator
        ↓
v0.0.7rc06 deterministic validated Consumption Selection builder
        ↓
v0.0.7rc07 milestone consolidation / freeze candidate
```

The formal v0.0.6 freeze adds no executable capability beyond the reviewed rc14 state. `v0.0.7rc01` defines accepted consumption semantics, rc02 canonical logical accounting, rc03 canonical YAML representation, rc04 parsed-instance schema validation, rc05 source-aware validation, rc06 deterministic validated construction, and rc07 consolidation-only freeze candidacy. Persistent selection/context state, AI context packaging, context-source or scope/reference resolution, applicability inference, Pattern selection, CI completion enforcement, engineering judgment, compliance, verification, completion and closure remain separately gated.
