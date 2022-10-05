from loader import dp
from aiogram import types


@dp.message_handler()
async def can_not_recognize(message: types.Message):
    await message.answer("Я не понимаю что вы от меня хотите =(")