# Frozen Baseline Manifest Scope

## v0.2.1rc02

## Purpose

Clarify the relationship between historical frozen baseline metadata
and active release identity.

## Historical Frozen Baseline Manifest

The frozen baseline manifest represents historical integrity metadata.

It preserves references to previous controlled baselines and is not the
active release identity source.

## Active Release Manifest

The active release manifest represents the current release identity.

Current release identification is controlled by:

- README release information;
- CHANGELOG release entry;
- release-manifest metadata.

## Governance Relationship

Historical baseline metadata:

    Protected reference

Active release metadata:

    Current evolution identity

The separation prevents historical records from being interpreted as
current release identifiers.
