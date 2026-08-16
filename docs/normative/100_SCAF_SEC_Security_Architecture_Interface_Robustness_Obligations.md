# SCAF-SEC — Security Architecture Interface & Robustness Obligations

**Release:** v0.0.2  
**Concern:** `SCAF-SEC`  
**Layer:** L1 Concern Authority + L2 Required Project Decisions  
**Status:** Normative RC

## 1. Purpose

`SCAF-SEC` **Defines Framework Semantics / Obligation** for the system security-architecture interface and robustness boundary: security-relevant assets/subjects/relationships; trust/security semantics; peer/subject identity, authentication and authorization architecture obligations; confidentiality/integrity/authenticity requirements where applicable; hostile freshness/anti-replay interfaces; credential/key lifecycle architecture interfaces; privilege/separation obligations; malformed/hostile-input and resource-abuse resistance; compromise/trust-loss consequences and containment interfaces; security-sensitive lifecycle/configuration constraints; security-service failure/re-establishment interfaces; and security evidence needs.

SCAF does **not** replace a project's external/project cybersecurity, threat, security-risk or regulatory acceptance authority. The applicable **Security Authority** remains the source authority for threat assumptions/model, security objectives/requirements, security risk evaluation/acceptance, regulatory/certification security acceptance and externally imposed security constraints. The **Project Design Authority Defines Project Instance / Decision** for the actual project trust/security architecture, allocations, mappings, project values and responsibility assignments using those controlled inputs. If one team/person performs multiple roles, those authority capacities remain semantically distinct.

`SCAF-SEC` is an architecture-interface concern, not a complete cybersecurity framework and not a cryptographic/credential implementation catalog. It does not define a universal threat model, risk-acceptance basis, cryptographic suite, credential format, key hierarchy, certificate model, secure element, security protocol, access-control mechanism or secure-storage technology.

## 2. L1 Authority Boundary

`SCAF-SEC` **Defines Framework Semantics / Obligation** for:

- applicability and trace of security-relevant architecture concerns to controlled Security Authority inputs;
- security-relevant assets, subjects/peers, trust relationships and protection objectives as architecture inputs without creating new core metamodel entities;
- security/trust semantics that constrain controlled ARCH structural decisions without redefining Node/Domain/topology authority;
- security-relevant peer/subject identity, authentication and authorization result semantics and responsibility assignment;
- confidentiality, integrity/authenticity and hostile-freshness/anti-replay obligations where Applicable;
- credential/key lifecycle architecture interfaces, including controlled issuance/provisioning/activation/use/revocation/expiry/rotation/retirement semantics where Applicable, without prescribing a key-management mechanism;
- privilege/separation and security-sensitive control/management-access obligations;
- malformed/hostile-input and resource-abuse security consequences using controlled INT/TIME/ROB semantics;
- compromise/trust-loss significance, security-specific denial/degradation constraints and handoff to ROB resilience response;
- security constraints on LIFE boot/update/activation and CFG-controlled security-relevant facts without taking LIFE/CFG authority;
- security evidence needs handed to OBS and verification claims handed to ASSUR without taking evidence/sufficiency authority;
- traceability and re-evaluation when controlled threat/objective/constraint/architecture assumptions change.

The **Project Design Authority Defines Project Instance / Decision** for actual trust/security allocations, selected project security policies/values where delegated, authentication/authorization architecture, protection requirements, privilege boundaries, security-sensitive lifecycle/configuration mappings and responsibility assignments, constrained by the applicable Security Authority and other source concerns.

## 3. Project-Applicable Obligations

### `SCAF-SEC-001` — Material security concern identification

**Target:** Project-Applicable Obligation

The project **SHALL** identify each security-relevant architecture concern whose omission, ambiguity, hostile manipulation, unauthorized use, loss of required protection, trust failure, compromise or security-service failure can materially affect an applicable Function, Capability, Service, Interaction, architecture/lifecycle/configuration decision, resilience decision, verification obligation or external security/safety/regulatory/risk constraint.

