import requests
import os
from dotenv import load_dotenv
from pathlib import Path

def send_telegram(message: str):
    env_path = Path(__file__).resolve().parents[1] / ".env"
    load_dotenv(dotenv_path=env_path)

    BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
    CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

    if not BOT_TOKEN or not CHAT_ID:
        print("❌ Telegram credentials not found.")
        return

    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": message,
        "parse_mode": "HTML"  # Markdown биш болгосон
    }

    try:
        response = requests.post(url, data=payload)
        print(f"📬 Status: {response.status_code}")
        print("📨 Telegram API response:", response.text)
    except Exception as e:
        print("❌ Telegram error:", e)
