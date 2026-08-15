"""
ShadBot Agent Platform

Runtime Integration Validator
"""

from __future__ import annotations

import time
from collections.abc import Callable

from .runtime_test_case import (
    RuntimeTestCase,
)
from .runtime_test_result import (
    RuntimeTestResult,
)


class RuntimeValidator:
    """
    Validates complete agent runtime flow.
    """

    def validate(
        self,
        *,
        executor: Callable[
            [dict[str, object]],
            dict[str, object],
        ],
        test_case: RuntimeTestCase,
        payload: dict[str, object],
    ) -> RuntimeTestResult:
        """
        Execute complete runtime validation.
        """

        start = time.perf_counter()

        try:

            result = executor(
                payload,
            )

            elapsed = (time.perf_counter() - start) * 1000

            success = result is not None and bool(result)

            return RuntimeTestResult(
                agent_id=test_case.agent_id,
                capability_id=test_case.capability_id,
                tool_id=test_case.tool_id,
                test_name=test_case.test_name,
                passed=(success == test_case.expected_success),
                message=(
                    "Runtime execution pipeline passed"
                    if success
                    else "Runtime execution pipeline failed"
                ),
                execution_time_ms=elapsed,
            )

        except Exception as exc:

            elapsed = (time.perf_counter() - start) * 1000

            return RuntimeTestResult(
                agent_id=test_case.agent_id,
                capability_id=test_case.capability_id,
                tool_id=test_case.tool_id,
                test_name=test_case.test_name,
                passed=False,
                message=str(exc),
                execution_time_ms=elapsed,
            )
