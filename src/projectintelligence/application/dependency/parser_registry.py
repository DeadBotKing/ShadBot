"""
ShadBot Project Intelligence

Dependency Parser Registry
"""

from __future__ import annotations

from dataclasses import dataclass

from projectintelligence.application.contracts.dependency.dependency_parser import (
    IDependencyParser,
)
from projectintelligence.application.dependency.parsers.cargo_parser import (
    CargoParser,
)
from projectintelligence.application.dependency.parsers.csproj_parser import (
    CsprojParser,
)
from projectintelligence.application.dependency.parsers.package_json_parser import (
    PackageJsonParser,
)
from projectintelligence.application.dependency.parsers.pom_parser import (
    PomParser,
)
from projectintelligence.application.dependency.parsers.pyproject_parser import (
    PyProjectParser,
)
from projectintelligence.application.dependency.parsers.requirements_parser import (
    RequirementsParser,
)


@dataclass(frozen=True, slots=True)
class ParserRegistration:
    """
    Associates a dependency manifest filename with its parser.
    """

    filename: str

    parser: IDependencyParser


class ParserRegistry:
    """
    Registry of dependency parsers.
    """

    def registrations(
        self,
    ) -> list[ParserRegistration]:
        """
        Return registered dependency parsers.
        """

        return [
            ParserRegistration(
                filename="requirements.txt",
                parser=RequirementsParser(),
            ),
            ParserRegistration(
                filename="pyproject.toml",
                parser=PyProjectParser(),
            ),
            ParserRegistration(
                filename="package.json",
                parser=PackageJsonParser(),
            ),
            ParserRegistration(
                filename="Cargo.toml",
                parser=CargoParser(),
            ),
            ParserRegistration(
                filename="pom.xml",
                parser=PomParser(),
            ),
            ParserRegistration(
                filename="*.csproj",
                parser=CsprojParser(),
            ),
        ]