### `SCAF-SEC-002` — Security Authority input and provenance

**Target:** Project-Applicable Obligation

For each material SEC concern, the project **SHALL** identify and trace the controlled Security Authority or other applicable external/project authority inputs that provide threat assumptions/model, security objectives/requirements, security risk constraints/acceptance basis, regulatory/certification constraints, authorization/trust constraints or other security-originated source decisions used by the project.

The project **SHALL NOT** treat a SCAF-SEC obligation, implementation artifact or architecture record as a replacement source for those external/project authority decisions merely because it records or integrates them.

### `SCAF-SEC-003` — Security-relevant asset / subject / service scope

**Target:** Project-Applicable Obligation

Where protection depends on distinguishing security-relevant assets, data, Functions, Services, participants, subjects/peers, administrative/control capabilities or other protected architecture interests, the project **SHALL** define the project representation and consequence needed to identify what requires controlled security treatment and why.

**Boundary note (informative):** this obligation does not add Asset, Principal, Credential or Threat as SCAF core metamodel entities.

### `SCAF-SEC-004` — Trust / security relationship semantics

**Target:** Project-Applicable Obligation

Where project behavior depends on a trust/security relationship between Systems, Nodes, Roles, Services, Interfaces, Interactions, Domains or external participants, the project **SHALL** define the required trust/security semantics, permitted assumptions and consequence when the required relationship is absent, unknown, revoked, violated or cannot be established.

**Boundary note (informative):** `SCAF-ARCH` retains actual structural Node/Domain/topology authority; SEC supplies the controlled security/trust semantics and constraints used by the architecture decision.

### `SCAF-SEC-005` — Security-relevant peer / subject identity semantics

**Target:** Project-Applicable Obligation

Where a security decision depends on distinguishing a peer, subject, actor, device identity, service identity, administrative identity or other security-relevant claimant, the project **SHALL** define the controlled security identity/reference semantics, identity source/provenance, ambiguity/unknown handling and project consequence needed for the applicable security decision.

A security-relevant identity **SHALL NOT** be treated as identical to `SCAF-INT` Protocol/Connection Session Identity merely because one session carries or is associated with that identity.

### `SCAF-SEC-006` — Authentication applicability and result semantics

**Target:** Project-Applicable Obligation

Where authentication is material, the project **SHALL** define what claim/subject/peer is authenticated, the controlled authentication-result semantics, the responsibility that determines/maintains the authoritative project authentication result, and the consequence of failure, unknown, indeterminate, unavailable or expired authentication state.

**Boundary note (informative):** this obligation does not prescribe a password, certificate, signature, challenge-response, hardware root or other authentication mechanism.

### `SCAF-SEC-007` — Authorization applicability and result semantics

**Target:** Project-Applicable Obligation

Where authorization is material, the project **SHALL** define the protected action/resource/Service/transition to which the authorization applies, the controlled authorization decision basis, the responsibility that determines/maintains the authoritative project authorization result, and the consequence of denied, unknown, indeterminate, stale or unavailable authorization state.

The authorization decision **SHALL** trace to the applicable Security Authority/PDA-controlled policy or constraint and **SHALL NOT** be inferred solely from successful communication, authentication, configuration presence or possession of an artifact unless the controlled project decision explicitly establishes that relationship.

### `SCAF-SEC-008` — Security-decision unknown / indeterminate semantics

**Target:** Project-Applicable Obligation

Where a security-sensitive decision may be unknown, indeterminate, unavailable, conflicting, stale or based on insufficiently established identity/trust/authorization information, the project **SHALL** define the controlled representation/decision semantics and the consequence of proceeding, refusing, degrading or deferring the affected action.

### `SCAF-SEC-009` — Confidentiality applicability and required outcome

**Target:** Project-Applicable Obligation

