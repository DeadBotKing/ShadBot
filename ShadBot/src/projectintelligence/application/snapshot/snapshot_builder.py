"""
ShadBot Project Intelligence

Snapshot Builder
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

from projectintelligence.application.contracts.project.workspace_scanner import (
    IWorkspaceScanner,
)
from projectintelligence.application.contracts.snapshot.snapshot_builder import (
    ISnapshotBuilder,
)
from projectintelligence.application.snapshot.directory_tree_builder import (
    DirectoryTreeBuilder,
)
from projectintelligence.application.snapshot.hash_calculator import (
    HashCalculator,
)
from projectintelligence.domain.project.project_entity import ProjectEntity
from projectintelligence.domain.snapshot.project_snapshot import ProjectSnapshot


@dataclass(slots=True)
class SnapshotBuilder(ISnapshotBuilder):
    """
    Builds a project snapshot from the current workspace.
    """

    workspace_scanner: IWorkspaceScanner
    hash_calculator: HashCalculator
    directory_tree_builder: DirectoryTreeBuilder

    def build(
        self,
        project: ProjectEntity,
    ) -> ProjectSnapshot:
        """
        Build a snapshot for the given project.
        """

        files = self.workspace_scanner.scan(project.workspace)

        directory_count = self._count_directories(project.workspace)

        file_hashes = self.hash_calculator.calculate_many(
            files=files,
            workspace=project.workspace,
        )

        architecture_tree = self.directory_tree_builder.build(
            files=files,
            workspace=project.workspace,
        )

        return ProjectSnapshot(
            project_id=project.project_id,
            workspace=project.workspace,
            file_count=len(files),
            directory_count=directory_count,
            file_hashes=file_hashes,
            architecture_tree=architecture_tree,
        )

    @staticmethod
    def _count_directories(
        workspace: Path,
    ) -> int:
        """
        Count directories in the workspace.
        """

        return sum(1 for path in workspace.rglob("*") if path.is_dir())
