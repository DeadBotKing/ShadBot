# ShadBot — گزارش رفع باگ

**تاریخ:** ۲۰۲۶-۰۸-۱۵
**پایه:** کامیت `8ad310c`
**وضعیت تست:** ۲۲۱ پاس / ۰ شکست / ۰ هنگ (قبل: ۲۱۱ پاس، ولی بخشی از آن‌ها بی‌معنا بودند)

---

## خلاصه

پنج مشکل رفع شد. سه‌تای اول از جنس **«کد وانمود می‌کرد کار می‌کند»** بودند — یعنی تست سبز می‌دادند بدون اینکه چیزی واقعاً بررسی شود. این خطرناک‌ترین نوع باگ است چون اعتماد کاذب می‌سازد.

| # | مشکل | شدت | وضعیت |
|---|------|-----|-------|
| ۱ | Quality Gate همیشه PASS برمی‌گرداند | 🔴 بحرانی | رفع شد |
| ۲ | LLM کد هاردکد به‌جای تولید واقعی | 🔴 بحرانی | رفع شد |
| ۳ | `FullIntegrationVerifier` بدون بررسی True می‌داد | 🟠 بالا | رفع شد |
| ۴ | فورک‌بمب pytest (هنگ سیستم) | 🟠 بالا | تکمیل شد |
| ۵ | ۸ خطای `undefined name 'Any'` + حلقه چاپ خراب | 🟡 متوسط | رفع شد |

---

## ۱. Quality Gate تقلبی بود 🔴

**فایل:** `src/agentplatform/application/quality_gate/validators.py`

### قبل
هیچ ابزاری اجرا نمی‌شد. همه‌ی validatorها بدون توجه به وضعیت کد `True` برمی‌گرداندند:

```python
def validate(self, project_path: str) -> CheckResult:
    if os.environ.get("PYTEST_CURRENT_TEST"):
        return CheckResult("ruff", True, "Simulated ruff lint validation passed.", 1.0)
    return CheckResult("ruff", True, "Linting verified.", 1.0)   # ruff هرگز صدا نمی‌شد
```

این مستقیماً **Rule 12** و **Rule 27** خودتان را نقض می‌کرد و دلیل ریشه‌ای این بود که گزارش `V1.0_ENTERPRISE_RELEASE_REPORT.md` ادعای «۱۰۰٪ کامل» می‌کرد.

### بعد
- `ruff` / `black` / `mypy` / `pytest` واقعاً به‌صورت زیرپروسه اجرا می‌شوند، با timeout و بدون `shell=True`
- `SecurityValidator` یک اسکنر AST واقعی است: `eval`/`exec`/`compile`، `shell=True` و سکرت‌های هاردکد را پیدا می‌کند
- `ArchitectureValidator` واقعاً جهت وابستگی Clean Architecture را با تحلیل AST بررسی می‌کند
- `SyntaxValidator` جدید اضافه شد (بدون وابستگی خارجی، هرگز skip نمی‌شود)

### مهم‌ترین تغییر مفهومی: تفکیک SKIP از PASS

فیلد `skipped` به `CheckResult` اضافه شد. اگر ابزاری نصب نباشد، نتیجه **skipped** است نه pass — و:

```python
approved = bool(executed) and all(check.passed for check in executed)
```

یعنی گیتی که هیچ چک اجرا نکرده، **هرگز approved نمی‌شود**. قبلاً چنین گیتی «قبول» اعلام می‌شد.

### نتیجه واقعی روی خود ShadBot
گیت جدید بلافاصله مشکلات واقعی پیدا کرد که نسخه قلابی پنهان می‌کرد:

```
syntax         passed=True   All 1094 Python file(s) parse successfully.
security       passed=False  16 security finding(s)
architecture   passed=False  23 dependency-direction violation(s)
```

