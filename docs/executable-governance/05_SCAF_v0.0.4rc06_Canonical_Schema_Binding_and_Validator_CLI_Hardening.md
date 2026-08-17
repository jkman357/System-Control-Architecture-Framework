# SCAF v0.0.4rc06 — Canonical Schema Binding & Validator CLI Hardening

**Development Release:** v0.0.4rc06  
**Status:** Focused R5-01 Closure RC  
**Date:** 2026-08-17

## 1. Purpose

This RC closes the sole Minor finding from the independent v0.0.4rc05 schema/validator review:

```text
R5-01 — public --schema override could replace the accepted structural contract and still emit normal RESULT: PASS
```

The accepted rc05 schema/validator architecture is not reopened. This RC only hardens the normal production CLI so the reviewed canonical schema cannot be replaced by caller-selected schema or repository-root arguments.

## 2. Canonical Production CLI Binding

The normal production invocation remains:

```text
python -m tools.scaf_validator.validator
```

The production CLI now derives its repository root from the reviewed validator module location and always loads:

```text
schemas/authority-registry.schema.json
```

from that repository.

The following caller-selectable production arguments are intentionally not supported:

```text
--schema
--repo-root
```

The optional `--registry <path>` remains supported so a registry copy or mutation can be validated, but the selected registry is always evaluated against the canonical repository schema and canonical frozen Markdown source.

Function-level schema/repository injection remains available for controlled unit-test use through existing Python APIs. It is not a production PASS-producing CLI path and does not alter semantic authority.

## 3. CLI Regression Contract

The regression suite adds an end-to-end subprocess test that:

1. mutates schema-owned accepted fields (`record_kind` and `relations`);
2. verifies the production CLI returns non-zero / `RESULT: FAIL` under the canonical schema;
3. attempts the former `--schema <lax-schema>` bypass;
4. verifies the production CLI rejects that argument and cannot emit a normal PASS result.

The original seven rc05 regressions remain in place.

## 4. Authority Boundary

Frozen normative Markdown remains semantic authority. The schema remains the reviewed structural representation contract, and the validator remains a subordinate conformance checker. Canonical CLI binding prevents a caller from silently substituting a weaker contract; it does not elevate schema or validator above frozen Markdown.

Release-integrity / frozen-source byte authentication remains a separate concern from semantic/source-aware validator behavior and is not silently folded into this RC.

## 5. Non-Regression Requirements

This RC shall preserve without semantic change:

- repository-root `authority-registry.yaml`;
- all 294 accepted rc03 records and `representation_release = v0.0.4rc03`;
- `schemas/authority-registry.schema.json`;
- accepted rc01–rc05 executable-governance contracts except current navigation/release-state wording;
- frozen `docs/normative/`;
- frozen `docs/l3/`;
- the two authority classes and 294 / 218 / 76 inventory;
- empty initial `relations`;
- project-state and L3 Pattern exclusion.

## 6. Deferred Scope

This RC does not add:

- CI enforcement or merge blocking;
- registry generation or hybrid ownership;
- generated indexes/views;
- code generation;
- automatic project applicability inference;
- machine-readable L2→L3 relation semantics;
- new L3 Patterns / third tranche / SEC-primary realization;
- M3/M4;
- L4.

## 7. Closure Gate

The independent review shall determine whether `R5-01` is fully closed without reopening accepted upstream authority/registry/schema semantics.

Expected gate label:

```text
V0.0.4 CANONICAL-SCHEMA BINDING / VALIDATOR-CLI HARDENING GATE
```
