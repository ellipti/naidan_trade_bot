import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os
import time
from datetime import datetime, timedelta

def generate_demo_chart(symbol="XAUUSD", timeframe="15m", return_data=False):
    """Demo функц - жинхэнэ зах зээлийн график үүсгэх"""
    
    # Demo өгөгдөл үүсгэх
    periods = 100
    dates = pd.date_range(end=datetime.now(), periods=periods, freq='15T')
    
    # Artificial price data - XAUUSD-ийн жишээ үнэ
    base_price = 2000.0  # Gold эхлэх үнэ
    price_changes = np.random.normal(0, 2, periods)  # Random price movements
    prices = []
    current_price = base_price
    
    for change in price_changes:
        current_price += change
        prices.append(current_price)
    
    # OHLC өгөгдөл үүсгэх
    data = []
    for i, (date, close) in enumerate(zip(dates, prices)):
        high = close + np.random.uniform(0, 3)
        low = close - np.random.uniform(0, 3)
        open_price = prices[i-1] if i > 0 else close
        
        data.append({
            'time': date,
            'open': open_price,
            'high': high,
            'low': low,
            'close': close
        })
    
    df = pd.DataFrame(data)
    
    # График зурах
    plt.figure(figsize=(12, 6))
    plt.plot(df['time'], df['close'], label='Close Price', linewidth=2, color='blue')
    plt.fill_between(df['time'], df['low'], df['high'], alpha=0.3, color='lightblue')
    
    plt.title(f"{symbol} - {timeframe} Chart (Demo Data)", fontsize=16, fontweight='bold')
    plt.xlabel("Цаг", fontsize=12)
    plt.ylabel("Үнэ (USD)", fontsize=12)
    plt.grid(True, alpha=0.3)
    plt.legend()
    plt.tight_layout()
    
    # График хадгалах
    timestamp = int(time.time())
    save_path = f"images/demo_chart_{symbol}_{timeframe}_{timestamp}.png"
    os.makedirs("images", exist_ok=True)
    plt.savefig(save_path, dpi=300, bbox_inches='tight')
    plt.close()
    
    print(f"📊 Demo график үүсгэгдлээ: {save_path}")
    
    if return_data:
        return save_path, df
    return save_path

if __name__ == "__main__":
    # Test функц
    chart_path = generate_demo_chart()
    print(f"✅ Chart saved to: {chart_path}")