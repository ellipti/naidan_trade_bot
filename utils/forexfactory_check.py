import requests
from bs4 import BeautifulSoup
from datetime import datetime

def is_high_impact_news(pair: str) -> bool:
    try:
        headers = {
            "User-Agent": (
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                "AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/115.0.0.0 Safari/537.36"
            ),
            "Accept-Language": "en-US,en;q=0.9",
            "Accept-Encoding": "gzip, deflate, br",
            "Referer": "https://www.forexfactory.com/",
        }

        url = "https://www.forexfactory.com/calendar.php"
        response = requests.get(url, headers=headers, timeout=10)

        if response.status_code != 200:
            print(f"❌ ForexFactory хуудас нээгдсэнгүй. Статус: {response.status_code}")
            return False

        soup = BeautifulSoup(response.content, "html.parser")
        rows = soup.find_all("tr", class_="calendar__row")

        for row in rows:
            impact = row.find("td", class_="calendar__impact")
            currency = row.find("td", class_="calendar__currency")

            if not all([impact, currency]):
                continue

            impact_level = impact.find("span")
            if impact_level and "High" in impact_level.get("title", ""):
                news_currency = currency.text.strip()
                if pair.startswith(news_currency):
                    print(f"🚨 Өнөөдөр {news_currency}-ийн өндөр нөлөөтэй мэдээ байна.")
                    return True

        print(f"✅ No high impact news found for {pair}")
        return False

    except Exception as e:
        print(f"❌ ForexFactory холболт амжилтгүй. {e}")
        return False
