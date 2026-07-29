"""
ShadBot Project Intelligence

Persistence Batch Result
"""

from __future__ import annotations

from dataclasses import dataclass

from projectintelligence.application.models.results.persistence_result import (
    PersistenceResult,
)


@dataclass(slots=True, frozen=True)
class PersistenceBatchResult:
    """
    Represents the result of persisting multiple intelligence artifacts.
    """

    results: tuple[PersistenceResult, ...]

    @property
    def success(self) -> bool:
        """
        Returns True when all persistence operations succeeded.
        """

        return all(
            result.success
            for result in self.results
        )