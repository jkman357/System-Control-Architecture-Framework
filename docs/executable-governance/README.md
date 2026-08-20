# SCAF Executable Governance Baseline

**Release:** v0.0.4  
**Status:** Frozen Executable Governance Baseline  
**Upstream Baselines:** frozen v0.0.2 L1/L2; frozen v0.0.3 L3

## Active v0.0.10 Development

`v0.0.10rc01 — Controlled Context Assembly Semantic Foundation` defined the downstream semantic boundary between validated authority/source-association truth and bounded consumer context. Its independent review returned clean `PASS / GATE YES` with zero findings and no blocking evidence limitations.

`v0.0.10rc02 — Canonical Controlled Context Package Logical Model Foundation` fixed the representation-neutral package aggregate, authority/association totality, per-association materialization accounting, package-local item identity and controlled provenance. Its independent review also returned clean `PASS / GATE YES` with zero candidate-source findings and zero blocking review-evidence limitations.

`v0.0.10rc03 — Canonical Controlled Context Package Machine-Readable Representation Foundation` serializes that accepted logical model as one deterministic YAML representation before any package schema, validator or builder.

Canonical representation chain:

```text
exact validated Consumption Selection
        ↓
exact validated Context Source Association Set
        ↓
examples/controlled-context-package.yaml
        ├─ upstream_binding
        ├─ assembly_objective
        ├─ authority_context_entries [exactly one per validated I]
        │    ├─ association_envelope
        │    └─ materialization_decisions [exactly one per association]
        └─ materialized_context_items [0..n]
             └─ controlled provenance bases [1..n]
```

Key rc03 invariants include:

```text
association_handle = package-local reference only, not upstream association identity
Authority Context Entry domain = validated I exactly
association envelope = exact accepted upstream association truth
accepted association -> exactly one Materialization Decision
not_materialized -> [] item refs + explicit controlled basis
Materialized Context Item != Source Unit / Controlled Source Association
item provenance <-> referencing Materialization Decision correspondence
source_preserving != derived; derived != authoritative source truth
payload boundary = source_reference only in rc03
package representation != schema validity != source-aware package consistency
package conformance != engineering-context sufficiency
controlled association truth != package materialization truth != runtime observation
machine-readable != machine-decided
```

The RC introduces no package schema, production validator, builder, content loader, inline source content, fragment/chunk syntax, summarization algorithm, ranking/token-budget policy, prompt/model integration, general Source Resolver, currentness model, CI gate, authority-registry change, new PAO/FNI or L4 guidance.

See:

- [`56_SCAF_v0.0.10rc01_Controlled_Context_Assembly_Semantic_Foundation.md`](56_SCAF_v0.0.10rc01_Controlled_Context_Assembly_Semantic_Foundation.md)
- [`57_SCAF_v0.0.10rc02_Canonical_Controlled_Context_Package_Logical_Model_Foundation.md`](57_SCAF_v0.0.10rc02_Canonical_Controlled_Context_Package_Logical_Model_Foundation.md)
- [`58_SCAF_v0.0.10rc03_Canonical_Controlled_Context_Package_Machine_Readable_Representation_Foundation.md`](58_SCAF_v0.0.10rc03_Canonical_Controlled_Context_Package_Machine_Readable_Representation_Foundation.md)

A clean rc03 review authorizes only a new dependency/value assessment; it does not pre-authorize rc04 or a package schema.

## Frozen v0.0.9 Milestone

`v0.0.9 — Frozen Context Source Association and Source-Aware Validation Baseline` is promoted from the cleanly reviewed `v0.0.9rc05` source state after explicit governance approval and a dependency/value `STOP` decision.

Accepted chain:

```text
rc01 source-resolution semantics
  ↓
rc02 canonical logical model
  ↓
rc03 canonical deterministic YAML
  ↓
rc04 parsed-instance JSON Schema
  ↓
rc05 production source-aware validator
  ↓
formal v0.0.9 freeze
```

