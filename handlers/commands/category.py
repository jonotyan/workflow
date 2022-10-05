from aiogram import types
from utils.parser.web_requests import CategoryDict
from states.states import ChooseCategory
from loader import dp

# TODO: переименовать функцию\done


# async def show_available_categories(message):
#     text = ''
#     num = 0
#     for category in CategoryDict:
#         num += 1
#         text += f"{num}: {category}\n"
#     await message.answer(text)


@dp.message_handler(commands=['category'])
async def category_command_respond(message: types.Message):
    await message.answer("Этот бот имеет в себе очень много разных категорий, вы можете выбрать любую из ниже перечисленных:")
    await ChooseCategory.stateChoosingCat.set()
