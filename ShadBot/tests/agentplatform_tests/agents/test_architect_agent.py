"""
ShadBot Agent Platform

Architect Agent tests.
"""

from __future__ import annotations

from uuid import uuid4

from agentplatform.application.brain import AgentBrain
from agentplatform.domain.architecture_plan import ArchitecturePlan
from agentplatform.domain.context import AgentExecutionContext
from agentplatform.domain.results import AgentResult
from agentplatform.infrastructure.agents import ArchitectAgent


class FakeReasoning:
    """
    Fake reasoning implementation.
    """

    def reason(
        self,
        role,
        context,
    ) -> str:
        return "Architecture design generated."


def create_agent() -> ArchitectAgent:
    """
    Create architect agent.
    """

    brain = AgentBrain(
        reasoning=FakeReasoning(),
    )

    return ArchitectAgent(
        role=None,  # type: ignore[arg-type]
        brain=brain,
    )


def create_context() -> AgentExecutionContext:
    """
    Create execution context.
    """

    return AgentExecutionContext(
        project_id=uuid4(),
        task_id=uuid4(),
        instructions="Design architecture.",
        task_title="Implement feature",
        task_description="Create enterprise module",
        task_type="development",
    )


def test_architect_agent_execution() -> None:
    """
    Validate architect workflow.
    """

    agent = create_agent()

    context = create_context()

    result = agent.run(
        context,
    )

    assert isinstance(
        result,
        AgentResult,
    )

    assert result.success is True

    assert result.message == ("Architecture plan generated.")

    assert "architecture_plan" in result.data

    plan = result.data["architecture_plan"]

    assert isinstance(
        plan,
        ArchitecturePlan,
    )

    assert plan.summary == ("Architecture design generated.")

    assert (
        len(
            plan.implementation_order,
        )
        == 1
    )

    assert "Architect does not generate source code" in plan.constraints
