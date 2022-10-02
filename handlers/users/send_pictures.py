from aiogram import types

import states.states
from .web_requests import PictureGeter, CategoryList
from loader import dp, bot
from states.states import ChooseCategory
from aiogram.dispatcher import FSMContext
from aiogram.utils.exceptions import InvalidHTTPUrlContent, RetryAfter
from keyboards.default.new_keyboard import keyboard
from aiogram.dispatcher.filters import Text, Command
from .category import something

temp: str = ""


@dp.message_handler(state=ChooseCategory.stateChoosingCat)
async def set_category(message: types.Message):
    global temp
    for_check = message.text.capitalize()
    if for_check in CategoryList:
        await message.answer(
            f"Вы выбрали: {message.text}\nТеперь укажите количество картинок которое хотите получить (не больше 100)")
        temp = for_check
        await ChooseCategory.stateChoosingCount.set()
    else:
        await message.answer('Такой категории нет, возможно вы ввели цифру или допустили орфографическую ошибку\nВы можете попробовать снова ;)')


@dp.message_handler(state=ChooseCategory.stateChoosingCount)
async def set_count(message: types.Message, state: FSMContext):
    global temp
    parsed_pictures = PictureGeter.get_list_with_pictures(int(message.text), temp)
    print(parsed_pictures)
    for url_link in parsed_pictures:
        try:
            await bot.send_photo(chat_id=message.chat.id, photo=url_link)
        except InvalidHTTPUrlContent:
            pass
    await state.finish()
    await message.answer("Хотите выбрать еще одну категорию ?", reply_markup=keyboard)


@dp.message_handler(Text(equals=["Да"]))
async def reply_on(message: types.Message):
    await message.answer("Как пожелаете =)", reply_markup=types.ReplyKeyboardRemove())
    await something(message)
    await ChooseCategory.stateChoosingCat.set()


@dp.message_handler(Text(equals=["Нет"]))
async def reply_on(message: types.Message):
    await message.answer("Мы благодарны за то что вы используете нашего бота ;)", reply_markup=types.ReplyKeyboardRemove())

