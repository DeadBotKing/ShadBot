"""
ShadBot Project Intelligence

Cargo Parser
"""

from __future__ import annotations

from pathlib import Path

from projectintelligence.application.contracts.dependency.dependency_parser import (
    IDependencyParser,
)


class CargoParser(IDependencyParser):
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
