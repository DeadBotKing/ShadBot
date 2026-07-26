"""
ShadBot Project Intelligence

Snapshot Builder Implementation
"""

from __future__ import annotations

import hashlib
from pathlib import Path

from projectintelligence.application.contracts.snapshot.snapshot_builder import (
    ISnapshotBuilder,
)
from projectintelligence.domain.project.project_entity import (
    ProjectEntity,
)
from projectintelligence.domain.snapshot.project_snapshot import (
    ProjectSnapshot,
)


class SnapshotBuilder(ISnapshotBuilder):
    """
    Builds a ProjectSnapshot from a project workspace.

    This implementation is responsible only for
    filesystem-level snapshot creation.
    """

    def build(
        self,
        project: ProjectEntity,
    ) -> ProjectSnapshot:
        """
        Build a snapshot from project workspace.
        """

        files = [
            path
            for path in project.workspace.rglob("*")
            if path.is_file()
        ]

        directories = [
            path
            for path in project.workspace.rglob("*")
            if path.is_dir()
        ]

        file_hashes = {
            str(file): self._calculate_hash(file)
            for file in files
        }

        return ProjectSnapshot(
            project_id=project.project_id,
            workspace=project.workspace,
            file_count=len(files),
            directory_count=len(directories),
            file_hashes=file_hashes,
        )

    def _calculate_hash(
        self,
        file: Path,
    ) -> str:
        """
        Calculate SHA256 hash for a file.
        """

        sha256 = hashlib.sha256()

        with file.open("rb") as stream:
            while chunk := stream.read(8192):
                sha256.update(chunk)

        return sha256.hexdigest()