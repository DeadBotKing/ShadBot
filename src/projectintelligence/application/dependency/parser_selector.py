"""
ShadBot Project Intelligence

Dependency Parser Selector
"""

from __future__ import annotations

from pathlib import Path

from projectintelligence.application.contracts.dependency.dependency_parser import (
    IDependencyParser,
)
from projectintelligence.application.dependency.parser_registry import (
    ParserRegistration,
    ParserRegistry,
)


class ParserSelector:
    """
    Selects dependency parsers for project manifest files.
    """

    def __init__(
        self,
        parser_registry: ParserRegistry,
    ) -> None:
        self._parser_registry = parser_registry

    def select(
        self,
        files: list[Path],
    ) -> list[tuple[Path, IDependencyParser]]:
        """
        Select matching parsers for project files.
        """

        selected: list[tuple[Path, IDependencyParser]] = []

        registrations = self._parser_registry.registrations()

        for file in files:
            for registration in registrations:
                if self._matches(
                    file=file,
                    registration=registration,
                ):
                    selected.append(
                        (
                            file,
                            registration.parser,
                        )
                    )

        return selected

    @staticmethod
    def _matches(
        file: Path,
        registration: ParserRegistration,
    ) -> bool:
        """
        Determine whether a parser matches a file.
        """

        filename = registration.filename

        if filename.startswith("*."):
            return file.suffix == filename[1:]

        return file.name == filename
