# SCAF v0.0.6rc03 — SCAF-APP Project Application Record Basis-Role and State-Compatibility Hardening

**Development Release:** v0.0.6rc03  
**Status:** Canonical Record Model Finding Closure / Review Candidate  
**Date:** 2026-08-18  
**Upstream Frozen Baselines:** v0.0.2 L1/L2; v0.0.3 L3; v0.0.4 Executable Governance; v0.0.5 L3 Machine-Readable Traceability  
**Accepted Development Basis:** v0.0.6rc01 SCAF-APP semantic foundation  
**Immediate Predecessor:** v0.0.6rc02 canonical logical record model  
**Review Findings Addressed:** `SCAF-RC02-001` (Major), `SCAF-RC02-002` (Minor)

## 1. Decision Purpose

The independent v0.0.6rc02 review preserved all frozen baselines and accepted most of the canonical logical record structure, but returned:

```text
Critical: 0
Major:    1
Minor:    1
Trivial:  0

V0.0.6RC02 SCAF-APP CANONICAL PROJECT APPLICATION RECORD MODEL GATE: NO
```

The review identified two bounded determinism gaps:

1. `SCAF-RC02-001` — reference roles were not sufficiently qualified to determine which references directly constitute the applicability disposition basis;
2. `SCAF-RC02-002` — the allowed-state semantics of `unresolved_reason` and `awaiting_refs` were deferred rather than frozen.

v0.0.6rc03 closes only those findings. It does not advance to concrete serialization, JSON Schema, validator implementation, project-scope resolution, automated applicability inference, Effective Project Profile generation, CI applicability-completion enforcement, new L3 work, or L4 guidance.

## 2. Preserved rc01 / rc02 Contract

Unless explicitly refined below, rc03 preserves the accepted rc01 semantic boundary and the unaffected rc02 canonical record model.

The Project Application Record remains a project-side applicability disposition / trace surface. It is not:

- SCAF normative authority;
- Project Design Authority;
- the underlying Controlled Decision when owned elsewhere;
- deviation/risk/verification/evidence/closure authority;
- a Pattern-selection authority;
- a project-completion PASS/FAIL record.

The initial record domain remains the frozen 218 Project-Applicable Obligations. Framework Normative Invariants remain outside the Project Application Record target domain.

The initial applicability tokens remain:

```text
applicable
not_applicable
undetermined
```

`undetermined` remains a legitimate engineering-unresolved state and is not representation invalidity merely because the engineering question is still open.

## 3. Finding SCAF-RC02-001 Closure — Direct Basis Qualification

### 3.1 Canonical rule

For the current applicability disposition, **only** the following `disposition_basis` members may satisfy applicability-basis sufficiency:

```text
disposition_basis.summary
disposition_basis.basis_refs
```

The mere presence of any of the following does **not** satisfy the applicability-basis requirement:

```text
decision_refs
authority_refs
supporting_refs
```

This rule is state-independent for `applicable` and `not_applicable` and prevents a later serializer/schema/validator from inventing its own basis-role qualification rule.

### 3.2 `disposition_basis.summary`

`summary` is project-controlled rationale text that directly explains or states the basis for the **current applicability disposition**.

When present, it is an applicability-basis element rather than generic project commentary.

It does not become Project Design Authority merely because it records rationale.

### 3.3 `disposition_basis.basis_refs`

`basis_refs` are controlled references whose semantic role is specifically:

> **directly establish, justify, or substantively support the current applicability disposition for the declared project scope.**

A reference belongs in `basis_refs` only when the referenced controlled source is part of the direct basis for deciding that the SCAF obligation is `applicable`, `not_applicable`, or remains `undetermined` for the declared scope.

Examples of sources that may qualify when they directly support the applicability disposition include:

- controlled scope/boundary definitions;
- applicable external-authority inputs;
- controlled architecture/interface facts;
- controlled analyses establishing relevance or non-relevance;
- controlled decisions whose subject is the applicability judgment itself.

The referenced artifact type does not determine the role. The role is determined by whether that controlled source directly supports the current applicability disposition.

### 3.4 `decision_refs`

`decision_refs` remain trace references to project-controlled decisions/judgments relevant to applicability or required downstream project determinations.

They do not satisfy applicability-basis sufficiency merely by existing.

A decision artifact that directly forms part of the applicability basis may be referenced through `basis_refs`. If project traceability separately requires that same controlled decision to be exposed on the `decision_refs` surface, the same controlled target may appear in both role-specific reference surfaces. Such repeated targeting represents distinct semantic roles; it is not duplicate applicability authority.

A downstream realization/design/verification decision that does not directly justify the applicability disposition belongs in `decision_refs` only and cannot make an otherwise unsupported applicability assertion valid.

