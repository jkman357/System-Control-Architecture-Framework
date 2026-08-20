# Changelog

## v0.0.10rc04 — Controlled Context Package Schema Foundation

- Continue only after the independent rc03 review returned clean `PASS / GATE YES` with zero candidate-source findings and zero blocking review-evidence limitations, and a separate dependency/value assessment found one repository-owned structural contract materially necessary before source-aware package validation or builder work.
- Add `schemas/controlled-context-package.schema.json` as the JSON Schema Draft 2020-12 structural contract for the accepted `v0.0.10rc03` Controlled Context Package representation.
- Preserve `v0.0.10rc03` as the representation release while identifying the rc04 schema independently as `urn:scaf:schema:controlled-context-package:v0.0.10rc04`.
- Enforce closed parsed-object shapes, exact required/optional members, representation constants, bounded token vocabularies, non-empty strings/lists and lowercase SHA-256 syntax.
- Encode non-overlapping `materialized` and `not_materialized` decision shapes, including non-empty item references for materialized outcomes and explicit empty refs plus non-empty basis for not-materialized outcomes.
- Preserve the exact rc03 Controlled Source Association projection shape and the initial reference-only `source_reference` payload boundary.
- Preserve `package representation != parsed-instance structural validity != source-aware package consistency != engineering-context sufficiency`.
- Keep exact upstream byte proof, validated-`I` coverage, Association Envelope fidelity, semantic/reference uniqueness, one-decision-per-association accounting, decision/provenance correspondence, canonical raw-YAML ordering, source loading/currentness, engineering sufficiency and consumer/model authority outside schema ownership.
- Add no production package validator, builder/generator, loader, inline source content, fragment/chunk syntax, summarization, ranking/token-budget policy, prompt/model integration, Source Resolver/currentness behavior, CI package gate, authority-registry change, new PAO/FNI or L4 guidance.
- Apply frozen v0.0.8 proportional governance: a clean rc04 review leads only to a new dependency/value assessment, not automatic rc05.

## v0.0.10rc03 — Canonical Controlled Context Package Machine-Readable Representation Foundation

- Continue only after the independent rc02 review returned clean `PASS / GATE YES` with zero candidate-source findings and zero blocking review-evidence limitations, and a separate dependency/value assessment found one canonical package serialization materially necessary before schema/validator work.
- Add `examples/controlled-context-package.yaml` as the deterministic canonical YAML representation of the accepted rc02 Controlled Context Package logical model.
- Bind the package to the exact current Consumption Selection and Context Source Association Set bytes, kind/release metadata and exact opaque project scope.
- Serialize exactly one Authority Context Entry per validated `I` authority, including the explicit zero-association entry for `SCAF-AK-002`.
- Preserve each accepted Controlled Source Association through a package-local association handle plus source-fidelity association projection; the handle is package-local and is not a new upstream association identity.
- Require exactly one Materialization Decision per accepted association and serialize both `materialized` and explicit `not_materialized` outcomes without converting omission into applicability, source validity, waiver, risk acceptance or closure.
- Add package-local Materialized Context Item identity, controlled provenance bases, bidirectional decision/provenance correspondence and the initial `source_preserving` / `derived` context-semantic vocabulary.
- Keep the initial payload boundary reference-only (`source_reference`) so rc03 introduces no inline source copying, fragment syntax, content loader or transformation algorithm.
- Define deterministic canonical member/list ordering and future strict-YAML validation direction without adding a production schema or validator.
- Preserve `package representation != schema validity != source-aware package consistency != engineering-context sufficiency`, `controlled association truth != package materialization truth != runtime observation`, and `machine-readable != machine-decided`.
- Add no package schema, validator, builder, loader, chunking, summarization algorithm, ranking/token-budget policy, prompt/model integration, Source Resolver/currentness behavior, CI gate, authority-registry change, new PAO/FNI or L4 guidance.
- Apply frozen v0.0.8 proportional governance: a clean rc03 review leads only to a new dependency/value assessment, not automatic rc04.

## v0.0.10rc02 — Canonical Controlled Context Package Logical Model Foundation

- Continue only after the independent rc01 review returned clean `PASS / GATE YES` with zero candidate-source findings and no blocking review-evidence limitations, and a separate dependency/value assessment found the representation-neutral package model materially necessary before serialization/builder work.
- Define one canonical Controlled Context Package bound to the exact validated Consumption Selection, exact validated Context Source Association Set and one explicit Assembly Objective.
- Require exactly one Authority Context Entry per authority in validated `I`, preserving authority presence even with zero associations or zero materialized content.
- Preserve an exact controlled Association Envelope for every authority and require exactly one Materialization Decision for every accepted controlled association.
- Make package-level context omission explicit through zero-materialization accounting instead of silent association/content disappearance.
- Define a shared Materialized Context Item Catalog with package-local identity and `1..n` exact controlled provenance bases per item.
- Permit traceable multi-association/cross-authority derived items without merging authority ownership or promoting derived context into source authority.
- Preserve package logical totality/conformance separately from engineering-context sufficiency, verification, compliance, release and closure.
- Preserve `controlled association truth != runtime resolution/materialization observation`, `context inclusion != applicability`, `derived context != authoritative source truth`, and `machine-readable != machine-decided`.
- Add no Context Package YAML/JSON, schema, validator, builder, content loader, fragment/chunk policy, summarization algorithm, ranking/token-budget policy, prompt/model integration, general Source Resolver, CI gate, authority-registry change, new PAO/FNI or L4 guidance.
- Apply frozen v0.0.8 proportional governance: a clean rc02 review leads only to a new dependency/value assessment, not automatic rc03.

## v0.0.10rc01 — Controlled Context Assembly Semantic Foundation

- Open v0.0.10 only after the frozen v0.0.9 STOP/freeze and a separate global dependency/value assessment identified the remaining AI-consumption last-mile ambiguity between validated source relationships and the bounded context actually presented to a consumer.
- Define representation-neutral Controlled Context Assembly downstream of the exact validated Consumption Selection and Context Source Association chain.
- Preserve the validated included authority domain `I` as the controlled context authority envelope; an authority does not disappear merely because it has zero associations or zero materialized source content.
- Establish `source association != context materialization` and separate the controlled authority/association envelope from materialized consumer content.
- Establish `context inclusion != applicability` and `context omission != not_applicable / source invalid / waiver / accepted risk / closure`.
- Define a future Controlled Context Package as a bounded consumer artifact with traceable upstream provenance, not a new engineering authority or replacement source of truth.
- Preserve `derived context representation != authoritative source truth`, `context completeness != engineering completion`, and `context presented to AI != authority granted to AI`.
- Preserve `controlled association truth != runtime resolution/materialization observation` and the frozen invalid-vs-unresolved distinction.
- State that external source association does not itself grant content-use/redistribution authorization.
- Keep future assembly deterministic for machine-determinable facts while preserving explicit engineering judgment: `machine-readable != machine-decided`.
- Add no Context Package representation/schema/validator/builder, loader, fragment/chunk policy, summarization, ranking/token-budget policy, prompt/model adapter, Source Resolver, currentness model, CI gate, authority-registry change, new PAO/FNI or L4 guidance.
- Apply frozen v0.0.8 proportional governance: a clean rc01 review leads only to a new dependency/value assessment, not automatic rc02.

## v0.0.9 — Frozen Context Source Association and Source-Aware Validation Baseline

- Formally freeze the cleanly reviewed `v0.0.9rc05` source state after explicit governance approval and the required post-review dependency/value STOP assessment.
- Preserve the accepted rc01→rc05 chain: Context Source Resolution semantics, canonical logical model, deterministic YAML representation, Draft 2020-12 schema and production source-aware validator.
- Record the corrected rc05 independent review as `PASS / GATE YES` with 0 Critical / 0 Major / 0 Minor / 0 Trivial candidate-source findings and zero blocking review-evidence limitations.
- Record that the reviewed rc05 source ZIP remained unchanged during the review-instruction count correction and matched SHA-256 `1ecd58ebc50b5a30fcfd52994da687594fbafb0fd411fda0db6f58e9ecdd0dca`.
- Preserve `controlled association truth != runtime resolution observation` and `parsed-instance structural validity != source-aware consistency != engineering correctness`.
- Preserve the bounded `repo:<repository-relative POSIX path>` exact-byte proof as validator behavior only; do not promote it into general source discovery/resolution semantics.
- Record the post-rc05 dependency/value decision `STOP`: no material current dependency justifies a general Source Resolver, runtime resolution/currentness model, Context Assembly or rc06.
- Add no new authority-registry entry, PAO/FNI, resolver, source discovery, Git traversal, content processing, CI gate or L4 capability.
- Freeze v0.0.9 as immutable; future work requires a new controlled version/RC line and explicit Current Decision Horizon.

## v0.0.9rc05 — Context Source Association Source-Aware Validator Foundation

- Continue only after the independent rc04 review returned clean `PASS / GATE YES` with zero findings and zero blocking review-evidence limitations and a separate dependency/value assessment found source-aware consistency validation materially necessary.
- Add `tools/scaf_context_source_association_validator/` as the production validator for the accepted rc03 association representation and rc04 schema.
- Validate the exact bound Consumption Selection through the accepted source-aware Consumption Selection validator before reconstructing included domain `I`.
- Prove exact selection SHA/kind/release/scope binding and exact Authority Source Entry coverage of validated `I`, preserving explicit zero associations as distinct from omitted entries.
- Prove Source Unit ID/identity uniqueness, association reference integrity, unused-catalog absence, semantic association uniqueness and canonical raw/list ordering.
- Add bounded exact-byte verification for explicit SHA-256 Instance Constraints over already-declared `repo:<repository-relative POSIX path>` identities without creating repository discovery or a general resolver.
- Preserve `controlled association truth != runtime resolution observation` and `source-aware consistency != engineering correctness`.
- Add no candidate discovery, Git-history traversal, currentness/supersession model, runtime Resolution Observation representation, content processing, Context Assembly, CI gate, authority-registry change, new PAO/FNI or L4 guidance.
- Apply frozen v0.0.8 proportional governance: a clean rc05 review leads only to a new dependency/value assessment, not automatic rc06/resolver work.

## v0.0.9rc04 — Context Source Association Schema Foundation

- Continue only after the independent rc03 review returned clean `PASS / GATE YES` with zero findings and zero blocking review-evidence limitations and a separate dependency/value assessment found a parsed-instance structural schema materially necessary before source-aware validator work.
- Add `schemas/context-source-associations.schema.json` as the JSON Schema Draft 2020-12 structural contract for the accepted `v0.0.9rc03` canonical YAML representation.
- Encode exact representation identity, required/optional members, closed object shapes, bounded token vocabularies, non-empty basis lists and lowercase SHA-256 syntax.
- Preserve explicit zero-association representation and the accepted atomic association / bounded Authority Qualification / Instance Constraint shapes.
- Preserve `controlled association truth != runtime resolution observation`; no resolver/currentness state model is introduced.
- Explicitly separate parsed-instance structural validity from source-aware consistency and engineering correctness.
- Keep exact selection-byte proof, validated-I coverage, Source Unit reference integrity, semantic uniqueness/order, source-byte instance proof, resolver/currentness behavior, applicability/satisfaction/verification/closure and Context Assembly outside schema authority.
- Add no production validator, resolver, content processing, CI gate, authority-registry change, new PAO/FNI, scope resolver or L4 guidance.
- Apply frozen v0.0.8 proportional governance: a clean rc04 review leads only to a new dependency/value assessment, not automatic rc05.

## v0.0.9rc03 — Canonical Context Source Association Machine-Readable Representation Foundation

- Continue only after the independent rc02 review returned clean `PASS / GATE YES` with zero findings and zero open blocking review-evidence limitations and a separate dependency/value assessment found a canonical machine-readable representation materially necessary before schema/validator work.
- Add `examples/context-source-associations.yaml` as the canonical `v0.0.9rc03` YAML representation of the accepted rc02 Context Source Association logical model.
- Bind one association set to the exact current Consumption Selection bytes and preserve complete validated `I` coverage with explicit zero-association entries.
- Serialize a shared Source Unit Catalog, atomic Controlled Source Associations, relationship semantic/scope, association provenance, optional bounded Authority Qualification, and optional SHA-256 Instance Constraint.
- Freeze initial representation vocabularies for source control domain, relationship semantic, association assertion kind, authority qualification kind, and SHA-256 instance constraint.
- Define deterministic ordering and semantic uniqueness needed for future byte-stable tooling.
- Preserve `controlled association truth != runtime resolution observation`; the canonical artifact contains no runtime resolver status/currentness fields.
- Keep source resolution separate from obligation satisfaction and downstream Context Assembly.
- Add no schema, production validator, resolver, source scanning, content processing, ranking/token-budget policy, AI context package, CI gate, authority-registry change, new PAO/FNI or L4 guidance.
- Apply frozen v0.0.8 proportional governance: a clean rc03 review leads only to a new dependency/value assessment, not automatic rc04.

## v0.0.9rc02 — Canonical Context Source Association Logical Model Foundation

- Continue the controlled v0.0.9 line after the independent rc01 review returned clean `PASS / GATE YES` with zero findings and zero open blocking review-evidence limitations.
- Record the post-rc01 dependency/value decision that a canonical logical model is required before machine-readable serialization because otherwise association truth, cardinality, provenance, source-instance binding, and resolver behavior can diverge.
- Define one Context Source Association Set bound to one exact validated Consumption Selection and exactly its included authority domain `I`.
- Require exactly one Authority Source Entry for every authority in `I`, making zero associations explicit rather than equivalent to omitted/incomplete data.
- Define a shared Source Unit Catalog and atomic Controlled Source Association model with one relationship semantic per association plus bounded relationship scope, controlled basis/provenance, optional authority qualification, and optional source-instance constraint.
- Establish the two-plane invariant `controlled association truth != runtime resolution observation`; missing, unresolvable and stale/superseded are resolver/currentness observations and do not silently rewrite controlled relationship truth.
- Preserve source identity vs exact source instance, discovery vs controlled association, relationship vs authority, source existence vs satisfaction, exact opaque scope, and existing authority/applicability/closure ownership.
- Add no YAML/JSON representation, schema, validator, resolver, filesystem/Git scan, content processing, ranking/token-budget policy, AI Context Assembly, CI gate, or authority-registry change.
- Apply frozen v0.0.8 proportional governance: a clean rc02 review leads only to a new dependency/value assessment, not automatic rc03.

## v0.0.9rc01 — Context Source Resolution Semantic Foundation

- Start the controlled v0.0.9 line from formal frozen v0.0.8 without reopening frozen authority, Project Application, Effective Project Profile, Consumption Selection, or lifecycle-proportional governance baselines.
- Define Context Source Resolution as a downstream relationship-resolution stage over the validated Consumption Selection included domain `I`, not a content-loading or AI-context stage.
- Define Source Unit, source identity versus exact source instance, and Source Association as a trace/relationship construct that creates no new engineering authority.
- Separate relationship role, source authority, source ownership, association provenance, resolvability/currentness, and obligation satisfaction.
- Establish `discovery != controlled association`, `locator resolves != current/authoritative`, `source exists != obligation satisfied`, and `source resolution != context inclusion`.
- Preserve zero/many source cardinality and distinguish no association, unresolved locator, stale/superseded source, and missing source without changing applicability/waiver/closure semantics.
- Preserve exact opaque project scope and the frozen authority chain; introduce no scope resolver, authority inference, or external trust expansion.
- Add no source-association representation/schema/resolver, filesystem scanning, content extraction, ranking/token-budget policy, AI context assembly, CI source-mapping gate, or authority-registry change.
- Apply frozen v0.0.8 proportional governance: a clean rc01 review leads only to a dependency/value decision, not automatic rc02.

## v0.0.8 — Frozen Lifecycle-Proportional Governance Semantic Baseline

- Formally freeze the cleanly reviewed `v0.0.8rc01` semantic source state after explicit governance approval and dependency/value STOP assessment.
- Preserve the subject-scoped Current Decision Horizon, governance proportionality, Evidence Availability Rule, Progression Sufficiency, five-question Materiality Stop Rule, engineering-impact/current-disposition separation, controlled deferral/revisit semantics, reversibility boundary, external-authority preservation, and SCAF self-application.
- Record the rc01 independent review as `PASS / GATE YES` with 0 Critical / 0 Major / 0 Minor / 0 Trivial findings and zero open review-evidence limitations.
- Record that the expected rc01 source ZIP SHA-256 `f0164be6a201691229f9181bb45cd1553803fa6051567975e5734b2e4e6aefaa` matched the independently computed review digest exactly.
- Preserve the frozen authority inventory at `294 / 218 / 76`, L3 inventory at `12 / 119`, and all frozen representation/executable sources unchanged.
- Apply the Materiality Stop Rule to SCAF itself: no rc02 is required for this milestone because no current material progression ambiguity justifies further formalization.
- Add no lifecycle state machine, machine-readable disposition record, schema, validator, CI gate, authority-registry promotion, Context Source Resolution, or AI context mechanism.
- Freeze v0.0.8 as immutable; all deferred capabilities require a separately justified future version/RC line.

## v0.0.8rc01 — Lifecycle-Proportional Governance Semantic Foundation

- Start the controlled v0.0.8 line from formal frozen v0.0.7 without reopening frozen Consumption Selection or earlier authority/executable baselines.
- Define the subject-scoped **Current Decision Horizon** as the decisions and currently producible evidence required to support the next intended engineering action.
- Establish governance proportionality: review depth follows current decision consequence and reasonably available evidence rather than theoretical maximum completeness.
- Establish the Evidence Availability Rule: not-yet-producible empirical evidence is not an automatic current blocker; future property/measurement/owner/revisit obligations remain explicit.
- Define **Progression Sufficiency** separately from completion, verification, compliance, release and closure.
- Define a five-question Materiality Stop Rule covering behavioral divergence, authority contradiction, material correctness/risk, next-stage implementability/verifiability, and expensive/irreversible commitment.
- Keep engineering impact separate from current progression disposition and require controlled revisit triggers for deferred engineering obligations.
- Preserve applicable external-authority requirements and existing PDA/Realization/Verification/closure ownership.
- Add no lifecycle state machine, schema, validator, CI gate, authority-registry change, Context Source Resolution or AI context mechanism.
- Require SCAF to apply the same proportionality/stop discipline to its own RC progression.

## v0.0.7 — Frozen Consumption Selection Baseline

- Formally freeze the cleanly reviewed `v0.0.7rc07` source state after explicit governance approval.
- Preserve the accepted rc01→rc06 Consumption Selection chain: semantics, canonical logical model, rc03 YAML representation, rc04 JSON Schema, rc05 source-aware validator, and rc06 deterministic validated builder.
- Record the rc07 freeze-candidate review as `PASS / GATE YES` with 0 Critical / 0 Major / 0 Minor / 0 Trivial findings.
- Preserve the current milestone review execution inventory as `34 / 34` builder + `37 / 37` validator + inherited `191 / 191` = `262` completed tests, while retaining 191 as the historical inherited/frozen baseline.
- Preserve exact source-profile provenance, exact opaque scope, `D/E/I/O/X`, bounded omission, source-entry fidelity, and engineering-authority separation unchanged.
- Keep context-source resolution, AI context assembly/orchestration, ranking/token-budget policy, CI applicability-completion enforcement, L4 guidance, Development Context Recovery, and other deferred capabilities outside the frozen baseline.
- Add no semantic or executable capability relative to committed rc07; the freeze changes release-state/navigation documentation only.

## v0.0.7rc07 — Consumption Selection Milestone Consolidation and Freeze Candidate

- Continue after the independent rc06 review returned clean `PASS / GATE YES` with zero findings.
- Add a documentation/navigation-only milestone consolidation record for the accepted rc01→rc06 Consumption Selection chain.
- Consolidate consumption semantics, canonical logical model, rc03 YAML representation, rc04 schema, rc05 source-aware validator, and rc06 deterministic validated builder into one freeze-candidate boundary.
- Record that all accepted rc01→rc06 reviews are clean with zero open findings entering rc07.
- Record the current review-covered execution inventory as `34 / 34` rc06 builder + `37 / 37` rc05 validator + inherited `191 / 191` baseline = `262` completed tests; the historical frozen baseline remains 191.
- Preserve exact-scope, source-provenance, `D/E/I/O/X`, bounded-omission, source-entry fidelity, `included != applicable`, `excluded/omitted != not_applicable`, `predicate excluded != bounded omitted`, and `undetermined != no_current_disposition` boundaries unchanged.
- Preserve context-source resolution, AI context assembly/orchestration, ranking/token-budget policy, CI applicability-completion enforcement, L4 guidance, Development Context Recovery, and other deferred capabilities as separately gated.
- Add no executable capability. A clean rc07 review establishes freeze eligibility only; formal v0.0.7 still requires a separate explicit governance decision.

## v0.0.7rc06 — Deterministic Consumption Selection Builder Foundation

- Continue the controlled v0.0.7 line after the independent rc05 review returned clean `PASS / GATE YES` with zero findings.
- Add `tools/scaf_consumption_selection_builder/` as the first deterministic builder for the accepted rc03 Consumption Selection representation.
- Validate the exact selected Effective Project Profile before consuming profile state and construct only from explicit bounded purpose/state/authority/omission inputs.
- Derive representation identity from the repository-owned accepted rc04 schema and preserve `representation_release: v0.0.7rc03`.
- Deterministically derive `D/E/I/O/X`, exact selected-entry projections, bounded omission, and complete/filtered class without ranking, token-budget, semantic matching, or scope inference.
- Preserve caller-declared omission as exact eligible authority IDs only; `applied:true` with empty omission remains valid.
- Require every generated result to pass the accepted rc05 source-aware Consumption Selection validator against the same captured source snapshots before return/emission.
- Reproduce the accepted rc03 fixture bytes exactly after removing only its leading non-authoritative comments.
- Add 34 bounded builder regressions while preserving the accepted 37-test rc05 suite and inherited 191-test baseline.
- Introduce no context-source resolver, AI context package/orchestration, Pattern selection, CI completion gate, L4 guidance, or Development Context Recovery mechanism.

## v0.0.7rc05 — Consumption Selection Source-Aware Validator Foundation

- Continue the controlled v0.0.7 line after the independent rc04 review returned clean `PASS / GATE YES` with zero findings.
- Add `tools/scaf_consumption_selection_validator/` as the first source-aware executable validator for the accepted rc03 Consumption Selection representation and rc04 schema.
- Capture selected Consumption Selection / Effective Project Profile / Project Application bytes plus repository-owned validation sources into private validation snapshots.
- Enforce rc03 raw-YAML/canonical ordering, rc04 schema conformance, and frozen v0.0.6 source-aware validation of the exact bound Effective Project Profile before selection proof.
- Prove exact source-profile SHA-256/provenance binding, exact authority-selector domain membership, selected-entry source fidelity, and canonical selector/entry ordering.
- Reconstruct `D/E/I/O/X`, enforce no-omission `I == E`, preserve accepted applied-omission subset semantics, and prove serialized complete/filtered classification.
- Preserve `included != applicable`, `excluded/omitted != not_applicable`, `predicate excluded != bounded omitted`, `undetermined != no_current_disposition`, and Project Design Authority separation.
- Add 37 bounded source-aware validator regressions; introduce no builder/generator, context-source resolver, AI package/orchestration, CI completion gate, L4 guidance, or Development Context Recovery mechanism.

## v0.0.7rc04 — Consumption Selection Schema Foundation

