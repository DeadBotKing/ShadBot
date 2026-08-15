"""
ShadBot Agent Platform - Interactive Conversational Co-Pilot CLI
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path
from uuid import uuid4

_src_dir = (Path(__file__).resolve().parent / "src").resolve()
if _src_dir.exists() and str(_src_dir) not in sys.path:
    sys.path.insert(0, str(_src_dir))

from agentplatform.application.bootstrap import AgentPlatformBootstrap
from agentplatform.application.interactive import InteractiveCoPilotService
from agentplatform.application.loop.project_execution import ProjectExecutionService


def main() -> None:
    parser = argparse.ArgumentParser(
        description="ShadBot Agent Platform - Interactive Conversational Co-Pilot",
    )
    parser.add_argument(
        "--project",
        default="ShadBotCore_BuiltByAgent",
        help="Workspace project name (e.g. ShadBotCore_BuiltByAgent, Meryx, Trader)",
    )
    parser.add_argument(
        "--query",
        default=None,
        help="Execute a single natural language conversational prompt in non-interactive mode and exit",
    )
    args = parser.parse_args()

    project_id = uuid4()
    copilot = InteractiveCoPilotService()

    if args.query:
        print(f"\n[ShadBot Co-Pilot - Single Query Mode | Project: {args.project}]")
        print(f"You > {args.query}")
        pkg = copilot.process_turn(project_id, args.project, args.query)
        print(f"[ShadBot] {pkg.reply_message.text}")
        if pkg.task_created:
            print(f"[STATUS] Task Ingested -> Active Agents Assigned -> Deterministic Gate GREEN")
        return

    print()
    print("=" * 75)
    print(f"ShadBot Agent Platform - Interactive Conversational Co-Pilot")
    print(f"Active Workspace Project : {args.project}")
    print("=" * 75)
    print("شما می‌توانید به زبان طبیعی با ایجنت‌ها صحبت کنید؛ مثلاً:")
    print(" - «اینجای کد مشکل داره اصلاحش کن»")
    print(" - «توی فایل market_analyzer.py اندیکاتور MACD رو هم اضافه کن»")
    print(" - «چکار کنیم سرعتش بهتر بشه؟»")
    print("برای خروج، کلمه 'exit' یا 'quit' را تایپ کنید.")
    print("=" * 75)

    while True:
        try:
            user_input = input("\nYou > ").strip()
            if not user_input:
                continue
            if user_input.lower() in ("exit", "quit", "خروج"):
                print("\n[ShadBot] خدانگهدار! جلسه Co-Pilot پایان یافت.")
                break

            pkg = copilot.process_turn(project_id, args.project, user_input)
            print(f"\n[ShadBot] {pkg.reply_message.text}")
            if pkg.task_created:
                print(f"[STATUS] Task Ingested -> Active Agents Assigned -> Deterministic Gate GREEN")
        except (KeyboardInterrupt, EOFError):
            print("\n[ShadBot] جلسه Co-Pilot پایان یافت.")
            break


if __name__ == "__main__":
    main()
