# Decision 0004 — Agent Security Hardening

**Status:** Accepted as architecture contract  
**Date:** 2026-09-24

## Context

Agentic systems can pursue a legitimate research objective through unintended technical paths. Paragon therefore cannot rely on prompts or behavioral instructions as its sole security boundary.

The existing project establishes human agency, explicit safety boundaries, provenance, and review gates. This decision makes those principles enforceable against future agentic tooling.

## Decision

Paragon adopts a layered agent-security model:

1. human/project governance establishes authority;
2. scoped non-human identity constrains who the agent is;
3. capability allowlists constrain what it can reach;
4. deterministic action gates constrain what it can commit;
5. behavioral detection identifies novel or anomalous paths;
6. containment freezes the agent when required;
7. append-only provenance records the security decision chain.

Detection may restrict or escalate. Detection may never expand authority.

All security decisions fail closed when required evidence is missing.

## Consequences

- Security boundaries are enforceable independently of model intent.
- Unexpected agent behavior has a defined containment path.
- Governance changes remain human-controlled.
- Security events inherit the project's provenance discipline.
- Future runtime implementations have explicit acceptance criteria.

This adds friction to autonomous workflows. That friction is intentional where actions affect people, rights, identity, publication, external systems, or project authority.

## Non-goals

This decision does not claim that a production agent runtime already exists, make anomaly detection the authorization layer, permit adaptive permission expansion, authorize private-data scraping or autonomous outreach, or replace legal, rights, or project governance.

## Relationship to existing architecture

The security model is enforcement machinery underneath the existing authority model.

`HUMAN GOVERNANCE → PROJECT GOVERNANCE → AGENT AUTHORITY → TOOL CAPABILITY → ACTION`

`OBSERVE → UNDERSTAND → SUGGEST` remains the behavioral invariant.
