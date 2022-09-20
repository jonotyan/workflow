from aiogram import types
from loader import dp, bot
from data.config import change_admin_mode, get_admin_mode, ADMINS
from aiogram.dispatcher.filters.builtin import AdminFilter

# TODO: проверить наличие админского id для текущего хендлера
@dp.message_handler(AdminFilter())
async def admin_mode(message: types.Message):
    if message.text == 'admin off':
        change_admin_mode(False)
    elif message.text = 'admin on':
        change_admin_mode(True)

@dp.message_handler(state=None)
async def bot_echo(message: types.Message):

    if message.text.lower().strip() in CategoryList:
        # save category
        ChooseCategory.stateChoosingCount.set()
        await message.answer('Ты написал', message.text)
    # обработка категории (текст)
    else:
        await message.answer('такой категории нет')
        # TODO: добавить отправку сообщений админу (на все хендлеры)
        if await get_admin_mode():
            bot.send_message(int(ADMINS[0]), 'текст действия пользователя')


@dp.message_handler(state=ChooseCategory.stateChoosingCount)
async def bot_echo(message: types.Message):

    # TODO: доделать этот хендлер

    # получаем фотки по заданному кол-ву (категория + кол-во)
    await state.finish() # завершаем все состояния
    # скачиваем и сохраняем
    # отправляем медиагруппу
    bot.send_media_group(chat_id, media)
    # удаляем из папки

