"""
ShadBot Project Intelligence

Framework Registry
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class FrameworkSignature:
    """
    Represents a framework detection signature.
    """

    framework: str

    required_files: tuple[str, ...] = ()

    required_imports: tuple[str, ...] = ()

    required_dependencies: tuple[str, ...] = ()


class FrameworkRegistry:
    """
    Registry of known framework signatures.
    """

    def signatures(
        self,
    ) -> list[FrameworkSignature]:
        """
        Return all supported framework signatures.
        """

        return [
            FrameworkSignature(
                framework="Django",
                required_files=("manage.py",),
            ),
            FrameworkSignature(
                framework="FastAPI",
                required_dependencies=("fastapi",),
            ),
            FrameworkSignature(
                framework="Flask",
                required_dependencies=("flask",),
            ),
            FrameworkSignature(
                framework="React",
                required_files=("package.json",),
                required_dependencies=("react",),
            ),
            FrameworkSignature(
                framework="Next.js",
                required_dependencies=("next",),
            ),
            FrameworkSignature(
                framework="Vue",
                required_dependencies=("vue",),
            ),
            FrameworkSignature(
                framework="Angular",
                required_files=("angular.json",),
            ),
            FrameworkSignature(
                framework="NestJS",
                required_dependencies=("@nestjs/core",),
            ),
            FrameworkSignature(
                framework="ASP.NET Core",
                required_files=("*.csproj",),
            ),
            FrameworkSignature(
                framework="Spring Boot",
                required_files=(
                    "pom.xml",
                    "build.gradle",
                ),
            ),
            FrameworkSignature(
                framework="Cargo",
                required_files=("Cargo.toml",),
            ),
            FrameworkSignature(
                framework="Gin",
                required_dependencies=("github.com/gin-gonic/gin",),
            ),
        ]
