"""
ShadBot Agent Platform

Architecture planner service.
"""

from __future__ import annotations

from agentplatform.domain.architecture import (
    ArchitectureDirectory,
    ArchitectureFile,
    ArchitecturePlan,
)


class ArchitecturePlanner:
    """
    Converts architect output into executable architecture plan.
    """

    def create_plan(
        self,
        project_name: str,
        response: str,
    ) -> ArchitecturePlan:
        """
        Build architecture plan from architect response.
        """

        directories: list[ArchitectureDirectory] = []
        files: list[ArchitectureFile] = []

        section = None

        for line in response.splitlines():
            line = line.strip()

            if not line:
                continue

            if line.startswith("DIRECTORIES:"):
                section = "directories"
                continue

            if line.startswith("FILES:"):
                section = "files"
                continue

            if not line.startswith("-"):
                continue

            value = line.removeprefix("-").strip()

            if section == "directories":
                directories.append(
                    ArchitectureDirectory(
                        path=value,
                    ),
                )

            elif section == "files":
                files.append(
                    ArchitectureFile(
                        path=value,
                        content="",
                    ),
                )

        return ArchitecturePlan(
            project_name=project_name,
            directories=tuple(directories),
            files=tuple(files),
        )
