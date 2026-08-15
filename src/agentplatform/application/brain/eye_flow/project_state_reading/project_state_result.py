"""
ShadBot Agent Platform

Project State Reading Result
"""

from __future__ import annotations

from dataclasses import dataclass
from uuid import UUID

from .project_state import ProjectState


@dataclass(frozen=True, slots=True)
class ProjectStateResult:
    """
    Result produced by ProjectStateReader.

    A successful result always contains a complete ProjectState.
    """

    state: ProjectState

    @property
    def project_id(self) -> UUID:
        """
        Return the project identifier.
        """

        return self.state.project_id

    @property
    def project_name(self) -> str:
        """
        Return the project name.
        """

        return self.state.project_name

    @property
    def is_available(self) -> bool:
        """
        Return whether the project is available.
        """

        return self.state.is_available

    @property
    def is_ready(self) -> bool:
        """
        Return whether the project is ready.
        """

        return self.state.is_ready