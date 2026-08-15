"""
ShadBot Agent Platform

Tool Validator
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


class ToolValidator:
    """
    Validates agent tools.
    """

    def validate(
        self,
        tool: Tool,
        test_case: ToolTestCase,
    ) -> ToolTestResult:
        """
        Validate tool state.
        """

        if tool is None:

            return ToolTestResult(
                tool_id=test_case.tool_id,
                test_name=test_case.test_name,
                passed=False,
                message="Tool does not exist",
            )

        if not tool.enabled:

            return ToolTestResult(
                tool_id=test_case.tool_id,
                test_name=test_case.test_name,
                passed=False,
                message="Tool is disabled",
            )

        if not tool.can_execute():

            return ToolTestResult(
                tool_id=test_case.tool_id,
                test_name=test_case.test_name,
                passed=False,
                message="Tool cannot execute",
            )

        return ToolTestResult(
            tool_id=test_case.tool_id,
            test_name=test_case.test_name,
            passed=True,
            message="Tool validation passed",
        )