Where confidentiality is required by the applicable Security Authority/project decision, the project **SHALL** define the protected information/Service/context, the required confidentiality outcome and the controlled consequence when the required confidentiality property cannot be established or maintained.

**Boundary note (informative):** L1/L2 SEC does not prescribe encryption, key size, cipher suite, tunnel, memory protection or storage mechanism.

### `SCAF-SEC-010` — Integrity / authenticity applicability and required outcome

**Target:** Project-Applicable Obligation

Where integrity or authenticity is required, the project **SHALL** define the protected information/action/artifact/context, the required integrity/authenticity outcome, the source/provenance relationship needed to interpret the result, and the consequence when the required property is false, unknown or cannot be established.

**Boundary note (informative):** exchanged-data contract validity remains under `SCAF-INT`; CFG item validity/source semantics remain under `SCAF-CFG`; OBS evidence integrity/provenance remains under `SCAF-OBS`.

### `SCAF-SEC-011` — Hostile freshness / anti-replay semantics

**Target:** Project-Applicable Obligation

Where replay, reuse, duplicated authorization material, stale security state or hostile re-presentation can materially affect a security decision, the project **SHALL** define the required security freshness/anti-replay decision semantics, source identity/session/context dependencies and the consequence when freshness/replay eligibility is false, unknown or cannot be established.

**Boundary note (informative):** `SCAF-INT` retains semantic duplicate/order/session contract meaning and `SCAF-TIME` retains measurable age/timebase/uncertainty properties used by the security decision.

### `SCAF-SEC-012` — Security age / expiry / validity-window consequence

**Target:** Project-Applicable Obligation

Where a security decision depends on age, expiry, validity window, timeout, clock relationship or temporal uncertainty, the project **SHALL** define the security consequence/eligibility decision that consumes the applicable controlled `SCAF-TIME` property and the result when the required temporal basis is unavailable, ambiguous or outside its permitted condition.

The security decision **SHALL NOT** redefine the TIME timebase, clock identity, synchronization, uncertainty, window/deadline value or Time Epoch used to evaluate it.

### `SCAF-SEC-013` — Credential / key lifecycle architecture semantics

**Target:** Project-Applicable Obligation

Where credentials, keys, tokens, trust anchors or equivalent security-enabling material are material to project security decisions, the project **SHALL** define the applicable lifecycle semantics and source responsibility needed to distinguish controlled creation/provisioning, activation/use eligibility, replacement/rotation, revocation, expiry, retirement/destruction or other materially distinct states/results.

The project **SHALL** define the controlled consequence when the required credential/key lifecycle result is unknown, incomplete, unavailable, revoked, expired or cannot be established.

**Boundary note (informative):** this obligation defines security lifecycle semantics/interfaces, not a universal key-management service, secure element, PKI, certificate format or cryptographic implementation.

### `SCAF-SEC-014` — Privilege / separation obligation

**Target:** Project-Applicable Obligation

Where privilege, administrative authority, execution authority, data access or security-sensitive control capability requires separation, the project **SHALL** define the applicable privilege/separation boundary, permitted authority/action relationship, controlled escalation/delegation conditions where applicable, and the consequence of violation, ambiguity or uncontrolled privilege transfer.

**Boundary note (informative):** actual structural separation is a PDA decision under applicable `SCAF-ARCH` obligations; implementation mechanisms belong to Project Realization/`SCAF-PROF`.

### `SCAF-SEC-015` — Security-sensitive management / control path

**Target:** Project-Applicable Obligation

Where a management, maintenance, provisioning, diagnostic, update, administrative or other control path can change security-relevant system behavior or controlled state, the project **SHALL** define the applicable security eligibility/authorization constraints, source authority and consequence of unauthorized, ambiguous or unavailable control authority.

The existence of an Interface, diagnostic capability or configuration channel **SHALL NOT** by itself authorize the security-sensitive action.

