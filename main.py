import asyncio
from aiogram import Bot, Dispatcher, types

API_TOKEN = "8229350603:AAG42YW2p5ypjaFkVwAHwSUsHBAfe7ZHexI"

bot = Bot(token=API_TOKEN)
dp = Dispatcher()

@dp.message()
async def handle_messages(message: types.Message):
    if not message.text:
        return
    
    await message.answer("Xabar qabul qilindi!")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
