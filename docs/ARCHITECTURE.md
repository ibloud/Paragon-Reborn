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

For the current card/tarot design reference, see
[Paragon Tarot — Complete Production Research](paragon-tarot-research%202.md).

## Runtime boundary

The browser layer is a design and companion surface. Unreal Engine 5 is the proposed production client/runtime for high-fidelity assets, Gameplay Ability System integration, physics, and replication. Server authority must be explicit for gameplay-affecting state.

## Asset integration boundary

Third-party Paragon-derived assets are governed by
[Paragon Asset Integration Contract](PARAGON_ASSET_INTEGRATION.md).

That contract is a production/compliance gate, not a gameplay or constitutional rule. It requires current listing/license verification, provenance tracking, separation of third-party assets from original project IP, and release checks before distribution.

The public repository must not become a redistribution channel for Epic/Fab assets. The exact applicable listing and license control any particular asset.

## Decision rules

- Prefer a small verified behavior over an untested abstraction.
- Treat networking and persistence as trust boundaries.
- Do not claim cross-engine parity without shared fixtures and test results.
- Keep proprietary or restricted assets outside source control.
- Record consequential architecture changes as short decision documents under `docs/decisions/`.
- For any Paragon-derived asset, follow `docs/PARAGON_ASSET_INTEGRATION.md` before import or release.
