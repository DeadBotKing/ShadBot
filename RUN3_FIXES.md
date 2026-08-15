# اجرای سوم — نتیجه و سه اصلاح جدید

مخزن: `963ecd3` («Agent Code 3») · سوئیت: **۲۶۴ passed + ۱ skipped**

---

## کیفیت کد جهش کرد

اصلاح پرامپت per-file دقیقاً همان کاری را کرد که انتظار داشتیم:

| معیار | اجرای ۲ | اجرای ۳ |
|---|---|---|
| طول پاسخ‌ها | `1746` × ۸ بار | **۱۱ پاسخ، همه متفاوت** (۸۵۶ تا ۳۱۴۳) |
| type annotation | **۰٪** | **۸۱٪** (۳۱ از ۳۸ تابع) |
| `@dataclass(frozen=True)` | **۰** | **۸** |
| بدنه‌ی `pass` | ۳۴٪ | **۷٪** |
| docstring | ۱ فایل | **۴۵ مورد** |
| خط کد | ۳۲ | **۵۳۸** |
| فایل یکتا | ۶/۶ | **۱۰/۱۰** |
| ساختار | تخت | **۱۱ ماژول در ۷ پکیج با `__init__.py`** |

معماری هم درست است: `AgentOrchestrator` وابستگی‌هایش را با تزریق سازنده
می‌گیرد، دامنه immutable است، و `[PASS] architecture` واقعی است.

---

## اما ۵ ماژول import نشدند — سه علت

### باگ P: پیشوند `src.` در importها

هر ۵ خطا یک ریشه داشتند:

```
from src.agentplatform.domain.agents.agent_role import AgentRole
→ ModuleNotFoundError: No module named 'src.agentplatform.domain.agents'
```

`src/` روی `sys.path` است، پس بخشی از نام پکیج نیست. **این تقصیر من بود:**
در پرامپت مسیر فایل `src/agentplatform/...` را می‌دادم و مدل همان را در
import تکرار می‌کرد.

**دو لایه اصلاح:**

۱. پرامپت حالا مسیر import را صریح می‌گوید:
```
THIS MODULE'S IMPORT PATH:
agentplatform.domain.agents.agent_role
(the 'src/' directory is the source root and is NEVER part of an import
statement - never write "from src.something import X")
```
فایل‌های همسایه هم به‌صورت مسیر نقطه‌ای نمایش داده می‌شوند، نه مسیر فایل.

۲. `ModuleSplitter.strip_source_root_imports()` — چون مدل‌های کوچک دستور را
نادیده می‌گیرند، خروجی به‌صورت قطعی تعمیر می‌شود. نام‌های مشروع مثل
`source_control` یا `srcutils` دست‌نخورده می‌مانند.

### باگ Q: فایل برنامه‌ریزی‌شده هرگز نوشته نشد

`agent_role.py` در نقشه بود، ولی مدل `AgentRole` را داخل `agent_contract.py`
نوشت. نتیجه: فایل وجود نداشت و ۵ ماژول به آن وابسته شکستند.

حالا `CodeGenerationService` بررسی می‌کند فایل درخواستی واقعاً نوشته شده یا
نه. اگر نه، دنبال همان نماد در فایل‌های نوشته‌شده می‌گردد و یک shim
re-export می‌سازد:

```python
"""Re-export of AgentRole."""

from agentplatform.domain.contracts.agent_contract import AgentRole

__all__ = ["AgentRole"]
```

اگر نماد پیدا نشود، shim صریحاً `NotImplementedError` می‌دهد — نه یک فایل
خالی که گیت را فریب بدهد.

### باگ R: چرخه‌ی import با پیام گمراه‌کننده

بعد از رفع دو مورد بالا، خطای واقعی ظاهر شد: `agent_orchestrator` از
`platform_service` import می‌کند و برعکس. پیام خام
`cannot import name 'AgentOrchestrator'` آدم را دنبال نمادی می‌فرستد که
اتفاقاً موجود است.

حالا گیت می‌گوید: `CIRCULAR IMPORT (or missing symbol): ...`

و پرامپت قانون صریح گرفت:
> NEVER create a circular import: if module A imports B, then B must not
> import A. Depend downwards only (entry point -> application -> domain).

**این نقص واقعی طراحی مدل است، نه باگ ابزار** — و درست است که گیت FAIL بدهد.

---

## اصلاحات قبلی همه کار کردند

- `[QUALITY GATE TARGET]` مسیر درست را نشان داد
- `[CODE GENERATION] Created N missing __init__.py` — ۱۲ فایل ساخته شد
- `smoke_run` شکست را گرفت: `run.py: exited with code 1`
- `run.py` جدید واقعاً ۵ ماژول شکسته را گزارش کرد (نسخه‌ی قدیمی
  «operational» می‌گفت و `exit=0`)

---

## انتظار از اجرای بعدی

با باگ P و Q رفع‌شده، آن ۵ ماژول باید import شوند. باقی‌مانده احتمالاً
چرخه‌ی import است که حالا هم در پرامپت ممنوع شده و هم اگر رخ دهد با نام
درست گزارش می‌شود.
