from __future__ import annotations

from projectintelligence.application.knowledge.rules.registry.rule_registry import (
    RuleRegistry,
)
from projectintelligence.application.knowledge.rules.rule_engine import (
    RuleEngine,
)


class RuleEngineFactory:
    """
    Creates configured RuleEngine instances.

    Factory isolates dependency creation from application services
    and pipeline orchestration.
    """

    @staticmethod
    def create() -> RuleEngine:
        """
        Create a RuleEngine with all registered rules loaded.
        """

        engine = RuleEngine()

        for rule in RuleRegistry.get_rules():
            engine.register(rule)

        return engine
