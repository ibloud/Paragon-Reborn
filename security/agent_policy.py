"""Dependency-free reference policy for Paragon agent enforcement."""

from dataclasses import dataclass
from enum import Enum


class Decision(str, Enum):
    CONTINUE = "continue"
    STOP = "stop"
    CONTAIN = "contain"
    DENY = "deny"


class State(str, Enum):
    NORMAL = "normal"
    SUSPICIOUS = "suspicious"
    CONTAINED = "contained"
    REVIEWED = "reviewed"
    RELEASED = "released"
    FORBIDDEN = "forbidden"


class Action(str, Enum):
    READ = "read"
    DRAFT = "draft"
    ASK = "ask"
    ACT = "act"


@dataclass(frozen=True)
class Authorization:
    identity_ok: bool
    capability_ok: bool
    resource_ok: bool
    governance_ok: bool
    provenance_ok: bool


@dataclass(frozen=True)
class Observation:
    unknown: bool = False
    suspicious: bool = False
    forbidden: bool = False


def authorize(auth: Authorization, action: Action, obs: Observation) -> Decision:
    """Return a fail-closed deterministic decision."""
    if obs.forbidden:
        return Decision.DENY
    if obs.unknown:
        return Decision.STOP
    if obs.suspicious:
        return Decision.CONTAIN
    if not all((auth.identity_ok, auth.capability_ok, auth.resource_ok,
                auth.governance_ok, auth.provenance_ok)):
        return Decision.STOP
    if action is Action.ACT and not auth.governance_ok:
        return Decision.STOP
    return Decision.CONTINUE


_ALLOWED_TRANSITIONS = {
    State.NORMAL: {State.SUSPICIOUS, State.CONTAINED, State.FORBIDDEN},
    State.SUSPICIOUS: {State.CONTAINED, State.FORBIDDEN},
    State.CONTAINED: {State.REVIEWED, State.FORBIDDEN},
    State.REVIEWED: {State.RELEASED, State.CONTAINED, State.FORBIDDEN},
    State.RELEASED: {State.NORMAL, State.SUSPICIOUS, State.CONTAINED, State.FORBIDDEN},
    State.FORBIDDEN: set(),
}


def transition(current: State, target: State) -> State:
    """Apply the containment state machine; invalid transitions fail closed."""
    if target not in _ALLOWED_TRANSITIONS[current]:
        raise ValueError(f"invalid security-state transition: {current.value} -> {target.value}")
    return target