- Continue the controlled v0.0.7 line after the independent rc03 review returned clean `PASS / GATE YES` with zero findings.
- Add `schemas/consumption-selection.schema.json` as the JSON Schema Draft 2020-12 foundation for the accepted rc03 Consumption Selection representation.
- Preserve `representation_release: v0.0.7rc03`; rc04 formalizes the accepted serialization rather than creating a new representation release.
- Enforce the exact nine-member parsed root, source-binding shape, four-state selector vocabulary, authority-selector variants, bounded-omission variants, selected-entry state/trace shapes, and complete/filtered token vocabulary.
- Reject unknown schema-owned members, malformed lowercase SHA-256 strings, parsed null/type mismatches, duplicate state/explicit-ID strings, and exact duplicate complete selected-entry objects.
- Keep source-profile validity, actual digest correspondence, provenance equality, authority/domain membership, D/E/I/O/X set algebra, selected-entry source fidelity, complete/filtered derivation, canonical physical YAML order, and engineering authority outside schema-only proof.
- Preserve the accepted `included != applicable`, `excluded/omitted != not_applicable`, `predicate excluded != bounded omitted`, and `undetermined != no_current_disposition` boundaries.
- Introduce no source-aware Consumption Selection validator, builder/generator, API, CLI, context-source resolver, AI package, CI completion gate, L4 guidance, or Development Context Recovery mechanism.

## v0.0.7rc03 — Canonical Consumption / Context-Selection Machine-Readable Representation Foundation

- Continue the controlled v0.0.7 line after the independent rc02 review returned clean `PASS / GATE YES` with zero findings.
- Add `examples/consumption-selection.yaml` as the first canonical YAML representation of the accepted Consumption Selection logical model.
- Define an exact nine-member top-level representation and deterministic nested mapping/list order.
- Bind the record to exact Effective Project Profile source bytes plus frozen release/scope/Project Application provenance.
- Serialize only bounded state/authority selectors, explicit bounded-omission metadata, included source-profile projections, and derived complete/filtered class.
- Do not serialize redundant authoritative E/O/X lists; reconstruct them from the validated source profile and canonical selection inputs.
- Preserve selected-entry authority/state/record-trace fidelity and Project Application truth upstream.
- Preserve `included != applicable`, `excluded != not_applicable`, `predicate excluded != bounded omitted`, and `undetermined != no_current_disposition`.
- Add one illustrative filtered fixture with `|D|=218`, `|E|=3`, `|I|=2`, `|O|=1`, and `|X|=215`.
- Introduce no schema, validator, builder/generator, API, CLI, context-source resolver, AI package, CI completion gate, L4 guidance, or Development Context Recovery mechanism.

## v0.0.7rc02 — Canonical Consumption / Context-Selection Model Foundation

- Continue the controlled v0.0.7 line after the independent rc01 review returned clean `PASS / GATE YES` with zero findings.
- Add a representation-neutral canonical logical model for one subordinate Consumption Selection over one validated Effective Project Profile snapshot.
- Bind consumption to the exact validated profile bytes plus `scaf_source_release`, exact `project_scope_ref`, and Project Application source SHA-256 provenance.
- Define the canonical eligibility predicate as a bounded intersection of an explicit frozen-state selector and exact authority selector.
- Distinguish predicate eligibility/exclusion from explicit bounded omission, with `D = I + O + X` and `E = I + O`.
- Define complete versus filtered selection as a derived fact rather than a new engineering or applicability state.
- Preserve selected-entry `scaf_authority_id`, frozen `profile_state`, and Project Application record trace exactly.
- Preserve `included in context != applicable`, `excluded from context != not_applicable`, exact-scope semantics, and `undetermined != no_current_disposition`.
- Keep Project Application rationale/provenance upstream and define no context-content resolver.
- Introduce no serialization, schema, validator, builder/generator, API, CLI, AI context package, resolver, CI completion gate, L4 guidance, or Development Context Recovery mechanism.

## v0.0.7rc01 — Effective Project Profile Consumption Semantic Foundation

- Start a new controlled development line from formal frozen `v0.0.6` without modifying or respinning the frozen baseline.
- Define the downstream consumption semantics for a validated Effective Project Profile before introducing any context-package representation or executable consumer.
- Preserve the four frozen profile states exactly: `applicable`, `not_applicable`, `undetermined`, and `no_current_disposition`.
- Preserve `undetermined != no_current_disposition`, exact-scope semantics, source provenance, and Project Application traceability.
- Permit deterministic state partitioning and explicitly declared filtering as subordinate consumption operations only.
- Define that `included in context != applicable` and `excluded from context != not_applicable`.
- Prohibit consumption from inferring implementation, Pattern selection, verification, compliance, approval, release readiness, or closure.
- Distinguish complete-profile consumption from filtered consumption; filtered results may not claim complete profile coverage.
- Require later executable consumers to own or chain the accepted profile validation boundary rather than trust caller assertions or parsed substitutes.
- Introduce no context-package model, serialization, schema, validator, generator, API, CLI, resolver, persistent context state, CI completion gate, L4 guidance, or Development Context Recovery mechanism.

## v0.0.6 — Frozen Machine-Readable Project Application and Effective Project Profile Baseline

- Formally freeze the independently reviewed `v0.0.6rc14` source state after a clean freeze-candidate review with zero findings and gate `YES`.
- Freeze the accepted Project Application semantics, canonical representation, schema, source-aware validator, and validated deterministic query boundary.
- Freeze the accepted Effective Project Profile semantics, canonical representation, schema, source-aware validator, and deterministic validated generator boundary.
- Preserve exact-scope semantics, `undetermined != no_current_disposition`, source-snapshot provenance, validated-input ownership, and no applicability inference.
- Preserve Project Design Authority / engineering / compliance / verification / closure separation.
- Freeze the review-covered regression baseline at `98 / 98` v0.0.6 development tests plus `93 / 93` inherited frozen tests (`191 / 191` combined).
- Preserve the existing upstream frozen v0.0.2, v0.0.3, v0.0.4, and v0.0.5 baselines unchanged.
- Add `docs/executable-governance/39_SCAF_v0.0.6_Formal_Freeze_Decision.md`.
- Mark v0.0.6 immutable; future capability work must begin on a new controlled RC/version line.

## v0.0.6rc14 — Project Application / Effective Project Profile Milestone Consolidation and Freeze Candidate

- Continue after the independent rc13 review returned clean `PASS / GATE YES` with zero findings.
- Add a consolidation-only controlled record covering the accepted rc01→rc13 Project Application and Effective Project Profile dependency chain.
- Consolidate historical finding closure: rc02 Major/Minor findings closed by rc03; rc04 Minor fixture-coverage finding closed by rc05; no accepted finding remains open.
- Consolidate the accepted Project Application record/representation/schema/validator/query boundary and the Effective Project Profile semantics/representation/schema/validator/generator boundary.
- Record the current accepted regression inventory: 98 v0.0.6 executable-development tests plus 93 frozen v0.0.4/v0.0.5 regression tests, for 191 review-covered repository tests.
- Preserve the exact-scope, invalid-vs-unresolved, `undetermined` versus `no_current_disposition`, validated-input, and engineering-authority boundaries.
- Explicitly defer context packaging, scope/reference resolution, applicability inference, Pattern selection, CI applicability-completion enforcement, compliance/verification/closure determination, L4 guidance, and Development Context Recovery.
- Change documentation/navigation only; no accepted representation, schema, validator, query, generator, frozen source, workflow, trust boundary, or test implementation is modified.
- Mark rc14 as a milestone / freeze candidate only. Formal `v0.0.6` freeze still requires a separate explicit governance decision.

## v0.0.6rc13 — Effective Project Profile Deterministic Generator Foundation

- Continue the controlled v0.0.6 line after the independent rc12 review returned clean `PASS / GATE YES` with zero findings.
- Add `tools/scaf_effective_project_profile_generator/` as a deterministic validated generator for the accepted Effective Project Profile representation.
- Accept one exact opaque `project_scope_ref` plus one selected Project Application source; keep repository/schema/authority/normative inputs repository-owned.
- Capture Project Application and authority/normative inputs into a private boundary, require frozen authority proof and accepted rc07 Project Application proof, then derive the source-release-bound complete PAO domain.
- Copy `applicable`, `not_applicable`, and `undetermined` only from validated exact-scope current Project Application records; derive `no_current_disposition` only from exact-pair absence.
- Derive the source release from validated records, with a repository-owned Project Application schema fallback for a valid zero-record dataset; do not hard-code the current v0.0.2 / 218 inventory.
- Bind output to SHA-256 of the exact captured Project Application bytes and serialize the accepted rc10 representation deterministically.
- Self-validate every generated result through the accepted rc12 source-aware validator before returning/emitting it.
- Emit successful CLI output as canonical YAML only on stdout; introduce no persistent profile registry/cache or source write-back.
- Preserve exact-scope resolution neutrality, valid `undetermined`, Project Design Authority ownership, and all engineering/compliance/verification/closure boundaries.
- Add 25 bounded generator regressions while preserving accepted/frozen validation behavior.
- Introduce no applicability inference, Pattern selection, AI approval, context package, CI completion gate, code generation, L4 guidance, or Development Context Recovery workflow state.

## v0.0.6rc12 — Effective Project Profile Source-Aware Validator Foundation

- Continue the controlled v0.0.6 line after the independent rc11 review returned clean `PASS / GATE YES` with zero findings.
- Add `tools/scaf_effective_project_profile_validator/` as the first executable Effective Project Profile representation/source-aware validator.
- Execute the accepted rc10 raw-YAML policy before chaining the accepted rc11 Draft 2020-12 profile schema.
- Compare `project_application_source_sha256` to SHA-256 computed over the exact selected Project Application bytes.
- Validate the frozen authority-registry snapshot before deriving the source-release-bound Project-Applicable Obligation domain.
- Validate the same selected Project Application snapshot through the accepted rc07 validator before profile/source correspondence checks.
- Enforce complete PAO-domain coverage, cross-entry authority-ID uniqueness, PAO-only/source-release membership, and canonical root/entry/sequence ordering.
- Require recorded profile states to resolve to the exact current Project Application record with matching authority, exact scope, state, and source release.
- Require every `no_current_disposition` entry to be supported by actual absence of the exact authority/scope pair in the same validated Project Application snapshot.
- Keep project scope exact-string and resolution-neutral; preserve valid `undetermined` as engineering-unresolved state.
- Report only `PROFILE REPRESENTATION/SOURCE RESULT: PASS/FAIL`; do not infer engineering correctness, Project Design Authority approval, Pattern selection, compliance, verification, completion, release or closure.
- Introduce no profile generator, query API, resolver, applicability inference, AI approval, context package, CI completion gate, code generation, new L3 Pattern, L4 guidance, or Development Context Recovery workflow state.
- Change no accepted rc10 profile fixture, rc11 profile schema, Project Application fixture/schema/validator/views, frozen source, workflow, trust boundary, or frozen regression implementation.

## v0.0.6rc11 — Effective Project Profile Schema Foundation

- Continue the controlled v0.0.6 line after the independent rc10 review returned clean `PASS / GATE YES` with zero findings.
- Add `schemas/effective-project-profile.schema.json` as the formal JSON Schema Draft 2020-12 foundation for the accepted rc10 profile representation.
- Preserve `representation_release: v0.0.6rc10`; rc11 formalizes that accepted representation rather than creating a new serialization revision.
- Encode the exact six-member parsed root shape, profile kind/release constants, non-empty source-release/scope strings, lowercase 64-hex source-digest syntax, and the accepted four-state entry vocabulary.
- Require `project_application_record_id` for `applicable`, `not_applicable`, and `undetermined`; prohibit it for profile-only `no_current_disposition`.
- Reject unknown root/entry members, parsed null/type mismatches, unsupported state tokens, malformed digest strings, and exact duplicate complete entry objects.
- Explicitly keep complete PAO-domain coverage, cross-entry authority-ID uniqueness, authority existence/class, Project Application trace correctness, actual source-SHA correspondence, entry ordering, and raw-YAML restrictions outside schema-only proof.
- Preserve `undetermined` as valid engineering-unresolved state and `no_current_disposition` as profile-only dataset-relative absence.
- Introduce no profile generator, source-aware validator, API/CLI, resolver, applicability inference, AI approval, context package, CI completion gate, code generation, new L3 Pattern, L4 guidance, or Development Context Recovery workflow state.
- Change no accepted rc10 fixture, Project Application representation/schema/validator/views, frozen source, workflow, trust boundary, or regression implementation.

## v0.0.6rc10 — Effective Project Profile Canonical Representation Foundation

- Continue the controlled v0.0.6 line after the independent rc09 review returned clean `PASS / GATE YES` with zero findings.
- Add `docs/executable-governance/34_SCAF_v0.0.6rc10_Effective_Project_Profile_Canonical_Representation_Foundation.md`.
- Add `examples/effective-project-profile.yaml` as the first canonical machine-readable Effective Project Profile YAML fixture.
- Preserve the rc09 four-state semantics: `applicable`, `not_applicable`, `undetermined`, and profile-only `no_current_disposition`.
- Bind each profile to one exact opaque `project_scope_ref`, one SCAF source release, and the SHA-256 of the exact Project Application source bytes used for derivation.
- Represent the complete validated Project-Applicable Obligation domain exactly once, ordered by exact `scaf_authority_id`; exclude FNI.
- Require `project_application_record_id` only for states backed by a current Project Application record and prohibit it for `no_current_disposition`.
- Keep Project Application rationale/provenance in the Project Application source rather than duplicating it into the profile.
- Do not serialize redundant state counts, timestamps, environment-specific paths, Pattern recommendations, implementation/compliance/verification/closure state, or copied authority text.
- Introduce no profile schema, generator, validator, API, CLI, scope/reference resolver, applicability inference, AI approval, context package, CI completion gate, code generation, new L3 Pattern, L4 guidance, or Development Context Recovery workflow state.
- Change no frozen/accepted source, Project Application fixture/schema/validator/views, workflow, trust boundary, or regression implementation.

## v0.0.6rc09 — Effective Project Profile Semantic Foundation

- Continue the controlled v0.0.6 line after the independent rc08 review returned clean `PASS / GATE YES` with zero findings.
- Add `docs/executable-governance/33_SCAF_v0.0.6rc09_Effective_Project_Profile_Semantic_Foundation.md`.
- Define Effective Project Profile as a subordinate derived current-state projection over one exact selected project scope and the complete validated Project-Applicable Obligation domain for the bound SCAF source release.
- Define the mutually exclusive/exhaustive profile states `applicable`, `not_applicable`, `undetermined`, and `no_current_disposition`.
- Define `no_current_disposition` as profile-only derived absence of a current Project Application record for the exact PAO/scope pair in the selected validated dataset; do not add it to the Project Application applicability vocabulary.
- Preserve `undetermined` as explicit engineering-unresolved state and keep it distinct from record absence.
- Define total-domain partition semantics without hard-coding the current 218-PAO inventory as a permanent cross-release constant.
- Keep project-scope matching exact-string and resolution-neutral; define no scope hierarchy, inheritance or resolver.
- Prohibit applicability inference from L3 traces, other scopes, Pattern availability, implementation/evidence presence, or record absence.
- Preserve Project Design Authority, applicability correctness, Pattern selection, compliance, verification/evidence, risk and closure outside profile authority.
- Introduce no profile serialization/schema/generator/API/CLI, context package, CI completion gate, code generation, new L3 Pattern, L4 guidance, or Development Context Recovery workflow state.
- Change no frozen/accepted source, schema, validator, query implementation, workflow, trust boundary or regression behavior.

## v0.0.6rc08 — Project Application Validated Read/Query View Foundation

- Continue the controlled v0.0.6 line after the independent rc07 review returned clean `PASS / GATE YES` with zero findings.
- Add `tools/scaf_project_application_views/` as a deterministic validated read-only Project Application query foundation.
- Add supported validation-owning Python APIs `query_record()`, `query_authority()`, and `query_scope()`; callers cannot substitute pre-parsed records or caller-created validation contexts.
- Validate and consume the selected Project Application bytes from the same private snapshot before projection.
- Make authority queries use a source-validated frozen Project-Applicable Obligation query domain, including valid zero-record results for known PAOs with no current Project Application record.
- Keep scope queries as exact opaque-string filters and explicitly report `scope_resolution: not_performed`; no scope existence/resolution claim is introduced.
- Preserve deterministic record projections, stable applicability counts, detached read-only result copies, and deterministic text/JSON output.
- Keep the production CLI repository/schema/authority-registry boundary fixed while allowing caller selection of the Project Application dataset.
- Preserve representation-valid `undetermined` as legitimate engineering-unresolved state.
- Introduce no project-scope/reference resolver, applicability inference, AI approval, Pattern recommendation/selection, Effective Project Profile, context packaging, CI completion gate, code generation, new L3 Pattern, L4 guidance, or Development Context Recovery workflow state.
- Change no frozen v0.0.2/v0.0.3/v0.0.4/v0.0.5 source, accepted rc04 fixture, rc06 schema, rc07 validator, or frozen regression behavior.

## v0.0.6rc07 — Project Application Validator Foundation

- Continue the controlled v0.0.6 line after the independent rc06 review returned clean `GATE: YES` with zero findings and confirmed the schema boundary is ready for a separately reviewed Project Application validator.
- Add `tools/scaf_project_application_validator/` as the first executable Project Application representation/source-aware validator foundation.
- Chain raw-YAML policy checks, strict safe loading, the accepted rc06 Draft 2020-12 schema, cross-record identity checks, deterministic record/reference-list ordering, frozen authority-registry validation, and `scaf_authority_id` source-aware target resolution.
- Reject duplicate YAML keys, anchors, aliases, merge keys, custom tags, multi-document streams, and non-string mapping keys before parsed-instance validation.
- Enforce unique `record_id` values and unique active `(scaf_authority_id, project_scope_ref)` pairs across the current-state dataset.
- Enforce accepted exact-ascending ordering for records and the five canonical repeating reference roles.
- Resolve each `scaf_authority_id` only after the frozen authority registry passes its existing source-aware validator; require target class `Project-Applicable Obligation` and source-release consistency.
- Keep project-controlled scope/reference values opaque; do not introduce a project reference locator/resolver.
- Report `REPRESENTATION RESULT: PASS/FAIL` only; do not convert representation conformance into applicability correctness, Project Design Authority approval, compliance, verification, Pattern selection or closure.
- Add bounded validator regressions while keeping all frozen v0.0.4/v0.0.5 suites and accepted rc04 fixture / rc06 schema unchanged.
- Introduce no automatic applicability inference, AI approval, Pattern recommendation/selection, Effective Project Profile, context packager, CI applicability-completion gate, code generation, new L3 Pattern or L4 guidance.

## v0.0.6rc06 — Project Application Schema Foundation

- Continue the controlled v0.0.6 line after the independent rc05 review returned clean `GATE: YES`, closed `SCAF-RC04-001`, and reported zero new findings.
- Add `schemas/project-application.schema.json` using JSON Schema Draft 2020-12 to encode the machine-determinable parsed-instance portion of the accepted rc04 Project Application representation contract.
- Add `docs/executable-governance/30_SCAF_v0.0.6rc06_Project_Application_Schema_Foundation.md` defining schema scope, authority boundary, coverage and explicit limitations.
- Preserve `representation_release: v0.0.6rc04`; rc06 is a schema release and does not revise the accepted serialization contract.
- Encode exact record field set, constants, applicability vocabulary, reference-list types, state-dependent `disposition_basis` presence/prohibition, resolved-state direct-basis structural sufficiency, null/type constraints and exact duplicate rejection within individual reference lists.
- Keep `undetermined` representation-valid when `unresolved_reason` / `awaiting_refs` satisfy the accepted current-state contract.
- Explicitly do not claim schema-only enforcement of lexical ordering, cross-record `record_id` or authority/scope uniqueness, raw-YAML duplicate-key/anchor restrictions, framework authority resolution, opaque reference resolution or engineering correctness.
- Do not duplicate the frozen 218 Project-Applicable Obligation population into the schema; source-aware authority-class/existence checks remain for a later validator.
- Introduce no Project Application validator, resolver, applicability inference, AI approval, Pattern selection, Effective Project Profile, CI completion gate, code generation, new L3 Pattern or L4 guidance.
- Change no frozen normative/L3 source, frozen registry/schema/tool/workflow/release-integrity/trust surface, accepted rc04 fixture, or frozen regression behavior.

## v0.0.6rc05 — Project Application Serialization Fixture Coverage Hardening

- Continue the controlled v0.0.6 line after the independent rc04 review returned `GATE: YES` with one Minor finding, `SCAF-RC04-001`, and no frozen-baseline regression.
- Add `docs/executable-governance/29_SCAF_v0.0.6rc05_Project_Application_Serialization_Fixture_Coverage_Hardening.md`.
- Close only the rc04 fixture-coverage gap; do not change the accepted rc04 serialization contract.
- Expand `examples/project-application.yaml` so each canonical repeating reference role (`basis_refs`, `awaiting_refs`, `decision_refs`, `authority_refs`, `supporting_refs`) has at least one multi-item illustrative example across the existing three-record fixture.
- Keep every expanded list ordered by exact serialized string ascending and duplicate-free, making the accepted deterministic collection rule directly observable rather than vacuously satisfied by single-item lists.
- Retain exactly the same three record identities and applicability states (`applicable`, `not_applicable`, `undetermined`).
- Retain `representation_release: v0.0.6rc04` because rc05 is fixture coverage hardening, not a new serialization-contract revision.
- Preserve direct-basis role separation, current-state compatibility, opaque-reference semantics, invalid-vs-unresolved separation, and all Project Design Authority / project-governance boundaries.
- Introduce no JSON Schema, Project Application validator, scope/reference resolver, automatic applicability inference, Pattern selection, Effective Project Profile, CI completion gate, code generation, new L3 Pattern, or L4 guidance.
- Change no frozen normative/L3 source, registry, schema, executable validator/query implementation, workflow, release-integrity manifest, external trust input, or accepted regression behavior.

## v0.0.6rc04 — SCAF-APP Concrete Project Application Serialization Foundation

- Continue the controlled v0.0.6 line after the independent rc03 review returned `GATE: YES`, closed `SCAF-RC02-001` / `SCAF-RC02-002`, and reported zero new findings.
- Add `docs/executable-governance/28_SCAF_v0.0.6rc04_SCAF_APP_Concrete_Project_Application_Serialization_Foundation.md`.
- Add `examples/project-application.yaml` as the first concrete illustrative YAML serialization fixture for the accepted Project Application Record contract; the fixture does not assert real project applicability decisions.
- Freeze the initial top-level YAML shape as one mapping containing `records`, with each record serialized using the accepted eleven canonical logical fields.
- Preserve exact applicability tokens `applicable`, `not_applicable`, and `undetermined`.
- Preserve rc03 direct-basis semantics: only `disposition_basis.summary` / `basis_refs` may satisfy direct applicability basis; top-level decision/authority/supporting references remain role-distinct.
- Define explicit current-state serialization rules for `summary`, `basis_refs`, `unresolved_reason`, and `awaiting_refs`, including omission, required empty-list representation, and prohibition of YAML null placeholders.
- Keep `unresolved_reason` / `awaiting_refs` absent from resolved current states and require `unresolved_reason` for `undetermined`.
- Serialize reference surfaces as opaque non-empty string lists without defining a scope/reference locator grammar or resolver.
- Define deterministic record/reference-list ordering and prohibit duplicate list items, duplicate mapping keys, YAML anchors/aliases, merge keys, custom tags, and multi-document streams.
- Keep the concrete fixture subordinate to SCAF-APP semantics and separate from frozen `authority-registry.yaml` / `l3-trace-registry.yaml`.
- Introduce no JSON Schema, Project Application validator, project-scope/reference resolver, history model, automatic applicability classifier, Pattern selection, Effective Project Profile, CI applicability-completion gate, code generation, new L3 Pattern, or L4 guidance.
- Change no frozen normative/L3 source, frozen registry/schema/tool/workflow/release-integrity/trust surface, or accepted regression behavior.

## v0.0.6rc03 — SCAF-APP Project Application Record Basis-Role and State-Compatibility Hardening

