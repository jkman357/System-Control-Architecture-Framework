# Input Baseline

## 1. Purpose

This document records the exact source and review inputs used for the frozen **System Control Architecture Framework (SCAF) v0.0.1** architecture-convergence baseline.

## 2. Gen1 Formal Baseline

**Input archive:** `host-device-control-framework-main.zip`  
**SHA-256:** `907db1580b4829132c93173ecdd4af8f001cd8ec41fc65e1b0e481b076a89bcb`  
**Files:** 72

Treatment:

- formal Gen1 historical baseline;
- source material for concept extraction and migration mapping;
- not modified in place;
- SCAF does not inherit its directory layout by default.

Notable self-declared baseline documents include:

- `Coordinator_Node_Control_Framework.md` — v1.1.7, Baseline;
- `Framework_Application_Analysis_Template.md` — v1.1.9, Baseline;
- `Protocol_YAML_Definition_Guide.md` — v1.1.7, Baseline;
- `Protocol_YAML_Template.md` — v1.1.1, Baseline;
- `Coordinator_Software_Engineering_Rules.md` — v1.1.1, Baseline;
- `Coordinator_Architecture_Patterns.md` — v1.1.1, Baseline;
- `Coordinator_UI_Engineering_Guide.md` — v1.1.2, Baseline;
- `CSharp_Coding_Rules.md` — v1.0.5, Baseline;
- `Repository_Validation_Checklist.md` — v1.1.3, Baseline.

Other authorities are marked Draft for Review or RC inside Gen1. SCAF mapping records source maturity rather than silently promoting them.

## 3. Supplemental Resilience Source

**Input archive:** `Embedded_Incident_Crash_Recorder_Framework-main.zip`  
**SHA-256:** `c1479b2b2be0febbdb72c7fbed160686fe2f17b99ac6cf54e8e98f10dadaf76c`  
**Files:** 2

Primary specification:

- `README.md`;
- version `v1.0.1rc03`;
- date `2026-08-14`;
- generic embedded-system scope.

Treatment:

- supplemental donor for robustness, resilience, diagnostics, evidence survivability, recovery and observer-effect concepts;
- **not** counted as Gen1 original content;
- generic concepts are separated from recorder-specific API/ABI, record-layout, RAM-budget and implementation recommendations.

## 4. Independent Review Input

**Input:** `framework-gen2-v0.0.1rc1-independent-architecture-review.md`  
**SHA-256:** `99df555ece83b597c2ecd031ddbae09ca15c20beea6cf04c333eaf99309bd158`

Treatment:

- review evidence and correction input for rc03;
- not a normative SCAF source;
- used to challenge taxonomy planes, Node metamodel, migration evidence, robustness semantics and Framework Scan responsibility;
- review findings are incorporated only where independently accepted into rc03 architecture decisions.

### rc02 Review

**Input:** `System-Control-Architecture-Framework-v0.0.1rc02-independent-review.md`  
**SHA-256:** `5a24461595e6814db6caf54f797614f2b27cf9ec0481215d5f3fc49a35caf961`

Treatment:

- independent architecture/framework review evidence for rc03;
- not a normative SCAF source;
- used to challenge framework-vs-project authority, plane relations, CTX/ARCH dependency ownership, assurance ownership, Framework Scan startup usability, timebase authority, security scope and migration reproducibility.


### rc03 Review

**Input:** `SCAF-v0.0.1rc03-independent-architecture-review.md`  
**SHA-256:** `9ebf16ef4569cb31e5d846bd16571d82634d78232ca64fd3549bfd4210d7054c`

Treatment:

- independent architecture/framework review evidence for rc04;
- not a normative SCAF source;
- confirmed that the architecture skeleton and framework-vs-project authority split are structurally viable;
- used to close canonical authority-diagram consistency, authority-grammar usage, Framework Scan closure semantics, Service/Capability and hierarchical System/Node ambiguity, ROB/LIFE/OBS boundaries, security-vs-project authority wording and multi-source migration traceability.

### rc04 Review

**Input:** `SCAF-v0.0.1rc04-independent-architecture-review(1).md`  
**SHA-256:** `96aafa8b0ad9d184327ec364acc948765327ace3cb3617b145c629358552ef51`

Treatment:

