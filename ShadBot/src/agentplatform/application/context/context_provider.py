"""
ShadBot Agent Platform

Brain context provider contract.
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any


class ContextProvider(ABC):
    """
    Provides cognitive context fragments.
    """

    @abstractmethod
    def provide(
        self,
    ) -> dict[str, Any]:
        raise NotImplementedError
