import asyncio
from aiogram import Bot, Dispatcher, types

api = '8229350603:AAG42YW2p5ypjaFkVwAHwSUsHBAfe7ZHexI'
bot = Bot(token=api)
dp = Dispatcher()

@dp.message()
async def handle_messages(message: types.Message):
if not message.text:
return

async def main():
await dp.start_polling(bot)

if name == "main":
asyncio.run(main())
