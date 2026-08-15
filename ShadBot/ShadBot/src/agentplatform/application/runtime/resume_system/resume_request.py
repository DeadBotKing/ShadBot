"""
ShadBot Agent Platform

Resume Request model for 7.6 Resume System.
"""

from __future__ import annotations

from dataclasses import dataclass
from uuid import UUID


@dataclass(frozen=True, slots=True)
class ResumeRequest:
    project_id: UUID
    target_session_id: UUID | None = None
