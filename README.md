# System Control Architecture Framework (SCAF)

**Current Formal Release:** v0.1.0
**Active Development RC:** v0.2.0rc09
**Status:** Engineering Evidence Candidate Representation and L3 Readiness Dependency & Value Assessment
**Date:** 2026-08-22

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
| `v0.0.10` | Frozen Controlled Context Assembly and Source-Aware Package Validation baseline |
| `v0.1.0` | Frozen Minimum L4 Construction Guidance baseline |

The formal v0.1.0 baseline is frozen and immutable. Active development now continues on `v0.2.0rc09`. The rc08 evidence-relationship semantic candidate passed clean review with zero findings; rc09 assesses the minimum executable representation needed for the complete reviewed candidate set and whether the L2 evidence foundation is ready to support a later Evidence-Driven Engineering L3 Pattern.

Frozen releases are not modified in place. Detailed release history, review gates and finding closure are maintained in [`CHANGELOG.md`](CHANGELOG.md).

## Framework Layers

```text
L1/L2 — Normative Authority
  What system/project concerns must be addressed and who owns the decision?
        ↓
L3 — Pattern / Mechanism Catalog
  What reusable architecture mechanisms may be considered?
        ↓
L4 — Construction / Verification Guidance
  How can an accepted architecture mechanism be made construction-ready without replacing Project Design Authority?
```

The frozen L1/L2 and L3 layers remain canonical for their accepted scope. Formal v0.1.0 introduces no modification to either frozen layer.

## Active v0.2.0rc09 Candidate Representation and L3 Readiness Assessment

The v0.2.0rc01-to-rc08 development line now contains eight reviewed candidate OBS obligations:

```text
SCAF-OBS-041..045  diagnostic-instrumentation / probe lifecycle foundation
SCAF-OBS-046       evidence realization applicability binding
SCAF-OBS-047       baseline / change relationship for comparative evidence
SCAF-OBS-048       before/after verification-closure evidence relationship
```

The machine-readable candidate authority intentionally still represents only `SCAF-OBS-041..045` at `299 / 223 / 76`. rc09 concludes that representing the three reviewed rc08 PAOs now has real executable-governance value, with an expected complete candidate inventory of `302 / 226 / 76`.

The representation cannot safely be a simple three-record append under the current rc01-only candidate-source contract. Correct provenance is now multi-source:

```text
SCAF-OBS-041..045 -> v0.2.0rc01 semantic source
SCAF-OBS-046..048 -> v0.2.0rc08 semantic source
```

Therefore the next justified migration is a candidate-only multi-source authority representation/schema/validator foundation that preserves the exact 294 formal projection, per-record semantic provenance and formal-prerequisite fail-stop behavior.

rc09 also concludes that the L2 evidence/observability semantics are now sufficient to support a future **Evidence-Driven Engineering** L3 Pattern. Immediate L3 creation remains stopped until the full reviewed L2 candidate set is machine-readably represented and validated. Candidate Project Application / Effective Project Profile migration remains parked.

See `docs/normative-evolution/05_SCAF_v0.2.0rc09_Engineering_Evidence_Candidate_Representation_and_L3_Readiness_Dependency_and_Value_Assessment.md`.

## Frozen v0.1.0 Milestone

`v0.1.0 — Frozen Minimum L4 Construction Guidance Baseline` is the formal baseline promoted from the cleanly reviewed `v0.1.0rc03` source state after the required post-review dependency/value STOP assessment.

The accepted development chain is:

```text
v0.1.0rc01
L4 Minimum Construction Guidance Semantic and Layer Boundary Foundation
        ↓
v0.1.0rc02
SCAF-L4-001 — Bounded Queue / Backpressure / Overload Construction Guidance
        ↓
v0.1.0rc03
SCAF-L4-002 — Runtime Health Supervision and Watchdog Construction Guidance
        ↓
v0.1.0
formal frozen baseline
```

