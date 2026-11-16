# Return to the Void

## Loptr Lab mission and participation

Loptr Lab is a pre-seed, people-over-profit, accessibility-first venture working toward a self-sustaining model within a capitalist economy. Money sustains the work; meaningful change for people is its purpose. We accept funding only on terms that keep people and accessibility first. Our long-term vision includes universal basic income. We aim to bring change to life and leave a transparent record of what we tried, what worked, and what failed so others can carry it forward. This mission governs our projects, funding decisions, and partnerships; it is not a temporary marketing position.

Current open review and contribution opportunities are voluntary and unpaid. Before work begins, agree in writing on scope, time, what will be public, credit preferences, and an exit path. You can stop at any point. Participation does not promise employment, ownership, revenue share, academic credit, or future pay. Any paid commission or other formal arrangement requires a separate signed agreement before work begins. External assistance or benefits belong to the participant and are not compensation from Loptr Lab.

Financial support is optional and sustains infrastructure, maintenance, accessibility work, and documented development. Paying does not buy contributor status, canon authority, approvals, ownership, or employment. Participation and accessibility are not sponsorship rewards. Project-specific licenses and existing signed agreements continue to apply.

[Full mission and participation terms](https://github.com/ibloud/ibloud.github.io/blob/main/MISSION.md).


Technical roadmap and project hub for an original hero-card game experiment: tarot-informed build choices, consequential stories, and companion prototypes. Historical Paragon research records the starting point; new production content follows an independent character and world design path.

> **Project status: concept and pre-production.** This repository currently hosts the public roadmap and static project site. It does not yet contain a playable MOBA, an Unreal Engine project, or a reusable game framework.

- Project site: https://ibloud.github.io/Paragon-Reborn/
- Project context: https://sites.google.com/view/rtn2thevoid/journey
- Architecture: [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md)
- Roadmap: [ROADMAP.md](ROADMAP.md)
- Contributing: [CONTRIBUTING.md](CONTRIBUTING.md)
- Participant learning paths: [docs/PARTICIPANT_LEARNING_PATHS.md](docs/PARTICIPANT_LEARNING_PATHS.md)
- Independent music licensing: [docs/MUSIC_LICENSING.md](docs/MUSIC_LICENSING.md)
- Current original hero-card direction: [design and staged prototype](docs/ORIGINAL_HERO_CARD_DIRECTION.md)
- Original-content transition: [rights and provenance boundary](docs/ORIGINAL_CONTENT_RIGHTS.md)
- Historical tarot research (not production clearance): [research archive](docs/paragon-tarot-research.md)
- Historical Tarot LWB (not cleared for new production): [docs/paragon-tarot-LWB.pdf](docs/paragon-tarot-LWB.pdf)

## Repository responsibility

This repository is the coordination hub for Return to the Void. It owns the roadmap, architecture boundaries, public website, and—when development reaches that stage—the Unreal Engine implementation.

Related repositories own distinct concerns:

| Repository | Responsibility |
|---|---|
| [Loptr-Lab/veiled-dominion-engine](https://github.com/Loptr-Lab/veiled-dominion-engine) | Browser-native prototypes for rules, deck construction, lore, and lightweight visualization |
| [Loptr-Lab/training](https://github.com/Loptr-Lab/training) | Contributor exercises and technical training |
| [ibloud/violets-revenge](https://github.com/ibloud/violets-revenge) | Separate 1v4 game and portfolio project |

Capabilities described in this repository are **planned** unless they link to working source, automated tests, or a published demo.

## What Epic's release provides

Epic released Paragon art and audio assets for use in Unreal Engine projects. These include characters, animations, effects, environments, and supporting visual material.

The release does **not** provide a complete game. Return to the Void must independently implement:

- game rules, abilities, progression, objectives, and balance;
- authoritative networking, matchmaking, persistence, and anti-cheat;
- user interfaces and accessibility;
- minion, tower, and jungle AI;
- card data, deck validation, and runtime effects;
- operations, testing, moderation, and deployment.

No Epic assets are distributed by this repository. See [docs/PARAGON_ASSET_NOTES.md](docs/PARAGON_ASSET_NOTES.md).

## Proposed architecture

The web layer is intended for rapid, testable rule experiments. Unreal Engine 5 is intended for production rendering, Gameplay Ability System integration, physics, and replicated gameplay. Shared rules must be described through versioned, engine-independent schemas and behavioral tests before equivalent implementations are accepted.

This boundary is a proposal, not evidence that each system is already implemented.

## First milestone

The first meaningful proof should be a deliberately small vertical slice:

1. one controllable original hero using original or generic placeholder assets;
2. one replicated ability;
3. one compact test arena;
4. one card modifier represented by shared data;
5. one automated gameplay rule test;
6. documented local setup and a captured demo.

Expansion to additional heroes, progression systems, or live-service infrastructure should follow only after that slice is repeatable.

## Development

The current site is dependency-free. Open `index.html` directly in a browser.

Run the repository checks with:

```bash
python3 scripts/validate_repo.py
```

## License

Original documentation and website content are licensed under [CC BY 4.0](LICENSE). Any future source-code license must be declared explicitly before code is accepted.

Paragon assets are not included and are governed by Epic Games' applicable terms.
