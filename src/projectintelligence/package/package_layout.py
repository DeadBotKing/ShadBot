"""
ShadBot Project Intelligence

Package Layout
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path


@dataclass(slots=True, frozen=True)
class PackageLayout:
    """
    Represents the directory layout of a Project Intelligence Package.
    """

    root: Path

    @property
    def manifest_file(self) -> Path:
        return self.root / "manifest.json"

    @property
    def metadata_file(self) -> Path:
        return self.root / "metadata.json"

    @property
    def snapshot_file(self) -> Path:
        return self.root / "snapshot.json"

    @property
    def knowledge_file(self) -> Path:
        return self.root / "knowledge.json"

    @property
    def context_file(self) -> Path:
        return self.root / "context.json"

    @property
    def resume_file(self) -> Path:
        return self.root / "resume.json"

    @property
    def evolution_file(self) -> Path:
        return self.root / "evolution.json"

    @property
    def agent_context_file(self) -> Path:
        return self.root / "agent_context.json"

    @property
    def logs_directory(self) -> Path:
        return self.root / "logs"

    def create(self) -> None:
        """
        Create the complete package directory structure.
        """

        self.root.mkdir(
            parents=True,
            exist_ok=True,
        )

        self.logs_directory.mkdir(
            parents=True,
            exist_ok=True,
        )
