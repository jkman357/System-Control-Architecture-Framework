# SCAF Controlled Context Package Source-Aware Validator

This package implements the production validation boundary introduced by **SCAF v0.0.10rc05** for the accepted Controlled Context Package representation.

It validates deterministic representation/source consistency only.

```text
Controlled Context Package bytes
        ↓
strict YAML / canonical raw representation policy
        ↓
accepted rc04 package schema
        ↓
exact bound Context Source Association Set
        ↓
accepted Context Source Association source-aware validation
        ↓
exact bound Consumption Selection / validated I
        ↓
package source-aware consistency proof
        ↓
PASS / INVALID
```

The validator proves, within its bounded contract:

- strict one-document YAML policy, duplicate-key rejection, no aliases/anchors/merge/custom tags, string mapping keys, quoted canonical string values, and LF line endings;
- accepted rc04 package schema validity;
- accepted canonical raw/list ordering;
- exact package binding to the selected Consumption Selection and Context Source Association bytes/kind/release/scope;
- accepted upstream Context Source Association source-aware validation before package-domain reasoning;
- exact Authority Context Entry coverage of validated `I`;
- exact Association Envelope fidelity to accepted upstream Controlled Source Associations;
- package-wide `association_handle` uniqueness;
- exactly one same-authority Materialization Decision per accepted association;
- unique package-local Materialized Context Item IDs;
- materialized item reference resolution and orphan-item absence;
- Controlled Provenance Basis resolution; and
- bidirectional Materialization Decision ↔ item provenance correspondence.

A validator PASS does **not** prove:

```text
engineering-context sufficiency
implementation correctness
verification / compliance sufficiency
risk acceptance
release readiness
closure
source currentness / latest state
content loading success
content-use / redistribution authorization
AI / human engineering authority
```

The validator is not a builder/generator, content loader, Source Resolver, ranking/token-budget engine, prompt/model adapter, or CI gate.

## Usage

From the repository root:

```text
python -m tools.scaf_controlled_context_package_validator.validator
```

Optional project-side input selectors:

```text
--package
--associations
--selection
--profile
--project-application
```

The repository-owned package schema and accepted upstream validator implementations are intentionally not CLI override points.

Programmatic entry point:

```python
validate_controlled_context_package(
    repo_root,
    package_path=None,
    associations_path=None,
    selection_path=None,
    profile_path=None,
    project_application_path=None,
)
```

## Regression suite

```text
python -m unittest tools.scaf_controlled_context_package_validator.tests.test_validator
```

The rc05 suite includes accepted-fixture coverage plus bounded negative checks for raw YAML ambiguity, upstream invalidity, binding mismatch, authority-domain mismatch, Association Envelope divergence, handle/decision inconsistency, item-reference defects, provenance defects, and canonical ordering.
