from __future__ import annotations

from projectintelligence.application.knowledge.rules.architecture.architecture_layer_rule import (
    ArchitectureLayerRule,
)
from projectintelligence.application.knowledge.rules.base_rule import (
    BaseRule,
)


class RuleRegistry:
    """
    Central registry for all knowledge analysis rules.

    This registry provides a single entry point for rule discovery
    while keeping rule creation isolated from RuleEngine.
    """

    @staticmethod
    def get_rules() -> tuple[BaseRule, ...]:
        """
        Returns all registered rules.
        """

        return (ArchitectureLayerRule(),)
