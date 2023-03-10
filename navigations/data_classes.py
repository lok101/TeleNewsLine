from aiogram.filters.callback_data import CallbackData
from aiogram import types

from dataclasses import dataclass


class BaseFactoryButton(CallbackData, prefix="base"):
    page_name: str


class FactoryDefaultButton(BaseFactoryButton, prefix="default"):
    page_name: str


class FactoryProductButton(BaseFactoryButton, prefix="product"):
    page_name: str


class FactoryEmptyButton(BaseFactoryButton, prefix='empty'):
    page_name: str


class FactoryNavButton(BaseFactoryButton, prefix='nav'):
    page_name: str


class FactoryNewChannelButton(BaseFactoryButton, prefix='new_channel'):
    page_name: str


class FactoryBackButton(BaseFactoryButton, prefix='back'):
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
    name: str = '➖                                                                                   ➖'
    callback: str = 'empty_button'


@dataclass
class ButtonNav(BaseButton):
    name: str = '⏺'
    callback: str = 'empty_button'


@dataclass
class SessionData:
    user_id: int = 0
    message_id: int = 0
    chat_id: int = 0
    stack_key: int = 0

    text: str = None
    reply_markup: types.reply_keyboard_markup = None

    current_page_name: str = None
    previous_page_name: str = None
