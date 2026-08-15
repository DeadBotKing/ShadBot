"""
ShadBot Agent Platform

Unified service for Phase 10 Self Improvement System.
"""

from __future__ import annotations

from typing import Sequence
from agentplatform.domain.results import AgentResult
from .brain_evolution import BrainEvolutionManager, BrainEvolutionReport
from .experiment_engine import ControlledExperiment, ExperimentEngine
from .improvement_proposal import AutonomousImprovementProposal, ProposalGenerator
from .performance_tracker import PerformanceTracker, PerformanceTrend
from .reflection_analyzer import ReflectionAnalysisResult, ReflectionAnalyzer


class SelfImprovementServiceLayer:
    """
    Orchestrates reflection analysis, performance tracking, controlled experimentation, proposal generation, and brain evolution.
    """

    def __init__(
        self,
        analyzer: ReflectionAnalyzer | None = None,
        tracker: PerformanceTracker | None = None,
        exp_engine: ExperimentEngine | None = None,
        proposal_gen: ProposalGenerator | None = None,
        evolution_mgr: BrainEvolutionManager | None = None,
    ) -> None:
        self.analyzer = analyzer or ReflectionAnalyzer()
        self.tracker = tracker or PerformanceTracker()
        self.exp_engine = exp_engine or ExperimentEngine()
        self.proposal_gen = proposal_gen or ProposalGenerator()
        self.evolution_mgr = evolution_mgr or BrainEvolutionManager()

    def run_improvement_cycle(self, results: Sequence[AgentResult]) -> tuple[ReflectionAnalysisResult, PerformanceTrend, ControlledExperiment, AutonomousImprovementProposal, BrainEvolutionReport]:
        analysis = self.analyzer.analyze(results)
        trend = self.tracker.track(analysis)
        exp = self.exp_engine.create_experiment("Optimizing prompt context reduces syntax retries.")
        prop = self.proposal_gen.generate(exp)
        evo = self.evolution_mgr.evolve(prop)
        return analysis, trend, exp, prop, evo

    def get_cycle_summary(self, results: Sequence[AgentResult]) -> dict[str, object]:
        analysis, trend, exp, prop, evo = self.run_improvement_cycle(results)
        return {
            "reflection_analysis": analysis.to_dict(),
            "performance_trend": trend.to_dict(),
            "controlled_experiment": exp.to_dict(),
            "improvement_proposal": prop.to_dict(),
            "brain_evolution": evo.to_dict(),
        }
