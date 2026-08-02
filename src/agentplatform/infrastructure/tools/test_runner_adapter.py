"""
ShadBot Agent Platform

Test runner adapter.
"""

from __future__ import annotations

from agentplatform.domain.tools import (
    ToolContract,
    ToolType,
)

from .test_runner import TestRunner


class TestRunnerAdapter(ToolContract):
    """
    Adapter exposing test execution as agent tool.
    """

    def __init__(self) -> None:
        self._runner = TestRunner()

    @property
    def tool_type(self) -> ToolType:
        return ToolType.TEST_RUNNER

    def execute(
        self,
        payload: dict[str, object],
    ) -> dict[str, object]:
        action = str(
            payload.get("action", ""),
        )

        if action == "python":
            return self._runner.run_python_file(
                str(payload["path"]),
            )

        if action == "pytest":
            path = payload.get("path")

            return self._runner.run_pytest(
                str(path) if path is not None else None,
            )

        raise ValueError(
            f"Unsupported test action: {action}",
        )
