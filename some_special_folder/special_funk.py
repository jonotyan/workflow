from aiogram import types
from states.states import StatesGroup
from loader import dp
from aiogram.dispatcher import FSMContext
from data.config import IS_ADMIN


@dp.message_handler(state=StatesGroup.stateInSpecialCommand)
async def category_command_respond(msg: types.Message, state: FSMContext):
    if IS_ADMIN(msg.chat.id):
        print(0)
        with open("W:/for_her.txt", "r") as file:
            line = file.read()
            await msg.answer(line)
            file.close()
    else:
        await state.finish()