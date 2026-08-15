"""
ShadBot Agent Platform

R&D Agent tests.
"""

from __future__ import annotations

from uuid import uuid4

from agentplatform.domain.context import AgentExecutionContext
from agentplatform.domain.results import AgentResult
from agentplatform.infrastructure.agents.rnd_agent import RND_Agent


class FakeToolExecutor:
    def execute(self, tool_type, payload):
        return {"status": "SUCCESS", "findings": ["Explored new technique"]}


def test_rnd_agent_execution() -> None:
    agent = RND_Agent(tool_executor=FakeToolExecutor())
    context = AgentExecutionContext(
        project_id=uuid4(),
        task_id=uuid4(),
        instructions="Research new ML algorithms",
        task_title="R&D Task",
    )

    result = agent.run(context)
    assert isinstance(result, AgentResult)
    assert result.success is True
    assert result.data["agent"] == "rnd"
    research_obj = result.data["research"]
    assert research_obj.query == "Research new ML algorithms"
    assert research_obj.summary == "RND execution completed."
