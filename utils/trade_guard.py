# utils/trade_guard.py

import os
import json
import time

LAST_DECISION_FILE = "last_decision.json"

# 🕒 Timeframe тохиргоо (секундээр)
TIMEFRAME_INTERVALS = {
    "M1": 60 * 60,       # 1 trade per hour
    "M15": 60 * 60 * 5,  # 1 trade per 5 hours
    "M30": 60 * 60 * 5,
    "H1": 60 * 60 * 6,
}

def load_last_decision():
    if not os.path.exists(LAST_DECISION_FILE):
        return {}
    with open(LAST_DECISION_FILE, "r") as f:
        return json.load(f)

def save_last_decision(symbol, timeframe):
    decisions = load_last_decision()
    decisions[f"{symbol}_{timeframe}"] = {
        "timestamp": time.time()
    }
    with open(LAST_DECISION_FILE, "w") as f:
        json.dump(decisions, f, indent=4)

def should_trade(symbol, timeframe) -> bool:
    decisions = load_last_decision()
    key = f"{symbol}_{timeframe}"

    if key not in decisions:
        return True

    last_ts = decisions[key]["timestamp"]
    interval = TIMEFRAME_INTERVALS.get(timeframe, 3600)
    now = time.time()

    return (now - last_ts) > interval
