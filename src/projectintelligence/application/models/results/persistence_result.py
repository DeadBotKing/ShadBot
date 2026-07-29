"""
ShadBot Project Intelligence

Persistence Result
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone


@dataclass(slots=True, frozen=True)
class PersistenceResult:
    """
    Represents the result of a persistence operation.
    """

    success: bool

    operation: str

    entity: str

    identifier: str | None = None

    message: str = ""

    created_at: datetime = field(default_factory=datetime.now(timezone.utc))

    @classmethod
    def succeeded(
        cls,
        operation: str,
        entity: str,
        identifier: str | None = None,
        message: str = "",
    ) -> "PersistenceResult":
        return cls(
            success=True,
            operation=operation,
            entity=entity,
            identifier=identifier,
            message=message,
        )

    @classmethod
    def failed(
        cls,
        operation: str,
        entity: str,
        message: str,
        identifier: str | None = None,
    ) -> "PersistenceResult":
        return cls(
            success=False,
            operation=operation,
            entity=entity,
            identifier=identifier,
            message=message,
        )