The frozen boundaries remain:

```text
controlled association truth != runtime resolution observation
parsed-instance structural validity != source-aware consistency != engineering correctness
validator != general Source Resolver
```

The clean corrected rc05 review returned `PASS / GATE YES` with zero candidate-source findings and zero blocking review-evidence limitations. Executed evidence included rc05 `25 / 25 PASS`, direct upstream Consumption Selection `37 / 37 PASS`, all required production checks PASS and `git diff --check` PASS.

v0.0.9 controlled records:

- `50_SCAF_v0.0.9rc01_Context_Source_Resolution_Semantic_Foundation.md` — accepted Context Source Resolution semantics.
- `51_SCAF_v0.0.9rc02_Canonical_Context_Source_Association_Logical_Model_Foundation.md` — accepted canonical representation-neutral logical model.
- `52_SCAF_v0.0.9rc03_Canonical_Context_Source_Association_Machine_Readable_Representation_Foundation.md` — accepted deterministic YAML representation.
- `53_SCAF_v0.0.9rc04_Context_Source_Association_Schema_Foundation.md` — accepted parsed-instance JSON Schema foundation.
- `54_SCAF_v0.0.9rc05_Context_Source_Association_Source_Aware_Validator_Foundation.md` — accepted production source-aware validation boundary.
- `55_SCAF_v0.0.9_Formal_Freeze_Decision.md` — formal explicit freeze decision and immutable baseline boundary.

The post-rc05 dependency/value assessment found no current material dependency requiring a general Source Resolver or downstream Context Assembly. Resolver/discovery/currentness/runtime-observation/content/AI-context/CI/L4 work remains separately gated and is not authorized by the freeze.

## Frozen v0.0.8 Milestone

`v0.0.8 — Frozen Lifecycle-Proportional Governance Semantic Baseline` is the formal semantic baseline promoted from the cleanly reviewed `v0.0.8rc01` source state after explicit governance approval and the required dependency/value STOP assessment.

Accepted rc01 review state:

```text
Critical / Major / Minor / Trivial: 0 / 0 / 0 / 0
Open review-evidence limitations: 0
V0.0.8RC01 LIFECYCLE-PROPORTIONAL GOVERNANCE
SEMANTIC FOUNDATION GATE: YES
```

The frozen semantic boundary establishes:

```text
Current Decision Horizon = subject-scoped + next-action-scoped
governance depth proportional to current decision / consequence / available evidence
not-yet-producible empirical evidence != automatic current blocker
progression sufficient != complete / verified / compliant / released / closed
engineering impact != current progression disposition
deferred != resolved / waived / closed
all Materiality Stop Rule answers NO -> theoretical completeness alone is non-blocking
```

The post-review dependency/value assessment applied that same stop rule to SCAF itself and concluded that no rc02 was required for this milestone. The formal freeze therefore demonstrates SCAF self-application rather than automatically extending the RC line for theoretical completeness.

v0.0.8 controlled records:

- `48_SCAF_v0.0.8rc01_Lifecycle_Proportional_Governance_Semantic_Foundation.md` — accepted Current Decision Horizon, governance proportionality, evidence availability, Progression Sufficiency, Materiality Stop Rule, impact/disposition separation, controlled deferral/revisit and SCAF self-application semantics.
- `49_SCAF_v0.0.8_Formal_Freeze_Decision.md` — formal explicit freeze decision, dependency/value STOP disposition and immutable v0.0.8 boundary.

The baseline adds no lifecycle state machine, machine-readable disposition record, schema, validator, CI gate, authority-registry promotion, Context Source Resolution or AI context mechanism. Frozen L3 Pattern `M0`→`M4` maturity, existing authority ownership and the `294 / 218 / 76` authority inventory remain unchanged.

## Frozen v0.0.7 Milestone

