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
    Dependency parser registration metadata.
    """

    filename_pattern: str

    ecosystem: str

    parser: IDependencyParser


class ParserRegistry:
    """
    Central dependency parser registry.

    Defines supported dependency ecosystems.
    """

    def registrations(
        self,
    ) -> tuple[ParserRegistration, ...]:
        """
        Return all supported dependency parsers.
        """

        return (
            ParserRegistration(
                filename_pattern="requirements.txt",
                ecosystem="python",
                parser=RequirementsParser(),
            ),
            ParserRegistration(
                filename_pattern="pyproject.toml",
                ecosystem="python",
                parser=PyProjectParser(),
            ),
            ParserRegistration(
                filename_pattern="package.json",
                ecosystem="javascript",
                parser=PackageJsonParser(),
            ),
            ParserRegistration(
                filename_pattern="Cargo.toml",
                ecosystem="rust",
                parser=CargoParser(),
            ),
            ParserRegistration(
                filename_pattern="pom.xml",
                ecosystem="java",
                parser=PomParser(),
            ),
            ParserRegistration(
                filename_pattern=".csproj",
                ecosystem="dotnet",
                parser=CsprojParser(),
            ),
        )
