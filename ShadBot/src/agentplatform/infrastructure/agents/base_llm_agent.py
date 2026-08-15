"""
ShadBot Agent Platform

Enterprise Base LLM Agent implementation.
"""

from __future__ import annotations

from abc import abstractmethod
from datetime import datetime, timezone
from typing import Any

from agentplatform.application.brain import AgentBrain
from agentplatform.application.memory import MemoryService
from agentplatform.application.tooling import ToolExecutor
from agentplatform.domain.agents import AgentRole
from agentplatform.domain.context import AgentExecutionContext
from agentplatform.domain.results import AgentResult
from agentplatform.domain.tools import ToolType

from .base_agent import BaseAgent


class BaseLLMAgent(BaseAgent):
    """
    Enterprise foundation for all LLM powered agents.

    Responsibilities:
    - Agent lifecycle management
    - LLM reasoning access
    - Tool execution access
    - Project memory interaction
    - Execution metadata enrichment
    - Standardized failure handling

    Does not contain business logic.
    """

    def __init__(
        self,
        role: AgentRole,
        brain: AgentBrain,
        tool_executor: ToolExecutor | None = None,
        memory_service: MemoryService | None = None,
        capabilities: list[Any] | None = None,
    ) -> None:
        super().__init__(role=role, capabilities=capabilities)
        self._role = role
        self._brain = brain
        self._tool_executor = tool_executor
        self._memory_service = memory_service

    @property
    def role(
        self,
    ) -> AgentRole:
        return self._role

    @property
    def name(
        self,
    ) -> str:
        return self._role.value

    @property
    def brain(
        self,
    ) -> AgentBrain:
        return self._brain

    @property
    def tool_executor(
        self,
    ) -> ToolExecutor | None:
        return self._tool_executor

    @property
    def memory_service(
        self,
    ) -> MemoryService | None:
        return self._memory_service

    def execute(
        self,
        context: AgentExecutionContext,
    ) -> AgentResult:
        """
        Execute enterprise agent lifecycle.
        """

        started_at = datetime.now(
            timezone.utc,
        )

        try:
            self.before_execute(
                context,
            )

            result = self.run(
                context,
            )

            self.after_execute(
                context,
                result,
            )

            finished_at = datetime.now(timezone.utc)
            return AgentResult(
                success=result.success,
                message=result.message,
                approved=result.approved,
                data={
                    **result.data,
                    "agent": self.name,
                    "role": self.role.value,
                    "elapsed_seconds": (finished_at - started_at).total_seconds(),
                    "execution_started_at": (started_at.isoformat()),
                    "execution_finished_at": finished_at.isoformat(),
                },
            )

        except Exception as exc:
            result = self.on_failure(
                context,
                exc,
            )
            elapsed = (
                datetime.now(timezone.utc) - started_at
            ).total_seconds()
            data = dict(result.data)
            data["elapsed_seconds"] = elapsed
            return AgentResult(
                success=result.success,
                message=result.message,
                approved=result.approved,
                data=data,
            )

    def think(
        self,
        context: AgentExecutionContext,
    ) -> str:
        """
        Execute LLM reasoning.
        """

        return self._brain.think(
            self._role,
            context,
        )

    def use_tool(
        self,
        tool_type: ToolType,
        payload: dict[str, object],
    ) -> dict[str, object]:
        """
        Execute an available agent tool.
        """

        if self._tool_executor is None:
            raise RuntimeError(
                "Tool executor is not configured.",
            )

        return self._tool_executor.execute(
            tool_type,
            payload,
        )

    def remember(
        self,
        context: AgentExecutionContext,
        content: str,
        source: str,
        confidence: float = 1.0,
    ) -> Any:
        """
        Store project scoped memory.
        """

        if self._memory_service is None:
            return None

        return self._memory_service.remember(
            project_id=context.project_id,
            content=content,
            source=source,
            confidence=confidence,
        )

    def recall(
        self,
        context: AgentExecutionContext,
    ) -> list[Any]:
        """
        Retrieve project scoped memory.
        """

        if self._memory_service is None:
            return []

        return self._memory_service.recall(
            project_id=context.project_id,
        )

    def before_execute(
        self,
        context: AgentExecutionContext,
    ) -> None:
        """
        Lifecycle hook before execution.
        """

    def after_execute(
        self,
        context: AgentExecutionContext,
        result: AgentResult,
    ) -> None:
        """
        Lifecycle hook after successful execution.
        """

    def on_failure(
        self,
        context: AgentExecutionContext,
        exception: Exception,
    ) -> AgentResult:
        """
        Standard failure handling.
        """

        detail = str(exception).strip() or type(exception).__name__
        return AgentResult(
            success=False,
            approved=False,
            message=detail,
            data={
                "agent": self.name,
                "role": self.role.value,
                "error_type": type(exception).__name__,
                "execution_id": str(
                    context.execution_id,
                ),
            },
        )

    @abstractmethod
    def run(
        self,
        context: AgentExecutionContext,
    ) -> AgentResult:
        """
        Agent-specific workflow.
        """

        raise NotImplementedError
