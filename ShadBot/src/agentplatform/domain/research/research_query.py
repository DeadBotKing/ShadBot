"""
ShadBot Agent Platform

Research Query Model.
"""

from __future__ import annotations

from dataclasses import dataclass
from uuid import UUID


@dataclass(frozen=True, slots=True)
class ResearchQuery:
    """
    Defines research request.
    """

    task_id: UUID

    subject: str

    context: str

    constraints: tuple[str, ...] = ()
