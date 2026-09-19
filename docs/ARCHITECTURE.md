# Architecture

## Status

This document describes the proposed system boundary. Components are planned unless linked to working code and tests.

## Responsibilities

| Component | Owns | Does not own |
|---|---|---|
| Paragon-Reborn | Roadmap, public site, architecture contracts, future Unreal implementation | Redistributing Epic assets |
| veiled-dominion-engine | Browser prototypes, deck/rule experiments, lightweight visualization | Production Unreal rendering or authoritative game servers |
| training | Contributor preparation and scored exercises | Production runtime code |

## Legacy-project validation boundary

Paragon ReBorn can serve as a controlled proving environment for bringing older or previously paused projects up to current standards. The validation path is:

~~~
OLD PROJECT → INVENTORY → PROVENANCE / RIGHTS → DEPENDENCIES → GAP ANALYSIS → CONTROLLED REBUILD → PLAYABILITY / ACCESSIBILITY / DATA TEST → DOCUMENTED RESULT → PRODUCTION DECISION
~~~

This is a process boundary, not a rights grant. Historical presence, technical availability, repository history, or prototype success does not establish ownership, permission, commercial use, grant use, trademark rights, or production acceptance.

The detailed evidence matrix lives in [LEGACY_PROJECT_VALIDATION.md](LEGACY_PROJECT_VALIDATION.md).

## Shared rules contract

Engine-independent schemas should describe heroes, cards, abilities, costs, cooldowns, and status effects. Fixtures should contain expected outcomes. Browser and Unreal implementations may differ internally, but both must satisfy the same behavioral examples.

For the current card/tarot design reference, see
[Paragon Tarot — Complete Production Research](paragon-tarot-research%202.md).

## Runtime boundary

The browser layer is a design and companion surface. Unreal Engine 5 is the proposed production client/runtime for high-fidelity assets, Gameplay Ability System integration, physics, and replication. Server authority must be explicit for gameplay-affecting state.

## Decision rules

- Prefer a small verified behavior over an untested abstraction.
- Treat networking and persistence as trust boundaries.
- Do not claim cross-engine parity without shared fixtures and test results.
- Keep proprietary or restricted assets outside source control.
- Record consequential architecture changes as short decision documents under `docs/decisions/`.
