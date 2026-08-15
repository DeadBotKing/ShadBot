"""
ShadBot Agent Platform

Agent execution loop tests.
"""

from __future__ import annotations

from uuid import uuid4

from agentplatform.application.loop import AgentExecutionLoop
from agentplatform.application.retry import (
    RetryEngine,
    RetryPolicy,
)
from agentplatform.application.runtime.retry_coordinator import (
    RetryCoordinator,
)
from agentplatform.application.tasks import ProjectTaskService
from agentplatform.application.validation import ValidationEngine
from agentplatform.domain.context import AgentExecutionContext
from agentplatform.domain.results import AgentResult
from agentplatform.domain.tasks import AgentTask, TaskType
from agentplatform.infrastructure.tasks import YamlTaskLoader


class FakeRuntime:
    def execute(
        self,
        task: AgentTask,
        context: AgentExecutionContext,
    ) -> list[AgentResult]:
        return [
            AgentResult(
                success=True,
                message="Completed",
            )
        ]


def create_task() -> AgentTask:
    return AgentTask(
        title="Test task",
        description="Test execution loop",
        task_type=TaskType.IMPLEMENTATION,
    )


def create_context() -> AgentExecutionContext:
    return AgentExecutionContext(
        project_id=uuid4(),
        task_id=uuid4(),
        instructions="Execute test",
        metadata={},
        task_title="Test task",
        task_description="Test execution loop",
        task_type="implementation",
    )


class FakeBrain:
    pass


def test_execution_loop_accepts_successful_execution() -> None:
    loop = AgentExecutionLoop(
        brain=FakeBrain(),
        runtime=FakeRuntime(),  # type: ignore[arg-type]
        retry_coordinator=RetryCoordinator(
            retry_engine=RetryEngine(
                policy=RetryPolicy(
                    max_retries=3,
                ),
            ),
        ),
        validation_engine=ValidationEngine(),
        task_service=ProjectTaskService(
            loader=YamlTaskLoader(),
        ),
    )

    results = loop.execute(
        create_task(),
        create_context(),
    )

    assert len(results) == 1
    assert results[0].success is True
