from aiogram.types import callback_query
from aiogram.utils.keyboard import InlineKeyboardBuilder

from data_classes import NavButtonCallback
from pages import nav
from navigations.control import controller


class Create:
    @staticmethod
    async def start_menu(message, bot):
        """ Высылает стартовое меню в ответ на команду. """
        chat_id = message.chat.id
        await bot.send_message(
            chat_id=chat_id,
            text='Hello Test',
            reply_markup=Create.keyboard('start_menu', chat_id),
            parse_mode="Markdown"
        )

    @staticmethod
    async def send_menu_from_callback(callback: callback_query, callback_data: NavButtonCallback, bot) -> None:
        """ Высылает необходимое меню в ответ на callback. """
        chat_id = callback.message.chat.id
        message_id = callback.message.message_id

        page_name = callback_data.page_name
        activate_back_btn = callback_data.button_is_back
        keyboard = Create.keyboard(page_name, chat_id, activate_back_btn)

        await bot.edit_message_text(
            chat_id=chat_id,
            message_id=message_id,
            text='Hello Test',
            reply_markup=keyboard,
            parse_mode="Markdown"
        )

    @staticmethod
    def keyboard(page_name: str, chat_id: str, activate_back_btn=False) -> InlineKeyboardBuilder.as_markup:
        """ Формирует клавиатуру для страницы с переданным адресом. """
        keyboard = InlineKeyboardBuilder()
        buttons = nav[page_name]['buttons']

        for key, value in buttons.items():
            keyboard.button(text=key, callback_data=NavButtonCallback(page_name=value, is_back=False))
        Create.add_back_button(keyboard, page_name, chat_id, activate_back_btn)
        keyboard.adjust(1)

        return keyboard.as_markup()

    @staticmethod
    def add_back_button(keyboard: InlineKeyboardBuilder, page_name: str, chat_id: str, activate_back_btn: bool):
        """ Добавляет кнопку назад в клавиатуру. """
        if activate_back_btn is True:
            controller.stack.delete_last_position(chat_id)

        previous_menu = controller.stack.get_last_position(chat_id=chat_id)
        current_menu = nav[page_name]['current_menu']

        if previous_menu is not None and current_menu != previous_menu:
            keyboard.button(text='Назад', callback_data=NavButtonCallback(page_name=previous_menu, is_back=True))
        controller.stack.set_new_last_position(chat_id=chat_id, position=current_menu)

        return keyboard
