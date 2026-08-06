"""
ShadBot Agent Platform

Agent orchestrator tests.
"""

from __future__ import annotations

from uuid import uuid4

from agentplatform.application.orchestration import AgentOrchestrator
from agentplatform.domain.context import AgentExecutionContext
from agentplatform.domain.results import AgentResult


class FakeAgent:
    name = "architect"

    def run(
        self,
        context: AgentExecutionContext,
    ) -> AgentResult:
        return AgentResult(
            success=True,
            message="Architecture completed.",
            data={
                "agent": "architect",
                "architecture_plan": "plan",
            },
        )


class FakeExecutionService:
    def execute(
        self,
        agent,
        context,
    ) -> AgentResult:
        return agent.run(context)


def create_context() -> AgentExecutionContext:
    return AgentExecutionContext(
        project_id=uuid4(),
        task_id=uuid4(),
        instructions="orchestrate",
        metadata={},
    )


def test_orchestrator_propagates_agent_result() -> None:
    orchestrator = AgentOrchestrator(
        execution_service=FakeExecutionService(),  # type: ignore[arg-type]
    )

    results = orchestrator.execute_pipeline(
        agents=[
            FakeAgent(),  # type: ignore[arg-type]
        ],
        context=create_context(),
    )

    assert len(results) == 1

    assert results[0].success is True

    assert results[0].data["agent"] == "architect"