### `SCAF-SEC-016` — Malformed / hostile input security consequence

**Target:** Project-Applicable Obligation

Where malformed, adversarially crafted, abusive or otherwise hostile input can materially affect a security objective or protected Function/Service, the project **SHALL** define the security-relevant acceptance/refusal/limitation consequence and trace the contract-level interpretation to the applicable `SCAF-INT` decision and any robustness-significant response to `SCAF-ROB`.

**Boundary note (informative):** this obligation does not prescribe a parser, sanitizer, firewall, packet filter, validation library or protocol-specific defense.

### `SCAF-SEC-017` — Resource-abuse / denial security consequence

**Target:** Project-Applicable Obligation

Where adversarial or unauthorized use of CPU, memory, storage, bandwidth, queue capacity, connection/session capacity, service calls or other controlled resources can materially affect a security objective or required Service, the project **SHALL** define the security consequence and required security eligibility/limitation decision using applicable `SCAF-TIME` measurable resource/capacity properties and, where robustness-significant, applicable `SCAF-ROB` resilience obligations.

### `SCAF-SEC-018` — Compromise / trust-loss significance

**Target:** Project-Applicable Obligation

Where compromise, suspected compromise, credential revocation, trust loss or hostile control of a participant/Service/security responsibility is material, the project **SHALL** define the security-specific interpretation, affected trust/security relationships, affected permissions/claims and the consequence required by the applicable Security Authority/PDA decision.

The project **SHALL** distinguish a security-originated compromise/trust decision from the general ROB health/failure/resilience decision and from RUN operational-state representation.

### `SCAF-SEC-019` — Compromise containment interface

**Target:** Project-Applicable Obligation

Where compromise/trust loss requires limitation of propagation, privilege, communication, configuration effect, lifecycle action or Service access, the project **SHALL** define the required security containment constraint/outcome and trace its structural dependency to controlled `SCAF-ARCH` decisions and its robustness-significant containment/degradation/recovery response to applicable `SCAF-ROB` decisions.

**Boundary note (informative):** SEC does not prescribe network segmentation, process isolation, firewall rules, redundant topology, sandboxing, reset or quarantine mechanism at L1/L2.

### `SCAF-SEC-020` — Security degradation / fallback / downgrade outcome

**Target:** Project-Applicable Obligation

Where a required security property/capability cannot be established, maintained or negotiated, the project **SHALL** define whether operation is denied, limited, degraded, deferred or otherwise controlled, and trace the resulting Function/Service consequence to `SCAF-CTX` and any operational/resilience representation to applicable `SCAF-RUN`/`SCAF-ROB` decisions.

The project **SHALL NOT** silently downgrade to a weaker security condition merely because a stronger mechanism/capability is unavailable unless that downgrade is an explicit controlled project decision consistent with the applicable Security Authority constraints.

### `SCAF-SEC-021` — Security-service dependency / failure interface

**Target:** Project-Applicable Obligation

Where a Function/Service/security decision depends on a security Service or responsibility such as identity, authentication, authorization, credential/trust management or integrity/confidentiality support, the project **SHALL** identify the dependency and define the controlled consequence when that security Service/responsibility is unavailable, inconsistent, compromised, indeterminate or returns an unusable result.

Any robustness-significant health/failure/recovery response **SHALL** trace to applicable `SCAF-ROB` obligations rather than being redefined by SEC.

### `SCAF-SEC-022` — Security constraints on LIFE transactions

**Target:** Project-Applicable Obligation

Where boot, reset, update, activation, rollback or other `SCAF-LIFE` transaction is security-sensitive, the project **SHALL** identify the controlled security authorization/trust/integrity/eligibility inputs required by the lifecycle decision and trace the security result to the applicable LIFE precondition/result mapping.

A security eligibility/authorization result **SHALL NOT** by itself establish LIFE transaction acceptance, completion, activation, rollback or Boot Incarnation.

