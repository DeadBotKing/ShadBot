"""
ShadBot Project Intelligence

Snapshot Builder Contract
"""

from __future__ import annotations

from abc import ABC, abstractmethod

from projectintelligence.domain.project.project_entity import ProjectEntity
from projectintelligence.domain.snapshot.project_snapshot import ProjectSnapshot


class ISnapshotBuilder(ABC):
    """
    Contract for building project snapshots.
    """

    @abstractmethod
    def build(
        self,
        project: ProjectEntity,
    ) -> ProjectSnapshot:
        """
        Build a project snapshot.
        """
        raise NotImplementedError
