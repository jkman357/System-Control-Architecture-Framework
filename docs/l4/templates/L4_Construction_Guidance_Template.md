# <L4 Guidance Title>

**L4 ID:** `<allocate only when publishing>`  
**Status:** Draft  
**Introduced In:** `<release>`  
**Supersedes:** None  

> This template is an authoring aid. Copying the template does not allocate an L4 identity or make the content accepted SCAF guidance.

## 1. Purpose / Scope

Describe the bounded construction problem addressed by this guidance.

## 2. L2 / L3 Trace

### Relevant L2 authority / concern basis

- `<authority / obligation ID>` — `<why relevant>`

### Relevant L3 Pattern / Mechanism

- `<SCAF-PAT-...>` — `<relationship>`

Trace does not imply automatic project adoption or L2 satisfaction.

## 3. Construction Preconditions

- `<capability / assumption required for this guidance to be meaningful>`

### Not Suitable When

- `<condition where this guidance should not be applied as-is>`

These are L4 construction preconditions, not Project Application dispositions.

## 4. Recommended Implementation Shape

Describe participants, responsibilities, state/data flow and construction structure at the minimum depth needed to begin implementation.

Avoid unnecessary vendor APIs, code layout, variable names and arbitrary values.

## 5. Construction Constraints

- `<condition necessary to preserve the claimed guidance realization>`

Construction Constraints do not create new universal L2 obligations.

## 6. Construction Invariants

- `<property that must remain true across valid realization variations>`

## 7. Construction Assumptions

- `<assumption requiring project confirmation / replacement / rejection>`

Remember:

```text
L4 assumption != project fact
```

## 8. Required Project Decisions

Project Design Authority must decide, as applicable:

- ownership;
- thresholds / timing;
- capacity;
- retry / escalation;
- platform binding;
- recovery consequences;
- persistence / evidence budget;
- verification thresholds;
- other material project-specific values.

Do not insert example values as hidden project defaults.

## 9. Interface / State Considerations

- `<interface/state semantics material to construction>`

## 10. Timing Considerations

- `<quantities / ordering / deadline relationships the project must bound>`

## 11. Concurrency / Reentrancy Considerations

- `<execution contexts / serialization / ISR-task-thread boundaries>`

Use `Not Applicable` with reason when genuinely irrelevant.

## 12. Capacity / Resource Considerations

- `<burst, service rate, queue/buffer/storage/memory/processing bounds>`

### Bounded Exhaustion Behavior

- `<what project must decide when the bounded resource reaches capacity>`

## 13. Lifecycle Considerations

Address applicable phases:

- initialization / partial initialization;
- entry to operation;
- normal operation;
- reconfiguration;
- recovery / reintegration;
- shutdown / reset;
- update / activation;
- power transition.

## 14. Failure / Recovery Behavior

- `<detectable invalid/failure condition>`
- `<containment / retry / escalation>`
- `<recovery ownership>`
- `<degraded behavior>`

## 15. Diagnostics / Observability

State what must be observable to determine whether the mechanism behaved as intended.

- `<state / cause / error / timing / counter / evidence point>`

## 16. Verification Intent

For each important construction property, state:

- property to prove;
- bounded valid/invalid condition;
- expected observable behavior;
- future empirical evidence expected when reasonably producible.

Do not write project-specific executed results here.

## 17. Invalid / Incomplete Construction Conditions

- `<bounded condition that makes the claimed realization inconsistent or materially incomplete>`

Do not classify legitimate unresolved engineering judgment as Invalid merely because a later project decision/evidence stage has not been reached.

## 18. Known Variations / Trade-offs

- `<variation>` — `<trade-off>`

## 19. Material Deviation Considerations

Identify which departures would materially affect architecture intent, behavior, timing, failure/recovery, data integrity, observability or verification intent and therefore deserve retained PDA rationale.

## 20. Example Realization (Optional)

> **This example realization illustrates one possible conforming approach and is not the canonical implementation.**

Keep example values and APIs clearly non-authoritative and non-project-adopted unless explicitly decided elsewhere.

## 21. Provenance / Reference Basis

Describe the actual basis and maturity of the guidance without promoting references into authority.

## 22. Revision / Supersession Notes

Describe material construction-semantic changes, compatibility implications, or supersession when applicable.
