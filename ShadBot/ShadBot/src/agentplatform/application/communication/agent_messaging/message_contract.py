"""
ShadBot Agent Platform

Message Contract interface for 8.2 Agent Messaging.
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from .message_entity import AgentMessage


class MessageReceiverContract(ABC):
    """
    Contract for receiving direct agent messages.
    """

    @abstractmethod
    def on_message(self, message: AgentMessage) -> None:
        raise NotImplementedError
