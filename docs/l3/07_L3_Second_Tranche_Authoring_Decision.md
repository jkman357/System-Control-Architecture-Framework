# SCAF L3 Second-Tranche Authoring Decision

**Development Release:** v0.0.3rc10  
**Decision Scope:** controlled second representative L3 tranche  
**Upstream Baseline:** frozen v0.0.2 L1/L2  
**Decision Type:** Pattern-ID allocation and Candidate/M1 authoring from rc07-approved categories

## 1. Purpose

This release-scoped record documents why v0.0.3rc08 allocates exactly five new Pattern identities after the independent v0.0.3rc07 coverage / second-tranche planning review returned:

```text
L3 SECOND-TRANCHE PLANNING GATE: YES
```

The rc07 review found no Critical, Major, Minor or Trivial release/regression finding, independently reproduced the 60/218 controlled trace-reference coverage view, and authorized later Pattern-ID allocation from six approved candidate categories.

This record does not modify frozen L1/L2 authority, does not change the first seven `Available / M2` entries, and does not authorize M2/Available status for the five new entries.

## 2. rc07 Category Disposition

| rc07 candidate category | rc07 disposition | rc08 action |
|---|---|---|
| Failure-Domain Containment / Isolation (`FTL`) | APPROVE FOR SECOND-TRANCHE AUTHORING | allocate `SCAF-PAT-FTL-001` |
| Controlled Failover with Graceful Degradation (`FTL`) | APPROVE FOR SECOND-TRANCHE AUTHORING | allocate `SCAF-PAT-FTL-002` |
| Bounded Queue / Backpressure / Overload Protection (`TIM`) | APPROVE FOR SECOND-TRANCHE AUTHORING | allocate `SCAF-PAT-TIM-001` |
| Timebase / Clock-Relationship / Epoch Validity (`TIM`) | APPROVE FOR SECOND-TRANCHE AUTHORING | allocate `SCAF-PAT-TIM-002` |
| Generation/Epoch-Based Cross-Participant State Convergence (`SYN`) | APPROVE FOR SECOND-TRANCHE AUTHORING | allocate `SCAF-PAT-SYN-001` |
| Evidence Retrieval / Export / Transformation Integrity (`EVD`) | APPROVE FOR SECOND-TRANCHE AUTHORING | **approved but deferred** to keep rc08 focused on opening FTL/TIM/SYN |
| Controlled Configuration Activation / Source Precedence (`PST`) | REJECT / REFRAME | **no ID allocated**; must be reframed/re-reviewed before reconsideration |

SEC-primary realization remains behind the separate security-realization gate identified by rc07.

## 3. New Published Identities

v0.0.3rc08 publishes exactly five new immutable Pattern identities:

- `SCAF-PAT-FTL-001` — Failure-Domain Containment / Isolation;
- `SCAF-PAT-FTL-002` — Controlled Failover with Graceful Degradation;
- `SCAF-PAT-TIM-001` — Bounded Queue / Backpressure / Overload Protection;
- `SCAF-PAT-TIM-002` — Timebase / Clock-Relationship / Epoch Validity;
- `SCAF-PAT-SYN-001` — Generation/Epoch-Based Cross-Participant State Convergence.

All five enter the catalog as:

```text
Catalog Status: Candidate
Maturity: M1 — Structured
Introduced In: v0.0.3rc08
```

Publication makes each ID and its primary-family component subject to the stable-ID / immutable-primary-family rules. Candidate/M1 does not imply availability, recommendation, project selection, compliance, verification or L2 satisfaction.

## 4. Why Five, Not All Six Approved Categories

The rc07 gate authorizes a **small controlled second tranche** from approved categories; it does not require every approved category to be authored immediately.

rc08 deliberately selects five categories because they open the previously empty `FTL`, `TIM` and `SYN` families and provide the highest taxonomy/authority stress value in one focused review. The approved EVD export/transformation category remains available for a later tranche without needing to repeat the rc07 planning approval unless its intended scope materially changes.

## 5. Authority / Family Intent

- `FTL-001` must use Project Design Authority-defined structural/Domain boundaries; it must not redefine ARCH topology.
- `FTL-002` must keep failover/degraded-Service outcome distinct from containment, generic retry and universal redundancy topology.
- `TIM-001` must own only the bounded queue/capacity mechanism; INT retains data-contract semantics and ROB retains post-violation resilience response.
- `TIM-002` must qualify clock/timebase relationship validity without prescribing synchronization technology or taking downstream INT/RUN/ROB authority.
- `SYN-001` must remain a convergence mechanism independent of reconnect; `COM-001` retains reconnect Interaction/session establishment and may compose with SYN.

## 6. Preserved State

v0.0.3rc08 preserves:

- the first seven published entries as `Available / M2`, introduced in v0.0.3rc03;
- their architecture bodies and existing L2 traces unchanged except for current `Development Release` metadata;
- the frozen v0.0.2 normative tree and 294 / 218 / 76 inventory;
- many-to-many L2→L3 trace semantics and the prohibition on generic `satisfies`;
- Project Design Authority ownership of project mechanism selection/configuration;
- external source-authority ownership;
- the L3/L4 boundary.

## 7. Deferred / Closed Gates

v0.0.3rc08 does not:

- author the approved EVD export/transformation Pattern;
- allocate the rejected/reframe PST candidate;
- create a SEC-primary Pattern;
- promote any new entry beyond Candidate/M1;
- promote any existing entry to M3/M4;
- start L4 guidance;
- introduce schema, validator, generated registry/index, CI, code generation or executable governance.

## 8. Immediate Gate

The immediate gate is an independent **second-tranche Pattern review**. It shall review all five new entries entry-by-entry for family identity, L2 trace classification, PDA/source-authority boundaries, non-duplication with existing Patterns, composition semantics and L3/L4 conformance.

No new second-tranche entry may advance to M2 or `Available` until that review and any required closure cycle are completed.
