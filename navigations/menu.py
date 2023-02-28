from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

from control import controller
from navigations.bot_navigation_menu import MenuPage
from navigations.bot_navigation_products import Product
from navigations.data_classes import FactoryBackButton, BaseButton
import control
from navigations.user_pages import menu_pages
from navigations.user_products import products
import logging
from logger import logger


class BotMenu(dict):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.add_pages(menu_pages)
        self.add_products(products)

    def add_pages(self, pages: list[MenuPage]):
        for page in pages:
            self.update(page.get_page())

    def add_products(self, products: dict[Product]):
        for product_button_list in products.values():
            for product in product_button_list:
                self.update(product.get_product())


bot_menu = BotMenu()


class Create:
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
        buttons: list[BaseButton] = bot_menu[page_name]['buttons']

        for button in buttons:
            if isinstance(button, tuple):
                button_row = button
                btns = list()
                for button in button_row:
                    text = button.name
                    callback = button.callback
                    builder = control.set_button_builder[button.__class__.__name__]

                    btns.append(InlineKeyboardButton(text=text, callback_data=builder(page_name=callback).pack()))
                keyboard.row(*btns)
            else:
                text = button.name
                callback = button.callback
                builder = control.set_button_builder[button.__class__.__name__]

                keyboard.row(InlineKeyboardButton(text=text, callback_data=builder(page_name=callback).pack()))

        self._add_back_button(keyboard, page_name, user_id)
        logger.debug(controller.stack.data)

        return keyboard.as_markup()

    @staticmethod
    def _add_back_button(keyboard, page_name, user_id):
        """ Добавляет кнопку назад в клавиатуру. """

        previous_menu = controller.stack.get_previous_position_in_stack(user_id=user_id)
        page_name = bot_menu[page_name]['page_name']

        if previous_menu is not None and page_name != previous_menu:
            keyboard.row(InlineKeyboardButton(
                text='➖                                        Назад                                        ➖',
                callback_data=FactoryBackButton(page_name=previous_menu).pack()))

        return keyboard
