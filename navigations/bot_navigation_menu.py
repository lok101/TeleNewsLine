from typing import Union

from navigations.data_classes import BaseButton, ProductMenu
from navigations.user_products import products


class MenuPage:
    def __init__(self, page_name: str, message_text: str,
                 buttons: Union[list[BaseButton] | ProductMenu] = ProductMenu()):
        self.page_name = page_name
        self.message_text = message_text
        if isinstance(buttons, ProductMenu):
            self.buttons = [button.get_product_button() for button in products[page_name]]
        else:
            self.buttons = buttons

    def get_page(self) -> dict:
        return {self.page_name: self.__dict__}