"""
ShadBot Agent Platform

Unified service for 8.2 Agent Messaging.
"""

from __future__ import annotations

from typing import Any
from uuid import UUID, uuid4
from .message_contract import MessageReceiverContract
from .message_entity import AgentMessage
from .message_history import MessageHistoryTracker
from .message_priority import MessagePriorityManager
from .message_routing import MessageRouter
from .message_validation import MessageValidationResult, MessageValidator


class AgentMessagingService:
    """
    Orchestrates sending, validation, routing, prioritization, and history tracking of agent messages.
    """

    def __init__(
        self,
        validator: MessageValidator | None = None,
        router: MessageRouter | None = None,
        priority_mgr: MessagePriorityManager | None = None,
        history: MessageHistoryTracker | None = None,
    ) -> None:
        self.validator = validator or MessageValidator()
        self.router = router or MessageRouter()
        self.priority_mgr = priority_mgr or MessagePriorityManager()
        self.history = history or MessageHistoryTracker()

    def register_agent(self, agent_name: str, receiver: MessageReceiverContract) -> None:
        self.router.register_receiver(agent_name, receiver)

    def send_message(
        self,
        sender: str,
        receiver: str,
        msg_type: str,
        payload: dict[str, Any],
        priority: str = "NORMAL",
    ) -> tuple[AgentMessage, MessageValidationResult, bool]:
        msg = AgentMessage(
            message_id=uuid4(),
            sender=sender,
            receiver=receiver,
            message_type=msg_type,
            payload=payload,
            priority=priority,
        )
        val = self.validator.validate(msg)
        if not val.valid:
            return msg, val, False

        self.history.record_message(msg)
        delivered = self.router.route_message(msg)
        return msg, val, delivered
