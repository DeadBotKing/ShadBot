"""
ShadBot Agent Platform

Agent Transition Manager component for 6.4 Agent Handoff.
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from uuid import UUID
from .handoff_request import HandoffRequest


@dataclass(frozen=True, slots=True)
class AgentTransitionRecord:
    from_agent: str
    to_agent: str
    task_id: UUID
    timestamp: str


class AgentTransitionManager:
    """
    Manages and records state transitions between agents.
    """

    def __init__(self) -> None:
        self._transitions: list[AgentTransitionRecord] = []

    def record_transition(self, request: HandoffRequest) -> AgentTransitionRecord:
        rec = AgentTransitionRecord(
            from_agent=request.source_agent_name,
            to_agent=request.target_agent_name,
            task_id=request.task_id,
            timestamp=datetime.now(timezone.utc).isoformat(),
        )
        self._transitions.append(rec)
        return rec

    def get_transitions(self) -> tuple[AgentTransitionRecord, ...]:
        return tuple(self._transitions)
