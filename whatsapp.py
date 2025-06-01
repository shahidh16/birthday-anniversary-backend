import requests

# Replace these with your actual values
ACCESS_TOKEN = "EAARXTprZCMm8BO43ReAVFgbP5L5cYeqKvo95pm58AyJUVKuWSnoSuG2AjhlIreT6tKx0WmRsPKalsPuCdGzBuTjSHv04QKZABwWhiy2xAFiWq2X4uFyrvkhZCcqUGXWpdkvQ7ns8cbneto7KJZBc6Yq2vXfoXy7P0Gsj0kBnYcFMzRZBYHJoFlgNm7eYkg404SxBNiTd6nSLyCAWQSEEzZCoTjyK5TnBAZD"
PHONE_NUMBER_ID = "595103680362268"
TO_PHONE_NUMBER = "9790306178" 

WHATSAPP_API_URL = f"https://graph.facebook.com/v19.0/{PHONE_NUMBER_ID}/messages"

def send_whatsapp_message(to_number, message):
    headers = {
        "Authorization": f"Bearer {ACCESS_TOKEN}",
        "Content-Type": "application/json"
    }

    payload = {
        "messaging_product": "whatsapp",
        "to": to_number,
        "type": "text",
        "text": {
            "body": message
        }
    }

    response = requests.post(WHATSAPP_API_URL, headers=headers, json=payload)

    if response.status_code == 200:
        print("✅ Message sent successfully!")
    else:
        print(f"❌ Failed to send message: {response.status_code} {response.text}")

if __name__ == "__main__":
    send_whatsapp_message(TO_PHONE_NUMBER, "Hello from your WhatsApp Reminder Bot! 🎉")
