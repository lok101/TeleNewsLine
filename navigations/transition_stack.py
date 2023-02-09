from collections import deque
from typing import Optional


class TransitionStack:
    """ Словарь "data" хранит стеки всех пользователей, в качестве ключей используя user_id.
        В этом классе описаны методы работы со стеком переходов каждого пользователя.
        Обеспечивает работу кнопки "Назад".
     """
    data = {}

    def set_new_last_position(self, user_id: str, position: str) -> None:
        """ Добавляет позицию в стек. """
        self.data.setdefault(user_id, deque())
        self.data[user_id].append(position)

    def get_last_position(self, user_id: str) -> Optional[str]:
        """ Возвращает (не удаляя) значение последней позиции стека. """
        stack_for_current_user = self.data.get(user_id, None)
        if isinstance(stack_for_current_user, deque) and len(stack_for_current_user) > 0:
            return stack_for_current_user[-1]
        return None

    def delete_last_position(self, user_id: str) -> None:
        """ Удаляет последнюю позицию в стеке. """
        stack_for_current_user = self.data.get(user_id, None)
        if isinstance(stack_for_current_user, deque):
            stack_for_current_user.pop()
