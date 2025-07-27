import os
import json
import re
from dotenv import load_dotenv
from utils.mt5_handler import initialize_mt5
from utils.candlestick_patterns import detect_patterns
from utils.mt5_handler import get_candles
from utils.draw_chart import draw_market_chart
from utils.vision_gpt import analyze_chart
from utils.trade_executor import execute_trade
from utils.send_telegram import send_telegram
from utils.trading_econ_check import is_high_impact_news
from datetime import datetime
from pathlib import Path
from MetaTrader5 import TIMEFRAME_M30
import MetaTrader5 as mt5

load_dotenv()

SYMBOLS = ["XAUUSD", "SP500"]
TIMEFRAMES = ["30m"]

def chart_condition_check(gpt_response_text: str) -> bool:
    if "no clear" in gpt_response_text.lower():
        print("❌ График дээр тодорхой дохио илрээгүй.")
        return False
    if "low quality" in gpt_response_text.lower():
        print("❌ График чанар муу байна.")
        return False
    if "not visible" in gpt_response_text.lower():
        print("❌ Шаардлагатай индикатор харагдахгүй байна.")
        return False
    return True

def log_gpt_decision(symbol, timeframe, prompt, gpt_response, chart_path):
    log_entry = {
        "symbol": symbol,
        "timeframe": timeframe,
        "datetime": datetime.utcnow().isoformat(),
        "prompt": prompt,
        "gpt_response": gpt_response,
        "chart_path": chart_path
    }
    Path("logs").mkdir(exist_ok=True)
    with open("logs/gpt_logs.jsonl", "a", encoding="utf-8") as f:
        f.write(json.dumps(log_entry, ensure_ascii=False) + "\n")

def extract_trade_params(text):
    try:
        entry_match = re.search(r"(Entry|Орох үнэ)[^\d]*(\d+\.?\d*)", text, re.IGNORECASE)
        sl_match = re.search(r"(Stop Loss|SL|Зогсоох алдагдал)[^\d]*(\d+\.?\d*)", text, re.IGNORECASE)
        tp_match = re.search(r"(Take Profit|TP|Ашиг авах)[^\d]*(\d+\.?\d*)", text, re.IGNORECASE)
        if not (entry_match and sl_match and tp_match):
            return None
        return {
            "entry": float(entry_match.group(2)),
            "sl": float(sl_match.group(2)),
            "tp": float(tp_match.group(2))
        }
    except Exception as e:
        print(f"❌ GPT хариу parse алдаа: {e}")
        return None

def parse_decision(text):
    import json, re

    try:
        # Extract JSON block using regex
        json_match = re.search(r"\{.*?\}", text, re.DOTALL)
        if not json_match:
            return None, None, None, None, "GPT хариунд JSON формат олдсонгүй."
        
        json_str = json_match.group(0)
        data = json.loads(json_str)

        action = data.get("Decision", "").upper()
        entry = float(data["Entry"])
        sl = float(data["StopLoss"])
        tp = float(data["TakeProfit"])
        reason = data.get("Reason", "")

        return action, entry, sl, tp, reason
    except Exception as e:
        return None, None, None, None, f"GPT шийдвэр parse хийхэд алдаа гарлаа: {e}"

def build_mongolian_summary(symbol, timeframe, action, entry, sl, tp, reason):
    return (
        f"📊 GPT Арилжааны Шийдвэр\n\n"
        f"💱 Хослол: {symbol}\n"
        f"⏱ Хугацаа: {timeframe}\n"
        f"📌 Шийдвэр: {action}\n\n"
        f"📥 Орох үнэ: {entry}\n"
        f"🛑 Зогсоох алдагдал: {sl}\n"
        f"🎯 Ашиг авах түвшин: {tp}\n\n"
        f"🧠 Тайлбар: {reason}"
    )

