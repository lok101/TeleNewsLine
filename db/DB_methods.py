from aiogram import types
from pyrogram import Client

from db.models import Channel, User
from db.base import session
from db.data_classes import ChannelData
from logger import logging

app = Client("my_account")


class DBController:

    @staticmethod
    def get_or_add_user_by_user_id(message: types.Message):

        user_name = message.from_user.username
        user_id = message.from_user.id

        entry = session.get(User, user_id)

        if entry is None:
            entry = User(id=user_id, name=user_name)
            session.add(entry)
            logging.info(f'Пользователь {user_name} добавлен в БД.')
        return entry

    @staticmethod
    def get_channel_by_channel_id(channel: ChannelData):
        channel_id = channel.id
        chanel_name = channel.name
        entry = session.get(Channel, channel_id)

        if entry is None:
            entry = Channel(id=channel_id, name=chanel_name)
            session.add(entry)
        return entry

    @staticmethod
    def add_new_user(message: types.Message) -> None:
        DBController.get_or_add_user_by_user_id(message)
        session.commit()

    @staticmethod
    def set_new_channel(channel: ChannelData, message: types.Message) -> None:

        user = DBController.get_or_add_user_by_user_id(message)
        channel = DBController.get_channel_by_channel_id(channel)

        channel.users.append(user)
        session.add(channel)

        session.commit()
