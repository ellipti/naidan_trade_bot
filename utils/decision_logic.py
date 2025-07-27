# utils/decision_logic.py

import openai
import json
import os

# ✅ OpenAI API Key config
openai.api_key = os.getenv("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")  # .env эсвэл config.py-р дамжуулж болно

def send_to_gpt_and_get_decision(prompt: str, image_path: str) -> dict:
    """
    GPT-4o Vision API-д prompt + chart зураг илгээж, арилжааны шийдвэр гаргуулна.
    """

    print("📡 Sending data to GPT-4o Vision API...")

    # 📤 Image binary ачаалах
    with open(image_path, "rb") as f:
        image_bytes = f.read()

    try:
        # 🔗 Vision API дуудлага
        response = openai.ChatCompletion.create(
            model="gpt-4o",
            messages=[
                {
                    "role": "system",
                    "content": "You are an expert forex trading assistant."
                },
                {
                    "role": "user",
                    "content": [
                        { "type": "text", "text": prompt },
                        { "type": "image_url", "image_url": { "url": "data:image/png;base64," + image_bytes.encode("base64").decode(), "detail": "auto" } }
                    ]
                }
            ],
            max_tokens=500,
            temperature=0.3
        )

        # 📥 GPT хариуг авах
        content = response["choices"][0]["message"]["content"]

        # 🎯 JSON гэж үзэж хөрвүүлнэ
        decision = json.loads(content)
        print("✅ GPT decision:", decision)

        return decision

    except Exception as e:
        print("❌ GPT Vision API error:", e)
        return {
            "action": "WAIT",
            "confidence": 0.0,
            "reason": "GPT error fallback",
            "stop_loss": 0.0,
            "take_profit": 0.0
        }