### `SCAF-SEC-023` — Security constraints on CFG-controlled facts

**Target:** Project-Applicable Obligation

Where security decisions depend on an authorization-related CFG input/fact, trust-related configuration, credential reference, integrity/confidentiality policy input, security mode or other configuration/persistent-state fact, the project **SHALL** trace the security decision to the applicable authoritative `SCAF-CFG` source/value/version/validity/commit semantics and define the security consequence when that controlled CFG fact is unavailable, invalid, incompatible, unknown or not security-eligible.

The security relevance of a CFG value **SHALL NOT** transfer CFG source authority to SEC.

### `SCAF-SEC-024` — Security evidence need / OBS handoff

**Target:** Project-Applicable Obligation

Where operation, diagnosis, incident response, security verification or investigation depends on observing a security-relevant fact/decision/result, the project **SHALL** identify the source-defined security fact/decision/result that must be observable and trace the observation/evidence need to an applicable `SCAF-OBS` project decision.

**Boundary note (informative):** `SCAF-SEC-038` carries the normative SEC/OBS authority partition; SEC does not define OBS evidence identity/provenance/quality/preservation/correlation/export semantics merely because the evidence is security-relevant.

### `SCAF-SEC-025` — Multi-participant security-decision consistency

**Target:** Project-Applicable Obligation

Where multiple participants make or consume related security identity/trust/authentication/authorization/security-eligibility decisions, the project **SHALL** define the required consistency/relationship, authoritative decision/source responsibilities, permitted disagreement/unknown condition and consequence when the required security relationship cannot be established.

**Boundary note (informative):** measurable synchronization/age belongs to TIME; transport/session semantics belong to INT; configuration replication belongs to CFG; no consensus/leader protocol is prescribed.

### `SCAF-SEC-026` — Security trust re-establishment / re-authorization eligibility

**Target:** Project-Applicable Obligation

Where a previously denied, revoked, compromised, expired or indeterminate security relationship may later become eligible for use again, the project **SHALL** define the security-specific eligibility/decision criteria and source authority required to re-establish trust/authorization/security use, together with the consequence when those criteria cannot be established.

**Boundary note (informative):** this security decision does not re-own `SCAF-ROB` general recovery/reintegration semantics or `SCAF-RUN` operational readiness/current-state authority.

### `SCAF-SEC-027` — Security verification-claim identification

**Target:** Project-Applicable Obligation

For each material security decision/property whose satisfaction must be demonstrated, the project **SHALL** identify the security claim/property and trace it to the applicable project verification obligation and evidence need without treating SEC as the authority that determines actual evidence sufficiency.

### `SCAF-SEC-028` — Security decision traceability

**Target:** Project-Applicable Obligation

For each material SEC decision, the project **SHALL** trace the decision to the motivating Security Authority/external input and applicable `SCAF-CTX`, `SCAF-ARCH`, `SCAF-INT`, `SCAF-TIME`, `SCAF-RUN`, `SCAF-ROB`, `SCAF-LIFE`, `SCAF-OBS`, `SCAF-CFG` or `SCAF-ASSUR` decision as appropriate.

### `SCAF-SEC-029` — Security assumption / constraint re-evaluation

**Target:** Project-Applicable Obligation

A material change to threat assumptions/model, security objective/requirement, trust relationship, identity/authentication/authorization basis, credential/key lifecycle assumption, protected asset/service, security-relevant interaction, privilege/separation decision, LIFE/CFG security dependency, external security/regulatory/risk constraint or known compromise condition **SHALL** trigger re-evaluation of affected SEC and dependent project decisions.

### `SCAF-SEC-030` — Security-sensitive persistent / credential-state relationship

**Target:** Project-Applicable Obligation

Where a security-relevant credential reference, trust state, authorization input, revocation/expiry fact or other security-related state is persisted or restored across lifecycle instances, the project **SHALL** define the source-authority relationship and consumption eligibility among applicable SEC, CFG, LIFE and TIME decisions so that persistence/restoration does not silently establish current security eligibility.

