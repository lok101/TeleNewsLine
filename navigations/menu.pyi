from aiogram import Bot
from aiogram.types import callback_query, message
from aiogram.utils.keyboard import InlineKeyboardBuilder as KeyBuilder

from navigations.data_classes import FactoryEmptyButton, FactoryDefaultButton, FactoryBackButton


class Create:
    is_back_button_click: bool = False

    async def start_menu(self: Create, message: message, bot: Bot) -> None: ...


    async def send_menu_on_button_click(
            self: Create,
            callback: callback_query,
            callback_data: (FactoryDefaultButton, FactoryEmptyButton),
            bot: Bot
    ) -> None: ...

    async def send_menu_on_back_button_click(
            self: Create,
            callback: callback_query,
            callback_data: FactoryBackButton,
            bot: Bot
    ) -> None: ...

    def default_keyboard(
            self: Create,
            page_name: str,
            user_id: str
    ) -> KeyBuilder.as_markup: ...

    def add_back_button(self: Create, keyboard: KeyBuilder, page_name: str, user_id: str) -> KeyBuilder: ...
