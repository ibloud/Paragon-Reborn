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

## Agent security boundary

Future agentic tooling is governed by [Agent Security Contract](AGENT-SECURITY.md). The security model is enforcement machinery underneath project governance, not an autonomous governance layer.

Authority flows downward only:

`HUMAN GOVERNANCE → PROJECT GOVERNANCE → AGENT AUTHORITY → TOOL CAPABILITY → INDIVIDUAL ACTION`

The invariant `OBSERVE → UNDERSTAND → SUGGEST` remains intact. Missing authorization, identity, capability, resource scope, governance, provenance, or containment state fails closed. Behavioral anomaly detection may contain or escalate but may never grant authority.

The reference implementation lives under `security/`; its tests define acceptance criteria for a future runtime sandbox, identity boundary, capability broker, and egress controls.

## Decision rules

- Prefer a small verified behavior over an untested abstraction.
- Treat networking, persistence, agent identity, capabilities, and egress as trust boundaries.
- Do not claim cross-engine parity without shared fixtures and test results.
- Keep proprietary or restricted assets outside source control.
- Record consequential architecture changes as short decision documents under `docs/decisions/`.
