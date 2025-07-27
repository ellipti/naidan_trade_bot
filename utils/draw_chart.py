import MetaTrader5 as mt5
import pandas as pd
import matplotlib.pyplot as plt
import os
import time

def draw_market_chart(symbol: str, timeframe: str = '1H', return_rates=False):
    if not mt5.initialize():
        raise RuntimeError("❌ MetaTrader 5 холбогдож чадсангүй.")

    timeframe_map = {
        "1m": mt5.TIMEFRAME_M1,
        "5m": mt5.TIMEFRAME_M5,
        "15m": mt5.TIMEFRAME_M15,
        "30m": mt5.TIMEFRAME_M30,
        "1H": mt5.TIMEFRAME_H1,
        "4H": mt5.TIMEFRAME_H4,
        "1D": mt5.TIMEFRAME_D1
    }

    tf = timeframe_map.get(timeframe)
    if not tf:
        raise ValueError(f"❌ Timeframe тохирохгүй байна: {timeframe}")

    rates = mt5.copy_rates_from_pos(symbol, tf, 0, 100)
    if rates is None or len(rates) == 0:
        raise ValueError("❌ Үнэний мэдээлэл олдсонгүй.")

    df = pd.DataFrame(rates)
    df['time'] = pd.to_datetime(df['time'], unit='s')

    plt.figure(figsize=(10, 5))
    plt.plot(df['time'], df['close'], label='Close Price')
    plt.title(f"{symbol} - {timeframe} Chart")
    plt.xlabel("Time")
    plt.ylabel("Price")
    plt.grid(True)
    plt.legend()

    timestamp = int(time.time())
    save_path = f"images/chart_{symbol}_{timeframe}_{timestamp}.png"
    os.makedirs("images", exist_ok=True)
    plt.savefig(save_path)
    plt.close()

    if return_rates:
        return save_path, rates
    return save_path