- Continue the controlled v0.0.6 line after the independent rc02 review returned `GATE: NO` with `SCAF-RC02-001` (Major) and `SCAF-RC02-002` (Minor), with no frozen-baseline regression.
- Add `docs/executable-governance/27_SCAF_v0.0.6rc03_SCAF_APP_Project_Application_Record_Basis_Role_and_State_Compatibility_Hardening.md`.
- Close `SCAF-RC02-001` by defining `disposition_basis.summary` and `disposition_basis.basis_refs` as the only surfaces that may satisfy direct applicability-basis sufficiency.
- Define `basis_refs` as controlled references that directly establish, justify, or substantively support the current applicability disposition for the declared scope.
- Keep `decision_refs`, `authority_refs`, and `supporting_refs` as role-distinct decision trace, authority provenance, and related-context surfaces; their mere presence cannot satisfy applicability-basis requirements.
- Permit the same controlled target to appear on multiple role-specific reference surfaces only when it genuinely fulfills each named role; no cross-role inference is authorized.
- Close `SCAF-RC02-002` with an explicit state-compatibility matrix for all `disposition_basis` members.
- Require `unresolved_reason` exactly once for `undetermined`; prohibit `unresolved_reason` and `awaiting_refs` for `applicable` and `not_applicable` current-state records.
- Keep `summary` / `basis_refs` available for all applicability states while requiring `unresolved_reason` to remain the explicit unresolved-state basis for `undetermined`.
- Define current-state versus historical-state separation: resolved records shall not retain unresolved-only members as ad hoc history storage; history/supersession/re-evaluation remains deferred.
- Preserve representation-invalid versus engineering-unresolved separation and preserve all Project Design Authority / project-governance ownership boundaries.
- Introduce no concrete project-application serialization, schema, validator, scope resolver, automatic applicability classifier, Effective Project Profile, CI completion gate, code generation, new L3 Pattern, or L4 guidance.
- Change no frozen normative/L3 source, registry, schema, executable validator/query implementation, workflow, release-integrity manifest, external trust input, or accepted regression behavior.

## v0.0.6rc02 — SCAF-APP Canonical Project Application Record Model

- Continue the controlled v0.0.6 line after the independent rc01 review returned `PASS / GATE YES` with zero Critical, Major, Minor, or Trivial findings.
- Add `docs/executable-governance/26_SCAF_v0.0.6rc02_SCAF_APP_Canonical_Project_Application_Record_Model.md`.
- Convert the accepted rc01 semantic foundation into a deterministic canonical logical record contract without yet introducing a concrete project-application dataset/schema/validator.
- Define canonical logical fields: `record_id`, `record_kind`, `representation_release`, `scaf_authority_id`, `scaf_source_release`, `project_scope_ref`, `applicability`, `disposition_basis`, `decision_refs`, `authority_refs`, and `supporting_refs`.
- Freeze the initial applicability token vocabulary as `applicable`, `not_applicable`, and `undetermined`.
- Keep Project Application Record identity project-local and distinct from frozen SCAF authority identity; prevent ambiguous duplicate applicability assertions for the same `(scaf_authority_id, project_scope_ref)` pair.
- Keep `project_scope_ref` explicit and project-controlled while deferring scope-kind hierarchy, inheritance and registry syntax.
- Define structured `disposition_basis` semantics with `summary`, `basis_refs`, `unresolved_reason`, and `awaiting_refs`.
- Require controlled basis/provenance for `not_applicable`; prohibit a bare N/A token with no attributable basis.
- Require `unresolved_reason` for `undetermined` while preserving `undetermined` as valid engineering-unresolved state rather than representation failure.
- Preserve Project Design Authority and other project-governance authority ownership through bounded `decision_refs`, `authority_refs`, and `supporting_refs`; references do not transfer authority to the Project Application Record or tooling.
- Preserve the separation between representation-invalid conditions and engineering-unresolved work.
- Explicitly defer decision/deviation/risk/verification/evidence/closure/re-evaluation state fields, tailoring taxonomy, Pattern selection and implementation state rather than collapsing them into a single status.
- Preserve frozen framework truth in `authority-registry.yaml`, frozen L2↔L3 trace in `l3-trace-registry.yaml`, and the no-applicability/no-selection/no-satisfaction inference boundary.
- Change no frozen normative/L3 source, machine-readable registry, schema, validator/query implementation, workflow, release-integrity manifest, external trust input, or accepted regression behavior.

## v0.0.6rc01 — SCAF-APP Machine-Readable Project Application Semantic Model Foundation

- Open the first controlled development line after the formal v0.0.5 freeze without modifying or respinning the frozen v0.0.5 baseline.
- Select project-application semantics as the next gap-driven milestone rather than automatically advancing to L4.
- Add `docs/executable-governance/25_SCAF_v0.0.6rc01_SCAF_APP_Machine_Readable_Project_Application_Semantic_Model_Foundation.md`.
- Define the semantic role and authority boundary of a future machine-readable `SCAF-APP` Project Application Record.
- Require explicit project-scope binding so applicability is not silently generalized across Project/System/Node/domain/interface/service scopes.
- Define `Applicable`, `Not Applicable`, and `Undetermined` as distinct applicability semantic classes while deliberately deferring exact serialization tokens/schema fields.
- Preserve `Undetermined` as legitimate unresolved engineering state distinct from malformed representation, project failure, verification failure, non-compliance, or `Not Applicable`.
- Preserve frozen `SCAF-AK-003` separation among applicability, decision, deviation, risk, verification, evidence, closure, and re-evaluation rather than introducing a single PASS/FAIL project status.
- Establish rationale/provenance semantics for project engineering judgment while preserving Project Design Authority and other underlying authority ownership.
- Preserve the boundary that tool-determinable representation facts are not equivalent to project engineering judgment or project authority decisions.
- Preserve framework truth and project truth as separate representation surfaces; do not add project applicability/PDA/rationale/verification/closure state to frozen `authority-registry.yaml`.
- Preserve the frozen v0.0.5 boundary that L2↔L3 trace presence/absence does not imply project applicability, Pattern selection, satisfaction, verification, closure, or project failure.
- Defer concrete project-application serialization, schema, validator, project-scope registry, full lifecycle state serialization, tailoring taxonomy, automatic applicability inference, generated Effective Project Profile, resolver/context packaging, CI enforcement, code generation, new L3 content, and L4 guidance.
- Change no frozen normative/L3 source, machine-readable registry, schema, executable validator/query implementation, workflow, release-integrity manifest, external trust input, or accepted regression behavior.

## v0.0.5 — Frozen L3 Machine-Readable Traceability Baseline

- Formally freeze the reviewed `v0.0.5rc10` source state as `v0.0.5 — Frozen L3 Machine-Readable Traceability Baseline` after the independent freeze-candidate review returned `GATE: YES` with zero Critical, Major, Minor, or Trivial findings.
- Preserve the accepted authority inventory at 294 records / 218 Project-Applicable Obligations / 76 Framework Normative Invariants.
- Freeze the accepted L3 machine-readable trace inventory at 12 Patterns / 119 relations / 23 Primary / 41 Supporting / 55 Constraint / 82 unique referenced L2 IDs / 15 qualifier-bearing relations.
- Freeze the controlled relation vocabulary (`primary_realization_candidate`, `supporting_realization`, `constraint_input`) and seven-field relation representation.
- Freeze the accepted source-aware trace-validation boundary and same-root trace + authority validation ownership before supported L2↔L3 projection.
- Freeze the supported read-only public query API (`TraceViewError`, `query_l2`, `query_pattern`), deterministic projection/order/JSON behavior, zero-relation semantics, and Framework Normative Invariant query-domain boundary.
- Preserve the frozen v0.0.2 L1/L2 source identity, frozen v0.0.3 L3 source identity, and frozen v0.0.4 executable-governance controls unchanged.
- Preserve regression baselines at rc6 trace-validator 24/24, trace-view/query 28/28, and frozen executable-governance 41/41.
- Preserve the six-artifact production trust set and external-trust-input model unchanged. The freeze-candidate review did not independently execute the production external-trust gate because the required repository-external trust bundle was unavailable; no production PASS is claimed.
- Add `docs/executable-governance/24_SCAF_v0.0.5_Formal_Freeze_Decision.md` and update release/navigation documentation only.
- `v0.0.5` is immutable after this explicit governance freeze decision. Future capability work must begin on a new controlled RC/version line and must not modify this frozen baseline in place.

### rc10 freeze-candidate review disposition

```text
Critical: 0
Major:    0
Minor:    0
Trivial:  0

V0.0.5 L3 MACHINE-READABLE TRACEABILITY MILESTONE CONSOLIDATION / FREEZE-CANDIDATE GATE: YES
```

## v0.0.5rc10 — L3 Machine-Readable Traceability Milestone Consolidation and Freeze Candidate

- Continue the controlled v0.0.5 line after the independent **full-source rc9 re-review** returned a clean gate `YES` with zero Critical, Major, Minor, or Trivial findings.
- Record `RC7-01: REMAINS RESOLVED`, `RC8-01: REMAINS RESOLVED`, `RC8-02: REMAINS RESOLVED`, and `RC9-01: NOT APPLICABLE UNDER CORRECTED CONTRACT` as the accepted pre-consolidation finding state.
- Consolidate the v0.0.5 dependency chain from the machine-readable trace model through exact serialization, schema/source-extraction contract, source-aware validation, and validated deterministic read-only L2↔L3 consumption.
- Preserve the frozen v0.0.2 L1/L2 and v0.0.3 L3 semantic baselines, frozen v0.0.4 executable-governance baseline, authority registry/schema, trace registry/schema, accepted validators, trace-view/query implementation, workflow, six-artifact production trust set, and all regression code unchanged.
- Preserve the accepted trace inventory at 12 Patterns / 119 relations / 23 Primary / 41 Supporting / 55 Constraint / 82 unique L2 IDs / 15 qualifiers.
- Preserve the authority inventory at 294 records / 218 Project-Applicable Obligations / 76 Framework Normative Invariants.
- Preserve the accepted regression inventories at rc6 trace validator 24/24, rc9 trace views/query 28/28, and frozen executable-governance 41/41.
- Define rc10 as **consolidation-only**: no new relation semantics, authority semantics, project-applicability inference, recommendation/selection, generated persisted indexes, registry generation, code generation, CI/trust-chain expansion, new L3 Pattern work, M3/M4, or L4 guidance.
- Add `docs/executable-governance/23_SCAF_v0.0.5rc10_L3_Machine_Readable_Traceability_Milestone_Consolidation_and_Freeze_Candidate.md` and update only current release/navigation/consolidation documentation.
- Establish freeze-candidate eligibility for independent review only. rc10 is **not** a formal frozen `v0.0.5`; formal freeze requires a separate explicit governance decision after a clean freeze-candidate review.

### rc9 full-source re-review disposition

```text
Critical: 0
Major:    0
Minor:    0
Trivial:  0

RC7-01: REMAINS RESOLVED
RC8-01: REMAINS RESOLVED
RC8-02: REMAINS RESOLVED
RC9-01: NOT APPLICABLE UNDER CORRECTED CONTRACT

V0.0.5 L3 TRACE VIEWS AUTHORITY VALIDATION AND CLI EXECUTION BOUNDARY CLOSURE RE-REVIEW GATE: YES
```

## v0.0.5rc9 — L3 Trace Views Authority Validation and CLI Execution Boundary Closure

- Continue the controlled v0.0.5 line after the independent rc8 review confirmed `RC7-01: RESOLVED` but returned `V0.0.5 L3 TRACE VIEWS VALIDATED PROGRAMMATIC API BOUNDARY HARDENING GATE: NO` with `RC8-01` Major and `RC8-02` Minor.
- Close `RC8-01` by requiring every supported public trace query to pass both the accepted rc6 source-aware trace validator and the frozen authority-registry schema/source-aware validator against the same resolved repository root before any view is returned.
- Reuse the accepted frozen `tools.scaf_validator.validator.validate_registry()` implementation unchanged; do not duplicate authority-schema/source validation inside trace views.
- Keep `query_l2(repo_root, l2_id)` and `query_pattern(repo_root, pattern_id)` as the supported validation-owning public Python API and preserve internal/private projection helpers.
- Close `RC8-02` by replacing eager package re-export with lazy package attribute resolution so importing `tools.scaf_trace_views` does not preload the `python -m tools.scaf_trace_views.query` target.
- Add real subprocess regressions for the documented `python -m` command requiring successful stdout with empty stderr and fail-closed validation errors with empty stdout/non-zero exit.
- Add bounded negative-condition regressions for authority-class drift, fabricated Project-Applicable authority records, and invalid authority-registry state via both public query directions.
- Expand the trace-view/query development suite from 23 to 28 tests.
- Preserve accepted trace-view projection semantics, all 119 relations, seven-field fidelity, qualifiers, zero-relation behavior, deterministic ordering/JSON, and the no-applicability/no-compliance/no-closure boundary.
- Preserve the accepted rc6 trace validator, frozen authority validator, authority/trace registries and schemas, frozen v0.0.2/v0.0.3 trees, frozen v0.0.4 controls, 41-test regression inventory, workflow and six-artifact production trust set unchanged.

### rc8 review disposition

```text
Critical: 0
Major:    1
Minor:    1
Trivial:  0

RC7-01: RESOLVED
RC8-01 — Supported public queries consume authority-registry classification state outside the owned rc6 validation proof
RC8-02 — Eager package re-export preloads/re-executes the documented python -m CLI target

V0.0.5 L3 TRACE VIEWS VALIDATED PROGRAMMATIC API BOUNDARY HARDENING GATE: NO
```

## v0.0.5rc8 — L3 Trace Views Validated Programmatic API Boundary Hardening

- Continue the controlled v0.0.5 line after the independent rc7 review returned `V0.0.5 L3 DETERMINISTIC TRACE VIEWS / QUERY FOUNDATION GATE: NO` with one blocking Major, `RC7-01`.
- Close `RC7-01` by removing the caller-constructible public `TraceContext` and public `build_l2_view()` / `build_pattern_view()` view-builder surfaces.
- Define `query_l2(repo_root, l2_id)` and `query_pattern(repo_root, pattern_id)` as the supported public Python query APIs; each owns the rc6 `validate_repository()` proof before returning any view.
- Make the CLI call the same public query APIs so CLI and programmatic consumers share one validation-owning trust path.
- Rename validated context and projection helpers as internal implementation details and require an internal validation seal before a `_ValidatedTraceContext` can be constructed.
- Add explicit package/module `__all__` exports so the supported public API surface is limited to `TraceViewError`, `query_l2`, `query_pattern`, and module `main` where applicable.
- Preserve all rc7 trace-view semantics: typed relation classes, seven-field relation fidelity, qualifiers, multi-type pairs, zero-relation behavior, Project-Applicable query domain, deterministic ordering, deterministic JSON, and stdout-only CLI behavior.
- Expand the trace-view/query development suite from 17 to 23 tests with focused coverage for public L2 validation ownership, public Pattern validation ownership, invalid-repository failure through public APIs, caller-constructed internal-context rejection, legacy public-symbol removal, package export surface, and CLI reuse of the same public query entry point.
- Preserve accepted rc3 registry, rc4 trace schema, rc6 source-aware validator, frozen authority/frozen trees, v0.0.4 executable controls, 41-test frozen regression inventory, and six-artifact production external-trust gate unchanged.
- Defer persisted/generated indexes, registry generation, resolver/context selection, semantic ranking, project applicability, recommendation/selection, compliance/verification/closure inference, new L3 work, M3/M4, L4, code generation, and CI/trust-chain expansion.

### rc7 review disposition

```text
Critical: 0
Major:    1
Minor:    0
Trivial:  0

RC7-01 — Public view-builder path can return trace views from an unvalidated caller-constructed TraceContext

V0.0.5 L3 DETERMINISTIC TRACE VIEWS / QUERY FOUNDATION GATE: NO
```

## v0.0.5rc7 — L3 Deterministic Trace Views / Query Foundation

- Continue the controlled v0.0.5 line after the independent rc6 review resolved `R5-01` and `R5-02`, opened zero new findings, and returned `V0.0.5 L3 TRACE VALIDATOR FAIL-CLOSED SOURCE-BOUNDARY HARDENING GATE: YES`.
- Add `tools/scaf_trace_views/` as the first controlled read-only consumer of the accepted source-validated L3 trace.
- Require every view/query invocation to pass the rc6 source-aware trace validator before emitting any view payload.
- Add deterministic L2 -> L3 lookup by known authority identity while preserving typed relation class, qualifier context, source locator and source release.
- Add deterministic L3 Pattern -> L2 lookup by known frozen Pattern identity with the same seven-field relation fidelity.
- Preserve relation classes as `primary_realization_candidate`, `supporting_realization`, and `constraint_input`; do not flatten them into a generic candidate/related list.
- Preserve the accepted multi-type Pattern/L2 pairs as distinct typed records.
- Define L2-view ordering by relation type then `pattern_id`, and Pattern-view ordering by relation type then `l2_id`.
- Treat a known Project-Applicable Obligation with no current L3 trace as a valid zero-relation result rather than an error or negative applicability decision.
- Keep Framework Normative Invariants outside the current L2-to-L3 query domain and fail closed on unknown/non-project-applicable identities, unknown frozen Pattern identities, or any repository state that fails source-aware trace validation.
- Provide deterministic stdout text and JSON output; do not create or persist generated index files.
- Add a separate 17-test trace-view/query development regression suite covering bidirectional lookup, full 119-relation coverage, qualifier/multi-type preservation, ordering, zero-result semantics, Project-Applicable-domain enforcement, invalid-ID behavior, validated-source gating and deterministic JSON.
- Add `docs/executable-governance/20_SCAF_v0.0.5rc7_L3_Deterministic_Trace_Views_and_Query_Foundation.md`.
- Preserve `l3-trace-registry.yaml`, the rc4 trace schema, rc6 trace validator, authority registry, frozen baselines, frozen 41-test inventory, rc6 24-test validator inventory, and six-artifact production trust chain unchanged.
- Preserve the boundary that Queried / Traced / Serialized / Source-validated does not imply Applicable, Recommended, Selected, Satisfied, Compliant, Verified, or Closed.
- Defer persisted/generated index files, registry generation/rewrite, authority/context resolver logic, semantic ranking/relevance, project applicability, Pattern recommendation/auto-selection, L4, code generation and CI/trust-chain expansion.

### rc6 review disposition

```text
Critical: 0
Major:    0
Minor:    0
Trivial:  0

R5-01: RESOLVED
R5-02: RESOLVED

V0.0.5 L3 TRACE VALIDATOR FAIL-CLOSED SOURCE-BOUNDARY HARDENING GATE: YES
```

## v0.0.5rc6 — L3 Trace Validator Fail-Closed Source-Boundary Hardening

- Continue the controlled v0.0.5 line after the independent rc5 review returned `V0.0.5 L3 SOURCE-AWARE TRACE VALIDATOR FOUNDATION GATE: NO` with two blocking Major findings.
- Close `R5-01` by making Constraint Inputs separator parsing position-aware: clause start rejects leading comma, while every later ID/item transition requires an explicit comma.
- Reject adjacency of code-span L2 IDs without comma and reject a later reviewed leading qualifier such as `applicable` when its preceding comma separator is missing.
- Preserve the accepted rc4 semicolon reset, `applicable`, one-ID `conditional ... where ...`, direct `where ...`, and `outcomes when ...` semantics without broadening the grammar.
- Close `R5-02` by structurally locating exactly one `## Metadata` section and exactly one reviewed `| Field | Value |` table inside that section.
- Restrict machine-authoritative `Pattern ID`, `Primary L2 Trace`, `Supporting L2 Trace`, and `Constraint Inputs` extraction to that single metadata table.
- Ensure same-key rows under narrative headings/tables cannot replace or supplement the authoritative Metadata table.
- Require missing Metadata section/table/required rows to fail closed.
- Expand `tools/scaf_trace_validator` regressions from 16 to 24 tests, including the independent rc5 reproductions and bounded source-boundary variants.
- Keep the accepted rc3 `l3-trace-registry.yaml`, rc4 trace schema, frozen authority registry, frozen v0.0.2/v0.0.3 sources, and all frozen v0.0.4 executable controls unchanged.
- Preserve the frozen 41-test regression inventory and six-artifact external-trust production gate; the rc6 trace validator remains a separately reviewed development control outside that frozen trust set.
- Add `docs/executable-governance/19_SCAF_v0.0.5rc6_L3_Trace_Validator_Fail_Closed_Source_Boundary_Hardening.md`.
- Defer registry generation, generated views/indexes, resolver/context packaging, project applicability/selection inference, compliance/verification/closure inference, L4, and CI/trust-chain expansion.

### rc5 review disposition

```text
Critical: 0
Major:    2
Minor:    0
Trivial:  0

R5-01 — Constraint parser accepted missing/misplaced comma separators
R5-02 — Authoritative-row extraction was not confined to the ## Metadata table

V0.0.5 L3 SOURCE-AWARE TRACE VALIDATOR FOUNDATION GATE: NO
```

## v0.0.5rc5 — L3 Source-Aware Trace Validator Foundation

- Continue the controlled v0.0.5 line after the independent rc4 review returned `V0.0.5 L3 TRACE SCHEMA / SOURCE-EXTRACTION CONTRACT FOUNDATION GATE: YES` with zero findings.
- Add `tools/scaf_trace_validator/validator.py` as an independent executable implementation of the accepted rc4 trace schema and frozen-source extraction contract.
- Validate `l3-trace-registry.yaml` with duplicate-key-rejecting YAML loading and the accepted Draft 2020-12 `schemas/l3-trace-registry.schema.json`.
- Reconstruct relations only from the frozen Pattern metadata rows `Primary L2 Trace`, `Supporting L2 Trace`, and `Constraint Inputs`; narrative prose remains non-authoritative for machine edge creation.
- Implement the accepted rc4 fail-closed parsing rules for comma/semicolon scope, `applicable`, one-ID `conditional ... where ...`, direct `where ...`, `outcomes when ...`, and bounded qualifier whitespace normalization.
- Require exact equality between the canonically sorted frozen-source reconstruction and all seven serialized fields of the 119-record registry population.
- Prove `(pattern_id, relation_type, l2_id)` tuple uniqueness independently of JSON Schema `uniqueItems` and prove canonical cross-record ordering independently of schema validation.
- Resolve every serialized L2 identity against frozen `authority-registry.yaml`; current accepted population resolves all 82 unique referenced L2 IDs.
- Add sixteen focused trace-validator regressions covering accepted PASS, omission/invention, tuple duplicates, ordering, qualifier omission/reassociation, unresolved L2 identities, source locator mismatch, unsupported syntax, metadata-row duplication, and narrative non-authority.
- Keep accepted rc3 `l3-trace-registry.yaml` and accepted rc4 trace schema byte-unchanged.
- Preserve frozen v0.0.2/v0.0.3 source, frozen v0.0.4 executable controls, the 41-test frozen regression inventory, six-artifact external trust bundle, workflow and production CI-gate behavior unchanged.
- Keep the rc5 trace validator outside the frozen v0.0.4 trust bundle and do not claim CI/merge enforcement for the new development control.
- Defer automatic trace-registry generation, generated forward/reverse views, authority/context resolver, project applicability inference, Pattern auto-selection, satisfaction/compliance/verification/closure inference, new L3 work, M3/M4, L4 guidance, code generation and CI/trust expansion.


## v0.0.5rc4 — L3 Trace Schema & Source-Extraction Contract Foundation

- Continue the controlled v0.0.5 line after the independent rc3 review returned `V0.0.5 L3 MACHINE-READABLE TRACE SERIALIZATION FOUNDATION GATE: YES` with zero findings.
- Add `schemas/l3-trace-registry.schema.json` using JSON Schema Draft 2020-12 as the structural contract for the accepted rc3 `l3-trace-registry.yaml`.
- Bind the current schema to `trace_registry_version: 1`, `representation_release: v0.0.5rc3`, the accepted twelve Pattern identities/source paths, the three controlled relation classes/source fields, exactly 119 records, the 23 / 41 / 55 relation split, and 15 non-null qualifiers.
- Reject unknown top-level and relation-record fields; require the accepted seven-field record shape and nullable/non-empty-string qualifier representation.
- Explicitly keep composite triple uniqueness, canonical cross-record ordering, L2 authority resolution, exact source membership and qualifier fidelity outside JSON Schema and in the future source-aware validator proof contract.
- Add `docs/executable-governance/17_SCAF_v0.0.5rc4_L3_Trace_Schema_and_Source_Extraction_Contract_Foundation.md`.
- Define deterministic extraction only from frozen metadata rows `Primary L2 Trace`, `Supporting L2 Trace`, and `Constraint Inputs`; narrative `## 5. L2 Trace` prose remains non-authoritative for machine edges.
- Define fail-closed parsing for the current frozen `applicable`, `conditional ... where ...`, direct `where ...`, and `applicable ... outcomes when ...` qualifier forms, including semicolon scope reset, comma-group behavior and canonical whitespace preservation.
- Require unsupported/new source syntax to fail rather than being inferred by future parser code.
- Keep accepted rc3 `l3-trace-registry.yaml` byte-unchanged with `representation_release: v0.0.5rc3`; keep frozen `authority-registry.yaml`, frozen baselines and v0.0.4 executable controls unchanged.
- Preserve all 41 accepted executable-governance regressions and production external-trust CI-gate behavior.
- Defer executable trace parser/validator, automatic registry generation, generated reverse/forward views, resolver/context packaging, project inference, Pattern auto-selection, new L3 work, M3/M4, L4 guidance, code generation and additional CI/trust capability.


