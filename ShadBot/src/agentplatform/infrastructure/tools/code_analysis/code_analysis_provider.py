"""
ShadBot Agent Platform

Code Analysis Provider
"""

from __future__ import annotations

from dataclasses import dataclass

from .ast_analyzer import ASTAnalyzer
from .complexity_analyzer import ComplexityAnalyzer
from .dependency_analyzer import DependencyAnalyzer
from .import_analyzer import ImportAnalyzer
from .language_detector import LanguageDetector
from .source_analyzer import SourceAnalyzer
from .symbol_extractor import SymbolExtractor


@dataclass(slots=True)
class CodeAnalysisToolProvider:
    """
    Provides code analysis tools.
    """

    source: SourceAnalyzer
    language: LanguageDetector
    imports: ImportAnalyzer
    symbols: SymbolExtractor
    ast: ASTAnalyzer
    complexity: ComplexityAnalyzer
    dependencies: DependencyAnalyzer

    @classmethod
    def create(
        cls,
    ) -> "CodeAnalysisToolProvider":

        return cls(
            source=SourceAnalyzer(),
            language=LanguageDetector(),
            imports=ImportAnalyzer(),
            symbols=SymbolExtractor(),
            ast=ASTAnalyzer(),
            complexity=ComplexityAnalyzer(),
            dependencies=DependencyAnalyzer(),
        )
