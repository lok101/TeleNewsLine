from aiogram.filters.callback_data import CallbackData
from dataclasses import dataclass


class FactoryDefaultButton(CallbackData, prefix="default"):
    page_name: str


class FactoryProductButton(CallbackData, prefix="product"):
    page_name: str


class FactoryEmptyButton(CallbackData, prefix='empty'):
    page_name: str


class FactoryNewChannelButton(CallbackData, prefix='new_channel'):
    page_name: str


class FactoryBackButton(CallbackData, prefix='back'):
    page_name: str


@dataclass
class BaseButton:
    name: str
    callback: str


@dataclass
class ButtonDefault(BaseButton):
    name: str
    callback: str


@dataclass
class ButtonProduct(BaseButton):
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


@dataclass
class ProductMenu:
    pass
