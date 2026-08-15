"""
ShadBot Project Intelligence

Project Scanner Contract
"""

from __future__ import annotations

from abc import ABC, abstractmethod

from projectintelligence.domain.project.project_entity import (
    ProjectEntity,
)
from projectintelligence.domain.snapshot.project_snapshot import (
    ProjectSnapshot,
)


class IProjectScanner(ABC):
    """
    Contract for all project scanners.
    """

    @abstractmethod
    def scan(
        self,
        project: ProjectEntity,
    ) -> ProjectSnapshot:
        """
        Scan a project workspace and build a snapshot.
        """
        raise NotImplementedError
