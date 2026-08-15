"""
ShadBot Agent Platform

Unit tests for Interactive Conversational Co-Pilot.
"""

from __future__ import annotations

from uuid import uuid4
from agentplatform.application.interactive import (
    ConversationalIntentDetector,
    InteractiveCoPilotService,
    InteractiveFeedbackHandler,
)
from agentplatform.domain.interactive import InteractiveActionType


def test_conversational_intent_detector_identifies_bugfix() -> None:
    detector = ConversationalIntentDetector()
    intent = detector.detect("توی فایل src/main.py این باگ رو اصلاح کن")
    assert intent.action_type == InteractiveActionType.BUG_FIX
    assert intent.target_file == "src/main.py"


def test_conversational_intent_detector_identifies_feature_addition() -> None:
    detector = ConversationalIntentDetector()
    intent = detector.detect("توی فایل market_analyzer.py اندیکاتور MACD رو هم اضافه کن")
    assert intent.action_type == InteractiveActionType.FEATURE_ADDITION
    assert intent.target_file == "market_analyzer.py"


def test_interactive_feedback_handler_creates_task() -> None:
    detector = ConversationalIntentDetector()
    intent = detector.detect("اینجای کد مشکل داره اصلاحش کن")
    task, summary = InteractiveFeedbackHandler().handle_feedback(intent)
    assert task is not None
    assert "Interactive Co-Pilot" in task.title
    assert "bug_fix" in str(task.title).lower()


def test_interactive_copilot_service_executes_chat() -> None:
    service = InteractiveCoPilotService()
    pid = uuid4()
    pkg = service.process_turn(pid, "Meryx", "چکار کنیم سرعتش بهتر بشه؟")
    assert len(pkg.session.messages) == 2
    assert pkg.session.messages[0].sender == "user"
    assert pkg.session.messages[1].sender == "shadbot"
    assert pkg.deterministic_gate_passed is True
