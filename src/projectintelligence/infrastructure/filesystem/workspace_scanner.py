"""
ShadBot Project Intelligence

Workspace Scanner
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

from projectintelligence.application.contracts.project.workspace_scanner import (
    IWorkspaceScanner,
)
from projectintelligence.infrastructure.filesystem.directory_walker import (
    DirectoryWalker,
)
from projectintelligence.infrastructure.filesystem.file_collector import (
    FileCollector,
)
from projectintelligence.infrastructure.filesystem.ignore_manager import (
    IgnoreManager,
)


@dataclass(slots=True)
class WorkspaceScanner(
    IWorkspaceScanner,
):
    """
    Coordinates filesystem scanning.

    This class orchestrates filesystem components
    without implementing filesystem logic itself.
    """

    directory_walker: DirectoryWalker
    ignore_manager: IgnoreManager
    file_collector: FileCollector

    def scan(
        self,
        workspace: Path,
    ) -> list[Path]:
        """
        Scan a workspace and return collected files.
        """

        paths = (
            path
            for path in self.directory_walker.walk(workspace)
            if not self.ignore_manager.should_ignore(path)
        )

        return self.file_collector.collect(paths)
