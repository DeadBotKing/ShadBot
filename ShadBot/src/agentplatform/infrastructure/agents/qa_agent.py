"""
ShadBot Agent Platform

Enterprise QA Agent.
"""

from __future__ import annotations

from typing import Any

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

from .base_llm_agent import BaseLLMAgent

SHADBOT_BUILD = "2026-08-13-qafix"


class QAAgent(BaseLLMAgent):
    """
    Responsible for quality assurance.

    Responsibilities:
    - Test generation
    - Test execution
    - Coverage analysis
    - Regression detection
    - Release validation
    """

    def __init__(
        self,
        tool_executor: ToolExecutor | None = None,
        role: Any = AgentRole.QA,
        brain: Any = None,
        memory_service: Any = None,
        **kwargs: Any,
    ) -> None:

        super().__init__(
            role=role,
            brain=brain,
            tool_executor=tool_executor,
            memory_service=memory_service,
        )

    @property
    def name(self) -> str:
        return "qa"

    def run(
        self,
        context: AgentExecutionContext,
    ) -> AgentResult:
        """
        Execute QA workflow.

        Tool/check failures are captured as findings. The agent itself
        completes successfully so the pipeline can continue to reviewer.
        """

        if context.target_project is None:
            return AgentResult(
                success=False,
                message="Target project is required.",
                data={
                    "agent": self.name,
                },
            )

        if self._tool_executor is None:
            return AgentResult(
                success=False,
                message="Tool executor is not configured.",
                data={
                    "agent": self.name,
                },
            )

        project_path = str(
            context.target_project.path,
        )

        print(f"[QA] build={SHADBOT_BUILD} validating {project_path}")

        tests = self._safe_tool(
            ToolType.TEST_RUNNER,
            {
                "path": project_path,
            },
        )

        validation = self._safe_tool(
            ToolType.QUALITY_VALIDATOR,
            {
                "path": project_path,
            },
        )

        coverage = self._safe_tool(
            ToolType.TEST_RUNNER,
            {
                "path": project_path,
                "action": "coverage_analysis",
            },
        )

        regression = self._safe_tool(
            ToolType.QUALITY_VALIDATOR,
            {
                "path": project_path,
                "action": "regression_analysis",
            },
        )

        findings = self._has_findings(tests, validation, coverage, regression)
        message = (
            "QA workflow completed with findings."
            if findings
            else "QA workflow completed."
        )

        return AgentResult(
            success=True,
            approved=not findings,
            message=message,
            data={
                "agent": self.name,
                "shadbot_build": SHADBOT_BUILD,
                "tests": tests,
                "validation": validation,
                "coverage": coverage,
                "regression_analysis": regression,
                "findings": findings,
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

    @staticmethod
    def _has_findings(*reports: dict[str, object]) -> bool:
        for report in reports:
            if report.get("success") is False:
                return True
            if str(report.get("status", "")).upper() == "FAIL":
                return True
            if report.get("error"):
                return True
        return False
