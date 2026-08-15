"""
ShadBot Agent Platform

Conversational Intent Detector service.
"""

from __future__ import annotations

import re
from dataclasses import dataclass
from typing import Any
from agentplatform.domain.interactive import InteractiveActionType


@dataclass(frozen=True, slots=True)
class ConversationalIntent:
    action_type: InteractiveActionType
    target_file: str | None
    clean_instruction: str
    confidence: float


class ConversationalIntentDetector:
    """
    Analyzes natural language human input to detect co-pilot intent and target files.
    """

    def detect(self, user_text: str) -> ConversationalIntent:
        text_lower = user_text.lower()

        pattern = r"['\"`]?([a-zA-Z0-9_/]+\.(?:py|md|yaml|yml|json|txt))['\"`]?"
        match = re.search(pattern, user_text)
        target_file = match.group(1) if match else None

        if any(w in text_lower for w in ("مشکل", "باگ", "خطا", "ارور", "fix", "bug", "error", "issue", "اصلاح")):
            action = InteractiveActionType.BUG_FIX
        elif any(w in text_lower for w in ("اضافه", "add", "new", "feature", "قابلیت", "اندیکاتور")):
            action = InteractiveActionType.FEATURE_ADDITION
        elif any(w in text_lower for w in ("بهتر", "سرعت", "بهینه", "fast", "optimiz", "speed", "performance")):
            action = InteractiveActionType.OPTIMIZATION
        elif any(w in text_lower for w in ("توضیح", "چرا", "چطور", "explain", "how", "why")):
            action = InteractiveActionType.EXPLANATION
        elif any(w in text_lower for w in ("تمیز", "refactor", "ساختار")):
            action = InteractiveActionType.REFACTORING
        else:
            action = InteractiveActionType.GENERAL_CHAT

        return ConversationalIntent(
            action_type=action,
            target_file=target_file,
            clean_instruction=user_text.strip(),
            confidence=0.92,
        )
