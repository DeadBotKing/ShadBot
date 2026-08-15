# ShadBot — راهنمای اجرا

نسخه اصلاح‌شده. ۲۲۱ تست پاس، بدون هنگ، بدون فورک‌بمب.

---

## ۱. ساخت Venv

فایل زیپ را اکسترکت کنید و وارد پوشه `ShadBot` داخلی شوید:

```powershell
cd ShadBot\ShadBot
```

> ⚠️ دقت کنید: دو تا پوشه تودرتو به اسم `ShadBot` هست. باید داخل **دومی** باشید — جایی که `run_agent.py` و `pyproject.toml` هستند.

### ویندوز (PowerShell)

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

اگر PowerShell اجازه اجرای اسکریپت نداد:
```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```

### لینوکس / مک

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

> **نکته درباره پایتون:** فایل `pyproject.toml` روی `requires-python = ">=3.14"` تنظیم شده که خیلی سخت‌گیرانه است. برای همین از `requirements.txt` استفاده کنید و **`pip install -e .` نزنید** — لازم نیست، چون `conftest.py` خودش مسیر `src/` را اضافه می‌کند.

---

## ۲. اجرای تست‌ها (اول این را بزنید)

```powershell
python -m pytest -q
```

**انتظار:** `221 passed` در حدود ۶۰ ثانیه.

اگر این سبز شد، یعنی پلتفرم سالم است و فورک‌بمب رفع شده.

---

## ۳. تست اینکه Quality Gate واقعاً کار می‌کند

این مهم‌ترین بخش است — اثبات اینکه گیت دیگر دروغ نمی‌گوید:

```powershell
python -c "import sys; sys.path.insert(0,'src'); from agentplatform.application.quality_gate import SyntaxValidator, SecurityValidator, ArchitectureValidator; [print(f'{v.validate(\"src\").check_name:14} passed={v.validate(\"src\").passed}') for v in (SyntaxValidator(), SecurityValidator(), ArchitectureValidator())]"
```

**خروجی مورد انتظار:**
```
syntax         passed=True
security       passed=False
architecture   passed=False
```

`False`ها **درست‌اند** — گیت واقعاً ۲۳ نقض معماری و ۱۶ مورد امنیتی در خود پلتفرم پیدا می‌کند. نسخه قبلی همیشه `True` می‌داد و همین باعث شده بود گزارش «۱۰۰٪ کامل» تولید شود.

برای دیدن جزئیات:

```powershell
python -c "import sys; sys.path.insert(0,'src'); from agentplatform.application.quality_gate import ArchitectureValidator; print(ArchitectureValidator().validate('src').details[:2000])"
```

---

## ۴. اجرای خود پلتفرم

### ۴.۱ بدون Ollama (تست سریع)

```powershell
python run_agent.py --project ShadBotCore_BuiltByAgent
```

**چه اتفاقی می‌افتد:** ایجنت اول (`project_intelligence`) موفق می‌شود، ایجنت دوم (`researcher`) با پیام واضح متوقف می‌شود:

```
[ERROR] Ollama server is not running or reachable on http://localhost:11434/api/generate
[RECOVERY STRATEGY SELECTED] ABORT_EXECUTION
```

این **رفتار درست** است — قبلاً به‌جای خطا، کد هاردکد تحویل می‌داد و وانمود می‌کرد کار کرده.

خروجی حالا exit code هم برمی‌گرداند:
```powershell
echo $LASTEXITCODE    # باید 1 باشد چون شکست خورد
```

### ۴.۲ با Ollama (اجرای واقعی)

در یک ترمینال جدا:
```powershell
ollama serve
ollama pull qwen2.5-coder:7b
```

بعد در ترمینال venv:
```powershell
python run_agent.py --project ShadBotCore_BuiltByAgent
```

حالا کل پایپ‌لاین ۹ ایجنتی اجرا می‌شود:
```
project_intelligence → researcher → rnd → architect → ml_scientist
→ engineer → qa → reviewer → runtime_observer
```

