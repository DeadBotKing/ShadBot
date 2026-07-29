"""
ShadBot Project Intelligence

Agent Context Metadata
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone
from uuid import UUID


@dataclass(frozen=True, slots=True)
class AgentContextMetadata:
    """
    Metadata describing an agent context package.
    """

    context_id: UUID

    version: str

    contract_version: str = "1.0"

    created_at: datetime = field(default_factory=lambda: datetime.now(timezone.utc))
