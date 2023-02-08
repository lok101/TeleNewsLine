from aiogram.filters.callback_data import CallbackData


class NavButtonCallback(CallbackData, prefix="nav"):
    page_name: str
    button_is_back: bool
