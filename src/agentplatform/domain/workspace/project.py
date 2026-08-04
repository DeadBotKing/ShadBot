"""
ShadBot Agent Platform

Workspace project model.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True, slots=True)
class Project:
    """
    Represents a project inside a workspace.
    """

    name: str

    path: Path

    project_type: str
