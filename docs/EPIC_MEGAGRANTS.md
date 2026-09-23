# Epic MegaGrants

This page tracks grant-readiness separately from the engineering roadmap. The roadmap answers **what we are building**; this document answers **what evidence should be ready when a future submission window opens**.

## Current status

As of **September 18, 2026**, Epic's 2026 Cycle 2 submission window has closed. The published review period is September 5–December 4, 2026, with notices scheduled for December 7–11. Epic has not yet published dates for the next submission cycle.

Official program information: https://www.unrealengine.com/megagrants

## 2026 published schedule

| Cycle | Submission window | Review | Notices |
|---|---|---|---|
| 2026 Cycle 1 | January 12–March 20, 2026 | March 21–June 14 | June 15–19 |
| 2026 Cycle 2 | June 29–September 4, 2026 | September 5–December 4 | December 7–11 |

Dates above are from Epic's published MegaGrants schedule. Future dates should be added only after Epic publishes them.

## What should be ready before the next application

Grant readiness should follow demonstrated project progress rather than replace it.

- **Rules contract:** versioned schemas, deterministic fixture, validator, and documented expected outcomes.
- **Vertical slice:** one playable Unreal Engine hero, one replicated ability, one compact arena, one card modifier, and documented local setup.
- **Validation:** automated smoke test plus a short captured demonstration.
- **Network proof:** server-authoritative execution, two-client replication, and basic latency/reconciliation measurements.
- **Public documentation:** architecture boundaries, contribution path, licensing/asset boundaries, and accurate project status.

See [ROADMAP.md](../ROADMAP.md) for the engineering sequence.

## Evidence standard

The repository should distinguish clearly between:

- **implemented** — backed by working source and/or tests;
- **demonstrated** — backed by a reproducible demo;
- **documented** — a stated design or boundary;
- **planned** — a future milestone.

Do not describe a playable Unreal Engine implementation, production networking, or other future capability as completed until it has evidence in the repository or a linked demonstration.

## Direct-link landing page

A dedicated landing page is available at:

**https://ibloud.github.io/Paragon-Reborn/megagrant/**

It is intentionally designed as a stable direct link for promotion, outreach, contributor onboarding, technical review, and public comment.

The landing page is **not required to remain in the site's primary navigation after the relevant grant dates become historical**. The URL should remain live as an evergreen campaign/review endpoint, with dated information updated when Epic publishes a new cycle.

## Public call to participate

The project welcomes:

- technical review and architecture criticism;
- documentation corrections;
- rules/test contributions;
- Unreal implementation work when the project reaches that stage;
- questions and comments through GitHub Issues.

Start with [CONTRIBUTING.md](../CONTRIBUTING.md).

## Source

Epic Games — Epic MegaGrants: https://www.unrealengine.com/megagrants
