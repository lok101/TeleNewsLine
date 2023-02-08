from collections import deque


class TransitionStack:
    """ В этом классе описаны методы работы со стеком переходов каждого пользователя.
        Обеспечивает работу кнопки "Назад".
        Словарь "data" хранит стеки всех пользователей, в качестве ключей используя chat_id.
     """
    data = {}

    def set_new_last_position(self, chat_id: str, position: str) -> None:
        """ Добавляет позицию в стек. """
        self.data.setdefault(chat_id, deque())
        self.data[chat_id].append(position)

    def get_last_position(self, chat_id: str) -> (str, None):
        """ Возвращает (не удаляя) значение последней позиции стека. """
        stack_for_current_user = self.data.get(chat_id, None)
        if isinstance(stack_for_current_user, deque) and len(stack_for_current_user) > 0:
            return stack_for_current_user[-1]
        return None

    def delete_last_position(self, chat_id: str) -> None:
        """ Удаляет последнюю позицию в стеке. """
        stack_for_current_user = self.data.get(chat_id, None)
        if isinstance(stack_for_current_user, deque):
            stack_for_current_user.pop()
