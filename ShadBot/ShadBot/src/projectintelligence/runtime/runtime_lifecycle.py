"""
ShadBot Project Intelligence

Runtime Lifecycle
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from enum import StrEnum


class RuntimeStatus(StrEnum):
    """
    Runtime execution status.
    """

    CREATED = "created"

    STARTING = "starting"

    RUNNING = "running"

    COMPLETED = "completed"

    FAILED = "failed"


@dataclass(slots=True)
class RuntimeLifecycle:
    """
    Represents the lifecycle of a single Project Intelligence runtime
    execution.
    """

    status: RuntimeStatus = RuntimeStatus.CREATED

    started_at: datetime | None = None

    completed_at: datetime | None = None

    failed_at: datetime | None = None

    def mark_starting(self) -> None:
        """
        Transition runtime to starting.
        """

        self.status = RuntimeStatus.STARTING

    def mark_running(self) -> None:
        """
        Transition runtime to running.
        """

        self.status = RuntimeStatus.RUNNING

        if self.started_at is None:
            self.started_at = datetime.now(
                timezone.utc,
            )

    def mark_completed(self) -> None:
        """
        Transition runtime to completed.
        """

        self.status = RuntimeStatus.COMPLETED

        self.completed_at = datetime.now(
            timezone.utc,
        )

    def mark_failed(self) -> None:
        """
        Transition runtime to failed.
        """

        self.status = RuntimeStatus.FAILED

        self.failed_at = datetime.now(
            timezone.utc,
        )

    @property
    def is_running(self) -> bool:
        """
        Returns whether runtime is currently running.
        """

        return self.status is RuntimeStatus.RUNNING

    @property
    def is_completed(self) -> bool:
        """
        Returns whether runtime completed successfully.
        """

        return self.status is RuntimeStatus.COMPLETED

    @property
    def is_failed(self) -> bool:
        """
        Returns whether runtime failed.
        """

        return self.status is RuntimeStatus.FAILED
