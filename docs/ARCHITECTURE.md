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

## Decision rules

- Prefer a small verified behavior over an untested abstraction.
- Treat networking and persistence as trust boundaries.
- Do not claim cross-engine parity without shared fixtures and test results.
- Keep proprietary or restricted assets outside source control.
- Record consequential architecture changes as short decision documents under `docs/decisions/`.
