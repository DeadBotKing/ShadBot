"""
ShadBot Agent Platform

Enterprise Runtime Observer Agent.
"""

from __future__ import annotations

from typing import Any
from agentplatform.domain.agents import AgentRole

from agentplatform.application.tooling import (
    ToolExecutor,
)
from agentplatform.domain.context import (
    AgentExecutionContext,
)
from agentplatform.domain.results import (
    AgentResult,
)
from agentplatform.domain.tools import (
    ToolType,
)

from .base_llm_agent import BaseLLMAgent


class RuntimeObserverAgent(BaseLLMAgent):
    """
    Responsible for runtime intelligence.

    Responsibilities:
    - Runtime monitoring
    - Runtime analysis
    - Failure detection
    - Performance analysis
    - Anomaly detection
    """

    def __init__(
        self,
        tool_executor: ToolExecutor | None = None,
        role: Any = AgentRole.RUNTIME_OBSERVER,
        brain: Any = None,
        memory_service: Any = None,
        **kwargs: Any,
    ) -> None:

        super().__init__(
            role=role,
            brain=brain,
            tool_executor=tool_executor,
            memory_service=memory_service,
        )

    @property
    def name(self) -> str:
        return "runtime_observer"

    def run(
        self,
        context: AgentExecutionContext,
    ) -> AgentResult:
        """
        Execute runtime observation workflow.
        """

        if context.target_project is None:
            return AgentResult(
                success=False,
                message="Target project is required.",
                data={
                    "agent": self.name,
                },
            )

        project_path = str(
            context.target_project.path,
        )

        monitoring = self.tool_executor.execute(
            ToolType.EXECUTION_MONITOR,
            {
                "path": project_path,
            },
        )

        metrics = self.tool_executor.execute(
            ToolType.METRICS_COLLECTOR,
            {
                "path": project_path,
            },
        )

        logs = self.tool_executor.execute(
            ToolType.LOG_ANALYZER,
            {
                "path": project_path,
            },
        )

        health = self.tool_executor.execute(
            ToolType.SYSTEM_HEALTH,
            {
                "path": project_path,
            },
        )

        return AgentResult(
            success=True,
            message="Runtime observation completed.",
            data={
                "agent": self.name,
                "monitoring": monitoring,
                "metrics": metrics,
                "logs": logs,
                "health": health,
            },
        )
