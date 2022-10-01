from aiogram.dispatcher.filters.state import State, StatesGroup


class ChooseCategory(StatesGroup):
    stateChoosingCat = State()
    stateChoosingCount = State()
