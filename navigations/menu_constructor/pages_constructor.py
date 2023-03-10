import math

from navigations.data_classes import BaseButton, ButtonEmpty, ButtonNav
from menu_structure.user_products import products
import settings


class Page:
    def get_page(self) -> dict: pass


class DefaultPage(Page):
    def __init__(self, page_name: str, message_text: str, buttons: list[BaseButton]):
        self.page_name = page_name
        self.message_text = message_text
        self.buttons = self._create_buttons_menu(buttons, page_name)

    def get_page(self) -> dict:
        return {self.page_name: self.__dict__}

    @staticmethod
    def _create_buttons_menu(buttons: list[BaseButton], page_name: str):
        if settings.menu_height < len(buttons):
            raise Exception(f'Превышен размер меню в {page_name}. '
                            f'Увеличьте допустимый размер меню в настройках '
                            f'или уменьшите количество кнопок в меню {page_name}')
        for _ in range(settings.menu_height - len(buttons)):
            buttons.append(ButtonEmpty())
        return buttons


class ProductPage(Page):
    def __init__(self, page_name: str, message_text: str):
        self.height = settings.menu_height - 1
        self.page_amount = None
        self.page_number = None
        self.page_name = page_name
        self.message_text = message_text

        self.buttons = self._load_buttons()
        self.pages = self._create_pages()
        self._add_buttons_in_pages()

    def get_page(self) -> dict:
        return self.pages

    def _load_buttons(self):
        buttons = [button.get_product_button() for button in products[self.page_name]]
        self.page_amount = math.ceil(len(buttons) / self.height)
        needed_buttons = self.page_amount * self.height - len(buttons)
        for _ in range(needed_buttons - len(buttons)):
            buttons.append(ButtonEmpty())

        return buttons

    def _create_pages(self):
        pages = dict()
        for number_page in range(1, self.page_amount + 1):
            prefix = f'-{number_page}' if number_page != 1 else ''
            name_new_page = f'{self.page_name}{prefix}'
            pages.update({name_new_page: {
                'page_name': name_new_page,
                'message_text': self.message_text,
            }})
        return pages

    def _add_buttons_in_pages(self):

        for self.page_number, page in zip(range(self.page_amount), self.pages.values()):
            start_sampling = self.page_number * self.height
            end_sampling = self.page_number * self.height + self.height
            page['buttons'] = self.buttons[start_sampling: end_sampling]

            page['buttons'].append((
                self._get_left_navigation_button(),
                self._get_center_navigation_button(),
                self._get_right_navigation_button(),
            ))

    def _get_center_navigation_button(self):
        return ButtonEmpty(name=f'{self.page_number + 1}/{self.page_amount}')

    def _get_left_navigation_button(self):
        prefix = f'-{self.page_number}' if self.page_number != 1 else ''
        if self.page_number != 0:
            return ButtonNav(name='◀️', callback=f'{self.page_name}{prefix}')
        else:
            return ButtonEmpty(name='⛔️')

    def _get_right_navigation_button(self):
        prefix = f'-{self.page_number + 2}'
        if self.page_number + 1 < self.page_amount:
            return ButtonNav(name='▶️', callback=f'{self.page_name}{prefix}')
        else:
            return ButtonEmpty(name='⛔️')
