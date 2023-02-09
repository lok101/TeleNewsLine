from aiogram import Bot
from aiogram.types import callback_query, message
from aiogram.utils.keyboard import InlineKeyboardBuilder as KeyBuilder

from navigations.data_classes import FactoryEmptyButton, FactoryDefaultButton, FactoryBackButton


class Create:
    @staticmethod
    async def start_menu(message: message, bot: Bot): ...

    @staticmethod
    async def send_menu_on_button_click(
            callback: callback_query,
            callback_data: (FactoryDefaultButton, FactoryEmptyButton),
            bot: Bot
    ) -> None: ...

    @staticmethod
    async def send_menu_on_back_button_click(
            callback: callback_query,
            callback_data: FactoryBackButton,
            bot: Bot
    ) -> None: ...

    @staticmethod
    def keyboard(
            page_name: str,
            user_id: str
    ) -> KeyBuilder.as_markup: ...

    @staticmethod
    def add_back_button(keyboard: KeyBuilder, page_name: str, user_id: str) -> KeyBuilder: ...
