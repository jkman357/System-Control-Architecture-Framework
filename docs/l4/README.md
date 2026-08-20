# SCAF L4 Construction / Verification Guidance

**Development Release:** v0.1.0rc01  
**Upstream Baselines:** frozen v0.0.2 L1/L2; frozen v0.0.3 L3; frozen v0.0.10 controlled-context baseline  
**Status:** L4 semantic / layer-boundary foundation review candidate; no published L4 guidance entries yet

## Purpose

L4 is the construction-facing SCAF layer. It provides concrete implementation and verification guidance downstream of accepted architecture obligations and reusable L3 Patterns / Mechanisms while preserving Project Design Authority.

The intended chain is:

```text
L1 / L2 authority
        ↓
L3 Pattern / Mechanism
        ↓
L4 Construction / Verification Guidance
        ↓
Project Design Authority
        ↓
Project Realization
        ↓
Project Verification / Assurance Authority
```

L4 is expected to evolve more frequently than L3 and substantially more frequently than the stable L1/L2 core.

## rc01 Scope

v0.1.0rc01 establishes only the semantic and layer-boundary foundation needed before representative L4 entries are authored.

It defines:

- L4 purpose and non-authority boundary;
- L2/L3/L4/PDA separation;
- many-to-many L3↔L4 trace semantics;
- stable L4 identity form;
- Construction Constraint / Recommended Practice / Example Realization distinctions;
- Required Project Decision semantics and no-hidden-default rule;
- Construction Invariants and Assumptions;
- ownership, interface/state, timing, concurrency, capacity, lifecycle and failure/recovery construction questions;
- observability and Verification Intent coupling;
- material deviation, anti-over-specification and platform-neutral-first rules;
- L4 composition/conflict and L4→L3 escalation rules;
- non-retroactivity, revision/supersession and partial-catalog semantics;
- Construction Readiness as the milestone acceptance concept.

It intentionally adds no published L4 entry, registry, schema, validator, trace registry, project-side adoption record, platform implementation, reference code, code generator or CI gate.

## Files

| Path | Purpose |
|---|---|
| `00_L4_Minimum_Construction_Guidance_Contract.md` | Canonical rc01 L4 semantic / layer-boundary contract |
| `templates/L4_Construction_Guidance_Template.md` | Authoring aid for later representative entries; allocates no identity |

## Governing Distinctions

```text
L4 guidance != new framework authority
L4 recommendation != Project Design Decision
L4 example != canonical implementation
L4 Verification Intent != project test result
Construction Ready != buildable / verified / compliant / closed
no L4 guidance != concern not applicable
```

A clean rc01 review permits only a new dependency/value assessment for the smallest useful representative L4 tranche. It does not pre-authorize a broad catalog or executable L4 tooling.
