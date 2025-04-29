import requests

# ضع توكن البوت الخاص بك هنا
BOT_TOKEN = '7251405209:AAEy-iBVV14VtRzUAYeb59FV3kJb2TqzGV0'

# رابط API لإلغاء تفعيل الويب هوك
url = f"https://api.telegram.org/bot{BOT_TOKEN}/deleteWebhook"

# إرسال الطلب
response = requests.get(url)

# التحقق من النجاح وطباعة الرسالة
if response.status_code == 200 and response.json().get("ok"):
    print(" تم تسجيل دخول المهيب تم تسجيل دخول منظمه النسور // بكسم امه الي يلعب ويانا شعارنا موجود ")
else:
    print("فشل في حذف الويب هوك:", response.text)
