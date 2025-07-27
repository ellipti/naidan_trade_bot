import os
from dotenv import load_dotenv
from utils.draw_chart import draw_market_chart
from utils.vision_gpt import analyze_chart
from utils.trading_econ_check import is_high_impact_news
from utils.send_telegram import send_telegram
from utils.time_utils import should_trade

# .env файлаас API KEY, TOKEN зэргийг ачааллах
load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

symbol = "XAUUSD"
timeframe = "15m"

def send_to_gpt_and_get_decision(prompt, image_path):
    return analyze_chart(prompt, image_path)

def run_bot():
    
    print("📊 График зурж байна...")
    image_file = draw_market_chart(symbol, timeframe)

    print("📰 Эдийн засгийн мэдээ шалгаж байна...")
    if is_high_impact_news(symbol):
        print("⚠️ Өндөр нөлөөтэй эдийн засгийн мэдээ байна. Арилжаа хийхгүй.")
        return
    else:
        print("✅ Нөлөө өндөртэй мэдээ илрээгүй.")

    print("🧠 GPT шийдвэр авч байна...")
    try:
        prompt = f"""
Та бол мэргэшсэн форекс шинжээч.
Энэ графикийг шинжлээд дараах үндсэн чиглэл, төвшингүүдийг санал болгоно уу:

- Арилжааны шийдвэр (ХУДАЛДАЖ АВАХ, ХУДАЛДАХ эсвэл ХҮЛЭЭХ)
- Оролтын үнэ, Stop Loss (SL), Take Profit (TP)
- Техникийн тайлбар (support/resistance, liquidity zones, order blocks, candlestick patterns)

Хослол: {symbol}, Цагийн хүрээ: {timeframe}
"""
        print("🧠 GPT Vision API ажиллаж байна...")
        gpt_response = send_to_gpt_and_get_decision(prompt.strip(), image_file)
        print("📩 GPT хариу амжилттай ирлээ.")

        telegram_message = f"""📈 Арилжааны шийдвэр
📌 Хослол: {symbol}
⏱ Цагийн хүрээ: {timeframe}

{gpt_response}

🤖 AI-ийн шинжилгээг үндэслэн боловсруулав."""
        send_telegram(telegram_message, TELEGRAM_BOT_TOKEN, TELEGRAM_CHAT_ID)

        print("✅ Telegram мессеж илгээгдлээ.")
    except Exception as e:
        print(f"❌ GPT Decision error: {e}")

if __name__ == "__main__":
    run_bot()
