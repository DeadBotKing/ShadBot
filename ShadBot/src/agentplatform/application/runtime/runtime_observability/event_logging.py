"""
ShadBot Agent Platform

Runtime Event Logging component for 7.7 Runtime Observability.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone


@dataclass(frozen=True, slots=True)
class RuntimeLogEntry:
    level: str  # INFO, WARN, ERROR
    message: str
    timestamp: str = field(default_factory=lambda: datetime.now(timezone.utc).isoformat())


class RuntimeEventLogger:
    """
    Logs structured runtime events for diagnostic observability.
    """

    def __init__(self) -> None:
        self._logs: list[RuntimeLogEntry] = []

    def log(self, level: str, message: str) -> RuntimeLogEntry:
        entry = RuntimeLogEntry(level.upper(), message)
        self._logs.append(entry)
        return entry

    def get_logs(self) -> tuple[RuntimeLogEntry, ...]:
        return tuple(self._logs)