## v0.0.5rc3 — L3 Machine-Readable Trace Serialization Foundation

- Continue the controlled v0.0.5 line after rc2 closed `R1-01` and `R1-02` and returned `V0.0.5 L3 TRACE MODEL DETERMINISM / QUALIFIER-FIDELITY CLEANUP GATE: YES`.
- Add repository-root `l3-trace-registry.yaml` as the first concrete subordinate serialization of the frozen v0.0.3 L3 trace metadata.
- Serialize exactly 119 unique typed relation records across 12 Patterns: 23 `primary_realization_candidate`, 41 `supporting_realization`, and 55 `constraint_input`, referencing 82 unique frozen L2 IDs.
- Realize the accepted canonical ordering by `pattern_id`, fixed relation-type order, then `l2_id`.
- Serialize each record with `pattern_id`, `relation_type`, `l2_id`, `pattern_source_path`, `pattern_source_field`, `source_release`, and always-present nullable `qualifier`.
- Preserve 15 material source-qualifier associations as canonical source-fidelity text without introducing executable applicability/condition semantics.
- Keep frozen v0.0.3 Pattern Markdown metadata as semantic trace authority and keep `authority-registry.yaml` separate and unchanged.
- Add `docs/executable-governance/16_SCAF_v0.0.5rc3_L3_Machine_Readable_Trace_Serialization_Foundation.md`.
- Preserve frozen v0.0.2/v0.0.3/v0.0.4 identities and all 41 accepted executable-governance regressions.
- Defer trace schema, executable trace validator/generator, generated reverse index, resolver/context packaging, project inference, new L3 work, M3/M4, L4 guidance, code generation, and additional CI/trust capability.

### rc3 review disposition

```text
Critical: 0
Major:    0
Minor:    0
Trivial:  0

V0.0.5 L3 MACHINE-READABLE TRACE SERIALIZATION FOUNDATION GATE: YES
```

## v0.0.5rc2 — L3 Trace Model Determinism & Qualifier-Fidelity Cleanup

- Continue the controlled v0.0.5 line after the independent rc1 review returned `V0.0.5 L3 MACHINE-READABLE TRACE REPRESENTATION MODEL FOUNDATION GATE: YES, AFTER MINOR CLEANUP`.
- Close `R1-01` by making material qualifier association mandatory in the future machine-readable representation and explicit in the future source-aware validator proof contract.
- Require later validation to reject qualifier omission, semantic alteration, scope expansion/truncation, and association with the wrong `l2_id` / relation record.
- Keep exact qualifier extraction/grouping/serialization syntax deferred and preserve the rule that qualifiers are controlled source context rather than executable project-applicability predicates.
- Close `R1-02` by changing the defined canonical future serialization ordering from advisory `should` to mandatory `shall`.
- Preserve ordering as representation determinism only, not semantic precedence.
- Preserve the rc1 relation vocabulary, 12 / 23 / 41 / 55 / 119 / 82 trace inventory, relation identity, authority-registry separation, resolver/project boundary and L4 boundary.
- Change only current navigation/history, the rc1 model contract, and the new focused rc2 closure record.
- Preserve all executable/frozen v0.0.2/v0.0.3/v0.0.4 artifacts and all 41 accepted executable-governance regressions unchanged.
- Continue to defer serialization, schema, validator implementation, generated views, resolver, project inference, new L3 work, M3/M4, L4, code generation and additional CI/trust capability.

### rc1 review disposition

```text
Critical: 0
Major:    0
Minor:    2
Trivial:  0

R1-01 — Material qualifier fidelity missing from future validator proof contract
R1-02 — Canonical deterministic ordering used advisory should

V0.0.5 L3 MACHINE-READABLE TRACE REPRESENTATION MODEL FOUNDATION GATE: YES, AFTER MINOR CLEANUP
```

## v0.0.5rc1 — L3 Machine-Readable Trace Representation Model Foundation

- Open the first controlled development line after the formal v0.0.4 executable-governance freeze.
- Select the rc1 scope from post-baseline gap/dependency analysis rather than assuming the next release must advance to L4.
- Define a subordinate machine-readable representation model for the already-frozen v0.0.3 L2-to-L3 Pattern trace semantics.
- Preserve frozen Pattern Markdown metadata as semantic trace authority and define future machine representation/generated views as subordinate/derived.
- Define controlled machine relation identifiers: `primary_realization_candidate`, `supporting_realization`, and `constraint_input`; retain the generic-`satisfies` prohibition.
- Record the current frozen trace inventory as 12 Patterns / 119 relations / 82 unique referenced L2 IDs, split 23 Primary / 41 Supporting / 55 Constraint relations.
- Define deterministic future relation identity as `(pattern_id, relation_type, l2_id)` and explicitly permit the same Pattern/L2 pair to carry more than one relation type where the frozen source does so.
- Define source-locator semantics from Pattern source path + Pattern identity + authoritative metadata field.
- Preserve existing natural-language trace qualifiers as controlled source context without interpreting them as executable project-applicability predicates.
- Keep the frozen 294-record `authority-registry.yaml` separate, with zero `SCAF-PAT-*` records and 294 empty `relations` fields.
- Define generated forward/reverse views as reproducible navigation only; reverse views must preserve relation type and material qualifiers.
- Reaffirm that traced/resolved does not imply Applicable, Selected, Satisfied, Compliant, Verified, or Closed.
- Do not introduce a concrete trace serialization, schema, validator, generated index, resolver, project inference, L4 guidance, new L3 Pattern, M3/M4, or new CI/trust capability in rc1.
- Refactor `README.md` to current-state/navigation content and keep detailed release/review history in this CHANGELOG and controlled governance records.
- Preserve frozen v0.0.2/v0.0.3/v0.0.4 semantics and executable identities unchanged.

## v0.0.4 — 2026-08-17

Formal **Frozen Executable Governance Baseline** created by explicit governance freeze decision after the independent v0.0.4rc13 review returned **`R12-01: RESOLVED`** and **`V0.0.4 FREEZE-CANDIDATE CONTROL-CHAIN DOCUMENTATION CLOSURE GATE: YES`**, with 0 Critical, 0 Major, 0 Minor, 0 Trivial and 0 open accepted upstream findings.

- freezes the reviewed rc13 executable-governance milestone as formal `v0.0.4`;
- adds `docs/executable-governance/13_SCAF_v0.0.4_Formal_Freeze_Decision.md`;
- synchronizes current release/navigation state from `v0.0.4rc13` to `v0.0.4`;
- preserves the reviewed 294 / 218 / 76 authority inventory, zero `SCAF-PAT-*` registry records and 294 empty machine-readable relations;
- preserves frozen v0.0.2 L1/L2 and v0.0.3 L3 protected-tree identities and the twelve `Available / M2 — Architecture Reviewed` L3 Patterns;
- preserves all accepted executable artifacts, six control-plane trust identities and 8 / 9 / 11 / 13 = 41 regressions unchanged from the reviewed rc13 candidate;
- preserves the runtime trust/control order: external trust input -> six topology/SHA-256 identity checks -> external-pin verification -> frozen-baseline integrity -> authority-registry validation -> same-root stage attestation -> gate result;
- preserves the historical rc10 `NO`, rc11 `YES`, rc12 `YES, AFTER MINOR CLEANUP`, and rc13 closure `YES` review dispositions;
- does not add fork-PR enforcement, branch-protection administration, signing/PKI/provenance, trust-bundle distribution, generated views, registry generation, code generation, project inference, non-empty L2-to-L3 relation semantics, new L3 work, M3/M4, or L4;
- establishes that `v0.0.4` is immutable and future work must proceed on a new controlled RC/version line.

## v0.0.4rc13 — 2026-08-17

Focused freeze-candidate documentation closure after the independent v0.0.4rc12 review returned **`V0.0.4 EXECUTABLE-GOVERNANCE MILESTONE CONSOLIDATION / FREEZE-CANDIDATE GATE: YES, AFTER MINOR CLEANUP`** and opened one Minor finding, `R12-01`.

- closes `R12-01` by explicitly separating capability/development layering from production runtime execution order;
- relabels the rc12 consolidation control-chain diagram as non-runtime capability/development layering;
- adds the verified runtime sequence: external CI trust input -> six fixed control-plane path/topology and SHA-256 identity checks -> external-pin verification -> frozen-baseline release integrity -> authority-registry semantic/structural/source validation -> same-root stage attestation -> CI gate PASS/FAIL;
- updates root README and executable-governance navigation to use the same distinction;
- adds `docs/executable-governance/12_SCAF_v0.0.4rc13_Freeze_Candidate_Control_Chain_Documentation_Closure.md`;
- changes no executable code, workflow, registry/schema, manifest, regression code, frozen normative content, or frozen L3 content;
- preserves the 8 / 9 / 11 / 13 regression inventory, six control-plane trust identities, 294 / 218 / 76 authority inventory, empty machine-readable relations, and twelve Available / M2 L3 Patterns;
- preserves the historical rc10 `NO`, rc11 `YES`, and rc12 `YES, AFTER MINOR CLEANUP` review dispositions;
- remains an RC and does not perform the formal `v0.0.4` freeze;
- continues to defer fork-PR enforcement, branch protection, signing/PKI/provenance, trust-bundle distribution, generated views, registry generation, code generation, project inference, non-empty L2→L3 relation semantics, new L3 work, M3/M4, and L4.

## v0.0.4rc12 — 2026-08-17

Executable-governance milestone consolidation / freeze-candidate RC after the independent v0.0.4rc11 review returned **`V0.0.4 CI REPOSITORY PATH-COMPONENT / ROOT-BINDING HARDENING GATE: YES`**, resolved `R10-01`, and opened no Critical, Major, Minor, or Trivial finding.

- adds one consolidation record covering the complete rc01→rc11 development/review sequence, including the rc10 `NO` result and rc11 closure;
- consolidates the current executable-governance control chain, six-artifact CI trust identity set, fixed three-stage gate, root/path hardening, and 41-test regression inventory;
- records the frozen v0.0.2 L1/L2 and v0.0.3 L3 fingerprints and the accepted 294 / 218 / 76 / twelve-Pattern populations;
- records the current authority/trust non-equivalence and the frozen / candidate / deferred boundary;
- defines explicit v0.0.4 freeze-candidate acceptance criteria and an explicit rule that a review `YES` creates freeze eligibility only, not a formal freeze;
- changes only README / CHANGELOG / executable-governance navigation plus the new rc12 consolidation record;
- preserves all executable code, workflow behavior, registry/schema, manifest, control/checker identities, regression code, frozen normative/L3 content, and accepted governance records `00_*` through `10_*`;
- does not add fork-PR enforcement, branch-protection administration, signing/PKI/provenance, generated views, registry generation, code generation, project inference, non-empty L2→L3 relation semantics, new L3 work, M3/M4, or L4.

## v0.0.4rc11 — 2026-08-17

Focused closure/hardening RC after the independent v0.0.4rc10 review returned `V0.0.4 CI TRUST-INPUT / EXECUTABLE-GOVERNANCE GATE FOUNDATION GATE: NO` with one Major blocking finding, `R10-01`.

- changed CI gate production repository-root derivation so it is bound to the lexical current checkout root rather than silently deriving root from `Path(__file__).resolve()`;
- added component-by-component no-follow path inspection for every fixed control-plane artifact path;
- requires parent components to be real directories and terminal control artifacts to be real regular files before resolution/hash/execution;
- re-checks downstream executable paths immediately before stage execution;
- requires each successful downstream control to report exactly the same verified `Repository:` root before the overall gate can continue;
- hardened the GitHub Actions bootstrap so every component of `tools/scaf_ci_gate/gate.py` is checked with `lstat` before the externally pinned SHA-256 is computed;
- added regression coverage for parent-component symlinks across all six pinned artifacts, the reproduced gate-root shadow-repository pivot, the reproduced validator-stage shadow pivot, runtime stage-root attestation, and bootstrap check-before-hash ordering;
- extended `tools/scaf_ci_gate` regressions from 8 to 13 tests while preserving the accepted validator (8), release-integrity (9), and external-pin (11) suites;
- added `docs/executable-governance/10_SCAF_v0.0.4rc11_CI_Repository_Path_Component_and_Root_Binding_Hardening.md`;
- preserved the rc10 trust-bundle semantics, six-artifact pin set, fixed stage order, trusted-main/manual workflow scope, frozen baselines, authority/project/L3 boundaries, and deferred PR/signing/provenance/generated-view/L4 scope.

## v0.0.4rc10 — 2026-08-17

CI trust-input model and executable-governance gate foundation after the independent v0.0.4rc09 review returned **`V0.0.4 EXTERNAL-PIN LOCAL-ARTIFACT SYMLINK-HARDENING GATE: YES`**, closed `R8-01`, and identified no new finding.

### Added

- added `tools/scaf_ci_gate/gate.py` as a bounded fail-closed orchestration surface above the accepted external-pin, frozen-byte-integrity and semantic/source-aware validation controls;
- defined an external `scaf_executable_governance_ci` trust-bundle contract that pins exactly six control-plane artifacts, including the CI gate itself;
- required the nested accepted external pin to use the same manifest/release-integrity-checker SHA-256 values as the top-level CI trust pins;
- added eight CI-gate regressions covering accepted three-stage execution/order, outside-repository trust input, control hash mismatch, nested-pin inconsistency, mutated validator identity, CLI override rejection, workflow trigger/trust-input boundary and full-SHA GitHub action pinning;
- added `.github/workflows/scaf-executable-governance.yml` as the first minimal trusted-main/manual CI executor;
- added `docs/executable-governance/09_SCAF_v0.0.4rc10_CI_Trust_Input_Model_and_Executable_Governance_Gate_Foundation.md`.

### CI Trust / Enforcement Position

- workflow trust input is supplied through external Actions secret `SCAF_CI_TRUST_BUNDLE_B64` and decoded only under `RUNNER_TEMP`;
- missing external trust input fails closed;
- workflow bootstraps `tools/scaf_ci_gate/gate.py` SHA-256 before executing repository gate code;
- gate verifies all six pinned control-plane artifacts before running any accepted control stage;
- stage order is fixed as external pin -> frozen baseline integrity -> authority-registry validation;
- stage failure stops progression and produces non-zero gate result;
- checkout credentials are not persisted and GitHub-maintained actions are pinned to reviewed full commit SHAs;
- rc10 workflow is deliberately limited to `push` on `main` and `workflow_dispatch`.

### Preserved / Deferred

- preserve accepted rc09 external-pin behavior and eleven regressions;
- preserve accepted rc07/rc08 release-integrity manifest/checker semantics and nine regressions;
- preserve accepted authority registry/schema/semantic validator and eight regressions;
- preserve frozen v0.0.2/v0.0.3 trees and 294 / 218 / 76 / twelve-Pattern inventories;
- do not claim fork-PR/`pull_request_target` enforcement, branch-protection configuration, workflow self-authentication, signing/PKI/provenance, canonical external trust-bundle distribution, generated views/indexes, registry generation, code generation, project inference, machine-readable L2→L3 relations, new L3, M3/M4 or L4.

## v0.0.4rc09 — 2026-08-17

Focused external-pin local pinned-artifact symlink hardening after the independent v0.0.4rc08 review returned **`V0.0.4 RELEASE-INTEGRITY DIAGNOSTIC-CLEANUP / EXTERNAL-PINNING FOUNDATION GATE: YES, AFTER MINOR CLEANUP`** and opened one Minor finding, `R8-01`.

### Fixed

- close `R8-01` by checking each fixed local pinned artifact's lexical repository path for symlink status before path resolution;
- preserve repository-root confinement after resolution and regular-file / SHA-256 verification after the lexical symlink check;
- ensure an in-repository same-byte symlink cannot satisfy the documented local pinned-artifact regular-file policy.

### Added

- add two end-to-end production CLI regressions, one for the canonical frozen-baseline manifest path and one for the release-integrity checker path, each requiring same-byte in-repository symlink replacement to return non-zero / `RESULT: FAIL`;
- extend the external-pin regression suite from 9 to 11 tests;
- add `docs/executable-governance/08_SCAF_v0.0.4rc09_External_Pin_Local_Artifact_Symlink_Hardening.md`.

### Preserved / Deferred

- preserve the rc08 external pin document contract, fixed artifact identities, SHA-256 algorithm and outside-repository pin-file rule;
- preserve the rc07 frozen-baseline manifest and release-integrity checker/test semantics unchanged;
- preserve the accepted authority registry/schema/semantic validator and frozen v0.0.2/v0.0.3 trees;
- do not add CI/merge enforcement, signing/PKI/provenance, canonical external-pin storage, generated views/indexes, registry generation, code generation, project inference, machine-readable L2→L3 relations, new L3 work, M3/M4 or L4.

## v0.0.4rc08 — 2026-08-17

Release-integrity diagnostic cleanup and external-pinning foundation after the independent v0.0.4rc07 review returned **`V0.0.4 FROZEN-BASELINE RELEASE-INTEGRITY FOUNDATION GATE: YES`**, with no Critical/Major/Minor findings and two non-blocking Trivial findings (`R7-01`, `R7-02`).

### Changed

- closed `R7-01` by making each protected-tree summary report `MISMATCH` whenever that tree has any integrity/structural error, including symlink-only failure, while preserving the existing overall fail-closed result;
- closed `R7-02` by completing the rc07 CHANGELOG enumeration of the eighth release-integrity regression category;
- extended the release-integrity regression suite from eight to nine tests with a symlink-summary diagnostic regression.

### Added

- added `tools/scaf_external_pin/checker.py` as a separate external-pin verification surface;
- defined an external JSON pin contract that pins exactly the canonical frozen-baseline manifest and release-integrity checker by SHA-256;
- required the trusted pin file to be outside the repository and to be a regular non-symlink file;
- added nine external-pin regressions covering accepted pin PASS, manifest-hash mismatch, checker-hash mismatch, duplicate/extra artifacts, in-repository pin rejection, external-pin symlink rejection, CWD/module-location binding, bad-pin CLI failure, and repository/artifact/hash-algorithm override rejection;
- added `docs/executable-governance/07_SCAF_v0.0.4rc08_Release_Integrity_Diagnostic_Cleanup_and_External_Pinning_Foundation.md`.

### Preserved / Deferred

- preserved the rc07 canonical manifest and frozen v0.0.2/v0.0.3 tree fingerprints;
- preserved the accepted authority registry/schema/semantic validator and all eight validator regressions;
- preserved semantic authority/project/L3 boundaries;
- did not add CI/merge enforcement, signing/PKI/provenance services, canonical external pin storage, generated views/indexes, registry generation, code generation, applicability inference, machine-readable L2→L3 relations, new L3 work, M3/M4 or L4.

## v0.0.4rc07 — 2026-08-17

Frozen-baseline release-integrity foundation after the independent v0.0.4rc06 review returned **`V0.0.4 CANONICAL-SCHEMA BINDING / VALIDATOR-CLI HARDENING GATE: YES`**, resolved `R5-01`, and opened no new finding.

### Added

- added `release-integrity/frozen-baseline-manifest.json` containing per-file SHA-256 values for exactly 11 frozen v0.0.2 normative files and 30 frozen v0.0.3 L3 files plus the accepted aggregate tree fingerprints;
- added `tools/scaf_release_integrity/checker.py` as a standalone fail-closed byte-integrity checker bound to the reviewed repository/module location and canonical manifest;
- added release-integrity usage/trust-boundary documentation;
- added eight regression tests for accepted state, byte mutation, file addition, file removal, manifest-hash corruption, manifest path escape, CWD/module-location binding, and production CLI override rejection;
- added `docs/executable-governance/06_SCAF_v0.0.4rc07_Frozen_Baseline_Release_Integrity_Foundation.md`.

### Validated

- canonical integrity checker passes with 2 protected trees / 41 protected files / 0 errors;
- `docs/normative/` aggregate remains `86ca06dbb586b8e0f47c8efbe731635633484bf58de2ddd3e90639a42090775f`;
- `docs/l3/` aggregate remains `eddb26826ce83d7a9aae028cf3c4f7f630b304c41e3bcbbfe8f00e51d3248eeb`;
- all eight release-integrity regressions pass.

### Preserved

- accepted 294-record `authority-registry.yaml`, canonical schema and semantic/source-aware validator foundation;
- accepted rc01–rc06 governance contracts except current navigation/release-state wording;
- frozen v0.0.2 and v0.0.3 source bytes and inventories;
- canonical Markdown semantic authority and project/L3 boundary semantics.

### Deliberately Not Added

- no CI enforcement or merge blocking;
- no manifest signing or external trust root;
- no registry/schema/validator freeze expansion;
- no registry generation, generated views/indexes or code generation;
- no project applicability inference or machine-readable L2→L3 relation vocabulary;
- no new L3 Pattern, M3/M4 or L4 work.

## v0.0.4rc06 — 2026-08-17

Focused canonical-schema binding and validator production-CLI hardening after the independent v0.0.4rc05 review returned **`V0.0.4 AUTHORITY-REGISTRY SCHEMA-VALIDATOR FOUNDATION GATE: YES, AFTER MINOR CLEANUP`** and opened one Minor finding, `R5-01`, against caller-selectable schema substitution.

### Changed

- removed production CLI `--schema` override so the normal PASS-producing path always uses repository canonical `schemas/authority-registry.schema.json`;
- removed production CLI `--repo-root` override so schema/source authority context is derived from the reviewed validator module's repository rather than a caller-selected repository root;
- retained optional `--registry <path>` only for choosing the representation under test while keeping canonical schema/source fixed;
- documented that alternate schema/repository injection remains function-level test API behavior rather than production CLI behavior;
- updated current repository/executable-governance navigation to rc06 and the focused `R5-01` closure gate.

### Added

- added an end-to-end CLI regression that mutates schema-owned `record_kind` and `relations`, verifies canonical-schema `RESULT: FAIL`, then verifies the former `--schema <lax-schema>` bypass is rejected as an unsupported production argument;
- added `docs/executable-governance/05_SCAF_v0.0.4rc06_Canonical_Schema_Binding_and_Validator_CLI_Hardening.md`.

### Preserved

- accepted `authority-registry.yaml` and all 294 rc03 records unchanged;
- accepted rc05 canonical JSON Schema unchanged;
- accepted authority-model / determinism / serialization / release-state / schema-validator contracts unchanged;
- frozen v0.0.2 normative content and 294 / 218 / 76 inventory;
- frozen v0.0.3 L3 content and twelve Available / M2 Pattern identities;
- canonical Markdown semantic precedence, project-state exclusion and empty initial relations.

### Deliberately Not Added

- no CI enforcement or merge blocking;
- no release-integrity/frozen-source byte authentication folded into the semantic validator;
- no registry generation, generated indexes/views or code generation;
- no automatic project applicability inference;
- no machine-readable L2→L3 relation vocabulary;
- no new L3 Pattern, SEC-primary realization, M3/M4 or L4 work.

### Gate

- verify `R5-01` is fully closed on the normal CLI surface;
- verify attempted alternate-schema CLI substitution cannot produce normal PASS;
- execute accepted-registry validation and the full regression suite;
- verify accepted registry/schema/contracts/frozen trees remain unchanged;
- return an explicit `V0.0.4 CANONICAL-SCHEMA BINDING / VALIDATOR-CLI HARDENING GATE` decision.

