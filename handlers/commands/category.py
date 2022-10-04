from aiogram import types
from utils.parser.web_requests import CategoryList
from states.states import ChooseCategory
from loader import dp


async def something(message):
    text = ''
    num = 0
    for category in CategoryList:
        num += 1
        text += f"{num}: {category}\n"
    await message.answer(text)


@dp.message_handler(commands=['category'])
async def show_available_categories(message: types.Message):
    await message.answer("Этот бот имеет в себе очень много разных категорий, вы можете выбрать любую из ниже перечисленных:")
    await something(message)
    await ChooseCategory.stateChoosingCat.set()
