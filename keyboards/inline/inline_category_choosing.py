from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from utils.parser.web_requests import CategoryDict

keyboard_inline = InlineKeyboardMarkup(row_width=3)
on_page = 1


async def reset_keyboard(keyboard: InlineKeyboardMarkup):
    global keyboard_inline
    keyboard_inline = keyboard


async def switch_page_on_next():
    global on_page
    on_page += 1
    if on_page >= 6:
        on_page = 1
    print(on_page)
    return on_page


async def switch_page_on_back():
    global on_page
    on_page -= 1
    on_page += 1
    if on_page <= 0:
        on_page = 5
    return on_page


async def clear_keyboard():
    global keyboard_inline
    keyboard_inline = InlineKeyboardMarkup(row_width=3)


async def create_and_add_next_button():
    button_next = InlineKeyboardButton(text="Далее", callback_data="switch_page_on_next")
    keyboard_inline.add(button_next)


async def create_and_add_page_buttons():
    button_back = InlineKeyboardButton(text="Назад", callback_data="switch_page_on_back")
    keyboard_inline.add(button_back)
    await create_and_add_next_button()


async def show_page(page: int):
    buttons = []
    await clear_keyboard()
    for key, value in CategoryDict.items():
        if value == page:
            button = InlineKeyboardButton(text=key, callback_data="None")
            buttons.append(button)
    keyboard_inline.add(*buttons)


async def init_keyboard(num):
    await show_page(num)
    await create_and_add_next_button()
    return keyboard_inline
