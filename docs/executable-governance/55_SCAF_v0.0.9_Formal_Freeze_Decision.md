# SCAF v0.0.9 — Formal Freeze Decision

**Date:** 2026-08-19  
**Status:** Frozen Context Source Association and Source-Aware Validation Baseline  
**Freeze Source:** `v0.0.9rc05`  
**Freeze Source Commit:** `0fea6cfb7f5eba8a4a7e4f38868d50b9f3264b3e`  
**Independent Review:** `V0.0.9RC05 CONTEXT SOURCE ASSOCIATION SOURCE-AWARE VALIDATOR FOUNDATION GATE: YES`

## 1. Explicit Governance Decision

The independently reviewed `v0.0.9rc05` source state is formally frozen as:

```text
SCAF v0.0.9 — Frozen Context Source Association and Source-Aware Validation Baseline
```

This freeze is an explicit governance decision made after the clean rc05 review and the required post-review dependency/value assessment.

No new semantic or executable capability is introduced by the freeze itself. Relative to committed rc05, the formal release changes only release-state/navigation documentation and adds this freeze-decision record.

## 2. Freeze Basis

The corrected rc05 independent review reported:

```text
Critical: 0
Major:    0
Minor:    0
Trivial:  0
Blocking review-evidence limitations: 0

V0.0.9RC05 CONTEXT SOURCE ASSOCIATION
SOURCE-AWARE VALIDATOR FOUNDATION GATE: YES
```

The review independently confirmed:

```text
source delta: 7 Added / 3 Changed / 0 Removed
exact rc04 predecessor: PASS
frozen/prior accepted surfaces: unchanged
rc05 validator regressions: 25 / 25 PASS
upstream Consumption Selection regressions: 37 / 37 PASS
repository-owned production checks: PASS
git diff --check: PASS
```

The reviewed rc05 source ZIP SHA-256 was:

```text
1ecd58ebc50b5a30fcfd52994da687594fbafb0fd411fda0db6f58e9ecdd0dca
```

The first rc05 review attempt was blocked only because the review instructions incorrectly stated `8 Added / 3 Changed / 0 Removed` while enumerating and supplying seven added source files. The rc05 source ZIP was not changed or respun. The review instructions were corrected to `7 Added / 3 Changed / 0 Removed`, after which a fresh independent review returned the clean gate above.

This review-evidence correction did not modify candidate source and did not create a source finding.

## 3. v0.0.9 Development Chain

The frozen v0.0.9 line is the accepted sequence:

```text
v0.0.9rc01
Context Source Resolution semantics
        ↓
v0.0.9rc02
canonical representation-neutral logical model
        ↓
v0.0.9rc03
canonical deterministic YAML representation
        ↓
v0.0.9rc04
JSON Schema Draft 2020-12 structural contract
        ↓
v0.0.9rc05
production source-aware validator
        ↓
v0.0.9
formal frozen baseline
```

Each RC was separately gated. Progression was not automatic: every follow-on RC required a clean review plus a dependency/value assessment under the frozen v0.0.8 lifecycle-proportional governance rule.

## 4. Frozen Scope

v0.0.9 freezes the accepted Context Source Association chain from validated Consumption Selection output to deterministic source-aware association validation.

The frozen scope includes:

- Context Source Resolution semantic boundaries over validated Consumption Selection included domain `I`;
- the representation-neutral Context Source Association logical model;
- exact upstream Consumption Selection binding;
- complete `I` coverage with explicit zero-association semantics;
- shared Source Unit Catalog and many-to-many authority/source association cardinality;
- atomic Controlled Source Association semantics;
- relationship semantic, relationship scope, association provenance and bounded Authority Qualification separation;
- Source Identity, optional Instance Constraint and runtime-resolved Source Instance separation;
- deterministic canonical YAML representation;
- JSON Schema Draft 2020-12 parsed-instance structural contract;
- production source-aware validator;
- deterministic catalog/reference/semantic uniqueness and canonical-order checks;
- bounded path-safe exact-byte SHA-256 proof for explicitly declared repository-local `repo:<repository-relative POSIX path>` identities.

