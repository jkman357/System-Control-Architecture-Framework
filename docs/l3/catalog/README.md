# L3 Catalog Placement

This directory will contain future SCAF L3 Pattern / Mechanism entries after the v0.0.3rc01 catalog contract passes review.

Expected family paths are:

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

Empty family directories are not committed in v0.0.3rc01. A family directory should be created when its first actual `SCAF-PAT-*` entry is introduced.

Pattern identity is based on the primary mechanism family. Cross-concern coverage belongs in pattern metadata through L2 trace relations rather than by duplicating the same pattern under multiple family paths.
