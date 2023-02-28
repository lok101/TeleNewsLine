from collections import deque

from navigations.user_pages import menu_pages


class TransitionStack:
    """ Словарь "data" хранит стеки всех пользователей, в качестве ключей используя user_id.
        В этом классе описаны методы работы со стеком переходов каждого пользователя.
        Обеспечивает работу кнопки "Назад".
     """
    data = {}

    # todo поправить работу стека при рестарте бота.

    def add_position_in_stack(self, user_id: str, position: str) -> None:
        """ Добавляет позицию в стек. """
        self.data.setdefault(user_id, deque())
        self.data[user_id].append(position)

    def add_start_position_in_stack(self, user_id: str) -> None:
        """ Добавляет позицию стартового меню в стек. """
        self.data.setdefault(user_id, deque())
        self.data[user_id].append(menu_pages[0].page_name)

    def delete_position_in_stack(self, user_id: str) -> None:
        """ Удаляет последнюю позицию в стеке. """
        stack_for_current_user = self.data.get(user_id, None)
        if isinstance(stack_for_current_user, deque):
            stack_for_current_user.pop()

    def get_previous_position_in_stack(self, user_id: str) -> str:
        stack_for_current_user = self.data.get(user_id, None)
        previous_position = menu_pages[0].page_name
        try:
            previous_position = stack_for_current_user[-2]
        except IndexError:
            pass
        finally:
            return previous_position

    def clear_stack(self, user_id: str) -> None:
        self.data.setdefault(user_id, deque())
        self.data[user_id].clear()
