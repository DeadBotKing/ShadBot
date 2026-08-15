"""
ShadBot Agent Platform

Reflection strategy contract.
"""

from __future__ import annotations

from abc import ABC, abstractmethod

from agentplatform.domain.cognition import (
    ReflectionRequest,
    ReflectionResult,
)


class ReflectionStrategy(ABC):
    """
    Base contract for reflection strategies.
    """

    @abstractmethod
    def reflect(
        self,
        request: ReflectionRequest,
    ) -> ReflectionResult:
        raise NotImplementedError
