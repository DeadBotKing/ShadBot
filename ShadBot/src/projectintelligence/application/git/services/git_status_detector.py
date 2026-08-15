from __future__ import annotations

from ..contracts.git_repository import IGitRepository
from ..models.git_status import GitStatus


class GitStatusDetector:
    """
    Detects current Git repository status.

    This service contains application logic only.
    It depends on repository abstraction.
    """

    def __init__(
        self,
        git_repository: IGitRepository,
    ) -> None:
        self._git_repository = git_repository

    def detect(self) -> GitStatus:
        """
        Returns current Git repository status.
        """

        return self._git_repository.get_status()
