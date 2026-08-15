"""
ShadBot Agent Platform

Project Intelligence Agent tests.
"""

from __future__ import annotations

from pathlib import Path
from uuid import uuid4

from agentplatform.domain.context import AgentExecutionContext
from agentplatform.domain.results import AgentResult
from agentplatform.domain.tools import ToolType
from agentplatform.domain.workspace import Project
from agentplatform.infrastructure.agents import (
    ProjectIntelligenceAgent,
)


class FakeToolExecutor:
    """
    Fake project analyzer tool executor.
    """

    def __init__(self) -> None:
        self.executed_tool = None
        self.payload = None

    def execute(
        self,
        tool_type: ToolType,
        payload: dict[str, object],
    ) -> dict[str, object]:
        self.executed_tool = tool_type
        self.payload = payload

        return {
            "summary": "Meryx project analyzed.",
            "technologies": [
                "Python",
                "Django",
            ],
            "frameworks": [
                "Django",
            ],
            "languages": [
                "Python",
            ],
            "dependencies": {
                "django": "6.0",
            },
            "architecture": "Layered architecture",
            "conventions": [
                "CamelCase",
            ],
            "constraints": [
                "Enterprise only",
            ],
            "recommendations": [
                "Continue implementation",
            ],
            "current_state": "Phase 1",
        }


def create_context() -> AgentExecutionContext:
    """
    Create execution context.
    """

    project = Project(
        name="Meryx",
        path=Path("C:/Workspace/Meryx"),
        project_type="software",
    )

    return AgentExecutionContext(
        project_id=uuid4(),
        task_id=uuid4(),
        instructions="Analyze project.",
        target_project=project,
    )


def test_project_intelligence_agent_execution() -> None:
    """
    Validate project intelligence analysis.
    """

    executor = FakeToolExecutor()

    agent = ProjectIntelligenceAgent(
        tool_executor=executor,  # type: ignore[arg-type]
    )

    context = create_context()

    result = agent.run(
        context,
    )

    assert isinstance(
        result,
        AgentResult,
    )

    assert result.success is True

    assert result.message == "Project intelligence analysis completed."

    assert executor.executed_tool == ToolType.PROJECT_ANALYZER

    assert executor.payload == {
        "path": "C:/Workspace/Meryx",
    }

    assert "agent_context_package" in context.metadata

    package = context.metadata["agent_context_package"]

    assert package.summary == "Meryx project analyzed."

    assert package.technologies == (
        "Python",
        "Django",
    )

    assert package.frameworks == ("Django",)

    assert package.languages == ("Python",)

    assert package.dependencies == {
        "django": "6.0",
    }

    assert package.architecture_description == ("Layered architecture")

    assert package.conventions == ("CamelCase",)

    assert package.constraints == ("Enterprise only",)

    assert package.recommendations == ("Continue implementation",)

    assert package.current_state == "Phase 1"
