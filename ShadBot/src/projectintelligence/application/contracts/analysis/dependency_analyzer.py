"""
ShadBot Project Intelligence

Dependency Analyzer Contract
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from pathlib import Path


class IDependencyAnalyzer(ABC):
    """
    Contract responsible for analyzing project dependencies.
    """

    @abstractmethod
    def analyze(
        self,
        workspace: Path,
    ) -> dict[str, str]:
        """
        Analyze project dependencies.

        Returns:
            Mapping of dependency name to detected version.
        """
        raise NotImplementedError
