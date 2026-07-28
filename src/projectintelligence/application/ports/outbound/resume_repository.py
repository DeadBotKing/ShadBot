"""
ShadBot Project Intelligence

Resume Repository Port
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from uuid import UUID

from projectintelligence.domain.resume.project_resume import (
    ProjectResume,
)


class ResumeRepository(ABC):
    """
    Outbound port for persisting and retrieving project resumes.

    Implementations remain independent from persistence technology.
    """

    @abstractmethod
    def save(
        self,
        resume: ProjectResume,
    ) -> None:
        """
        Persist a project resume.
        """

    @abstractmethod
    def update(
        self,
        resume: ProjectResume,
    ) -> None:
        """
        Update an existing project resume.
        """

    @abstractmethod
    def delete(
        self,
        resume_id: UUID,
    ) -> None:
        """
        Delete a project resume.
        """

    @abstractmethod
    def exists(
        self,
        resume_id: UUID,
    ) -> bool:
        """
        Check whether a resume exists.
        """

    @abstractmethod
    def get_by_id(
        self,
        resume_id: UUID,
    ) -> ProjectResume | None:
        """
        Retrieve resume by identifier.
        """

    @abstractmethod
    def get_latest(
        self,
        project_id: UUID,
    ) -> ProjectResume | None:
        """
        Retrieve latest resume of a project.
        """

    @abstractmethod
    def list_by_project(
        self,
        project_id: UUID,
    ) -> list[ProjectResume]:
        """
        Retrieve all resumes belonging to a project.
        """

    @abstractmethod
    def count(
        self,
        project_id: UUID,
    ) -> int:
        """
        Count generated resumes for a project.
        """