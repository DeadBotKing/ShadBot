"""
ShadBot Project Intelligence

Test Analyzer Contract
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from pathlib import Path

from projectintelligence.domain.testing.testing_context import (
    TestingContext,
)


class ITestAnalyzer(ABC):
    """
    Contract for analyzing project testing intelligence.
    """

    @abstractmethod
    def analyze(
        self,
        workspace: Path,
    ) -> TestingContext:
        """
        Analyze project testing information.
        """
        raise NotImplementedError
