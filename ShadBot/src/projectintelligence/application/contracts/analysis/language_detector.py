"""
ShadBot Project Intelligence

Language Detector Contract
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from pathlib import Path


class ILanguageDetector(ABC):
    """
    Contract responsible for detecting programming languages
    used within a project.
    """

    @abstractmethod
    def detect(
        self,
        files: list[Path],
    ) -> set[str]:
        """
        Detect programming languages from project files.
        """
        raise NotImplementedError
