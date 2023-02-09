from aiogram.utils.keyboard import InlineKeyboardBuilder

from navigations.control import controller
from navigations.data_classes import FactoryBackButton, DefaultMenuButton, EmptyMenuButton
from navigations.pages import nav
from navigations import control


class Create:
    @staticmethod
    async def start_menu(message, bot):
        """ Высылает стартовое меню в ответ на команду. """
        chat_id = message.chat.id
        user_id = message.from_user.id
        keyboard = Create.keyboard(
            page_name='start_menu',
            user_id=user_id)

        await bot.send_message(
            chat_id=chat_id,
            text='Hello Test',
            reply_markup=keyboard,
            parse_mode="Markdown"
        )

    @staticmethod
    async def send_menu_from_callback(callback, callback_data, bot):
        """ Высылает необходимое меню в ответ на callback. """
        chat_id = callback.message.chat.id
        user_id = callback.from_user.id
        message_id = callback.message.message_id

        page_name = callback_data.page_name
        activate_back_btn = callback_data.button_is_back

        keyboard = Create.keyboard(
            page_name=page_name,
            user_id=user_id,
            activate_back_btn=activate_back_btn)

        await bot.edit_message_text(
            chat_id=chat_id,
            message_id=message_id,
            text='Hello Test',
            reply_markup=keyboard,
            parse_mode="Markdown"
        )

    @staticmethod
    def keyboard(page_name, user_id, activate_back_btn=False):
        """ Формирует клавиатуру для страницы с переданным адресом. """
        keyboard = InlineKeyboardBuilder()
        buttons: list[DefaultMenuButton, EmptyMenuButton] = nav[page_name]['buttons']

        for button in buttons:
            text = button.name
            callback = button.callback
            builder = control.set_button_builder(button)

            keyboard.button(text=text, callback_data=builder(page_name=callback, button_is_back=False))

        Create.add_back_button(keyboard, page_name, user_id, activate_back_btn)
        keyboard.adjust(1)

        return keyboard.as_markup()

    @staticmethod
    def add_back_button(keyboard, page_name, user_id, activate_back_btn):
        """ Добавляет кнопку назад в клавиатуру. """
        if activate_back_btn is True:
            controller.stack.delete_last_position(user_id)

        previous_menu = controller.stack.get_last_position(user_id=user_id)
        current_menu = nav[page_name]['current_menu']

        if previous_menu is not None and current_menu != previous_menu:
            keyboard.button(text='Назад', callback_data=FactoryBackButton(page_name=previous_menu, button_is_back=True))
        controller.stack.set_new_last_position(user_id=user_id, position=current_menu)

        return keyboard
