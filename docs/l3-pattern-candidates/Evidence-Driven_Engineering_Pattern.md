# Evidence-Driven Engineering Pattern Candidate Semantic Foundation

## Purpose

This L3 pattern candidate defines a reusable engineering approach for
improving system understanding, diagnosis, verification and closure
through controlled evidence lifecycle management.

The pattern is domain-neutral and is not bound to a specific product,
hardware platform, operating system, or implementation framework.

## Evidence Model

The pattern uses four evidence categories:

- Source Evidence
- Change Evidence
- Runtime Evidence
- Probe Evidence

## Evidence Lifecycle

Baseline

-> Evidence Collection

-> Behavioral Analysis

-> First Behavioral Divergence Identification

-> Hypothesis Formation

-> Targeted Probe

-> Additional Evidence

-> Verification

-> Closure

## Observability Lifecycle

Temporary Probe:

Exploratory observability introduced to answer a bounded engineering
question.

Diagnostic:

Operational observability intentionally retained for ongoing system
understanding.

Lifecycle:

Temporary Probe

- Remove
- Retain temporarily
- Promote or redesign

Promoted observability becomes Diagnostic.

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

## Layer Separation

SCAF:

Defines engineering principles and reusable patterns.

Implementation Framework:

Provides concrete evidence capture, retention, and export mechanisms.

Specific System Application:

Applies the pattern to a particular system realization.

## Scope Exclusions

This candidate does not introduce:

- authority registry migration
- Project Application migration
- Effective Project Profile migration
- L4 expansion
- code generation
- generic instrumentation CI
