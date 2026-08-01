"""
ShadBot Project Intelligence

PyProject Parser
"""

from __future__ import annotations

import tomllib
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
        Parse dependencies from pyproject.toml.
        """

        dependencies: dict[str, str] = {}

        if not manifest.exists():
            return dependencies

        with manifest.open(
            "rb",
        ) as file:
            data = tomllib.load(file)

        project = data.get(
            "project",
            {},
        )

        for dependency in project.get(
            "dependencies",
            [],
        ):
            name, version = self._parse_dependency(
                dependency,
            )

            dependencies[name] = version

        optional = project.get(
            "optional-dependencies",
            {},
        )

        for group in optional.values():
            for dependency in group:
                name, version = self._parse_dependency(
                    dependency,
                )

                dependencies[name] = version

        poetry = (
            data.get(
                "tool",
                {},
            )
            .get(
                "poetry",
                {},
            )
            .get(
                "dependencies",
                {},
            )
        )

        for name, version in poetry.items():
            if name.lower() == "python":
                continue

            dependencies[name] = str(
                version,
            )

        return dependencies

    @staticmethod
    def _parse_dependency(
        value: str,
    ) -> tuple[str, str]:
        """
        Normalize dependency string.
        """

        for operator in (
            "==",
            ">=",
            "<=",
            "~=",
            ">",
            "<",
        ):
            if operator in value:
                name, version = value.split(
                    operator,
                    maxsplit=1,
                )

                return (
                    name.strip(),
                    operator + version.strip(),
                )

        return (
            value.strip(),
            "",
        )
