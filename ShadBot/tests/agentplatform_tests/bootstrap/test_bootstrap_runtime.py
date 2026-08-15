"""
ShadBot Agent Platform

Bootstrap integration tests.
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


def test_bootstrap_builds_runtime() -> None:
    """
    Ensure bootstrap creates a working runtime.
    """

    runtime = AgentPlatformBootstrap().build()

    task = AgentTask(
        title="Create calculator service",
        description="Create production quality calculator implementation.",
        task_type=TaskType.IMPLEMENTATION,
    )

    context = AgentExecutionContext(
        project_id=uuid4(),
        task_id=task.id,
        instructions="Generate production code.",
        task_title=task.title,
        task_description=task.description,
        task_type=task.task_type.value,
        metadata={
            "output_file": "generated/calculator.py",
        },
    )

    results = runtime.execute(
        task,
        context,
    )

    assert results
    assert len(results) == 4

    messages = [result.message for result in results]

    assert "Project intelligence analysis completed." in messages
    assert "Architecture plan generated." in messages
    assert "Engineering completed." in messages
    assert "Review workflow completed." in messages