نمونه نقض معماری (نقض Rule 1 و Rule 3):
```
application/bootstrap/project_intelligence_bootstrap.py:200:
    application layer imports 'projectintelligence.infrastructure.filesystem.directory_walker'
```

> ⚠️ این ۲۳ مورد را عمداً رفع نکردم — اصلاحشان یعنی بازطراحی composition root با تزریق وابستگی، که تصمیم معماری شماست نه من. حالا حداقل **دیده می‌شوند**.

---

## ۲. LLM کد هاردکد تحویل می‌داد 🔴

**فایل:** `src/agentplatform/infrastructure/llm/ollama_provider.py`

### قبل
تابع `_get_fallback_response` حدود **۱۶۱ خط کد آماده** داشت — پیاده‌سازی کامل SMA/EMA/RSI، کلاس `AgentRole`، `AgentContract` — که وقتی Ollama در دسترس نبود تحویل می‌داد:

```python
if "indicator" in lower or "sma" in lower or "rsi" in lower:
    return '''def calculate_sma(prices, period): ...'''   # ۱۰۰+ خط کد از پیش نوشته
```

**چرا خطرناک بود:** تست‌ها سبز می‌شدند و فایل تولید می‌شد، ولی هیچ ربطی به کار مدل نداشت. عملاً غیرممکن بود بفهمید پایپ‌لاین واقعاً کار می‌کند یا فقط متن ثابت پس می‌دهد.

### بعد
هر ۱۶۱ خط حذف شد و جای آن یک stub صادق نشست:

```python
STUB_RESPONSE_MARKER = "# [SHADBOT-STUB-NO-LLM]"

def _stub_response(self, prompt: str) -> str:
    digest = hashlib.sha256(prompt.encode()).hexdigest()[:12]
    return (
        f"{STUB_RESPONSE_MARKER}\n"
        f"# prompt_sha256={digest} prompt_chars={len(prompt)}\n"
        f"raise NotImplementedError('ShadBot stub output: no LLM backend was available.')\n"
    )
```

خروجی حالا **خودش را لو می‌دهد**: هم مارکر دارد، هم اگر اجرا شود `NotImplementedError` می‌دهد. غیرممکن است اشتباهی به‌عنوان کد واقعی رد شود.

همچنین `except Exception` به `except requests.RequestException` و `except ValueError` تفکیک شد (Rule 18).

---

## ۳. تأییدکننده یکپارچگی دروغ می‌گفت 🟠

**فایل:** `src/agentplatform/application/release/integration_verifier.py`

### قبل
```python
def verify_all(self) -> IntegrationVerificationReport:
    return IntegrationVerificationReport(
        all_systems_operational=True,        # بدون هیچ بررسی‌ای
        verified_phases=tuple(range(1, 13)),
        status_summary="Phases 1 through 12 fully integrated and operational.",
    )
```

### بعد
هر ۱۲ فاز با import واقعی probe می‌شود:

```python
PHASE_PROBES = {
    5:  ("Brain Orchestrator",       "agentplatform.application.brain"),
    9:  ("Quality Gate System",      "agentplatform.application.quality_gate"),
    12: ("Production Freeze",        "agentplatform.application.release"),
    ...
}
```

اگر فازی import نشود، در `failed_phases` و `failures` با دلیل دقیق گزارش می‌شود. خبر خوب: هر ۱۲ فاز واقعاً import می‌شوند — یعنی ادعا درست بود، ولی حالا **اثبات‌شده** است نه ادعاشده.

---

## ۴. فورک‌بمب pytest 🟠

**فایل‌ها:** `infrastructure/tools/test_runner.py`, `infrastructure/tools/quality_validator.py`

همان چیزی که در بررسی قبلی سندباکس من را کشت (load average به ۱۰.۹۸ رسید). شما گارد `PYTEST_CURRENT_TEST` را در `test_runner.py` اضافه کرده بودید، ولی دو سوراخ باقی بود:

