# تحلیل خروجی ایجنت‌ها — ShadBotCore_BuiltByAgent

تاریخ: ۲۰۲۶-۰۸-۱۵ · مخزن: `DeadBotKing/ShadBot` @ `1829066` («Agent's Make Codes»)

---

## حکم کوتاه

**نه. ایجنت‌ها آنچه خواسته شده بود را نساختند.**

خروجی ۱۴ فایل پایتون است که syntax درستی دارند و به همین دلیل گیت `[PASS] syntax` می‌دهد،
اما **هیچ‌کدام قابل import نیستند**، **۷ تای‌شان محتوای کاملاً یکسان دارند**، و هیچ‌کدام
ربطی به نامی که روی فایل است ندارند.

مهم‌تر از آن: **حکم گیت که دیدید مربوط به این پروژه نبود.** گیت به‌دلیل یک باگ مسیر،
کل پلتفرم ShadBot را validate کرد، نه پروژه‌ی تولیدشده را.

---

## ۱. چه چیزی خواسته شده بود؟

از `tasks/backlog.yaml`:

> Implement the complete ShadBot Agent Platform in `src/agentplatform/` from Phase 1 through Phase 12.
> 1. Domain Layer: immutable domain contracts and entities
> 2. Application Layer: stateless application services
> 3. Quality Gate: Deterministic Quality Gate validation to ensure 100% GREEN

یعنی: پلتفرم باید **خودش را بازتولید کند** (self-hosting / meta-agent).

---

## ۲. چه چیزی واقعاً ساخته شد؟

| معیار | مقدار |
|---|---|
| فایل پایتون تولیدشده | ۱۴ |
| خط کد مؤثر | ۷۴۲ |
| **محتوای یکتا** | **۶ از ۱۴** |
| فایل قابل import | **۰ از ۱۴** |
| توابع خالی (`pass`) | **۳۴ از ۹۹ = ۳۴٪** |
| فایل `__init__.py` | **۰** |
| تست | **۰** |
| فازهای ۱ تا ۱۲ | هیچ‌کدام |

### ۲.۱ هفت فایل، یک محتوا

```
8c96c95ee19433dd3c50b09d8bea1d2c  application/orchestration/agent_orchestrator.py
8c96c95ee19433dd3c50b09d8bea1d2c  application/platform/platform_service.py
8c96c95ee19433dd3c50b09d8bea1d2c  application/quality_gate/quality_gate_service.py
8c96c95ee19433dd3c50b09d8bea1d2c  domain/agents/agent_role.py
8c96c95ee19433dd3c50b09d8bea1d2c  domain/contracts/agent_contract.py
8c96c95ee19433dd3c50b09d8bea1d2c  infrastructure/agents/engineer_agent.py
8c96c95ee19433dd3c50b09d8bea1d2c  infrastructure/agents/project_intelligence_agent.py
```

هفت فایل با هفت نام متفاوت و بایت‌به‌بایت یکسان. این مستقیماً همان چیزی است که در
لاگ خودتان دیدید: `Length: 1485 chars` که **۶ بار** تکرار شد.

### ۲.۲ محتوای فایل‌ها ربطی به نامشان ندارد

فایل `domain/agents/agent_role.py` باید یک enum نقش باشد. محتوای واقعی‌اش:

```python
# src/agentplatform/domain/models.py
@dataclass(frozen=True)
class Agent: ...
# src/agentplatform/domain/services.py
class DomainService:
    def get_all_agents(self) -> List[Agent]:
        pass
# src/agentplatform/application/services.py
class ApplicationService: ...
# src/agentplatform/application/validation.py
class QualityGate: ...
# src/agentplatform/__init__.py
from .application.services import ApplicationService
```

**پنج ماژول مختلف در یک فایل چسبیده‌اند.** مدل خروجی چندفایلی تولید کرده
(با کامنت `# src/...` به‌عنوان جداکننده) و لایه‌ی parsing پلتفرم به‌جای تقسیم آن‌ها،
کل متن را در یک فایل ریخته است. در کل ۷۰ سرآیند `# src/...` در ۱۴ فایل وجود دارد.

### ۲.۳ هیچ‌چیز اجرا نمی‌شود

```
importable: 0/14

FAIL agentplatform.domain.agents.agent_role:
     ModuleNotFoundError: No module named 'agentplatform.domain.agents.models'
FAIL agentplatform.service:
     ModuleNotFoundError: No module named 'agentplatform.application.services'
...
```

هر ۱۴ فایل. علت روشن است: کد `from .models import Agent` را import می‌کند، اما
`models.py` هرگز به‌عنوان فایل جدا نوشته نشد — محتوایش داخل همان فایل چسبیده است.

### ۲.۴ `run.py` کاری نمی‌کند

```python
def main() -> int:
    print("Starting ShadBotCore_BuiltByAgent...")
    src_dir = Path(__file__).parent / "src"
    if src_dir.exists():
        sys.path.insert(0, str(src_dir))
    print("Project ShadBotCore_BuiltByAgent is operational.")
    return 0
```

«operational» را چاپ می‌کند بدون اینکه حتی یک ماژول را import کند. اگر import می‌کرد،
کرش می‌کرد. این یک template ثابت است، نه کد تولیدشده.

---

## ۳. باگ I — گیت پروژه‌ی اشتباه را validate می‌کند (بحرانی)

در لاگ شما:

```
[PASS] syntax: All 1094 Python file(s) parse successfully.
```

اما پروژه‌ی تولیدشده **۱۵ فایل** دارد. عدد ۱۰۹۴ تعداد فایل‌های **خود پلتفرم ShadBot** است.

### ریشه

`src/agentplatform/application/orchestration/agent_orchestrator.py` خط ۲۸۸:

```python
project_path_str = str(current_context.metadata.get("project_path", "."))
project_path = Path(project_path_str)
if not project_path.exists():
    project_path = Path(".")          # ← سقوط خاموش

det_report = self.deterministic_gate.verify_deterministic(project_path)
```

جست‌وجوی کل مخزن نشان می‌دهد **هیچ‌جا `context.metadata["project_path"]` مقداردهی نمی‌شود.**
تنها نتیجه‌ی جست‌وجو یک دیکشنری خروجی در `project_analyzer_tool.py` است که ربطی به
این metadata ندارد. پس `.get(...)` همیشه `"."` برمی‌گرداند و گیت روی دایرکتوری جاری
(یعنی `ShadBot/ShadBot/`) اجرا می‌شود.

### اثبات عملی

```
scanning ".":                 All 1200 Python file(s) parse successfully.
scanning real target:         All 15 Python file(s) parse successfully.
```

(۱۲۰۰ در محیط من چون فایل‌های اضافه دارم؛ ۱۰۹۴ در محیط شما. هر دو = کل پلتفرم.)

### پیامد

تمام حکم‌هایی که در گیت دیدید مربوط به کد **خودِ پلتفرم** است، نه کار ایجنت‌ها:

| خروجی گیت | واقعاً درباره‌ی چیست |
|---|---|
| `[FAIL] ruff: E501 Line too long` | کد پلتفرم |
| `[FAIL] mypy: stubs not installed for "yaml"` | `backlog_task_loader.py` پلتفرم |
| `[FAIL] security: 16 finding(s) across 1094 files` | همان ۱۶ مورد `shell=True` که در FIX_REPORT مستند کردم |
| `[FAIL] architecture: 23 violation(s) across 900 files` | همان ۲۳ نقض شناخته‌شده‌ی پلتفرم |
| `[PASS] pytest` | **۲۲۳ تست خودِ پلتفرم** — پروژه‌ی تولیدشده اصلاً تست ندارد |

آن `[PASS] pytest` خطرناک‌ترین بخش است: به‌نظر می‌رسد کد ایجنت تست دارد و پاس می‌شود،
در حالی که تست‌های خود ShadBot اجرا شده‌اند.

### حکم واقعی پروژه‌ی تولیدشده

وقتی گیت را دستی روی مسیر درست اجرا کردم:

```
executed=4/6 | failed=ruff | skipped=pytest,mypy
  [PASS] syntax        14 فایل parse می‌شوند
  [SKIP] pytest        پوشه‌ی tests وجود ندارد
  [FAIL] ruff
  [SKIP] mypy          نصب نیست
  [PASS] security
  [PASS] architecture
```

توجه کنید `[SKIP] pytest — No tests directory` — این حقیقت است. ایجنت‌ها صفر تست نوشتند.

---

## ۴. چرا این اتفاق افتاد؟

سه علت مستقل، به ترتیب اهمیت:

**الف) پرامپت تکراری / بدون context.** شش پاسخ با طول دقیقاً `1485 chars`. مدل برای
فایل‌های مختلف عملاً یک پرامپت می‌گیرد و همان جواب کلی را می‌دهد. ایجنت نمی‌داند
دارد `agent_role.py` می‌نویسد یا `platform_service.py`.

