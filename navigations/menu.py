from aiogram.utils.keyboard import InlineKeyboardBuilder

from control import controller
from navigations.data_classes import FactoryBackButton, ButtonDefault, ButtonEmpty, MenuPage
import control
from navigations.user_pages import menu_pages


class BotMenu(dict):
    def add_pages(self, pages: list[MenuPage]):
        for page in pages:
            self.update(page.get_page())


bot_menu = BotMenu()
bot_menu.add_pages(menu_pages)


class Create:
    is_back_button_click: bool = False

    async def start_menu(self, message, bot):
        """ Высылает стартовое меню в ответ на команду. """
        chat_id = message.chat.id
        user_id = message.from_user.id
        keyboard = self.default_keyboard(
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

        keyboard = self.default_keyboard(
            page_name=page_name,
            user_id=user_id)

        await bot.edit_message_text(
            chat_id=chat_id,
            message_id=message_id,
            text='Hello Test',
            reply_markup=keyboard,
            parse_mode="Markdown"
        )

    def default_keyboard(self, page_name, user_id):
        """ Формирует клавиатуру для страницы с переданным адресом. """
        keyboard = InlineKeyboardBuilder()
        buttons: list[ButtonDefault, ButtonEmpty] = bot_menu[page_name]['buttons']

        for button in buttons:
            text = button.name
            callback = button.callback
            builder = control.set_button_builder[button.__class__.__name__]

            keyboard.button(text=text, callback_data=builder(page_name=callback))

        self.add_back_button(keyboard, page_name, user_id)
        keyboard.adjust(1)

        return keyboard.as_markup()

    def add_back_button(self, keyboard, page_name, user_id):
        """ Добавляет кнопку назад в клавиатуру. """
        if self.is_back_button_click is True:
            controller.stack.delete_last_position(user_id)

        previous_menu = controller.stack.get_last_position(user_id=user_id)
        page_name = bot_menu[page_name]['page_name']

        if previous_menu is not None and page_name != previous_menu:
            keyboard.button(text='Назад', callback_data=FactoryBackButton(page_name=previous_menu))
        controller.stack.set_new_last_position(user_id=user_id, position=page_name)

        return keyboard
