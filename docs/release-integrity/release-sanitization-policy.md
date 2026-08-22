# Release Sanitization Policy

## v0.2.1rc04

## Purpose

Define separation between development packages and public release
packages.

## Package Types

### Development Package

Purpose:
- repository development;
- internal review;
- engineering evolution.

May contain:
- Git history;
- development metadata;
- repository workflow files.

### Public Release Package

Purpose:
- external review;
- documentation distribution;
- controlled sharing.

Should remove:
- .git;
- personal repository metadata;
- temporary local artifacts.

Optional removal:
- .github workflow files.

## Governance Relationship

Development Package
        |
        v
Release Sanitization
        |
        v
Public Release Package

Sanitization changes package contents only and does not modify
architecture definitions or Pattern authority.
