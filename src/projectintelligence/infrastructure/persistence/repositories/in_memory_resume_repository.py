"""
ShadBot Project Intelligence

In Memory Resume Repository
"""

from __future__ import annotations

from uuid import UUID

from projectintelligence.application.ports.outbound.resume_repository import (
    ResumeRepository,
)

from projectintelligence.domain.resume.project_resume import (
    ProjectResume,
)


class InMemoryResumeRepository(
    ResumeRepository,
):
    """
    In-memory implementation of project resume persistence.
    """

    def __init__(self) -> None:
        self._storage: dict[
            UUID,
            ProjectResume,
        ] = {}

    def save(
        self,
        resume: ProjectResume,
    ) -> None:
        self._storage[
            resume.metadata.resume_id
        ] = resume

    def update(
        self,
        resume: ProjectResume,
    ) -> None:
        self._storage[
            resume.metadata.resume_id
        ] = resume

    def delete(
        self,
        resume_id: UUID,
    ) -> None:
        self._storage.pop(
            resume_id,
            None,
        )

    def exists(
        self,
        resume_id: UUID,
    ) -> bool:
        return resume_id in self._storage

    def get_by_id(
        self,
        resume_id: UUID,
    ) -> ProjectResume | None:
        return self._storage.get(
            resume_id,
        )

    def get_latest(
        self,
        project_id: UUID,
    ) -> ProjectResume | None:

        resumes = [
            resume
            for resume in self._storage.values()
            if resume.project_id == project_id
        ]

        if not resumes:
            return None

        return max(
            resumes,
            key=lambda item: item.metadata.generated_at,
        )

    def list_by_project(
        self,
        project_id: UUID,
    ) -> list[ProjectResume]:

        return [
            resume
            for resume in self._storage.values()
            if resume.project_id == project_id
        ]

    def count(
        self,
        project_id: UUID,
    ) -> int:

        return len(
            self.list_by_project(
                project_id,
            ),
        )