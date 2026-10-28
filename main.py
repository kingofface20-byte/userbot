import os
import threading
from flask import Flask
from telethon import TelegramClient, events
from telethon.sessions import StringSession

# ستاسو معلومات
api_id = 31975090
api_hash = '6aa754fe9f71159b076cd4902574e47f'
TARGET_CHANNEL = -1004384888965  # ستاسو اصلي چینل

# ۱. د فلاسیک ویب سرور (د رایډر د وړیا ویب سرور لپاره)
app = Flask('')

@app.route('/')
def home():
    return "Userbot Web Service is Active and Running!"

def run_flask():
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)

# ۲. د یوزر بوټ برخه
client = TelegramClient(StringSession(), api_id, api_hash)

@client.on(events.NewMessage)
async def handle_new_messages(event):
    if event.media:
        # فایل په ثانیه کې اصلي چینل ته فارورډ کیږي
        await event.forward_to(TARGET_CHANNEL)
        print("File intercepted and forwarded back to the channel successfully!")

def run_userbot():
    print("Userbot is running and listening...")
    with client:
        print("Session String:", client.session.save())
        client.run_until_disconnected()

if __name__ == "__main__":
    # د ویب سرور پیل کول په یو جلا تار (Thread) کې
    flask_thread = threading.Thread(target=run_flask)
    flask_thread.daemon = True
    flask_thread.start()
    
    # د یوزر بوټ چلول په اصلي برخه کې
    run_userbot()