**ب) لایه‌ی parsing خروجی چندفایلی را نمی‌شکند.** مدل درست عمل می‌کند و با
`# src/path.py` مرزها را مشخص می‌کند؛ پلتفرم این مرزها را نادیده می‌گیرد و همه را
در یک فایل می‌ریزد. رفع این مورد نسبتاً ساده است و بیشترین سود را دارد.

**ج) هیچ حلقه‌ی بازخورد اجرایی وجود ندارد.** هیچ مرحله‌ای کد تولیدشده را import
نمی‌کند. اگر می‌کرد، همان بار اول ۱۴ خطا می‌گرفت و repair loop فعال می‌شد.

**نکته‌ی مثبت:** مدل `qwen2.5-coder:7b` بد کار نکرده — dataclass های frozen، تزریق
وابستگی، و مرزبندی لایه‌ها در خروجی‌اش درست است. مشکل در orchestration است، نه مدل.

---

## ۵. سه اصلاح به‌ترتیب اولویت

**۱. باگ I را رفع کنید** (چند خط). در `agent_orchestrator.py` مسیر پروژه را از
`context.target_project.path` بگیرید و اگر وجود نداشت **خطا بدهید**، نه سقوط به `.`:

```python
project_path = Path(context.target_project.path).resolve()
if not project_path.exists():
    raise ValueError(f"target project path does not exist: {project_path}")
```

