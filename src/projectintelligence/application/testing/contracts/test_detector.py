"""
ShadBot Project Intelligence

Test Detector Contract
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from pathlib import Path

from projectintelligence.domain.testing.models.test_framework import (
    TestFramework,
)


class ITestDetector(ABC):
    """
    Contract for detecting project testing frameworks.
    """

    @abstractmethod
    def detect(
        self,
        workspace: Path,
    ) -> list[TestFramework]:
        """
        Detect available testing frameworks.
        """
        raise NotImplementedError
