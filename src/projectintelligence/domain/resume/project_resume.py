"""
ShadBot Project Intelligence

Project Resume Aggregate Root
"""

from __future__ import annotations

from dataclasses import dataclass
from uuid import UUID

from projectintelligence.domain.resume.completed_work import CompletedWork
from projectintelligence.domain.resume.pending_work import PendingWork
from projectintelligence.domain.resume.project_recommendation import (
    ProjectRecommendation,
)
from projectintelligence.domain.resume.project_state import ProjectState
from projectintelligence.domain.resume.project_summary import ProjectSummary
from projectintelligence.domain.resume.resume_metadata import ResumeMetadata


@dataclass(frozen=True, slots=True)
class ProjectResume:
    """
    Aggregate root representing the complete resumable state of a project.

    This object contains every piece of information required by downstream
    systems to understand where a project currently stands without scanning
    the workspace again.
    """

    project_id: UUID

    metadata: ResumeMetadata

    state: ProjectState

    summary: ProjectSummary

    completed_work: tuple[CompletedWork, ...]

    pending_work: tuple[PendingWork, ...]

    recommendations: tuple[ProjectRecommendation, ...]