The milestone establishes a deliberately coarse but usable L4 layer so an engineer or AI consumer can move from accepted architecture Pattern context toward responsible implementation without transferring Project Design Authority or inventing hidden project defaults.

The two accepted representative identities are intentionally different in construction character:

```text
SCAF-L4-001
capacity / overload / concurrency / bounded-exhaustion construction

SCAF-L4-002
progress / supervision / independence / lifecycle / escalation construction
```

Their clean independent reviews provide bounded cross-problem evidence that the rc01 L4 contract generalizes beyond one problem type. This is sufficient for the first L4 milestone; it is not a claim that the L4 catalog is complete.

The frozen distinctions include:

```text
L4 guidance != new framework authority
L4 recommendation != Project Design Decision
L4 example != canonical implementation
L4 Verification Intent != verification result
Construction Ready != buildable / complete / correct / verified / compliant / closed
no L4 guidance != upstream concern not applicable
```

The post-rc03 dependency/value assessment concluded **STOP**: no current material ambiguity or construction dependency justifies `v0.1.0rc04`, a third representative entry, broad catalog population, L4 registry/schema/validator, executable L3↔L4 trace, project adoption/pinning machinery, platform-specific realization guidance, reference implementation/code generation, or CI enforcement.

The formal freeze adds no semantic or executable capability beyond reviewed rc03 and does not reopen the frozen v0.0.10 Controlled Context Package builder/materialization-policy decision. See [`docs/executable-governance/65_SCAF_v0.1.0_Formal_Freeze_Decision.md`](docs/executable-governance/65_SCAF_v0.1.0_Formal_Freeze_Decision.md).

## Frozen v0.0.10 Milestone

`v0.0.10 — Frozen Controlled Context Assembly and Source-Aware Package Validation Baseline` is the formal baseline promoted from the cleanly reviewed `v0.0.10rc05` source state after the required post-review dependency/value STOP assessment.

The accepted development chain is:

```text
v0.0.10rc01  Controlled Context Assembly Semantic Foundation
        ↓
v0.0.10rc02  Canonical Controlled Context Package Logical Model
        ↓
v0.0.10rc03  Canonical Machine-Readable Package Representation
        ↓
v0.0.10rc04  Controlled Context Package Schema Foundation
        ↓
v0.0.10rc05  Controlled Context Package Source-Aware Validator Foundation
        ↓
v0.0.10      formal frozen baseline
```

The frozen chain establishes a deterministic downstream contract from validated Consumption Selection and Context Source Association truth to a controlled consumer-facing package while preserving the upstream engineering authority boundary.

The governing validation separation remains:

```text
package representation
!= parsed-instance structural validity
!= source-aware package consistency
!= engineering-context sufficiency
```

The source-aware validator proves exact upstream byte/kind/release/scope binding, exact validated-`I` coverage, Association Envelope fidelity, package-wide handle uniqueness, complete Materialization Decision accounting, Materialized Context Item reference/orphan integrity, Controlled Provenance Basis resolution, bidirectional decision/provenance correspondence, and canonical ordering.

A validator PASS does **not** prove engineering-context sufficiency, implementation correctness, verification/compliance, risk acceptance, release readiness, closure, source currentness, content-use authorization, or consumer/AI engineering authority.

The explicit post-rc05 dependency/value assessment concluded **STOP** for a package builder: no current semantic ambiguity, validator divergence, blocked executable dependency, difficult-to-reverse commitment, or concrete consumer evidence justifies builder/materialization-policy work now. Therefore no `v0.0.10rc06` is required.

The formal freeze adds no new semantic or executable capability beyond reviewed rc05. See [`docs/executable-governance/61_SCAF_v0.0.10_Formal_Freeze_Decision.md`](docs/executable-governance/61_SCAF_v0.0.10_Formal_Freeze_Decision.md).

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
| `docs/normative/` | Frozen v0.0.2 L1/L2 semantic authority used by the formal v0.1.0 release |
| `docs/normative-evolution/` | Active post-freeze L1/L2 candidate overlays; not canonical until explicit promotion |
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
