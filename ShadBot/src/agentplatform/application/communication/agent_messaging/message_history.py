"""
ShadBot Agent Platform

Message History Tracking component for 8.2 Agent Messaging.
"""

from __future__ import annotations

from typing import Sequence
from uuid import UUID
from .message_entity import AgentMessage


class MessageHistoryTracker:
    """
    Tracks and retrieves agent communication history for audit and debugging.
    """

    def __init__(self) -> None:
        self._history: list[AgentMessage] = []

    def record_message(self, message: AgentMessage) -> None:
        self._history.append(message)

    def get_agent_messages(self, agent_name: str) -> tuple[AgentMessage, ...]:
        return tuple(m for m in self._history if m.sender == agent_name or m.receiver == agent_name)
