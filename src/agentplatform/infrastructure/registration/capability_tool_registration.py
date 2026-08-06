"""
ShadBot Agent Platform

Capability to tool binding registration.
"""

from __future__ import annotations

from agentplatform.domain.capabilities import CapabilityType
from agentplatform.domain.tools import ToolType


class CapabilityToolBinding:
    """
    Maps agent capabilities to required tools.
    """

    def __init__(
        self,
    ) -> None:
        self._bindings: dict[
            CapabilityType,
            set[ToolType],
        ] = {}

    def register(
        self,
        capability: CapabilityType,
        tools: set[ToolType],
    ) -> None:
        self._bindings[capability] = tools

    def get_tools(
        self,
        capability: CapabilityType,
    ) -> set[ToolType]:
        return self._bindings.get(
            capability,
            set(),
        )

    def exists(
        self,
        capability: CapabilityType,
    ) -> bool:
        return capability in self._bindings


def register_default_capability_tools(
    registry: CapabilityToolBinding,
) -> CapabilityToolBinding:
    """
    Register capability requirements.
    """

    registry.register(
        CapabilityType.CODE_GENERATION,
        {
            ToolType.FILE_SYSTEM,
            ToolType.TERMINAL,
            ToolType.BUILD_RUNNER,
            ToolType.GIT,
        },
    )

    registry.register(
        CapabilityType.CODE_REFACTORING,
        {
            ToolType.FILE_SYSTEM,
            ToolType.TERMINAL,
            ToolType.QUALITY_VALIDATOR,
        },
    )

    registry.register(
        CapabilityType.DEBUGGING,
        {
            ToolType.TERMINAL,
            ToolType.LOG_ANALYZER,
            ToolType.QUALITY_VALIDATOR,
        },
    )

    registry.register(
        CapabilityType.TEST_GENERATION,
        {
            ToolType.FILE_SYSTEM,
            ToolType.TEST_RUNNER,
        },
    )

    registry.register(
        CapabilityType.PROJECT_ANALYSIS,
        {
            ToolType.PROJECT_ANALYZER,
            ToolType.FILE_SYSTEM,
        },
    )

    registry.register(
        CapabilityType.WORKSPACE_SCAN,
        {
            ToolType.PROJECT_ANALYZER,
            ToolType.FILE_SYSTEM,
        },
    )

    registry.register(
        CapabilityType.DEPENDENCY_ANALYSIS,
        {
            ToolType.PROJECT_ANALYZER,
            ToolType.FILE_SYSTEM,
        },
    )

    registry.register(
        CapabilityType.RESEARCH,
        {
            ToolType.RESEARCH,
            ToolType.DOCUMENTATION_ANALYSIS,
            ToolType.TECHNOLOGY_COMPARISON,
        },
    )

    registry.register(
        CapabilityType.TECHNOLOGY_SELECTION,
        {
            ToolType.TECHNOLOGY_COMPARISON,
            ToolType.RESEARCH,
        },
    )

    registry.register(
        CapabilityType.MODEL_EVALUATION,
        {
            ToolType.MODEL_EVALUATION,
            ToolType.EXPERIMENT_TRACKING,
        },
    )

    registry.register(
        CapabilityType.MODEL_TRAINING,
        {
            ToolType.MODEL_TRAINING,
            ToolType.MODEL_TRAINER,
            ToolType.DATASET_MANAGER,
        },
    )

    registry.register(
        CapabilityType.RETRAINING,
        {
            ToolType.MODEL_TRAINING,
            ToolType.DATASET_MANAGER,
            ToolType.EXPERIMENT_TRACKING,
        },
    )

    registry.register(
        CapabilityType.IMPROVEMENT_LOOP,
        {
            ToolType.IMPROVEMENT_LOOP,
            ToolType.MODEL_EVALUATION,
            ToolType.EXPERIMENT_TRACKING,
        },
    )

    registry.register(
        CapabilityType.RUNTIME_MONITORING,
        {
            ToolType.EXECUTION_MONITOR,
            ToolType.METRICS_COLLECTOR,
        },
    )

    registry.register(
        CapabilityType.ANOMALY_DETECTION,
        {
            ToolType.LOG_ANALYZER,
            ToolType.METRICS_COLLECTOR,
        },
    )

    registry.register(
        CapabilityType.SECURITY_ANALYSIS,
        {
            ToolType.QUALITY_VALIDATOR,
            ToolType.STATIC_ANALYZER,
        },
    )

    return registry
