from aiogram import types
from .web_requests import CategoryList
from states.states import ChooseCategory
from loader import dp


@dp.message_handler(commands=['category'])
async def show_available_categories(message: types.Message):
    text = ''
    num = 0
    await message.answer("Этот бот имеет в себе очень много разных категорий, вы можете выбрать любую из ниже перечисленных:")
    for category in CategoryList:
        num +=1
        text += f"{num}: {category}\n"
    await message.answer(text)
    await ChooseCategory.stateChoosingCat.set()
