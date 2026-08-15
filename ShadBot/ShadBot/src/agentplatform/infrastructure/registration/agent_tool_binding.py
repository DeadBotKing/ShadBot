"""
ShadBot Agent Platform

Agent tool binding registration.
"""

from __future__ import annotations

from agentplatform.application.tooling import (
    ToolRegistry,
)
from agentplatform.domain.agents import (
    AgentRole,
)
from agentplatform.domain.tools import (
    ToolType,
)

AGENT_TOOL_BINDINGS: dict[
    AgentRole,
    list[ToolType],
] = {
    AgentRole.PROJECT_INTELLIGENCE: [
        ToolType.FILE_SYSTEM,
        ToolType.PROJECT_ANALYZER,
        ToolType.GIT,
        ToolType.DOCUMENTATION_ANALYSIS,
    ],
    AgentRole.ARCHITECT: [
        ToolType.RESEARCH,
        ToolType.TECHNOLOGY_COMPARISON,
        ToolType.DOCUMENTATION_ANALYSIS,
        ToolType.PROJECT_ANALYZER,
    ],
    AgentRole.RESEARCHER: [
        ToolType.RESEARCH,
        ToolType.DOCUMENTATION_ANALYSIS,
        ToolType.TECHNOLOGY_COMPARISON,
    ],
    AgentRole.RND: [
        ToolType.RESEARCH,
        ToolType.EXPERIMENT_DESIGN,
        ToolType.EXPERIMENT_TRACKING,
        ToolType.TECHNOLOGY_COMPARISON,
    ],
    AgentRole.ENGINEER: [
        ToolType.FILE_SYSTEM,
        ToolType.TERMINAL,
        ToolType.BUILD_RUNNER,
        ToolType.TEST_RUNNER,
        ToolType.GIT,
        ToolType.QUALITY_VALIDATOR,
    ],
    AgentRole.QA: [
        ToolType.TEST_RUNNER,
        ToolType.QUALITY_VALIDATOR,
        ToolType.LOG_ANALYZER,
    ],
    AgentRole.REVIEWER: [
        ToolType.QUALITY_VALIDATOR,
        (
            ToolType.SECURITY_ANALYSIS
            if hasattr(ToolType, "SECURITY_ANALYSIS")
            else ToolType.QUALITY_VALIDATOR
        ),
        ToolType.TEST_RUNNER,
    ],
    AgentRole.ML_SCIENTIST: [
        ToolType.MODEL_EVALUATION,
        ToolType.MODEL_TRAINING,
        ToolType.EXPERIMENT_TRACKING,
        ToolType.EXPERIMENT_DESIGN,
    ],
    AgentRole.RUNTIME_OBSERVER: [
        ToolType.EXECUTION_MONITOR,
        ToolType.METRICS_COLLECTOR,
        ToolType.LOG_ANALYZER,
        ToolType.SYSTEM_HEALTH,
    ],
}


def get_agent_tools(
    role: AgentRole,
) -> list[ToolType]:
    """
    Return allowed tools for agent role.
    """

    return AGENT_TOOL_BINDINGS.get(
        role,
        [],
    )


def validate_agent_tools(
    role: AgentRole,
    registry: ToolRegistry,
) -> list[ToolType]:
    """
    Validate that required tools exist.
    """

    missing: list[ToolType] = []

    for tool in get_agent_tools(role):

        if not registry.exists(tool):
            missing.append(tool)

    return missing
