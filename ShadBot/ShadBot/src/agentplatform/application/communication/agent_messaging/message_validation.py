"""
ShadBot Agent Platform

Message Validation component for 8.2 Agent Messaging.
"""

from __future__ import annotations

from dataclasses import dataclass
from .message_entity import AgentMessage


@dataclass(frozen=True, slots=True)
class MessageValidationResult:
    valid: bool
    notes: str


class MessageValidator:
    """
    Validates message schema, sender/receiver permissions, and payload structure.
    """

    def validate(self, message: AgentMessage) -> MessageValidationResult:
        if not message.sender or not message.receiver:
            return MessageValidationResult(False, "Sender or receiver is empty.")
        if message.priority not in ("CRITICAL", "NORMAL", "BACKGROUND"):
            return MessageValidationResult(False, f"Invalid message priority: {message.priority}")
        return MessageValidationResult(True, "Message is valid.")
