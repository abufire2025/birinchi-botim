from aiogram import Bot,Dispatcher,executor
from aiogram.types import Message
api='8229350603:AAG42YW2p5ypjaFkVwAHwSUsHBAfe7ZHexI'
bot=Bot(api)
dp=Dispatcher(bot)

@dp.message_handler(commands='start')
async def getstart(message:Message):
    await message.answer('Xush kelib siz')
@dp.message_handler(text='Salom')
async def getsalom(message:Message):
    chatid=message.chat.id
    await bot.send_message(chat_id=chatid,text='Hello')
    await message.answer('Alik')



@dp.message_handler(lambda message:'salom'in message.text.lower())
async def salom(message:Message):
    await message.answer('Assalomu Alaykum')
@dp.message_handler(lambda message: 'qalaysan' in message.text.lower())
async def qalaysan(message: Message):
    await message.answer('Yahshi raxmat ozingizchi')
    @dp.message_handler(lambda message:'zor'in message.text.lower())
    async def zor(message:Message):
     await message.answer('Kuningiz Yaxshi ottimi')
    @dp.message_handler(lambda message: 'ha'in message.text.lower())
    async def ha(message:Message):
         await message.answer('Ha yaxshi Nma bilan Bantsiz')
    @dp.message_handler(lambda message:'dars qilayapman'in message.text.lower())
    async def darsqilayapman(message:Message):
        await message.answer('Qanaqa Dars')
    @dp.message_handler(lambda message :'it dan'in message.text.lower())
    async def itdan(message :Message):
        await message.answer('Ha qanaqa dars')

    @dp.message_handler(lambda message: ' bot yaratyapmiz ' in message.text.lower())
    async def botyaratyapmiz(message : Message):
        await message.answer('Ha osson mikan')

executor.start_polling(dp, skip_updates=True)




