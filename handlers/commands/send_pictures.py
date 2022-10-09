from aiogram import types
from utils.parser.web_requests import CategoryDict
from loader import dp, bot
from states.states import StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.utils.exceptions import InvalidHTTPUrlContent, WrongFileIdentifier, RetryAfter
from keyboards.default.reply_keyboard import keyboard_continue_or_stop
from keyboards.inline.inline_keyboard_for_category_choosing import init_keyboard, switch_page_on_back, switch_page_on_next
from aiogram.dispatcher.filters import Text
from .category import category_command_respond
from data.config import IS_ADMIN
from LowLevelModuls.messages import set_category_for_parser_and_run
from ..vars_for_handlers.vars import *


@dp.callback_query_handler(text=["switch_page_on_next", "switch_page_on_back"], state=StatesGroup.stateChoosingCat)
async def page_buttons(call: types.CallbackQuery):
    if call.data == "switch_page_on_next":
        now_on_page = await switch_page_on_next()
        new_keyboard = await init_keyboard(now_on_page)
        await call.message.edit_reply_markup(reply_markup=new_keyboard)

    elif call.data == "switch_page_on_back":
        now_on_page = await switch_page_on_back()
        new_keyboard = await init_keyboard(now_on_page)
        await call.message.edit_reply_markup(reply_markup=new_keyboard)


@dp.callback_query_handler(text=CategoryDict.keys(), state=StatesGroup.stateChoosingCat)
async def get_category_chosen_by_user(call: types.CallbackQuery):
    await set_temp_category(call.data)
    await call.answer(f"Выбрана категория : {call.data}")
    await bot.delete_message(message_id=await get_message_id_to_edit(), chat_id=call.from_user.id)
    await bot.send_message(chat_id=call.from_user.id, text=f"Вы выбрали категорию: {call.data} =)")
    await bot.send_message(chat_id=call.from_user.id, text="А теперь введите количество желаемых картинок ;)")
    await StatesGroup.stateChoosingCount.set()


@dp.errors_handler(exception=RetryAfter)
@dp.message_handler(state=StatesGroup.stateChoosingCount)
async def set_count(message: types.Message, state: FSMContext):
    await set_category_for_parser_and_run(message)
    await state.finish()
    await message.answer("Хотите выбрать еще одну категорию ?", reply_markup=keyboard_continue_or_stop)
    await StatesGroup.stateContinueOrStop.set()


@dp.message_handler(Text(equals=["Да"]), state=StatesGroup.stateContinueOrStop)
async def reply_on(message: types.Message):
    await message.answer("Как пожелаете =)", reply_markup=types.ReplyKeyboardRemove())
    await category_command_respond(message)


@dp.message_handler(Text(equals=["Нет"]), state=StatesGroup.stateContinueOrStop)
async def reply_on(message: types.Message, state: FSMContext):
    await message.answer("Мы благодарны за то что вы используете нашего бота ;)", reply_markup=types.ReplyKeyboardRemove())
    await state.finish()


@dp.message_handler(commands=['Get_DataBase'])
async def get_data_base(message: types.Message):
    if IS_ADMIN(message.chat.id):
        db = "d"
        await message.answer(db)
    else:
        await message.answer("У вас нет на это прав ;)")

