import requests

BOT_TOKEN = '8039418238:AAFKGrmnbEDVX2UTl82ZN6vMQRYGPmUrCWo'  # жишээ: 6089xxxxxx:AAGxxxxxxxxxxxx
URL = f"https://api.telegram.org/bot{BOT_TOKEN}/getUpdates"

response = requests.get(URL)
print(response.json())