بدون این، هیچ حکمی درباره‌ی کار ایجنت‌ها قابل اعتماد نیست.

**۲. خروجی چندفایلی را تقسیم کنید.** روی `^#\s*(?:src/)?(\S+\.py)$` تقسیم کنید و هر
بلوک را در مسیر خودش بنویسید، و `__init__.py` بسازید.

**۳. یک چک import به گیت اضافه کنید.** بعد از syntax، هر ماژول را واقعاً import کنید.
این تنها راهی است که «۰ از ۱۴ قابل import» را به یک FAIL صریح تبدیل می‌کند.

پس از این سه، پرامپت را per-file کنید تا پاسخ‌های ۱۴۸۵ کاراکتری تکراری از بین بروند.

---

## ۶. جمع‌بندی

| پرسش | پاسخ |
|---|---|
| گیت درست کار می‌کند؟ | بله — کرش رفع شد، `executed=6/6` |
| گیت پروژه‌ی درست را چک می‌کند؟ | **نه** — باگ I |
| ایجنت‌ها چیزی ساختند؟ | ۷۴۲ خط، ۶ محتوای یکتا |
| آنچه خواسته شد ساخته شد؟ | **نه** — نه فاز ۱–۱۲، نه تست، نه کد اجراشدنی |
| کد تولیدشده اجرا می‌شود؟ | **نه** — ۰ از ۱۴ قابل import |
| مقصر مدل است؟ | نه — orchestration و parsing |

---
---

# پیوست — سه اصلاح انجام شد

