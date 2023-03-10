from collections import deque

from navigations.data_classes import SessionData
from menu_structure.user_pages import menu_pages
from exceptions import EmptyTransitionStack


class TransitionStack:
    """ Словарь "data" хранит стеки всех пользователей, в качестве ключей используя user_id.
        В этом классе описаны методы работы со стеком переходов каждого пользователя.
        Обеспечивает работу кнопки "Назад".
     """
    data = {}

    # todo поправить работу стека при рестарте бота.

    def is_actual_menu_page(self, stack_key: int):
        return bool(self.data.get(stack_key, False))

    def add_position_in_stack(self, message_data: SessionData) -> None:
        """ Добавляет позицию в стек. """
        self._create_stack(message_data)
        self.data[message_data.stack_key].append(message_data.current_page_name)

    def add_start_position_in_stack(self, message_data: SessionData) -> None:
        """ Добавляет позицию стартового меню в стек. """
        self._create_stack(message_data)
        self.data[message_data.stack_key].append(menu_pages[0].page_name)

    def delete_position_in_stack(self, message_data: SessionData) -> None:
        """ Удаляет последнюю позицию в стеке. """
        self._clear_stack(message_data)
        stack_for_current_user = self.data.get(message_data.stack_key, None)
        try:
            stack_for_current_user.pop()
        except IndexError:
            raise EmptyTransitionStack(
                'Стек переходов пуст. '
                'Пользователь работает с сообщением из предыдущей сессии.'
            )

    def replace_last_position(self, message_data: SessionData) -> None:
        """ Заменяет последнюю позицию в стеке на переданную. """
        try:
            self.delete_position_in_stack(message_data)
        except EmptyTransitionStack:
            pass
        self.add_position_in_stack(message_data)

    def get_previous_position_in_stack(self, message_data: SessionData) -> str:
        """ Возвращает предпоследнюю позицию стека. """
        self._create_stack(message_data)
        stack_for_current_user = self.data.get(message_data.stack_key, None)
        previous_position = menu_pages[0].page_name
        try:
            previous_position = stack_for_current_user[-2]
        except IndexError:
            pass
        finally:
            return previous_position

    def _clear_stack(self, message_data: SessionData) -> None:
        """ Очищает стек. """
        self._create_stack(message_data)
        self.data[message_data.stack_key].clear()

    def _create_stack(self, message_data: SessionData) -> None:
        self.data.setdefault(message_data.stack_key, deque([menu_pages[0].page_name]))


NAV_HISTORY = TransitionStack()
