"""
ShadBot Agent Platform

Enterprise agent capability registration.
"""

from __future__ import annotations

from agentplatform.application.capabilities import (
    CapabilityRegistry,
)
from agentplatform.domain.agents import AgentRole
from agentplatform.domain.capabilities import (
    Capability,
    CapabilityType,
)


def register_default_capabilities(
    registry: CapabilityRegistry,
) -> CapabilityRegistry:
    """
    Register enterprise capabilities for all agents.
    """

    assignments = {
        AgentRole.PROJECT_INTELLIGENCE: [
            Capability(
                CapabilityType.WORKSPACE_SCAN,
                "Scan workspace and collect project intelligence.",
            ),
            Capability(
                CapabilityType.DEPENDENCY_ANALYSIS,
                "Analyze project dependencies.",
            ),
            Capability(
                CapabilityType.KNOWLEDGE_GENERATION,
                "Generate project knowledge context.",
            ),
            Capability(
                CapabilityType.ARCHITECTURE_UNDERSTANDING,
                "Understand existing system architecture.",
            ),
            Capability(
                CapabilityType.SYSTEM_ANALYSIS,
                "Analyze complete system structure.",
            ),
        ],
        AgentRole.ARCHITECT: [
            Capability(
                CapabilityType.ARCHITECTURE_DESIGN,
                "Design enterprise software architecture.",
            ),
            Capability(
                CapabilityType.TECHNOLOGY_SELECTION,
                "Select suitable technologies.",
            ),
            Capability(
                CapabilityType.SYSTEM_ANALYSIS,
                "Analyze system requirements and structure.",
            ),
            Capability(
                CapabilityType.FEASIBILITY_ANALYSIS,
                "Evaluate technical feasibility.",
            ),
            Capability(
                CapabilityType.ARCHITECTURE_UNDERSTANDING,
                "Understand existing architectures.",
            ),
            Capability(
                CapabilityType.INNOVATION_ANALYSIS,
                "Analyze architectural improvements.",
            ),
        ],
        AgentRole.RESEARCHER: [
            Capability(
                CapabilityType.RESEARCH,
                "Perform technical research.",
            ),
            Capability(
                CapabilityType.TECHNOLOGY_RESEARCH,
                "Research technologies and solutions.",
            ),
            Capability(
                CapabilityType.SYSTEM_ANALYSIS,
                "Analyze technical information.",
            ),
            Capability(
                CapabilityType.DOCUMENTATION_ANALYSIS,
                "Analyze technical documentation.",
            ),
            Capability(
                CapabilityType.FEASIBILITY_ANALYSIS,
                "Evaluate solution feasibility.",
            ),
            Capability(
                CapabilityType.KNOWLEDGE_GENERATION,
                "Generate technical knowledge.",
            ),
        ],
        AgentRole.RND: [
            Capability(
                CapabilityType.RESEARCH,
                "Research advanced solutions.",
            ),
            Capability(
                CapabilityType.KNOWLEDGE_GENERATION,
                "Generate innovation knowledge.",
            ),
            Capability(
                CapabilityType.EXPERIMENT_DESIGN,
                "Design experiments.",
            ),
            Capability(
                CapabilityType.EXPERIMENT_EXECUTION,
                "Execute experiments.",
            ),
            Capability(
                CapabilityType.EXPERIMENT_TRACKING,
                "Track experiments.",
            ),
            Capability(
                CapabilityType.IDEA_GENERATION,
                "Generate improvement ideas.",
            ),
            Capability(
                CapabilityType.PROTOTYPE_DEVELOPMENT,
                "Develop prototypes.",
            ),
            Capability(
                CapabilityType.INNOVATION_ANALYSIS,
                "Analyze innovation opportunities.",
            ),
        ],
        AgentRole.ENGINEER: [
            Capability(
                CapabilityType.CODE_GENERATION,
                "Generate production code.",
            ),
            Capability(
                CapabilityType.IMPLEMENTATION,
                "Implement approved designs.",
            ),
            Capability(
                CapabilityType.CODE_REFACTORING,
                "Refactor existing code.",
            ),
            Capability(
                CapabilityType.REFACTORING,
                "Perform advanced refactoring.",
            ),
            Capability(
                CapabilityType.TEST_GENERATION,
                "Generate automated tests.",
            ),
            Capability(
                CapabilityType.DEBUGGING,
                "Debug software problems.",
            ),
            Capability(
                CapabilityType.FAILURE_ANALYSIS,
                "Analyze implementation failures.",
            ),
            Capability(
                CapabilityType.PERFORMANCE_ANALYSIS,
                "Optimize implementation performance.",
            ),
            Capability(
                CapabilityType.SECURITY_ANALYSIS,
                "Apply secure coding practices.",
            ),
        ],
        AgentRole.REVIEWER: [
            Capability(
                CapabilityType.CODE_REVIEW,
                "Review code quality.",
            ),
            Capability(
                CapabilityType.VALIDATION,
                "Validate implementation.",
            ),
            Capability(
                CapabilityType.SECURITY_ANALYSIS,
                "Review security risks.",
            ),
            Capability(
                CapabilityType.PERFORMANCE_ANALYSIS,
                "Review performance.",
            ),
            Capability(
                CapabilityType.ARCHITECTURE_UNDERSTANDING,
                "Validate architecture consistency.",
            ),
            Capability(
                CapabilityType.STYLE_ANALYSIS,
                "Analyze code style.",
            ),
            Capability(
                CapabilityType.COVERAGE_ANALYSIS,
                "Analyze test coverage.",
            ),
            Capability(
                CapabilityType.REGRESSION_ANALYSIS,
                "Detect regressions.",
            ),
        ],
        AgentRole.QA: [
            Capability(
                CapabilityType.TEST_GENERATION,
                "Generate test scenarios.",
            ),
            Capability(
                CapabilityType.TESTING,
                "Execute quality tests.",
            ),
            Capability(
                CapabilityType.COVERAGE_ANALYSIS,
                "Analyze test coverage.",
            ),
            Capability(
                CapabilityType.REGRESSION_ANALYSIS,
                "Detect regressions.",
            ),
            Capability(
                CapabilityType.VALIDATION,
                "Validate release quality.",
            ),
        ],
        AgentRole.RUNTIME_OBSERVER: [
            Capability(
                CapabilityType.RUNTIME_MONITORING,
                "Monitor runtime execution.",
            ),
            Capability(
                CapabilityType.RUNTIME_ANALYSIS,
                "Analyze runtime behavior.",
            ),
            Capability(
                CapabilityType.FAILURE_ANALYSIS,
                "Analyze runtime failures.",
            ),
            Capability(
                CapabilityType.PERFORMANCE_ANALYSIS,
                "Analyze runtime performance.",
            ),
            Capability(
                CapabilityType.ANOMALY_DETECTION,
                "Detect anomalies.",
            ),
        ],
        AgentRole.ML_SCIENTIST: [
            Capability(
                CapabilityType.MODEL_TRAINING,
                "Train machine learning models.",
            ),
            Capability(
                CapabilityType.MODEL_EVALUATION,
                "Evaluate models.",
            ),
            Capability(
                CapabilityType.MODEL_IMPROVEMENT,
                "Improve model architecture.",
            ),
            Capability(
                CapabilityType.HYPERPARAMETER_SEARCH,
                "Optimize hyperparameters.",
            ),
            Capability(
                CapabilityType.EXPERIMENT_DESIGN,
                "Design ML experiments.",
            ),
            Capability(
                CapabilityType.EXPERIMENT_TRACKING,
                "Track ML experiments.",
            ),
            Capability(
                CapabilityType.RETRAINING,
                "Execute retraining.",
            ),
            Capability(
                CapabilityType.IMPROVEMENT_LOOP,
                "Run ML improvement loops.",
            ),
            Capability(
                CapabilityType.ANOMALY_DETECTION,
                "Detect model anomalies.",
            ),
            Capability(
                CapabilityType.REGRESSION_ANALYSIS,
                "Analyze model regressions.",
            ),
            Capability(
                CapabilityType.PERFORMANCE_ANALYSIS,
                "Analyze model performance.",
            ),
        ],
    }

    for role, capabilities in assignments.items():
        for capability in capabilities:
            registry.register(
                role,
                capability,
            )

    return registry