A persisted security-related value **SHALL NOT** by itself establish current authentication, authorization, trust or lifecycle eligibility merely because it survives reset/boot/update.

## 4. Framework Normative Invariants

### `SCAF-SEC-031` — External Security Authority / SCAF-SEC / PDA boundary

**Target:** Framework Normative Invariant

The applicable Security Authority remains source authority for threat assumptions/model, security objectives/requirements, security risk evaluation/acceptance, regulatory/certification security acceptance and externally imposed security constraints. `SCAF-SEC` **Defines Framework Semantics / Obligation** for the SCAF security architecture concern. The Project Design Authority **Defines Project Instance / Decision** for actual project trust/security architecture decisions using those controlled inputs.

A specific/detailed security constraint **SHALL NOT** become a SCAF-SEC or PDA-originated threat/risk/acceptance decision merely because it constrains architecture.

### `SCAF-SEC-032` — SEC / ARCH boundary

**Target:** Framework Normative Invariant

`SCAF-SEC` **Defines Framework Semantics / Obligation** for security/trust meaning, required security separation/relationship constraints and security-originated architecture inputs.

`SCAF-ARCH` **Defines Framework Semantics / Obligation** for System/Node/Domain/topology/allocation/shared-resource structure, and the Project Design Authority defines actual project structural boundaries. SEC **SHALL NOT** redefine Node/Domain/topology semantics merely to express trust or security constraints.

### `SCAF-SEC-033` — SEC / INT boundary

**Target:** Framework Normative Invariant

`SCAF-INT` **Defines Framework Semantics / Obligation** for Interface/Interaction contract, exchange validity, semantic ordering, compatibility/evolution, targeting/routing and Protocol/Connection Session Identity.

`SCAF-SEC` **Defines Framework Semantics / Obligation** for security identity/trust/authentication/authorization/protection constraints applied to those controlled interactions. A security authentication/authorization result **SHALL NOT** redefine INT session identity/contract semantics, and an INT-valid/delivered exchange **SHALL NOT** by itself establish security authentication/authorization.

### `SCAF-SEC-034` — SEC / TIME boundary

**Target:** Framework Normative Invariant

`SCAF-TIME` **Defines Framework Semantics / Obligation** for timebase/clock identity, synchronization, drift/offset/uncertainty, measurable age/deadline/window/capacity and Time Epoch/Time Domain semantics.

`SCAF-SEC` may define the security consequence/eligibility of those controlled temporal properties but **SHALL NOT** create a replacement timebase, expiry calculation authority, window value or Time Epoch.

### `SCAF-SEC-035` — SEC / RUN boundary

**Target:** Framework Normative Invariant

`SCAF-RUN` **Defines Framework Semantics / Obligation** for operational-state meaning, readiness/availability, transition/result consistency, authoritative current operational state and Operational Incarnation.

`SCAF-SEC` may define security eligibility/authorization/trust constraints used by RUN decisions but **SHALL NOT** directly establish authoritative RUN current state/readiness merely because a security decision permits or denies an operation.

### `SCAF-SEC-036` — SEC / ROB boundary

**Target:** Framework Normative Invariant

`SCAF-SEC` **Defines Framework Semantics / Obligation** for security-originated condition/trust/authorization/protection meaning and security-specific consequence/constraint.

`SCAF-ROB` **Defines Framework Semantics / Obligation** for general Fault/Error/Failure meaning, health determination, containment/degradation/recovery/reintegration and resilience response when a security-originated condition becomes robustness-significant. SEC **SHALL NOT** re-own general ROB recovery/failover/resilience authority.

### `SCAF-SEC-037` — SEC / LIFE boundary

**Target:** Framework Normative Invariant

`SCAF-LIFE` **Defines Framework Semantics / Obligation** for boot/reset/power/update/activation/rollback transaction/state/result semantics and Boot Incarnation.

