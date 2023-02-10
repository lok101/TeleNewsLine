from aiogram import types

from db.models import Channel, User, session


class ChannelsDBController:
    @staticmethod
    def set_new_channel(message: types.message) -> None:
        # todo сделать проверку ссылки или имени и преобразование к нужному виду.

        user_id = message.from_user.id
        user_name = message.from_user.username
        channel_name = message.text

        # todo сделать проверку работоспособности указанного канала.

        # todo проверить нет ли такого канала в БД. Если есть, то добавить в существующую запись.

        channel = Channel(name=channel_name)
        user = User(id=user_id, name=user_name)
        channel.users.append(user)
        session.add(channel)

        session.commit()
