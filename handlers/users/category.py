from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from web_requests import CategoryList

from loader import dp


@dp.message_handler(Command())
async def bot_start(message: types.Message):
    for i in CategoryList:
        await message.answer(i)
