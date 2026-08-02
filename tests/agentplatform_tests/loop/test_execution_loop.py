"""
ShadBot Agent Platform

Agent execution loop tests.
"""

from __future__ import annotations

from uuid import uuid4

from agentplatform.application.decision import DecisionEngine
from agentplatform.application.loop import AgentExecutionLoop
from agentplatform.application.retry import (
    RetryEngine,
    RetryPolicy,
)
from agentplatform.application.runtime.retry_coordinator import (
    RetryCoordinator,
)
from agentplatform.domain.context import AgentExecutionContext
from agentplatform.domain.results import AgentResult
from agentplatform.domain.tasks import AgentTask, TaskType


class FakeRuntime:
    """
    Fake runtime for execution loop testing.
    """

    def __init__(
        self,
        results: list[list[AgentResult]],
    ) -> None:
        self._results = results
        self._index = 0

    def execute(
        self,
        task: AgentTask,
        context: AgentExecutionContext,
    ) -> list[AgentResult]:
        result = self._results[self._index]

        self._index += 1

        return result


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


def create_loop(
    runtime: FakeRuntime,
) -> AgentExecutionLoop:
    retry_engine = RetryEngine(
        policy=RetryPolicy(
            max_retries=3,
        ),
    )

    return AgentExecutionLoop(
        runtime=runtime,
        decision_engine=DecisionEngine(),
        retry_coordinator=RetryCoordinator(
            retry_engine=retry_engine,
        ),
    )


def test_execution_loop_accepts_successful_execution() -> None:
    runtime = FakeRuntime(
        [
            [
                AgentResult(
                    success=True,
                    message="Completed",
                ),
            ],
        ],
    )

    loop = create_loop(runtime)

    results = loop.execute(
        create_task(),
        create_context(),
    )

    assert len(results) == 1
    assert results[0].success is True


def test_execution_loop_retries_failed_review() -> None:
    runtime = FakeRuntime(
        [
            [
                AgentResult(
                    success=True,
                    message="Rejected",
                    approved=False,
                    data={},
                ),
            ],
            [
                AgentResult(
                    success=True,
                    message="Accepted",
                    approved=True,
                ),
            ],
        ],
    )

    loop = create_loop(runtime)

    results = loop.execute(
        create_task(),
        create_context(),
    )

    assert len(results) == 1
    assert results[0].message == "Accepted"
