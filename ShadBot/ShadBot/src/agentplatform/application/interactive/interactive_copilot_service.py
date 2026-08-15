"""
ShadBot Agent Platform

Interactive Co-Pilot Service.
"""

from __future__ import annotations

from dataclasses import dataclass
from uuid import UUID, uuid4
from agentplatform.domain.interactive import (
    InteractiveActionType,
    InteractiveCoPilotSession,
    InteractiveMessage,
)
from .conversational_intent_detector import ConversationalIntent, ConversationalIntentDetector
from .interactive_feedback_handler import InteractiveFeedbackHandler


@dataclass(frozen=True, slots=True)
class InteractiveResponsePackage:
    session: InteractiveCoPilotSession
    reply_message: InteractiveMessage
    task_created: bool
    task_title: str | None
    deterministic_gate_passed: bool


class InteractiveCoPilotService:
    """
    Orchestrates interactive conversational turns, intent detection, task generation, and co-pilot replies.
    """

    def __init__(
        self,
        detector: ConversationalIntentDetector | None = None,
        handler: InteractiveFeedbackHandler | None = None,
    ) -> None:
        self.detector = detector or ConversationalIntentDetector()
        self.handler = handler or InteractiveFeedbackHandler()
        self._sessions: dict[UUID, InteractiveCoPilotSession] = {}

    def get_or_create_session(self, project_id: UUID, project_name: str) -> InteractiveCoPilotSession:
        if project_id not in self._sessions:
            sess = InteractiveCoPilotSession(
                session_id=uuid4(),
                project_id=project_id,
                project_name=project_name,
            )
            self._sessions[project_id] = sess
        return self._sessions[project_id]

    def process_turn(self, project_id: UUID, project_name: str, user_text: str) -> InteractiveResponsePackage:
        sess = self.get_or_create_session(project_id, project_name)
        user_msg = InteractiveMessage(
            message_id=uuid4(),
            sender="user",
            text=user_text,
            action_type="user_input",
        )
        intent = self.detector.detect(user_text)
        task, summary = self.handler.handle_feedback(intent)

        reply_text = ""
        if task:
            reply_text = f"درخواست شما ({intent.action_type.value}) دریافت شد. تسک «{task.title}» ساخته شد و ایجنت‌های تخصصی در حال اصلاح کد هستند..."
        else:
            reply_text = f"توضیح سیستم: درخواست شما بررسی شد. {summary}"

        bot_msg = InteractiveMessage(
            message_id=uuid4(),
            sender="shadbot",
            text=reply_text,
            action_type=intent.action_type.value,
            target_file=intent.target_file,
        )

        new_messages = sess.messages + (user_msg, bot_msg)
        updated_sess = InteractiveCoPilotSession(
            session_id=sess.session_id,
            project_id=sess.project_id,
            project_name=sess.project_name,
            messages=new_messages,
            created_at=sess.created_at,
        )
        self._sessions[project_id] = updated_sess

        return InteractiveResponsePackage(
            session=updated_sess,
            reply_message=bot_msg,
            task_created=(task is not None),
            task_title=task.title if task else None,
            deterministic_gate_passed=True,
        )
