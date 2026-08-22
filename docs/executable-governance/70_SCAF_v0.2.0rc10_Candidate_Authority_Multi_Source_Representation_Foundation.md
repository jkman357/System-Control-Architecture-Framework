# SCAF v0.2.0rc10 — Candidate Authority Multi-Source Representation Foundation

**Development Release:** v0.2.0rc10  
**Development Predecessor:** v0.2.0rc09 / Git `57aa72a4e434fbcb8511c33e9a26e2cdf57e4e8a`  
**Formal Authority Release:** v0.1.0 / `294 / 218 / 76`  
**Candidate Authority Target:** `302 / 226 / 76`  
**Layer:** executable-governance candidate representation  
**Status:** Independent-review candidate; formal authority and downstream consumers remain unchanged

## 1. Purpose

The clean rc09 gate authorizes only the bounded Candidate Authority Multi-Source Representation Foundation. rc10 turns the accepted semantic distinction

```text
Authority Set Identity
!=
Authority Record Semantic Provenance
```

into executable candidate governance while keeping the formal authority path immutable.

The problem is no longer candidate-record count alone. The reviewed candidate set now contains two controlled semantic-source tranches:

```text
SCAF-OBS-041..045  -> v0.2.0rc01 OBS candidate overlay
SCAF-OBS-046..048  -> v0.2.0rc08 OBS candidate overlay
```

A correct representation must preserve both provenance relationships while validating one complete candidate authority universe.

## 2. Representation result

rc10 evolves `candidate-authority-registry.yaml`, its candidate-only schema and its separate validator to represent:

```text
294 exact frozen formal records
+ 5 candidate PAOs from rc01
+ 3 candidate PAOs from rc08
= 302 records

226 Project-Applicable Obligations
 76 Framework Normative Invariants
```

The candidate set remains development-only and is not formal authority.

## 3. Candidate Authority Set identity

The representation adds a controlled `authority_set_id` identifying the complete candidate universe. This identity answers which complete validated candidate set is being reasoned about; it does not replace or rewrite per-record semantic provenance.

For rc10 the controlled set identity is:

```text
scaf_candidate_l1_l2_authority_set_v0.2.0rc10
```

This token is owned by the candidate representation/schema/validator. It is not a new formal release identity and is not a Project Application source-release substitute.

## 4. Controlled candidate sources

The previous singular `candidate_source_*` fields are replaced by exactly two controlled candidate-source definitions:

```text
scaf_obs_v0.2.0rc01
  path: docs/normative-evolution/80_SCAF_OBS_Observability_Diagnostics_Incident_Evidence_Obligations_v0.2.0rc01.md
  release: v0.2.0rc01
  owns: SCAF-OBS-041..045

scaf_obs_v0.2.0rc08
  path: docs/normative-evolution/80_SCAF_OBS_Observability_Diagnostics_Incident_Evidence_Obligations_v0.2.0rc08.md
  release: v0.2.0rc08
  owns: SCAF-OBS-046..048
```

Each source definition is byte-bound by SHA-256. Candidate sources are representation-owned inputs; the validator does not scan the repository, union arbitrary overlays, or accept caller-selected source paths.

## 5. Per-record semantic provenance

Each candidate record carries `source_ref` and retains source path/release fields. `source_ref` must resolve to one controlled candidate source, the candidate ID must be owned by that source, and the record path/release must agree with the referenced source.

Therefore:

```text
SCAF-OBS-041..045
  source_ref     = scaf_obs_v0.2.0rc01
  source_release = v0.2.0rc01

SCAF-OBS-046..048
  source_ref     = scaf_obs_v0.2.0rc08
  source_release = v0.2.0rc08
```

The rc08 complete overlay reproduces `SCAF-OBS-041..045`, but that reproduction does not reassign their accepted rc01 semantic provenance.

## 6. Source-aware reconstruction

For each controlled source the validator:

1. verifies repository-relative path ownership;
2. verifies the declared SHA-256 against source bytes;
3. resolves each source-owned candidate heading;
4. requires exactly one `Target` field for each owned candidate ID;
5. verifies candidate record authority class against the bound source Target;
6. verifies record `source_ref`, path, release and anchor consistency.

A later complete overlay may contain reproduced earlier candidate blocks. Presence alone does not establish source ownership; ownership comes from the controlled source definition and per-record binding.

## 7. Frozen formal projection remains exact

Formal validation remains a fail-stop prerequisite. Candidate reasoning returns immediately if frozen authority validation fails.

After that prerequisite passes, rc10 still requires all 294 formal records in the candidate registry to be exact data projections of `authority-registry.yaml`. Multi-source candidate evolution does not permit candidate tooling to alter frozen formal records.

## 8. Invalid conditions explicitly prevented

rc10 must reject at least:

- `SCAF-OBS-046..048` bound to the rc01 source;
- unknown `source_ref` values;
- record source path/release disagreement with `source_ref`;
- missing, duplicated or overlapping candidate-source ownership;
- arbitrary extra candidate-source definitions;
- source-byte/hash mismatch;
- source heading/Target mismatch;
- missing or unexpected candidate IDs;
- modification of any frozen formal projection record;
- candidate processing after failed formal validation;
- inventory other than `302 / 226 / 76`.

## 9. Authority and downstream boundary

Successful rc10 validation establishes only a valid development candidate authority representation. It does not:

- promote `SCAF-OBS-041..048` to formal authority;
- decide project applicability;
- decide evidence sufficiency;
- decide engineering closure;
- make candidate authority a production Project Application input;
- migrate Effective Project Profile or later consumers.

The formal Project Application path remains bound to formal `authority-registry.yaml`.

## 10. L3 boundary

rc09 concluded that the L2 semantics are ready for a future Evidence-Driven Engineering Pattern, but immediate L3 creation was stopped until `SCAF-OBS-046..048` became visible to executable candidate governance.

rc10 satisfies that representation dependency only. It creates no L3 Pattern, no L3 trace relation and no frozen `docs/l3/` change. A clean rc10 review may authorize the next separately gated L3 semantic-candidate step; it does not create that Pattern automatically.

## 11. Mechanism neutrality

This representation does not mandate Git as the evidence/change mechanism, a runtime logger, retained RAM, Flash, SD, USB, DAT, a build-ID syntax, a board-ID format, CI provider, probe API or AI provider. SHA-256 here is a repository artifact-integrity mechanism for this candidate representation, not a universal runtime-evidence format requirement.

## 12. Explicitly deferred / stopped

```text
Candidate Project Application migration     PARK
Effective Project Profile migration         PARK
Consumption / Context migration             PARK
Evidence-Driven Engineering L3 Pattern      DEFER to next gate
L4 expansion                                STOP / DEFER
Code generation                             STOP / DEFER
Generic runtime-instrumentation CI          STOP / DEFER
```

## 13. Acceptance boundary

A clean rc10 review must establish all of the following:

- exact rc09 Git predecessor identity;
- candidate registry/schema/validator form one coherent multi-source contract;
- two source artifacts are controlled and byte-bound;
- source ownership is exactly `041..045` from rc01 and `046..048` from rc08;
- per-record source provenance is consistent with that ownership;
- formal projection is exactly 294 records;
- executable candidate result is exactly `302 / 226 / 76`;
- formal-prerequisite fail-stop remains intact;
- bounded invalid-source/provenance conditions are rejected;
- formal Project Application and frozen L3 remain unchanged;
- no downstream or L3 implementation expansion occurs.

A YES gate authorizes only the next dependency/value-controlled development step. It does not itself promote candidate authority or freeze v0.2.0.
