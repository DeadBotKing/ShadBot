from __future__ import annotations

from abc import ABC, abstractmethod

from .models.rule_result import RuleResult


class BaseRule(ABC):
    """
    Base contract for all knowledge analysis rules.

    Rules are responsible only for analyzing extracted project
    information and producing RuleResult objects.

    Rules must never modify ProjectKnowledge directly.
    """

    @property
    @abstractmethod
    def name(self) -> str:
        """
        Unique rule identifier.
        """

        raise NotImplementedError

    @abstractmethod
    def evaluate(self, context: object) -> RuleResult:
        """
        Execute rule analysis against provided knowledge context.

        Args:
            context:
                Input data required by the rule.

        Returns:
            RuleResult containing generated findings.
        """

        raise NotImplementedError
