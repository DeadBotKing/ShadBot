"""
ShadBot Agent Platform

End-to-end agent platform tests.
"""

from __future__ import annotations

from uuid import uuid4

from agentplatform.application.bootstrap import (
    AgentPlatformBootstrap,
)
from agentplatform.domain.context import (
    AgentExecutionContext,
)
from agentplatform.domain.tasks import (
    AgentTask,
    TaskType,
)


def test_agent_platform_executes_complete_pipeline() -> None:
    bootstrap = AgentPlatformBootstrap()

    loop = bootstrap.build()

    task = AgentTask(
        title="Generate trading feature",
        description="Create production quality market analysis module",
        task_type=TaskType.IMPLEMENTATION,
    )

    context = AgentExecutionContext(
        project_id=uuid4(),
        task_id=task.id,
        instructions=("Analyze task, design solution, " "implement and review."),
        metadata={
            "test": "e2e",
        },
        task_title=task.title,
        task_description=task.description,
        task_type=task.task_type.value,
    )

    results = loop.execute(
        task,
        context,
    )

    assert results

    assert all(result.success for result in results)