## v0.0.4rc05 — 2026-08-16

Authority-registry schema and structural/source-aware validator foundation after the independent v0.0.4rc04 review returned **`V0.0.4 AUTHORITY-REGISTRY RELEASE-STATE CLEANUP GATE: YES`**, resolved `R3-01`, and found no remaining blocker to the separately gated validation stage.

### Added

- added `schemas/authority-registry.schema.json` using JSON Schema Draft 2020-12 for the accepted rc03 ten-field / 294-record representation;
- added `tools/scaf_validator/validator.py` for YAML duplicate-key rejection, local schema validation, source-aware identity/coverage/path/anchor/Target fidelity checks, and fail-closed PASS/FAIL output;
- added `tools/scaf_validator/requirements.txt` with bounded PyYAML/jsonschema dependency ranges;
- added validator usage/boundary documentation;
- added eight regression tests covering the accepted registry plus duplicate ID, anchor mismatch, source-path mismatch, Target/class mismatch, non-empty relations and Pattern-identity contamination;
- added `docs/executable-governance/04_SCAF_v0.0.4rc05_Authority_Registry_Schema_and_Structural_Validator_Foundation.md`.

### Validated

- accepted registry passes with 294 records / 294 unique IDs / 294 canonical source IDs / 218 Project-Applicable Obligations / 76 Framework Normative Invariants / 0 errors;
- seven validator regression tests pass;
- source-aware validation uses canonical requirement headings rather than arbitrary textual ID occurrences;
- schema/validator remain subordinate to frozen normative Markdown semantic authority.

### Preserved

- `authority-registry.yaml` byte-for-byte from rc04/accepted rc03 serialization, including all 294 `representation_release = v0.0.4rc03` values;
- accepted authority-model, determinism-cleanup, serialization and release-state-cleanup contracts;
- frozen v0.0.2 L1/L2 normative content and 294 / 218 / 76 inventory;
- frozen v0.0.3 L3 content, twelve Pattern identities, lifecycle/maturity and trace semantics;
- empty initial `relations`, project-state exclusion and canonical Markdown precedence.

### Deliberately Not Added

- no CI enforcement or merge blocking;
- no registry generator or hybrid ownership;
- no generated reverse indexes/views;
- no code generation;
- no automatic project applicability inference;
- no machine-readable L2→L3 relation vocabulary;
- no new L3 Pattern, SEC-primary realization, M3/M4 or L4 work.

### Gate

- independently verify rc04→rc05 non-regression for registry/contracts/frozen trees;
- verify the schema is valid and expresses only the accepted ten-field representation contract;
- execute the validator and regression tests;
- verify fail-closed source-aware behavior and canonical Markdown precedence;
- return an explicit `V0.0.4 AUTHORITY-REGISTRY SCHEMA-VALIDATOR FOUNDATION GATE` decision.

## v0.0.4rc04 — 2026-08-16

Focused repository-state documentation cleanup after the independent v0.0.4rc03 serialization review returned **`V0.0.4 INITIAL AUTHORITY-REGISTRY SERIALIZATION GATE: YES, AFTER MINOR CLEANUP`**, accepted the 294-record registry population, and opened one Minor finding, `R3-01`, against stale current-state/navigation text in the root README.

### Changed

- updated root release identity to v0.0.4rc04 / Authority-Registry Release-State Documentation Cleanup RC;
- synchronized the root README repository file map with `authority-registry.yaml`, the rc03 serialization record, and the rc04 cleanup record;
- corrected CI / Automation Position to state that registry serialization is already accepted and schema/validator remain future scope;
- extended the release sequence through rc03 and current rc04;
- corrected Current Governance State so rc03 is the accepted serialization stage and rc04 is the focused `R3-01` cleanup stage;
- synchronized executable-governance navigation and current-gate text to the rc04 cleanup state;
- added `docs/executable-governance/03_SCAF_v0.0.4rc04_Authority_Registry_Release_State_Documentation_Cleanup.md`.

### Preserved

- `authority-registry.yaml` byte-for-byte from rc03, including all 294 `representation_release = v0.0.4rc03` values;
- accepted authority-model semantics and rc02 determinism closure;
- accepted rc03 serialization format, population and ownership contract;
- frozen v0.0.2 L1/L2 normative content and 294 / 218 / 76 inventory;
- frozen v0.0.3 L3 content, twelve Pattern identities, lifecycle/maturity and trace semantics;
- canonical Markdown precedence and project/L3 authority boundaries.

### Deliberately Not Added

- no schema or validator implementation;
- no test fixtures or regression-test framework;
- no generator or generated reverse indexes/views;
- no CI enforcement or code generation;
- no automatic applicability inference;
- no machine-readable L2→L3 relation vocabulary;
- no new L3 Pattern, SEC-primary realization, M3/M4 or L4 work.

### Gate

- independently verify `R3-01` is fully closed;
- verify root README current-state/navigation text is internally consistent with accepted rc03 serialization and current rc04 cleanup status;
- verify `authority-registry.yaml`, accepted authority-model/serialization contracts, `docs/normative/`, and `docs/l3/` are unchanged from rc03;
- return an explicit `V0.0.4 AUTHORITY-REGISTRY RELEASE-STATE CLEANUP GATE` decision.

## v0.0.4rc03 — 2026-08-16

Initial controlled serialization of the frozen v0.0.2 L1/L2 authority inventory after the independent v0.0.4rc02 review returned **`V0.0.4 AUTHORITY-MODEL DETERMINISM CLOSURE GATE: YES`**, resolved upstream `R1-01`, and found no remaining blocking issue.

### Added

- added repository-root `authority-registry.yaml` as the first machine-readable SCAF authority representation;
- serialized exactly 294 frozen L1/L2 normative requirement records;
- reproduced exactly 218 `Project-Applicable Obligation` and 76 `Framework Normative Invariant` source Target classifications;
- used exactly one record per frozen requirement ID and excluded all `SCAF-PAT-*` identities;
- populated the accepted deterministic values `record_kind = normative_requirement`, `layer = l1_l2_normative_authority`, `source_anchor = id`, `source_release = v0.0.2`, `representation_release = v0.0.4rc03`, `status = represented`, and empty `relations`;
- added `docs/executable-governance/02_SCAF_v0.0.4rc03_Initial_Authority_Registry_Serialization.md` to define the concrete YAML shape, controlled-curated ownership, audit reproducibility, completeness claim and review gate;
- synchronized current README and executable-governance navigation to the rc03 serialization stage.

### Preserved

- frozen normative Markdown as canonical semantic authority over the machine-readable registry;
- frozen v0.0.2 L1/L2 semantics, IDs, Target classes and 294 / 218 / 76 inventory;
- frozen v0.0.3 L3 Pattern bodies, twelve identities, `Available / M2` states, trace semantics and L3/L4 boundary;
- accepted rc02 deterministic authority-record semantics without adding per-record inferred layers or new status vocabulary;
- project Applicability / PDA / realization / verification / evidence / closure boundaries;
- initial `relations` as empty and non-semantic until a separately reviewed relation contract exists.

### Deliberately Not Added

- no schema or validator;
- no generator or hybrid registry ownership;
- no generated registry/reverse index;
- no CI enforcement or code generation;
- no automatic project applicability inference;
- no machine-readable L2→L3 relations;
- no new L3 Pattern, third tranche, SEC-primary realization, M3/M4 or L4 work.

### Gate

- independently verify YAML parseability and exact rc03 record shape;
- verify 294 / 294 unique IDs and exact 218 / 76 source classification reproduction;
- verify every record resolves through `source_path` + `source_anchor == id` to exactly one canonical source requirement block;
- verify all deterministic constants and empty `relations` values;
- verify there are no `SCAF-PAT-*` records and no project-owned state fields;
- verify rc02→rc03 frozen `docs/normative/` and `docs/l3/` byte/hash non-regression;
- return an explicit `V0.0.4 INITIAL AUTHORITY-REGISTRY SERIALIZATION GATE` decision.

## v0.0.4rc02 — 2026-08-16

Focused authority-model determinism cleanup after the independent v0.0.4rc01 review returned **PASS CONDITIONALLY / `V0.0.4 AUTHORITY-MODEL FOUNDATION GATE: YES, AFTER MINOR CLEANUP`** with 0 Critical, 0 Major, 1 Minor (`R1-01`) and 0 Trivial findings.

### Changed

- closed `R1-01` by fixing the initial `layer` semantic value to exactly `l1_l2_normative_authority`;
- prohibited serializer inference of per-record `L1`/`L2` classification where the frozen source does not provide such a record-level classification;
- fixed initial `source_anchor` to exactly the authority `id` and defined canonical resolution as exactly one matching requirement heading/block inside `source_path`;
- explicitly rejected renderer-generated Markdown slugs, line numbers and generated-index positions as canonical authority anchors;
- fixed the only initial record `status` value to exactly `represented`, with representation-only meaning and no source/project lifecycle, applicability, compliance, verification, closure, maturity, availability or Pattern-selection semantics;
- made the initial `relations` population rule explicitly empty/omitted unless a separately reviewed relation contract exists;
- added `docs/executable-governance/01_SCAF_v0.0.4rc02_Authority_Model_Determinism_Cleanup.md`;
- synchronized current README and executable-governance navigation/gate wording to rc02.

### Preserved

- frozen v0.0.2 L1/L2 normative semantics, identities and 294 / 218 / 76 inventory;
- frozen v0.0.3 L3 Pattern bodies, twelve identities, `Available / M2` states, trace semantics and L3/L4 boundary;
- frozen normative Markdown as canonical semantic authority;
- exactly two initial authority classes;
- project Applicability / PDA / realization / verification / evidence / closure boundaries;
- exclusion of all `SCAF-PAT-*` identities from the initial normative authority-record population.

### Deliberately Not Added

- no 294-record `authority-registry.yaml` or equivalent serialization;
- no schema or validator;
- no generated registry/reverse index;
- no CI enforcement or code generation;
- no automatic applicability inference;
- no new L3 Pattern, third tranche, SEC-primary realization, M3/M4 or L4 work.

### Gate

- independently verify `R1-01` is fully closed;
- verify all three mandatory-field semantics are deterministic and non-authority-expanding;
- verify initial `relations` remain empty/omitted;
- verify rc01→rc02 frozen-upstream non-regression;
- verify no registry/schema/validator/CI/codegen or catalog-expansion scope was pulled into rc02;
- return an explicit `V0.0.4 AUTHORITY-MODEL DETERMINISM CLOSURE GATE` decision.

## v0.0.4rc01 — 2026-08-16

First post-v0.0.3 executable-governance development RC. This release defines the semantic authority model that must be reviewed before any machine-readable authority registry, schema, validator or CI enforcement is introduced.

### Added

- added `docs/executable-governance/README.md` as the controlled development scope/order/gate entry point;
- added `docs/executable-governance/00_SCAF_Machine_Readable_Authority_Model.md`;
- defined canonical-source precedence: frozen normative Markdown remains semantic authority and a machine-readable representation cannot override it;
- bounded the initial future registry population to the frozen v0.0.2 inventory of 294 requirement IDs / 218 Project-Applicable Obligations / 76 Framework Normative Invariants;
- defined stable record identity, initial authority classes, minimum semantic fields, representation lifecycle/staleness behavior, completeness criteria and fail-closed authority-resolution expectations;
- explicitly separated project-owned applicability/PDA/realization/verification/evidence/closure state from the framework authority registry;
- explicitly kept the twelve frozen v0.0.3 `SCAF-PAT-*` identities outside the initial normative authority-record population.

### Preserved

- frozen v0.0.2 L1/L2 normative semantics and 294 stable requirement identities;
- frozen v0.0.3 L3 catalog semantics, twelve Pattern identities, `Available / M2` states, trace relations and L3/L4 boundary;
- human semantic authority before executable representation;
- project Design Authority / Verification Authority / closure boundaries.

### Deliberately Not Added

- no `authority-registry.yaml` or other registry serialization;
- no JSON Schema or alternate schema language;
- no validator implementation or test fixture;
- no generated registry/reverse index;
- no CI enforcement or code generation;
- no automatic project applicability inference;
- no third-tranche Pattern, SEC-primary realization, M3/M4 or L4 expansion.

### Gate

- independently verify the new authority model does not create a competing normative authority source;
- verify the initial 294-record population boundary and 218/76 Target-class preservation are consistent with the frozen v0.0.2 baseline;
- verify project application/PDA/realization/verification/evidence/closure state remains outside the framework registry;
- verify L3 Pattern identities are not promoted into normative authority records;
- verify identity, completeness, conflict/staleness and fail-closed semantics are precise enough for a later serialization RC;
- return an explicit `V0.0.4 AUTHORITY-MODEL FOUNDATION GATE` decision without implementing the registry/schema/validator.

## v0.0.3 — 2026-08-16

Frozen L3 Pattern / Mechanism Catalog Baseline.

This release is created by explicit governance freeze decision after the independent `v0.0.3rc14` final-navigation closure review returned **`L3 V0.0.3 FREEZE-CANDIDATE CLOSURE GATE: YES`**, recorded upstream finding `R12-01` as **RESOLVED**, opened no Critical, Major, Minor or Trivial finding, confirmed the frozen v0.0.2 baseline, verified exactly twelve published Pattern identities, reproduced 12 / 12 rc13→rc14 Pattern-body non-regression checks, preserved the `FTL-001` trace closure, and found no separately gated scope expansion.

### Frozen

- L3 catalog-governance semantics;
- L3 Pattern metadata contract;
- L3 trace and project-selection semantics;
- twelve published Pattern identities;
- twelve `Available / M2 — Architecture Reviewed` lifecycle states;
- initial-seven `Introduced In v0.0.3rc03` history;
- second-five `Introduced In v0.0.3rc08` history;
- immutable primary-family identity and `Supersedes: None` state;
- reviewed Pattern architecture/trace/authority/L3-L4 boundaries.

### Semantic Change from v0.0.3rc14

- **None intended.**
- The freeze action changes release/freeze state and current release metadata only.
- Pattern bodies and trace relations remain semantically unchanged from the independently reviewed rc14 tree.
- The frozen v0.0.2 normative tree remains byte-stable at 294 / 218 / 76.

### Added

- `docs/l3/14_L3_v0.0.3_Freeze_Decision.md` as the formal freeze record.

### Not Included / Still Separately Gated

- third-tranche catalog expansion;
- deferred EVD export/transformation authoring;
- rejected/reframe PST configuration-activation authoring;
- SEC-primary realization;
- M3/M4;
- L4 implementation/verification guidance;
- schema, validator, generated registry/reverse index, CI, code generation or executable governance.

### Governance

- `v0.0.3` is frozen and shall not be modified in place.
- Later semantic work must continue on a new controlled RC development line.

## v0.0.3rc14 — 2026-08-16

Final freeze-candidate navigation cleanup after the independent v0.0.3rc13 focused closure review returned **`L3 V0.0.3 FREEZE-CANDIDATE CLOSURE GATE: YES, AFTER MINOR CLEANUP`**. The review confirmed the architecture/trace/lifecycle baseline, frozen normative integrity, 12 / 12 Pattern-body non-regression, `FTL-001` trace closure, and scope control; it opened no new/regression finding. The sole remaining residue of upstream `R12-01` was one stale active `Immediate Gate` paragraph in `docs/l3/03_L3_Pattern_Index.md`.

### Changed

- updated `docs/l3/03_L3_Pattern_Index.md` `## 5. Immediate Gate` from the stale rc12 review position to the rc14 final-navigation closure position;
- synchronized current release/navigation wording to v0.0.3rc14;
- added this rc14 release record as the final cleanup RC before any explicit freeze decision.

### Preserved

- exactly twelve published numeric `SCAF-PAT-*` identities;
- all twelve as `Available / M2 — Architecture Reviewed`;
- initial-seven `Introduced In: v0.0.3rc03`;
- second-five `Introduced In: v0.0.3rc08`;
- all immutable primary families, `Supersedes: None`, Pattern bodies and trace relations apart from current Development Release metadata;
- the rc09 `FTL-001` `SCAF-ROB-007` Constraint Input / `SCAF-ROB-015` Supporting closure;
- frozen v0.0.2 normative content and all 294 IDs / 218 Project-Applicable Obligations / 76 Framework Normative Invariants;
- many-to-many L2→L3 trace, bounded `Available` semantics, PDA/source-authority ownership and L3/L4 separation.

### Deliberately Not Added / Promoted

- v0.0.3 is **not frozen by rc14**;
- no thirteenth Pattern ID or third tranche;
- no deferred EVD Pattern, revived rejected/reframe PST Pattern or SEC-primary Pattern;
- no M3/M4, L4, schema, validator, generated registry/reverse index, CI, code generation or executable governance.

### Gate

- independently verify upstream `R12-01` is fully resolved;
- verify no stale active rc12/rc13 immediate-gate text remains in current navigation surfaces;
- verify rc13→rc14 12 / 12 Pattern-body non-regression with only Development Release metadata changes;
- verify the frozen v0.0.2 baseline remains byte-stable;
- return an explicit `L3 V0.0.3 FREEZE-CANDIDATE CLOSURE GATE` decision without performing the freeze.

## v0.0.3rc13 — 2026-08-16

Focused freeze-candidate release-record cleanup after the independent v0.0.3rc12 review returned **`FREEZE CANDIDATE NEEDS MINOR CLEANUP` / `L3 V0.0.3 FREEZE-CANDIDATE GATE: YES, AFTER MINOR CLEANUP`** with 0 Critical, 0 Major, 1 Minor (`R12-01`) and 0 Trivial findings.

### Changed

- updated root README current release/gate wording from the stale rc11 availability-acceptance position to the rc13 freeze-candidate closure position;
- added rc12 and rc13 to the root README current sequence;
- replaced stale `No CI is included in v0.0.3rc09` wording with release-stable `No CI is included in the v0.0.3 L3 baseline`;
- replaced `v0.0.3rc06 intentionally does not define:` in the living L3 metadata contract with `The v0.0.3 L3 baseline intentionally does not define:`;
- added `docs/l3/12_L3_v0.0.3_Freeze_Candidate_Release_Record_Cleanup.md`;
- synchronized current L3 README, governance, index and catalog navigation wording to the rc13 focused closure gate;
- corrected the rc12 CHANGELOG cleanup claim so the historical release record reflects the actual rc12 reviewed tree.

### Preserved

- exactly twelve published numeric `SCAF-PAT-*` identities;
- all twelve as `Available / M2 — Architecture Reviewed`;
- initial-seven `Introduced In: v0.0.3rc03`;
- second-five `Introduced In: v0.0.3rc08`;
- all immutable primary families, `Supersedes: None`, Pattern bodies and trace relations apart from current Development Release metadata;
- the rc09 `FTL-001` `SCAF-ROB-007` Constraint Input / `SCAF-ROB-015` Supporting closure;
- frozen v0.0.2 normative content and all 294 IDs / 218 Project-Applicable Obligations / 76 Framework Normative Invariants;
- many-to-many L2→L3 trace, bounded `Available` semantics, PDA/source-authority ownership and L3/L4 separation.

### Deliberately Not Added / Promoted

- v0.0.3 is **not frozen by rc13**;
- no thirteenth Pattern ID or third tranche;
- no deferred EVD Pattern, revived rejected/reframe PST Pattern or SEC-primary Pattern;
- no M3/M4, L4, schema, validator, generated registry/reverse index, CI, code generation or executable governance.

### Gate

- independently verify `R12-01` is fully resolved;
- verify root README, L3 navigation/contract surfaces and CHANGELOG tell one coherent rc13 freeze-candidate closure story;
- verify rc12→rc13 12 / 12 Pattern-body non-regression with only Development Release metadata changes;
- verify the frozen v0.0.2 baseline remains byte-stable;
- return an explicit `L3 V0.0.3 FREEZE-CANDIDATE CLOSURE GATE` decision without performing the freeze.

## v0.0.3rc12 — 2026-08-16

L3 milestone consolidation / freeze-candidate audit preparation after the independent v0.0.3rc11 availability-acceptance review returned **PASS / `L3 SECOND-TRANCHE PATTERN-AVAILABILITY ACCEPTANCE GATE: YES`**, confirmed all twelve entries as `Available / M2`, reproduced 12 / 12 Pattern-body non-regression hashes, preserved the frozen v0.0.2 baseline and opened no Critical, Major, Minor or Trivial finding.

### Added

- added `docs/l3/11_L3_v0.0.3_Milestone_Consolidation_and_Freeze_Candidate.md`;
- consolidated the complete v0.0.3 L3 review/lifecycle evidence from rc01 through rc11;
- defined explicit freeze-candidate criteria covering frozen-upstream integrity, twelve-ID stability, lifecycle semantics, Pattern-body non-regression, contract coherence, finding closure, authority preservation, bounded deferral and release-record consistency;
- defined the proposed v0.0.3 L3 frozen scope if a later explicit freeze decision is made.

### Changed

- updated current release/navigation/gate metadata to v0.0.3rc12;
- updated release-facing freeze-candidate wording and identified the remaining stale point-release metadata-contract wording for cleanup before freeze.
- normalized historical second-tranche decision-record `Development Release` labels so `07` / `08` / `09` / `10` identify their actual originating releases rc08 / rc09 / rc10 / rc11 instead of inheriting the current development release.

### Preserved

- exactly twelve published numeric `SCAF-PAT-*` identities;
- all twelve as `Available / M2 — Architecture Reviewed`;
- initial-seven `Introduced In: v0.0.3rc03` history;
- second-five `Introduced In: v0.0.3rc08` history;
- all immutable primary families and `Supersedes: None`;
- all Pattern architecture/trace bodies apart from current Development Release metadata;
- the rc09 `FTL-001` `SCAF-ROB-007` Constraint Input / `SCAF-ROB-015` Supporting closure;
- frozen v0.0.2 normative content and all 294 IDs / 218 Project-Applicable Obligations / 76 Framework Normative Invariants;
- many-to-many L2→L3 trace, PDA/source-authority, `Available` semantics and L3/L4 boundaries.

### Deliberately Not Added / Promoted

- v0.0.3 is **not frozen by rc12**;
- no thirteenth Pattern ID or third tranche;
- no deferred EVD Pattern;
- no revived rejected/reframe PST Pattern;
- no SEC-primary Pattern;
- no M3/M4, L4, schema, validator, generated registry/reverse index, CI, code generation or executable governance.

### Gate

- independently verify the complete v0.0.3 L3 milestone as a bounded freeze candidate;
- verify rc11→rc12 12 / 12 Pattern-body non-regression with only Development Release metadata changes;
- verify all review findings are closed and all release records are mutually consistent;
- determine whether deferred work is cleanly isolated future scope rather than an unresolved v0.0.3 baseline defect;
- return an explicit `L3 V0.0.3 FREEZE-CANDIDATE GATE` decision without performing the freeze.

## v0.0.3rc11 — 2026-08-16

Second-tranche catalog availability acceptance after the independent v0.0.3rc10 maturity / availability review returned **PASS / `L3 SECOND-TRANCHE PATTERN-LIFECYCLE GATE: YES`**, validated **5 / 5 `M2 VALID`**, judged **5 / 5 `READY FOR AVAILABLE`**, confirmed **12 / 12 Pattern-body non-regression PASS**, and opened no new Critical, Major, Minor or Trivial finding.

### Changed

- explicitly promoted `SCAF-PAT-FTL-001`, `SCAF-PAT-FTL-002`, `SCAF-PAT-TIM-001`, `SCAF-PAT-TIM-002`, and `SCAF-PAT-SYN-001` from `Catalog Status: Candidate` to `Catalog Status: Available`;
- retained `M2 — Architecture Reviewed` for all five; no M3/M4 maturity claim is made;
- retained each second-tranche Pattern ID, immutable primary family and `Introduced In: v0.0.3rc08` value;
- added `docs/l3/10_L3_Second_Tranche_Availability_Acceptance.md` as the release-scoped explicit catalog acceptance record;
- updated current README, L3 navigation/index, governance gate and Pattern release/status metadata for v0.0.3rc11.

