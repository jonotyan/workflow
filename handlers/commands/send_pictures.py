from aiogram import types
from utils.parser.web_requests import PictureGeter
from loader import dp, bot
from states.states import ChooseCategory
from aiogram.dispatcher import FSMContext
from aiogram.utils.exceptions import InvalidHTTPUrlContent, WrongFileIdentifier, RetryAfter
from keyboards.default.new_keyboard import keyboard
from keyboards.inline.inline_category_choosing import init_keyboard, keyboard_inline, switch_page_on_back, switch_page_on_next, reset_keyboard
from aiogram.dispatcher.filters import Text
from .category import category_command_respond
from data.config import ADMINS
from LowLevelModuls.messages import set_category


@dp.callback_query_handler(text=["switch_page_on_next", "switch_page_on_back"])
async def get_answer(call: types.CallbackQuery):
    if call.data == "switch_page_on_next":
        await reset_keyboard(await init_keyboard(await switch_page_on_next()))
    elif call.data == "switch_page_on_back":
        await reset_keyboard(await init_keyboard(await switch_page_on_back()))
    await call.answer()


@dp.message_handler(state=ChooseCategory.stateChoosingCat)
async def get_category_chosen_by_user(message: types.Message):
    await message.answer("sfs", reply_markup=await init_keyboard(1))

    # global temp
    # results_of_settings = await set_category(message)
    #
    # if results_of_settings[1]:
    #     await ChooseCategory.stateChoosingCount.set()
    #
    # temp = results_of_settings[2]
    #
    # await message.answer(results_of_settings[0])


@dp.errors_handler(exception=RetryAfter)
@dp.message_handler(state=ChooseCategory.stateChoosingCount)
async def set_count(message: types.Message, state: FSMContext):
    if int(message.text) > 100:
        await message.answer("Дайте мне немного времени")
    parsed_pictures = PictureGeter.get_list_with_urls_on_pictures(int(message.text), temp)
    print(parsed_pictures)
    for url_link in parsed_pictures:
        try:
            await bot.send_photo(chat_id=message.chat.id, photo=url_link)
        except InvalidHTTPUrlContent or WrongFileIdentifier or AttributeError:
            pass

    await state.finish()
    await message.answer("Хотите выбрать еще одну категорию ?", reply_markup=keyboard)


@dp.message_handler(Text(equals=["Да"]))
async def reply_on(message: types.Message):
    await message.answer("Как пожелаете =)", reply_markup=types.ReplyKeyboardRemove())
    await category_command_respond(message)
    await ChooseCategory.stateChoosingCat.set()


@dp.message_handler(Text(equals=["Нет"]))
async def reply_on(message: types.Message):
    await message.answer("Мы благодарны за то что вы используете нашего бота ;)", reply_markup=types.ReplyKeyboardRemove())


@dp.message_handler(commands=['Get_DataBase'])
async def get_data_base(message: types.Message):
    if message.chat.id == int(ADMINS[0]):
        db = "d"
        await message.answer(db)
    else:
        await message.answer("Ты золотце, если ты видишь это сообщение значит все работает как нада)")
        print(message.chat.id)
