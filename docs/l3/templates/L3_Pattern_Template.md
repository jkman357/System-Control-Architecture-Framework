# SCAF L3 Pattern Template

**Development Release:** v0.0.3rc07  
**Status:** Authoring template for additional Candidate entries

> **Template only — new Pattern IDs may be assigned only through the controlled catalog-development/review process. Published IDs are stable and shall not be reused.**

## Metadata

| Field | Value |
|---|---|
| Pattern ID | `SCAF-PAT-<FAMILY>-<NNN>` |
| Pattern Name | `<name>` |
| Pattern Family | `<SUP / COM / REC / FTL / TIM / PST / LCM / EVD / SYN / SEC>` |
| Pattern Kind | `<Mechanism / Composite Pattern / Reference Subsystem>` |
| Catalog Status | `<Draft / Candidate / Available / Deprecated / Retired>` |
| Maturity | `<M0 / M1 / M2 / M3 / M4>` |
| Introduced In | `<release>` |
| Primary L2 Trace | `<Primary Realization Candidate relation(s)>` |
| Supporting L2 Trace | `<Supporting Realization relation(s) or None>` |
| Constraint Inputs | `<frozen L2 Constraint Input relation(s) or None>` |
| Profile Facets | `<relevant realization facets>` |
| Provenance / Reference Basis | `<source and maturity>` |

## 1. Intent

Describe the architecture intent of the mechanism.

## 2. Problem

Describe the problem/condition the mechanism addresses without rewriting the traced L2 obligation.

## 3. Applicability

State the conditions under which the pattern should be considered.

## 4. Non-Applicability / Cautions

State contexts, assumptions or failure conditions that make the pattern unsuitable or materially weaker.

## 5. L2 Trace

### 5.1 Primary Realization Candidate

- `<SCAF-...-NNN>` — `<why this pattern is a primary candidate>`

### 5.2 Supporting Realization

- `<SCAF-...-NNN>` — `<supporting relation>`

### 5.3 Constraint Inputs

- `<SCAF-...-NNN>` — `<frozen L2 semantic/constraint consumed by this pattern>`

Do not use a generic `satisfies` relation. Actual project Controlled Decision references do not belong in this catalog trace field; record their decision categories under `Required PDA Decisions` and the concrete references in project-side application records.

## 6. Required PDA Decisions

List the project-specific architecture decisions that remain unresolved by this pattern.

- `<decision category>`
- `<decision category>`

Do not invent project-specific values. Keep externally owned safety/security/regulatory/risk constraints under `External Authority Considerations`; list here only the PDA-owned architecture/integration decision categories made subject to those inputs.

## 7. Mechanism Summary

Describe the technology-neutral mechanism architecture, responsibilities, conceptual state/information flow and behavior.

## 8. Variants

Describe legitimate architectural variants or state `None identified`.

## 9. Forces / Tradeoffs

Describe material decision forces such as latency, resource cost, coupling, availability, complexity, diagnosability and failure independence.

## 10. Failure / Weakness Modes

Describe ways the mechanism can fail, misclassify, become ineffective or create a new hazard/dependency.

## 11. Selection Consequences

Describe architectural constraints, assumptions or follow-on decisions created by selection.

## 12. Composition Relations

### Requires

- `<pattern/mechanism or None>`

### Commonly Composed With

- `<pattern/mechanism or None>`

### Alternative To

- `<pattern/mechanism or None>`

### Conflicts With

- `<pattern/mechanism or None>`

### Subsumes

- `<pattern/mechanism or None>`

### Supersedes

- `<published pattern identity or None>`

## 13. External Authority Considerations

Identify applicable external safety/security/regulatory/risk authority inputs or state `None identified`.

## 14. Re-evaluation Triggers

Identify material changes that should cause project re-evaluation of this pattern selection.

## 15. Provenance / Reference Basis

Record the source basis and source maturity. Do not promote Draft/RC donor material merely because it informed the pattern.

## 16. L3 / L4 Boundary Note

State what implementation- or verification-specific detail is intentionally deferred to project realization or later L4 guidance.
