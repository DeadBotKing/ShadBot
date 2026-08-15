"""
ShadBot Agent Platform

Execution Validator
"""

from __future__ import annotations

import time

from agentplatform.domain.tools import (
    ToolContract,
)

from .execution_test_case import (
    ExecutionTestCase,
)
from .execution_test_result import (
    ExecutionTestResult,
)


class ExecutionValidator:
    """
    Validates execution pipeline.
    """

    def validate(
        self,
        *,
        executor: ToolContract,
        test_case: ExecutionTestCase,
        payload: dict[str, object],
    ) -> ExecutionTestResult:
        """
        Execute validation scenario.
        """

        start = time.perf_counter()

        try:

            result = executor.execute(
                payload,
            )

            elapsed = (time.perf_counter() - start) * 1000

            success = result is not None

            return ExecutionTestResult(
                capability_id=test_case.capability_id,
                tool_id=test_case.tool_id,
                test_name=test_case.test_name,
                passed=success == test_case.expected_success,
                message=(
                    "Execution completed successfully"
                    if success
                    else "Execution returned empty result"
                ),
                execution_time_ms=elapsed,
            )

        except Exception as exc:

            elapsed = (time.perf_counter() - start) * 1000

            return ExecutionTestResult(
                capability_id=test_case.capability_id,
                tool_id=test_case.tool_id,
                test_name=test_case.test_name,
                passed=False,
                message=str(exc),
                execution_time_ms=elapsed,
            )
