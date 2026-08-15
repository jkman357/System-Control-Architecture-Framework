# Gen1 Repository Inventory

## 1. Summary

- Gen1 formal baseline files discovered: **72**
- Supplemental Crash Recorder files discovered: **2**
- Gen1 files machine-read in this RC: **72 / 72**
- Supplemental files machine-read in this RC: **2 / 2**
- CI copied into SCAF: **No**

The action column describes the **SCAF artifact disposition**, not whether the underlying idea is valuable. `Retire` often means that a Gen1 path-coupled implementation artifact should not be copied; its concept may still be retained through a different SCAF authority.

## 2. Action Vocabulary

| Action | Meaning |
|---|---|
| Keep | Artifact or legal/meta role can remain substantially intact |
| Move | Concept remains but belongs under a different SCAF taxonomy branch |
| Merge | Content is useful but should be consolidated with overlapping authorities |
| Rewrite | Concept is core but current framing / responsibility model is too Gen1-specific |
| Retire | Do not carry this artifact forward as a SCAF artifact |
| New | Required SCAF capability not represented by a sufficient Gen1 artifact |

## 3. Complete Gen1 File Inventory

| # | Path | Lines | Gen1 Version | Gen1 Status | Role | SCAF Action | Reason |
|---:|---|---:|---|---|---|---|---|
| 1 | `.gitattributes` | 23 | — | — | Repository text-normalization policy | **Retire** | Do not carry repository mechanics into taxonomy RC; reintroduce later if needed. |
| 2 | `.github/CODEOWNERS` | 30 | — | — | External repository ownership enforcement map | **Retire** | Governance concept is valid; file is coupled to Gen1 repository paths and ownership. |
| 3 | `.github/REPOSITORY_PROTECTION.md` | 44 | — | — | External trust / release protection requirements | **Move** | Move concepts to SCAF Governance; do not copy path-specific controls yet. |
| 4 | `.github/workflows/document-validation.yml` | 36 | — | — | GitHub Actions validation workflow | **Retire** | No CI in v0.0.1; future tooling must follow stable SCAF contracts. |
| 5 | `CHANGELOG.md` | 271 | — | — | Gen1 revision history | **Keep** | Preserve as historical source only; SCAF has its own changelog. |
| 6 | `CONTRIBUTING.md` | 37 | — | — | Contribution and IP policy | **Rewrite** | Legal/governance intent may remain, but SCAF repository scope and contribution model must be re-established. |
| 7 | `LICENSE` | 37 | — | — | Repository legal terms | **Keep** | Carried into SCAF analysis RC unless separately changed. |
| 8 | `NOTICE.md` | 63 | — | — | Copyright, disclaimer, AI and third-party notice | **Rewrite** | Preserve legal concepts, rewrite against SCAF identity and final governance structure. |
| 9 | `README.md` | 277 | — | — | Gen1 repository entry point and document routing | **Rewrite** | SCAF requires a new system-level entry point and taxonomy. |
| 10 | `authority-registry.yaml` | 529 | — | — | Machine-readable document authority and prerequisite registry | **Merge** | Authority-registry concept is strong; rebuild after SCAF topic ownership converges. |
| 11 | `docs/coding-rules/CSharp_Coding_Rules.md` | 2397 | v1.0.5 | Baseline | Normative language and implementation authority for Product-owned C# code | **Move** | Move into Implementation Profiles; retain language-specific detail outside system core. |
| 12 | `docs/coding-rules/Embedded_C_Coding_Rules.md` | 4217 | v1.1.0-rc.1 | Draft for Review | Normative language and implementation authority for Product-owned Embedded C code | **Move** | Move into Implementation Profiles; retain language-specific detail outside system core. |
| 13 | `docs/coding-rules/README.md` | 18 | — | — | Directory index / authority-routing summary | **Retire** | SCAF will use a new taxonomy and new navigation structure. |
| 14 | `docs/coordinator/Coordinator_Architecture_Patterns.md` | 663 | v1.1.1 | Baseline | Topic-specific normative engineering authority for Coordinator architecture patterns, subordinate to Coordinator Software Engineering Rules | **Merge** | Generalize Coordinator-specific rules into Node Role/Profile concerns; preserve UI-only specialization where useful. |
| 15 | `docs/coordinator/Coordinator_Concurrency_Guide.md` | 496 | v1.1.0 | Draft for Review | Proposed topic-specific normative engineering authority for Coordinator concurrency, subordinate to Coordinator Software Engineering Rules | **Merge** | Generalize Coordinator-specific rules into Node Role/Profile concerns; preserve UI-only specialization where useful. |
| 16 | `docs/coordinator/Coordinator_Logging_Guide.md` | 541 | v1.1.1 | Draft for Review | Proposed topic-specific normative engineering authority for Coordinator logging implementation, subordinate to Coordinator Software Engineering Rules | **Merge** | Generalize Coordinator-specific rules into Node Role/Profile concerns; preserve UI-only specialization where useful. |
| 17 | `docs/coordinator/Coordinator_Software_Engineering_Rules.md` | 1841 | v1.1.1 | Baseline | Normative engineering authority for Coordinator-owned software | **Merge** | Generalize Coordinator-specific rules into Node Role/Profile concerns; preserve UI-only specialization where useful. |
| 18 | `docs/coordinator/Coordinator_Testing_Guide.md` | 678 | v1.1.1 | Draft for Review | Proposed topic-specific normative engineering authority for Coordinator engineering tests, subordinate to Coordinator Software Engineering Rules | **Merge** | Generalize Coordinator-specific rules into Node Role/Profile concerns; preserve UI-only specialization where useful. |
| 19 | `docs/coordinator/Coordinator_UI_Engineering_Guide.md` | 638 | v1.1.2 | Baseline | Topic-specific normative engineering authority for Coordinator UI implementation, subordinate to Coordinator Software Engineering Rules | **Merge** | Generalize Coordinator-specific rules into Node Role/Profile concerns; preserve UI-only specialization where useful. |
| 20 | `docs/coordinator/README.md` | 20 | — | — | Coordinator document index / authority summary | **Retire** | Coordinator is no longer a top-level SCAF document domain. |
| 21 | `docs/framework/AI_Engineering_Usage_Guide.md` | 1358 | v1.1.4-rc.1 | Draft for Review | Normative AI task-routing and repository-governance authority | **Move** | Move under Engineering Governance / AI-assisted engineering; keep subordinate to core system framework. |
| 22 | `docs/framework/Coordinator_Node_Control_Framework.md` | 3227 | v1.1.7 | Baseline | Normative architecture and framework-governance authority | **Rewrite** | Primary concept donor; replace Coordinator/embedded framing with System/Node/Role taxonomy and resilience lifecycle. |
| 23 | `docs/framework/Framework_Application_Analysis_Template.md` | 2849 | v1.1.9 | Baseline | Normative framework-application analysis method | **Rewrite** | Evolve into SCAF Framework Scan / Applicability Analysis and project decision/evidence model. |
| 24 | `docs/framework/README.md` | 15 | — | — | Framework document index / authority summary | **Retire** | Replaced by the SCAF repository entry point and system-level taxonomy. |
| 25 | `docs/node/Node_Software_Engineering_Rules.md` | 524 | v1.1.0 | Draft for Review | Proposed normative engineering authority for Node-owned software realization | **Rewrite** | Generalize software-only Node rules to heterogeneous Node engineering plus implementation profiles. |
| 26 | `docs/node/README.md` | 26 | — | — | Node document index / reading order | **Retire** | Node remains a core concept but not as a standalone Gen1 directory authority. |
| 27 | `docs/protocol/Protocol_Compatibility_Rules.md` | 367 | v1.1.0 | Draft for Review | Proposed normative Protocol compatibility and evolution authority shared by Coordinator and Node implementations | **Move** | Preserve protocol concept under Interface & Data Contract taxonomy; remove fixed Coordinator/Node assumptions. |
| 28 | `docs/protocol/Protocol_Registry_Governance.md` | 350 | v1.1.0 | Draft for Review | Proposed normative Protocol identifier Registry and allocation-governance authority shared by Coordinator and Node implementations | **Move** | Preserve protocol concept under Interface & Data Contract taxonomy; remove fixed Coordinator/Node assumptions. |
| 29 | `docs/protocol/Protocol_Security_Profile.md` | 418 | v1.1.0 | Draft for Review | Proposed normative Protocol security-profile and secure-session governance authority shared by Coordinator and Node implementations | **Move** | Preserve protocol concept under Interface & Data Contract taxonomy; remove fixed Coordinator/Node assumptions. |
| 30 | `docs/protocol/Protocol_YAML_Definition_Guide.md` | 3399 | v1.1.7 | Baseline | Normative Protocol YAML syntax, semantics, machine-verifiable representation, validation, and Code Generation authority | **Move** | Preserve protocol concept under Interface & Data Contract taxonomy; remove fixed Coordinator/Node assumptions. |
| 31 | `docs/protocol/Protocol_YAML_Template.md` | 3916 | v1.1.1 | Baseline | Normative reusable Protocol YAML template authority | **Merge** | Keep reusable protocol contract structure, but reduce duplication with definition guide and move to Interface Contract profile. |
| 32 | `docs/protocol/README.md` | 19 | — | — | Protocol document index / authority summary | **Retire** | Protocol becomes part of the broader Interface & Data Contract taxonomy. |
| 33 | `docs/validation/AI_Generated_Artifact_Validation_Guide.md` | 365 | v1.1.0 | Draft for Review | Proposed operational AI-artifact validation method; not an independent Product, architecture, Protocol, role, coding, safety, security, or compliance authority | **Merge** | Merge checklist-specific obligations into a unified verification/evidence model; regenerate focused checklists later. |
| 34 | `docs/validation/Coding_Rules_Review_Checklist.md` | 145 | v1.0.1-rc.1 | Draft for Review | Proposed operational common Coding Rules review checklist; not an independent language or Product requirement authority | **Merge** | Merge checklist-specific obligations into a unified verification/evidence model; regenerate focused checklists later. |
| 35 | `docs/validation/Framework_Conformance_Checklist.md` | 172 | v1.1.5 | Draft for Review | Proposed operational Framework conformance checklist; not an independent architecture or Product requirement authority | **Merge** | Merge checklist-specific obligations into a unified verification/evidence model; regenerate focused checklists later. |
| 36 | `docs/validation/Protocol_Validation_Checklist.md` | 205 | v1.1.6 | Draft for Review | Proposed operational Protocol conformance checklist; not an independent Protocol or Product requirement authority | **Merge** | Merge checklist-specific obligations into a unified verification/evidence model; regenerate focused checklists later. |
| 37 | `docs/validation/README.md` | 64 | — | — | Validation document index / reading order | **Retire** | Validation is reorganized under unified Verification, Fault Injection & Evidence. |
| 38 | `docs/validation/Repository_Validation_Checklist.md` | 188 | v1.1.3 | Baseline | Operational validation method; not a Product or architecture authority | **Merge** | Merge checklist-specific obligations into a unified verification/evidence model; regenerate focused checklists later. |
| 39 | `docs/validation/Validation_Evidence_Guide.md` | 389 | v1.1.0 | Draft for Review | Proposed operational validation-evidence method; not a Product, architecture, Protocol, role, or language authority | **Merge** | Elevate evidence model into SCAF Verification & Evidence, integrated with incident evidence and applicability decisions. |
| 40 | `examples/framework-conformance-claim.yaml` | 56 | — | — | Machine-readable conformance claim example | **Rewrite** | Concept remains; data model must reflect SCAF applicability and evidence taxonomy. |
| 41 | `legal-baseline.yaml` | 31 | — | — | Legal baseline digest / external-anchor state | **Move** | Move under later Governance/tooling; defer machine enforcement. |
| 42 | `requirements-validation.txt` | 30 | — | — | Pinned Python dependencies for validators | **Retire** | Validator implementation detail; not part of taxonomy RC. |
| 43 | `schema/framework-conformance-claim.schema.yaml` | 170 | — | — | Schema for conformance claims | **Rewrite** | Defer until Framework Scan/conformance model is stable. |
| 44 | `schema/protocol.schema.yaml` | 223 | — | — | Executable protocol schema subset | **Rewrite** | Protocol contract remains, but schema must align with SCAF interface taxonomy. |
| 45 | `tests/fixtures/protocol/invalid_address_reuse_session.yaml` | 57 | — | — | Positive/negative protocol semantic-validation fixture | **Retire** | Defer fixture migration until executable-invariant extraction and a stable machine-readable contract exist; preserve scenario intent for later donor audit. |
| 46 | `tests/fixtures/protocol/invalid_boolean_string.yaml` | 57 | — | — | Positive/negative protocol semantic-validation fixture | **Retire** | Defer fixture migration until executable-invariant extraction and a stable machine-readable contract exist; preserve scenario intent for later donor audit. |
| 47 | `tests/fixtures/protocol/invalid_bounded_parallel_update.yaml` | 57 | — | — | Positive/negative protocol semantic-validation fixture | **Retire** | Defer fixture migration until executable-invariant extraction and a stable machine-readable contract exist; preserve scenario intent for later donor audit. |
| 48 | `tests/fixtures/protocol/invalid_broadcast_response_policy.yaml` | 57 | — | — | Positive/negative protocol semantic-validation fixture | **Retire** | Defer fixture migration until executable-invariant extraction and a stable machine-readable contract exist; preserve scenario intent for later donor audit. |
| 49 | `tests/fixtures/protocol/invalid_explicit_blank_core_profile.yaml` | 57 | — | — | Positive/negative protocol semantic-validation fixture | **Retire** | Defer fixture migration until executable-invariant extraction and a stable machine-readable contract exist; preserve scenario intent for later donor audit. |
| 50 | `tests/fixtures/protocol/invalid_explicit_empty_core_profile.yaml` | 46 | — | — | Positive/negative protocol semantic-validation fixture | **Retire** | Defer fixture migration until executable-invariant extraction and a stable machine-readable contract exist; preserve scenario intent for later donor audit. |
| 51 | `tests/fixtures/protocol/invalid_group_session_without_profile.yaml` | 57 | — | — | Positive/negative protocol semantic-validation fixture | **Retire** | Defer fixture migration until executable-invariant extraction and a stable machine-readable contract exist; preserve scenario intent for later donor audit. |
| 52 | `tests/fixtures/protocol/invalid_identity_conflict_policy.yaml` | 57 | — | — | Positive/negative protocol semantic-validation fixture | **Retire** | Defer fixture migration until executable-invariant extraction and a stable machine-readable contract exist; preserve scenario intent for later donor audit. |
| 53 | `tests/fixtures/protocol/invalid_legacy_empty_profile.yaml` | 13 | — | — | Positive/negative protocol semantic-validation fixture | **Retire** | Defer fixture migration until executable-invariant extraction and a stable machine-readable contract exist; preserve scenario intent for later donor audit. |
| 54 | `tests/fixtures/protocol/invalid_maximum_nodes_zero.yaml` | 57 | — | — | Positive/negative protocol semantic-validation fixture | **Retire** | Defer fixture migration until executable-invariant extraction and a stable machine-readable contract exist; preserve scenario intent for later donor audit. |
| 55 | `tests/fixtures/protocol/invalid_multi_target_partial_failure.yaml` | 57 | — | — | Positive/negative protocol semantic-validation fixture | **Retire** | Defer fixture migration until executable-invariant extraction and a stable machine-readable contract exist; preserve scenario intent for later donor audit. |
| 56 | `tests/fixtures/protocol/invalid_scope_typo.yaml` | 57 | — | — | Positive/negative protocol semantic-validation fixture | **Retire** | Defer fixture migration until executable-invariant extraction and a stable machine-readable contract exist; preserve scenario intent for later donor audit. |
| 57 | `tests/fixtures/protocol/invalid_shared_bus_without_addressing.yaml` | 57 | — | — | Positive/negative protocol semantic-validation fixture | **Retire** | Defer fixture migration until executable-invariant extraction and a stable machine-readable contract exist; preserve scenario intent for later donor audit. |
| 58 | `tests/fixtures/protocol/valid_legacy_single_node.yaml` | 24 | — | — | Positive/negative protocol semantic-validation fixture | **Retire** | Defer fixture migration until executable-invariant extraction and a stable machine-readable contract exist; preserve scenario intent for later donor audit. |
| 59 | `tests/fixtures/protocol/valid_multi_independent.yaml` | 58 | — | — | Positive/negative protocol semantic-validation fixture | **Retire** | Defer fixture migration until executable-invariant extraction and a stable machine-readable contract exist; preserve scenario intent for later donor audit. |
| 60 | `tests/fixtures/protocol/valid_multi_shared_bus.yaml` | 57 | — | — | Positive/negative protocol semantic-validation fixture | **Retire** | Defer fixture migration until executable-invariant extraction and a stable machine-readable contract exist; preserve scenario intent for later donor audit. |
| 61 | `tests/fixtures/protocol/valid_routed_gateway.yaml` | 58 | — | — | Positive/negative protocol semantic-validation fixture | **Retire** | Defer fixture migration until executable-invariant extraction and a stable machine-readable contract exist; preserve scenario intent for later donor audit. |
| 62 | `tests/fixtures/protocol/valid_single_node.yaml` | 57 | — | — | Positive/negative protocol semantic-validation fixture | **Retire** | Defer fixture migration until executable-invariant extraction and a stable machine-readable contract exist; preserve scenario intent for later donor audit. |
| 63 | `tests/fixtures/protocol_expectations.yaml` | 38 | — | — | Expected validator outcomes for protocol fixtures | **Retire** | Tool/test implementation deferred until SCAF schemas stabilize. |
| 64 | `tests/test_security_regressions.py` | 297 | — | — | Regression tests for Gen1 validation/tooling behavior | **Retire** | No test-tool migration in taxonomy RC; mine required invariants before rebuilding. |
| 65 | `tests/test_validate_protocol.py` | 101 | — | — | Regression tests for Gen1 validation/tooling behavior | **Retire** | No test-tool migration in taxonomy RC; mine required invariants before rebuilding. |
| 66 | `tests/test_validate_repository.py` | 596 | — | — | Regression tests for Gen1 validation/tooling behavior | **Retire** | No test-tool migration in taxonomy RC; mine required invariants before rebuilding. |
| 67 | `tests/test_verify_external_anchor.py` | 102 | — | — | Regression tests for Gen1 validation/tooling behavior | **Retire** | No test-tool migration in taxonomy RC; mine required invariants before rebuilding. |
| 68 | `third-party-evidence/README.md` | 5 | — | — | Third-party evidence storage guidance | **Move** | Retain evidence concept under Governance; repository layout deferred. |
| 69 | `third-party-materials.yaml` | 13 | — | — | Third-party material registry | **Move** | Retain governance concept; machine format deferred. |
| 70 | `tools/validate_protocol.py` | 648 | — | — | Gen1 repository/protocol/external-anchor validation tool | **Retire** | Tool implementation is path/schema coupled; rebuild later from stable SCAF contracts. |
| 71 | `tools/validate_repository.py` | 1674 | — | — | Gen1 repository/protocol/external-anchor validation tool | **Retire** | Tool implementation is path/schema coupled; rebuild later from stable SCAF contracts. |
| 72 | `tools/verify_external_anchor.py` | 246 | — | — | Gen1 repository/protocol/external-anchor validation tool | **Retire** | Tool implementation is path/schema coupled; rebuild later from stable SCAF contracts. |


## 4. Supplemental Source Inventory

| # | Path | Lines | Version / Status | Role | SCAF Action |
|---:|---|---:|---|---|---|
| 1 | `README.md` | 4954 | v1.0.1rc03 / Specification RC | Incident evidence, first-abnormal-state, survivability, persistence, recovery, recorder self-protection, observer-effect and implementation contract | **Merge** into `SCAF-ROB` / `SCAF-OBS` / `SCAF-ASSUR`; keep recorder implementation details subordinate |
| 2 | `LICENSE` | legal text | — | Legal terms | **Retire**; retain as supplemental-source provenance only; SCAF uses its own repository license |

## 5. Inventory Observation

Gen1 is already more than a Host/Device communication framework. It contains a substantial architecture, protocol, multi-node, update, security, concurrency, validation, evidence, AI-engineering and repository-governance system. The principal SCAF problem is therefore **not lack of content**. The problem is that content is distributed across role-specific, language-specific, protocol-specific, validation-specific and repository-specific authorities that grew around the Gen1 Coordinator/Node structure.

SCAF should extract and re-home the durable concepts rather than reproducing the same folder graph with broader names.