### Availability Evidence Basis

- rc10 independently validated all five M2 states;
- rc10 independently judged all five entries `READY FOR AVAILABLE`;
- rc10 verified 12 / 12 controlled Pattern-body normalized hashes;
- rc10 opened no cleanup finding and preserved the rc09 `FTL-001` trace closure;
- the rc10 review performed no automatic Catalog Status transition, preserving the requirement for this later explicit repository lifecycle decision.

### Preserved

- all twelve published Pattern IDs and immutable primary families;
- the initial seven `Available / M2 / Introduced In: v0.0.3rc03` states;
- the second five `M2 — Architecture Reviewed / Introduced In: v0.0.3rc08` states;
- all Pattern architecture/trace bodies apart from current Development Release and the five intended Catalog Status metadata transitions;
- exactly twelve numeric `SCAF-PAT-*` identities and no `Supersedes` event;
- frozen v0.0.2 `docs/normative/` content and all 294 normative IDs / 218 Project-Applicable Obligations / 76 Framework Normative Invariants;
- many-to-many L2→L3 trace, PDA/source-authority and L3/L4 boundaries.

### Deliberately Not Added / Promoted

- no thirteenth Pattern ID or third tranche;
- no M3/M4 promotion;
- no deferred EVD export/transformation Pattern;
- no revived rejected/reframe PST configuration-activation Pattern;
- no SEC-primary Pattern;
- no L4, schema, validator, generated registry/reverse index, CI, code generation or executable governance.

### Gate

- independently verify all five rc10 readiness recommendations support the rc11 acceptance transitions;
- verify the transition is lifecycle-only with no mechanism/trace rewrite;
- verify all twelve IDs/families/history and frozen v0.0.2 baseline remain stable;
- verify `Available` retains its bounded catalog meaning and does not become project selection/compliance/satisfaction authority.

## v0.0.3rc10 — 2026-08-16

Second-tranche lifecycle decision after the independent v0.0.3rc09 focused review returned **PASS / `L3 SECOND-TRANCHE TRACE-CLOSURE GATE: YES`**, confirmed `R8-01` Resolved and found no new Critical, Major, Minor or Trivial finding.

### Changed

- added `docs/l3/09_L3_Second_Tranche_Lifecycle_Decision.md` as the release-scoped second-tranche maturity decision record;
- advanced `SCAF-PAT-FTL-001`, `SCAF-PAT-FTL-002`, `SCAF-PAT-TIM-001`, `SCAF-PAT-TIM-002`, and `SCAF-PAT-SYN-001` from `M1 — Structured` to `M2 — Architecture Reviewed`;
- retained `Catalog Status: Candidate` for all five so maturity and availability remain independent lifecycle axes;
- updated current release/navigation/gate wording for v0.0.3rc10.

### Evidence Basis

- rc08 independently reviewed all five second-tranche entries for family/mechanism fit, L2 trace, authority boundaries, non-duplication, PDA ownership and L3/L4 conformance;
- rc09 corrected the sole Minor `R8-01` in `FTL-001` and its focused review confirmed the finding fully Resolved with no regression;
- the frozen v0.0.2 baseline and twelve published Pattern identities remain stable.

### Preserved

- all five second-tranche IDs, immutable primary families, `Candidate` status and `Introduced In: v0.0.3rc08`;
- all seven initial-tranche `Available / M2 / Introduced In v0.0.3rc03` states;
- all Pattern architecture/trace bodies except current Development Release and the five intended Maturity metadata changes;
- exactly twelve numeric `SCAF-PAT-*` identities and no `Supersedes` event;
- frozen v0.0.2 `docs/normative/` content and all 294 normative IDs / 218 Project-Applicable Obligations / 76 Framework Normative Invariants;
- many-to-many trace, PDA/source-authority and L3/L4 boundaries.

### Deliberately Not Added / Promoted

- no `Candidate`→`Available` transition for the five second-tranche entries;
- no deferred EVD export/transformation Pattern;
- no revived PST configuration-activation Pattern;
- no SEC-primary Pattern;
- no third tranche, M3/M4, L4, schema, validator, generated registry/index, CI, code generation or executable governance.

### Gate

- independently validate M2 for each of the five second-tranche entries;
- independently assess `READY FOR AVAILABLE` entry by entry without changing status;
- reconfirm `FTL-001` `ROB-007` Constraint Input closure, twelve-ID inventory, initial-seven non-regression and frozen-baseline integrity.

## v0.0.3rc09 — 2026-08-16

Focused second-tranche trace cleanup after the independent v0.0.3rc08 Pattern review returned **PASS WITH MINOR CLEANUP / `L3 SECOND-TRANCHE PATTERN GATE: YES, AFTER MINOR CLEANUP`**, with **0 Critical, 0 Major and 1 Minor** finding.

### Changed

- added `docs/l3/08_L3_Second_Tranche_Trace_Cleanup.md` as the release-scoped `R8-01` closure record;
- corrected `SCAF-PAT-FTL-001` by moving `SCAF-ROB-007` from `Supporting L2 Trace` to `Constraint Inputs`;
- revised `FTL-001` detailed trace rationale so the project-identified material failure-propagation path is explicitly consumed as an upstream constraint on containment placement/configuration rather than represented as FTL-owned realization;
- retained `SCAF-ROB-015` as the Supporting Realization identified by the rc08 review;
- updated current release/gate/navigation metadata for v0.0.3rc09.

### Preserved

- `SCAF-PAT-FTL-001` ID, immutable `FTL` primary family, Candidate/M1 lifecycle state and `Introduced In: v0.0.3rc08`;
- the other four second-tranche Pattern architecture/trace bodies unchanged except current Development Release metadata;
- the initial seven Pattern architecture/trace bodies and `Available / M2` lifecycle states unchanged except current Development Release metadata;
- exactly twelve numeric `SCAF-PAT-*` identities; no thirteenth identity or `Supersedes` event;
- frozen v0.0.2 `docs/normative/` content and all 294 normative IDs / 218 Project-Applicable Obligations / 76 Framework Normative Invariants;
- many-to-many L2→L3 trace semantics, PDA/source-authority boundaries and the L3/L4 boundary.

### Deliberately Not Added / Promoted

- no M2 or `Available` promotion for the five second-tranche entries;
- no authoring of the deferred EVD export/transformation category;
- no Pattern ID for the rejected/reframe PST configuration-activation proposal;
- no SEC-primary Pattern;
- no third tranche, M3/M4, L4, schema, validator, generated registry/index, CI, code generation or executable governance.

### Gate

- independently verify `R8-01` is Resolved and `SCAF-ROB-007` is now a Constraint Input in `FTL-001`;
- verify `SCAF-ROB-015` remains Supporting Realization and `FTL-001` identity/lifecycle/family remain stable;
- verify the other eleven Pattern architecture bodies are non-regressed except Development Release metadata;
- reconfirm frozen v0.0.2 byte stability and the 294 / 218 / 76 inventory;
- do not auto-promote or open additional catalog scope from this cleanup RC alone.

## v0.0.3rc08 — 2026-08-16

Controlled second representative L3 Pattern tranche after the independent v0.0.3rc07 coverage / second-tranche planning review returned **PASS / `L3 SECOND-TRANCHE PLANNING GATE: YES`**, approved six later-authoring categories, rejected/reframed the PST configuration-activation proposal, preserved the SEC-primary hold, and opened no Critical, Major, Minor or Trivial release finding.

### Added

- added `docs/l3/07_L3_Second_Tranche_Authoring_Decision.md` recording the rc07 category dispositions and the deliberately limited rc08 authoring scope;
- published five new permanent Pattern identities as `Candidate / M1` entries:
  - `SCAF-PAT-FTL-001` — Failure-Domain Containment / Isolation;
  - `SCAF-PAT-FTL-002` — Controlled Failover with Graceful Degradation;
  - `SCAF-PAT-TIM-001` — Bounded Queue / Backpressure / Overload Protection;
  - `SCAF-PAT-TIM-002` — Timebase / Clock-Relationship / Epoch Validity;
  - `SCAF-PAT-SYN-001` — Generation/Epoch-Based Cross-Participant State Convergence;
- opened the previously empty `FTL`, `TIM` and `SYN` mechanism families with structured architecture-level entries;
- added explicit cross-family composition/boundary statements for FTL containment versus failover, TIM capacity versus ROB/INT authority, and SYN convergence versus existing COM reconnect semantics.

### Preserved

- the initial seven published Pattern identities as `Available / M2`, all still `Introduced In: v0.0.3rc03`;
- initial seven Pattern architecture/trace content unchanged except current Development Release metadata;
- frozen v0.0.2 `docs/normative/` content and all 294 normative IDs / 218 Project-Applicable Obligations / 76 Framework Normative Invariants;
- many-to-many L2→L3 trace semantics and the prohibition on generic L2→L3 `satisfies` shortcuts;
- Project Design Authority ownership of project mechanism selection/configuration and external source-authority ownership;
- L3/L4 boundary and separate later gates.

### Deliberately Deferred / Rejected

- the rc07-approved Evidence Retrieval / Export / Transformation Integrity (`EVD`) category is deferred to keep rc08 focused on the new FTL/TIM/SYN family stress test;
- no ID is allocated for Controlled Configuration Activation / Source Precedence (`PST`), which remains `REJECT / REFRAME` pending a stable principal mechanism/family basis;
- no SEC-primary Pattern is authored before the dedicated security-realization gate;
- no new Pattern is promoted beyond Candidate/M1;
- no M3/M4, L4, schema, validator, generated registry/index, CI, code generation or executable governance is introduced.

### Gate

- independently review all five new Candidate/M1 Patterns for family fit, trace classification, PDA/source-authority preservation, non-duplication, composition and L3/L4 conformance;
- verify `FTL-001` does not redefine ARCH Domains and `FTL-002` remains distinct from containment/retry/universal redundancy;
- verify TIM entries preserve TIME-owned measurable semantics while INT/ROB/RUN retain their downstream authorities;
- verify `SYN-001` complements rather than reclassifies/duplicates `SCAF-PAT-COM-001` and does not prescribe consensus/leader algorithms;
- reconfirm the initial seven Available/M2 entries and frozen v0.0.2 baseline are non-regressed;
- do not auto-promote the five new entries or open the deferred/rejected/security/L4/executable-governance scopes from this authoring RC alone.
## v0.0.3rc07 — 2026-08-16

L3 catalog trace-reference coverage and second-tranche planning after the independent v0.0.3rc06 availability-acceptance review returned **PASS / `INITIAL L3 PATTERN-AVAILABILITY ACCEPTANCE GATE: YES`**, validated **7 / 7 `AVAILABLE ACCEPTANCE VALID`**, confirmed **7 / 7 pattern-body non-regression**, and opened no Critical, Major, Minor or Trivial finding.

### Added

- added `docs/l3/06_L3_Catalog_Coverage_and_Second_Tranche_Planning.md` as a descriptive, human-readable coverage and expansion-planning artifact;
- established **trace-reference coverage** semantics that explicitly do not mean project applicability, compliance, obligation satisfaction or catalog completeness;
- recorded the current seven-pattern explicit trace surface: 60 distinct frozen Project-Applicable Obligations; two additional Framework Invariants appear only as provenance/mechanism-boundary references and are excluded from trace-coverage counts;
- added concern-level coverage counts and interpretations that distinguish expected low pattern coverage in AK/CTX/ARCH/RUN from actual reusable mechanism opportunities;
- added a controlled second-tranche prioritization model based on mechanism reuse, L2 leverage, taxonomy stress value, cross-concern value, technology neutrality, non-duplication and reviewability;
- proposed seven planning-only candidate categories across FTL, TIM, SYN, EVD and PST without allocating any Pattern ID;
- retained SEC realization behind a separate security-specific abstraction/review gate.

### Preserved

- exactly seven published Pattern IDs, all `Available / M2` and all introduced in v0.0.3rc03;
- existing Pattern mechanism bodies, L2 trace relations, immutable primary families and lifecycle states;
- frozen v0.0.2 `docs/normative/` content and all 294 normative IDs / 218 Project-Applicable Obligations / 76 Framework Normative Invariants;
- many-to-many L2→L3 trace semantics and the prohibition on generic L2→L3 `satisfies` shortcuts;
- Project Design Authority ownership of actual mechanism selection/configuration;
- L3/L4 boundary and later gates on M3/M4, L4 and executable governance.

### Deliberately Not Added / Promoted

- no eighth Pattern ID or second-tranche Pattern entry;
- no change to `Available / M2` lifecycle state of the initial seven patterns;
- no M3/M4 maturity claim;
- no SEC Pattern entry;
- no L4 implementation/verification guidance;
- no schema, validator, generated registry/index, CI, code generation or executable-governance machinery.

### Gate

- independently review whether trace-reference coverage is represented correctly and cannot be confused with satisfaction/compliance/completeness;
- verify concern-level low coverage is not automatically treated as a catalog defect;
- review each proposed second-tranche category for reusable mechanism intent, family fit, non-duplication and L3/L4 safety;
- decide which candidate categories, if any, may receive Pattern IDs in the next RC;
- keep security realization, M3/M4, L4 and executable-governance work separately gated.

# Changelog

## v0.0.3rc06 — 2026-08-16

Initial L3 pattern-tranche availability acceptance after the independent v0.0.3rc05 maturity / availability review returned **PASS / `INITIAL L3 PATTERN-LIFECYCLE GATE: YES`**, validated **7 / 7 `M2 VALID`**, judged **7 / 7 `READY FOR AVAILABLE`**, and opened no new Critical, Major, Minor or Trivial finding.

### Changed

- explicitly promoted all seven published initial-tranche entries from `Catalog Status: Candidate` to `Catalog Status: Available`;
- retained `M2 — Architecture Reviewed` for all seven entries; no M3/M4 maturity claim is made;
- retained every published Pattern ID, immutable primary family and `Introduced In: v0.0.3rc03` value;
- added `docs/l3/05_L3_Initial_Tranche_Availability_Acceptance.md` as the release-scoped catalog acceptance record;
- updated current README, L3 navigation/index, governance gate and pattern release/status metadata for v0.0.3rc06;
- kept Pattern architecture bodies, L2 trace semantics, PDA decisions, external-authority boundaries and L3/L4 boundaries unchanged apart from release/status lifecycle metadata.

### Availability Evidence Basis

- the rc05 independent review verified exact archive identity and frozen-baseline byte stability;
- all seven entries were independently assessed `M2 VALID`;
- all seven entries were independently assessed `READY FOR AVAILABLE`;
- no Critical/Major/Minor/Trivial cleanup item remained before explicit catalog acceptance;
- the review performed no automatic status transition, preserving the requirement for a later explicit repository lifecycle decision now recorded by rc06.

### Preserved

- exactly seven published Pattern IDs; no eighth identity;
- `M2 — Architecture Reviewed` for every entry;
- `Introduced In: v0.0.3rc03` for every entry;
- immutable primary families and `Supersedes: None` lifecycle state;
- frozen v0.0.2 `docs/normative/` content and all 294 normative IDs / 218 Project-Applicable Obligations / 76 Framework Normative Invariants;
- many-to-many L2→L3 trace semantics and the prohibition on generic L2→L3 `satisfies` shortcuts;
- Project Design Authority ownership of project mechanism selection/configuration and external source-authority ownership of external constraints;
- L3/L4 boundary and gates on schema, validator, CI, code generation and executable governance.

### Deliberately Not Added / Promoted

- no second pattern tranche or eighth Pattern ID;
- no M3/M4 maturity claim;
- no primary-family move, Pattern-ID replacement or `Supersedes` event;
- no L4 implementation / verification guidance;
- no schema, validator, generated registry/index, CI, code generation or executable-governance machinery.

### Gate

- independently confirm that the rc06 Candidate→Available transitions are supported by the rc05 entry-by-entry readiness evidence;
- confirm all seven identities remain Available/M2 with unchanged family and introduction history;
- confirm pattern architecture/trace content did not change to obtain availability;
- reconfirm frozen v0.0.2 integrity and accepted catalog-lifecycle semantics;
- only after a successful rc06 review may the initial seven-pattern availability milestone be considered closed; second-tranche, M3, L4 and executable-governance work remain separate decisions.

## v0.0.3rc05 — 2026-08-16

Initial L3 pattern-tranche maturity decision after the independent v0.0.3rc04 trace-closure review returned **PASS / `INITIAL L3 PATTERN-TRANCHE TRACE-CLOSURE GATE: YES`**, with `R3-01` through `R3-04` fully Resolved and no new Critical, Major, Minor or Trivial finding.

### Changed

- advanced all seven published initial-tranche patterns from `M1 — Structured` to `M2 — Architecture Reviewed`;
- retained `Catalog Status: Candidate` for all seven entries so maturity and catalog availability remain independent lifecycle axes;
- added a release-scoped initial-tranche lifecycle decision record documenting the M2 evidence basis and the separate `Available` acceptance gate;
- clarified catalog governance so M2 promotion requires completed independent architecture review/closure of material authority, trace and L3/L4 findings;
- clarified that Candidate→Available is a separate explicit catalog acceptance decision and does not follow automatically from M2;
- advanced current L3 development labels and release/gate wording to v0.0.3rc05.

### M2 Evidence Basis

- v0.0.3rc03 independently reviewed all seven entries for authority boundary, L2 trace, primary-family placement, PDA/external-authority separation and L3/L4 conformance;
- v0.0.3rc04 closed all four localized Minor trace findings from that review;
- the rc04 focused closure review confirmed all four findings Resolved and found no new Critical/Major/Minor/Trivial regression;
- the seven IDs, immutable primary families, index counts and frozen v0.0.2 baseline remain stable.

### Preserved

- the same seven published Pattern IDs and immutable primary families introduced in v0.0.3rc03;
- `Catalog Status: Candidate` for every current pattern;
- `Introduced In: v0.0.3rc03` for all seven identities;
- frozen v0.0.2 `docs/normative/` content and all 294 normative IDs / 218 Project-Applicable Obligations / 76 Framework Normative Invariants;
- many-to-many L2→L3 trace semantics and the prohibition on generic L2→L3 `satisfies` shortcuts;
- Project Design Authority ownership of project mechanism selection/configuration and external source-authority ownership of external constraints;
- L3/L4 boundary and gates on schema, validator, CI, code generation and executable governance.

### Deliberately Not Added / Promoted

- no Candidate→Available transition in this RC;
- no eighth Pattern ID, second tranche, primary-family move, `Supersedes` event or Pattern-ID replacement;
- no M3/M4 maturity claim;
- no L4 implementation / verification guidance;
- no schema, validator, CI or executable-governance machinery.

### Gate

- independently verify the M2 evidence basis for each of the seven entries;
- assess Candidate→Available readiness entry by entry using the catalog lifecycle criteria, without auto-promoting any entry;
- reconfirm Pattern identity/family, frozen-baseline integrity, L2 trace, PDA/external-authority and L3/L4 boundaries;
- only after a successful rc05 review may a later RC explicitly promote reviewed entries to `Available` and separately decide whether a small second tranche should begin.

## v0.0.3rc04 — 2026-08-16

Localized initial L3 pattern-tranche trace cleanup after the independent v0.0.3rc03 review returned **PASS WITH MINOR CLEANUP / `INITIAL L3 PATTERN-TRANCHE GATE: YES, AFTER MINOR CLEANUP`**, with no Critical or Major finding and four Minor trace-contract findings.

### Changed

- resolved `R3-01` in `SCAF-PAT-SUP-002` by removing `SCAF-ROB-032` from Primary Realization Candidate trace and removing `SCAF-LIFE-008` / `SCAF-LIFE-009` from Supporting Realization while retaining those LIFE obligations as reset-semantics Constraint Inputs;
- clarified that any downstream repeated recovery/escalation is where applicable `SCAF-ROB-032` termination semantics are evaluated, without giving the watchdog recovery authority;
- resolved `R3-02` in `SCAF-PAT-REC-001` by adding conditional `SCAF-INT-007` duplicate/order semantics for repeated/interleaved Interaction exchanges and conditional `SCAF-INT-010` session-incarnation semantics where retry continuity crosses/reuses connection sessions, while retaining `SCAF-INT-013` for negative/non-conforming Interaction outcomes;
- resolved `R3-03` in `SCAF-PAT-LCM-001` by adding `SCAF-RUN-009` as the explicit LIFE-to-RUN readiness-handoff Constraint Input and preserving separate LIFE update/activation and RUN readiness authorities;
- resolved `R3-04` in `SCAF-PAT-EVD-001` by adding `SCAF-OBS-009` as the causal/derived-inference claim-basis Constraint Input so recorder evidence cannot self-author root-cause claims;
- advanced current L3 development labels and release/gate wording to v0.0.3rc04.

### Preserved

- all seven published Pattern IDs and immutable primary families;
- `Catalog Status: Candidate` and `Maturity: M1 — Structured` for every current pattern;
- frozen v0.0.2 `docs/normative/` content and all 294 normative IDs / 218 Project-Applicable Obligations / 76 Framework Normative Invariants;
- many-to-many L2→L3 trace semantics and the prohibition on generic L2→L3 `satisfies` shortcuts;
- Project Design Authority ownership of project mechanism selection/configuration and external source-authority ownership of external constraints;
- L3/L4 boundary and gates on schema, validator, CI, code generation and executable governance.

### Deliberately Not Added / Promoted

- no eighth Pattern ID or second pattern tranche;
- no primary-family move, `Supersedes` lifecycle event or Pattern-ID replacement;
- no Candidate→Available promotion;
- no M1→M2 promotion;
- no L4 implementation / verification guidance;
- no schema, validator, CI or executable-governance machinery.

### Gate

- run a focused independent rc04 closure review of `R3-01` through `R3-04`;
- regress all seven published IDs, primary families, Candidate/M1 states, index counts and L3/L4 boundaries;
- reconfirm the frozen v0.0.2 normative tree byte-stable and the 294 / 218 / 76 inventory unchanged;
- only after successful closure, allow the next RC to make explicit entry-by-entry M2 / `Available` decisions and separately decide whether a second tranche should begin.

## v0.0.3rc03 — 2026-08-16

Initial representative L3 Pattern / Mechanism tranche after the v0.0.3rc02 focused closure review returned **PASS / `L3 CATALOG-CONTRACT CLOSURE GATE: YES`**.

### Added

- published the first seven permanent L3 Pattern identities as `Candidate / M1` entries:
  - `SCAF-PAT-SUP-001` — Heartbeat / Liveness Supervision;
  - `SCAF-PAT-SUP-002` — Independent Watchdog with Escalation;
  - `SCAF-PAT-REC-001` — Bounded Retry with Escalation;
  - `SCAF-PAT-COM-001` — Reconnect plus State Reconciliation;
  - `SCAF-PAT-PST-001` — Atomic Dual-Copy Persistent State;
  - `SCAF-PAT-LCM-001` — Transactional Update with Rollback;
  - `SCAF-PAT-EVD-001` — Pre/Post-Trigger Retained Incident Evidence Ring;
- added family directories only for mechanism families that now contain published entries;
- added pattern-level metadata, L2 trace, PDA-decision, composition, failure-mode, provenance and L3/L4 boundary content for the initial tranche.

### Changed

- closed rc02 review Trivial `R2-01` by aligning the root README gate wording with the completed focused rc02 closure review and the open rc03 initial-pattern tranche;
- advanced L3 governance/metadata/trace/template development labels to v0.0.3rc03;
- updated the L3 index from zero-pattern planning state to the seven-entry Candidate/M1 navigation state;
- made the accepted contract explicitly applicable to current as well as future pattern entries;
- opened the independent initial-tranche conformance review gate while keeping `Available` promotion and broad catalog expansion closed.

### Preserved

- frozen v0.0.2 `docs/normative/` content and all 294 normative IDs / 218 Project-Applicable Obligations / 76 Framework Normative Invariants;
- many-to-many L2→L3 trace semantics and the prohibition on generic L2→L3 `satisfies` shortcuts;
- Project Design Authority ownership of project mechanism selection/configuration;
- separation among Catalog Status, Pattern Maturity and project-side Pattern Selection State;
- the mechanism-family primary-identity rule and post-publication immutability;
- L3/L4 boundary and the gates on schema, validator, CI, code generation and executable governance.

