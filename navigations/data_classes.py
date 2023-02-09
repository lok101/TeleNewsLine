from aiogram.filters.callback_data import CallbackData
from dataclasses import dataclass


class FactoryDefaultButton(CallbackData, prefix="default"):
    page_name: str
    button_is_back: bool


class FactoryEmptyButton(CallbackData, prefix='empty'):
    page_name: str
    button_is_back: bool


class FactoryBackButton(CallbackData, prefix='back'):
    page_name: str
    button_is_back: bool


@dataclass
class DefaultMenuButton:
    name: str
    callback: str


@dataclass
class EmptyMenuButton:
    name: str = '⬜️  ⬜️  ⬜️  ⬜️'
    callback: str = 'empty_button'
