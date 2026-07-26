"""
ShadBot Project Intelligence

PyProject Parser
"""

from __future__ import annotations

from pathlib import Path

from projectintelligence.application.contracts.dependency.dependency_parser import (
    IDependencyParser,
)


class PyProjectParser(IDependencyParser):
    """
    Parses pyproject.toml dependency manifests.
    """

    def parse(
        self,
        manifest: Path,
    ) -> dict[str, str]:
        """
        Parse dependencies from a pyproject.toml file.
        """

        return {}
