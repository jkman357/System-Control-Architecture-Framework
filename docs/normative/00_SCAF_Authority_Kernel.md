# SCAF Authority Kernel

**Release:** v0.0.2rc09  
**Layer:** L1 Authority Kernel  
**Status:** Normative RC

## 1. Purpose

This document defines the normative authority grammar used by System Control Architecture Framework (SCAF) L1/L2 content. It preserves the frozen v0.0.1 architecture baseline while distinguishing framework-side semantics from project-side decisions, realization, verification, closure and trace.

This document does **not** reopen the frozen top-level taxonomy or core metamodel.

## 2. Normative Targets and Keywords

SCAF normative statements have an explicit **target class**.

### 2.1 Project-Applicable Obligation

A **Project-Applicable Obligation** applies to a project when the obligation is Applicable through SCAF Project Application / Framework Scan.

For Project-Applicable Obligations:

- **SHALL** — mandatory when Applicable;
- **SHOULD** — expected unless a controlled rationale/deviation is recorded;
- **MAY** — permitted option.

A Project-Applicable Obligation is expected to map, where relevant, to project applicability, consequence, decision, authority, Applicable Satisfaction Basis, verification, evidence, closure and re-evaluation trace.

### 2.2 Framework Normative Invariant

A **Framework Normative Invariant** constrains SCAF normative content, framework governance, migration/promotion behavior or authoring semantics. It is not itself a project architecture obligation and is not required to map to a Project Design Authority or project Framework Scan item.

A requirement identifier may be retained for traceability, but its target class shall remain explicit.

### 2.3 Requirement ID stability

Requirement identifiers are intended to remain stable across RCs where practical, but may change before a future normative freeze when splitting a compound obligation or correcting its target class is necessary to preserve authority semantics.

## 3. Authority Vocabulary

### 3.1 SCAF Concern Authority

A **SCAF Concern Authority** is the framework-side normative authority for a defined architecture concern. It **Defines Framework Semantics / Obligation** for that concern.

It does **not** define the actual project-specific topology, threshold, allocation, boundary, selected mechanism or implementation choice.

### 3.2 Project Design Authority

A **Project Design Authority (PDA)** is the designated project-side authority role responsible for a specific project architecture decision.

The PDA **Defines Project Instance / Decision** for the project-specific value needed to satisfy applicable SCAF obligations and other project constraints.

### 3.3 Controlled Decision

A **Controlled Decision** is the project-specific architecture decision made by a designated authority role. Examples include a Node boundary, service allocation, timing threshold, trust boundary or selected lifecycle strategy.

### 3.4 Authoritative Artifact

An **Authoritative Artifact** records one or more Controlled Decisions. Examples include an architecture specification, interface contract, controlled configuration decision, hazard-derived constraint record or equivalent project artifact.

An artifact is not automatically the authority role that owns or approves the recorded decision.

### 3.5 Project Realization

**Project Realization** is the project-side implementation responsibility/activity and resulting implementation artifacts that realize Project Design Authority decisions.

Project Realization is not a SCAF framework plane and is not equivalent to `SCAF-PROF`.

### 3.6 Project Verification / Assurance Authority

A **Project Verification / Assurance Authority** is the project-side role that executes/evaluates required verification, applies applicable assurance/evidence rules and determines whether project evidence is sufficient for the verification claim under project governance.

It is not equivalent to `SCAF-ASSUR` and does not acquire underlying requirement, design, risk-acceptance, deviation, or other underlying closure authority merely because it evaluates evidence.

### 3.7 SCAF-PROF

`SCAF-PROF` is framework-side realization/profile content. It may **Define Framework Semantics / Obligation**, **Constrain** or **Guide Realization** through profile semantics, compatibility rules, candidate patterns or technology-specific guidance.

`SCAF-PROF` does **not** itself Realize a project design decision. Project Realization performs the actual realization.

### 3.8 SCAF-ASSUR

`SCAF-ASSUR` is framework-side assurance authority. It **Defines Framework Semantics / Obligation** for verification method classes, coverage semantics, evidence properties and evidence-sufficiency criteria.

`SCAF-ASSUR` does **not** perform project verification, determine whether a particular project's evidence is sufficient, define project thresholds or own underlying project closure.

### 3.9 SCAF-APP

`SCAF-APP` is the framework-side Project Application / Framework Scan authority. It **Defines Framework Semantics / Obligation** for applicability/disposition/trace semantics.

