"""
ShadBot Agent Platform

Unit tests for 8.2 Agent Messaging.
"""

from __future__ import annotations

from agentplatform.application.communication.agent_messaging import (
    AgentMessage,
    AgentMessagingService,
    MessageReceiverContract,
)


class FakeReceiver(MessageReceiverContract):
    def __init__(self) -> None:
        self.messages: list[AgentMessage] = []

    def on_message(self, message: AgentMessage) -> None:
        self.messages.append(message)


def test_agent_messaging_service_sends_message() -> None:
    service = AgentMessagingService()
    receiver = FakeReceiver()
    service.register_agent("engineer", receiver)

    msg, val, delivered = service.send_message(
        sender="architect",
        receiver="engineer",
        msg_type="ArchitectureCompleted",
        payload={"plan": "Layered"},
        priority="CRITICAL",
    )
    assert val.valid is True
    assert delivered is True
    assert len(receiver.messages) == 1
    assert receiver.messages[0].priority == "CRITICAL"


def test_agent_messaging_history_tracks_messages() -> None:
    service = AgentMessagingService()
    service.send_message("architect", "engineer", "test", {})
    history = service.history.get_agent_messages("architect")
    assert len(history) == 1
