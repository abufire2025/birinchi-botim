import asyncio
import os
from aiogram import Bot, Dispatcher, types
from flask import Flask
from threading import Thread

API_TOKEN = "8229350603:AAG42YW2p5ypjaFkVwAHwSUsHBAfe7ZHexI"

bot = Bot(token=API_TOKEN)
dp = Dispatcher()

app = Flask(__name__)

@app.route('/')
def home():
    return "Bot tirik!"

def run():
    port = int(os.environ.get("PORT", 8080))
    app.run(host='0.0.0.0', port=port)

def keep_alive():
    t = Thread(target=run)
    t.daemon = True
    t.start()

@dp.message()
async def handle_messages(message: types.Message):
    if not message.text:
        return

    text = message.text.lower()

    if "/start" in text:
        await message.answer("Xush kelibsiz! ✅ Men 24/7 ishlayman.")
    elif "salom" in text:
        await message.answer("Assalomu alaykum!")
    elif "qalaysan" in text:
        await message.answer("Yaxshi, rahmat! Oʻzingizchi?")
    else:
        await message.answer("Xabaringizni oldim!")

async def main():
    keep_alive()
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
