"""
ShadBot Project Intelligence

Knowledge Rule Contract
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Generic, TypeVar

TInput = TypeVar("TInput")
TOutput = TypeVar("TOutput")


class BaseRule(ABC, Generic[TInput, TOutput]):
    """
    Base contract for all Project Intelligence knowledge rules.
    """

    @abstractmethod
    def applies_to(
        self,
        source: TInput,
    ) -> bool:
        """
        Determine whether this rule can be applied.
        """

    @abstractmethod
    def execute(
        self,
        source: TInput,
    ) -> TOutput:
        """
        Execute the rule.
        """