## v0.0.3rc02 — 2026-08-16

Focused L3 catalog-contract cleanup after the independent v0.0.3rc01 architecture review returned **PASS WITH MINOR CLEANUP / L3 CATALOG-CONTRACT GATE: YES, AFTER MINOR CLEANUP**, with no Critical or Major findings.

### Changed

- replaced concrete-looking `SCAF-PAT-*-001` examples with non-allocating `<NNN>` placeholders and defined that an ID is **published** only when assigned to an instantiated catalog entry in a repository release;
- clarified that illustrative pattern identifiers/placeholders do not allocate or reserve identities;
- defined primary pattern family by the pattern's principal reusable mechanism intent rather than by dominant frozen-concern trace;
- made the primary-family component immutable after pattern-ID publication and required a new ID plus explicit `Supersedes` lifecycle relation for genuine post-publication primary-family change;
- narrowed catalog `Constraint Input` targets to frozen L2 obligations and moved actual project Controlled Decision references to project-side selection/application records;
- kept decision categories in `Required PDA Decisions` while separating externally owned safety/security/regulatory/risk inputs into `External Authority Considerations`;
- represented `Subsumes` and `Supersedes` as distinct metadata/template relations;
- corrected the review baseline CTX SHA-256 manifest value used by the focused review instruction.

### Preserved

- frozen v0.0.2 L1/L2 normative baseline;
- 294 normative requirement IDs: 218 Project-Applicable Obligations and 76 Framework Normative Invariants;
- L3 mechanism-family taxonomy;
- many-to-many L2→L3 trace model and prohibition on generic L2→L3 `satisfies`;
- Project Design Authority ownership of project mechanism selection/configuration;
- independent catalog status, pattern maturity and project selection state;
- L3/L4 boundary;
- zero instantiated `SCAF-PAT-*` pattern entries.

### Deliberately Not Added

- actual L3 pattern instances or allocated Pattern IDs;
- L4 implementation / verification guidance;
- schema, validator, CI or executable-governance machinery.

### Gate

- run a focused independent rc02 closure review against rc01 findings L3-01 through L3-05 and T-01;
- confirm each finding is Resolved or explicitly identify any regression/new issue;
- reconfirm the frozen v0.0.2 normative baseline is byte-stable;
- if the focused review passes without Critical/Major findings and no unresolved identity/trace-authority defect remains, allow the next RC to allocate the first small representative `SCAF-PAT-*` tranche.

## v0.0.3rc01 — 2026-08-16

First controlled L3 Pattern / Mechanism Catalog architecture / contract RC downstream of the frozen v0.0.2 L1/L2 baseline.

### Added

- `docs/l3/README.md` establishing the L3 development scope and frozen-upstream rule;
- `docs/l3/00_L3_Catalog_Governance.md` defining the L3 `SCAF-PROF` authority position, mechanism-family taxonomy, `SCAF-PAT-<FAMILY>-<NNN>` identity rule, catalog status/maturity, composition semantics and L3/L4 boundary;
- `docs/l3/01_L3_Pattern_Metadata_Contract.md` defining the human-readable metadata contract, including mandatory `Required PDA Decisions`;
- `docs/l3/02_L3_Trace_and_Selection_Model.md` defining many-to-many L2→L3 trace semantics and separating catalog status from project selection state;
- `docs/l3/03_L3_Pattern_Index.md` as a non-authoritative planning/navigation index;
- `docs/l3/catalog/README.md` defining future mechanism-family placement;
- `docs/l3/templates/L3_Pattern_Template.md` for later pattern authoring.

### Architecture Decisions

- L3 is a downstream `SCAF-PROF` candidate realization catalog, not a third-level extension of the frozen concern requirement tree;
- L3 uses mechanism families (`SUP`, `COM`, `REC`, `FTL`, `TIM`, `PST`, `LCM`, `EVD`, `SYN`, `SEC`) rather than duplicating CTX/ARCH/INT/TIME/RUN/ROB/LIFE/OBS/CFG/SEC authority homes;
- pattern trace relations are `Primary Realization Candidate`, `Supporting Realization` and `Constraint Input`; a generic L2→L3 `satisfies` relation is intentionally prohibited;
- pattern selection/configuration remains a Project Design Authority decision and catalog selection alone does not establish L2 satisfaction;
- catalog lifecycle `Status` and engineering `Maturity` are independent dimensions;
- profile facets are orthogonal to mechanism families;
- project-specific mechanisms outside the catalog remain permitted when the applicable frozen obligations and external constraints are satisfied.

### Frozen Baseline Integrity

- **No `docs/normative/` v0.0.2 file is intentionally changed.**
- No frozen L1/L2 requirement ID, Target class, primary authority home, core metamodel entity or top-level concern taxonomy is reopened by this RC.

### Deliberately Not Added

- actual `SCAF-PAT-*` pattern instances;
- L4 implementation or verification guidance;
- machine-readable schema / authority registry;
- validator, generated reverse-trace index or CI;
- code generation / executable governance.

### Gate

- perform an independent L3 architecture / structure review;
- confirm frozen v0.0.2 normative hashes are unchanged;
- confirm L3 does not redefine L2 semantics or Project Design Authority;
- confirm the many-to-many trace model preserves multiple valid mechanism choices;
- confirm status/maturity, selection semantics and L3/L4 separation are sufficiently stable before allocating the first `SCAF-PAT-*` IDs.

## v0.0.2 — 2026-08-16

Frozen L1/L2 Baseline.

This release is created by explicit governance freeze decision after the independent `v0.0.2rc15` L1/L2 freeze-candidate audit returned **Yes**, with no Critical, Major, Minor or Trivial issues. The audit verified the rc15 archive SHA-256, confirmed all 294 parsed requirement blocks are stable relative to rc14, and found no cross-boundary, identity, source/evidence/closure, Framework Scan, L3/L4 or donor-promotion regression.

### Frozen

- Authority Kernel;
- SCAF-CTX;
- SCAF-ARCH;
- SCAF-INT;
- SCAF-TIME;
- SCAF-RUN;
- SCAF-ROB;
- SCAF-LIFE;
- SCAF-OBS;
- SCAF-CFG;
- SCAF-SEC;
- 294 normative requirement IDs;
- 218 Project-Applicable Obligations;
- 76 Framework Normative Invariants;
- primary authority homes and reviewed cross-boundary semantics;
- Boot / Operational / Session / Time Epoch / CFG / Security / OBS identity separation;
- source / evidence / evidence-sufficiency / underlying-closure separation;
- Framework Scan semantics;
- donor-promotion and L1/L2 mechanism-neutrality gates.

### Normative Semantic Change from v0.0.2rc15

- **None intended.**
- The freeze action changes release/freeze state only.
- Normative documents change release metadata from `v0.0.2rc15` to `v0.0.2`; requirement blocks remain unchanged.

### Not Included in the Frozen Baseline

- L3 pattern / mechanism catalogs;
- L4 implementation / verification guidance;
- schema;
- validator;
- CI;
- generated conformance tooling.

### Governance

- `v0.0.2` is frozen and must not be modified in place.
- Later L3/L4 or executable-governance work must trace to this frozen L1/L2 baseline and use a new development version when normative evolution is required.

## v0.0.2rc15 — 2026-08-16

Freeze-candidate release-hygiene closure after the independent rc14 audit found no Critical/Major issues, confirmed the four rc13 editorial findings Resolved, found no normative/cross-boundary/identity/Framework-Scan/L3-L4/donor-promotion regression, and returned the freeze gate Yes after one trivial non-semantic README cleanup.

### Changed

- corrected the stale README sentence that incorrectly described the next gate as another final integrated L1/L2 review;
- aligned the README introduction with the actual rc15 narrow freeze-candidate audit followed by an explicit governance freeze decision;
- synchronized current release / gate positioning to v0.0.2rc15;
- updated normative document release labels to v0.0.2rc15 without intended normative-body semantic change.

### Normative Semantic Change

- **None intended.**
- All 294 requirement IDs and all Target classes are preserved.
- Primary authority homes, cross-boundary semantics, identity semantics, Framework Scan semantics, verification/evidence/closure semantics, Security Authority provenance and donor-promotion gates are carried forward unchanged from rc14.

### Deliberately Not Added

- new top-level concerns or core metamodel entities;
- architecture rediscovery or taxonomy changes;
- L3 pattern / mechanism catalogs;
- L4 implementation / verification guidance;
- schema, validator, CI or generated conformance tooling.

### Gate

- perform a narrow independent rc15 L1/L2 freeze-candidate audit;
- confirm the rc14 audit T-01 README wording is Resolved;
- confirm 294 IDs / Targets and normative semantics remain stable;
- if the audit passes, make the explicit governance L1/L2 freeze decision.

## v0.0.2rc14 — 2026-08-16

Final editorial closure / L1/L2 freeze candidate after the independent rc13 final integrated review found no Critical/Major issues, judged the complete L1/L2 backbone Stable after minor editorial cleanup, and returned the freeze-candidate gate Yes after those editorial items are closed.

### Changed

- removed the lower-case normative-looking `shall` from Authority Kernel descriptive prose outside a Target-classified requirement block;
- normalized `SCAF-OBS-020` second prohibition to the canonical `**SHALL NOT**` normative-keyword form;
- corrected `docs/00_Input_Baseline.md` section numbering so the controlled-rewrite derivation note follows §7 as §8;
- corrected `docs/03_Gen1_to_Gen2_Concept_Mapping.md` duplicate §8 numbering by renumbering the controlled-rewrite-use section to §9;
- synchronized README, Authority Kernel release label, current gate and freeze-candidate positioning to v0.0.2rc14.

### Normative Semantic Change

- **None intended.**
- Requirement IDs, Target classes, primary authority homes, cross-boundary semantics, identity semantics, Framework Scan semantics, verification/evidence/closure semantics and donor-promotion gates are carried forward unchanged from rc13.

### Deliberately Not Added

- new top-level concerns or core metamodel entities;
- architecture rediscovery or taxonomy changes;
- L3 pattern / mechanism catalogs;
- L4 implementation / verification guidance;
- schema, validator, CI or generated conformance tooling.

### Gate

- perform a narrow independent rc14 freeze-candidate audit;
- confirm the four rc13 editorial findings are Resolved;
- confirm the rc13 normative architecture is unchanged except for non-semantic editorial cleanup;
- if the audit passes, make an explicit governance decision whether to freeze the L1/L2 baseline.

## v0.0.2rc13 — 2026-08-16

Final integrated L1/L2 consolidation after independent rc12 SCAF-SEC review found no Critical/Major issues, judged SEC Stable after minor cleanup, confirmed SEC integration with the existing L1/L2 backbone as Pass, and cleared SCAF to enter final consolidation before a freeze-candidate decision.

### Changed

- corrected `SCAF-SEC-024` to reference the normative `SCAF-SEC-038` SEC/OBS boundary;
- clarified `SCAF-SEC-017` so `SCAF-ROB` resilience obligations apply where resource abuse is robustness-significant;
- narrowed `SCAF-SEC-023` from ambiguous `CFG-controlled authorization` wording to authorization-related CFG input/fact semantics while preserving Security Authority and CFG source authority;
- normalized residual ROB structural-boundary wording to an applicable Project Design Authority decision under SCAF-ARCH;
- normalized residual CTX safety/hazard source-authority wording without changing safety/risk acceptance authority;
- consolidated current release/gate wording for the complete CTX/ARCH/INT/TIME/RUN/ROB/LIFE/OBS/CFG/SEC L1/L2 backbone;
- synchronized README, Authority Kernel release label, read-coverage position and current freeze-candidate gate.

### Deliberately Not Added

- new top-level concerns or core metamodel entities;
- SCAF taxonomy changes or architecture rediscovery;
- L3 pattern / mechanism catalogs;
- L4 implementation / verification guidance;
- cryptographic, resilience, lifecycle, logging, configuration or protocol implementation mechanisms;
- schema, validator, CI or generated conformance tooling.

### Gate

- perform independent final integrated L1/L2 review;
- determine whether the complete L1/L2 backbone is suitable as a freeze candidate;
- keep L3 closed until the integrated review passes and an explicit freeze decision is made.

## v0.0.2rc12 — 2026-08-16

SCAF-SEC controlled L1/L2 normative tranche after independent rc11 integrated review found no Critical/Major issues, accepted CTX/ARCH/INT/TIME/RUN/ROB/LIFE/OBS/CFG as Stable, and cleared SEC to start with parallel minor consolidation cleanup.

### Added

- `docs/normative/100_SCAF_SEC_Security_Architecture_Interface_Robustness_Obligations.md`;
- L1 authority separation for External Security Authority -> SCAF-SEC -> Project Design Authority;
- project obligations for security-relevant assets/subjects/trust relationships, security identity, authentication, authorization, confidentiality, integrity/authenticity, hostile freshness/anti-replay and credential/key lifecycle architecture semantics;
- project obligations for privilege/separation, security-sensitive control paths, hostile input/resource abuse, compromise/trust loss, compromise containment, security degradation/downgrade, security-service dependency and trust re-establishment eligibility;
- project obligations for security-sensitive LIFE/CFG relationships, security evidence needs, multi-participant security-decision consistency, verification-claim trace and re-evaluation;
- explicit SEC/ARCH, SEC/INT, SEC/TIME, SEC/RUN, SEC/ROB, SEC/LIFE, SEC/OBS, SEC/CFG, SEC/ASSUR, identity-partition and SEC/PROF realization boundaries.

### Changed

- normalized older Project-Applicable boundary/non-prescription explanatory prose as informative notes where identified by the rc11 integrated review;
- replaced `SCAF-INT-017` non-canonical `owned by SCAF-ROB` wording with Authority Kernel framework-semantics grammar;
- replaced the stale ROB `persistent configuration ownership` phrase with authoritative CFG source/value semantics;
- synchronized README, Authority Kernel release labels and read-coverage position for the SEC tranche;
- retained the frozen v0.0.1 architecture baseline and stable CTX/ARCH/INT/TIME/RUN/ROB/LIFE/OBS/CFG authority homes.

### Deliberately Not Added

- new top-level taxonomy or core metamodel entities;
- universal threat model, security objective, risk-acceptance policy or certification acceptance authority;
- universal encryption/signature algorithm, key size, certificate/PKI, secure element, TPM/HSM, secure-boot implementation, firewall, sandbox, credential store, password/token format or access-control mechanism;
- L3 pattern/mechanism catalog or L4 implementation/verification guidance;
- schema, validator, generated checklist or CI;
- broad Draft/RC donor promotion, final migration proof or normative freeze.

## v0.0.2rc11 — 2026-08-16

Integrated L1/L2 consolidation after independent rc10 review accepted CFG as Stable after minor cleanup and judged the CTX -> ARCH -> INT -> TIME -> RUN -> ROB -> LIFE -> OBS -> CFG backbone Stable after targeted consolidation. No new concern tranche is added.

### Changed

- narrowed broad CFG `corruption recovery` wording to corruption/loss/unavailability interpretation, CFG source-state disposition/restoration eligibility and authoritative resulting CFG state, while preserving ROB recovery/resilience-response authority;
- completed `SCAF-CFG-016` derived-value provenance with source identity, version/context, derivation basis, resulting-value provenance and invalid/unknown/incompatible-input consequence;
- normalized framework-boundary/non-prescription prose in `SCAF-CFG-006`, `SCAF-CFG-010`, `SCAF-CFG-018` and `SCAF-CFG-022` as informative boundary notes;
- hardened CFG item/version identity so physical storage locators do not by themselves establish semantic CFG identity;
- rewrote `SCAF-CFG-023` as a CFG-source-fact observability need traced to OBS, rather than CFG defining OBS evidence semantics;
- added explicit INT-to-CFG hardening: INT-valid/delivered/decoded configuration data does not by itself establish CFG acceptance, commit, activation/application or authoritative CFG source state;
- normalized older RUN/ROB/LIFE/OBS forward references to PDA-assigned authoritative CFG source responsibility and CFG source/value/version/migration/commit semantics;
- synchronized README, Authority Kernel release label and read-coverage positioning for the pre-SEC consolidation gate;
- retained the frozen v0.0.1 architecture baseline and existing concern taxonomy.

### Deliberately Not Added

- `SCAF-SEC` normative tranche;
- new top-level taxonomy or core metamodel entities;
- L3 pattern/mechanism catalog;
- L4 implementation/verification guidance;
- schema, validator, generated checklist or CI;
- broad Draft/RC donor promotion, final migration proof or normative freeze.

## v0.0.2rc10 — 2026-08-16

SCAF-CFG controlled L1/L2 normative tranche after independent rc09 review cleared the OBS architecture gate and allowed CFG authoring to begin with localized OBS cleanup.

### Added

- `docs/normative/90_SCAF_CFG_Configuration_Persistent_Operational_State_Obligations.md`;
- L1 authority boundaries for configuration/persistent operational-state classification, authoritative source responsibility, item identity/provenance, defaults/provisioning, validation, version/migration, atomic commit, CFG-side rollback/corruption handling, calibration/parameter state and synchronization/consistency;
- project obligations for unknown/uninitialized semantics, multiple-source precedence, LIFE update/activation coordination, RUN persistent/current-state mapping, OBS evidence views of CFG facts and external configuration constraints;
- explicit CFG/OBS, CFG/LIFE, CFG/RUN, CFG/INT, CFG/TIME, CFG/ROB, CFG/ARCH, external-authority, CFG/ASSUR, artifact/source-authority, identity-partition and CFG/PROF realization boundaries.

### Changed

- removed the framework-self timebase prohibition from `SCAF-OBS-006` Project-Applicable target and retained it only as an informative note backed by `SCAF-OBS-033`;
- normalized framework-boundary/non-prescription prose in Project-Applicable OBS obligations as informative notes;
- narrowed `SCAF-OBS-009` to causal/derived-inference claims and separated first-observed abnormal evidence semantics in `SCAF-OBS-016`;
- narrowed `SCAF-OBS-021` to retention/accessibility/expiration while retaining lifecycle survivability in `SCAF-OBS-018`;
- corrected stale README rc08 release/gate/repository-content text and remaining ROB non-normative editorial residue;
- updated all normative release labels and Authority Kernel gate-table label to rc10;
- retained the frozen v0.0.1 architecture baseline and stable Authority Kernel / CTX / ARCH / INT / TIME / RUN / ROB / LIFE authority homes.

### Deliberately Not Added

- `SCAF-SEC` normative tranche;
- new top-level taxonomy or core metamodel entities;
- universal configuration file/schema/database/NVM layout/migration/rollback/synchronization mechanisms;
- L3/L4 mechanism or implementation guidance;
- schema, validator, generated checklist or CI;
- broad Draft/RC donor promotion, final migration proof or normative freeze.

## v0.0.2rc09 — 2026-08-15

SCAF-OBS controlled L1/L2 normative tranche after independent rc08 review cleared the LIFE architecture gate and allowed OBS authoring to begin with localized LIFE cleanup.

### Added

- `docs/normative/80_SCAF_OBS_Observability_Diagnostics_Incident_Evidence_Obligations.md`;
- L1 authority boundaries for operational observability, diagnostics, incident evidence, evidence identity/provenance, time/identity correlation, evidence quality/missingness, preservation/survivability/accessibility/export, observer self-health and observer effect;
- project obligations for source-authority trace, first-abnormal versus later/terminal evidence, incident timeline/correlation, lifecycle survivability, early-boot/crash-loop evidence, four-way identity recording, evidence copies/transforms, persistent evidence/CFG distinction and external evidence constraints;
- explicit OBS/RUN, OBS/ROB, OBS/LIFE, OBS/INT, OBS/TIME, OBS/CFG, OBS/ASSUR, external-authority, four-way-identity, OBS/ARCH, causal-inference and OBS/PROF realization boundaries.

### Changed

- moved the `SCAF-LIFE-014` framework self-rule out of the Project-Applicable target by converting it to an informative boundary note backed by existing framework invariants;
- narrowed `SCAF-LIFE-007` Boot Incarnation triggers to LIFE-controlled boot/lifecycle instances and preserved RUN authority for runtime-only operational restart/replacement;
- changed `SCAF-LIFE-010` from intrinsic retained-state validity wording to lifecycle-transition consumption eligibility using controlled source-authority validity/provenance/version semantics;
- normalized `SCAF-LIFE-012` and `SCAF-LIFE-013` to PDA-assigned lifecycle authoritative-result responsibility and lifecycle responsibility handoff wording;
- separated `SCAF-LIFE-016` lifecycle activation/eligibility from RUN Service readiness/availability;
- replaced `SCAF-LIFE-018` bare `safely or correctly` wording with applicable controlled continuation/eligibility criteria and source-authority trace;
- corrected minor LIFE/ROB editorial residue and updated README, Authority Kernel gate label and read-coverage position for rc09;
- retained the frozen v0.0.1 architecture baseline and stable Authority Kernel / CTX / ARCH / INT / TIME / RUN / ROB authority homes.

### Deliberately Not Added

- `SCAF-CFG` or `SCAF-SEC` normative tranches;
- new top-level taxonomy or core metamodel entities;
- universal log schema, ring buffer, retained-RAM layout, crash-recorder API, storage technology, telemetry protocol or diagnostic mechanism;
- L3/L4 mechanism or implementation guidance;
- schema, validator, generated checklist or CI;
- broad Draft/RC donor promotion, final migration proof or normative freeze.

## v0.0.2rc08 — 2026-08-15

SCAF-LIFE controlled L1/L2 normative tranche after independent rc07 review cleared the ROB architecture gate and allowed LIFE authoring to begin with localized ROB cleanup.

### Added

- `docs/normative/70_SCAF_LIFE_Boot_Power_Reset_Update_Lifecycle_Obligations.md`;
- L1 authority boundaries for boot/power/reset/update/activation/rollback lifecycle transaction/state/result semantics and Boot Incarnation / Boot Generation;
- project obligations for lifecycle authority/result responsibility, request-versus-result semantics, LIFE-to-RUN readiness handoff, reset classification/cause, retained-state validity, power lifecycle, update preconditions/atomicity/activation/rollback/resume and multi-participant lifecycle coordination;
- explicit LIFE/RUN, LIFE/ROB, LIFE/TIME, LIFE/INT, LIFE/CFG, LIFE/OBS, identity-partition, LIFE/ARCH, external safety/security/risk and LIFE/PROF realization boundaries.

### Changed

- split `SCAF-ROB-005` detectability/latent-condition disposition from diagnostic-coverage objective by adding `SCAF-ROB-031`;
- split `SCAF-ROB-011` recovery/repair outcome from retry/escalation termination by adding `SCAF-ROB-032`;
- clarified `SCAF-ROB-014` so residual-risk decision/acceptance is explicitly made by the applicable risk authority;
- split `SCAF-ROB-027` ROB/OBS evidence-observation boundary from ROB/ASSUR evidence-sufficiency boundary by adding `SCAF-ROB-033`;
- normalized health/failure terminology so ROB classifications/decision outcomes are not confused with RUN operational states;
- replaced residual `approved` and project-actor-like ROB prose with controlled Authority Kernel relation language;
- updated README, Authority Kernel gate label and read-coverage position for rc08;
- retained the frozen v0.0.1 architecture baseline and stable Authority Kernel / CTX / ARCH / INT / TIME / RUN authority homes.

### Deliberately Not Added

- `SCAF-OBS`, `SCAF-CFG` or `SCAF-SEC` normative tranches;
- new top-level taxonomy or core metamodel entities;
- universal bootloader/A-B partition/update protocol/reset sequence/power sequencing/watchdog/recovery mechanisms;
- L3/L4 mechanism or implementation guidance;
- schema, validator, generated checklist or CI;
- broad Draft/RC donor promotion, final migration proof or normative freeze.

## v0.0.2rc07 — 2026-08-15

SCAF-ROB controlled L1/L2 normative tranche after independent rc06 review cleared the RUN architecture gate and allowed ROB authoring to begin with localized RUN cleanup.

### Added