`SCAF-SEC` may define security authorization/trust/integrity/eligibility inputs that constrain a LIFE transaction but **SHALL NOT** redefine lifecycle transaction acceptance/completion/activation/rollback result or Boot Incarnation.

### `SCAF-SEC-038` — SEC / OBS boundary

**Target:** Framework Normative Invariant

`SCAF-SEC` **Defines Framework Semantics / Obligation** for the security fact/decision/result and security claim that may require observation/evidence.

`SCAF-OBS` **Defines Framework Semantics / Obligation** for evidence identity/provenance/quality/missingness/preservation/correlation/export. SEC **SHALL NOT** become OBS evidence authority merely because evidence supports a security decision or incident.

### `SCAF-SEC-039` — SEC / CFG boundary

**Target:** Framework Normative Invariant

`SCAF-CFG` **Defines Framework Semantics / Obligation** for authoritative configuration/persistent-state source/value/version/validity/migration/commit/CFG-side rollback semantics.

`SCAF-SEC` may consume or constrain security-relevant CFG decisions using controlled Security Authority inputs but **SHALL NOT** become CFG source authority. A security-sensitive configuration value **SHALL NOT** become a Security Authority objective/risk/acceptance decision merely because CFG stores it.

### `SCAF-SEC-040` — SEC / ASSUR evidence-sufficiency and closure boundary

**Target:** Framework Normative Invariant

`SCAF-SEC` **Defines Framework Semantics / Obligation** for security architecture decisions/properties/claims that require verification.

`SCAF-ASSUR` **Defines Framework Semantics / Obligation** for verification methods, verification-evidence properties and evidence-sufficiency criteria; the Project Verification / Assurance Authority evaluates actual project evidence sufficiency. Security evidence sufficiency **SHALL NOT** transfer residual-risk acceptance, regulatory/certification acceptance or underlying security requirement closure to SEC/ASSUR unless the applicable authority is explicitly delegated that separate authority capacity.

### `SCAF-SEC-041` — Security identity / core identity partition

**Target:** Framework Normative Invariant

A project-defined security peer/subject/credential identity or security-claimant identity is a SEC concern semantic where Applicable and is distinct from `SCAF-INT` Protocol/Connection Session Identity, `SCAF-LIFE` Boot Incarnation, `SCAF-RUN` Operational Incarnation, `SCAF-TIME` Time Epoch/Domain, `SCAF-CFG` item/version identity and `SCAF-OBS` evidence-item identity.

A project may explicitly map/correlate those identities, but no identity **SHALL** be inferred to equal another merely because one event/session/record commonly carries both.

### `SCAF-SEC-042` — SEC / PROF / Project Realization mechanism boundary

**Target:** Framework Normative Invariant

`SCAF-SEC` **Defines Framework Semantics / Obligation** for security architecture properties and required project decisions, not universal realization mechanisms.

`SCAF-PROF` may **Guide Realization** / **Constrain** applicable realization choices, and Project Realization implements the selected mechanism. No L1/L2 SEC requirement **SHALL** universally mandate an encryption/signature algorithm, key size, certificate format, PKI, credential store, secure element, TPM/HSM, hardware root of trust, secure-boot implementation, firewall, sandbox, access-control technology, security protocol, password scheme, token format or other implementation technology.

## 5. Required Project Decisions / Records

The following table is informative and does not create additional normative requirements.

