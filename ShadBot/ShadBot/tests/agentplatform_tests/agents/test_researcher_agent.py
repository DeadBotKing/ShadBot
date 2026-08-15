"""
ShadBot Agent Platform

Researcher Agent tests.
"""

from __future__ import annotations

from uuid import uuid4

from agentplatform.application.brain import AgentBrain
from agentplatform.application.llm import LLMProvider
from agentplatform.domain.context import AgentExecutionContext
from agentplatform.domain.research import ResearchReport
from agentplatform.domain.results import AgentResult
from agentplatform.infrastructure.agents import ResearcherAgent


class FakeLLM(LLMProvider):
    """
    Fake LLM provider.
    """

    def generate(
        self,
        prompt: str,
    ) -> str:
        return "Research analysis completed."


class FakeReasoning:
    """
    Fake reasoning layer.
    """

    def reason(
        self,
        role,
        context,
    ) -> str:
        return "Enterprise pattern research completed."


def create_agent() -> ResearcherAgent:
    """
    Create researcher agent.
    """

    brain = AgentBrain(
        reasoning=FakeReasoning(),
    )

    return ResearcherAgent(
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
        instructions="Research architecture patterns.",
    )


def test_researcher_agent_execution() -> None:
    """
    Validate researcher workflow.
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

    assert result.message == "Research completed."

    assert "research_report" in result.data

    report = result.data["research_report"]

    assert isinstance(
        report,
        ResearchReport,
    )

    assert report.summary == ("Enterprise pattern research completed.")

    assert "Clean Architecture" in report.patterns
