"""
ShadBot Agent Platform

Validation context provider.
"""

from __future__ import annotations

from typing import Any

from agentplatform.application.validation import (
    ValidationEngine,
)
from agentplatform.domain.validation import (
    ValidationProfile,
    ValidationRequest,
)


class ValidationContextProvider:
    """
    Provides validation context.
    """

    def __init__(
        self,
        validation_engine: ValidationEngine,
        request: ValidationRequest,
        profile: ValidationProfile,
    ) -> None:

        self._validation_engine = validation_engine
        self._request = request
        self._profile = profile

    def provide(
        self,
    ) -> dict[str, Any]:
        """
        Build validation context.
        """

        result = self._validation_engine.validate(
            self._request,
            self._profile,
        )

        return {
            "passed": result.passed,
            "results": result.results,
            "failures": result.failures,
        }
