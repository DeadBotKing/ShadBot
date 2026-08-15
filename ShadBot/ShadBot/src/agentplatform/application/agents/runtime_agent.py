"""
ShadBot Agent Platform

Runtime Agent
"""

from __future__ import annotations

from dataclasses import dataclass, field

from agentplatform.application.brain import AgentBrain
from agentplatform.domain.agents import (
    AgentCapability,
    AgentRole,
)
from agentplatform.domain.context import BrainContext

from .attention_binding import AttentionBinding
from .decision_binding import DecisionBinding
from .eye_binding import EyeBinding
from .goal_binding import GoalBinding
from .learning_binding import LearningBinding
from .memory_binding import MemoryBinding
from .planning_binding import PlanningBinding
from .profile_binding import ProfileBinding
from .reasoning_binding import ReasoningBinding
from .reflection_binding import ReflectionBinding
from .runtime_agent_state import RuntimeAgentState
from .validation_binding import ValidationBinding


@dataclass(slots=True)
class RuntimeAgent:
    """
    Executable runtime representation of an Agent.
    """

    role: AgentRole

    brain: AgentBrain

    capabilities: set[AgentCapability] = field(
        default_factory=set,
    )

    state: RuntimeAgentState = field(
        default_factory=RuntimeAgentState,
    )

    context: BrainContext | None = None

    memory: MemoryBinding | None = None

    eyes: EyeBinding | None = None

    reasoning: ReasoningBinding | None = None

    decision: DecisionBinding | None = None

    profile: ProfileBinding | None = None

    planning: PlanningBinding | None = None

    reflection: ReflectionBinding | None = None

    validation: ValidationBinding | None = None

    learning: LearningBinding | None = None

    goal: GoalBinding | None = None

    attention: AttentionBinding | None = None

    def supports(
        self,
        capability: AgentCapability,
    ) -> bool:
        """
        Check capability.
        """

        return capability in self.capabilities
