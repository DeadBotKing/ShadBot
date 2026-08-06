"""
ShadBot Agent Platform

Enterprise ML Scientist Agent.
"""

from __future__ import annotations

from agentplatform.application.tooling import (
    ToolExecutor,
)
from agentplatform.domain.agents import (
    AgentRole,
)
from agentplatform.domain.capabilities import (
    Capability,
    CapabilityType,
)
from agentplatform.domain.context import (
    AgentExecutionContext,
)
from agentplatform.domain.results import (
    AgentResult,
)
from agentplatform.domain.tools import (
    ToolType,
)

from .base_agent import BaseAgent


class MLScientistAgent(BaseAgent):
    """
    Responsible for machine learning intelligence.

    Responsibilities:
    - Model evaluation
    - Model training
    - Experiment design
    - Hyperparameter search
    - Improvement loop
    - Retraining strategy
    """

    def __init__(
        self,
        tool_executor: ToolExecutor,
    ) -> None:

        super().__init__(
            capabilities=[
                Capability(
                    CapabilityType.MODEL_EVALUATION,
                    "Evaluate machine learning model performance.",
                ),
                Capability(
                    CapabilityType.MODEL_TRAINING,
                    "Train machine learning models.",
                ),
                Capability(
                    CapabilityType.MODEL_IMPROVEMENT,
                    "Improve model architecture and parameters.",
                ),
                Capability(
                    CapabilityType.HYPERPARAMETER_SEARCH,
                    "Optimize model hyperparameters.",
                ),
                Capability(
                    CapabilityType.EXPERIMENT_DESIGN,
                    "Design machine learning experiments.",
                ),
                Capability(
                    CapabilityType.EXPERIMENT_TRACKING,
                    "Track ML experiments and results.",
                ),
                Capability(
                    CapabilityType.RETRAINING,
                    "Execute retraining workflows.",
                ),
                Capability(
                    CapabilityType.IMPROVEMENT_LOOP,
                    "Run iterative model improvement cycles.",
                ),
                Capability(
                    CapabilityType.PERFORMANCE_ANALYSIS,
                    "Analyze model performance metrics.",
                ),
                Capability(
                    CapabilityType.ANOMALY_DETECTION,
                    "Detect abnormal model behavior.",
                ),
                Capability(
                    CapabilityType.REGRESSION_ANALYSIS,
                    "Detect model regression.",
                ),
            ],
        )

        self._tool_executor = tool_executor

    @property
    def name(self) -> str:
        return "ml_scientist"

    def run(
        self,
        context: AgentExecutionContext,
    ) -> AgentResult:
        """
        Execute ML scientist workflow.
        """

        if context.target_project is None:
            return AgentResult(
                success=False,
                message="Target project required.",
                data={
                    "agent": self.name,
                },
            )

        project_path = str(
            context.target_project.path,
        )

        evaluation = self._tool_executor.execute(
            ToolType.MODEL_EVALUATION,
            {
                "path": project_path,
            },
        )

        experiments = self._tool_executor.execute(
            ToolType.EXPERIMENT_DESIGN,
            {
                "path": project_path,
            },
        )

        tracking = self._tool_executor.execute(
            ToolType.EXPERIMENT_TRACKING,
            {
                "path": project_path,
            },
        )

        retraining = self._tool_executor.execute(
            ToolType.MODEL_TRAINING,
            {
                "path": project_path,
                "operation": "retraining",
            },
        )

        return AgentResult(
            success=True,
            message=("ML Scientist workflow completed."),
            data={
                "agent": self.name,
                "role": AgentRole.ML_SCIENTIST.value,
                "capabilities": [
                    capability.capability_type.value for capability in self.capabilities
                ],
                "evaluation": evaluation,
                "experiments": experiments,
                "tracking": tracking,
                "retraining": retraining,
            },
        )
