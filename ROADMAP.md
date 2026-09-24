# Roadmap

This roadmap prioritizes evidence over breadth. Dates are intentionally omitted until maintainers assign owners and capacity.

## Phase 0 — Repository foundation

- [x] Clarify that this repository is a project hub in pre-production
- [x] Document repository boundaries
- [x] Add contribution guidance and automated repository checks
- [x] Separate licensing from Paragon asset notes
- [x] Add agent-security contract, fail-closed policy reference, containment model, and tests
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
- [ ] Runtime implementation of agent identity, capability, action, provenance, and egress boundaries

Exit criterion: two remote clients complete the documented gameplay scenario consistently, and any agentic tooling remains fail-closed at every external action boundary.

## Non-goals until the vertical slice passes

- full hero roster;
- matchmaking at production scale;
- monetization;
- esports infrastructure;
- large asset imports;
- custom launcher or account platform.
