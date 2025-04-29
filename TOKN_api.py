import time
import requests

BOT_TOKEN = '7251405209:AAEy-iBVV14VtRzUAYeb59FV3kJb2TqzGV0'
API_URL = f"https://api.telegram.org/bot{BOT_TOKEN}/"

# حذف Webhook
requests.get(API_URL + "deleteWebhook")

def get_updates(offset=None):
    url = API_URL + "getUpdates"
    if offset:
        url += f"?offset={offset}"
    return requests.get(url).json()

def send_message(chat_id, text):
    url = API_URL + "sendMessage"
    payload = {"chat_id": chat_id, "text": text}
    requests.post(url, data=payload)

def main():
    print("البوت يعمل الآن بدون توقف...")
    last_update_id = None

    while True:
        updates = get_updates(last_update_id)
        if "result" in updates:
            for update in updates["result"]:
                last_update_id = update["update_id"] + 1
                message = update.get("message", {})
                text = message.get("text", "")
                chat_id = message.get("chat", {}).get("id")

                if text == "/start":
                    send_message(chat_id, " تم تسجيل دخول المهيب تم تسجيل دخول منظمه النسور // بكسم امه الي يلعب ويانا شعارنا موجود ")

        time.sleep(1)

if __name__ == "__main__":
    main()
