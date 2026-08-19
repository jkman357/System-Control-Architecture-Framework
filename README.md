# System Control Architecture Framework (SCAF)

**Current Formal Release:** v0.0.9
**Active Development RC:** v0.0.10rc02
**Status:** Canonical Controlled Context Package Logical Model Foundation / Review Candidate
**Date:** 2026-08-19

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
| `v0.0.6` | Frozen Machine-Readable Project Application and Effective Project Profile baseline |
| `v0.0.7` | Frozen Consumption Selection baseline |
| `v0.0.8` | Frozen Lifecycle-Proportional Governance Semantic baseline |
| `v0.0.9` | Frozen Context Source Association and Source-Aware Validation baseline |

The formal v0.0.9 baseline is now frozen and immutable. It promotes the independently reviewed `v0.0.9rc05` Context Source Association source-aware validation state after the required post-review dependency/value STOP assessment, without reopening earlier frozen authority, applicability, profile, selection, traceability, or lifecycle-proportional governance baselines.

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

The frozen L1/L2 and L3 layers remain canonical for their accepted scope. v0.0.6 does not reopen them.

## Active v0.0.10 Development

`v0.0.10rc01` established the representation-neutral **Controlled Context Assembly Semantic Foundation** and its independent review returned clean `PASS / GATE YES` with zero candidate-source findings and no blocking review-evidence limitations.

The post-rc01 dependency/value assessment identified one material pre-serialization ambiguity: different package implementations could preserve materially different authority, association-accounting and provenance models even while agreeing with the rc01 high-level semantics.

`v0.0.10rc02` therefore defines the **Canonical Controlled Context Package Logical Model** before any machine-readable representation or builder is introduced.

The governing logical shape is:

```text
exact validated Consumption Selection
        ↓
exact validated Context Source Association Set
        ↓
Controlled Context Package
        ├─ exact upstream binding
        ├─ one Assembly Objective
        ├─ one Authority Context Entry per validated I authority
        │    ├─ exact accepted Association Envelope
        │    └─ one Materialization Decision per association
        └─ 0..n traceable Materialized Context Items
```

The central package rule is that consumer-facing materialization may vary while validated authority and controlled association truth remain preserved. Package omission is explicit downstream accounting, not applicability or association removal; package conformance is not engineering sufficiency; derived context is not source authority; and context presented to AI does not grant engineering authority.

The RC remains representation-neutral. It adds no Context Package YAML/JSON, schema, validator, builder, loader, fragment/chunk policy, summarization algorithm, ranking/token-budget policy, prompt/model integration, general Source Resolver, CI gate, authority-registry change, new PAO/FNI or L4 guidance. A clean review authorizes only a new dependency/value assessment. See [`docs/executable-governance/56_SCAF_v0.0.10rc01_Controlled_Context_Assembly_Semantic_Foundation.md`](docs/executable-governance/56_SCAF_v0.0.10rc01_Controlled_Context_Assembly_Semantic_Foundation.md) and [`docs/executable-governance/57_SCAF_v0.0.10rc02_Canonical_Controlled_Context_Package_Logical_Model_Foundation.md`](docs/executable-governance/57_SCAF_v0.0.10rc02_Canonical_Controlled_Context_Package_Logical_Model_Foundation.md).

## Frozen v0.0.6 Milestone

The v0.0.6rc14 freeze-candidate review returned a clean gate `YES` with no findings:

```text
Critical: 0
Major:    0
Minor:    0
Trivial:  0

V0.0.6 PROJECT APPLICATION / EFFECTIVE PROJECT PROFILE
MILESTONE CONSOLIDATION / FREEZE-CANDIDATE GATE: YES
```

The explicit governance freeze decision therefore promotes the reviewed rc14 source state to formal **v0.0.6 — Frozen Machine-Readable Project Application and Effective Project Profile Baseline**.

The frozen milestone preserves the accepted chain from Project Application semantics/representation/schema/source-aware validation/query through Effective Project Profile semantics/representation/schema/source-aware validation and deterministic generation. It preserves exact-scope semantics, `undetermined != no_current_disposition`, validated-input ownership, source-snapshot provenance, no applicability inference, and Project Design Authority separation.

The accepted review-covered regression inventory is `191 / 191 PASS` (`98 / 98` v0.0.6 development tests plus `93 / 93` inherited frozen tests). The formal freeze adds no new semantic or executable capability beyond rc14. See [`docs/executable-governance/39_SCAF_v0.0.6_Formal_Freeze_Decision.md`](docs/executable-governance/39_SCAF_v0.0.6_Formal_Freeze_Decision.md).

## Frozen v0.0.7 Milestone

