from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Да"),
         KeyboardButton(text="Нет")]
    ], resize_keyboard=True
)