# Framework Gen2

**Version:** v0.0.1rc1  
**Status:** Repository archaeology / taxonomy proposal release candidate  
**Date:** 2026-08-15

Framework Gen2 is a system-level engineering framework intended to reduce design omission, unclear responsibility, fault propagation, poor diagnosability, unrecoverable behavior, and unverifiable design decisions.

This release candidate does **not** attempt to rewrite the full Framework. It establishes the evidence base required before structural rewriting begins.

## Baseline Position

Two source repositories are analyzed separately:

1. **Gen1 formal baseline** — `host-device-control-framework`.
2. **Supplemental resilience source** — `Embedded_Incident_Crash_Recorder_Framework`.

The supplemental source is not retroactively treated as Gen1 content. Every Gen2 mapping shall preserve source provenance.

## Gen2 Direction

Gen2 generalizes the original Host / Device or Coordinator / Node model into:

```text
System
  -> Node
      -> Role(s)
      -> Capability / Resource / State
      -> Interface(s)
      -> Implementation Technology
```

A Node may be implemented by an MCU, PC, SoC, FPGA, DSP, Linux SBC, service process, gateway, or another computing element. A heterogeneous system may contain several implementation technologies and several role relationships at the same time.

`Coordinator`, `controller`, `device`, `gateway`, `supervisor`, `service tool`, and similar terms are therefore treated as **roles**, not as fixed top-level architecture classes.

## First-Phase Rules

Before taxonomy and mapping converge:

- do not perform a large-scale rewrite of Gen1 documents;
- do not preserve Gen1 directory boundaries merely because they already exist;
- identify one conceptual authority per topic before producing detailed normative text;
- keep implementation-specific guidance subordinate to system-level rules;
- preserve provenance of Gen1 and supplemental concepts;
- distinguish framework requirements, project decisions, implementation profiles, verification obligations, and evidence;
- explicitly list files that were not read.

## Framework Scan / Applicability Analysis

A primary Gen2 use case is project-start scanning in addition to Requirement Analysis. Candidate disposition / obligation states include:

- `Applicable`
- `Not Applicable`
- `TBD / Deferred`
- `Risk Identified`
- `Design Decision Required`
- `Verification Required`
- `Evidence Required`

These are intentionally preserved in this RC as design inputs. Their final data model is not frozen yet.

## Repository Content

| File | Purpose |
|---|---|
| `docs/00_Input_Baseline.md` | Input identity, source provenance, and analysis boundary |
| `docs/01_Gen1_Repository_Inventory.md` | Complete Gen1 and supplemental file inventory with preliminary action |
| `docs/02_Document_Role_Analysis.md` | Role and content analysis by document family |
| `docs/03_Gen1_to_Gen2_Concept_Mapping.md` | Concept-level mapping independent of Gen1 directories |
| `docs/04_Overlap_Obsolescence_and_Gap_Analysis.md` | Duplicate authority, outdated framing, overlap, and missing capabilities |
| `docs/05_Gen2_Taxonomy_Proposal.md` | Proposed system-level Gen2 taxonomy |
| `docs/06_Read_Coverage_Audit.md` | Read coverage and analysis-depth record |
| `CHANGELOG.md` | RC history |

## CI / Automation Position

**No CI is included in v0.0.1rc1.**

Gen1 contains substantial repository-validation tooling, schemas, fixtures, tests, CODEOWNERS rules, and GitHub Actions. These are valuable concepts, but copying them now would prematurely encode Gen1 structure into Gen2.

They remain mapped as future candidates under **Machine-Verifiable Framework / Tooling / Governance**. Tooling should be rebuilt only after the taxonomy, authority boundaries, and stable machine-readable contracts are defined.

## Release Policy

Discussion and iterative releases use RC versions. A non-RC version shall be created only after an explicit **freeze** decision.

Current sequence begins at:

```text
v0.0.1rc1
```

## Current Conclusion

This RC is an analysis baseline, not a final architecture baseline. Its purpose is to make the next decisions explicit:

```text
What Gen1 contains
      -> what remains valid
      -> what moves or merges
      -> what must be rewritten
      -> what must be retired
      -> what Gen2 must add
      -> where each concept belongs in the new system taxonomy
```
