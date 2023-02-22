from aiogram import types
from pyrogram import Client

from db.models import Channel, User
from db.base import session
from db.data_classes import ChannelData, DBResponse
from logger import logging

app = Client("my_account")


class DBController:

    @staticmethod
    def get_or_add_user_by_user_id(message: types.Message) -> DBResponse: ...

    @staticmethod
    def get_channel_by_channel_id(channel: ChannelData): ...

    @staticmethod
    def add_new_user(message: types.Message) -> None: ...

    @staticmethod
    def set_new_channel(channel: ChannelData, message: types.Message) -> None: ...
