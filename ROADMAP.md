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

## Phase 1.5 — Legacy project validation

- [ ] Inventory one older or paused project and its inherited material
- [ ] Record provenance and rights/license evidence for each retained dependency
- [ ] Separate independently rebuilt systems from inherited/third-party material
- [ ] Run current-standard gap analysis for accessibility, data, security, documentation, and production readiness
- [ ] Record unresolved restrictions and replacement paths
- [ ] Produce a validation case study showing discovery → verification → correction → control → retest

Exit criterion: the validation record identifies what can be rebuilt, what remains restricted or pending, and what evidence is required before production handoff.

## Phase 2 — Vertical slice

- [ ] One playable hero
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
