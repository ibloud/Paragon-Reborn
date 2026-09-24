# Paragon Agent Security Contract

## Status

Implemented as an architecture contract and deterministic validation reference. Runtime agent enforcement is not yet present in this pre-production repository.

## 1. Security invariant

The project invariant is: `OBSERVE → UNDERSTAND → SUGGEST`.

No agent pathway may terminate in autonomous external action when that action affects a person, their account, identity, publication, rights, or resources.

The invariant is machine-enforceable at the action boundary. An agent may prepare an action; the authority to commit the action remains outside the agent unless an explicitly governed capability permits it.

## 2. Authority hierarchy

Authority flows downward only: `HUMAN GOVERNANCE → PROJECT GOVERNANCE → AGENT AUTHORITY → TOOL CAPABILITY → INDIVIDUAL ACTION`.

An agent may not promote itself upward.

**Ambiguity travels upward, never downward.**

If governance, authorization, identity, capability, provenance, or containment state cannot be established, the action fails closed.

Missing evidence is not permission. Model confidence is not permission.

## 3. Deterministic enforcement layers

### Layer 1 — Identity boundary
Agents use scoped non-human identities.
- no inheritance of a human's unrestricted credential scope;
- credentials are bound to an explicit agent role and environment;
- identity scope is independently revocable;
- credentials are never discovered by the agent from arbitrary local or remote sources.

### Layer 2 — Capability boundary
Capabilities are explicit allowlists. Default state: **deny**.

A capability identifies tool, resource class, permitted operation, environment, data sensitivity boundary, and rate/volume constraint.

### Layer 3 — Action boundary
Actions are classified before execution.
- **READ**: approved resource scope only;
- **DRAFT**: proposed artifact without external commitment;
- **ASK**: requires human/governance decision;
- **ACT**: requires explicitly authorized capability and passes deterministic checks.

Irreversible, external-facing, identity-affecting, rights-affecting, or publication actions are never authorized solely by model reasoning.

## 4. Behavioral detection
Monitor novel tools/resources, unexpected sequences, route deviation, velocity, repeated boundary probing, unusual egress, and repeated authorization failures.

Anomaly detection may stop or escalate an action. It may **never grant a capability or expand permission**.

## 5. Adaptive governance
Safe direction: `trace → anomaly → containment/review → possible restriction`

Forbidden direction: `trace → model learns → permission expands`

The security system cannot learn its way around project governance. Changes to the prohibited-action list or authority hierarchy require an explicit governance change.

## 6. Containment
Security state machine: `NORMAL → SUSPICIOUS → CONTAINED → REVIEWED → RELEASED`

Additional terminal outcome: `FORBIDDEN → DENIED / FROZEN`

- **NORMAL** — expected and authorized behavior.
- **SUSPICIOUS** — novel/anomalous behavior; further action may halt.
- **CONTAINED** — capabilities frozen/restricted pending review.
- **REVIEWED** — human/governance review established a disposition.
- **RELEASED** — explicitly restored to an authorized operating state.
- **FORBIDDEN** — deterministic policy violation; deny immediately and record.

Explicit prohibition bypasses SUSPICIOUS and goes directly to denial/freeze.

## 7. Fail-closed decision logic
```text
AUTHORIZED
    |
    +-- expected   → CONTINUE
    +-- unknown    → STOP / ESCALATE
    +-- suspicious → CONTAIN / REVIEW
    +-- forbidden  → DENY / FREEZE / RECORD
```

**UNKNOWN never becomes AUTHORIZED through model confidence or adaptive learning.**

## 8. Security-event provenance
Every consequential agent transition produces an append-only provenance record: `IntentRecord → authorization decision → tool invocation → resource touched → result → behavioral classification → containment/release decision → human review`.

Minimum event fields: event identifier, timestamp, agent identity, governing intent, authority level, capability requested, resource, action, authorization result, policy version, behavioral classification, containment state, provenance/reference chain, and reviewer where applicable.

The agent cannot rewrite, delete, or retroactively alter its own security history.

## 9. Existing Paragon boundaries retained
This contract preserves OBSERVE → UNDERSTAND → SUGGEST; explicit prohibition of autonomous outreach and engagement actions; separation of original, licensed, proposed, and separately governed material; rights/provenance as evidence-backed state; legal and naming gates; and human review for governance changes.

## 10. Acceptance criteria
Future runtime implementation is not compliant unless tests demonstrate that:
1. missing authorization denies;
2. missing identity denies;
3. missing capability denies;
4. unknown resources cannot be reached by default;
5. forbidden actions are denied without model discretion;
6. suspicious behavior can contain an agent;
7. containment prevents further governed actions;
8. anomaly detection cannot grant permissions;
9. security events are append-only from the agent's perspective;
10. release from containment requires explicit governance;
11. governance ambiguity escalates rather than authorizes;
12. OBSERVE → UNDERSTAND → SUGGEST remains intact.