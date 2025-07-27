# utils/indicators.py

import pandas as pd
import pandas_ta as ta

def compute_indicators(df: pd.DataFrame) -> pd.DataFrame:
    """
    Ханшийн дата дээр RSI, MACD, EMA, Bollinger Bands зэрэг гол техник индикаторуудыг тооцоолно.
    """

    # ✅ EMA 50, EMA 200
    df["EMA_50"] = ta.ema(df["close"], length=50)
    df["EMA_200"] = ta.ema(df["close"], length=200)

    # ✅ RSI (14)
    df["RSI_14"] = ta.rsi(df["close"], length=14)

    # ✅ MACD (12, 26, 9)
    macd = ta.macd(df["close"], fast=12, slow=26, signal=9)
    df["MACD"] = macd["MACD_12_26_9"]
    df["MACD_signal"] = macd["MACDs_12_26_9"]
    df["MACD_hist"] = macd["MACDh_12_26_9"]

    # ✅ Bollinger Bands (20, 2.0)
    bbands = ta.bbands(df["close"], length=20, std=2)
    df["BB_upper"] = bbands["BBU_20_2.0"]
    df["BB_middle"] = bbands["BBM_20_2.0"]
    df["BB_lower"] = bbands["BBL_20_2.0"]

    # ✅ Ichimoku (optional: future span-г skip хийсэн)
    ichi = ta.ichimoku(df["high"], df["low"])
    df["tenkan_sen"] = ichi["ITS_9"]
    df["kijun_sen"] = ichi["IKS_26"]
    df["senkou_span_a"] = ichi["ISA_9"]
    df["senkou_span_b"] = ichi["ISB_26"]

    # ❌ NaN утгуудыг хасна
    df.dropna(inplace=True)

    return df
