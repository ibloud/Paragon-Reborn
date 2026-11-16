# Architecture

## Status

This document describes the proposed system boundary. Components are planned unless linked to working code and tests.

## Responsibilities

| Component | Owns | Does not own |
|---|---|---|
| Paragon-Reborn | Roadmap, public site, architecture contracts, future Unreal implementation | Redistributing Epic assets |
| veiled-dominion-engine | Browser prototypes, deck/rule experiments, lightweight visualization | Production Unreal rendering or authoritative game servers |
| training | Contributor preparation and scored exercises | Production runtime code |

## Shared rules contract

Engine-independent schemas should describe heroes, cards, abilities, costs, cooldowns, and status effects. Fixtures should contain expected outcomes. Browser and Unreal implementations may differ internally, but both must satisfy the same behavioral examples.

For the new hero-card experiment, see
[Original hero cards and consequential stories](ORIGINAL_HERO_CARD_DIRECTION.md) and
[original-content rights boundary](ORIGINAL_CONTENT_RIGHTS.md).
The [historical tarot research](paragon-tarot-research.md) is provenance, not a production roster.
This direction does not alter the v1 contract or canonical four-player Veiled Dominion rules.

## Runtime boundary

The browser layer is a design and companion surface. Unreal Engine 5 is the proposed production client/runtime for high-fidelity assets, Gameplay Ability System integration, physics, and replication. Server authority must be explicit for gameplay-affecting state.

## Asset integration boundary

The next proof uses original characters/placeholders under the [October 8 decision](decisions/2026-10-08-original-tarot-direction.md). The optional [Paragon Asset Integration Contract](PARAGON_ASSET_INTEGRATION.md) is a proposal in PR #13, not merged authority or import permission.

That proposed contract describes production/compliance checks, not gameplay or constitutional rules. It requires current listing/license verification, provenance tracking, separation of third-party assets from original project IP, and release checks before distribution.

The public repository must not become a redistribution channel for Epic/Fab assets. The exact applicable listing and license control any particular asset.

## Decision rules

- Prefer a small verified behavior over an untested abstraction.
- Treat networking and persistence as trust boundaries.
- Do not claim cross-engine parity without shared fixtures and test results.
- Keep proprietary or restricted assets outside source control.
- Record consequential architecture changes as short decision documents under `docs/decisions/`.
- Any optional Paragon-derived asset path requires a separate approved decision, acquisition-specific rights review and reconciliation of the proposed integration contract before import or release.
