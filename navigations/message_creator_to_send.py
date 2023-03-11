from typing import Union

from aiogram import types
from aiogram.utils.keyboard import InlineKeyboardBuilder

from exceptions import EmptyTransitionStack
from menu_structure.user_pages import menu_pages
from logger import logger
from navigations.data_classes import FactoryDefaultButton, SessionData, FactoryNewChannelButton, FactoryEmptyButton, \
    FactoryProductButton, FactoryNavButton, BaseFactoryButton, BaseButton, FactoryBackButton
from navigations.menu_constructor.main import BotMenu
from navigations.transition_stack import NAV_HISTORY

bot_menu = BotMenu()
set_button_builder = {
    'ButtonDefault': FactoryDefaultButton,
    'ButtonNewChannel': FactoryNewChannelButton,
    'ButtonEmpty': FactoryEmptyButton,
    'ButtonProduct': FactoryProductButton,
    'ButtonNav': FactoryNavButton,

}


class MessageCreator(SessionData):
    def __init__(
            self, tg_response_data: Union[types.CallbackQuery, types.Message], callback_data: BaseFactoryButton = None
    ):
        self._set_response_data(tg_response_data, callback_data)
        self._set_transition_stack_key()
        self._set_current_menu()

    def handel_back_button_press(self):
        try:
            NAV_HISTORY.delete_position_in_stack(self)
        except EmptyTransitionStack:
            logger.debug('Нажатие на устаревшую кнопку "назад".')
            NAV_HISTORY.add_start_position_in_stack(self)

    def set_session_and_message_data(self):
        self.user_id = self.message.from_user.id
        self.message_id = self.message.message_id
        self.chat_id = self.message.chat.id
        self.previous_page_name = NAV_HISTORY.get_previous_position_in_stack(self)
        self.text = 'TEST MESSAGE'
        self.reply_markup = self._default_keyboard()

    def _set_response_data(self, tg_response_data, callback_data):
        if isinstance(self.tg_response_data, types.Message):
            message = tg_response_data
        else:
            message = tg_response_data.message
        self.message = message
        self.tg_response_data = tg_response_data
        self.callback_data = callback_data

    def _set_transition_stack_key(self):
        if isinstance(self.tg_response_data, types.Message):
            user_id, message_id = self.tg_response_data.from_user.id, self.tg_response_data.message_id + 1
        elif isinstance(self.tg_response_data, types.CallbackQuery) and self.callback_data is not None:
            user_id, message_id = self.tg_response_data.from_user.id, self.tg_response_data.message.message_id
        else:
            raise Exception('Неизвестный тип сообщения, или не передан callback_data.')

        self.stack_key = int(f'{user_id}{message_id}')

    def _set_current_menu(self):
        if self.callback_data is not None:
            self.current_page_name = self.callback_data.page_name
        else:
            self.current_page_name = menu_pages[0].page_name

    def _default_keyboard(self):
        """ Формирует клавиатуру для страницы с переданным адресом. """

        self.keyboard = InlineKeyboardBuilder()
        buttons: list[BaseButton] = bot_menu[self.current_page_name]['buttons']

        for button in buttons:
            if isinstance(button, tuple):
                button_row = button
                btns = list()
                for btn in button_row:
                    text = btn.name
                    callback = btn.callback
                    builder = set_button_builder[btn.__class__.__name__]

                    btns.append(
                        types.InlineKeyboardButton(text=text, callback_data=builder(page_name=callback).pack())
                    )
                self.keyboard.row(*btns)
            else:
                text = button.name
                callback = button.callback
                builder = set_button_builder[button.__class__.__name__]

                self.keyboard.row(
                    types.InlineKeyboardButton(text=text, callback_data=builder(page_name=callback).pack())
                )

        self._add_back_button()
        self._add_my_profile_button()

        return self.keyboard.as_markup()

    def _add_back_button(self):
        """ Добавляет кнопку "назад" в клавиатуру. """

        name_start_menu = menu_pages[0].page_name
        if self.current_page_name != name_start_menu:
            self.keyboard.row(types.InlineKeyboardButton(
                text='➖                                   Назад                                   ➖',
                callback_data=FactoryBackButton(page_name=self.previous_page_name).pack()))

    def _add_my_profile_button(self):
        """ Добавляет кнопку "мой профиль" в клавиатуру. """

        start_page = menu_pages[0].page_name
        if self.current_page_name == start_page:
            self.keyboard.row(types.InlineKeyboardButton(
                text='➖                            Мой профиль.                            ➖',
                callback_data=FactoryDefaultButton(page_name='my_profile').pack()))
