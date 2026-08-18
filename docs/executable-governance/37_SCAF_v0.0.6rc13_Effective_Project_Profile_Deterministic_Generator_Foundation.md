# SCAF v0.0.6rc13 — Effective Project Profile Deterministic Generator Foundation

**Development Release:** v0.0.6rc13  
**Status:** Deterministic Profile Generator Foundation / Review Candidate  
**Date:** 2026-08-18  
**Upstream Frozen Baselines:** v0.0.2 L1/L2; v0.0.3 L3; v0.0.4 Executable Governance; v0.0.5 L3 Machine-Readable Traceability  
**Accepted Development Basis:** v0.0.6rc09 Effective Project Profile semantics; v0.0.6rc10 canonical profile representation; v0.0.6rc11 profile schema; v0.0.6rc12 source-aware profile validator  
**Immediate Predecessor:** v0.0.6rc12

## 1. Decision Purpose

The independent v0.0.6rc12 review returned a clean gate with zero findings:

```text
Critical: 0
Major:    0
Minor:    0
Trivial:  0

V0.0.6RC12 EFFECTIVE PROJECT PROFILE SOURCE-AWARE VALIDATOR FOUNDATION GATE: YES
```

The v0.0.6 line can now validate that an existing Effective Project Profile is
structurally canonical and source-consistent with one validated Project
Application snapshot and one validated source-release-bound SCAF PAO domain.

The remaining bounded consumption gap is generation:

> Given one exact project scope and a validated Project Application snapshot,
> can SCAF deterministically construct the accepted complete-domain profile
> without inventing applicability decisions and without requiring a human or AI
> to manually author hundreds of derived absence entries?

v0.0.6rc13 adds that deterministic generation boundary.

The governing rule is:

> **The rc13 generator may project validated recorded dispositions and validated
> exact-pair absence into the accepted Effective Project Profile representation.
> It shall not create or approve an engineering applicability judgment.**

## 2. Scope of rc13

rc13 adds:

```text
tools/scaf_effective_project_profile_generator/
```

Supported programmatic generation is:

```text
generate_effective_project_profile(
    repo_root,
    project_scope_ref,
    project_application_path=None,
) -> bytes
```

The production CLI is:

```text
python -m tools.scaf_effective_project_profile_generator.generator \
  --scope <project_scope_ref>
```

An alternate Project Application dataset may be selected:

```text
python -m tools.scaf_effective_project_profile_generator.generator \
  --scope <project_scope_ref> \
  --project-application <project-application.yaml>
```

Successful stdout contains only the generated canonical YAML bytes. The rc13
production CLI does not introduce a persistent profile registry or a built-in
write-back/output-file command.

## 3. Production Input Boundary

The production caller may select only:

```text
exact project_scope_ref
Project Application source path
```

The production caller cannot select or replace:

```text
SCAF repository root
Effective Project Profile schema
Project Application schema
authority registry
authority-registry schema
canonical normative source tree
```

Those contract inputs remain repository-owned.

The function-level `repo_root` exists for controlled programmatic/test isolation,
as with prior accepted SCAF validation/query tools. It is not a production CLI
override.

## 4. Validated-Input Ownership

Before derivation, rc13 captures:

```text
selected Project Application bytes
repository authority-registry bytes
repository authority-registry schema bytes
repository Project Application schema bytes
repository Effective Project Profile schema bytes
canonical normative Markdown bytes
```

into a private generation/validation boundary.

The generator then requires:

1. the frozen authority snapshot to pass the existing source-aware authority
   validator;
2. the same captured Project Application snapshot to pass the accepted rc07
   Project Application validator.

The generator does not accept caller-supplied parsed records, caller-built PAO
indices, caller-created validation reports, or caller-created validated
contexts as substitutes for those checks.

Later derivation consumes the same captured private snapshots.

## 5. Source-Release Determination

For a validated Project Application dataset containing records, rc13 derives the
profile source release from the validated records' `scaf_source_release`.

The accepted current Project Application representation also permits:

```yaml
records: []
```

For that valid zero-record case, no record-level source-release value exists.
rc13 therefore derives the source release from the repository-owned accepted
Project Application schema's `scaf_source_release` constant.

This fallback is deliberately repository-contract-owned. The caller does not
supply a source-release override.

The generator implementation does not permanently hard-code:

```text
v0.0.2
218
```

The current accepted schema/domain still resolves to v0.0.2 and 218 PAOs, but
those values are consumed from the reviewed repository contracts/sources.

