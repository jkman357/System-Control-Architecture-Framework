# SCAF v0.0.4rc04 — Authority-Registry Release-State Documentation Cleanup

**Development Release:** v0.0.4rc04  
**Status:** Focused `R3-01` repository-state documentation cleanup RC  
**Upstream Baselines:** frozen v0.0.2 L1/L2; frozen v0.0.3 L3  
**Upstream Gate:** `V0.0.4 INITIAL AUTHORITY-REGISTRY SERIALIZATION GATE: YES, AFTER MINOR CLEANUP`

## 1. Purpose

The independent v0.0.4rc03 review accepted the initial 294-record `authority-registry.yaml` serialization and identified one localized Minor finding, `R3-01`: later root-README sections still described rc02 as the current state, stated that registry serialization had not yet occurred, stopped the release sequence at rc02, and presented the already-closed rc02 determinism gate as the immediate gate.

rc04 closes only that repository-state/navigation inconsistency before a later schema + structural-validator RC is opened.

## 2. Cleanup Boundary

The rc04 cleanup updates current-state documentation so that the repository consistently describes:

- rc03 as the accepted initial 294-record serialization stage;
- `R3-01` as the only rc03 cleanup item;
- rc04 as the focused release-state documentation cleanup RC;
- the next separately gated stage as schema + structural validator;
- schema, validator implementation, tests, CI, code generation, generated indexes/views, automatic applicability inference, machine-readable L2→L3 relations, new L3 work, M3/M4 and L4 as not implemented by rc04.

## 3. Artifacts Intentionally Unchanged

rc04 shall not change:

- repository-root `authority-registry.yaml`;
- `docs/executable-governance/00_SCAF_Machine_Readable_Authority_Model.md`;
- `docs/executable-governance/01_SCAF_v0.0.4rc02_Authority_Model_Determinism_Cleanup.md`;
- `docs/executable-governance/02_SCAF_v0.0.4rc03_Initial_Authority_Registry_Serialization.md`;
- any file under `docs/normative/`;
- any file under `docs/l3/`.

In particular, all 294 registry records retain `representation_release: v0.0.4rc03`. rc04 is not a reserialization event.

## 4. Accepted Registry State Preserved

The accepted rc03 registry state remains:

```text
294 records / 294 unique IDs
218 Project-Applicable Obligations
76 Framework Normative Invariants
0 SCAF-PAT-* records
record_kind = normative_requirement
layer = l1_l2_normative_authority
source_anchor = id
source_release = v0.0.2
representation_release = v0.0.4rc03
status = represented
relations = []
```

Frozen normative Markdown remains canonical semantic authority; registry presence does not imply project applicability, satisfaction/compliance, realization, verification, evidence sufficiency, closure, waiver/risk acceptance, L3 availability/maturity, or Pattern selection.

## 5. Current-State Documentation Contract

After cleanup, the root README shall no longer contain a current-state assertion that:

- rc02 is the current v0.0.4 development state;
- the authority registry has not yet been serialized;
- the release sequence ends at rc02;
- the immediate gate is `V0.0.4 AUTHORITY-MODEL DETERMINISM CLOSURE GATE`.

Historical references to rc02 and its gate remain valid when explicitly presented as history/upstream context.

## 6. Gate

Independent review shall determine whether `R3-01` is fully resolved and whether the cleanup preserved the accepted registry and frozen upstream trees unchanged.

Expected decision:

```text
V0.0.4 AUTHORITY-REGISTRY RELEASE-STATE CLEANUP GATE: YES / YES, AFTER MINOR CLEANUP / NO
```

A `YES` authorizes only opening a later separately reviewed schema + structural-validator RC. It does not authorize CI, code generation, generated enforcement/views, project applicability inference, machine-readable L2→L3 relations, new L3 work, M3/M4 or L4 automatically.
