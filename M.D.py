from aiogram import types, Bot, executor, Dispatcher
from data import Api_Token
import logging
from buttons import menuMain

bot = Bot(token=Api_Token)
dp = Dispatcher(bot)

logging.basicConfig(level=logging.INFO)

@dp.message_handler(commands=["start"])
async def start(message:types.Message):
    username = message.from_user.full_name
    await message.answer(f"Salom {username} Botimizga xush kelib siz.\nKerakli Tilni tanlang", reply_markup=menuMain)
