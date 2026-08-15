"""
ShadBot Project Intelligence

Requirements Parser
"""

from __future__ import annotations

from pathlib import Path

from projectintelligence.application.contracts.dependency.dependency_parser import (
    IDependencyParser,
)


class RequirementsParser(IDependencyParser):
    """
    Parses Python requirements.txt files.
    """

    def parse(
        self,
        requirements_file: Path,
    ) -> dict[str, str]:
        """
        Parse dependencies from a requirements.txt file.
        """

        dependencies: dict[str, str] = {}

        if not requirements_file.exists():
            return dependencies

        for line in requirements_file.read_text(
            encoding="utf-8",
        ).splitlines():

            line = line.strip()

            if not line or line.startswith("#"):
                continue

            if "==" in line:
                package, version = line.split(
                    "==",
                    maxsplit=1,
                )

                dependencies[package.strip()] = version.strip()

                continue

            dependencies[line] = ""

        return dependencies
