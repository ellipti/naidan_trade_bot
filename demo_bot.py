import os
from demo_chart import generate_demo_chart

# Demo функцууд - жинхэнэ API keys-гүйгээр ажиллах
def demo_analyze_chart(prompt, image_path):
    """Demo GPT шинжилгээ - жинхэнэ OpenAI API-гүйгээр"""
    
    demo_response = """
🔍 **ТЕХНИКИЙН ШИНЖИЛГЭЭ - XAUUSD**

📊 **АРИЛЖААНЫ ШИЙДВЭР: ХУДАЛДАХ (SELL)**

💰 **ОРОЛТЫН ПАРАМЕТРУУД:**
- Оролтын үнэ: 2,010.50 USD
- Stop Loss (SL): 2,025.00 USD  
- Take Profit (TP): 1,985.00 USD

🔍 **ТЕХНИКИЙН ҮНДЭСЛЭЛ:**
- Хүчтэй resistance зүрэн дээр татаж буй байдал
- Bearish engulfing нөхцөл үүсч байна
- RSI хэт худалдан авагдсан (overbought) бүсэд орж байна
- 50 MA-ийн дагуу support сулалт харагдаж байна

⚠️ **ЭРСДЭЛИЙН УДИРДЛАГА:**
- Position size: 0.1 lot-аас ихгүй
- Risk/Reward ratio: 1:1.8

🤖 AI-ийн дүгнэлт: Богино хугацаанд доошлох хандлага дээдэлж байна.
"""
    return demo_response

def demo_send_telegram(message):
    """Demo Telegram мессеж илгээх"""
    print("📱 TELEGRAM МЕССЕЖ:")
    print("=" * 50)
    print(message)
    print("=" * 50)
    print("✅ Demo Telegram мессеж 'илгээгдлээ'")

def demo_check_news(symbol):
    """Demo эдийн засгийн мэдээ шалгах"""
    import random
    return random.choice([True, False])  # Санамсаргүй үр дүн

def run_demo_bot():
    """Demo bot ажиллуулах"""
    print("🤖 AIVO TRADING BOT - DEMO MODE")
    print("=" * 50)
    
    symbol = "XAUUSD"
    timeframe = "15m"
    
    print("📊 График зурж байна...")
    image_file = generate_demo_chart(symbol, timeframe)
    
    print("📰 Эдийн засгийн мэдээ шалгаж байна...")
    if demo_check_news(symbol):
        print("⚠️ Өндөр нөлөөтэй эдийн засгийн мэдээ байна. Арилжаа хийхгүй.")
        return
    else:
        print("✅ Нөлөө өндөртэй мэдээ илрээгүй.")
    
    print("🧠 GPT шийдвэр авч байна...")
    try:
        prompt = f"""
Та бол мэргэшсэн форекс шинжээч.
Энэ графикийг шинжлээд дараах үндсэн чиглэл, төвшингүүдийг санал болгоно уу:

- Арилжааны шийдвэр (ХУДАЛДАЖ АВАХ, ХУДАЛДАХ эсвэл ХҮЛЭЭХ)
- Оролтын үнэ, Stop Loss (SL), Take Profit (TP)
- Техникийн тайлбар (support/resistance, liquidity zones, order blocks, candlestick patterns)

Хослол: {symbol}, Цагийн хүрээ: {timeframe}
"""
        print("🧠 GPT Vision API ажиллаж байна... (DEMO)")
        gpt_response = demo_analyze_chart(prompt.strip(), image_file)
        print("📩 GPT хариу амжилттай ирлээ.")
        
        telegram_message = f"""📈 **АРИЛЖААНЫ ШИЙДВЭР - DEMO**
📌 Хослол: {symbol}
⏱ Цагийн хүрээ: {timeframe}

{gpt_response}

🤖 AI-ийн шинжилгээг үндэслэн боловсруулав.
📊 График зураг: {image_file}

⚠️ АНХААРУУЛГА: Энэ бол DEMO горим юм. Жинхэнэ арилжаанд ашиглахгүй байх!"""
        
        demo_send_telegram(telegram_message)
        
        print("✅ Demo процесс дууслаа.")
        print(f"📊 График файл: {image_file}")
        
    except Exception as e:
        print(f"❌ Demo error: {e}")

if __name__ == "__main__":
    run_demo_bot()