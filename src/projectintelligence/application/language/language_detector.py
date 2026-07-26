"""
ShadBot Project Intelligence

Language Detector
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

from projectintelligence.application.contracts.analysis.language_detector import (
    ILanguageDetector,
)
from projectintelligence.application.language.extension_registry import (
    ExtensionRegistry,
)
from projectintelligence.application.language.language_statistics import (
    LanguageStatistics,
)


@dataclass(slots=True)
class LanguageDetector(ILanguageDetector):
    """
    Detects programming languages used in a project.
    """

    extension_registry: ExtensionRegistry
    language_statistics: LanguageStatistics

    def detect(
        self,
        files: list[Path],
    ) -> list[str]:
        """
        Detect project languages.
        """

        detected = [self.extension_registry.detect(file_path) for file_path in files]

        statistics = self.language_statistics.collect(detected)

        return self.language_statistics.unique_languages(statistics)
