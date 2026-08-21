# SCAF v0.2.0rc03 — Candidate Machine-Readable Authority Representation Foundation

**Development Release:** v0.2.0rc03  
**Development Predecessor:** v0.2.0rc02 / Git `d35789a642569ac9ea0be1938857c47e12198d33`  
**Formal Authority Release:** v0.1.0 using the frozen `294 / 218 / 76` authority representation  
**Candidate Semantic Source:** accepted v0.2.0rc01 `SCAF-OBS` overlay  
**Layer:** executable-governance representation foundation  
**Status:** Independent-review candidate; not formal authority and not yet a downstream consumer input

## 1. Why this RC exists

The accepted rc01 semantic candidate introduced five Project-Applicable Obligations:

```text
SCAF-OBS-041
SCAF-OBS-042
SCAF-OBS-043
SCAF-OBS-044
SCAF-OBS-045
```

The rc02 dependency/value assessment concluded that the next justified migration is a separately controlled machine-readable L1/L2 authority representation. That conclusion passed independent review with zero findings and `GATE: YES`.

The reviewed rc02 report consumed for this RC has SHA-256:

```text
de5173d4f707304b27e92c94b9aeae0755d955c17e846a4c155270ab8a9494cb
```

Because the initial rc02 package had an incorrect immediate Git parent, a bounded supplemental verification was completed against the corrected package. That supplemental report has SHA-256:

```text
3e85d31627ef02cf35b228480070a0f0a681e844dd06b383f8594a82256bcd1f
```

It verified the corrected development lineage:

```text
formal v0.1.0
813d722e92cd329b1a4e457304913ae9ec056731
        ↓
accepted rc01
0cfe7e02bfeb5a8f2ca5710ad7ffb6287fa9101c
        ↓
accepted rc02
 d35789a642569ac9ea0be1938857c47e12198d33
        ↓
rc03 working-tree candidate
```

rc03 therefore implements only the representation foundation authorized by rc02.

## 2. Scope

rc03 adds four representation/validation artifacts:

1. `candidate-authority-registry.yaml` — development-only 299-record authority representation;
2. `schemas/candidate-authority-registry.schema.json` — candidate-only structural contract;
3. `tools/scaf_candidate_authority_validator/` — candidate source-aware validator and bounded regression tests;
4. this controlled decision record plus navigation/release-note updates.

rc03 also closes the non-blocking packaging-hygiene observation from the rc02 lineage supplement by removing tracked Python bytecode/cache files and adding a repository `.gitignore` for generated Python cache and common local virtual-environment directories. That cleanup changes no framework authority, validator source semantics or executable-governance decision semantics.

## 3. Formal authority remains unchanged

The formal v0.1.0 authority chain is not modified.

The following remain frozen and canonical for the formal release:

```text
authority-registry.yaml
schemas/authority-registry.schema.json
tools/scaf_validator/
docs/normative/
```

The production frozen validator must continue to report:

```text
294 total authority records
218 Project-Applicable Obligations
76 Framework Normative Invariants
```

rc03 does not change those files to make them accept candidate authority.

## 4. Candidate representation model

The new candidate registry explicitly declares that it is a development candidate rather than formal authority:

```text
registry_kind: scaf_candidate_l1_l2_authority_registry
development_release: v0.2.0rc03
candidate_status: development_candidate
formal_release: v0.1.0
```

It binds the candidate representation to two repository-controlled inputs:

```text
formal registry:
  authority-registry.yaml
  SHA-256 b6ca00b44ffc280098e9feff7c7bbffa068ea3a98835fc76fa6cd13af8657692

accepted candidate source:
  docs/normative-evolution/
  80_SCAF_OBS_Observability_Diagnostics_Incident_Evidence_Obligations_v0.2.0rc01.md
  SHA-256 9fe22a3a6a7e64eac7ed8d1fb80ea95ae63c3d9a43957e8013c1daf3aa07d008
```

This makes the candidate authority-envelope inputs explicit and prevents silent rebinding to a different frozen registry or a different semantic overlay.

## 5. Inventory consequence

The candidate registry contains exactly:

```text
299 total authority records
223 Project-Applicable Obligations
76 Framework Normative Invariants
```

The arithmetic is intentionally simple:

```text
294 frozen records + 5 candidate PAOs = 299
218 frozen PAOs    + 5 candidate PAOs = 223
76 frozen FNIs     + 0               = 76
```

The count is a candidate representation fact. It is not a claim that the formal validator or formal v0.1.0 authority has changed.

## 6. Frozen projection rule

The 294 frozen records embedded in `candidate-authority-registry.yaml` are required to be exact field-for-field reproductions of the corresponding records in formal `authority-registry.yaml`.

For those 294 records, rc03 does not rewrite:

- `id`;
- `record_kind`;
- `layer`;
- `authority_class`;
- `source_path`;
- `source_anchor`;
- `source_release`;
- `representation_release`;
- `status`;
- `relations`.

This preserves the distinction:

```text
candidate representation includes frozen authority
!=
candidate representation rewrites frozen authority
```

The candidate validator rejects a candidate registry that changes any frozen record.

## 7. Candidate-only record rule

The only records that may exist beyond the frozen 294-ID set are:

