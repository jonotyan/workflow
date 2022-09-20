from aiogram import types

from loader import dp, bot


@dp.message_handler(state=None)
async def bot_echo(message: types.Message):

    if message.text.lower().strip() in CategoryList:
        # save category
        ChooseCategory.stateChoosingCount.set()
        await message.answer('Ты написал', message.text)
    # обработка категории (текст)
    else:
        await message.answer('такой категории нет')


@dp.message_handler(state=ChooseCategory.stateChoosingCount)
async def bot_echo(message: types.Message):

    # получаем фотки по заданному кол-ву (категория + кол-во)
    await state.finish() # завершаем все состояния
    # скачиваем и сохраняем
    # отправляем медиагруппу
    bot.send_media_group(chat_id, media)
    # удаляем из папки