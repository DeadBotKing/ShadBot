"""
ShadBot Project Intelligence

Agent Context Metadata
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from uuid import UUID


@dataclass(frozen=True, slots=True)
class AgentContextMetadata:
    """
    Metadata describing an agent context package.
    """

    context_id: UUID

    version: str

    created_at: datetime