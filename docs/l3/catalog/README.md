# L3 Catalog Placement

v0.0.3rc09 is a focused second-tranche trace-cleanup release after the independent rc08 review returned `L3 SECOND-TRANCHE PATTERN GATE: YES, AFTER MINOR CLEANUP`.

The catalog still contains **twelve** published identities:

- seven initial-tranche entries remain `Available / M2`;
- five second-tranche entries remain `Candidate / M1`.

The only semantic Pattern edit in rc09 is the `FTL-001` reclassification of `SCAF-ROB-007` from Supporting L2 Trace to Constraint Inputs, preserving `SCAF-ROB-015` as Supporting Realization. No ID, family, status, maturity or `Introduced In` value changes.

Family paths are:

```text
catalog/SUP/
catalog/COM/
catalog/REC/
catalog/FTL/
catalog/TIM/
catalog/PST/
catalog/LCM/
catalog/EVD/
catalog/SYN/
catalog/SEC/
```

Pattern identity is based on the immutable primary mechanism family after publication. Cross-concern coverage belongs in pattern metadata through L2 trace relations rather than by duplicating the same pattern under multiple family paths.

The new FTL/TIM/SYN entries do not change the lifecycle state of the initial seven. `Candidate / M1` for the new entries means structured Pattern content awaiting independent architecture/trace review; it does not imply `Available`, project selection, recommendation, compliance, verification or L2 satisfaction.
