"""
ShadBot Agent Platform

Self improvement contract.
"""

from __future__ import annotations

from abc import ABC, abstractmethod

from agentplatform.domain.improvement import (
    ImprovementRequest,
    ImprovementResult,
)


class SelfImprovementContract(ABC):
    """
    Contract for self improvement systems.

    Defines the boundary between:
    - Brain
    - Learning Loop
    - Improvement Engine
    - Future Agent Evolution

    Implementations decide HOW improvement happens.
    """

    @abstractmethod
    def analyze(
        self,
        request: ImprovementRequest,
    ) -> ImprovementResult:
        """
        Analyze improvement opportunity.
        """
        raise NotImplementedError

    @abstractmethod
    def validate(
        self,
        result: ImprovementResult,
    ) -> bool:
        """
        Validate improvement result.
        """
        raise NotImplementedError

    @abstractmethod
    def apply(
        self,
        result: ImprovementResult,
    ) -> bool:
        """
        Apply approved improvement.

        Implementation controls actual execution.
        """
        raise NotImplementedError
