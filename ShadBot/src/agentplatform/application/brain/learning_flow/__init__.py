"""
ShadBot Agent Platform

5.11 Learning Flow module.
"""

from .experience_extraction import ExperienceExtractor, ExtractedExperience
from .knowledge_update import KnowledgeUpdateReport, KnowledgeUpdater
from .learning_flow_service import CompleteLearningPackage, LearningFlowService
from .pattern_recognition import PatternRecognizer, RecognizedPattern
from .strategy_improvement import StrategyAdjustment, StrategyImprover

__all__ = [
    "ExtractedExperience",
    "ExperienceExtractor",
    "RecognizedPattern",
    "PatternRecognizer",
    "KnowledgeUpdateReport",
    "KnowledgeUpdater",
    "StrategyAdjustment",
    "StrategyImprover",
    "CompleteLearningPackage",
    "LearningFlowService",
]
