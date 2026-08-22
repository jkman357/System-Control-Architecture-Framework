# SCAF Normative Evolution Candidates

This directory contains **development-line candidate normative overlays** created after a formal frozen SCAF release.

Candidate overlays exist so a new L1/L2 semantic change can be reviewed without editing the immutable formal normative baseline in place and without immediately forcing unreviewed changes through machine-readable authority, trace, Project Application, context-consumption or L4 artifacts.

## Authority status

The formal normative source for the current frozen release remains under:

```text
docs/normative/
```

A file in `docs/normative-evolution/` is **not yet accepted canonical authority** merely because it is present in an active development RC.

For a candidate overlay:

1. the named frozen normative source is the predecessor;
2. the candidate overlay shows the complete proposed replacement text for the affected source file;
3. unaffected frozen normative files remain inherited unchanged for review context;
4. candidate-only IDs are reserved for the development line but are not added to the frozen machine-readable authority registry until a separately reviewed representation migration is justified;
5. acceptance of the semantic candidate does not itself imply L3 Pattern, L4 Construction Guidance, schema, validator, CI, project-profile or consumer-context changes.

This separation preserves the rule:

```text
frozen release != active candidate
semantic acceptance != executable representation migration
```

## Active development state

`v0.2.0rc01` introduced one candidate overlay:

- `80_SCAF_OBS_Observability_Diagnostics_Incident_Evidence_Obligations_v0.2.0rc01.md`

It proposes L2 obligations for diagnostic-instrumentation lifecycle intent, temporary development instrumentation cleanup, explicit remove-or-retain disposition, instrumented-build evidence identity, and retained-observation operational non-dependence / observer-effect acceptance.

No file under the frozen `docs/normative/` tree is modified by `v0.2.0rc01`.

The independent rc01 review returned clean `PASS / GATE YES` with zero findings. `v0.2.0rc02` therefore performs only the required dependency/value assessment in:

- `02_SCAF_v0.2.0rc02_Diagnostic_Instrumentation_Dependency_and_Applicability_Assessment.md`

The rc02 assessment leaves the rc01 OBS overlay text unchanged and concludes that the smallest justified next migration is candidate machine-readable L1/L2 authority representation. Project Application, L3, L4, code generation and generic CI expansion remain deferred/STOP pending separate value gates.

## v0.2.0rc03 Representation Status

The accepted rc01 semantic overlay remains unchanged. rc03 does not promote it into `docs/normative/`. Instead, the separately controlled executable-governance layer now carries a candidate machine-readable authority representation under `candidate-authority-registry.yaml`, with its own candidate schema and source-aware validator.

Formal v0.1.0 authority remains canonical. Candidate machine-readable representation does not by itself authorize Project Application, L3, L4 or formal-promotion migration. See `docs/executable-governance/66_SCAF_v0.2.0rc03_Candidate_Authority_Representation_Foundation.md`.

## v0.2.0rc07 Engineering Evidence Gap Assessment

After the clean rc06 semantic-foundation review, downstream candidate-consumer implementation is temporarily parked while the active L2 evidence authority is re-evaluated. rc07 adds no new authority identity and does not modify the accepted rc01 OBS overlay.

The assessment is recorded in:

- `03_SCAF_v0.2.0rc07_Engineering_Evidence_Binding_Change_Applicability_and_Closure_Gap_Assessment.md`

It classifies existing authority coverage and identifies three material L2 gaps: generic evidence-to-realization applicability binding, baseline/change evidence relationship, and before/after verification-closure evidence relationship. Analysis methods such as first behavioral divergence and Evidence→Hypothesis→Probe remain deferred to a future L3 pattern after the L2 evidence foundation stabilizes.
