"""
ShadBot Agent Platform

Phase 10 Self Improvement System module.
"""

from .brain_evolution import BrainEvolutionManager, BrainEvolutionReport
from .experiment_engine import ControlledExperiment, ExperimentEngine
from .improvement_proposal import AutonomousImprovementProposal, ProposalGenerator
from .performance_tracker import PerformanceTracker, PerformanceTrend
from .reflection_analyzer import ReflectionAnalysisResult, ReflectionAnalyzer
from .self_improvement_service import SelfImprovementServiceLayer

__all__ = [
    "ReflectionAnalysisResult",
    "ReflectionAnalyzer",
    "PerformanceTrend",
    "PerformanceTracker",
    "ControlledExperiment",
    "ExperimentEngine",
    "AutonomousImprovementProposal",
    "ProposalGenerator",
    "BrainEvolutionReport",
    "BrainEvolutionManager",
    "SelfImprovementServiceLayer",
]