## 6. PAO Domain Derivation

After frozen authority proof, rc13 derives the complete profile domain as all
validated authority records satisfying:

```text
authority_class == Project-Applicable Obligation
source_release  == derived Project Application source release
```

The resulting PAO IDs are ordered by exact `scaf_authority_id` ascending.

Framework Normative Invariants and unknown IDs are not profile entries.

The generator does not infer domain membership from L3 traces, Pattern
availability, project artifacts, naming conventions, or previously generated
profiles.

## 7. Exact-Scope State Derivation

The caller-selected `project_scope_ref` is an opaque non-empty exact string.
rc13 performs no scope resolution, hierarchy, aliasing, inheritance, wildcard,
parent/child propagation, or normalization.

For each PAO in the validated domain, rc13 looks up exactly:

```text
(scaf_authority_id, project_scope_ref)
```

in the validated current Project Application snapshot.

If an exact current record exists, rc13 projects only:

```text
record.applicability
record.record_id
```

into the profile entry:

```text
applicable       -> applicable + project_application_record_id
not_applicable   -> not_applicable + project_application_record_id
undetermined     -> undetermined + project_application_record_id
```

If no exact current record exists, rc13 derives:

```text
no_current_disposition
```

with no synthetic Project Application record identity.

Therefore:

```text
recorded profile state
= copy of validated current exact-pair Project Application disposition

no_current_disposition
= exact-pair absence in the selected validated Project Application snapshot
```

No other source may set the profile state.

## 8. No Applicability Inference

The generator shall not derive `applicable`, `not_applicable`, or `undetermined`
from:

```text
L3 trace presence or relation type
Pattern availability
another project scope
scope naming
project-reference naming
implementation artifacts
verification evidence
compliance artifacts
absence of a Project Application record
AI recommendation
```

Record absence produces only profile-only `no_current_disposition`.

The generator does not resolve an `undetermined` state. If the validated source
record says `undetermined`, the generated profile says `undetermined`.

## 9. Exact Project Application Snapshot Provenance

The generated profile records:

```text
project_application_source_sha256
```

as SHA-256 of the exact captured Project Application source bytes consumed by
generation.

The digest retains the accepted rc10 meaning:

```text
exact source-snapshot provenance only
```

It does not establish signer identity, project approval, trust, semantic
equivalence between different serializations, engineering correctness, or
compliance evidence.

## 10. Deterministic Canonical Serialization

rc13 emits the accepted rc10 root order:

```text
profile_kind
representation_release
scaf_source_release
project_scope_ref
project_application_source_sha256
entries
```

Recorded entry order:

```text
scaf_authority_id
profile_state
project_application_record_id
```

Absence entry order:

```text
scaf_authority_id
profile_state
```

Entry sequence order:

```text
exact scaf_authority_id ascending
```

The accepted `profile_kind` and profile `representation_release` constants are
read from the repository-owned accepted rc11 profile schema rather than
inventing a new rc13 serialization release.

Scalar serialization uses deterministic double-quoted YAML strings and one
trailing newline. No timestamps, machine paths, random IDs, state-count copies,
or generator-environment metadata are emitted.

Physical order remains representation determinism only. It has no engineering
priority or authority meaning.

## 11. Non-Duplication of Project Application Truth

The generated profile does not copy:

```text
disposition_basis
decision_refs
authority_refs
supporting_refs
unresolved_reason
awaiting_refs
```

Recorded states retain only `project_application_record_id` as the trace back to
project-side disposition truth.

This prevents the generated profile from becoming a second independently
editable rationale/provenance source.

## 12. rc12 Self-Validation Before Emission

After deterministic derivation and serialization, rc13 writes the generated
bytes only to a private temporary profile snapshot and invokes the accepted
rc12 source-aware validator against:

```text
generated profile snapshot
same captured Project Application snapshot
same private repository validation boundary
```

The public API returns bytes only if rc12 reports PASS.

The production CLI writes bytes to stdout only if that same self-validation
passes.

Thus:

```text
generator output
        ↓
accepted rc12 representation/source proof
        ↓ PASS only
returned / emitted canonical YAML
```

This is a generator correctness boundary. It does not convert rc12 PASS into an
engineering/compliance/release verdict.

## 13. No Persistent State or Write-Back

rc13 does not create or maintain:

```text
persistent Effective Project Profile registry
profile cache
profile history
profile supersession state
Project Application write-back
authority-registry write-back
CI completion state
```

