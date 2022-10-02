from aiogram import types
from .web_requests import PictureGeter, CategoryList
from loader import dp, bot
from states.states import ChooseCategory
from aiogram.dispatcher import FSMContext

temp: str = ""


@dp.message_handler(state=ChooseCategory.stateChoosingCat)
async def set_category(message: types.Message):
    global temp
    for_check = message.text
    if for_check in CategoryList:
        await message.answer(
            f"Вы выбрали: {message.text}\nТеперь укажите количество картинок которое хотите получить (не больше 1000)")
        temp = for_check
        await ChooseCategory.stateChoosingCount.set()
    else:
        await message.answer('Такой категории нет, возможно вы ввели цифру или допустили орфографическую ошибку\nВы можете попробовать снова ;)')


@dp.message_handler(state=ChooseCategory.stateChoosingCount)
async def set_count(message: types.Message, state: FSMContext):
    global temp
    parsed_pictures = PictureGeter.get_list_with_pictures(int(message.text), temp)

    for url_link in parsed_pictures:
        await bot.send_photo(chat_id=message.chat.id, photo=url_link)

    await state.finish()



