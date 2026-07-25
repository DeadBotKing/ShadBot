"""
ShadBot Project Intelligence

Project Scanner Application Service
"""

from __future__ import annotations

from pathlib import Path

from projectintelligence.domain.project.project_entity import (
    ProjectEntity,
)

from projectintelligence.domain.snapshot.project_snapshot import (
    ProjectSnapshot,
)


class ProjectScannerService:
    """
    Application service responsible for scanning projects.
    """

    def scan(
        self,
        project: ProjectEntity,
    ) -> ProjectSnapshot:
        """
        Scan project workspace and create snapshot.
        """

        files = 0
        directories = 0

        workspace: Path = project.workspace

        for path in workspace.rglob("*"):
            if path.is_file():
                files += 1

            elif path.is_dir():
                directories += 1

        return ProjectSnapshot(
            project_id=project.project_id,
            workspace=workspace,
            file_count=files,
            directory_count=directories,
        )