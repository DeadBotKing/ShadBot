"""
ShadBot Agent Platform

Project State Reading Request
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from uuid import UUID


@dataclass(frozen=True, slots=True)
class ProjectStateRequest:
    """
    Request to construct a semantic project state.

    The request carries the project identity and the workspace
    location that should be observed.
    """

    project_id: UUID
    project_name: str
    project_path: Path
    project_type: str
    project_version: str

    workspace_path: Path
    recursive: bool = True