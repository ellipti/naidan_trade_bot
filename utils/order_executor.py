# utils/order_executor.py

import MetaTrader5 as mt5
from datetime import datetime
import pytz

def execute_trade(symbol: str, decision: dict):
    """
    GPT-ийн BUY/SELL шийдвэр дээр үндэслэн MT5 дээр арилжаа нээнэ.
    """

    # ✅ Дахин initialize хийж холбогдоно
    if not mt5.initialize():
        raise RuntimeError(f"MT5 init error: {mt5.last_error()}")

    print(f"🚀 Executing {decision['action']} order on {symbol}")

    # 📌 Тохиргоо
    lot = 0.1
    deviation = 10
    sl_price = float(decision["stop_loss"])
    tp_price = float(decision["take_profit"])
    action = decision["action"].upper()

    # 📈 Market price
    tick = mt5.symbol_info_tick(symbol)
    if tick is None:
        print("❌ Symbol not found or tick error.")
        mt5.shutdown()
        return

    price = tick.ask if action == "BUY" else tick.bid
    order_type = mt5.ORDER_TYPE_BUY if action == "BUY" else mt5.ORDER_TYPE_SELL

    # 🧾 Trade request
    request = {
        "action": mt5.TRADE_ACTION_DEAL,
        "symbol": symbol,
        "volume": lot,
        "type": order_type,
        "price": price,
        "sl": sl_price,
        "tp": tp_price,
        "deviation": deviation,
        "magic": 101010,
        "comment": "AI_Trade",
        "type_time": mt5.ORDER_TIME_GTC,
        "type_filling": mt5.ORDER_FILLING_IOC,
    }

    # 📤 Захиалгаа илгээнэ
    result = mt5.order_send(request)
    mt5.shutdown()

    # 🧾 Үр дүн
    if result.retcode != mt5.TRADE_RETCODE_DONE:
        print(f"❌ Trade failed: {result.retcode} | {result.comment}")
    else:
        print(f"✅ Trade executed: {action} {symbol} @ {price}")
        print("📦 Order ID:", result.order)
