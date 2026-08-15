"""
ShadBot Project Intelligence

Workspace Scanner Contract
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from pathlib import Path


class IWorkspaceScanner(ABC):
    """
    Contract responsible for scanning a project workspace.
    """

    @abstractmethod
    def scan(
        self,
        workspace: Path,
    ) -> list[Path]:
        """
        Scan a workspace and return discovered filesystem entries.
        """
        raise NotImplementedError
