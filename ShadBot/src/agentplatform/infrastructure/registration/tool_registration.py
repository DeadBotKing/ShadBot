"""
ShadBot Agent Platform

Enterprise default tool registration.
"""

from __future__ import annotations

from agentplatform.application.tooling import ToolRegistry
from agentplatform.domain.tooling import ToolDefinition
from agentplatform.domain.tools import ToolType
from agentplatform.infrastructure.tools.build_runner_adapter import (
    BuildRunnerAdapter,
)
from agentplatform.infrastructure.tools.code_execution_adapter import (
    CodeExecutionAdapter,
)
from agentplatform.infrastructure.tools.code_search_adapter import (
    CodeSearchAdapter,
)
from agentplatform.infrastructure.tools.diff_analyzer_adapter import (
    DiffAnalyzerAdapter,
)
from agentplatform.infrastructure.tools.documentation_analyzer_adapter import (
    DocumentationAnalyzerAdapter,
)
from agentplatform.infrastructure.tools.execution_monitor_adapter import (
    ExecutionMonitorAdapter,
)
from agentplatform.infrastructure.tools.experiment_executor_adapter import (
    ExperimentExecutorAdapter,
)
from agentplatform.infrastructure.tools.experiment_tracker_adapter import (
    ExperimentTrackerAdapter,
)
from agentplatform.infrastructure.tools.filesystem_tool_adapter import (
    FileSystemToolAdapter,
)
from agentplatform.infrastructure.tools.git_tool_adapter import (
    GitToolAdapter,
)
from agentplatform.infrastructure.tools.improvement_loop_adapter import (
    ImprovementLoopAdapter,
)
from agentplatform.infrastructure.tools.log_analyzer_adapter import (
    LogAnalyzerAdapter,
)
from agentplatform.infrastructure.tools.metrics_collector_adapter import (
    MetricsCollectorAdapter,
)
from agentplatform.infrastructure.tools.model_evaluation_adapter import (
    ModelEvaluationAdapter,
)
from agentplatform.infrastructure.tools.package_manager_adapter import (
    PackageManagerAdapter,
)
from agentplatform.infrastructure.tools.patch_applier_adapter import (
    PatchApplierAdapter,
)
from agentplatform.infrastructure.tools.project_analyzer_tool_adapter import (
    ProjectAnalyzerToolAdapter,
)
from agentplatform.infrastructure.tools.quality_validator_adapter import (
    QualityValidatorAdapter,
)
from agentplatform.infrastructure.tools.research_tool_adapter import (
    ResearchToolAdapter,
)
from agentplatform.infrastructure.tools.retraining_tool_adapter import (
    RetrainingToolAdapter,
)
from agentplatform.infrastructure.tools.system_health_adapter import (
    SystemHealthAdapter,
)
from agentplatform.infrastructure.tools.technology_comparator_adapter import (
    TechnologyComparatorAdapter,
)
from agentplatform.infrastructure.tools.terminal_tool_adapter import (
    TerminalToolAdapter,
)
from agentplatform.infrastructure.tools.test_runner_adapter import (
    TestRunnerAdapter,
)


def register_default_tools(
    registry: ToolRegistry,
) -> ToolRegistry:
    """
    Register all built-in enterprise tools.
    """

    tools = [
        (
            ToolType.FILE_SYSTEM,
            "filesystem",
            "Read and write project files.",
            FileSystemToolAdapter(),
        ),
        (
            ToolType.TERMINAL,
            "terminal",
            "Execute terminal commands.",
            TerminalToolAdapter(),
        ),
        (
            ToolType.GIT,
            "git",
            "Repository management operations.",
            GitToolAdapter(),
        ),
        (
            ToolType.TEST_RUNNER,
            "test_runner",
            "Execute automated tests.",
            TestRunnerAdapter(),
        ),
        (
            ToolType.BUILD_RUNNER,
            "build_runner",
            "Execute project builds.",
            BuildRunnerAdapter(),
        ),
        (
            ToolType.PROJECT_ANALYZER,
            "project_analyzer",
            "Analyze project intelligence.",
            ProjectAnalyzerToolAdapter(),
        ),
        (
            ToolType.QUALITY_VALIDATOR,
            "quality_validator",
            "Validate enterprise quality.",
            QualityValidatorAdapter(),
        ),
        (
            ToolType.RESEARCH,
            "research",
            "Perform technical research.",
            ResearchToolAdapter(),
        ),
        (
            ToolType.DOCUMENTATION_ANALYSIS,
            "documentation_analyzer",
            "Analyze documentation.",
            DocumentationAnalyzerAdapter(),
        ),
        (
            ToolType.TECHNOLOGY_COMPARISON,
            "technology_comparator",
            "Compare technologies.",
            TechnologyComparatorAdapter(),
        ),
        (
            ToolType.EXPERIMENT_TRACKING,
            "experiment_tracker",
            "Track experiments.",
            ExperimentTrackerAdapter(),
        ),
        (
            ToolType.MODEL_EVALUATION,
            "model_evaluation",
            "Evaluate ML models.",
            ModelEvaluationAdapter(),
        ),
        (
            ToolType.MODEL_TRAINING,
            "retraining",
            "Retrain ML models.",
            RetrainingToolAdapter(),
        ),
        (
            ToolType.EXPERIMENT_DESIGN,
            "experiment_executor",
            "Execute experiments.",
            ExperimentExecutorAdapter(),
        ),
        (
            ToolType.EXECUTION_MONITOR,
            "execution_monitor",
            "Monitor execution.",
            ExecutionMonitorAdapter(),
        ),
        (
            ToolType.METRICS_COLLECTOR,
            "metrics_collector",
            "Collect metrics.",
            MetricsCollectorAdapter(),
        ),
        (
            ToolType.LOG_ANALYZER,
            "log_analyzer",
            "Analyze system logs.",
            LogAnalyzerAdapter(),
        ),
        (
            ToolType.SYSTEM_HEALTH,
            "system_health",
            "Analyze system health.",
            SystemHealthAdapter(),
        ),
        (
            ToolType.CODE_EXECUTION,
            "code_execution",
            "Execute generated code safely.",
            CodeExecutionAdapter(),
        ),
        (
            ToolType.CODE_SEARCH,
            "code_search",
            "Search source code.",
            CodeSearchAdapter(),
        ),
        (
            ToolType.PATCH_APPLIER,
            "patch_applier",
            "Apply generated patches.",
            PatchApplierAdapter(),
        ),
        (
            ToolType.DIFF_ANALYZER,
            "diff_analyzer",
            "Analyze code differences.",
            DiffAnalyzerAdapter(),
        ),
        (
            ToolType.PACKAGE_MANAGER,
            "package_manager",
            "Manage project packages.",
            PackageManagerAdapter(),
        ),
        (
            ToolType.IMPROVEMENT_LOOP,
            "improvement_loop",
            "Run continuous improvement cycles.",
            ImprovementLoopAdapter(),
        ),
    ]

    for (
        tool_type,
        name,
        description,
        adapter,
    ) in tools:
        registry.register(
            ToolDefinition(
                name=name,
                tool_type=tool_type,
                description=description,
            ),
            adapter,
        )

    return registry