A project Framework Scan record **Dispositions / Traces** project state. It does not become SCAF normative authority, Project Design Authority, risk-acceptance authority, verification authority or closure authority.

### 3.10 External Authorities

External/project authorities such as safety, security, regulatory or risk authorities may define constraints, objectives, assumptions, requirements or acceptance decisions in their own scope.

A design-prescriptive external constraint remains an external-authority input to the Applicable Satisfaction Basis. The Project Design Authority integrates that constraint into the project architecture decision.

A project-side role acts as Project Design Authority for a decision only when project governance explicitly assigns that architecture decision authority to the role. The specificity of an external constraint alone does not convert the external authority into the PDA.

## 4. Canonical Authority Chain

```text
SCAF Concern Authority
    Defines Framework Semantics / Obligation
        ↓
Project Design Authority
    Defines Project Instance / Controlled Decision
        ↓
Project Realization
    Realizes the Controlled Decision
        ↓
Project Verification / Assurance Authority
    Verifies against the Applicable Satisfaction Basis

SCAF-APP cross-cuts the chain by Dispositioning / Tracing
applicability, decision, deviation, risk, verification obligation,
verification result/state, evidence, closure and re-evaluation state.

SCAF-PROF may Constrain / Guide Realization.
`SCAF-ASSUR` **Defines Framework Semantics / Obligation** for the verification/evidence semantics used
by Project Verification / Assurance Authority.
```

External authorities Constrain the project through their own controlled inputs; they do not create a competing SCAF architecture chain.

## 5. Project-Applicable Authority Obligations

### `SCAF-AK-001` — Framework and project authority separation

**Target:** Project-Applicable Obligation

For each Applicable SCAF obligation that requires a project-specific architecture value or decision, the project **SHALL** identify the Project Design Authority responsible for that decision.

A universal SCAF invariant may constrain or eliminate a degree of project choice, but that invariant **SHALL NOT** be interpreted as making the SCAF concern the project-side design authority for any remaining project instance/value.

### `SCAF-AK-002` — Authority role, decision and artifact separation

**Target:** Project-Applicable Obligation

The project **SHALL** distinguish:

1. the authority role that owns a decision;
2. the Controlled Decision itself; and
3. the Authoritative Artifact that records the decision.

A document, record, schema or tool **SHALL NOT** be treated as the decision authority merely because it stores the decision. A Framework Scan or equivalent project-application record **SHALL NOT** replace the Authoritative Artifact or Project Design Authority.

### `SCAF-AK-003` — Project Application state dimensions

**Target:** Project-Applicable Obligation

A Framework Scan or equivalent `SCAF-APP` record **SHALL** keep the following project dimensions distinguishable when applicable:

- applicability state;
- decision state;
- deviation state;
- risk state;
- verification obligation;
- verification execution/result state;
- evidence state;
- closure state; and
- re-evaluation trigger/trace.

### `SCAF-AK-004` — Project Realization separation from SCAF-PROF

**Target:** Project-Applicable Obligation

Project Realization **SHALL** remain the project-side responsibility/activity that implements the Controlled Decision.

Applicable `SCAF-PROF` content **MAY** Constrain or Guide Realization, but the project **SHALL NOT** represent that framework-side content as the project realization actor.

### `SCAF-AK-005` — Project verification separation from SCAF-ASSUR

**Target:** Project-Applicable Obligation

The project **SHALL** designate the Project Verification / Assurance Authority role(s) that execute/evaluate required verification and apply applicable evidence-sufficiency criteria.

The Project Verification / Assurance Authority **SHALL NOT** redefine the underlying project property, threshold, architecture decision or external acceptance constraint merely by performing verification.

### `SCAF-AK-006` — Applicable Satisfaction Basis

**Target:** Project-Applicable Obligation

For each verification obligation, the project **SHALL** establish an **Applicable Satisfaction Basis** sufficient to determine what is being verified.

The basis **SHALL** trace, as applicable, to:

- the source SCAF obligation;
- the Project Design Authority decision/value;
- applicable external-authority constraints; and
- controlled derived conditions needed for verification.

The Applicable Satisfaction Basis is a trace construct and **SHALL NOT** create a new authority.

### `SCAF-AK-007` — Evidence sufficiency evaluation

**Target:** Project-Applicable Obligation

