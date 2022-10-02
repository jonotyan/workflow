from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp


async def bot_start(message: types.Message):
    await message.answer(f"Привет, {message.from_user.full_name}! \nЯ умею показывать картинки :)\nДля вашего же удобства, все картинки поделены по категориям\nВведите /category для отображения всех категорий")

