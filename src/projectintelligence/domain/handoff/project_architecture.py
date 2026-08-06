"""
ShadBot Project Intelligence

Project architecture context.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class ProjectArchitecture:
    """
    Architectural understanding of project.
    """

    architecture_style: str

    modules: tuple[str, ...]

    frameworks: tuple[str, ...]

    languages: tuple[str, ...]

    conventions: tuple[str, ...]

    def to_dict(
        self,
    ) -> dict[str, object]:

        return {
            "architecture_style": self.architecture_style,
            "modules": list(self.modules),
            "frameworks": list(self.frameworks),
            "languages": list(self.languages),
            "conventions": list(self.conventions),
        }
