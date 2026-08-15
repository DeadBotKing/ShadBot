"""
ShadBot Agent Platform

Architecture executor.

Executes architecture plans by creating
directories and files.
"""

from __future__ import annotations

from pathlib import Path

from agentplatform.domain.architecture import (
    ArchitecturePlan,
)


class ArchitectureExecutor:
    """
    Executes architecture plans on filesystem.
    """

    def execute(
        self,
        plan: ArchitecturePlan,
        root_path: Path,
    ) -> None:
        """
        Create project structure from architecture plan.
        """

        for directory in plan.directories:
            path = root_path / directory.path

            path.mkdir(
                parents=True,
                exist_ok=True,
            )

        for file in plan.files:
            path = root_path / file.path

            path.parent.mkdir(
                parents=True,
                exist_ok=True,
            )

            path.write_text(
                file.content,
                encoding="utf-8",
            )
