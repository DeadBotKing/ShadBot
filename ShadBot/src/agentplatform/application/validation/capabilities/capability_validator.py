"""
ShadBot Agent Platform

Capability Validator
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


class CapabilityValidator:
    """
    Validates agent capabilities.
    """

    def validate(
        self,
        capability: Capability,
        test_case: CapabilityTestCase,
    ) -> CapabilityTestResult:
        """
        Execute capability validation.
        """

        if capability is None:
            return CapabilityTestResult(
                capability_id=test_case.capability_id,
                test_name=test_case.test_name,
                passed=False,
                message="Capability does not exist",
            )

        if not capability.enabled:
            return CapabilityTestResult(
                capability_id=test_case.capability_id,
                test_name=test_case.test_name,
                passed=False,
                message="Capability disabled",
            )

        return CapabilityTestResult(
            capability_id=test_case.capability_id,
            test_name=test_case.test_name,
            passed=True,
            message="Capability validation passed",
        )
