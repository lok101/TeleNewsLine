from typing import Union

from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

from exceptions import EmptyTransitionStack
from navigations.data_classes import *
from navigations.menu_constructor.main import BotMenu
from menu_structure.user_pages import menu_pages
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
        self._set_session_data(tg_response_data, callback_data)
        self._set_message_data()

    def handel_back_button_press(self):
        try:
            NAV_HISTORY.replace_last_position(self)
        except EmptyTransitionStack:
            NAV_HISTORY.add_start_position_in_stack(self)
            self.set_start_menu_in_current_page_name()

    def set_start_menu_in_current_page_name(self):
        self.current_page_name = menu_pages[0].page_name

    def _set_session_data(self, tg_response_data, callback_data):
        if isinstance(tg_response_data, types.Message):
            self._set_data_for_message_type(tg_response_data)
        elif isinstance(tg_response_data, types.CallbackQuery) and callback_data is not None:
            self._set_data_for_callback_type(tg_response_data, callback_data)
        else:
            raise Exception('Неизвестный тип сообщения, или не передан callback_data.')

    def _set_message_data(self):
        self.text = 'TEST MESSAGE'
        self.reply_markup = self._default_keyboard()

    def _set_data_for_message_type(self, message: types.Message):
        self.user_id = message.from_user.id
        self.message_id = message.message_id
        self.chat_id = message.chat.id
        self.current_page_name = menu_pages[0].page_name
        self.stack_key = int(f'{message.from_user.id}{message.message_id + 1}')

    def _set_data_for_callback_type(self, callback: types.CallbackQuery, callback_data: BaseFactoryButton = None):
        self.user_id = callback.from_user.id
        self.message_id = callback.message.message_id
        self.chat_id = callback.message.chat.id
        self.stack_key = int(f'{callback.from_user.id}{callback.message.message_id}')
        self.current_page_name = callback_data.page_name
        self.previous_page_name = NAV_HISTORY.get_previous_position_in_stack(self)

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

                    btns.append(InlineKeyboardButton(text=text, callback_data=builder(page_name=callback).pack()))
                self.keyboard.row(*btns)
            else:
                text = button.name
                callback = button.callback
                builder = set_button_builder[button.__class__.__name__]

                self.keyboard.row(InlineKeyboardButton(text=text, callback_data=builder(page_name=callback).pack()))

        self._add_back_button()
        self._add_my_profile_button()

        return self.keyboard.as_markup()

    def _add_back_button(self):
        """ Добавляет кнопку "назад" в клавиатуру. """

        page_name = bot_menu[self.current_page_name]['page_name']
        name_start_menu = menu_pages[0].page_name
        if page_name != name_start_menu:
            self.keyboard.row(InlineKeyboardButton(
                text='➖                                   Назад                                   ➖',
                callback_data=FactoryBackButton(page_name=self.previous_page_name).pack()))

    def _add_my_profile_button(self):
        """ Добавляет кнопку "мой профиль" в клавиатуру. """

        start_page = menu_pages[0].page_name
        if self.current_page_name == start_page:
            self.keyboard.row(InlineKeyboardButton(
                text='➖                            Мой профиль.                            ➖',
                callback_data=FactoryDefaultButton(page_name='my_profile').pack()))
