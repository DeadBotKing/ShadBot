"""
ShadBot Project Intelligence

Resume Storage Service
"""

from __future__ import annotations

from dataclasses import dataclass

from projectintelligence.application.models.results.persistence_result import (
    PersistenceResult,
)
from projectintelligence.application.ports.outbound.resume_repository import (
    ResumeRepository,
)
from projectintelligence.domain.resume.project_resume import (
    ProjectResume,
)


@dataclass(slots=True)
class ResumeStorageService:
    """
    Coordinates persistence of project resumes.
    """

    repository: ResumeRepository

    def save(
        self,
        resume: ProjectResume,
    ) -> PersistenceResult:
        self.repository.save(
            resume,
        )

        return PersistenceResult.succeeded(
            operation="save",
            entity="ProjectResume",
            identifier=str(resume.metadata.resume_id),
            message="Project resume stored successfully.",
        )