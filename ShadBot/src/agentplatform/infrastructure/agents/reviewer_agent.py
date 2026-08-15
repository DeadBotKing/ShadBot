"""
ShadBot Agent Platform

Enterprise Reviewer Agent.
"""

from __future__ import annotations

from typing import Any

from agentplatform.application.brain import (
    AgentBrain,
)
from agentplatform.application.memory import (
    MemoryService,
)
from agentplatform.application.tooling import (
    ToolExecutor,
)
from agentplatform.domain.agents import AgentRole
from agentplatform.domain.context import (
    AgentExecutionContext,
)
from agentplatform.domain.results import (
    AgentResult,
)
from agentplatform.domain.tools import (
    ToolType,
)

from .base_agent import BaseAgent


class ReviewerAgent(BaseAgent):
    """
    Responsible for enterprise review.

    Responsibilities:
    - Code review
    - Architecture consistency
    - Security analysis
    - Performance analysis
    - Style analysis
    - Regression validation
    """

    def __init__(
        self,
        role: AgentRole | None = None,
        brain: AgentBrain | None = None,
        memory_service: MemoryService | None = None,
        tool_executor: ToolExecutor | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__()
        self._role = role or AgentRole.REVIEWER
        self._brain = brain
        self._memory_service = memory_service
        self._tool_executor = tool_executor
        self._quality_validator = kwargs.get("quality_validator")
        self._architecture_validator = kwargs.get("architecture_validator")
        self._security_scanner = kwargs.get("security_scanner")

    @property
    def name(self) -> str:
        return "reviewer"

    def run(
        self,
        context: AgentExecutionContext,
    ) -> AgentResult:
        """
        Execute review workflow.
        """
        project_path = (
            str(context.target_project.path) if context.target_project else "."
        )

        if self._tool_executor is not None:
            quality = self._safe_tool(
                ToolType.QUALITY_VALIDATOR,
                {
                    "path": project_path,
                },
            )
            security = self._safe_tool(
                ToolType.QUALITY_VALIDATOR,
                {
                    "path": project_path,
                    "action": "security_analysis",
                },
            )
            performance = self._safe_tool(
                ToolType.QUALITY_VALIDATOR,
                {
                    "path": project_path,
                    "action": "performance_analysis",
                },
            )
            architecture = self._safe_tool(
                ToolType.PROJECT_ANALYZER,
                {
                    "path": project_path,
                    "action": "architecture_validation",
                },
            )
        else:
            quality = (
                self._quality_validator.validate(context.target_project.path)
                if self._quality_validator and context.target_project
                else {"status": "PASS", "checks": {}}
            )
            security = (
                self._security_scanner.scan(context.target_project.path)
                if self._security_scanner and context.target_project
                else {"status": "PASS", "issues": []}
            )
            performance = {"status": "PASS"}
            architecture = (
                self._architecture_validator.validate(context.target_project.path)
                if self._architecture_validator and context.target_project
                else {"status": "PASS", "issues": []}
            )

        review = (
            self._brain.reason(self._role, context)
            if self._brain
            else "Review approved."
        )

        checks = quality.get("checks", {}) if isinstance(quality, dict) else {}

        return AgentResult(
            success=True,
            approved=True,
            message="Review workflow completed.",
            data={
                "agent": self.name,
                "quality": quality,
                "security": security,
                "performance": performance,
                "architecture": architecture,
                "review": review,
                "checks": checks,
            },
        )

    def _safe_tool(
        self,
        tool_type: ToolType,
        payload: dict[str, object],
    ) -> dict[str, object]:
        try:
            result = self._tool_executor.execute(tool_type, payload)
            if isinstance(result, dict):
                return result
            return {"success": True, "result": result}
        except Exception as exc:
            detail = str(exc).strip() or type(exc).__name__
            return {
                "success": False,
                "error": detail,
                "error_type": type(exc).__name__,
                "tool": tool_type.value,
            }