1. **`quality_validator.py` گارد نداشت** و `pytest` را با `shell=True` صدا می‌زد
2. **هیچ‌کدام timeout نداشتند** — گارد جلوی recursion را می‌گیرد ولی نه جلوی هنگ

### تغییرات
- گارد recursion به `QualityValidator` هم اضافه شد
- `shell=True` → `shell=False` با آرگومان لیستی (رفع تزریق شل)
- `timeout=600` (قابل تنظیم با `SHADBOT_SUBPROCESS_TIMEOUT`) روی همه زیرپروسه‌ها
- کد خروج ۵ pytest («تستی پیدا نشد») دیگر شکست حساب نمی‌شود
- **مهم:** حالت nested دیگر PASS قلابی نمی‌دهد، بلکه `skipped=True` برمی‌گرداند

---

## ۵. خطاهای کوچک‌تر 🟡

**۸ خطای `undefined name 'Any'`** در ۴ فایل:
```
application/brain/agent_brain.py                       (۳ مورد)
application/brain/memory_flow/retrieval/memory_retriever.py
application/planning/planner.py                        (۲ مورد)
infrastructure/memory/in_memory_memory_repository.py   (۲ مورد)
```
`from __future__ import annotations` این‌ها را در زمان اجرا پنهان می‌کرد، ولی `mypy` و هر چیزی که `get_type_hints()` صدا بزند می‌شکست. `from typing import Any` اضافه شد.

**حلقه چاپ خراب در `run_agent.py`:** حلقه سه متغیر می‌ساخت و هیچ‌کدام را چاپ نمی‌کرد — گزارش پایانی همیشه خالی بود:
```python
for index, result in enumerate(results, start=1):
    elapsed = ...; agent_name = ...; status_str = ...   # هیچ print ی نبود
print("=" * 75)
```
رفع شد + `main()` حالا exit code برمی‌گرداند (`1` در صورت شکست) تا CI بتواند تشخیص دهد.

---

## تست‌ها

تست‌های قدیمی Quality Gate رفتار دروغین را **تثبیت** می‌کردند:
```python
assert PytestValidator().validate(".").passed is True   # فقط چون هاردکد بود
assert rep.overall_score == 1.0
```

این‌ها با ۱۶ تست معنادار جایگزین شدند که روی پروژه‌های واقعی روی دیسک کار می‌کنند:

| تست | چه چیزی را اثبات می‌کند |
|-----|-------------------------|
| `test_syntax_validator_detects_broken_code` | کد خراب واقعاً FAIL می‌شود |
| `test_security_validator_flags_dangerous_call` | `eval()` تشخیص داده می‌شود |
| `test_security_validator_flags_hardcoded_secret` | سکرت تشخیص داده می‌شود |
| `test_architecture_validator_detects_layer_violation` | نقض لایه گرفته می‌شود |
| `test_nested_pytest_is_skipped_not_passed` | **skip ≠ pass** |
| `test_service_never_approves_when_everything_skipped` | گیت خالی approve نمی‌شود |
| `test_deterministic_gate_fails_broken_project` | گیت روی پروژه خراب FAIL می‌دهد |

هر تست از fixtureهای `tmp_path` استفاده می‌کند و پروژه‌های واقعی (سالم و عمداً خراب) روی دیسک می‌سازد.

---

## کارهای باقی‌مانده (تصمیم شماست)

۱. **۲۳ نقض Clean Architecture** — عمدتاً composition rootها که مستقیم از infrastructure import می‌کنند. رفعش نیاز به تزریق وابستگی دارد.

۲. **۵ مورد `shell=True`** در `code_execution_adapter`, `experiment_executor_adapter`, `package_manager_adapter`, `static_analyzer_adapter`, `terminal_tool` — همان الگویی که در `quality_validator` رفع کردم.

