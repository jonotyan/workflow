# from aiogram import types
# from states.states import StatesGroup
# from loader import dp, bot
#
#
# @dp.message_handler(commands=['for_u'])
# async def category_command_respond(message: types.Message):
#     print(0)
#     await bot.send_message(text="Отправь боту любое сообщение ;)", chat_id=message.chat.id)
#     await StatesGroup.stateInSpecialCommand.set()