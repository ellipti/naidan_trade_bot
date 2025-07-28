# naidan_trade_bot
# 🤖 AIVO: AI-Powered Trading Bot for MetaTrader 5

AIVO бол ChatGPT Vision API, MetaTrader 5, болон Telegram-г хослуулсан **хиймэл оюунд суурилсан автомат арилжааны систем** юм. Энэ бот нь техникийн график, лааны хэлбэр, болон эдийн засгийн мэдээнд дүн шинжилгээ хийж, оновчтой арилжааны шийдвэр гаргадаг.

---

## 🔍 Гол боломжууд

- 📈 **GPT-4o Vision** ашиглан график шинжилгээ
- 💹 **MT5** дээрх реальны эсвэл демо арилжаа
- 🔄 Автомат **BUY / SELL / WAIT** шийдвэр гаргалт
- 🧠 Candlestick, Structure Break, Trend zone таних
- 🧾 **Telegram Bot**-оор арилжааны мэдэгдэл илгээх
- 📰 **Эдийн засгийн мэдээ** шүүлт (Trading Economics API)
- 🗂️ **Google Sheets** болон Firebase лог бүртгэл (сонголтоор)

---

## ⚙️ Ашигласан технологиуд

| Технологи | Тайлбар |
|-----------|---------|
| Python 3.11 | Үндсэн backend |
| MetaTrader5 | Захиалга гүйцэтгэх |
| OpenAI GPT-4o | Арилжааны шийдвэр, график шинжилгээ |
| Telegram Bot API | Real-time мэдэгдэл илгээх |
| TradingEconomics API | Эдийн засгийн мэдээ авах |
| Matplotlib | График зурж GPT-д илгээх |
| Google Sheets API | Арилжааны бүртгэл хадгалах (сонголтоор) |

---

## 🧱 Ботын бүтэц (Architecture)

MetaTrader 5 <--> draw_chart.py
↓
vision_gpt.py --(Chart)--> GPT-4o Vision
↓
run_full_cycle.py
↓ ↓
Telegram Trade Executor


---

## 📦 Төслийн бүтэц

ai_trade_bot/
├── run_full_cycle.py # Ботын үндсэн цикл
├── vision_gpt.py # GPT-д анализ хийлгэх
├── draw_chart.py # График зураг үүсгэх
├── trade_executor.py # Арилжаа гүйцэтгэх
├── mt5_handler.py # MT5 холболт
├── send_telegram.py # Telegram мэдэгдэл
├── forexfactory_check.py # Эдийн засгийн мэдээ
├── utils/
│ └── log_to_sheet.py # (сонголтоор) Google Sheet лог
├── last_decision.json # Сүүлийн арилжааны лог
├── requirements.txt # Зависимостууд

---

## 🚀 Ашиглах заавар

### 1. Шаардлагатай хангамж
```bash
pip install -r requirements.txt
OPENAI_API_KEY=sk-...
TELEGRAM_BOT_TOKEN=...
TELEGRAM_CHAT_ID=...
TRADING_ECONOMICS_API_KEY=...

python run_full_cycle.py

✅ Decision: SELL
💰 Entry: 2341.50
📉 SL: 2350.00
📈 TP: 2320.00
🧠 Reason: Bearish engulfing + lower highs
📸 Chart: [attached]

📈 Арилжааны стратегийн үндэс
Техникийн анализ: Pin bar, Hammer, Engulfing, Structure Break

Мэдээ шүүлт: NFP, CPI, FOMC зэрэг event-үүдийг зайлсхийх

GPT Reasoning: Зураг, текст анализ хослуулан шийдвэр гаргана

📋 Хөгжүүлэлтийн төлөвлөгөө (v2 roadmap)
 GPT Vision интеграц

 Telegram integration

 MT5 гүйцэтгэл

 Эдийн засгийн мэдээ шүүлтүүр

 Web dashboard (Flutter / React)

 Dynamic SL/TP zone бүхий AI logic

 Backtesting модуль

 Subscription систем + Signal хандалт

👨‍💻 Хувь нэмэр оруулах
Pull request, issue гаргах болон сайжруулах санаа байвал таатай хүлээн авна. Монголын трейдерүүдэд зориулсан AI автоматжуулалтын төслийг хамтдаа хөгжүүлье!
