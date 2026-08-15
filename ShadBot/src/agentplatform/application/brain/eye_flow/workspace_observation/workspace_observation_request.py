"""
ShadBot Agent Platform

Workspace Observation Request
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from uuid import UUID


@dataclass(frozen=True, slots=True)
class WorkspaceObservationRequest:
    """
    Request for observing project workspace.
    """

    project_id: UUID

    workspace_path: Path

    recursive: bool = True
