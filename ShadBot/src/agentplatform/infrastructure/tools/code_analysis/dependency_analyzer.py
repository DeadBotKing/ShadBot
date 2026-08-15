"""
ShadBot Agent Platform

Dependency Analyzer
"""

from .import_analyzer import (
    ImportAnalyzer,
)


class DependencyAnalyzer:
    """
    Analyzes source dependencies.
    """

    def __init__(self):

        self._imports = ImportAnalyzer()

    def analyze(
        self,
        source: str,
    ) -> dict[str, object]:

        imports = self._imports.analyze(
            source,
        )

        return {
            "dependencies": imports,
            "count": len(imports),
        }
