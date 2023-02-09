from aiogram import Bot
from aiogram.types import callback_query, message
from aiogram.utils.keyboard import InlineKeyboardBuilder as KeyBuilder

from navigations.data_classes import FactoryEmptyButton, FactoryDefaultButton


class Create:
    @staticmethod
    async def start_menu(message: message, bot: Bot): ...

    @staticmethod
    async def send_menu_from_callback(
            callback: callback_query,
            callback_data: (FactoryDefaultButton, FactoryEmptyButton),
            bot: Bot
    ) -> None: ...

    @staticmethod
    def keyboard(
            page_name: str,
            user_id: str,
            activate_back_btn: bool = False
    ) -> KeyBuilder.as_markup: ...

    @staticmethod
    def add_back_button(keyboard: KeyBuilder, page_name: str, user_id: str, activate_back_btn: bool) -> KeyBuilder: ...
