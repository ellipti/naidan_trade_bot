import MetaTrader5 as mt5
import pandas as pd
from datetime import datetime, timedelta

import MetaTrader5 as mt5

def initialize_mt5():
    if not mt5.initialize():
        print("❌ MT5 initialize() амжилтгүй.")
        return False

    account_info = mt5.account_info()
    if account_info is None:
        print("❌ MT5 account_info() уншигдсангүй.")
        mt5.shutdown()
        return False

    print(f"✅ MetaTrader 5 холбогдлоо.\n🧾 Account ID: {account_info.login}, Balance: {account_info.balance}")
    return True


def fetch_latest_chart(symbol="XAUUSD", timeframe="M15", bars=100):
    timeframe_map = {
        "1m": mt5.TIMEFRAME_M1,
        "5m": mt5.TIMEFRAME_M5,
        "15m": mt5.TIMEFRAME_M15,
        "30m": mt5.TIMEFRAME_M30,
        "1h": mt5.TIMEFRAME_H1,
        "4h": mt5.TIMEFRAME_H4,
        "1d": mt5.TIMEFRAME_D1,
    }

    if timeframe not in timeframe_map:
        raise ValueError(f"Timeframe тохирохгүй байна: {timeframe}")

    utc_from = datetime.now() - timedelta(minutes=bars * 15)
    rates = mt5.copy_rates_from(symbol, timeframe_map[timeframe], utc_from, bars)

    if rates is None or len(rates) == 0:
        raise RuntimeError(f"{symbol} симболын түүхэн дата татагдсангүй.")

    df = pd.DataFrame(rates)
    df['time'] = pd.to_datetime(df['time'], unit='s')
    return df

def get_candles(symbol, timeframe, count=50):
    rates = mt5.copy_rates_from_pos(symbol, timeframe, 0, count)
    if rates is None or len(rates) == 0:
        return []

    candles = []
    for r in rates:
        candles.append({
            "time": r['time'],
            "open": r['open'],
            "high": r['high'],
            "low": r['low'],
            "close": r['close'],
            "tick_volume": r['tick_volume']
        })
    return candles
