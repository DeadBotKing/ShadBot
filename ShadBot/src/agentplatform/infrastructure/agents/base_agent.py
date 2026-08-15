"""
ShadBot Agent Platform

Base agent implementation.
"""

from __future__ import annotations

from abc import ABC, abstractmethod

from agentplatform.application.tooling import (
    ToolExecutor,
)
from agentplatform.domain.capabilities import (
    Capability,
)
from agentplatform.domain.context import (
    AgentExecutionContext,
)
from agentplatform.domain.contracts import (
    AgentContract,
)
from agentplatform.domain.results import (
    AgentResult,
)


class BaseAgent(
    AgentContract,
    ABC,
):
    """
    Enterprise base implementation for all agents.
    """

    def __init__(
        self,
        role: object | None = None,
        capabilities: list[Capability] | None = None,
        tool_executor: ToolExecutor | None = None,
    ) -> None:

        self._role = role

        self._capabilities = capabilities if capabilities is not None else []

        self._tool_executor = tool_executor

    @property
    def role(
        self,
    ) -> object | None:
        return self._role

    @property
    def capabilities(
        self,
    ) -> list[Capability]:
        return self._capabilities

    @property
    def tool_executor(
        self,
    ) -> ToolExecutor | None:
        return self._tool_executor

    def execute(
        self,
        context: AgentExecutionContext,
    ) -> AgentResult:
        """
        Execute agent safely.
        """

        try:
            return self.run(context)

        except Exception as exc:
            detail = str(exc).strip() or type(exc).__name__
            return AgentResult(
                success=False,
                message=detail,
                data={
                    "agent_error": type(exc).__name__,
                },
            )

    @abstractmethod
    def run(
        self,
        context: AgentExecutionContext,
    ) -> AgentResult:
        """
        Agent-specific implementation.
        """

        raise NotImplementedError
