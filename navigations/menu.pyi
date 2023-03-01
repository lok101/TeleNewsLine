from aiogram import Bot
from aiogram.types import callback_query, message
from aiogram.utils.keyboard import InlineKeyboardBuilder as KeyBuilder

from navigations.data_classes import FactoryEmptyButton, FactoryDefaultButton


class Create:

    async def start_menu(self, message: message, bot: Bot) -> None: ...


    async def send_menu_on_button_click(
            self,
            callback: callback_query,
            callback_data: (FactoryDefaultButton, FactoryEmptyButton),
            bot: Bot
    ) -> None: ...


    def _default_keyboard(
            self: Create,
            page_name: str,
            user_id: str
    ) -> KeyBuilder.as_markup: ...

    @staticmethod
    def _add_back_button(keyboard: KeyBuilder, page_name: str, user_id: str) -> None: ...

    @staticmethod
    def _add_my_profile_button(keyboard: KeyBuilder, page_name: str) -> None: ...
