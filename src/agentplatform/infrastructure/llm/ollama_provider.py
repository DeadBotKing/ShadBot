"""
ShadBot Agent Platform

Ollama LLM provider.
"""

from __future__ import annotations

import requests

from agentplatform.application.llm import LLMProvider


class OllamaProvider(LLMProvider):
    """
    Ollama implementation of LLM provider.
    """

    def __init__(
        self,
        model: str = "qwen3-coder-next:latest",
        endpoint: str = "http://localhost:11434/api/generate",
        context_size: int = 8192,
        num_threads: int = 8,
        keep_alive: str = "5m",
    ) -> None:
        self._model = model
        self._endpoint = endpoint
        self._context_size = context_size
        self._num_threads = num_threads
        self._keep_alive = keep_alive

    def generate(
        self,
        prompt: str,
    ) -> str:
        """
        Generate response using Ollama.
        """

        response = requests.post(
            self._endpoint,
            json={
                "model": self._model,
                "prompt": prompt,
                "stream": False,
                "keep_alive": self._keep_alive,
                "options": {
                    "num_ctx": self._context_size,
                    "num_thread": self._num_threads,
                },
            },
            timeout=600,
        )

        response.raise_for_status()

        data = response.json()

        return str(
            data.get(
                "response",
                "",
            ),
        )