The CLI deliberately emits canonical YAML to stdout. A caller may explicitly
redirect stdout using ordinary operating-system facilities, but persistence is
outside generator authority.

## 14. Empty Project Application Dataset

A validated zero-record Project Application dataset generates a complete PAO
profile containing only:

```text
no_current_disposition
```

for the selected exact scope.

This does not mean the scope does not exist, the project has failed, every PAO
is not applicable, or the project is incomplete. It means only that the
selected validated current Project Application snapshot has no exact-pair
records.

The generated profile must still pass rc12 source-aware validation before it is
returned.

## 15. Authority Boundary

Successful generation establishes only:

```text
validated repository/source inputs were consumed
+
accepted deterministic profile projection rules were applied
+
accepted rc12 representation/source validation accepted the result
```

It does not establish:

```text
applicability correctness
not_applicable rationale adequacy
resolution of undetermined issues
scope correctness or approval
Project Design Authority approval
Pattern recommendation or selection
implementation satisfaction
verification/evidence sufficiency
compliance
risk acceptance
project completion
release readiness
closure
```

The governing separation remains:

```text
machine-determinable projection
!= engineering judgment
!= project authority decision
!= verification result
!= compliance result
!= closure
```

## 16. Explicit Non-Goals / Deferred Scope

rc13 does **not** add:

- a persistent generated profile file as repository authority;
- a profile registry/cache;
- profile history/supersession/re-evaluation semantics;
- profile read/query APIs beyond generation and existing validation;
- project-scope registry/resolver/hierarchy;
- project-reference resolution;
- automatic applicability inference;
- AI approval of engineering rationale;
- Project Design Authority automation;
- Pattern recommendation/selection;
- implementation/satisfaction/compliance determination;
- verification/evidence/closure determination;
- project completion PASS/FAIL;
- AI context packaging;
- CI applicability-completion enforcement;
- code generation from profile state;
- new L3 Pattern content;
- L4 guidance;
- Development Context Recovery / `.scaf/work-checkpoint.yaml` capability.

## 17. Canonical Example Outcome

For the accepted illustrative Project Application dataset and exact scope:

```text
example:scope:system
```

rc13 generates the accepted rc10 canonical fixture content, excluding only the
non-authoritative fixture comments:

```text
D = 218
applicable               1
not_applicable           0
undetermined             0
no_current_disposition 217
```

The recorded entry is:

```text
SCAF-AK-001
applicable
EXAMPLE-PA-001
```

For:

```text
example:scope:stateless-node
```

`SCAF-AK-002` is generated as `not_applicable` and `SCAF-AK-001` does not carry
across scopes.

For:

```text
example:scope:interface-if3
```

`SCAF-AK-003` remains valid `undetermined`.

For an unmatched exact scope, all current PAOs are generated as
`no_current_disposition`.

## 18. Review Expectations

Independent review should verify at minimum:

- package/Git predecessor is committed accepted rc12;
- effective change surface is exactly the intended rc13 generator/documentation surface;
- accepted rc09/rc10/rc11/rc12 inputs remain unchanged;
- public generation API owns validation and does not accept parsed/context substitutions;
- CLI exposes only `--scope` and `--project-application` project-side selectors;
- authority/normative and Project Application snapshots are captured before downstream consumption;
- invalid authority proof blocks generation;
- invalid Project Application blocks generation;
- source release/domain are not permanently hard-coded to v0.0.2/218;
- zero-record Project Application input uses the repository-owned schema source-release binding and generates complete absence state;
- exact-scope recorded states copy only accepted Project Application applicability/record ID;
- cross-scope dispositions do not carry over;
- unmatched scope produces only complete-domain `no_current_disposition`;
- generated source digest equals exact captured Project Application bytes;
- canonical output order is deterministic;
- canonical system-scope output equals the accepted rc10 fixture content apart from non-authoritative comments;
- generated output does not duplicate rationale/provenance fields;
- generated output passes accepted rc12 validation before emission;
- repeated identical inputs produce byte-identical output;
- generation does not create a persistent profile artifact or write source files;
- `undetermined` remains a valid unresolved engineering state;
- no applicability/compliance/Pattern/verification/closure inference is introduced;
- rc13 and all accepted/frozen regression suites pass.

## 19. Acceptance Position

v0.0.6rc13 is acceptable only if deterministic profile generation remains a
validated projection mechanism rather than a new engineering decision source.

A clean rc13 review may permit a later separately reviewed consumption/context
step or milestone-consolidation decision. It does not pre-authorize either.