The v0.0.7rc07 freeze-candidate review returned a clean gate `YES` with no findings:

```text
Critical: 0
Major:    0
Minor:    0
Trivial:  0

V0.0.7 CONSUMPTION SELECTION MILESTONE
CONSOLIDATION / FREEZE-CANDIDATE GATE: YES
```

The explicit governance freeze decision therefore promotes the reviewed rc07 source state to formal **v0.0.7 — Frozen Consumption Selection Baseline**.

The frozen milestone preserves the accepted rc01→rc06 chain from downstream Effective Project Profile consumption semantics through the canonical logical model, canonical YAML representation, parsed-instance JSON Schema, source-aware validation, and deterministic validated construction. It preserves exact source-profile provenance, exact opaque scope, `D/E/I/O/X`, bounded omission, selected-entry source fidelity, and the authority boundaries `included != applicable`, `excluded/omitted != not_applicable`, `predicate excluded != bounded omitted`, and `undetermined != no_current_disposition`.

The current v0.0.7 milestone review execution inventory is `262 tests PASS` (`34 / 34` rc06 builder + `37 / 37` rc05 validator + inherited `191 / 191`). The historical inherited/frozen baseline remains 191. The formal freeze adds no semantic or executable capability beyond the reviewed rc07 candidate. See [`docs/executable-governance/47_SCAF_v0.0.7_Formal_Freeze_Decision.md`](docs/executable-governance/47_SCAF_v0.0.7_Formal_Freeze_Decision.md).

Context-source resolution, context-content records, AI context packaging/orchestration, ranking/token-budget policy, CI applicability-completion enforcement, L4 guidance, Development Context Recovery, and other separately gated capabilities are not part of the frozen v0.0.7 baseline.

## Frozen v0.0.8 Milestone

`v0.0.8rc01` established the representation-neutral **Lifecycle-Proportional Governance Semantic Foundation** and its independent review returned a clean `PASS / GATE YES` with zero findings and zero open review-evidence limitations. The subsequent dependency/value assessment applied the accepted Materiality Stop Rule to SCAF itself and concluded that no rc02 was required for this milestone.

The formal v0.0.8 baseline therefore freezes the subject-scoped **Current Decision Horizon**, governance proportionality, Evidence Availability Rule, Progression Sufficiency, the five-question Materiality Stop Rule, engineering-impact/current-progression-disposition separation, controlled deferral with explicit revisit triggers, reversibility/expensive-commitment reasoning, external-authority preservation, and SCAF self-application.

The central rule remains:

```text
Governance depth follows the current engineering decision,
the consequence of unresolved ambiguity,
and evidence reasonably available now.
```

The frozen baseline adds no global lifecycle state machine, machine-readable disposition representation, schema, validator, CI gate, authority-registry promotion, Context Source Resolution or AI context mechanism. Frozen L3 `M0`→`M4` Pattern maturity and the `294 / 218 / 76` authority inventory remain unchanged.

The formal freeze adds no semantic or executable capability beyond the reviewed rc01 source state. See [`docs/executable-governance/49_SCAF_v0.0.8_Formal_Freeze_Decision.md`](docs/executable-governance/49_SCAF_v0.0.8_Formal_Freeze_Decision.md).

## Frozen v0.0.9 Milestone

`v0.0.9 — Frozen Context Source Association and Source-Aware Validation Baseline` is the formal baseline promoted from the cleanly reviewed `v0.0.9rc05` source state after the required post-review dependency/value STOP assessment.

The accepted development chain is:

```text
rc01 Context Source Resolution semantics
  ↓
rc02 canonical logical model
  ↓
rc03 canonical deterministic YAML representation
  ↓
rc04 JSON Schema Draft 2020-12 structural contract
  ↓
rc05 production source-aware validator
  ↓
v0.0.9 formal freeze
```

The clean corrected rc05 independent review reported `PASS / GATE YES`, zero candidate-source findings and zero blocking review-evidence limitations. The reviewed source ZIP remained unchanged through the review-instruction count correction and had SHA-256 `1ecd58ebc50b5a30fcfd52994da687594fbafb0fd411fda0db6f58e9ecdd0dca`.

The frozen executable boundary preserves:

```text
parsed-instance structural validity != source-aware consistency != engineering correctness
controlled association truth != runtime resolution observation
validator != general Source Resolver
```

The accepted rc05 evidence includes `25 / 25 PASS` Context Source Association validator regressions, `37 / 37 PASS` directly composed Consumption Selection regressions, and all required repository-owned production checks PASS.

The post-rc05 dependency/value assessment found no current material consumer dependency requiring a general Source Resolver, source discovery/currentness model, runtime Resolution Observation representation, Context Assembly, CI source-association gate or L4 work. The explicit decision is therefore `STOP → FREEZE`, not automatic rc06 progression.

