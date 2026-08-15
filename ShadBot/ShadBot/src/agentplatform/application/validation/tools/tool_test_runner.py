"""
ShadBot Agent Platform

Tool Test Runner
"""

from __future__ import annotations

from agentplatform.domain.tools import (
    Tool,
)

from .tool_test_case import (
    ToolTestCase,
)
from .tool_test_result import (
    ToolTestResult,
)
from .tool_validator import (
    ToolValidator,
)


class ToolTestRunner:
    """
    Executes tool validation suite.
    """

    def __init__(
        self,
        validator: ToolValidator,
    ) -> None:

        self._validator = validator

    def run(
        self,
        tool: Tool,
        tests: list[ToolTestCase],
    ) -> list[ToolTestResult]:
        """
        Run all tool tests.
        """

        results: list[ToolTestResult] = []

        for test in tests:

            result = self._validator.validate(
                tool,
                test,
            )

            results.append(
                result,
            )

        return results
