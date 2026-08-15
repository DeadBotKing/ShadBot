"""
ShadBot Project Intelligence

Framework Detector Contract
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from pathlib import Path


class IFrameworkDetector(ABC):
    """
    Contract responsible for detecting frameworks
    used within a project.
    """

    @abstractmethod
    def detect(
        self,
        files: list[Path],
    ) -> set[str]:
        """
        Detect frameworks from project files.
        """
        raise NotImplementedError
