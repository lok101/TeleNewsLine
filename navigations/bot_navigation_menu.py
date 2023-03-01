from typing import Union

from navigations.data_classes import BaseButton, ProductMenu, ButtonEmpty
from navigations.user_products import products
from settings import menu_height


class MenuPage:
    def __init__(self, page_name: str, message_text: str,
                 buttons: Union[list[BaseButton] | ProductMenu] = ProductMenu()):
        self.page_name = page_name
        self.message_text = message_text
        self.buttons = self.create_buttons_menu(buttons, page_name)

    @staticmethod
    def create_buttons_menu(buttons: Union[list[BaseButton] | ProductMenu], page_name: str):
        if isinstance(buttons, ProductMenu):
            buttons = [button.get_product_button() for button in products[page_name]]
        if menu_height - len(buttons) < 0:
            raise Exception(f'Превышен размер меню в {page_name}. '
                            f'Увеличьте допустимый размер меню в настройках '
                            f'или уменьшите количество кнопок в меню {page_name}')
        for _ in range(menu_height - len(buttons)):
            buttons.append(ButtonEmpty())
        return buttons

    def get_page(self) -> dict:
        return {self.page_name: self.__dict__}