The Project Verification / Assurance Authority **SHALL** determine whether project evidence is sufficient for the applicable verification claim by applying `SCAF-ASSUR` semantics and the Applicable Satisfaction Basis.

Evidence sufficiency **SHALL NOT** by itself grant authority to accept or close the underlying requirement, design decision, risk, deviation or other project obligation.

### `SCAF-AK-012` — Underlying closure authority

**Target:** Project-Applicable Obligation

The authority that owns the underlying requirement, design decision, risk acceptance or deviation **SHALL** retain the corresponding closure authority.

If project governance reassigns that underlying authority, the reassigned role **SHALL** be explicit and **SHALL** act in that underlying authority capacity, not merely in a verification role.

### `SCAF-AK-013` — Closure/disposition trace

**Target:** Project-Applicable Obligation

The project **SHALL** record applicable closure/disposition state and authority provenance through `SCAF-APP` or an equivalent controlled project-application record.

The project-application record **SHALL NOT** be treated as the underlying closure authority merely because it records the closure/disposition.

### `SCAF-AK-008` — Cross-cutting concerns and project-instance ownership

**Target:** Project-Applicable Obligation

Where multiple SCAF concerns constrain one project decision, the project **SHALL** preserve one explicit primary Project Design Authority for the decision or define an explicit coordinated decision rule.

The project trace **SHALL** distinguish the primary project-instance decision authority from other concern constraints, observations and verification obligations.

## 6. Framework Normative Invariants

### `SCAF-AK-009` — Controlled rewrite is not normative promotion

**Target:** Framework Normative Invariant

Content may enter controlled normative rewrite when its architecture home and source evidence are sufficient for drafting. Entry into rewrite **SHALL NOT** be interpreted as normative promotion or freeze.

Donor-derived normative statements **SHALL** retain source maturity and audit provenance. Draft/RC/mixed-maturity donors and executable-only invariants **SHALL NOT** be silently promoted to frozen SCAF authority.

Eligibility as rewrite input, eligibility for SCAF normative promotion and eligibility for freeze **SHALL** remain distinct gates.

### `SCAF-AK-010` — Framework governance boundary

**Target:** Framework Normative Invariant

SCAF Framework / Governance **SHALL** govern SCAF normative sources, authority semantics, precedence, provenance and SCAF release/change rules.

It **SHALL NOT** claim organizational governance of project design teams, Project Design Authority, Project Realization or Project Verification / Assurance Authority.

### `SCAF-AK-011` — Framework relation-language invariant

**Target:** Framework Normative Invariant

SCAF normative concern documents **SHALL** use relation language that preserves framework-side/project-side authority separation.

Where a SCAF concern does not own a project-instance value, it **SHALL** use relations such as **Constrains**, **Observes**, **Guides Realization** or framework-side assurance semantics rather than wording that implies duplicate project-instance ownership.

Unqualified `Defines`, `owns`, `acceptance` and `Realizes` **SHALL NOT** be used in normative authority declarations where they could obscure framework-side/project-side authority, evidence-sufficiency, or closure semantics.

## 7. Relation Grammar for Normative Documents

- **Defines Framework Semantics / Obligation** — framework-side semantic/normative owner.
- **Defines Project Instance / Decision** — designated project-side Controlled Decision owner.
- **Constrains** — adds a required condition without becoming project-instance owner.
- **Guides Realization** — framework-side profile/pattern guidance to Project Realization.
- **Realizes** — Project Realization implements a Controlled Decision / required property.
- **Observes** — runtime observation/evidence of a property without becoming its source authority.
- **Verifies** — Project Verification / Assurance Authority demonstrates/evaluates satisfaction.
- **Dispositions / Traces** — project application record of applicability, decision, deviation, risk, verification obligation, verification execution/result state, evidence, closure and re-evaluation state.

## 8. Rewrite and Promotion Gates

| Gate | Meaning in v0.0.2rc09 |
|---|---|
| Architecture convergence | Passed by frozen v0.0.1 baseline |
| Controlled L1/L2 rewrite | Open |
| Broad donor normative promotion | Closed pending donor-specific semantic/source audit |
| Final migration proof | Closed |
| Normative freeze | Closed until explicit freeze decision |

A donor concept may be used as controlled rewrite input without being eligible for normative promotion. A promoted normative statement requires sufficient donor-specific source/maturity/anchor reconciliation for the statement being promoted.
