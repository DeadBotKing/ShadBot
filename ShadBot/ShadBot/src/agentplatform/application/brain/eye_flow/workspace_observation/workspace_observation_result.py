"""
ShadBot Agent Platform

Workspace Observation Result
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from pathlib import Path


@dataclass(frozen=True, slots=True)
class WorkspaceObservationResult:
    """
    Workspace observation output.
    """

    workspace_path: Path

    files: tuple[Path, ...]

    directories: tuple[Path, ...]

    total_files: int

    total_directories: int

    observed_at: datetime
