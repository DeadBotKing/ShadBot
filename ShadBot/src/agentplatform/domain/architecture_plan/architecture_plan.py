"""
ShadBot Agent Platform

Architecture plan domain model.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from uuid import UUID

from .acceptance_criteria import AcceptanceCriteria
from .dependency_plan import DependencyPlan
from .file_plan import FilePlan
from .implementation_step import ImplementationStep
from .interface_plan import InterfacePlan


@dataclass(frozen=True, slots=True)
class ArchitecturePlan:
    """
    Enterprise architecture decision output.

    Produced by Architect Agent.
    Consumed by Engineer Agent.
    """

    plan_id: UUID

    task_id: UUID

    summary: str

    file_plan: tuple[FilePlan, ...]

    dependency_plan: tuple[DependencyPlan, ...]

    interface_plan: tuple[InterfacePlan, ...]

    implementation_order: tuple[ImplementationStep, ...]

    acceptance_criteria: tuple[AcceptanceCriteria, ...]

    constraints: tuple[str, ...] = field(
        default_factory=tuple,
    )
