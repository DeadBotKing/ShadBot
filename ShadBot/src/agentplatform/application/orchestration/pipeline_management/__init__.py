"""
ShadBot Agent Platform

6.3 Pipeline Management module.
"""

from .completion_detection import PipelineCompletionDetector
from .dependency_management import PipelineDependencyManager
from .pipeline_builder import PipelineBuilder
from .pipeline_definition import ExecutionPipeline, PipelineStep
from .pipeline_management_service import PipelineManagementService
from .state_tracking import PipelineState, PipelineStateTracker

__all__ = [
    "PipelineStep",
    "ExecutionPipeline",
    "PipelineBuilder",
    "PipelineState",
    "PipelineStateTracker",
    "PipelineDependencyManager",
    "PipelineCompletionDetector",
    "PipelineManagementService",
]
