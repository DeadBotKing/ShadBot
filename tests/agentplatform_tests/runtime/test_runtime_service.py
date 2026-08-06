"""
ShadBot Agent Platform

Runtime service tests.
"""

from __future__ import annotations

from uuid import uuid4

from agentplatform.application.registry import AgentRegistry
from agentplatform.application.runtime import AgentRuntimeService
from agentplatform.domain.context import AgentExecutionContext
from agentplatform.domain.results import AgentResult
from agentplatform.domain.tasks import AgentTask, TaskType


class FakeOrchestrator:
    def execute_pipeline(
        self,
        agents,
        context,
    ) -> list[AgentResult]:
        return [
            AgentResult(
                success=True,
                message="Runtime completed.",
            )
        ]


def create_task() -> AgentTask:
    return AgentTask(
        title="Runtime test",
        description="Test runtime execution.",
        task_type=TaskType.IMPLEMENTATION,
    )


def create_context() -> AgentExecutionContext:
    return AgentExecutionContext(
        project_id=uuid4(),
        task_id=uuid4(),
        instructions="Execute runtime.",
        metadata={},
    )


def test_runtime_service_execution() -> None:
    runtime = AgentRuntimeService(
        registry=AgentRegistry(),
        orchestrator=FakeOrchestrator(),  # type: ignore[arg-type]
    )

    results = runtime.execute(
        create_task(),
        create_context(),
    )

    assert len(results) == 1

    assert results[0].success is True

    assert results[0].message == "Runtime completed."
