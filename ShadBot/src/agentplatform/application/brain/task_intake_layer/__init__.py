"""
ShadBot Agent Platform

5.14 Task Intake Layer module.
"""

from .task_completion_reporter import TaskCompletionReport, TaskCompletionReporter
from .task_discovery import TaskDiscovery
from .task_intake_service import TaskIntakeService
from .task_normalizer import NormalizedTaskPackage, TaskNormalizer
from .task_parser import ParsedTaskMetadata, TaskParser
from .task_reader import TaskReader
from .task_state_manager import TaskIntakeState, TaskStateManager

__all__ = [
    "TaskDiscovery",
    "TaskReader",
    "ParsedTaskMetadata",
    "TaskParser",
    "NormalizedTaskPackage",
    "TaskNormalizer",
    "TaskIntakeState",
    "TaskStateManager",
    "TaskCompletionReport",
    "TaskCompletionReporter",
    "TaskIntakeService",
]
