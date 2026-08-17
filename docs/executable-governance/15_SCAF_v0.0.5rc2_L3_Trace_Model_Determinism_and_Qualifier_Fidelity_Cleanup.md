# SCAF v0.0.5rc2 — L3 Trace Model Determinism & Qualifier-Fidelity Cleanup

**Development Release:** v0.0.5rc2  
**Status:** Focused Model Cleanup / Review Candidate  
**Upstream Frozen Baselines:** v0.0.2 L1/L2; v0.0.3 L3; v0.0.4 Executable Governance

## 1. Decision Purpose

The independent v0.0.5rc1 review returned:

```text
V0.0.5 L3 MACHINE-READABLE TRACE REPRESENTATION MODEL FOUNDATION GATE: YES, AFTER MINOR CLEANUP
```

and opened two bounded Minor findings:

- `R1-01` — material qualifier fidelity was not explicitly part of the future source-aware validator proof contract;
- `R1-02` — canonical deterministic ordering was described with advisory `should` rather than a mandatory reproducibility rule.

This RC closes only those two model-contract findings. It adds no serialization, schema, validator implementation, generated index, resolver, project inference, L4 content, new L3 Pattern, M3/M4 claim or new CI/trust capability.

## 2. R1-01 Closure — Material Qualifier Fidelity

The rc1 model now states a mandatory fidelity invariant:

> Where frozen authoritative metadata associates material qualifier text/context with a relation, a future serialization shall preserve that qualifier association as controlled source text/context on the correct relation record.

The future source-aware validator proof contract is extended to reject:

- omission of material qualifier text/context;
- semantic alteration of that source context;
- scope expansion;
- scope truncation;
- association of the qualifier with a different `l2_id` / relation record.

This closes the gap where a future representation could otherwise reproduce all 119 relation triples while losing or mis-associating material qualifier context.

The cleanup does **not** define a formal qualifier grammar or condition language. Exact extraction, grouping and serialization syntax remain deferred to the later serialization/schema gate. Qualifier preservation therefore remains source-fidelity behavior and does not become project-applicability inference.

## 3. R1-02 Closure — Canonical Deterministic Ordering

The rc1 model's canonical ordering rule is changed from advisory `should` to mandatory `shall`.

A future canonical serialization shall use stable ordering based on:

1. `pattern_id` ascending;
2. relation-type order:
   - `primary_realization_candidate`;
   - `supporting_realization`;
   - `constraint_input`;
3. `l2_id` ascending.

This rule provides deterministic representation order for reproducible generation, review and later generator/validator agreement. It remains representation determinism only and does not establish semantic precedence between requirements, Patterns or relation classes.

## 4. Preserved Model Boundaries

The cleanup preserves all rc1 accepted boundaries:

```text
Frozen L3 Pattern Markdown metadata
        ↓ semantic trace authority
Future machine-readable L3 trace representation
        ↓ subordinate representation
Generated forward/reverse navigation
        ↓ derived only
Future resolver/context consumption
```

It also preserves:

```text
Resolved / Traced
!= Applicable
!= Selected
!= Satisfied
!= Compliant
!= Verified
!= Closed
```

The controlled relation vocabulary remains exactly:

```text
primary_realization_candidate
supporting_realization
constraint_input
```

and generic `satisfies` remains prohibited.

## 5. Preserved Frozen Inventory

No frozen source is changed. The accepted current inventory remains:

```text
Pattern identities:                  12
Primary relations:                   23
Supporting relations:                41
Constraint relations:                55
Total relation instances:           119
Unique referenced frozen L2 IDs:     82
```

`authority-registry.yaml` remains frozen and separate:

```text
294 records
218 Project-Applicable Obligations
76 Framework Normative Invariants
0 SCAF-PAT-* records
294 / 294 relations empty
```

## 6. Exact rc2 Change Boundary

This RC is documentation/model-contract cleanup only.

Changed:

```text
README.md
CHANGELOG.md
docs/executable-governance/README.md
docs/executable-governance/14_SCAF_v0.0.5rc1_L3_Machine_Readable_Trace_Representation_Model_Foundation.md
```

Added:

```text
docs/executable-governance/15_SCAF_v0.0.5rc2_L3_Trace_Model_Determinism_and_Qualifier_Fidelity_Cleanup.md
```

No executable code, schema, workflow, registry, manifest, regression test, frozen normative file or frozen L3 file is changed.

## 7. Deferred Scope

Still deferred:

- concrete trace serialization and filename;
- trace schema;
- trace parser/source-aware validator implementation;
- exact qualifier extraction/grouping syntax;
- generated forward/reverse index;
- authority/context resolver;
- automatic project applicability, Pattern selection, satisfaction, compliance, verification, evidence or closure inference;
- new L3 Patterns / third tranche / SEC-primary work;
- M3/M4;
- L4 implementation/verification guidance;
- code generation;
- additional CI/trust capability.

## 8. Closure Criteria

`R1-01` is resolved when independent review confirms that material qualifier fidelity is mandatory at the model level, explicitly included in the future validator proof contract, and still does not create executable applicability semantics.

`R1-02` is resolved when independent review confirms that the stated canonical ordering rule is mandatory and deterministic rather than advisory.

The intended closure gate is:

```text
R1-01: RESOLVED
R1-02: RESOLVED
V0.0.5 L3 TRACE MODEL DETERMINISM / QUALIFIER-FIDELITY CLEANUP GATE: YES
```
