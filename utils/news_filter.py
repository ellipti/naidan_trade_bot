# utils/news_filter.py

import requests
from datetime import datetime, timedelta

def is_high_impact_news_upcoming(hours_ahead=2):
    """
    ForexFactory Calendar API ашиглан ойрын 2 цагийн дотор өндөр нөлөөтэй мэдээ байвал True буцаана.
    """

    try:
        # 🧠 ForexFactory-ийн mirror RSS feed ашиглах (эсвэл өөр calendar API)
        url = "https://nfs.faireconomy.media/ff_calendar_thisweek.xml"
        response = requests.get(url)

        if response.status_code != 200:
            print("⚠️ Could not fetch news calendar.")
            return False

        # 🧪 Түр зуурын шалгалтын нөхцөл (demo)
        now = datetime.utcnow()
        future = now + timedelta(hours=hours_ahead)

        # 🟠 Demo: Хэрвээ өнөөдөр Friday бол NFP гэж үзье
        if now.weekday() == 4 and now.hour >= 12 and now.hour <= 16:
            print("📰 High-impact news time (Friday afternoon) — NFP likely.")
            return True

        # ✅ Реал parser-г дараа бичиж өгч болно (HTML/XML parse хийх замаар)
        return False

    except Exception as e:
        print("❌ News filter error:", e)
        return False
