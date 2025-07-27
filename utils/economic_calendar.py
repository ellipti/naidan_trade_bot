import requests
import datetime

def fetch_economic_calendar(days=2):
    """
    Investing.com-ийн API эндпоинтаас economic calendar-ийн мэдээллийг авч,
    өндөр/дундаж нөлөөтэй мэдээг буцаана.
    """

    base_date = datetime.date.today()
    date_from = base_date.strftime("%Y-%m-%d")
    date_to = (base_date + datetime.timedelta(days=days)).strftime("%Y-%m-%d")
    url = "https://www.investing.com/economic-calendar/Service/getCalendarFilteredData"
    headers = {
        "User-Agent": ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                       "AppleWebKit/537.36 (KHTML, like Gecko) "
                       "Chrome/115.0.0.0 Safari/537.36"),
        "x-requested-with": "XMLHttpRequest",
        "Referer": "https://www.investing.com/economic-calendar/"
    }
    data = {"dateFrom": date_from, "dateTo": date_to}
    resp = requests.post(url, headers=headers, data=data, timeout=10)
    resp.raise_for_status()
    events = resp.json().get("events", [])

    alerts = []
    for ev in events:
        impact = ev.get("impact")
        if impact in ("high", "medium"):
            alerts.append({
                "date": ev.get("year") + "-" + ev.get("month") + "-" + ev.get("day"),
                "time": ev.get("hour") + ":" + ev.get("minute"),
                "currency": ev.get("currency"),
                "impact": impact,
                "title": ev.get("title")
            })
    return alerts
