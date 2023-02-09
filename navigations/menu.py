from aiogram.utils.keyboard import InlineKeyboardBuilder

from navigations.control import controller
from navigations.data_classes import FactoryBackButton, DefaultMenuButton, EmptyMenuButton
from navigations.pages import nav
from navigations import control


class Create:
    is_back_button_click = False

    def __int__(self, is_back_button_click=False):
        self.is_back_button_click = is_back_button_click

    async def start_menu(self, message, bot):
        """ Высылает стартовое меню в ответ на команду. """
        chat_id = message.chat.id
        user_id = message.from_user.id
        keyboard = self.keyboard(
            page_name='start_menu',
            user_id=user_id)

        await bot.send_message(
            chat_id=chat_id,
            text='Hello Test',
            reply_markup=keyboard,
            parse_mode="Markdown"
        )

    async def send_menu_on_button_click(self, callback, callback_data, bot):
        """ Высылает необходимое меню в ответ на нажатие DefaultButton. """
        chat_id = callback.message.chat.id
        user_id = callback.from_user.id
        message_id = callback.message.message_id

        page_name = callback_data.page_name

        keyboard = self.keyboard(
            page_name=page_name,
            user_id=user_id)

        await bot.edit_message_text(
            chat_id=chat_id,
            message_id=message_id,
            text='Hello Test',
            reply_markup=keyboard,
            parse_mode="Markdown"
        )

    def keyboard(self, page_name, user_id):
        """ Формирует клавиатуру для страницы с переданным адресом. """
        keyboard = InlineKeyboardBuilder()
        buttons: list[DefaultMenuButton, EmptyMenuButton] = nav[page_name]['buttons']

        for button in buttons:
            text = button.name
            callback = button.callback
            builder = control.set_button_builder(button)

            keyboard.button(text=text, callback_data=builder(page_name=callback))

        self.add_back_button(keyboard, page_name, user_id)
        keyboard.adjust(1)

        return keyboard.as_markup()

    def add_back_button(self, keyboard, page_name, user_id):
        """ Добавляет кнопку назад в клавиатуру. """
        if self.is_back_button_click is True:
            controller.stack.delete_last_position(user_id)

        previous_menu = controller.stack.get_last_position(user_id=user_id)
        current_menu = nav[page_name]['current_menu']

        if previous_menu is not None and current_menu != previous_menu:
            keyboard.button(text='Назад', callback_data=FactoryBackButton(page_name=previous_menu))
        controller.stack.set_new_last_position(user_id=user_id, position=current_menu)

        return keyboard
