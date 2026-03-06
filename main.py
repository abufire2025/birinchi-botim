import asyncio
import os
from aiogram import Bot, Dispatcher, types
from flask import Flask
from threading import Thread

# 1. Bot sozlamalari
API_TOKEN = "8229350603:AAG42YW2p5ypjaFkVwAHwSUsHBAfe7ZHexI"

bot = Bot(token=API_TOKEN)
dp = Dispatcher()

# 2. Render talab qilayotgan Portni ochish (Flask)
app = Flask(__name__)

@app.route('/')
def home():
    return "Bot status: ONLINE"

def run_flask():
    # Render PORT muhit o'zgaruvchisini beradi
    port = int(os.environ.get("PORT", 8080))
    app.run(host='0.0.0.0', port=port)

# 3. Bot buyruqlari
@dp.message()
async def handle_messages(message: types.Message):
    if not message.text:
        return

    text = message.text.lower()

    if "/start" in text:
        await message.answer("Xush kelibsiz! ✅ Bot hozir LIVE holatida.")
    elif "salom" in text:
        await message.answer("Assalomu alaykum! Qalaysiz?")
    elif "qalaysan" in text:
        await message.answer("Yaxshi, rahmat! Oʻzingizchi?")
    else:
        await message.answer(f"Siz '{message.text}' deb yozdingiz. Xabar qabul qilindi!")

# 4. Asosiy ishga tushirish
async def main():
    # Flask serverni alohida oqimda yurgizish
    Thread(target=run_flask, daemon=True).start()

    # Telegram botni yoqish
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
