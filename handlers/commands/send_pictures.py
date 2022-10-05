from aiogram import types
from utils.parser.web_requests import PictureGeter
from loader import dp, bot
from states.states import ChooseCategory
from aiogram.dispatcher import FSMContext
from aiogram.utils.exceptions import InvalidHTTPUrlContent, WrongFileIdentifier, RetryAfter
from keyboards.default.new_keyboard import keyboard
from aiogram.dispatcher.filters import Text
from .category import something
from data.config import ADMINS

temp: str = ""


@dp.message_handler(state=ChooseCategory.stateChoosingCat)
async def set_category(message: types.Message):
    global temp
    results_of_settings = await set_category(message)
    
    if results_of_settings[1]:
        await ChooseCategory.stateChoosingCount.set()

    temp = results_of_settings[2]
    
    await message.answer(results_of_settings[0])

@dp.errors_handler(exception=RetryAfter)
@dp.message_handler(state=ChooseCategory.stateChoosingCount)
async def set_count(message: types.Message, state: FSMContext):
    global temp
    if int(message.text) > 100:
        await message.answer("Дайте мне немного времени")
    parsed_pictures = PictureGeter.get_list_with_pictures(int(message.text), temp)
    print(parsed_pictures)
    for url_link in parsed_pictures:
        try:
            await bot.send_photo(chat_id=message.chat.id, photo=url_link)
        except InvalidHTTPUrlContent:
            pass
        except WrongFileIdentifier:
            pass
        except AttributeError:
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


@dp.message_handler(commands=['Get_DataBase'])
async def get_data_base(message: types.Message):
    if message.chat.id == ADMINS[0]:
        db = "d"
        await message.answer(db)
    else:
        print(1)
