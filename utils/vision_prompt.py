# utils/vision_prompt.py

import pandas as pd
import json

def generate_prompt_and_image(df: pd.DataFrame, image_path: str, symbol: str, timeframe: str):
    """
    Индикаторуудыг JSON хэлбэрээр харуулж, ChatGPT Vision API-д илгээх prompt-г бүрдүүлнэ.
    """

    # 🔽 Сүүлийн 1 лааны дата-г авах
    last = df.iloc[-1]

    # 🧠 Prompt-д орох үндсэн өгөгдлүүд
    indicator_snapshot = {
        "symbol": symbol,
        "timeframe": timeframe,
        "price": float(last["close"]),
        "RSI_14": float(last["RSI_14"]),
        "EMA_50": float(last["EMA_50"]),
        "EMA_200": float(last["EMA_200"]),
        "MACD": float(last["MACD"]),
        "MACD_signal": float(last["MACD_signal"]),
        "MACD_hist": float(last["MACD_hist"]),
        "BB_upper": float(last["BB_upper"]),
        "BB_middle": float(last["BB_middle"]),
        "BB_lower": float(last["BB_lower"]),
        "tenkan_sen": float(last["tenkan_sen"]),
        "kijun_sen": float(last["kijun_sen"]),
        "senkou_span_a": float(last["senkou_span_a"]),
        "senkou_span_b": float(last["senkou_span_b"]),
    }

    # ✏️ Prompt текст
    prompt = f"""
You're an AI forex trading assistant. Please analyze the candlestick chart image and the following indicators to decide whether we should BUY, SELL, or WAIT.

Respond in this JSON format:
{{
  "action": "BUY or SELL or WAIT",
  "confidence": 0.0 to 1.0,
  "reason": "short explanation",
  "stop_loss": price,
  "take_profit": price
}}

Current market snapshot:
{json.dumps(indicator_snapshot, indent=2)}
"""

    return prompt, image_path
