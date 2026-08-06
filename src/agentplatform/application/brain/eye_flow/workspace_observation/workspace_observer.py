"""
ShadBot Agent Platform

Workspace Observer
"""

from __future__ import annotations

from datetime import datetime, timezone
from pathlib import Path

from .workspace_observation_request import (
    WorkspaceObservationRequest,
)
from .workspace_observation_result import (
    WorkspaceObservationResult,
)


class WorkspaceObserver:
    """
    Observes project workspace state.

    Responsible for:
    - filesystem discovery
    - project visibility
    - workspace state extraction

    Does not analyze code.
    Does not modify files.
    """

    def observe(
        self,
        request: WorkspaceObservationRequest,
    ) -> WorkspaceObservationResult:
        """
        Observe workspace.
        """

        files: list[Path] = []

        directories: list[Path] = []

        if request.recursive:

            for path in request.workspace_path.rglob("*"):

                if path.is_file():

                    files.append(path)

                elif path.is_dir():

                    directories.append(path)

        else:

            for path in request.workspace_path.iterdir():

                if path.is_file():

                    files.append(path)

                elif path.is_dir():

                    directories.append(path)

        return WorkspaceObservationResult(
            workspace_path=request.workspace_path,
            files=tuple(files),
            directories=tuple(directories),
            total_files=len(files),
            total_directories=len(directories),
            observed_at=datetime.now(
                timezone.utc,
            ),
        )
