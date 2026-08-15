"""
ShadBot Agent Platform

Task Normalizer component for 5.14 Task Intake Layer.
"""

from __future__ import annotations

from dataclasses import dataclass
from uuid import UUID, uuid4
from agentplatform.domain.tasks import AgentTask, TaskType
from .task_parser import ParsedTaskMetadata


@dataclass(frozen=True, slots=True)
class NormalizedTaskPackage:
    task_id: UUID
    task: AgentTask
    raw_metadata: ParsedTaskMetadata


class TaskNormalizer:
    """
    Normalizes parsed metadata into a standard AgentTask contract.
    """

    def normalize(self, metadata: ParsedTaskMetadata, task_type: TaskType = TaskType.IMPLEMENTATION) -> NormalizedTaskPackage:
        task = AgentTask(
            title=metadata.title,
            description=metadata.description,
            task_type=task_type,
        )
        return NormalizedTaskPackage(
            task_id=task.id,
            task=task,
            raw_metadata=metadata,
        )
