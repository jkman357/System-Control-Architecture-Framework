# Input Baseline

## 1. Purpose

This document records the exact source inputs used for Framework Gen2 v0.0.1rc1.

## 2. Gen1 Formal Baseline

**Input archive:** `host-device-control-framework-main.zip`  
**SHA-256:** `907db1580b4829132c93173ecdd4af8f001cd8ec41fc65e1b0e481b076a89bcb`  
**Files:** 72

Treatment:

- formal Gen1 historical baseline;
- source material for concept extraction and mapping;
- not modified in place;
- Gen2 does not inherit its directory layout by default.

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

Other authorities are marked Draft for Review or RC inside Gen1 and are treated according to their declared status rather than silently promoted.

## 3. Supplemental Resilience Source

**Input archive:** `Embedded_Incident_Crash_Recorder_Framework-main.zip`  
**SHA-256:** `c1479b2b2be0febbdb72c7fbed160686fe2f17b99ac6cf54e8e98f10dadaf76c`  
**Files:** 2

Primary specification:

- `README.md`
- version `v1.0.1rc03`
- date `2026-08-14`
- generic embedded-system scope

Treatment:

- supplemental source for robustness, resilience, diagnostics, evidence survivability, recovery, and observer-effect concepts;
- **not** counted as Gen1 original content;
- implementation-contract material is not automatically promoted into Gen2 system-level rules;
- generic concepts are separated from recorder-specific reference implementation details.

## 4. Analysis Boundary

v0.0.1rc1 performs:

1. repository inventory;
2. document-role analysis;
3. concept extraction;
4. Gen1 -> Gen2 mapping;
5. overlap / obsolescence / gap analysis;
6. taxonomy proposal;
7. read-coverage audit.

It does not yet perform:

- full normative rewrite;
- final authority registry design;
- final Framework Scan schema;
- schema implementation;
- validator implementation;
- test fixture migration;
- CI migration;
- reference implementation migration.

## 5. Provenance Rule

Every future Gen2 concept should be traceable to one or more of:

```text
Gen1 Baseline
Supplemental Crash Recorder
Gen2 New Requirement
External Requirement / Standard
Project-Specific Decision
```

This prevents new material from being mistaken for inherited baseline behavior and prevents supplemental implementation detail from silently becoming universal system policy.
