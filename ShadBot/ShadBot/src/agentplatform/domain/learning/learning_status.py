"""
ShadBot Agent Platform

Learning status.
"""

from __future__ import annotations

from enum import Enum


class LearningStatus(str, Enum):
    PENDING = "pending"
    RUNNING = "running"
    COMPLETED = "completed"
    FAILED = "failed"
