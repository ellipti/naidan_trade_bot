import MetaTrader5 as mt5
import time

def execute_trade(symbol, lot=0.1, sl_points=100, tp_points=200, trade_type='buy'):
    if not mt5.initialize():
        print("❌ MT5 initialization failed")
        return None

    # Зах зээлийн үнэ
    symbol_info = mt5.symbol_info(symbol)
    if symbol_info is None:
        print(f"❌ Failed to get symbol info for {symbol}")
        return None

    if not symbol_info.visible:
        mt5.symbol_select(symbol, True)

    price = mt5.symbol_info_tick(symbol).ask if trade_type == 'buy' else mt5.symbol_info_tick(symbol).bid
    deviation = 10

    sl = price - sl_points * symbol_info.point if trade_type == 'buy' else price + sl_points * symbol_info.point
    tp = price + tp_points * symbol_info.point if trade_type == 'buy' else price - tp_points * symbol_info.point

    request = {
        "action": mt5.TRADE_ACTION_DEAL,
        "symbol": symbol,
        "volume": lot,
        "type": mt5.ORDER_TYPE_BUY if trade_type == 'buy' else mt5.ORDER_TYPE_SELL,
        "price": price,
        "sl": round(sl, symbol_info.digits),
        "tp": round(tp, symbol_info.digits),
        "deviation": deviation,
        "magic": 234000,
        "comment": f"AI Trade {trade_type.upper()}",
        "type_time": mt5.ORDER_TIME_GTC,
        "type_filling": mt5.ORDER_FILLING_IOC,
    }

    result = mt5.order_send(request)
    if result.retcode != mt5.TRADE_RETCODE_DONE:
        print(f"❌ Trade execution failed. Code: {result.retcode}")
    else:
        print(f"✅ Trade executed: {trade_type.upper()} {symbol} at {price}")

    return result
