"""
ShadBot Agent Platform

Capability Test Runner
"""

from __future__ import annotations

from agentplatform.domain.capabilities import (
    Capability,
)

from .capability_test_case import (
    CapabilityTestCase,
)
from .capability_test_result import (
    CapabilityTestResult,
)
from .capability_validator import (
    CapabilityValidator,
)


class CapabilityTestRunner:
    """
    Runs capability validation suites.
    """

    def __init__(
        self,
        validator: CapabilityValidator,
    ) -> None:

        self._validator = validator

    def run(
        self,
        capability: Capability,
        tests: list[CapabilityTestCase],
    ) -> list[CapabilityTestResult]:
        """
        Execute capability tests.
        """

        results: list[CapabilityTestResult] = []

        for test in tests:

            result = self._validator.validate(
                capability,
                test,
            )

            results.append(
                result,
            )

        return results
