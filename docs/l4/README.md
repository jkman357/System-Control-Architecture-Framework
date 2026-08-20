# SCAF L4 Construction / Verification Guidance

**Release:** v0.1.0
**Upstream Baselines:** frozen v0.0.2 L1/L2; frozen v0.0.3 L3; frozen v0.0.10 controlled-context baseline
**Status:** Frozen Minimum L4 Construction Guidance Baseline; two accepted representative identities

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

## Frozen v0.1.0 Baseline

`v0.1.0rc01` established the accepted L4 semantic/layer contract.

`v0.1.0rc02` introduced and independently validated `SCAF-L4-001 — Bounded Queue / Backpressure / Overload Construction Guidance` as locally Construction Ready.

`v0.1.0rc03` introduced and independently validated `SCAF-L4-002 — Runtime Health Supervision and Watchdog Construction Guidance`, composing two frozen SUP Patterns and demonstrating cross-problem generalization of the same L4 contract.

The formal `v0.1.0` baseline freezes those two entries and the rc01 contract as the minimum construction-guidance milestone:

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

The L4 catalog is intentionally partial. Missing L4 guidance does not change upstream applicability or Pattern validity. Future L4 additions/improvements remain demand-driven and may evolve more frequently than L3; material architecture-mechanism defects are escalated to L3 rather than hidden in L4 prose.

No third L4 identity, registry, schema, validator, machine-readable L3↔L4 trace, project adoption record, platform API guidance, reference implementation, generator or CI gate is included in the frozen v0.1.0 baseline.

## Files

| Path | Purpose |
|---|---|
| `00_L4_Minimum_Construction_Guidance_Contract.md` | Accepted rc01 L4 semantic / layer-boundary contract |
| `templates/L4_Construction_Guidance_Template.md` | Non-instantiating authoring aid for representative entries |
| `catalog/SCAF-L4-001_Bounded_Queue_Backpressure_Overload_Construction_Guidance.md` | rc02 first representative L4 construction guidance; accepted after clean review and commit |
| `catalog/SCAF-L4-002_Runtime_Health_Supervision_and_Watchdog_Construction_Guidance.md` | Accepted second representative L4 construction guidance |

## Governing Distinctions

```text
L4 guidance != new framework authority
L4 recommendation != Project Design Decision
L4 example != canonical implementation
L4 Verification Intent != project test result
Construction Ready != buildable / verified / compliant / closed
no L4 guidance != concern not applicable
```

The post-rc03 dependency/value assessment concluded STOP for further v0.1.0 RC/catalog/tooling expansion. The two accepted representatives and rc01 contract are frozen as the minimum v0.1.0 L4 baseline; future additions require a new demand-driven decision horizon.
