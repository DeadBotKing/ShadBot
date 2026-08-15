"""
ShadBot Agent Platform

Memory storage abstraction.
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from pathlib import Path


class MemoryStorage(ABC):
    """
    Persistent memory storage contract.
    """

    @abstractmethod
    def read(
        self,
        path: Path,
    ) -> list[dict[str, object]]:
        """
        Read memory records.
        """

        raise NotImplementedError

    @abstractmethod
    def write(
        self,
        path: Path,
        data: list[dict[str, object]],
    ) -> None:
        """
        Write memory records.
        """

        raise NotImplementedError
