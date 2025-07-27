import requests

BOT_TOKEN = '8039418238:AAFKGrmnbEDVX2UTl82ZN6vMQRYGPmUrCWo'  # Жишээ: '6089xxxxx:AAxxxxxxxxxxxx'
CHANNEL_ID = '-1002807341269'  # Таны getUpdates-аас олсон chat_id

def send_post(message):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {
        'chat_id': CHANNEL_ID,
        'text': message,
        'parse_mode': 'HTML'  # Хэрэв форматгүй бол 'Markdown' ч байж болно
    }
    response = requests.post(url, data=payload)
    print(response.json())

# Жишээ мессеж
send_post("📈 AIVO Trade Bot-оос <b>амжилттай</b> пост илгээлээ.")
