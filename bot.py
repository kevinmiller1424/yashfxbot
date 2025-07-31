import asyncio
from telegram import Bot
import datetime
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

async def send_message():
    gst = pytz.timezone('Asia/Dubai')
    async with Bot(token=TOKEN) as bot:
        await bot.send_message(chat_id=CHANNEL_ID, text=MESSAGE)
        now = datetime.datetime.now(gst).strftime('%Y-%m-%d %H:%M:%S GST')
        print(f"✅ Message sent at {now}")

if __name__ == '__main__':
    asyncio.run(send_message())