`v0.0.7 — Frozen Consumption Selection Baseline` is the formal baseline promoted from the cleanly reviewed `v0.0.7rc07` freeze candidate by explicit governance decision on 2026-08-19.

Accepted freeze-candidate review state:

```text
Critical / Major / Minor / Trivial: 0 / 0 / 0 / 0
V0.0.7 CONSUMPTION SELECTION MILESTONE
CONSOLIDATION / FREEZE-CANDIDATE GATE: YES
```

The formal freeze is release-state/documentation-only relative to committed rc07. It adds no semantic or executable capability and changes no accepted representation, schema, validator, builder, frozen source, workflow, trust boundary, or regression implementation.

v0.0.7 controlled records:

- `40_SCAF_v0.0.7rc01_Effective_Project_Profile_Consumption_Semantic_Foundation.md` — accepted semantic boundary for downstream consumption, filtering, reporting, and future context-selection use of validated Effective Project Profile state without transferring engineering authority.
- `41_SCAF_v0.0.7rc02_Canonical_Consumption_Context_Selection_Model_Foundation.md` — accepted canonical representation-neutral logical model for source-bound consumption selection, deterministic eligibility, included entries, predicate exclusion, bounded omission, and complete/filtered classification.
- `42_SCAF_v0.0.7rc03_Canonical_Consumption_Context_Selection_Machine_Readable_Representation_Foundation.md` — accepted canonical YAML representation of the logical model, with exact source-profile binding, bounded selectors/omission, selected-entry fidelity, deterministic ordering, and no redundant E/O/X truth lists.
- `43_SCAF_v0.0.7rc04_Consumption_Selection_Schema_Foundation.md` — accepted JSON Schema Draft 2020-12 foundation for the rc03 parsed representation shape.
- `44_SCAF_v0.0.7rc05_Consumption_Selection_Source_Aware_Validator_Foundation.md` — accepted source-aware executable validator for raw-YAML/canonical order, rc04 schema, frozen bound-profile proof, exact provenance, selector/domain membership, selected-entry fidelity, D/E/I/O/X, omission consistency, and complete/filtered derivation.
- `45_SCAF_v0.0.7rc06_Deterministic_Consumption_Selection_Builder_Foundation.md` — accepted deterministic builder over one validated profile plus explicit bounded selection/omission inputs, with mandatory rc05 self-validation.
- `46_SCAF_v0.0.7rc07_Consumption_Selection_Milestone_Consolidation_and_Freeze_Candidate.md` — reviewed consolidation-only freeze candidate for the accepted rc01→rc06 Consumption Selection chain, clean review history, regression inventory, authority boundary, and deferred scope.
- `47_SCAF_v0.0.7_Formal_Freeze_Decision.md` — formal explicit freeze decision and immutable v0.0.7 baseline boundary.

The accepted current milestone review execution inventory is:

```text
rc06 builder:                 34 / 34 PASS
rc05 validator:               37 / 37 PASS
inherited accepted/frozen:   191 / 191 PASS
combined current inventory:  262 tests PASS
```

The historical inherited/frozen baseline remains 191. Context-source resolution, ranking/token-budget policy, AI context packaging/orchestration, CI completion enforcement, L4 guidance, and Development Context Recovery remain separately gated and outside frozen v0.0.7.

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
        ↓
frozen v0.0.7 Consumption Selection baseline
        ↓
v0.0.8rc01 Lifecycle-Proportional Governance semantic foundation
        ↓
dependency/value STOP assessment — no rc02 required
        ↓
frozen v0.0.8 Lifecycle-Proportional Governance Semantic baseline
```

The formal v0.0.8 freeze adds no executable capability beyond the reviewed rc01 source state. The milestone intentionally stops after one clean semantic RC plus dependency/value assessment: no machine-readable governance representation, schema, validator, CI progression gate, authority-registry promotion, Context Source Resolution or AI context mechanism is authorized by this freeze. Such capabilities remain separately gated and require a future Current Decision Horizon and value justification.
