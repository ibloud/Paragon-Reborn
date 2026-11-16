# Decision: Paragon asset integration boundary

**Date:** 2026-09-24  
**Status:** Historical proposal for implementation review in PR #13; not merged authority
**Scope:** Paragon-Reborn third-party Paragon-derived asset integration

The later [October 8 decision](2026-10-08-original-tarot-direction.md) retains original characters/placeholders for the next proof. This optional asset proposal does not override it.

## Decision

Use a dedicated production/compliance contract for Epic/Fab Paragon-derived assets rather than embedding licensing assumptions in gameplay architecture.

The contract is `docs/PARAGON_ASSET_INTEGRATION.md`.

## Rationale

The repository already separates original project systems from third-party marketplace assets. A dedicated gate makes provenance, current-term verification, branding restrictions, repository handling, UE5 import checks, and release checks explicit without turning legal assumptions into gameplay rules.

## Boundaries

- The contract does not define gameplay mechanics.
- It does not alter Veiled Dominion canon or the shared mechanics layer.
- It does not grant rights beyond the applicable current asset terms.
- Unresolved legal questions are escalated rather than inferred.
- Third-party assets remain outside public source control unless their applicable terms explicitly permit distribution.

## Verification basis

The contract records the current Fab Standard License and current Paragon listing controls that were verified for this implementation. It intentionally does not encode unverified historical or secondary claims as current legal requirements.

## Review trigger

Re-review when an asset listing, Fab terms, target engine/version, or distribution model changes, and before public release.