v0.0.9 controlled records:

- `50_SCAF_v0.0.9rc01_Context_Source_Resolution_Semantic_Foundation.md` — accepted Context Source Resolution semantics.
- `51_SCAF_v0.0.9rc02_Canonical_Context_Source_Association_Logical_Model_Foundation.md` — accepted representation-neutral logical model.
- `52_SCAF_v0.0.9rc03_Canonical_Context_Source_Association_Machine_Readable_Representation_Foundation.md` — accepted deterministic YAML representation.
- `53_SCAF_v0.0.9rc04_Context_Source_Association_Schema_Foundation.md` — accepted JSON Schema structural contract.
- `54_SCAF_v0.0.9rc05_Context_Source_Association_Source_Aware_Validator_Foundation.md` — accepted production source-aware validator boundary.
- `55_SCAF_v0.0.9_Formal_Freeze_Decision.md` — formal freeze decision, dependency/value STOP disposition and immutable v0.0.9 boundary.

General source resolution/discovery, Git-history traversal, currentness/supersession semantics, runtime resolution observations, content loading, AI Context Assembly, ranking/token budgeting, CI integration, authority expansion and L4 guidance remain separately gated.

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
| `schemas/` | Frozen authority/L3 trace schemas plus accepted Project Application, Effective Project Profile, and v0.0.7rc04 Consumption Selection schema foundations |
| `tools/scaf_validator/` | Frozen authority-registry semantic / structural / source-aware validator |
| `tools/scaf_trace_validator/` | Frozen v0.0.5 source-aware trace validator and regressions |
| `tools/scaf_trace_views/` | Frozen v0.0.5 deterministic validated read-only L2↔L3 trace views/query |
| `tools/scaf_project_application_validator/` | Accepted v0.0.6rc07 Project Application representation/source-aware validator foundation |
| `tools/scaf_project_application_views/` | Accepted v0.0.6rc08 validated deterministic read-only Project Application record/authority/scope queries |
| `tools/scaf_effective_project_profile_validator/` | Accepted v0.0.6rc12 Effective Project Profile representation/source-aware validator foundation |
| `tools/scaf_effective_project_profile_generator/` | Accepted v0.0.6rc13 deterministic validated Effective Project Profile generator foundation |
| `tools/scaf_consumption_selection_validator/` | Accepted v0.0.7rc05 source-aware Consumption Selection validator and bounded regressions |
| `tools/scaf_consumption_selection_builder/` | Accepted v0.0.7rc06 deterministic validated Consumption Selection builder and bounded regressions |
| `release-integrity/` | Frozen-baseline integrity manifest |
| `tools/scaf_release_integrity/` | Frozen-source byte-integrity checker |
| `tools/scaf_external_pin/` | External-pin verification |
| `tools/scaf_ci_gate/` | Executable-governance CI orchestration |
| `.github/workflows/` | Trusted-main/manual CI executor |
| `CHANGELOG.md` | Release / RC / review / finding history |

## Project Application

SCAF does not automatically decide project applicability or project architecture. A project remains responsible for controlled applicability, architecture/mechanism selection, adaptation, realization, verification/evidence, and closure decisions. Catalog availability and machine-readable trace are navigation/decision-support inputs, not automatic project authority.

`v0.0.6` formally freezes the accepted machine-readable Project Application and Effective Project Profile chain established through rc01→rc13 and consolidated/reviewed at rc14. The baseline includes Project Application semantics, canonical representation, schema, source-aware validation and validated queries, plus Effective Project Profile semantics, canonical representation, schema, source-aware validation and deterministic validated generation. It does not add scope resolution, applicability inference, Pattern selection, compliance/verification/closure authority, AI context packaging, CI completion enforcement, L4 guidance, or Development Context Recovery. See [`docs/executable-governance/39_SCAF_v0.0.6_Formal_Freeze_Decision.md`](docs/executable-governance/39_SCAF_v0.0.6_Formal_Freeze_Decision.md).

`v0.0.7rc01` established accepted consumption semantics; rc02 established the logical model; rc03 the canonical YAML representation; rc04 the parsed-instance schema; rc05 source-aware validation; rc06 deterministic validated construction; and rc07 consolidates that complete accepted chain as a freeze candidate while keeping context-source resolution and AI context assembly separately gated. See [`docs/executable-governance/46_SCAF_v0.0.7rc07_Consumption_Selection_Milestone_Consolidation_and_Freeze_Candidate.md`](docs/executable-governance/46_SCAF_v0.0.7rc07_Consumption_Selection_Milestone_Consolidation_and_Freeze_Candidate.md).

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
