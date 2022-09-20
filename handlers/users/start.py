from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp
welcome_text = "Я умею показывать картини :)\n Для вашего же удобства, все картинки поделены по категориям\n Введите /category для отображения всех категорий"


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"Привет, {message.from_user.full_name}!")
    await message.answer(welcome_text)
