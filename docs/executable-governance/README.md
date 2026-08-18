# SCAF Executable Governance Baseline

**Release:** v0.0.4  
**Status:** Frozen Executable Governance Baseline  
**Upstream Baselines:** frozen v0.0.2 L1/L2; frozen v0.0.3 L3

## Active v0.0.6 Development

`v0.0.6rc03 — SCAF-APP Project Application Record Basis-Role and State-Compatibility Hardening` continues the controlled line after the independent rc02 review returned `GATE: NO` with one Major (`SCAF-RC02-001`) and one Minor (`SCAF-RC02-002`) finding and no frozen-baseline regression.

rc03 is finding-closure only. It makes `disposition_basis.summary` and `disposition_basis.basis_refs` the only direct applicability-basis surfaces. `decision_refs`, `authority_refs`, and `supporting_refs` retain separate decision-trace, authority-provenance, and supporting-context roles and cannot satisfy applicability basis merely by presence.

rc03 also freezes the state-compatibility contract: `unresolved_reason` is required exactly once for `undetermined`, `awaiting_refs` is optional only for `undetermined`, and both members are prohibited for `applicable` / `not_applicable` current-state records. Historical unresolved context remains deferred to a separately reviewed history/supersession/re-evaluation model.

The Project Application Record remains a project-side disposition/trace surface. It does not become Project Design Authority, verification/risk/deviation/evidence/closure authority, and `undetermined` remains legitimate engineering-unresolved state distinct from representation invalidity.

rc03 intentionally adds no concrete project-application registry/dataset, schema, validator, project-scope registry, automatic applicability decision, Pattern selector, Effective Project Profile, CI completion gate or L4 content.

Controlled records:

- `25_SCAF_v0.0.6rc01_SCAF_APP_Machine_Readable_Project_Application_Semantic_Model_Foundation.md` — accepted machine-readable SCAF-APP Project Application semantic-model foundation;
- `26_SCAF_v0.0.6rc02_SCAF_APP_Canonical_Project_Application_Record_Model.md` — canonical logical record model whose independent review opened `SCAF-RC02-001` / `SCAF-RC02-002`;
- `27_SCAF_v0.0.6rc03_SCAF_APP_Project_Application_Record_Basis_Role_and_State_Compatibility_Hardening.md` — bounded closure of the rc02 basis-role and state-compatibility findings.

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
```

No automatic applicability inference, recommendation, selection, generated index, code generation, signing/provenance, CI completion enforcement, or L4 scope is implied by rc02. Concrete serialization/schema/validator work remains separately gated and review-driven.
