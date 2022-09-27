from aiogram import types
from .web_requests import PictureGeter, CategoryList
from loader import dp, bot
from states.states import ChooseCategory


@dp.message_handler(state=None)
async def bot_echo(message: types.Message):
    if message.text.capitalize() in CategoryList:
        ChooseCategory.stateChoosingCount.set()
        await message.answer('Ты написал', message.text)
    else:
        for i in CategoryList:
            print(i.isupper())
        await message.answer('такой категории нет')


@dp.message_handler(state=ChooseCategory.stateChoosingCount)
async def bot_echo(message: types.Message):

    # получаем фотки по заданному кол-ву (категория + кол-во)
    await state.finish() # завершаем все состояния
    # скачиваем и сохраняем
    # отправляем медиагруппу
    bot.send_media_group(chat_id, media)
    # удаляем из папки


