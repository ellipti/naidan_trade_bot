# utils/trading_econ_check.py
import os
import requests
from datetime import datetime, timedelta
from dotenv import load_dotenv

load_dotenv()

def is_high_impact_news(pair="XAUUSD", api_key=None):
    if api_key is None:
        api_key = os.getenv("TRADING_ECON_API_KEY")

    if api_key is None:
        print("❌ TRADING_ECON_API_KEY not found in environment.")
        return False

    base_url = "https://api.tradingeconomics.com/calendar"
    now = datetime.utcnow()
    start = now.strftime("%Y-%m-%dT%H:%M:%S")
    end = (now + timedelta(minutes=30)).strftime("%Y-%m-%dT%H:%M:%S")

    params = {
        "c": api_key,
        "d1": start,
        "d2": end,
    }

    try:
        response = requests.get(base_url, params=params)
        if response.status_code != 200:
            print(f"❌ TradingEconomics API статус: {response.status_code}")
            return False

        events = response.json()
        for event in events:
            impact = str(event.get("importance", "")).lower()
            currency = event.get("country", "")
            if impact in ["high", "3"] and pair[:3] in currency:
                print(f"⚠️ High impact news detected: {event.get('event', 'Unknown event')}")
                return True

        print("✅ No high-impact economic events found.")
        return False

    except Exception as e:
        print(f"❌ TradingEconomics шалгах үед алдаа гарлаа: {e}")
        return False
