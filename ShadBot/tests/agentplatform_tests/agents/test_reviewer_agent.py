"""
ShadBot Agent Platform

Reviewer agent tests.
"""

from __future__ import annotations

from pathlib import Path
from uuid import uuid4

from agentplatform.domain.context import AgentExecutionContext
from agentplatform.domain.workspace import Project
from agentplatform.infrastructure.agents.reviewer_agent import ReviewerAgent


class FakeQualityValidator:
    """
    Fake quality validator for agent test.
    """

    def validate(
        self,
        path: Path,
    ) -> dict[str, object]:
        return {
            "status": "PASS",
            "checks": {},
        }


class FakeArchitectureValidator:
    """
    Fake architecture validator for agent test.
    """

    def validate(
        self,
        path: Path,
    ) -> dict[str, object]:
        return {
            "status": "PASS",
            "issues": [],
        }


class FakeSecurityScanner:
    """
    Fake security scanner for agent test.
    """

    def scan(
        self,
        path: Path,
    ) -> dict[str, object]:
        return {
            "status": "PASS",
            "issues": [],
        }


def test_reviewer_agent_execution() -> None:
    context = AgentExecutionContext(
        project_id=uuid4(),
        task_id=uuid4(),
        instructions="Review code.",
        metadata={},
        task_title="Review Task",
        task_description="Review implementation.",
        task_type="review",
        target_project=Project(
            name="TestProject",
            path=Path("."),
            project_type="software",
        ),
    )

    agent = ReviewerAgent(
        quality_validator=FakeQualityValidator(),
        architecture_validator=FakeArchitectureValidator(),
        security_scanner=FakeSecurityScanner(),
    )

    result = agent.run(
        context,
    )

    assert result.success is True
    assert result.data["agent"] == "reviewer"
    assert result.approved is True
    assert "checks" in result.data
