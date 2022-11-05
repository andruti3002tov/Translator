from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from main import *
from Settings import TOKEN


bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply("Привет!\nНапиши мне что-нибудь!")


@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    await message.reply("Напиши мне что-нибудь, и я отправлю этот текст тебе в ответ!")


@dp.message_handler()
async def echo_message(msg: types.Message):
    send_text = Trans().trans(orig_text=msg.text, need_lang='ru')
    await bot.send_message(msg.from_user.id, send_text)















executor.start_polling(dp)