def run_bot():
    
    if not initialize_mt5():
        print("❌ MT5 холбогдсонгүй.")
        return
    
    for symbol in SYMBOLS:
        for timeframe in TIMEFRAMES:
            print(f"📊 {symbol} - {timeframe} график зурж байна...")
             # 🕯️ Лааны хэлбэр шалгах
            try:
                # ⬅️ MT5-оос лааны мэдээлэл татах
                candles = get_candles(symbol, TIMEFRAME_M30, count=50)
                # ⬅️ Лааны хэлбэрүүд илрүүлэх
                patterns = detect_patterns(candles)
                if patterns:
                    for pattern in patterns:
                        print("📌 Илэрсэн хэлбэр:", pattern['type'], "үндсэн лаа:", pattern['candle'])
                        
                else:
                    print("🔍 Лааны хэлбэр илрээгүй.")
            except Exception as e:
                print(f"❌ Лааны хэлбэр илрүүлэхэд алдаа гарлаа: {e}")
            
            try:
                image_file = draw_market_chart(symbol, timeframe)
            except Exception as e:
                print(f"❌ Chart зурж чадсангүй: {e}")
                continue

            if is_high_impact_news(symbol):
                print(f"⚠️ {symbol}: Эдийн засгийн өндөр нөлөөтэй мэдээ илэрсэн.")
                continue

            prompt = f"""
You're a professional forex analyst. Based on the following 5-day chart ({symbol}, {timeframe}):

1. Analyze structure (HH/HL, LL/LH, breaks)
2. Detect patterns (Engulfing, Pin Bar, etc)
3. Identify support/resistance zones and liquidity areas
4. Note Tokyo, London, NY session behaviors
5. Estimate RSI/MACD/Volume if visible

🎯 Respond ONLY in JSON like this:
{{
  "Decision": "BUY or SELL or WAIT",
  "Entry": "number",
  "StopLoss": "number",
  "TakeProfit": "number",
  "Reason": "1-2 sentence summary"
}}

Example:
{{
  "Decision": "SELL",
  "Entry": "3400",
  "StopLoss": "3435",
  "TakeProfit": "3380",
  "Reason": "Bearish structure with resistance at 3430 and potential reversal."
}}

Respond ONLY with JSON. No explanation.
"""

            print(f"🧠 GPT Vision анализ {symbol}-{timeframe} ...")
            decision_text = analyze_chart(prompt, image_file)
            print(f"📥 GPT Хариу:\n{decision_text}")
            log_gpt_decision(symbol, timeframe, prompt, decision_text, image_file)

            if not chart_condition_check(decision_text):
                send_telegram(f"📉 {symbol}-{timeframe} график дээр шийдвэр гаргах нөхцөл хангагдсангүй.")
                continue

            action, entry, sl, tp, reason = parse_decision(decision_text)

            if action == "WAIT":
                send_telegram(
                    f"📉 GPT Арилжааны Шийдвэр\n\n"
                    f"💱 Хослол: {symbol}\n"
                    f"⏱ Хугацаа: {timeframe}\n"
                    f"📌 Шийдвэр: Хүлээх (WAIT)\n\n"
                    "⏳ Зах зээл тодорхой бус байна."
                )
                continue

            if None in (action, entry, sl, tp):
                send_telegram(
                    f"⚠️ GPT шийдвэр дутуу байна: {symbol}-{timeframe}. Entry/SL/TP олдсонгүй."
                )
                continue

            message = build_mongolian_summary(symbol, timeframe, action, entry, sl, tp, reason)
            send_telegram(message)

            # ✅ Арилжаа хийх хэсэг
            lot = float(os.getenv("LOT_SIZE", 0.1))
            trade_type = action.lower()
            symbol_info = mt5.symbol_info(symbol)
            point = symbol_info.point

            sl_points = abs(entry - sl) / point
            tp_points = abs(tp - entry) / point

            print(f"▶️ Арилжаа: {action} | Entry: {entry}, SL: {sl}, TP: {tp} → points: SL={sl_points}, TP={tp_points}")
            execute_trade(
                symbol=symbol,
                lot=lot,
                sl_points=sl_points,
                tp_points=tp_points,
                trade_type=trade_type
            )

if __name__ == "__main__":
    run_bot()
