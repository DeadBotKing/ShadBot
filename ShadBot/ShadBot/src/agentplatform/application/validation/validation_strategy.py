"""
ShadBot Agent Platform

Validation strategy contract.
"""

from __future__ import annotations

from abc import ABC, abstractmethod

from agentplatform.domain.validation import (
    ValidationRequest,
)

from .validation_result import ValidationResult


class ValidationStrategy(ABC):
    """
    Base validation strategy.
    """

    @abstractmethod
    def validate(
        self,
        request: ValidationRequest,
    ) -> ValidationResult:
        raise NotImplementedError
