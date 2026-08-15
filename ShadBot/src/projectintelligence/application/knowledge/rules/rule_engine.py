from __future__ import annotations

from dataclasses import dataclass, field

from .base_rule import BaseRule
from .models.rule_result import RuleResult


@dataclass(slots=True)
class RuleEngine:
    """
    Executes registered knowledge analysis rules.

    RuleEngine is responsible for orchestration only.
    It does not create knowledge and does not modify project state.
    """

    rules: list[BaseRule] = field(default_factory=list)

    def register(self, rule: BaseRule) -> None:
        """
        Register a new rule.
        """

        self.rules.append(rule)

    def execute(self, context: object) -> tuple[RuleResult, ...]:
        """
        Execute all registered rules.

        A failed rule must not stop execution of other rules.
        """

        results: list[RuleResult] = []

        for rule in self.rules:
            try:
                result = rule.evaluate(context)
            except Exception as exc:
                result = RuleResult(
                    rule_name=rule.name,
                    executed=False,
                    error=str(exc),
                )

            results.append(result)

        return tuple(results)