تاریخ: ۲۰۲۶-۰۸-۱۵ · سوئیت: **۲۳۹ passed + ۱ skipped** (از ۲۲۳ قبلی، ۱۶ تست جدید)

---

## اصلاح ۱ — باگ I: گیت روی پروژه‌ی درست

**فایل‌ها:** `application/orchestration/agent_orchestrator.py`,
`application/loop/project_execution.py`

قبل:
```python
project_path_str = str(current_context.metadata.get("project_path", "."))
if not project_path.exists():
    project_path = Path(".")        # ← گیت خودِ پلتفرم را چک می‌کرد
```

بعد — متد `_resolve_target_project_path` با ترتیب اولویت صریح:

۱. `context.target_project.path` (که `run_agent.py` ست می‌کند)
۲. `metadata["project_path"]` (که حالا `project_execution.py` هم پرش می‌کند)

اگر هیچ‌کدام معتبر نبود، **`ValueError` می‌دهد** و هرگز به `.` سقوط نمی‌کند.
مسیرهایی که وجود ندارند یا فایل‌اند (نه دایرکتوری) رد می‌شوند.

**نکته‌ی مهم درباره‌ی رفتار خطا:** اولین پیاده‌سازی‌ام باعث شد ۷ تست موجود
بشکنند، چون contextهای تستی `target_project` ندارند. راه‌حل درست این نبود که
سخت‌گیری را کم کنم؛ در ارکستریتور `ValueError` گرفته می‌شود و به گزارشی تبدیل
می‌شود که **هر ۷ چک را SKIPPED** علامت می‌زند با
`UNVERIFIABLE (no target project) | executed=0/7`.

این همان اصل «skip ≠ pass» است: خط لوله‌ای که قابل راستی‌آزمایی نیست هرگز
سبز به‌نظر نمی‌رسد.

خط جدیدی که در اجرا خواهید دید:
```
[QUALITY GATE TARGET] C:\...\ShadBotWorkspace\ShadBotCore_BuiltByAgent
```
اگر این خط مسیر پروژه‌ی شما را نشان نداد، گیت هدف اشتباهی دارد.

---

## اصلاح ۲ — باگ J: تقسیم خروجی چندفایلی

**فایل جدید:** `application/generation/module_splitter.py`
**تغییر:** `application/generation/code_generation_service.py`

`ModuleSplitter` روی کامنت مسیر تقسیم می‌کند (`# src/foo/bar.py`،
`# File: ...`، `# --- ... ---`) و هر بلوک را در مسیر اعلام‌شده‌ی خودش می‌نویسد.

سه محافظ:

| محافظ | کار |
|---|---|
| `_sanitise` | مسیرهای مطلق و `..` را رد می‌کند |
| `_merge_duplicates` | مسیر تکراری را الحاق می‌کند، نه بازنویسی |
| `_propagate_shared_imports` | importهای stdlib را که مدل فقط یک‌بار بالای پاسخ نوشته، به ماژول‌های بعدی اضافه می‌کند |

آن محافظ سوم را بعد از دیدن نتیجه‌ی واقعی اضافه کردم: مدل
`from typing import List` را یک‌بار می‌نویسد و در ۴ ماژول بعدی از `List`
استفاده می‌کند. بدون این کار، تقسیم‌کردن باعث `NameError` می‌شد. فقط نام‌هایی
اضافه می‌شوند که واقعاً استفاده شده‌اند، پس import بی‌مصرف تولید نمی‌شود.
importهای نسبی (`from .models import`) هرگز منتقل نمی‌شوند چون مختص ماژول‌اند.

`CodeGenerationService` حالا `__init__.py` های گمشده را هم می‌سازد (`src/` را
به‌درستی به‌عنوان source root نه package در نظر می‌گیرد) و مسیرهای خارج از
ریشه‌ی پروژه را رد می‌کند.