| Decision / record | Project-side authority / provenance |
|---|---|
| Security Authority input / threat-objective-constraint provenance | Applicable Security / Regulatory / Risk Authority; integrated by Project Design Authority |
| Material security concern inventory / protected architecture interest | Project Design Authority using controlled source constraints |
| Trust/security relationships and project security allocations | Project Design Authority under SEC + ARCH constraints |
| Security identity / authentication / authorization semantics | Project Design Authority using applicable Security Authority inputs |
| Confidentiality / integrity / hostile-freshness requirement | Project Design Authority constrained by Security Authority and INT/TIME decisions |
| Credential/key lifecycle security semantics | Project Design Authority / applicable Security Authority |
| Privilege/separation / management-path eligibility | Project Design Authority using SEC/ARCH/INT/CFG/LIFE constraints |
| Compromise/trust-loss security consequence | Project Design Authority constrained by Security Authority; ROB handles general resilience response |
| LIFE security preconditions / CFG security-relevant input mapping | Project Design Authority using LIFE/CFG/SEC obligations |
| Security observation/evidence need | Project Design Authority using SEC + OBS obligations |
| Verification evidence-sufficiency evaluation | Project Verification / Assurance Authority using SCAF-ASSUR semantics |
| Residual security risk / certification acceptance | Applicable Security / Risk / Regulatory Authority |

`SCAF-APP` **Dispositions / Traces** these decisions but does not own them.

## 6. Concern Boundaries

- `SCAF-CTX` **Defines Framework Semantics / Obligation** for mission, Function/Service context and consequence motivating security needs.
- `SCAF-ARCH` **Defines Framework Semantics / Obligation** for structural/Node/Domain/topology allocations constrained by security/trust requirements.
- `SCAF-INT` **Defines Framework Semantics / Obligation** for Interface/Interaction contract, validity, ordering, compatibility and Session Identity; SEC applies controlled security constraints without taking contract/session authority.
- `SCAF-TIME` **Defines Framework Semantics / Obligation** for measurable age/expiry/window/timebase/synchronization/uncertainty/capacity properties consumed by security decisions.
- `SCAF-RUN` **Defines Framework Semantics / Obligation** for authoritative operational state/readiness/transition semantics constrained by security eligibility decisions where applicable.
- `SCAF-ROB` **Defines Framework Semantics / Obligation** for general failure/health/containment/degradation/recovery/resilience response when security-originated conditions become robustness-significant.
- `SCAF-LIFE` **Defines Framework Semantics / Obligation** for boot/reset/power/update/activation/rollback lifecycle transaction/result semantics constrained by security preconditions.
- `SCAF-OBS` **Defines Framework Semantics / Obligation** for evidence identity/provenance/quality/preservation/correlation/export supporting security diagnosis/verification/incidents.
- `SCAF-CFG` **Defines Framework Semantics / Obligation** for authoritative configuration/persistent-state source/value/version/validity/migration/commit/rollback semantics consumed by security decisions.
- `SCAF-SEC` **Defines Framework Semantics / Obligation** for the security architecture interface/robustness concern using applicable Security Authority inputs without replacing threat/risk/acceptance authority.
- `SCAF-ASSUR` **Defines Framework Semantics / Obligation** for verification/evidence-sufficiency semantics; Project Verification / Assurance Authority **Verifies** applicable security obligations and determines actual evidence sufficiency.
- `SCAF-PROF` may **Guide Realization** / **Constrain** applicable security implementations; Project Realization implements selected mechanisms.

## 7. Non-Normative Example

A multi-participant system may receive a security-sensitive update request over an INT-controlled management Interaction. The applicable Security Authority supplies the project security objectives/trust constraints; SEC requires the project to define the security identity/authentication/authorization and integrity/eligibility decision used by the update path; CFG supplies authoritative security-relevant configuration/version facts; TIME supplies any measurable expiry/window/uncertainty; LIFE **Defines Framework Semantics / Obligation** for the update/activation transaction/result; ROB **Defines Framework Semantics / Obligation** for the resilience response if compromise or failure becomes robustness-significant; RUN determines resulting operational readiness/state; and OBS records/correlates security/lifecycle evidence. Whether the realization uses certificates, symmetric keys, a secure element, TPM/HSM, signed images, secure boot, a firewall, sandbox, access-control lists or another mechanism is outside L1/L2 SEC normative scope.
