"""
ShadBot Agent Platform

Message Routing component for 8.2 Agent Messaging.
"""

from __future__ import annotations

from .message_contract import MessageReceiverContract
from .message_entity import AgentMessage


class MessageRouter:
    """
    Routes agent messages to their destination agent receiver.
    """

    def __init__(self) -> None:
        self._receivers: dict[str, MessageReceiverContract] = {}

    def register_receiver(self, agent_name: str, receiver: MessageReceiverContract) -> None:
        self._receivers[agent_name] = receiver

    def route_message(self, message: AgentMessage) -> bool:
        receiver = self._receivers.get(message.receiver)
        if receiver is None:
            return False
        receiver.on_message(message)
        return True