**تست روی خروجی واقعی ایجنت‌ها:** فایل `agent_role.py` که ۵ ماژول چسبیده بود،
به ۵ فایل درست تقسیم شد و هر ۵ تا parse می‌شوند. با بازنویسی کل خروجی از طریق
splitter، نسبت ماژول‌های قابل import از **۰/۱۴ به ۴/۹** رسید. باقی‌مانده‌ها
خطاهای واقعی مدل‌اند (کلاسی که هرگز تعریف نشده) — و درست است که گیت آن‌ها را
FAIL کند.

---

## اصلاح ۳ — باگ K: چک import در گیت

**تغییر:** `application/quality_gate/validators.py` (کلاس `ImportValidator`),
`deterministic_quality_gate.py` (چک هفتم)

هر ماژول واقعاً import می‌شود، **در زیرفرایند جدا** — چون import کردن کد
تولیدشده دستورات سطح ماژول را اجرا می‌کند و نباید فرایند گیت را آلوده کند.
نتیجه به‌صورت JSON برمی‌گردد. timeout دارد (کد تولیدشده ممکن است سطح ماژول
block کند) و **شماره‌ی خط دقیق** را گزارش می‌دهد.

روی پروژه‌ی شما:
```
[FAIL] imports: 14/14 module(s) cannot be imported:
agentplatform/domain/agents/agent_role.py:22: ModuleNotFoundError:
    No module named 'agentplatform.domain.agents.models'
...
```

این تفاوت بین «متن پایتون معتبر است» و «کد وجود دارد».

---

## حکم گیت — قبل و بعد

| | قبل از اصلاحات | بعد |
|---|---|---|
| هدف | `ShadBot/ShadBot/` (پلتفرم) | `ShadBotWorkspace/ShadBotCore_BuiltByAgent/` |
| فایل‌های اسکن‌شده | ۱۰۹۴ | ۱۴ |
| `[PASS] pytest` | ۲۲۳ تست خود ShadBot | `[SKIP] — No tests directory` |
| چک import | وجود نداشت | `[FAIL] 14/14` |
| خلاصه | `executed=6/6 \| failed=ruff,mypy,security,architecture` | `executed=5/7 \| failed=imports,ruff \| skipped=pytest,mypy` |

حکم قبلی درباره‌ی کد **خود پلتفرم** بود. حکم جدید درباره‌ی کار **ایجنت‌ها**ست.

---

## ۱۶ تست رگرسیون

`tests/agentplatform_tests/quality_gate/test_gate_target_and_imports.py`

| گروه | مهم‌ترین تست |
|---|---|
| باگ I (۵ تست) | `test_gate_target_never_falls_back_to_cwd` |
| باگ J (۶ تست) | `test_splitter_propagates_shared_stdlib_imports`, `test_splitter_rejects_path_traversal` |
| باگ K (۵ تست) | `test_import_validator_fails_parseable_but_unimportable_code` |

---

## قدم بعدی

اصلاح ۲ فقط روی **اجرای بعدی** اثر دارد — فایل‌های موجود در
`ShadBotCore_BuiltByAgent/` هنوز خروجی قدیمی‌اند. برای دیدن اثر واقعی:

```powershell
Remove-Item -Recurse -Force ..\ShadBotWorkspace\ShadBotCore_BuiltByAgent\src
python run_agent.py --project ShadBotCore_BuiltByAgent
```

انتظار داشته باشید: خط `[QUALITY GATE TARGET]` با مسیر درست، پیام
`[CODE GENERATION] Split response into N module(s)`، و یک `[FAIL] imports`
که این بار عدد بسیار کمتری از ۱۴/۱۴ دارد.

**کاری که هنوز نکرده‌ام:** پرامپت per-file. تا وقتی ۶ پاسخ با طول دقیقاً
`1485 chars` برمی‌گردد، ایجنت نمی‌داند دارد کدام فایل را می‌نویسد. سه اصلاح
بالا خرابی را *قابل دیدن* و *قابل بازیابی* کردند، اما علت ریشه‌ای پاسخ‌های
تکراری در لایه‌ی prompt است.
