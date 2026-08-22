# Evidence-Driven Engineering Pattern Candidate Semantic Foundation

## Purpose

A reusable, domain-neutral L3 pattern for controlled evidence lifecycle,
analysis, verification and engineering closure.

## Evidence Model

- Source Evidence
- Change Evidence
- Runtime Evidence
- Probe Evidence

## Evidence Lifecycle

Baseline -> Evidence Collection -> Behavioral Analysis ->
First Behavioral Divergence Identification -> Hypothesis Formation ->
Targeted Probe -> Additional Evidence -> Verification -> Closure

## Observability Lifecycle

Temporary Probe:

Exploratory observability introduced to answer a bounded engineering question.

Diagnostic:

Operational observability intentionally retained for ongoing system
understanding.

Probe is not automatically a Diagnostic.

## AI Assistance Boundary

AI may assist:
- source navigation
- evidence correlation
- hypothesis generation
- probe suggestion
- review assistance

AI does not obtain:
- design authority
- verification authority
- closure authority
- release authority

## Scope Exclusions

This pattern does not introduce:
- authority registry migration
- Project Application migration
- Effective Project Profile migration
- L4 expansion
- code generation
- generic instrumentation CI

## Layer Separation

SCAF:
Reusable engineering principles and patterns.

Implementation Framework:
Concrete evidence capture, retention and export realization.

Specific System Application:
Downstream application of the pattern.