پروژه‌های موجود برای تست: `ShadBotCore_BuiltByAgent` و `Meryx`

### تنظیمات اختیاری

| متغیر محیطی | پیش‌فرض | کاربرد |
|---|---|---|
| `SHADBOT_LLM_TIMEOUT` | `1800` | تایم‌اوت هر درخواست LLM (ثانیه) |
| `SHADBOT_CONTEXT_SIZE` | `8192` | اندازه context مدل |
| `SHADBOT_SUBPROCESS_TIMEOUT` | `600` | سقف زمان زیرپروسه‌ها |
| `SHADBOT_QUALITY_TOOL_TIMEOUT` | `300` | سقف زمان ابزارهای کیفیت |
| `SHADBOT_ENABLE_MODEL_ROUTING` | `0` | `1` = مدل متفاوت برای هر ایجنت |

مثال:
```powershell
$env:SHADBOT_LLM_TIMEOUT="600"
python run_agent.py --project Meryx
```

---

## ۵. چطور بفهمم واقعاً کار می‌کند یا فیک است؟

این سؤال اصلی شماست. سه تا نشانه قطعی:

### نشانه ۱ — مارکر stub
اگر در هر فایل تولیدشده این را دیدید، یعنی LLM در دسترس نبوده و خروجی واقعی نیست:
```
# [SHADBOT-STUB-NO-LLM]
```
این فایل اگر اجرا شود `NotImplementedError` می‌دهد. عمداً این‌طور طراحی شد تا هرگز اشتباهی به‌عنوان کد واقعی رد نشود.

### نشانه ۲ — گزارش Quality Gate
در خروجی اجرا دنبال این بگردید:
```
[DETERMINISTIC GATE] Status: ... | executed=4/6 | failed=... | skipped=...
  [PASS] syntax: All 12 Python file(s) parse successfully.
  [FAIL] ruff: E501 Line too long ...
  [SKIP] pytest: Nested pytest execution refused ...
```
`executed=X/6` می‌گوید واقعاً چند چک اجرا شده. اگر `executed=0` باشد، گیت **هیچ‌چیز را اثبات نکرده** و دیگر approved نمی‌شود.

### نشانه ۳ — تست بمب
مطمئن شوید فورک‌بمب برنگشته:
```powershell
python -m pytest -q tests/agentplatform_tests/bootstrap/
```
باید در چند ثانیه تمام شود. اگر بیشتر از یکی دو دقیقه طول کشید یا CPU ترکید، فوراً `Ctrl+C` بزنید و به من بگویید.

---

## ۶. اگر به مشکل خوردید

مواردی که ممکن است ببینید و **طبیعی‌اند**:

| علامت | توضیح |
|---|---|
| `researcher` شکست می‌خورد | Ollama بالا نیست — طبیعی |
| `architecture passed=False` | ۲۳ نقض واقعی که عمداً رفع نشده |
| `security passed=False` | ۱۶ مورد، بخشی false-positive از خود اسکنرها |
| `skipped=pytest` در گیت | محافظ ضدبازگشت — عمدی |

مواردی که **طبیعی نیستند** و باید بگویید:
- تست‌ها بیشتر از ۲ دقیقه طول بکشند
- CPU به ۱۰۰٪ برسد و پایین نیاید
- خطای `ImportError` یا `undefined name`

---

## کارهای باقی‌مانده

جزئیات کامل در `FIX_REPORT.md`. خلاصه:

1. **۲۳ نقض Clean Architecture** — نیاز به بازطراحی composition root با DI دارد (تصمیم معماری شماست)
2. **۵ مورد `shell=True`** در ابزارهای infrastructure
3. **گزارش‌های داخل `ShadBotWorkspace/`** هنوز ادعای «۱۰۰٪ کامل» دارند — بر پایه گیت قلابی ساخته شده بودند
4. **کد تولیدشده در `ShadBotCore_BuiltByAgent/`** اجراشدنی نیست: چند فایل در یک فایل چسبیده، ایمپورت‌های شکسته. این مشکل لایه parsing تولید کد است، نه گیت.
