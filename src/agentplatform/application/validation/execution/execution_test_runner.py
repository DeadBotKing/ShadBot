"""
ShadBot Agent Platform

Execution Test Runner
"""

from __future__ import annotations

from agentplatform.domain.tools import (
    ToolContract,
)

from .execution_test_case import (
    ExecutionTestCase,
)
from .execution_test_result import (
    ExecutionTestResult,
)
from .execution_validator import (
    ExecutionValidator,
)


class ExecutionTestRunner:
    """
    Runs execution validation suite.
    """

    def __init__(
        self,
        validator: ExecutionValidator,
    ) -> None:

        self._validator = validator

    def run(
        self,
        *,
        executor: ToolContract,
        tests: list[ExecutionTestCase],
        payload: dict[str, object],
    ) -> list[ExecutionTestResult]:
        """
        Execute all execution tests.
        """

        results: list[ExecutionTestResult] = []

        for test in tests:

            result = self._validator.validate(
                executor=executor,
                test_case=test,
                payload=payload,
            )

            results.append(
                result,
            )

        return results