- independent architecture/framework review evidence for rc05;
- not a normative SCAF source;
- confirmed no new Critical architecture flaw and accepted controlled normative rewrite;
- used to canonicalize the five SCAF framework planes vs project-side Project Design Authority, split time epoch from boot/session/operational incarnation identity, replace source-owned satisfaction wording with Applicable Satisfaction Basis, align migration targets with current authority semantics and remove stale rewrite-gate wording.


### rc05 Review

**Input:** `SCAF-v0.0.1rc05-independent-architecture-review.md`  
**SHA-256:** `b76cb97be2dddca4f1591059e782c5a9dfe4ea5b51392beabe932dca6b003c7b`

Treatment:

- independent authority-kernel / architecture-convergence gate review for the v0.0.1 freeze decision;
- not a normative SCAF source;
- reported **no Critical architecture issue**;
- directed architecture discovery and top-level taxonomy expansion to stop;
- accepted Framework Scan as a new-project startup architecture decision mechanism;
- accepted controlled L1/L2 normative rewrite with minor authority-language cleanup during the next development line;
- retained broad donor promotion, final migration proof and machine-enforcement work as separate future gates.

## 5. Analysis Boundary

The frozen v0.0.1 baseline preserves the rc05 architecture-convergence work:

1. preservation of complete Gen1 and supplemental repository inventory;
2. document-role analysis;
3. source-anchored concept migration mapping;
4. source-maturity and mapping-confidence recording;
5. authority-plane separation;
6. minimum core-metamodel definition;
7. authority-relation grammar definition;
8. robustness / resilience conceptual restructuring;
9. Framework Scan lifecycle restructuring;
10. overlap / obsolescence / gap analysis refresh;
11. three representative tabletop architecture exercises;
12. complete-state/closure worked Framework Scan traces for selected concerns in the PC + multiple MCU archetype;
13. canonical concern/Project Design/Realization/Assurance authority-chain closure;
14. five-plane vs project-side authority canonicalization;
15. time epoch / boot incarnation / protocol-session / operational-incarnation semantic partition;
16. Applicable Satisfaction Basis trace semantics;
17. migration-map alignment with the current authority model and per-donor promotion gates;
18. read-coverage and deep-audit-state audit.

It permits the next development line to perform **controlled L1/L2 normative rewrite** of the architecture kernel and audited/high-confidence content, while retaining donor-promotion gates.

It does **not** yet perform:

- broad/unrestricted normative rewrite;
- final authority registry design;
- final Framework Scan enum/schema freeze;
- schema implementation;
- validator implementation;
- test fixture migration;
- CI migration;
- reference implementation migration;
- complete requirement-by-requirement reconciliation of every Gen1 test/schema/tool invariant.

## 6. Provenance Classes

Every future SCAF concept should be traceable to one or more of:

```text
Gen1 Baseline
Gen1 Draft / RC Donor
Supplemental Crash Recorder
SCAF New Architecture Requirement
External Requirement / Standard
Project-Specific Decision
```

A source maturity marker is part of migration evidence. “Found in Gen1” is not equivalent to “accepted Gen1 baseline requirement.”

## 7. Reproducibility / Retrievability Note

The source archives are intentionally not copied into the SCAF source repository. Their archive names and SHA-256 digests identify the analyzed inputs, and source-section anchors in `03_Gen1_to_Gen2_Concept_Mapping.md` provide human-readable trace points.

However, **identity is not retrievability**. An independent reviewer cannot reproduce source-semantic review from SHA-256 alone unless the exact donor snapshot is obtainable. Before migration completion or broad normative promotion of donor-derived content, each donor snapshot must therefore gain an immutable/retrievable locator such as a repository commit/tag, release artifact locator, or controlled archive reference.

Frozen v0.0.1 source-evidence status:

- source identity: **available**;
- source anchors: **available for mapped core concepts**;
- immutable/retrievable donor snapshot locator: **pending**;
- independent source-semantic reproducibility: **not yet complete**.

## 9. v0.0.2rc01 Derivation Note

`v0.0.2rc01` is derived from the frozen SCAF `v0.0.1` architecture baseline. The frozen source release is not modified in place. New normative content is authored under `docs/normative/` and remains subject to the existing donor maturity/promotion gates.
