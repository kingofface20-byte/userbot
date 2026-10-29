import os
import threading
from flask import Flask
from telethon import TelegramClient, events
from telethon.sessions import StringSession

# ستاسو دقیق معلومات او سشن
api_id = 31975090
api_hash = '6aa754fe9f71159b076cd4902574e47f'
STRING_SESSION = '1BVtsOLQBuyNTyT_p1aAw9fsDplUbCVnFRs6roEv4WCJzf0g-0e-VYix66hNsj1Rr91Lokmp84bfTNhCwXnI-J1Bd1o3wo2-I5lTV8m-7tTNv5Lk-j5sh9S_55HiGuFcGNDb6KN04FHs5VJPuM5THUWqCiU_BNXMb-547Dqt9gCI84vWA6kBpqfetTxXk6AbJxCweH5ocjP26nprUxXZSLsWdpJIw3Wxusqfast8g3yKVhthpKfnVjfBvf4J0CEdvrSY2TWd2iSQE-oDrNQI-OwT2AtKZmL6h3giqO7B-wZGT_SFWlpyu35C-xOsG041WIUIcC6338XrPiujsI4diKFNAtfPleds='
TARGET_CHANNEL = -1004384888965  # ستاسو ځانګړی چینل

# ۱. د فلاسیک ویب سرور (د رینډر د وړیا ساتلو لپاره)
app = Flask('')

@app.route('/')
def home():
    return "Userbot Web Service is Active and Running!"

def run_flask():
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)

# ۲. د یوزر بوټ برخه
client = TelegramClient(StringSession(STRING_SESSION), api_id, api_hash)

# بوټ یوازې او یوازې د همدغه یو TARGET_CHANNEL پیغامونه او رسنۍ څاري
@client.on(events.NewMessage(chats=TARGET_CHANNEL))
async def handle_new_messages(event):
    if event.media:
        # فایل یا عکس په همدغه اصلي چینل ته بیرته فارورډ کیږي
        await event.forward_to(TARGET_CHANNEL)
        print("Media detected in target channel and forwarded back successfully!")

def run_userbot():
    print("Userbot is running and listening strictly to the target channel...")
    with client:
        client.run_until_disconnected()

if __name__ == "__main__":
    # د ویب سرور پیل کول په یو جلا تار کې
    flask_thread = threading.Thread(target=run_flask)
    flask_thread.daemon = True
    flask_thread.start()
    
    # د یوزر بوټ چلول
    run_userbot()
