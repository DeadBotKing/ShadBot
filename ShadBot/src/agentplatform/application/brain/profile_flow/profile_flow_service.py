"""
ShadBot Agent Platform

Unified service for 5.7 Profile Flow.
"""

from __future__ import annotations

from dataclasses import dataclass
from agentplatform.domain.agents import AgentRole
from .behavior_constraints import BehaviorConstraints, BehaviorConstraintSet
from .capability_awareness import CapabilityAwareness, CapabilityMatchResult
from .profile_loader import LoadedProfile, ProfileLoader


@dataclass(frozen=True, slots=True)
class AppliedProfilePackage:
    profile: LoadedProfile
    awareness: CapabilityMatchResult
    constraints: BehaviorConstraintSet


class ProfileFlowService:
    """
    Orchestrates profile loading, capability awareness, and behavior constraints.
    """

    def __init__(
        self,
        loader: ProfileLoader | None = None,
        awareness: CapabilityAwareness | None = None,
        constraints: BehaviorConstraints | None = None,
    ) -> None:
        self._loader = loader or ProfileLoader()
        self._awareness = awareness or CapabilityAwareness()
        self._constraints = constraints or BehaviorConstraints()

    def apply(self, role: AgentRole, task_type: str) -> AppliedProfilePackage:
        prof = self._loader.load(role)
        match = self._awareness.check(prof, task_type)
        const = self._constraints.enforce(prof)
        return AppliedProfilePackage(
            profile=prof,
            awareness=match,
            constraints=const,
        )