## 5. Governing Semantic Separations

The frozen baseline preserves:

```text
source relationship != source authority
source identity != exact source instance
discovery candidate != controlled association
relationship semantic != authority qualification
source ownership != association provenance
resolvable != current
source exists != obligation satisfied
source resolution != content loading / Context Assembly
```

The central two-plane invariant remains:

```text
controlled association truth
!= runtime resolution observation
```

A controlled association therefore does not disappear or change merely because a future resolver might observe the source as missing, unresolvable, stale, superseded or otherwise not current.

## 6. Representation and Validation Ownership

The frozen executable ownership separation is:

```text
parsed-instance structural validity
!= source-aware consistency
!= engineering correctness
```

The rc04 schema owns parsed-instance structure only.

The rc05 validator owns deterministic source-aware consistency for accepted inputs, including:

```text
strict YAML / canonical raw representation
rc04 structural schema
exact Consumption Selection bytes and binding proof
accepted upstream Consumption Selection validation
validated I reconstruction
Authority Source Entry coverage == validated I
Source Unit identity/reference consistency
unused Source Unit absence
semantic association uniqueness
canonical ordering
bounded explicit repository-local SHA-256 instance proof
```

A validator PASS does not mean:

```text
applicable engineering decision is correct
Project Design Authority has approved a design
implementation satisfies an obligation
verification is sufficient
risk is accepted
compliance is established
release is ready
closure is complete
```

Those remain owned by their existing engineering authorities and lifecycle evidence.

## 7. Validated-Input Ownership

The association artifact does not self-assert the authority domain it covers.

The frozen validation chain is:

```text
exact Consumption Selection bytes
        ↓
accepted Consumption Selection source-aware validation PASS
        ↓
validated included domain I
        ↓
Context Source Association coverage proof
```

If upstream validation fails, downstream `I` coverage proof does not proceed.

This preserves the existing SCAF rule that downstream machine-readable artifacts consume validated upstream truth rather than recreating it independently.

## 8. Explicit Zero Association

The frozen representation preserves:

```text
missing Authority Source Entry
!= explicit Authority Source Entry with associations: []
```

Every authority in validated `I` is represented exactly once in a complete association set, including authorities with zero current controlled associations.

This prevents omitted representation from silently becoming controlled absence truth.

## 9. Source Unit and Association Model

The frozen Source Unit Catalog preserves:

```text
one selected authority -> 0..n Source Units
one Source Unit         -> 1..n selected authorities
```

A Controlled Source Association remains one atomic statement composed of:

```text
one selected authority
+ one Source Unit
+ one relationship semantic
+ one relationship scope
+ controlled association provenance
+ optional bounded Authority Qualification
+ optional Instance Constraint
```

If one authority/source pair has materially different relationship semantics, those remain separate atomic associations rather than a single ambiguous multi-role assertion.

## 10. Authority Boundary

v0.0.9 creates no new engineering authority.

The frozen authority inventory remains:

```text
Authority records:              294
Project-Applicable Obligations: 218
Framework Normative Invariants:  76
```

No new `SCAF-AK-*` authority ID, PAO or FNI is introduced by v0.0.9.

`authority_qualification` remains property/relationship-scope bounded and must be grounded in existing authority ownership. A generic file-global `authoritative: true` shortcut remains outside the frozen model.

## 11. Exact Opaque Project Scope

The frozen v0.0.9 chain preserves the exact opaque `project_scope_ref` inherited through the validated Consumption Selection binding.

v0.0.9 introduces no:

```text
scope hierarchy
scope alias
scope wildcard
parent/child propagation
path-derived scope
cross-scope inheritance
scope resolver
```

Any future scope-resolution model requires a separately justified version/RC boundary.

## 12. Bounded Repository-Local Byte Proof

The rc05 validator supports exact instance proof only for an already-declared identity of the form:

```text
repo:<repository-relative POSIX path>
```

when an explicit SHA-256 `instance_constraint` requires byte proof.

