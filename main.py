import os
from telethon import TelegramClient, events
from telethon.sessions import StringSession

# ستاسو معلومات
api_id = 31975090
api_hash = '6aa754fe9f71159b076cd4902574e47f'
TARGET_CHANNEL = -1004384888965  # ستاسو اصلي چینل

# د یوزر بوټ پیل کول
client = TelegramClient(StringSession(), api_id, api_hash)

@client.on(events.NewMessage)
async def handle_new_messages(event):
    if event.media:
        # کله چې فایل په چینل کې راشي، سمدستي اصلي چینل ته فارورډ کیږي
        await event.forward_to(TARGET_CHANNEL)
        print("File intercepted and forwarded back to the channel successfully!")

with client:
    print("Userbot is running and listening...")
    # کله چې دلته شمیره او کوډ وغوښتل شي، د رایډر په لاګونو کې یې ولیکئ
    print("Session String:", client.session.save())
    client.run_until_disconnected()
