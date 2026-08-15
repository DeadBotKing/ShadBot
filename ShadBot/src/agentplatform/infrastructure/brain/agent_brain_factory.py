"""
ShadBot Agent Platform

Enterprise Agent Brain Factory.
"""

from __future__ import annotations

from agentplatform.application.brain import (
    AgentBrain,
    BrainFactory,
    BrainMemory,
    BrainProfile,
    BrainReasoning,
)
from agentplatform.application.memory import (
    MemoryService,
)
from agentplatform.domain.agents import AgentRole


class AgentBrainFactory(BrainFactory):
    """
    Enterprise brain factory.

    Responsibilities:
    - Create isolated agent brains
    - Attach agent personality profile
    - Attach project memory
    - Prepare cognitive identity
    """

    def __init__(
        self,
        reasoning: BrainReasoning,
        memory_service: MemoryService | None = None,
    ) -> None:

        self._reasoning = reasoning
        self._memory_service = memory_service

    def create(
        self,
        role: AgentRole,
    ) -> AgentBrain:
        """
        Create specialized agent brain.
        """

        memory = None

        if self._memory_service is not None:
            memory = BrainMemory(
                self._memory_service,
            )

        return AgentBrain(
            reasoning=self._reasoning,
            memory=memory,
            profile=self._create_profile(
                role,
            ),
        )

    def _create_profile(
        self,
        role: AgentRole,
    ) -> BrainProfile:
        """
        Create cognitive profile.
        """

        profiles = {
            AgentRole.ARCHITECT: BrainProfile(
                role=role,
                reasoning_style=("architecture_reasoning"),
                planning_style=("system_design"),
                decision_style=("technology_selection"),
                reflection_style=("architecture_review"),
                validation_style=("architecture_validation"),
            ),
            AgentRole.ENGINEER: BrainProfile(
                role=role,
                reasoning_style=("implementation_reasoning"),
                planning_style=("execution_planning"),
                decision_style=("coding_decision"),
                reflection_style=("code_reflection"),
                validation_style=("implementation_validation"),
            ),
            AgentRole.REVIEWER: BrainProfile(
                role=role,
                reasoning_style=("critical_review_reasoning"),
                planning_style=("review_planning"),
                decision_style=("quality_decision"),
                reflection_style=("review_analysis"),
                validation_style=("quality_validation"),
            ),
            AgentRole.ML_SCIENTIST: BrainProfile(
                role=role,
                reasoning_style=("ml_experiment_reasoning"),
                planning_style=("experiment_planning"),
                decision_style=("model_selection"),
                reflection_style=("experiment_analysis"),
                validation_style=("model_validation"),
            ),
            AgentRole.RESEARCHER: BrainProfile(
                role=role,
                reasoning_style=("research_reasoning"),
                planning_style=("research_planning"),
                decision_style=("alternative_selection"),
                reflection_style=("research_reflection"),
                validation_style=("research_validation"),
            ),
            AgentRole.QA: BrainProfile(
                role=role,
                reasoning_style=("quality_reasoning"),
                planning_style=("test_planning"),
                decision_style=("release_decision"),
                reflection_style=("failure_analysis"),
                validation_style=("release_validation"),
            ),
        }

        return profiles.get(
            role,
            BrainProfile(
                role=role,
                reasoning_style="general_reasoning",
                planning_style="general_planning",
                decision_style="general_decision",
                reflection_style="general_reflection",
                validation_style="general_validation",
            ),
        )