The validator rejects unsafe path forms and proves the SHA-256 of the explicitly referenced bytes.

This capability is intentionally bounded:

```text
direct proof of declared repository-local identity
!= repository source discovery
!= general Source Resolver
```

## 13. Dependency / Value Assessment and STOP Decision

After the clean rc05 review, the required dependency/value assessment asked whether v0.0.9 required a further RC for a general Source Resolver, runtime Resolution Observation model, source discovery/currentness logic, or downstream Context Assembly.

The assessment concluded:

```text
If work stops after rc05 now:

1. material semantic ambiguity remains?                         NO
2. validator implementations can legitimately diverge?         NO
3. an existing executable capability is blocked?               NO
4. stopping now creates an expensive/irreversible commitment?  NO
5. a current real consumer requires general source resolution? NO
```

Therefore:

```text
no material current dependency
        ↓
resolver work is not currently justified
        ↓
STOP
        ↓
freeze v0.0.9
```

This is an intentional STOP decision under frozen v0.0.8 governance, not an unfinished hidden gate.

## 14. Explicitly Deferred Capabilities

The following remain outside frozen v0.0.9 and are not pre-authorized by this freeze:

```text
general Source Resolver
repository/filesystem source discovery
Git-history traversal
remote/external source fetching
candidate-source discovery
semantic similarity mapping
runtime Resolution Observation representation
missing/unresolvable/stale/superseded/currentness state model
automatic source currentness/supersession policy
content extraction
fragment/chunk loading
ranking / priority / token-budget policy
AI Context Assembly / prompt construction / model orchestration
CI gate integration for source associations
scope resolver / hierarchy / inference
normative authority-registry expansion
new PAO/FNI
L4 implementation / verification guidance
```

Each future capability requires a new Current Decision Horizon and dependency/value justification.

## 15. External Pattern / Licensing Boundary

The reviewed v0.0.9 source line contains no direct incorporation of third-party code bodies, prompts, schema bodies, documentation passages or example content as part of the Context Source Association design.

The source-aware validator uses existing repository dependencies such as PyYAML and `jsonschema`; dependency use does not itself transfer engineering authority into SCAF.

Future direct incorporation of third-party implementation, text, schema, prompt or examples remains subject to separate license, copyright, attribution, NOTICE, redistribution and trademark review as applicable.

## 16. Frozen Inventory / Evidence

Accepted current evidence at freeze includes:

```text
Authority records:                         294
PAO:                                       218
FNI:                                        76
L3 Patterns:                                12
L3 Relations:                              119
Consumption Selection D/E/I/O/X:   218 / 3 / 2 / 1 / 215
rc05 Context Source Association tests: 25 / 25 PASS
upstream Consumption Selection tests: 37 / 37 PASS
repository-owned production checks: PASS
```

The historical pre-rc05 262-test inventory was not represented as rerun by the clean rc05 independent review because the corrected bounded-review conditions were satisfied. The freeze does not rewrite that historical evidence as newly executed evidence.

## 17. Formal Immutability Rule

After the formal freeze commit is created, `v0.0.9` is immutable.

Future work shall:

```text
not modify v0.0.9 in place
not respin v0.0.9 under the same formal version
not silently add resolver/currentness semantics to the frozen validator
not reinterpret validator PASS as engineering correctness or closure
not infer authorization for deferred Context Assembly or L4 capabilities
```

Any later change shall begin from a new controlled version/RC line with an explicit Current Decision Horizon.

## 18. Final Decision

The reviewed rc01→rc05 Context Source Association chain is coherent, machine-readable, structurally constrained and source-aware validated for its accepted boundary. The post-rc05 dependency/value assessment identifies no material current dependency requiring a further resolver RC.

The explicit governance decision is therefore:

```text
SCAF v0.0.9
Frozen Context Source Association and Source-Aware Validation Baseline

Freeze source:
v0.0.9rc05
0fea6cfb7f5eba8a4a7e4f38868d50b9f3264b3e

Formal status:
FROZEN / IMMUTABLE
```
