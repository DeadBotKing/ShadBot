"""
ShadBot Agent Platform

Reasoning context provider.
"""

from __future__ import annotations

from typing import Any

from agentplatform.domain.agents import AgentRole
from agentplatform.domain.context import (
    AgentExecutionContext,
)


class ReasoningContextProvider:
    """
    Provides reasoning metadata context.
    """

    def __init__(
        self,
        reasoning_engine: object,
        role: AgentRole,
        context: AgentExecutionContext,
    ) -> None:

        self._reasoning_engine = reasoning_engine
        self._role = role
        self._context = context

    def provide(
        self,
    ) -> dict[str, Any]:
        """
        Build reasoning context.
        """

        return {
            "agent_role": self._role.value,
            "context_id": str(
                self._context.execution_id,
            ),
            "reasoning_engine": (self._reasoning_engine.__class__.__name__),
        }
