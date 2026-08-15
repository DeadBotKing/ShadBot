"""
ShadBot Agent Platform

Runtime Integration Test Runner
"""

from __future__ import annotations

from collections.abc import Callable

from .runtime_test_case import (
    RuntimeTestCase,
)
from .runtime_test_result import (
    RuntimeTestResult,
)
from .runtime_validator import (
    RuntimeValidator,
)


class RuntimeTestRunner:
    """
    Executes runtime integration suites.
    """

    def __init__(
        self,
        validator: RuntimeValidator,
    ) -> None:

        self._validator = validator

    def run(
        self,
        *,
        executor: Callable[
            [dict[str, object]],
            dict[str, object],
        ],
        tests: list[RuntimeTestCase],
        payload: dict[str, object],
    ) -> list[RuntimeTestResult]:
        """
        Run runtime integration tests.
        """

        results: list[RuntimeTestResult] = []

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
