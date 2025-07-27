from dotenv import load_dotenv
from utils.send_telegram import send_telegram

load_dotenv()  # .env файлыг ачаална

send_telegram("✅ Telegram холболт амжилттай! 🤖📡")
