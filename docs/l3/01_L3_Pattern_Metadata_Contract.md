# SCAF L3 Pattern Metadata Contract

**Development Release:** v0.0.3rc01  
**Status:** Development contract  
**Applies To:** future `SCAF-PAT-*` catalog entries

## 1. Purpose

This document defines the metadata structure required for future SCAF L3 Pattern / Mechanism entries.

The contract is intentionally human-readable in v0.0.3rc01. It does not introduce YAML, JSON Schema, validation code or CI. Field stability may later become an input to executable governance after a separate gate.

## 2. Metadata Principles

Pattern metadata must make five boundaries visible:

1. **identity** — what catalog artifact is being referenced;
2. **upstream trace** — which frozen L2 obligations motivate or constrain the pattern;
3. **selection boundary** — what remains a Project Design Authority decision;
4. **realization boundary** — what mechanism architecture is described without entering L4 implementation detail;
5. **confidence/lifecycle** — how mature the pattern is and whether it is currently offered for selection.

## 3. Required Core Fields

Each future pattern entry must contain the following fields.

| Field | Required | Meaning |
|---|---:|---|
| `Pattern ID` | Yes | Stable `SCAF-PAT-<FAMILY>-<NNN>` identity |
| `Pattern Name` | Yes | Human-readable mechanism name |
| `Pattern Family` | Yes | Primary L3 family code |
| `Pattern Kind` | Yes | `Mechanism`, `Composite Pattern`, or `Reference Subsystem` |
| `Catalog Status` | Yes | `Draft`, `Candidate`, `Available`, `Deprecated`, or `Retired` |
| `Maturity` | Yes | `M0` through `M4` |
| `Introduced In` | Yes | First repository release containing the pattern ID |
| `Intent` | Yes | Architecture intent of the mechanism |
| `Problem` | Yes | Problem/condition the mechanism is intended to address |
| `Applicability` | Yes | Conditions under which the pattern should be considered |
| `Non-Applicability / Cautions` | Yes | Conditions that invalidate or weaken the mechanism |
| `Primary L2 Trace` | Yes | Frozen L2 obligation(s) that primarily motivate the pattern |
| `Supporting L2 Trace` | Yes | Other frozen obligations materially supported by the pattern; may be `None` |
| `Constraint Inputs` | Yes | Frozen obligations/project decisions whose semantics constrain use of the pattern; may be `None` |
| `Required PDA Decisions` | Yes | Project-specific decisions deliberately unresolved by the pattern |
| `Mechanism Summary` | Yes | Technology-neutral architecture description |
| `Variants` | Yes | Legitimate mechanism variants; may state `None identified` |
| `Forces / Tradeoffs` | Yes | Resource, latency, complexity, coupling, availability or other decision forces |
| `Failure / Weakness Modes` | Yes | Ways the pattern can fail, mislead or lose effectiveness |
| `Selection Consequences` | Yes | New constraints/assumptions created when selected |
| `Composition Relations` | Yes | Requires / commonly-composed / alternative / conflict / subsume relations; may be `None` |
| `Profile Facets` | Yes | Relevant realization-profile facets; may be broad/technology-neutral |
| `External Authority Considerations` | Yes | Safety/security/regulatory/risk inputs that may constrain project selection; may be `None identified` |
| `Re-evaluation Triggers` | Yes | Changes that should cause project re-evaluation of the selected pattern |
| `Provenance / Reference Basis` | Yes | Donor/reference/project-experience basis with source maturity; may identify SCAF-new synthesis |

## 4. Pattern Kind

Initial kinds are:

- `Mechanism` — one reusable architectural realization mechanism;
- `Composite Pattern` — a controlled composition of multiple mechanism roles/steps whose combined behavior is the reusable unit;
- `Reference Subsystem` — a reusable architecture arrangement with multiple cooperating responsibilities, still above product-specific L4 implementation.

`Pattern Kind` does not change upstream L2 authority and does not imply greater applicability.

## 5. L2 Trace Field Semantics

### 5.1 Primary L2 Trace

Identifies the frozen obligations for which the pattern is a **Primary Realization Candidate**.

This relation means the pattern is intentionally designed as a candidate mechanism for the obligation. It does not mean the obligation is satisfied merely by selecting the pattern.

### 5.2 Supporting L2 Trace

Identifies obligations for which the pattern can materially support a project realization but which are not the pattern's primary architectural purpose.

### 5.3 Constraint Inputs

Identifies frozen obligations or project decisions whose controlled semantics must be supplied to/configure the mechanism correctly.

Typical examples include timing bounds, interface semantics, lifecycle eligibility criteria, authoritative configuration state, operational-state meaning or evidence requirements.

The three trace fields are deliberately distinct and shall not be collapsed into a generic `satisfies` relation.

## 6. Required PDA Decisions

This field is mandatory because L3 must not silently become Project Design Authority.

It records project values/choices that the pattern intentionally does not decide, such as:

- monitored participant or protected responsibility;
- health/liveness meaning;
- timing interval and threshold;
- retry count/backoff/escalation policy;
- authoritative state/copy selection criteria;
- redundancy/voting/failover eligibility;
- storage/retention capacity;
- trust/key/credential authority choices;
- reset/restart/reintegration consequence;
- acceptable degraded behavior;
- external safety/security/regulatory constraint inputs.

The field should describe **decision categories**, not invent project values.

## 7. Profile Facets

`Profile Facets` may identify relevant environment dimensions without creating platform-specific top-level pattern trees.

Example structure:

```text
Compute / deployment: MCU, PC, SoC, distributed node
Execution model: bare metal, RTOS, process/service
Interaction / transport: local memory, UART, CAN, Ethernet, IPC
Persistence / storage: volatile memory, NVM, filesystem, database
```

A pattern should remain technology-neutral where the mechanism semantics are independent of those facets. Technology-specific restrictions belong only where necessary to preserve the pattern's validity.

## 8. Provenance / Reference Basis

Each pattern must distinguish the maturity of its source basis, for example:

- SCAF-new synthesis;
- frozen SCAF obligation-derived architecture synthesis;
- donor final baseline;
- donor Draft/RC content used only as controlled reference input;
- externally published architecture/standards guidance;
- project/reference implementation experience;
- field evidence.

Reference basis is evidence/provenance, not automatic normative promotion.

## 9. Metadata Not Yet Added

v0.0.3rc01 intentionally does not define:

- machine-readable field keys as normative schema identifiers;
- JSON/YAML serialization;
- schema versioning;
- automatic trace resolution;
- validator severity;
- CI rules;
- generated compliance reports.

Those remain behind the executable-governance gate.
