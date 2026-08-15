"""
ShadBot Agent Platform

Message Priority Management component for 8.2 Agent Messaging.
"""

from __future__ import annotations

from typing import Sequence
from .message_entity import AgentMessage


class MessagePriorityManager:
    """
    Sorts and prioritizes agent message queues by priority level.
    """

    def prioritize(self, messages: Sequence[AgentMessage]) -> tuple[AgentMessage, ...]:
        order = {"CRITICAL": 1, "NORMAL": 2, "BACKGROUND": 3}
        return tuple(sorted(messages, key=lambda m: order.get(m.priority, 99)))
