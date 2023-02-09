from aiogram import types


class UserChannels:
    """ Словарь "data" хранит подписки на каналы для всех пользователей, в качестве ключей используя user_id.
        В этом классе описаны методы работы со списком каналов каждого пользователя.
      """
    data = {}

    def set_new_channel(self, message: types.Message) -> None:
        """ Добавляет канал в список пользователя. """
        user_id = message.from_user.id
        channel_name = message.text
        self.data.setdefault(user_id, set())
        self.data[user_id].add(channel_name)

    def delete_channel(self, user_id: str, channel_name: str) -> None:
        user_channels = self.data.get(user_id, None)
        if user_channels is not None:
            user_channels.remove(channel_name)
