"""
ShadBot Agent Platform

Brain Runtime Instance component for 7.2 Brain Runtime.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone
from uuid import UUID, uuid4


@dataclass(frozen=True, slots=True)
class BrainRuntimeState:
    runtime_id: UUID
    status: str  # IDLE, REASONING, PLANNING, COMPLETED, FAILED
    last_synchronized: str


@dataclass(frozen=True, slots=True)
class BrainRuntimeInstance:
    runtime_id: UUID
    state: BrainRuntimeState
