from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp


@dp.message_handler(Command())
async def bot_start(message: types.Message):
    categories = """Выбери категорию
    2
    3
    4
    5"""
    await message.answer(categories)
