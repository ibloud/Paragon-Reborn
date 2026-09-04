# Return to the Void

Technical roadmap and project hub for an open-source MOBA concept built around Epic Games' released Paragon assets, a modular card system, and companion web prototypes.

> **Project status: concept and pre-production.** This repository currently hosts the public roadmap and static project site. It does not yet contain a playable MOBA, an Unreal Engine project, or a reusable game framework.

- Project site: https://ibloud.github.io/Paragon-Reborn/
- Project context: https://sites.google.com/view/rtn2thevoid/journey
- Architecture: [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md)
- Roadmap: [ROADMAP.md](ROADMAP.md)
- Contributing: [CONTRIBUTING.md](CONTRIBUTING.md)

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

1. one controllable hero;
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