۳. **`requires-python = ">=3.14"`** در `pyproject.toml` — پایتون ۳.۱۴ هنوز خیلی جدید است و `pip install -e .` را می‌شکند. اگر عمدی نیست، `>=3.11` منطقی‌تر است.

۴. **گزارش‌های داخل `ShadBotWorkspace/`** هنوز ادعای «۱۰۰٪ کامل / V1.0 منتشر شد» دارند. حالا که گیت واقعی داریم، بهتر است این‌ها بازتولید شوند.

۵. **کد تولیدشده توسط ایجنت** در `ShadBotWorkspace/ShadBotCore_BuiltByAgent/` هنوز اجراشدنی نیست: چند فایل در یک فایل چسبیده‌اند، ایمپورت‌های شکسته، بدنه‌های `pass`. این مشکل prompt/parsing لایه تولید است، نه گیت.

---

## پیوست — باگ H: کرش انکودینگ در ویندوز (این باگ از خود من بود)

**علامت:** بعد از اینکه هر ۹ ایجنت SUCCESS شدند، خودِ گیت کیفیت کرش کرد:

```
UnicodeDecodeError: 'charmap' codec can't decode byte 0x81 in position 5132
  (Thread-57 _readerthread, cp1252)
→ AttributeError: 'NoneType' object has no attribute 'strip'
   validators.py:98  _combine_output
```

**ریشه:** `subprocess.run(..., text=True)` بدون پارامتر `encoding=`، از کدک پیش‌فرض
سیستم‌عامل استفاده می‌کند. روی لینوکس این UTF-8 است و مشکلی پیش نمی‌آید، اما روی
ویندوز فارسی **cp1252** است. وقتی `ruff` خروجی UTF-8 تولید می‌کند (مثلاً چون کد شما
شامل متن فارسی، emoji یا کاراکتر `—` است)، ترد خواننده‌ی subprocess با
`UnicodeDecodeError` می‌میرد. نتیجه این است که `result.stdout` به‌جای رشته `None`
می‌شود — به همین دلیل خطایی که در نهایت می‌بینید `AttributeError` است نه خطای
انکودینگ، و این گمراه‌کننده است.

**اصلاح — دو لایه دفاعی:**

۱. **علت اصلی:** به تمام ۱۴ فراخوانی subprocess در ۱۲ فایل پارامترهای
   `encoding="utf-8", errors="replace"` اضافه شد. `errors="replace"` تضمین می‌کند
   حتی بایت واقعاً نامعتبر هم به‌جای کرش، به `` تبدیل شود.

۲. **دفاع در عمق:** `_combine_output` حالا امضای `stdout: str | None,
   stderr: str | None` دارد و قبل از `.strip()` مقدار `None` را بررسی می‌کند.
   همین کار برای `test_runner.py` هم انجام شد (`process.stdout or ""`).

**۳ تست رگرسیون اضافه شد:**

| تست | چه چیزی را اثبات می‌کند |
|-----|-------------------------|
| `test_combine_output_survives_none_streams` | با `stdout=None` دیگر `AttributeError` نمی‌دهد |
| `test_subprocess_calls_pin_utf8_encoding` | هیچ `text=True` بدون `encoding="utf-8"` باقی نمانده |
| `test_validator_handles_unicode_tool_output` | پروژه‌ای با متن فارسی از گیت رد می‌شود |

**تأیید عملی:** `ruff` نصب شد و روی یک پروژه‌ی آزمایشی حاوی فارسی، emoji و
`€ ± § ° ÿ` اجرا شد. خروجی کامل و بدون کرش decode شد.

> **قانون برای آینده:** هر فراخوانی جدید `subprocess` در این پروژه **باید**
> `encoding="utf-8", errors="replace"` داشته باشد. تست
> `test_subprocess_calls_pin_utf8_encoding` این قانون را نگه می‌دارد.

**وضعیت سوئیت:** ۲۲۳ passed + ۱ skipped (۲۲۱ قبلی + ۳ تست جدید).
