import asyncio
import datetime
from telegram import Bot
import pytz
import os

TOKEN = os.getenv("BOT_TOKEN") or '8360426787:AAH24XoV-2uB-iEMktKlFjtjDWYEInhVNY0'
CHANNEL_ID = os.getenv("CHANNEL_ID") or '-1002310864226'

MESSAGE = """
🧠 Help Us Improve — We Want Your Feedback

Your input will directly shape what we build next — no pitches, no promos, just honest feedback.

If you're open to sharing your thoughts, we’d really appreciate it.

👉 https://forms.gle/duCuVmzdChLjuBaN8

It only takes a few minutes, and it makes a big difference.

Thanks for helping us make this better.
"""

gst = pytz.timezone('Asia/Dubai')  # GST = UTC+4

async def send_message():
    async with Bot(token=TOKEN) as bot:
        await bot.send_message(chat_id=CHANNEL_ID, text=MESSAGE)
        print(f"✅ Message sent at {datetime.datetime.now(gst).strftime('%Y-%m-%d %H:%M:%S GST')}")

async def main():
    now_utc = datetime.datetime.utcnow()
    now_gst = now_utc.replace(tzinfo=pytz.utc).astimezone(gst)

    # Send only if it is exactly 01:00 AM GST on a Friday
  #  if now_gst.weekday() == 4 and now_gst.hour == 1 and now_gst.minute == 0:
    if now_gst.weekday() == 3 and now_gst.hour == 14 and now_gst.minute == 23:
        await send_message()
    else:
        print(f"⏰ Not time yet: {now_gst.strftime('%A %H:%M GST')} — skipping.")

if __name__ == '__main__':
    asyncio.run(main())
