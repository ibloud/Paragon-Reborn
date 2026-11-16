# Roadmap

This roadmap prioritizes evidence over breadth. Dates are intentionally omitted until maintainers assign owners and capacity.

## Phase 0 — Repository foundation

- [x] Clarify that this repository is a project hub in pre-production
- [x] Document repository boundaries
- [x] Add contribution guidance and automated repository checks
- [x] Separate licensing from Paragon asset notes
- [ ] Protect `main` and require pull-request review
- [ ] Create issue and pull-request templates
- [ ] Publish a maintained project board

## Phase 1 — Rules contract

- [x] Define versioned hero, ability, and card schemas
- [x] Specify deterministic rule examples
- [x] Add schema validation and behavioral tests
- [x] Identify the canonical implementation for each shared rule

Exit criterion: the same example data produces documented outcomes in a headless test suite.

**Current evidence:** `docs/rules/` contains the v1 contract, a deterministic first-slice fixture, and a dependency-free validator.

## Phase 2 — Vertical slice

- [ ] One playable original hero with generic/original assets
- [ ] One ability with cooldown and resource cost
- [ ] One small arena and target dummy
- [ ] One card modifier loaded from shared data
- [ ] Repeatable local setup
- [ ] Automated smoke test and recorded demo

Exit criterion: a new contributor can run and verify the slice from written instructions.

## Phase 3 — Network validation

- [ ] Server-authoritative ability execution
- [ ] Two-client replication test
- [ ] Basic latency and reconciliation measurements
- [ ] Threat model for cheating and trust boundaries

Exit criterion: two remote clients complete the documented gameplay scenario consistently.

## Non-goals until the vertical slice passes

- full hero roster;
- matchmaking at production scale;
- monetization;
- esports infrastructure;
- large asset imports;
- custom launcher or account platform.

## Original hero-card and story track — 2026-10-08

Direction: [original hero-card design](docs/ORIGINAL_HERO_CARD_DIRECTION.md).

- [x] Document tarot/build/story separation and original-IP transition.
- [x] Mark historical roster research as non-production.
- [ ] Review original character briefs and provenance records.
- [ ] Propose separately versioned exact mechanics without changing v1 fixtures.
- [ ] Prove one original hero, one modifier and one consequential authored choice.
- [ ] Verify deterministic replay, invalid-choice rejection and safe fallback.
- [ ] Expand to three heroes / twelve cards only after the first proof passes.
- [ ] Human accessibility and balance playtest; publish evidence and limitations.
- [ ] Audit historical public branding/downloads and clear intended release scope.

No playable tarot system or completed IP migration is claimed.
