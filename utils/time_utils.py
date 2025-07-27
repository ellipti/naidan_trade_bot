import json
import os
import time

LAST_DECISION_FILE = "last_decision.json"

def load_last_decision():
    if not os.path.exists(LAST_DECISION_FILE):
        return {}
    with open(LAST_DECISION_FILE, "r") as f:
        return json.load(f)

def save_last_decision(decision_data):
    with open(LAST_DECISION_FILE, "w") as f:
        json.dump(decision_data, f, indent=4)

def should_trade(timeframe):
    last = load_last_decision()
    now = time.time()

    timeframe_seconds = {
        "1m": 60 * 60,       # 1 цагт нэг удаа
        "15m": 60 * 60 * 5,  # 5 цагт нэг удаа
        "30m": 60 * 60 * 5,  # 5 цагт нэг удаа
    }

    if timeframe not in timeframe_seconds:
        return True

    last_time = last.get(timeframe, 0)
    if now - last_time >= timeframe_seconds[timeframe]:
        last[timeframe] = now
        save_last_decision(last)
        return True

    return False