- `docs/normative/60_SCAF_ROB_Robustness_Resilience_Obligations.md`;
- L1 authority boundaries for Fault/Error/Failure semantics, health/failure determination, detectability/latent conditions, propagation, runtime containment, tolerance/degradation/failover/reconfiguration, recovery/repair/retry and reintegration;
- project obligations for distributed partition/reconciliation resilience, correlated/common-mode faults, cascading/recovery-storm behavior, resource-exhaustion/long-run resilience, lifecycle/configuration failure response and robustness observability;
- explicit ROB/RUN, ROB/ARCH, ROB/TIME, ROB/INT, ROB/LIFE, ROB/OBS/ASSUR, ROB/CFG, external safety/security/risk and ROB/PROF realization boundaries.

### Changed

- clarified `SCAF-RUN-002` so Project Design Authority defines the project state model and assigns runtime authoritative-current-state responsibility, while state carriers/requests/logs do not become runtime state authority;
- normalized Project-Applicable RUN boundary prose as informative notes or separate trace obligations;
- replaced non-canonical `RUN controls / ROB controls` wording with Authority Kernel framework-semantics plus Project Design Authority project-instance grammar;
- split RUN/CFG from RUN/OBS and CTX operating-mode from incarnation-identity framework invariants;
- added atomic readiness/availability consequence trace and cross-participant measurable-consistency trace obligations;
- replaced RUN `disposition` wording that could be confused with SCAF-APP Disposition vocabulary;
- completed supporting Evidence-state terminology by replacing generic evidence `Accepted` with `Sufficient`;
- updated the Authority Kernel gate-table release label and README/read-coverage position for rc07;
- retained the frozen v0.0.1 architecture baseline and stable Authority Kernel / CTX / ARCH / INT / TIME authority homes.

### Deliberately Not Added

- `SCAF-LIFE`, `SCAF-OBS`, `SCAF-CFG` or `SCAF-SEC` normative tranches;
- new top-level taxonomy or core metamodel entities;
- universal watchdog/heartbeat/redundancy/voting/retry/failover/reset mechanisms;
- L3/L4 mechanism or implementation guidance;
- schema, validator, generated checklist or CI;
- broad Draft/RC donor promotion, final migration proof or normative freeze.

## v0.0.2rc06 — 2026-08-15

SCAF-RUN controlled L1/L2 normative tranche after independent rc05 review cleared INT/TIME authority boundaries and allowed RUN authoring to begin.

### Added

- `docs/normative/50_SCAF_RUN_Runtime_State_Operational_Lifecycle_Obligations.md`;
- L1 authority boundaries for operational/service state meaning, state domains, transition consistency, readiness/availability, generic operational lifecycle and Operational Incarnation;
- project obligations for state authority, state invariants, permitted transitions, transition conditions, readiness/availability criteria, CTX-mode mapping, LIFE-to-RUN handoff, cross-participant state consistency and Operational Incarnation;
- explicit RUN/INT/TIME, RUN/LIFE, RUN/ROB, RUN/CFG/OBS and operating-mode/incarnation framework invariants.

### Changed

- split `SCAF-TIME-004` clock/synchronization relationship semantics from dependent temporal-claim validity under clock-relationship loss by adding `SCAF-TIME-020`;
- normalized staged forward-reference wording so TIME can trace consequences to controlled INT/RUN/ROB requirements, decisions or obligations without requiring future normative IDs to already exist;
- normalized the supporting Framework Scan evidence-state wording from generic `Accepted` to evidence-sufficiency language;
- updated README and read-coverage status for the RUN tranche;
- retained the frozen v0.0.1 architecture baseline and stable Authority Kernel / CTX / ARCH / INT baselines.

### Deliberately Not Added

- `SCAF-ROB`, `SCAF-LIFE`, `SCAF-OBS`, `SCAF-CFG` or `SCAF-SEC` normative tranches;
- new top-level taxonomy or core metamodel entities;
- state-machine implementation patterns, RTOS/task/thread rules or scheduling mechanisms;
- L3/L4 mechanism or implementation guidance;
- schema, validator, generated checklist or CI;
- broad Draft/RC donor promotion, final migration proof or normative freeze.

## v0.0.2rc05 — 2026-08-15

Targeted INT/TIME authority-boundary closure after independent review of v0.0.2rc04.

### Changed

- tightened `SCAF-TIME-008` so TIME defines concurrency constraints only when needed to establish an explicitly TIME-owned measurable temporal/capacity/resource property;
- added an explicit TIME/INT/RUN concurrency-and-ordering framework invariant so INT keeps semantic ordering and RUN keeps operational-state/transition consistency;
- removed ROB detection/health authority from `SCAF-TIME-012`, leaving TIME with measurable starvation/fairness/overload bounds and prevention/bounding constraints;
- narrowed `SCAF-TIME-013` to accumulation model, operating horizon, measurable bound/capacity and margin, leaving exhaustion detection and rollover/renewal/degradation/recovery behavior to the applicable downstream concern;
- closed synchronization-loss semantics in `SCAF-TIME-004` by requiring dependent temporal claims to define validity/invalidation/re-evaluation behavior when the required clock relationship is unusable;
- normalized TIME wording to distinguish chronological/temporal ordering from `SCAF-INT` semantic ordering;
- strengthened `SCAF-INT-002` to preserve the frozen Interaction-to-Interface boundary relation and added a conditional separately-controlled Interface identity obligation;
- widened `SCAF-INT-003` participant coverage to external Systems/actors/applicable external participants without forcing Node modeling;
- strengthened `SCAF-INT-006` with explicit validity-state assignment criteria and contract-consequence trace;
- retained the frozen v0.0.1 architecture baseline and stable Authority Kernel / CTX / ARCH normative baselines.

### Deliberately Not Added

- `SCAF-RUN` normative tranche;
- new top-level taxonomy or core metamodel entities;
- new Capacity or Concurrency top-level concerns;
- ROB normative elaboration beyond preserving its frozen authority boundary;
- L3/L4 mechanism or implementation guidance;
- schema, validator, generated checklist or CI;
- broad Draft/RC donor promotion, final migration proof or normative freeze.

## v0.0.2rc04 — 2026-08-15

INT + TIME controlled L1/L2 normative tranche.

### Added

- `docs/normative/30_SCAF_INT_Interface_Interaction_Data_Contract_Obligations.md`;
- `docs/normative/40_SCAF_TIME_Timing_Concurrency_Capacity_Obligations.md`;
- explicit INT/TIME freshness-state versus measurable-time authority boundary;
- explicit protocol-session versus Time Epoch / Boot Incarnation / Operational Incarnation authority partition in normative form;
- project obligations for Interface/Interaction identity, contract semantics, validity/provenance/order/freshness, compatibility/evolution and session identity;
- project obligations for timebase, synchronization, temporal budgets, concurrency, queue/capacity, resource margin and long-duration bounded-growth properties.

### Changed

- accepted the rc03 independent review result that Authority Kernel / CTX / ARCH have no remaining Critical or Major closure defects;
- split `SCAF-CTX-007` consequence, ordinary continuity/degradation and safety-source provenance into more atomic project obligations;
- split underlying closure authority from SCAF-APP closure/disposition trace in the Authority Kernel;
- removed the remaining `verification obligation/result` lexical collapse from the Authority Kernel relation grammar;
- normalized supporting `SCAF-ASSUR` wording to framework-side verification/evidence-sufficiency criteria plus project-side evidence evaluation;
- updated README and read-coverage status for the INT + TIME tranche.

### Deliberately Not Added

- `SCAF-RUN` normative tranche;
- new top-level taxonomy or core metamodel entities;
- L3 watchdog/heartbeat/CRC/ECC/retry/failover mechanism catalogs;
- L4 MCU/PC/SoC/FPGA/DSP implementation rulebooks;
- schema, validator, generated checklist or CI;
- broad Draft/RC donor promotion, final migration proof or normative freeze.

## v0.0.2rc03 — 2026-08-15

Target/authority precision closure release after independent review of v0.0.2rc02. The frozen v0.0.1 architecture baseline remains unchanged.

### Changed

- split mixed requirement targets so Project-Applicable Obligations no longer contain SCAF framework self-rules;
- separated `SCAF-CTX-007` project consequence/outcome obligations from the `SCAF-CTX` / `SCAF-ROB` / safety-authority framework boundary invariant;
- restored applicable safety/hazard authority as the source authority for safety-significant safety objectives/conditions and risk-acceptance basis, with Project Design Authority integrating those inputs into architecture;
- separated `SCAF-ARCH-008` project containment-structure inputs from the framework-level ARCH/ROB containment-authority invariant;
- separated Decision from Deviation and Verification Obligation from Verification Execution/Result State in `SCAF-AK-003`;
- split evidence-sufficiency evaluation from underlying closure authority by adding `SCAF-AK-012`;
- moved the unqualified relation-language prohibition into the explicit `SCAF-AK-011` Framework Normative Invariant;
- split Node-decomposition applicability from Node-boundary definition into `SCAF-ARCH-002` and `SCAF-ARCH-016`;
- tightened `SCAF-CTX-003` Function traceability and `SCAF-ARCH-015` shared-dependency representation wording;
- normalized frozen-reference wording so current development-line semantics no longer carry stale rc01 labels or outdated evidence/acceptance language.

### Deliberately Not Added

- `SCAF-INT`, `SCAF-TIME` or `SCAF-RUN` normative tranches;
- new top-level taxonomy branches or core metamodel entities;
- L3 mechanism catalogs or L4 implementation rulebooks;
- schema, validator, CI or generated checklist machinery;
- broad donor promotion, final migration proof or normative freeze.

## v0.0.2rc02 — 2026-08-15

Targeted normative-precision correction release after independent review of v0.0.2rc01. The frozen v0.0.1 architecture baseline remains unchanged.

### Changed

- separated **Project-Applicable Obligations** from **Framework Normative Invariants** in the Authority Kernel;
- restored project evidence-sufficiency decisions exclusively to Project Verification / Assurance Authority while keeping `SCAF-ASSUR` as framework-side assurance/evidence semantic authority;
- clarified that external safety/security/regulatory/risk constraints do not automatically turn the external authority into Project Design Authority;
- separated decision/deviation, risk, verification and evidence state dimensions in `SCAF-AK-003`;
- tightened closure semantics so verification authority does not inherit underlying requirement/design/risk/deviation closure authority;
- split cross-cutting project ownership from framework authoring invariants;
- narrowed `SCAF-CTX-007` to consequence and required continuity/degradation/safety constraints, leaving failover/recovery response to `SCAF-ROB` and safety-significant conditions to applicable safety/hazard authority;
- converted `SCAF-CTX-010` into CTX trace-source readiness rather than duplicate architecture-justification authority;
- split material operating-mode context into `SCAF-CTX-012`;
- made Node decomposition explicitly applicability-driven in `SCAF-ARCH-002`;
- constrained Capability/Service allocation to the frozen System/Node metamodel typing;
- corrected `SCAF-ARCH-008` so Project Design Authority defines actual containment-relevant structural/Domain boundaries while `SCAF-ROB` owns runtime containment behavior;
- split compound ARCH obligations into structural context trace, logical-vs-structural dependency distinction and shared-dependency exposure requirements;
- clarified informative summary tables so they do not create duplicate normative obligations;
- normalized residual authority wording in supporting analysis material.

### Deliberately Not Added

- `SCAF-INT`, `SCAF-TIME` or `SCAF-RUN` normative tranches;
- new top-level taxonomy branches or core metamodel entities;
- L3 watchdog/heartbeat/CRC/ECC or other mechanism catalogs;
- broad L4 implementation rulebooks;
- schema, validator, CI or generated checklist machinery;
- broad donor promotion, final migration proof or normative freeze.

## v0.0.2rc01 — 2026-08-15

First controlled L1/L2 normative-rewrite release candidate after the frozen v0.0.1 architecture baseline.

### Added

- `docs/normative/00_SCAF_Authority_Kernel.md` with normative authority roles, relation grammar, Applicable Satisfaction Basis, closure semantics and rewrite/promotion gates;
- `docs/normative/10_SCAF_CTX_System_Context_Obligations.md` with initial L1/L2 System Context / Function / Capability / Service obligations;
- `docs/normative/20_SCAF_ARCH_System_Architecture_Obligations.md` with initial L1/L2 System / Node / Role / Domain architecture obligations;
- provisional normative requirement identifiers for the first controlled rewrite tranche.

### Changed

- separated framework-side `SCAF-PROF` from project-side Project Realization: profiles guide/constrain realization; project realization actors actually realize decisions;
- separated framework-side `SCAF-ASSUR` semantics from project-side Project Verification / Assurance Authority;
- normalized Authority Role -> Controlled Decision -> Authoritative Artifact vocabulary;
- normalized the authority relation grammar to distinguish `Guides Realization` from project-side `Realizes`;
- clarified controlled rewrite eligibility vs donor normative-promotion eligibility;
- updated freshness, containment, lifecycle and evidence overlap prose to use framework-side/project-side authority language;
- reframed already-owned Function/Service and Configuration areas as normative-elaboration coverage rather than taxonomy gaps;
- updated deferred CI/fixture wording to reflect the controlled rewrite phase rather than architecture-convergence status.

### Deliberately Not Added

- new top-level taxonomy branches or core metamodel entities;
- L3 mechanism catalogs such as watchdog, heartbeat, CRC or ECC guidance;
- broad L4 MCU/PC/SoC/FPGA/DSP implementation rulebooks;
- final schema, validator, generated checklist or CI enforcement;
- broad Draft/RC donor promotion, final migration proof or normative freeze.

## v0.0.1 — 2026-08-15

Frozen architecture-convergence / authority-kernel baseline.

### Release Decision

- frozen from the reviewed `v0.0.1rc05` baseline after independent review reported **no Critical architecture issues**;
- architecture discovery is closed for this baseline;
- top-level taxonomy expansion is closed unless a future concrete project demonstrates an authority-home failure that cannot be resolved within the existing model;
- Framework Scan is accepted as a new-project startup architecture decision mechanism;
- controlled L1/L2 normative rewrite is permitted on the next development line;
- MD-first / No-CI remains in effect.

### Freeze Scope

The v0.0.1 freeze locks the architecture-convergence baseline and authority kernel. It does **not** claim:

- completed Gen1 requirement-by-requirement migration;
- broad normative promotion of Draft/RC or mixed-maturity donor semantics;
- extraction of all schema/validator/test-fixture executable invariants;
- final machine-readable schema, validator or CI enforcement;
- completion of L1/L2 normative content, L3 pattern catalogs or L4 implementation guidance.

Known lexical/authority-language cleanup identified by the rc05 independent review is intentionally deferred to `v0.0.2rc01` controlled rewrite rather than reopening the v0.0.1 architecture-convergence cycle.

### Deliberately Not Added

- new top-level taxonomy branches or core metamodel entities;
- CI / GitHub Actions;
- validators or final schemas;
- broad implementation rulebooks or mechanism catalogs.

All notable changes to **System Control Architecture Framework (SCAF)** are recorded here.

## v0.0.1rc05 — 2026-08-15

Authority-kernel cleanup / controlled-rewrite baseline release candidate.

### Changed

- accepted the rc04 independent review conclusion that no Critical architecture flaw remains and controlled normative rewrite may continue;
- clarified that the five authority planes are **SCAF framework planes** and that Project Design Authority is a project-side authority bridge rather than an implicit sixth SCAF plane;
- narrowed Framework / Governance to SCAF normative-source, authority, precedence and release/change governance, explicitly excluding organizational governance of project design/realization;
- separated authority roles from the controlled artifacts that record their decisions;
- renamed `SCAF-RUN` to **Runtime Behavior, State & Operational Lifecycle** without changing the concern ID;
- partitioned Time Epoch / Time Domain (`SCAF-TIME`), Boot Incarnation (`SCAF-LIFE`), Protocol/Connection Session Identity (`SCAF-INT`), Operational Incarnation (`SCAF-RUN`) and OBS-recorded provenance/correlation;
- replaced ambiguous `source-owned satisfaction condition` wording with **Applicable Satisfaction Basis**, traceable to SCAF obligations, Project Design Authority values and applicable external authority constraints;
- aligned worked Framework Scan closure examples with the Applicable Satisfaction Basis terminology;
- split Gen1 Node identity / capability mapping into Node identity, capability semantics and capability allocation destinations;
- reframed Crash Recorder `boot epoch` as LIFE-owned boot-incarnation identity recorded by OBS, distinct from TIME-owned time epoch;
- strengthened per-donor promotion gating for stale-data, domain and implementation-rulebook donor families;
- reframed resolved robustness areas as coverage requiring normative elaboration rather than unresolved taxonomy gaps;
- changed stale `before normative rewrite` wording to controlled-rewrite / broad-expansion / promotion / freeze priorities;
- retained MD-first / No-CI policy and stopped top-level taxonomy expansion.

### Deliberately Not Added

- new top-level taxonomy branches or concerns;
- CI / GitHub Actions;
- validators or final schemas;
- broad L3 mechanism catalogs or L4 implementation rulebooks;
- frozen Draft/RC donor semantics;
- claims of completed Gen1 migration or normative freeze.

## v0.0.1rc04 — 2026-08-15

Architecture-closure / controlled-rewrite-entry release candidate.

### Changed

- accepted the rc03 independent review conclusion that the SCAF skeleton is converged enough for **controlled normative rewrite**;
- established one canonical authority model: Concern -> Project Design -> Realization -> Assurance, with `SCAF-APP` cross-cutting for disposition/trace and Governance governing the authorities;
- removed ambiguous bare `Defines` authority headings in system concerns and applied the full Framework-vs-Project authority grammar consistently;
- broke the Service/Capability circular definition and clarified subordinate System vs subordinate Node scope semantics;
- tightened the Node-boundary test so physical boundaries or verification tasks alone do not create Nodes;
- clarified `SCAF-ROB` vs `SCAF-LIFE` vs `SCAF-OBS` vs `SCAF-ASSUR` ownership for lifecycle failure, health decisions, evidence and verification;
- clarified Security Authority vs Project Design Authority: security authority owns threat/objective/risk constraints, while Project Design owns actual trust boundaries and architecture decisions;
- corrected the README robustness model so prevention/avoidance is design/realization strategy rather than Assurance ownership;
- replaced the broad eleven-row Framework Scan proof with complete state/authority/closure traces for selected concerns;
- clarified that Assurance verifies evidence sufficiency, source/project/risk authorities accept applicable closure, and `SCAF-APP` records the closure/deviation trace;
- strengthened per-donor maturity binding in multi-source migration rows and aligned distributed incident time provenance with both `SCAF-TIME` and `SCAF-OBS`;
- removed stale release-specific fixture wording from the Gen1 inventory;
- moved the project gate from architecture discovery to **controlled authority-preserving normative rewrite** while keeping migration/promotion/freeze gates explicit.

### Deliberately Not Added

- new top-level taxonomy branches;
- CI / GitHub Actions;
- validators or final schemas;
- generated checklists;
- broad MCU / FPGA / DSP / C / C# rulebooks;
- full cybersecurity or safety frameworks;
- frozen Draft/RC donor semantics;
- claims of completed Gen1 migration.

## v0.0.1rc03 — 2026-08-15

Authority-semantics and project-application convergence release candidate.

### Changed

- separated **SCAF Concern Authority** from **Project Design Authority** so framework semantics/obligations cannot be confused with project-specific architecture values;
- clarified that `SCAF-APP` dispositions/traces project state but does not become the project architecture authority;
- clarified that `SCAF-ASSUR` owns verification/evidence sufficiency, not underlying system-property thresholds;
- replaced the README's linear five-plane pipeline with non-linear governance / concern / project-design / realization / assurance relations;
- partitioned `SCAF-CTX` logical mission/service dependencies from `SCAF-ARCH` structural allocation/realization dependencies;
- defined `SCAF-RUN` as service/operational lifecycle and `SCAF-LIFE` as platform/system boot/reset/power/update lifecycle;
- moved primary timebase/clock/synchronization semantics to `SCAF-TIME` and added Clock/Time Domain;
- limited `SCAF-OBS` to observing/recording time provenance and synchronization quality for evidence;
- scoped `SCAF-SEC` as a system-control architecture interface to external/project cybersecurity authority rather than a replacement threat/risk framework;
- changed reference subsystems/patterns from a profile axis to a Realization Plane pattern category;
- made Framework Scan explicitly iterative for greenfield startup;
- added an end-to-end worked Framework Scan for the PC + multiple MCU archetype across eleven concerns;
- added per-donor source-maturity binding examples for multi-source migration rows;
- distinguished donor **source identity** from **source retrievability** and kept immutable donor locators as an explicit remaining gate item;
- incorporated the v0.0.1rc02 independent architecture review as non-normative correction input.

### Deliberately Not Added

- CI / GitHub Actions;
- validators or schemas;
- generated checklists;
- new normative rulebooks;
- large-scale normative rewrite.

## v0.0.1rc02 — 2026-08-15

Architecture / taxonomy convergence release candidate.

### Changed

- adopted the long-term framework name **System Control Architecture Framework (SCAF)**;
- retained `Gen2` only as lineage / migration context;
- defined that **Control** means system-level coordination/runtime/lifecycle/robustness concerns, not control theory and not only host-to-device control;
- separated **Framework/Governance**, **System Concern**, **Project Application**, **Assurance/Evidence**, and **Realization/Implementation** authority planes;
- removed Tooling and AI-Assisted Engineering from peer system-taxonomy status;
- expanded the core metamodel beyond Node-centric structure with Function / Service / Capability, Interface, Interaction and cross-cutting Domains;
- defined Node boundary criteria and clarified that Node is not synonymous with chip/process/device/fault/reset/power/security domain;
- introduced explicit authority relations: Defines / Constrains / Realizes / Observes / Verifies / Dispositions;
- separated artifact disposition from transformation in the migration mapping;
- added source document, section anchor, source maturity, target concern ID, confidence and deep-audit state to the concept mapping;
- replaced the linear robustness lifecycle with separate Fault/Error/Failure semantics, Runtime Resilience Response and Assurance models;
- added redundancy, failover, reconfiguration, repair, resynchronization, reintegration, diagnostic coverage and distributed-failure concerns;
- clarified that Safe State authority must come from applicable project safety/hazard authority when safety-relevant;
- made Function/Service dependency and Configuration/Persistent Operational State explicit concern homes;
- reworked Framework Scan into a decision/evidence lifecycle with independent Applicability / Decision / Risk / Verification / Evidence dimensions;
- clarified that Framework Scan dispositions project obligations but does not create or delete SCAF normative obligations;
- reorganized implementation profiles as composable axes instead of one mixed profile list;
- added distributed incident time provenance / synchronization quality / causal-correlation concerns;
- added three tabletop architecture archetypes to exercise the metamodel without adding new top-level branches;
- corrected read-coverage terminology from “three levels” to **four levels**;
- normalized the supplemental-source inventory action vocabulary.

### Deliberately Not Added

- CI / GitHub Actions;
- validators;
- Python tooling;
- test fixtures;
- machine-readable schemas;
- generated checklists;
- MCU / FPGA / DSP / .NET rulebooks;
- large-scale normative rewrite.

These remain deferred until the authority model and migration evidence converge.

## v0.0.1rc1 — 2026-08-15

Initial Framework Gen2 repository-archaeology / taxonomy working draft.

### Added

- formal separation between Gen1 baseline and supplemental Crash Recorder source;
- complete 72-file Gen1 repository inventory;
- complete supplemental-source inventory;
- document-role analysis;
- concept-level Gen1 -> Gen2 mapping;
- Keep / Move / Merge / Rewrite / Retire / New disposition model;
- overlap, outdated framing, responsibility-overlap and gap analysis;
- initial system-level taxonomy proposal;
- initial Robustness & Resilience direction;
- initial Framework Scan / Applicability Analysis direction;
- read-coverage audit with unread-file declaration.

## Release Rule

RC versions remain mutable only by creating the next RC. A non-RC release is produced only after an explicit freeze decision. `v0.0.1` was frozen on 2026-08-15 from the reviewed `v0.0.1rc05` baseline; future semantic work continues on a new RC development line and does not modify v0.0.1 in place.
