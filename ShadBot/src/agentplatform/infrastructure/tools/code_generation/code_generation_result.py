"""
ShadBot Agent Platform

Code Generation Result
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone
from uuid import UUID, uuid4


@dataclass(frozen=True, slots=True)
class CodeGenerationResult:
    """
    Result produced by code generation tools.
    """

    success: bool

    message: str

    generated_files: tuple[str, ...] = ()

    patches: tuple[str, ...] = ()

    result_id: UUID = field(
        default_factory=uuid4,
    )

    created_at: datetime = field(
        default_factory=lambda: datetime.now(
            timezone.utc,
        ),
    )