### 3.5 `authority_refs`

`authority_refs` identify project-governed authority roles/artifacts that own or approve relevant judgment.

They provide authority provenance. They do **not** directly establish why an obligation is applicable or not applicable and do not satisfy applicability-basis sufficiency merely by existing.

Authority ownership and applicability basis therefore remain distinct concepts:

```text
why this disposition is supportable
        !=
who owns / approves the judgment
```

### 3.6 `supporting_refs`

`supporting_refs` identify controlled related context that is useful to understand, navigate, or review the Project Application Record but does not, by its assigned role, directly constitute the applicability basis.

They may include related architecture, interface, verification planning, safety/security/risk analysis, external requirements, system context, or other controlled sources.

A source that directly justifies the applicability disposition shall be classified as `basis_refs` for that direct-basis role rather than relying on `supporting_refs` to satisfy basis sufficiency.

`supporting_refs` do not independently satisfy mandatory applicability-basis requirements.

### 3.7 Same source used in multiple roles

The same controlled target may appear on more than one reference surface only when it genuinely fulfills each named role.

For example:

```text
Controlled architecture decision D-17
    ├─ basis_refs      -> D-17 directly establishes applicability for scope N2
    └─ decision_refs   -> D-17 is also the controlled project decision artifact
```

This is role-explicit reuse, not arbitrary placement.

A consumer shall not infer that a source is direct applicability basis merely because the same target appears in `decision_refs`, `authority_refs`, or `supporting_refs`.

## 4. Revised State-Dependent Basis Sufficiency

### 4.1 `applicable`

For:

```text
applicability: applicable
```

at least one of the following shall be present and meaningful:

```text
disposition_basis.summary
disposition_basis.basis_refs
```

`decision_refs`, `authority_refs`, and `supporting_refs` may be present for their defined roles but cannot replace the required direct basis.

`applicable` still does not imply Pattern selection, implementation, satisfaction, compliance, verification, or closure.

### 4.2 `not_applicable`

For:

```text
applicability: not_applicable
```

at least one of the following shall be present and meaningful:

```text
disposition_basis.summary
disposition_basis.basis_refs
```

A bare `not_applicable` assertion remains invalid under the canonical logical contract.

The record shall additionally preserve enough project-controlled provenance to make ownership/approval of the judgment reviewable. That provenance may be carried by appropriate `authority_refs`, `decision_refs`, or by a directly referenced controlled basis source whose ownership is defined under the project governance model.

This provenance rule does not change the direct-basis qualification rule: authority or decision provenance alone cannot substitute for `summary` or `basis_refs`.

### 4.3 `undetermined`

For:

```text
applicability: undetermined
```

`disposition_basis.unresolved_reason` is required.

`disposition_basis.basis_refs` may identify controlled facts/inputs that directly explain why applicability remains unresolved. `disposition_basis.summary` may provide additional current-disposition rationale but does not replace the required `unresolved_reason`.

`disposition_basis.awaiting_refs` may identify controlled pending/missing inputs, decisions, authority assignments, or scope definitions expected to resolve the applicability question.

The record shall not invent a project decision merely to eliminate the unresolved state.

## 5. Finding SCAF-RC02-002 Closure — State Compatibility Matrix

The current-state semantics of all four `disposition_basis` members are frozen as follows:

| `disposition_basis` member | `applicable` | `not_applicable` | `undetermined` |
|---|---|---|---|
| `summary` | allowed; may satisfy direct basis | allowed; may satisfy direct basis | allowed; supplementary only; does not replace `unresolved_reason` |
| `basis_refs` | allowed; may satisfy direct basis | allowed; may satisfy direct basis | allowed; may identify controlled basis for why state remains unresolved |
| `unresolved_reason` | **prohibited** | **prohibited** | **required exactly once** |
| `awaiting_refs` | **prohibited** | **prohibited** | allowed 0..n |

These are semantic rules of the canonical logical record model, not implementation choices left to a future schema.

A later serializer/schema/validator may encode these rules but shall not redefine them.

## 6. Current State Versus Historical State

`disposition_basis` represents the basis of the **current** applicability disposition.

Once an `undetermined` record is resolved to `applicable` or `not_applicable`:

- `unresolved_reason` shall no longer be present in the current-state record;
- `awaiting_refs` shall no longer be present in the current-state record.

If the project needs to retain prior unresolved history, superseded basis, or re-evaluation history, that information belongs to a separately reviewed history/supersession/re-evaluation representation.

rc03 does not introduce such a history model.

A future implementation shall not overload the current-state fields to retain historical unresolved data.

## 7. Representation-Invalid Conditions Authorized After rc03

Subject to a later reviewed concrete serialization, the canonical logical contract authorizes a schema/validator to treat the following basis-related conditions as representation/contract invalidity:

