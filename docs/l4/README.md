# SCAF L4 Construction / Verification Guidance

**Development Release:** v0.1.0rc03
**Upstream Baselines:** frozen v0.0.2 L1/L2; frozen v0.0.3 L3; frozen v0.0.10 controlled-context baseline
**Status:** Second representative L4 construction guidance review candidate; two representative identities, second pending rc03 acceptance

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

## Current v0.1.0 Development

`v0.1.0rc01` established the accepted L4 semantic/layer contract.

`v0.1.0rc02` introduced the first representative entry, `SCAF-L4-001 — Bounded Queue / Backpressure / Overload Construction Guidance`. Independent review returned clean `PASS / GATE YES` and found the entry locally Construction Ready.

`v0.1.0rc03` introduces exactly one second representative candidate:

```text
SCAF-L4-002
Runtime Health Supervision and Watchdog Construction Guidance
```

Primary L3 trace:

```text
SCAF-PAT-SUP-001 — Heartbeat / Liveness Supervision ─┐
                                                     ├─> SCAF-L4-002
SCAF-PAT-SUP-002 — Independent Watchdog with Escalation ┘
```

The rc03 objective is cross-problem generalization, not catalog breadth: verify that the accepted L4 contract remains useful for runtime progress/liveness, supervisor failure, watchdog-service ownership, independence, lifecycle, escalation/reset, evidence and Verification Intent while preserving Project Design Authority and no-hidden-default behavior.

No third L4 identity, registry, schema, validator, machine-readable L3↔L4 trace, project adoption record, platform API guidance, reference implementation, generator or CI gate is introduced.

## Files

| Path | Purpose |
|---|---|
| `00_L4_Minimum_Construction_Guidance_Contract.md` | Accepted rc01 L4 semantic / layer-boundary contract |
| `templates/L4_Construction_Guidance_Template.md` | Non-instantiating authoring aid for representative entries |
| `catalog/SCAF-L4-001_Bounded_Queue_Backpressure_Overload_Construction_Guidance.md` | rc02 first representative L4 construction guidance; accepted after clean review and commit |
| `catalog/SCAF-L4-002_Runtime_Health_Supervision_and_Watchdog_Construction_Guidance.md` | rc03 second representative L4 construction guidance candidate |

## Governing Distinctions

```text
L4 guidance != new framework authority
L4 recommendation != Project Design Decision
L4 example != canonical implementation
L4 Verification Intent != project test result
Construction Ready != buildable / verified / compliant / closed
no L4 guidance != concern not applicable
```

A clean rc03 review permits only a new dependency/value assessment. It does not pre-authorize a third L4 entry, broad catalog expansion or executable L4 tooling; milestone consolidation/freeze should be considered first if cross-representative Construction Readiness is demonstrated.
