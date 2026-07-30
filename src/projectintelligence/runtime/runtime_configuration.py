"""
ShadBot Project Intelligence

Runtime Configuration
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path


@dataclass(slots=True, frozen=True)
class RuntimeConfiguration:
    """
    Immutable configuration for a single Project Intelligence
    runtime execution.
    """

    workspace: Path

    output_directory: Path | None = None

    project_name: str | None = None

    overwrite_output: bool = False

    fail_fast: bool = True

    def resolve_output_directory(self) -> Path:
        """
        Resolve the effective output directory.
        """

        if self.output_directory is not None:
            return self.output_directory

        return self.workspace / ".project-intelligence"

    @property
    def resolved_project_name(self) -> str:
        """
        Resolve the effective project name.
        """

        if self.project_name is not None:
            return self.project_name

        return self.workspace.name