- `applicable` with neither a meaningful `disposition_basis.summary` nor at least one `disposition_basis.basis_refs` entry;
- `not_applicable` with neither a meaningful `disposition_basis.summary` nor at least one `disposition_basis.basis_refs` entry;
- `undetermined` without exactly one `disposition_basis.unresolved_reason`;
- `unresolved_reason` present when applicability is `applicable` or `not_applicable`;
- `awaiting_refs` present when applicability is `applicable` or `not_applicable`;
- treating `decision_refs`, `authority_refs`, or `supporting_refs` alone as sufficient direct applicability basis;
- malformed or unresolvable controlled references once a separately reviewed reference-resolution contract exists.

These representation/contract conditions remain distinct from legitimate engineering-unresolved state.

For example:

```text
applicability: undetermined
unresolved_reason: controlled scope ownership is not yet decided
```

may be a valid Project Application Record even though the underlying engineering question remains open.

## 8. Negative Semantic Conditions

A conforming later serializer/schema/validator/query/AI consumer shall not infer:

```text
decision_refs present
    -> applicability basis exists

authority_refs present
    -> applicability basis exists

supporting_refs present
    -> applicability basis exists

applicable
    -> selected / implemented / satisfied / compliant / verified / closed

not_applicable
    -> obligation deleted / weakened / tailored / waived

undetermined
    -> malformed / failed / non-compliant

resolved current state
    -> historical unresolved fields may remain in current-state basis
```

The frozen v0.0.5 L2↔L3 trace boundary also remains unchanged:

```text
No L3 Pattern -> project failure        [not authorized]
L3 Pattern exists -> applicable         [not authorized]
primary candidate -> Pattern selected   [not authorized]
```

## 9. No New Authority Transfer

This finding closure does not transfer engineering authority to machine-readable representation or tooling.

Tools may later determine contract facts such as:

- whether direct-basis fields are present where required;
- whether unresolved-only members occur in compatible states;
- whether referenced identities resolve under an accepted reference contract.

Tools shall not determine, merely from those structural facts, whether the engineering judgment itself is correct.

The project remains responsible for the underlying engineering judgment and authority approval.

## 10. Frozen Baseline Preservation

rc03 changes no frozen normative/L3 source and no frozen executable-governance implementation.

The following remain unchanged:

- `docs/normative/`;
- `docs/l3/`;
- `authority-registry.yaml`;
- `l3-trace-registry.yaml`;
- `schemas/`;
- `tools/scaf_validator/`;
- `tools/scaf_trace_validator/`;
- `tools/scaf_trace_views/`;
- `tools/scaf_release_integrity/`;
- `tools/scaf_external_pin/`;
- `tools/scaf_ci_gate/`;
- `.github/workflows/`;
- `release-integrity/`.

The formal v0.0.5 baseline remains immutable.

## 11. Deferred Scope

rc03 does not introduce or pre-authorize:

- a concrete `project-application.yaml` / JSON dataset;
- JSON Schema or another serialization schema;
- a Project Application validator;
- a project-scope registry/resolver;
- canonical reference-object syntax or locator grammar;
- a history/supersession/re-evaluation model;
- full decision/deviation/risk/verification/evidence/closure state serialization;
- tailoring taxonomy;
- automatic applicability classification;
- AI approval of project judgments;
- Pattern recommendation/selection;
- Effective Project Profile generation;
- context resolver/packaging;
- CI applicability-completion enforcement;
- code generation;
- new L3 Patterns;
- L4 guidance.

The next development step remains review-driven. A clean rc03 review may authorize consideration of concrete serialization, but rc03 itself does not pre-select the serialization design.

## 12. Acceptance Conditions for rc03 Review

rc03 is ready to progress only if independent review confirms all of the following:

1. `SCAF-RC02-001` is closed because direct applicability-basis qualification is deterministic;
2. `decision_refs`, `authority_refs`, and `supporting_refs` cannot satisfy basis sufficiency merely by presence;
3. `basis_refs` has a distinct direct-basis role from `supporting_refs`;
4. same-target multi-role references are semantically explicit rather than arbitrary placement;
5. `SCAF-RC02-002` is closed by an explicit allowed-state matrix;
6. `unresolved_reason` and `awaiting_refs` are prohibited outside `undetermined` current state;
7. resolved current-state records do not retain unresolved-only members as historical storage;
8. representation invalidity remains distinct from engineering-unresolved work;
9. Project Design Authority and other project authority ownership remain unchanged;
10. no concrete serialization/schema/validator/L4 capability is introduced;
11. all frozen baseline integrity and accepted regression checks remain unchanged and passing.

A clean review closes the rc02 findings only. It does not freeze v0.0.6.
