"""
ShadBot Agent Platform

Agent execution loop.
"""

from __future__ import annotations

from dataclasses import dataclass

from agentplatform.application.brain import (
    AgentBrain,
)
from agentplatform.application.runtime import (
    AgentRuntimeService,
)
from agentplatform.application.runtime.retry_coordinator import (
    RetryCoordinator,
)
from agentplatform.application.tasks import (
    ProjectTaskService,
)
from agentplatform.application.validation import (
    ValidationEngine,
)
from agentplatform.domain.context import (
    AgentExecutionContext,
)
from agentplatform.domain.results import (
    AgentResult,
)
from agentplatform.domain.tasks import (
    AgentTask,
)


@dataclass(slots=True)
class AgentExecutionLoop:
    """
    Enterprise autonomous agent execution pipeline.
    """

    brain: AgentBrain

    runtime: AgentRuntimeService

    retry_coordinator: RetryCoordinator

    validation_engine: ValidationEngine

    task_service: ProjectTaskService

    def execute(
        self,
        task: AgentTask,
        context: AgentExecutionContext,
    ) -> list[AgentResult]:
        """
        Execute complete agent pipeline through runtime.
        """

        return self.runtime.execute(
            task,
            context,
        )