```text
SCAF-OBS-041
SCAF-OBS-042
SCAF-OBS-043
SCAF-OBS-044
SCAF-OBS-045
```

Each candidate-only record is represented as:

```text
record_kind: normative_requirement
layer: l1_l2_normative_authority
authority_class: Project-Applicable Obligation
source_path: accepted rc01 OBS candidate overlay
source_release: v0.2.0rc01
representation_release: v0.2.0rc03
status: candidate_represented
relations: []
```

`source_anchor` must equal `id`.

No new Framework Normative Invariant is introduced by this representation.

## 8. Candidate source-aware validation boundary

`tools/scaf_candidate_authority_validator/validator.py` is intentionally separate from the frozen validator.

Validation order is:

```text
validate formal authority-registry.yaml using the frozen validator
        ↓
verify frozen registry SHA-256 binding
        ↓
verify accepted rc01 candidate-source SHA-256 binding
        ↓
validate candidate registry structural schema
        ↓
prove 294-record frozen projection equality
        ↓
prove candidate-only ID set == OBS-041..045
        ↓
resolve OBS-041..045 from accepted candidate Markdown headings
        ↓
verify source Target / authority class / source-anchor fidelity
        ↓
reconstruct 299 / 223 / 76 candidate inventory
```

This preserves validated-input ownership: candidate reasoning does not proceed by pretending the frozen registry already contains candidate IDs.

## 9. Candidate schema boundary

`schemas/candidate-authority-registry.schema.json` is not a replacement for the frozen authority schema.

It requires:

- exact candidate top-level identity/release state;
- exact input SHA-256 bindings;
- exact `299` record array size;
- exact expected inventory values;
- frozen-record structural semantics compatible with the accepted frozen representation;
- exactly the five accepted OBS candidate IDs for candidate-record structure;
- candidate source/release/representation/status constants;
- no record relations in this foundation.

Source-aware consistency remains validator-owned rather than being falsely claimed by structural schema alone.

## 10. Consumer boundary

The candidate registry is **not** an input to the existing Project Application chain in rc03.

rc03 does not modify:

- `schemas/project-application.schema.json`;
- `tools/scaf_project_application_validator/`;
- Effective Project Profile schema/validator/generator;
- Consumption Selection representation/schema/validator/builder;
- Context Source Association machinery;
- Controlled Context Package machinery.

Therefore:

```text
candidate authority is machine-readable and source-aware validated
!=
candidate authority is already consumable by SCAF-APP
```

A clean rc03 review authorizes only a new dependency/value assessment for whether a candidate Project Application consumption boundary now has sufficient value.

## 11. L3 / L4 / implementation boundary

rc03 does not change:

- `l3-trace-registry.yaml`;
- `docs/l3/`;
- any L3 Pattern identity or trace relation;
- `docs/l4/`;
- any L4 construction guidance;
- probe/logging APIs;
- RAM/Flash/SD/USB realization policy;
- task priorities;
- code generation;
- generic runtime-instrumentation CI enforcement.

The rc02 STOP decisions remain in force.

## 12. Machine-readable does not mean machine-decided

rc03 makes candidate authority identity and source fidelity structurally executable. It does not automate engineering judgment that the accepted L2 obligations deliberately leave with project authorities.

In particular, rc03 does not decide:

- whether temporary instrumentation is technically justified;
- whether a removal criterion is adequate;
- whether cleanup is semantically complete;
- whether an instrumented and cleaned build are materially equivalent;
- whether regression depth is sufficient;
- whether observer effect is acceptable;
- whether an observation path is operationally independent in a concrete architecture.

Those remain project design/evidence/verification decisions unless a future project-specific contract makes a bounded subset mechanically checkable.

## 13. Packaging hygiene closure

The corrected rc02 source-package lineage supplement observed generated `__pycache__` / `.pyc` files as non-blocking source-package cleanliness noise. Those files were subsequently included in the user-created rc02 Git commit.

rc03 removes those generated cache files from tracked source and adds `.gitignore` entries for:

```text
__pycache__/
*.py[cod]
.venv/
venv/
```

This is a repository-hygiene correction only. It is not an authority migration and does not change Python source behavior.

## 14. Review gate

Independent review should verify at least that:

1. formal `authority-registry.yaml`, its schema and frozen validator remain unchanged;
2. the formal frozen validator still reports `294 / 218 / 76`;
3. candidate representation reports exactly `299 / 223 / 76`;
4. all 294 frozen records are exact field-for-field projections of formal records;
5. candidate-only IDs are exactly `SCAF-OBS-041..045`;
6. candidate records resolve only against the accepted rc01 OBS overlay and preserve Target/source-anchor fidelity;
7. candidate/frozen source and release state cannot be confused;
8. candidate schema and validator remain separate from the formal frozen chain;
9. Project Application and all later consumers are unchanged and cannot silently consume the candidate registry;
10. L3/L4/tooling STOP boundaries remain preserved;
11. the packaging-hygiene cleanup removes generated bytecode without changing Python source semantics;
12. a clean rc03 review authorizes only a new dependency/value assessment, not automatic downstream migration or formal promotion.

Acceptance of rc03 means only that the candidate authority representation foundation is truthful, bounded and source-aware validated. It does not freeze or promote v0.2.0 authority.
