# SCAF L3 Trace and Selection Model

**Development Release:** v0.0.3  
**Status:** Frozen L3 trace/selection baseline

## 1. Purpose

This document defines how L3 Pattern / Mechanism entries trace to the frozen v0.0.2 L1/L2 baseline and how projects may record pattern evaluation/selection without confusing catalog use with requirement satisfaction.

## 2. Trace Cardinality

The L2-to-L3 relationship is inherently many-to-many:

```text
Frozen L2 obligation  N  <------>  M  L3 patterns
```

One L2 obligation may have multiple valid realization mechanisms. One L3 pattern may materially relate to obligations from several frozen concerns.

This is expected and does not create duplicate concern authority because L3 does not own the upstream obligation semantics.

## 3. Allowed Upstream Trace Relations

Pattern entries use three upstream relation classes.

### 3.1 Primary Realization Candidate

The pattern is intentionally designed as a primary candidate mechanism for realizing an architectural outcome/decision required by the traced L2 obligation.

### 3.2 Supporting Realization

The pattern can materially support realization of the traced obligation but the obligation is not the pattern's principal intent.

### 3.3 Constraint Input

The traced target is a **frozen L2 obligation** whose semantics, and the controlled project decisions resulting from that obligation, constrain the pattern. The pattern consumes those semantics/constraints rather than redefining them.

At catalog level, `Constraint Input` does not point to a future project's concrete Controlled Decision artifact. The decision category is captured under `Required PDA Decisions`; actual project decision values and artifact references belong in project-side selection/application records.

Examples include:

- timing limits from `SCAF-TIME`;
- interaction/session semantics from `SCAF-INT`;
- operational-state meaning from `SCAF-RUN`;
- lifecycle eligibility/transaction semantics from `SCAF-LIFE`;
- authoritative configuration/persistent-state semantics from `SCAF-CFG`;
- evidence semantics from `SCAF-OBS`;
- security/trust constraints from `SCAF-SEC`.

## 4. Prohibited Trace Shortcut

The generic relation `satisfies` is not used between L2 and L3 catalog entries.

The following inference is invalid:

```text
L2 obligation traces to Pattern X
Pattern X selected
therefore L2 obligation is satisfied
```

Actual project satisfaction still depends on the frozen Authority Kernel semantics, including applicable project decisions, realization, verification/evidence and the Applicable Satisfaction Basis.

## 5. Trace Source of Truth

The authoritative human-readable L2 trace for this development stage resides in each pattern entry's metadata.

Any reverse index such as:

```text
L2 obligation -> candidate L3 patterns
```

is a **derived navigation view** only. It must not become an independent trace authority.

When executable governance is later opened, a generated reverse index should be preferred over dual manual maintenance.

## 6. Catalog Status vs Project Selection State

Catalog lifecycle and project decision state are independent dimensions.

Example:

```text
SCAF pattern catalog status: Available
Project A selection state: Selected
Project B selection state: Rejected
Project C selection state: Selected with Adaptation
```

The catalog does not record a universal project-selection result.

## 7. Project Pattern Selection States

A project-side pattern selection record may use:

| State | Meaning |
|---|---|
| `Not Evaluated` | Pattern has not been assessed for the project |
| `Considered` | Pattern has been assessed but no controlled selection decision is yet recorded |
| `Selected` | Project Design Authority selected the pattern without material architectural adaptation |
| `Selected with Adaptation` | Core pattern intent is retained but project-specific architectural adaptation is controlled and recorded |
| `Rejected` | Pattern was evaluated and intentionally not selected; rationale should be recorded when material |
| `Superseded` | An earlier project selection was replaced by another controlled project decision |

These states belong to project application/design records, not to the SCAF catalog artifact itself.

## 8. Selection Semantics

For each applicable L2 obligation, the project may:

1. identify candidate L3 patterns;
2. evaluate applicability, forces, failure modes and project constraints;
3. select one or more patterns, adapt a pattern, reject catalog candidates, or define another mechanism;
4. record the actual project decision under Project Design Authority;
5. implement the decision through Project Realization;
6. verify the required property using the applicable assurance/evidence basis.

Catalog availability never removes the need for controlled project architecture decisions.

## 9. Composition Semantics

A valid realization may require multiple patterns, for example:

```text
supervision
+
bounded retry / escalation
+
restart or failover
+
state reconciliation
+
retained incident evidence
```

Composition does not create a new upstream L2 obligation. It is a project realization strategy assembled under the existing frozen obligations and controlled project decisions.

Where a reusable composition becomes stable and independently meaningful, it may later be represented as a `Composite Pattern` with its own `SCAF-PAT-*` ID.

## 10. Pattern Alternatives

The catalog is intentionally non-exhaustive and non-exclusive.

A traced L2 obligation may have:

- multiple catalog alternatives;
- context-dependent variants;
- mutually incompatible patterns;
- project-specific mechanisms not yet represented in SCAF.

The absence of a project mechanism from the catalog does not by itself make the mechanism invalid. The project must still establish that applicable frozen obligations and external authority constraints are satisfied.

## 11. Re-evaluation

Pattern selection should be re-evaluated when a material input changes, including where applicable:

- L2 applicability/disposition;
- system/Node/Domain boundary;
- interaction or session semantics;
- timing/resource bounds;
- operational-state or lifecycle behavior;
- configuration/persistent-state authority;
- fault/health assumptions;
- evidence requirements;
- external safety/security/regulatory constraints;
- relevant realization profile facets;
- pattern status or known weakness.

The specific project re-evaluation trigger remains a controlled project/application decision.
