"""
ShadBot Project Intelligence

Knowledge Rule Engine
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Generic, TypeVar

from projectintelligence.application.knowledge.rules.base_rule import (
    BaseRule,
)

TInput = TypeVar("TInput")
TOutput = TypeVar("TOutput")


@dataclass(slots=True)
class RuleEngine(Generic[TInput, TOutput]):
    """
    Executes a collection of knowledge rules.
    """

    rules: tuple[BaseRule[TInput, TOutput], ...]

    def execute(
        self,
        source: TInput,
    ) -> tuple[TOutput, ...]:
        """
        Execute all applicable rules.
        """

        results: list[TOutput] = []

        for rule in self.rules:
            if rule.applies_to(source):
                results.append(
                    rule.execute(source),
                )

        return tuple(results)