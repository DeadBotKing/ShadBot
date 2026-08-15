from __future__ import annotations

from projectintelligence.application.knowledge.rules.architecture.architecture_layer_rule import (
    ArchitectureLayerRule,
)
from projectintelligence.application.knowledge.rules.base_rule import (
    BaseRule,
)


class ArchitectureRuleRegistry:
    """
    Provides architecture analysis rules.

    Registry isolates rule creation from the execution engine.
    """

    @staticmethod
    def get_rules() -> tuple[BaseRule, ...]:
        """
        Returns registered architecture rules.
        """

        return (ArchitectureLayerRule(),)
