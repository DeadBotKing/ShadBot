"""
ShadBot Project Intelligence

Resume Metadata
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from uuid import UUID


@dataclass(frozen=True, slots=True)
class ResumeMetadata:
    """
    Metadata describing a generated project resume.

    This object identifies the resume itself and records when
    it was produced and from which snapshot it originated.
    """

    resume_id: UUID

    snapshot_id: UUID

    generated_at: datetime

    generator_version: str
