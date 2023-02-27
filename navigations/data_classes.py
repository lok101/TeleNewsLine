from aiogram.filters.callback_data import CallbackData
from dataclasses import dataclass


class FactoryDefaultButton(CallbackData, prefix="default"):
    page_name: str


class FactoryEmptyButton(CallbackData, prefix='empty'):
    page_name: str


class FactoryNewChannelButton(CallbackData, prefix='new_channel'):
    page_name: str


class FactoryBackButton(CallbackData, prefix='back'):
    page_name: str


@dataclass
class BaseButton:
    pass


@dataclass
class ButtonDefault(BaseButton):
    name: str
    callback: str


@dataclass
class ButtonNewChannel(BaseButton):
    name: str = 'Добавить канал.'
    callback: str = 'new_channel'


@dataclass
class ButtonEmpty(BaseButton):
    name: str = '➖                                                                                                  ➖'
    callback: str = 'empty_button'


class MenuPage:
    def __init__(self, page_name: str, message_text: str, buttons: list[BaseButton]):
        self.page_name = page_name
        self.message_text = message_text
        self.buttons = buttons

    def get_page(self) -> dict:
        return {self.page_name: self.__dict__}
