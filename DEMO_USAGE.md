# 🤖 AIVO Trading Bot - Demo Заавар

Энэ бол **AIVO (AI-Powered Trading Bot)** бөгөөд GPT-4 Vision, MetaTrader 5, Telegram-г ашиглан автомат арилжаа хийдэг систем юм.

## 📋 Ботын онцлог

- 🧠 **GPT-4o Vision** ашиглан график шинжилгээ
- 📊 Автомат **XAUUSD, SP500** зэрэг хэрэгслүүдийн шинжилгээ
- 📱 **Telegram** дамжуулан real-time мэдэгдэл
- 📈 Техникийн анализ: Candlestick patterns, Support/Resistance, RSI
- ⚠️ Эдийн засгийн мэдээний шүүлтүүр

## 🚀 Хэрхэн ашиглах

### 1. Demo горим (API keys хэрэгтэй)

```bash
# Виртуал орчин идэвхжүүлэх
source venv/bin/activate

# Demo bot ажиллуулах
python demo_bot.py
```

### 2. Жинхэнэ арилжаа (Бүрэн тохиргоо шаардлагатай)

```bash
# .env файлд API keys оруулах
OPENAI_API_KEY=your_openai_api_key
TELEGRAM_BOT_TOKEN=your_telegram_bot_token
TELEGRAM_CHAT_ID=your_chat_id

# MetaTrader 5 ажиллуулах (Windows-д)
# Дараа нь:
python run_full_cycle_mn.py
```

## 📊 Демо шинжилгээний жишээ

```
🔍 ТЕХНИКИЙН ШИНЖИЛГЭЭ - XAUUSD

📊 АРИЛЖААНЫ ШИЙДВЭР: ХУДАЛДАХ (SELL)

💰 ОРОЛТЫН ПАРАМЕТРУУД:
- Оролтын үнэ: 2,010.50 USD
- Stop Loss (SL): 2,025.00 USD  
- Take Profit (TP): 1,985.00 USD

🔍 ТЕХНИКИЙН ҮНДЭСЛЭЛ:
- Хүчтэй resistance зүрэн дээр татаж буй байдал
- Bearish engulfing нөхцөл үүсч байна
- RSI хэт худалдан авагдсан (overbought) бүсэд орж байна
```

## 📂 Файлын бүтэц

```
├── demo_bot.py          # Demo горимын үндсэн файл
├── demo_chart.py        # Demo график үүсгэх
├── run_full_cycle_mn.py # Монгол хэл дээрх үндсэн бот
├── utils/               # Туслах функцууд
│   ├── vision_gpt.py    # GPT Vision шинжилгээ
│   ├── send_telegram.py # Telegram мессеж
│   └── draw_chart.py    # График зурах (MT5)
└── images/              # График зургууд
```

## ⚠️ Анхааруулга

- **Demo горим** нь зөвхөн системийг танилцуулах зорилготой
- Жинхэнэ арилжаанд хэрэглэхээс өмнө стратегийг сайтар тест хийх шаардлагатай
- Арилжааны эрсдэл өндөр байдаг - зөвхөн алдаж болох мөнгөөр арилжаа хийнэ үү

## 🔧 Шаардлагатай зависимости

```
pandas
pandas_ta
matplotlib
openai
python-dotenv
requests
```

## 🎯 Demo-г ажиллуулсны дараа

1. `images/` папкад график зургууд үүсэх
2. Console дээр Telegram мессежийн жишээ харагдах
3. Техникийн шинжилгээний дэлгэрэнгүй мэдээлэл гарах

---

*Хөгжүүлэгч: NAIDAN Trading Systems*  
*Бусад асуулт байвал GitHub issues хэсэгт бичнэ үү.*