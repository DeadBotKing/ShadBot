"""
ShadBot Project Intelligence

Dependency Parser Contract
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from pathlib import Path


class IDependencyParser(ABC):
    """
    Contract for dependency manifest parsers.
    """

    @abstractmethod
    def parse(
        self,
        manifest: Path,
    ) -> dict[str, str]:
        """
        Parse dependencies from a manifest file.
        """
        raise NotImplementedError
