"""
ShadBot Agent Platform

Reasoning request contract.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from uuid import UUID

from agentplatform.domain.agents import AgentRole
from agentplatform.domain.context import AgentExecutionContext

from .reasoning_mode import ReasoningMode


@dataclass(frozen=True, slots=True)
class ReasoningRequest:
    """
    Input contract for reasoning execution.
    """

    agent_role: AgentRole

    context: AgentExecutionContext

    mode: ReasoningMode = ReasoningMode.ANALYTICAL

    objective: str = ""

    metadata: dict[str, object] = field(
        default_factory=dict,
    )

    request_id: UUID | None = None
