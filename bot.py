import asyncio
import datetime
from telegram import Bot
import pytz

TOKEN = '8360426787:AAH24XoV-2uB-iEMktKlFjtjDWYEInhVNY0'
CHANNEL_ID = '-1002310864226'

MESSAGE = """
🧠 Help Us Improve — We Want Your Feedback

Your input will directly shape what we build next — no pitches, no promos, just honest feedback.

If you're open to sharing your thoughts, we’d really appreciate it.

👉 https://forms.gle/duCuVmzdChLjuBaN8

It only takes a few minutes, and it makes a big difference.

Thanks for helping us make this better.
"""

gst = pytz.timezone('Asia/Dubai')

async def send_message():
    async with Bot(token=TOKEN) as bot:
        await bot.send_message(chat_id=CHANNEL_ID, text=MESSAGE)
        now = datetime.datetime.now(gst).strftime('%Y-%m-%d %H:%M:%S GST')
        print(f"✅ Message sent at {now}")

async def scheduler():
    while True:
        now_utc = datetime.datetime.utcnow()
        now_gst = now_utc.replace(tzinfo=pytz.utc).astimezone(gst)
        print(f"⏰ Checking time: {now_gst.strftime('%A %H:%M')} GST")

        # Thursday = 3 (Monday=0), but pytz weekday() starts Monday=0 so Thursday=3
        # If your environment uses different weekday numbering adjust accordingly
        if now_gst.weekday() == 3 and now_gst.hour == 14 and now_gst.minute == 35:
            await send_message()
            await asyncio.sleep(60)  # wait 1 minute to avoid duplicate sends

        await asyncio.sleep(20)  # check every 20 seconds

if __name__ == '__main__':
    asyncio.run(scheduler())
