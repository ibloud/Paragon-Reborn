# Shared Rules Contract

This directory defines the engine-independent contract for the first playable slice of Return to the Void.

The contract is intentionally small. It is designed to let the browser prototype and future Unreal Engine implementation agree on the same inputs and expected gameplay outcomes without sharing runtime code.

## Contract

- Schemas are versioned under `schemas/`.
- Deterministic examples are fixtures under `fixtures/`.
- A fixture's expected outcome is normative for the behavior it describes.
- Runtime implementations may differ internally, but they must satisfy the fixture outcomes.
- No Epic Games assets belong in these files.

## First-slice scope

The initial contract covers:

1. one hero with health and a resource;
2. one ability with a cooldown and resource cost;
3. one card modifier;
4. deterministic damage and cooldown behavior.

The contract does not yet define matchmaking, persistence, AI, progression, or production networking.

## Acceptance target

Phase 1 is complete when the same fixture data can be executed by a headless rules test and the future Unreal implementation can consume equivalent data without changing the documented outcomes.
