"""
ShadBot Project Intelligence

Dependency Analyzer
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

from projectintelligence.application.contracts.analysis.dependency_analyzer import (
    IDependencyAnalyzer,
)
from projectintelligence.application.dependency.parser_selector import (
    ParserSelector,
)


@dataclass(slots=True)
class DependencyAnalyzer(IDependencyAnalyzer):
    """
    Analyzes project dependency manifests.
    """

    parser_selector: ParserSelector

    def analyze(
        self,
        files: list[Path],
    ) -> dict[str, str]:
        """
        Analyze project dependencies.
        """

        dependencies: dict[str, str] = {}

        for manifest, parser in self.parser_selector.select(files):
            dependencies.update(parser.parse(manifest))

        return dependencies
