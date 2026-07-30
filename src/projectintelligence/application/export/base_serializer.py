"""
ShadBot Project Intelligence

Base Serializer Contract
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any


class BaseSerializer(ABC):
    """
    Base contract for converting intelligence artifacts
    into JSON serializable structures.
    """

    @abstractmethod
    def serialize(
        self,
        value: Any,
    ) -> dict[str, Any]:
        """
        Convert domain object into JSON-safe dictionary.
        """
        raise NotImplementedError
