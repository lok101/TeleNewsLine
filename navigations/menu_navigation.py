from navigations.menu import Create
from navigations.transition_stack import TransitionStack
from control import controller

create = Create()
stack = TransitionStack()


class ControlNavigation:

    @staticmethod
    async def start(message, bot):
        controller.stack.add_start_position_in_stack(message.from_user.id)
        await create.start_menu(message, bot)

    @staticmethod
    async def forth(callback, callback_data, bot):
        controller.stack.add_position_in_stack(callback.from_user.id, callback_data.page_name)
        await create.send_menu_on_button_click(callback, callback_data, bot)

    @staticmethod
    async def back(callback, callback_data, bot):
        controller.stack.delete_position_in_stack(callback.from_user.id)
        await create.send_menu_on_button_click(callback, callback_data, bot)

    @staticmethod
    async def nav(callback, callback_data, bot):
        controller.stack.replace_last_position(callback.from_user.id, callback_data.page_name)
        await create.send_menu_on_button_click(callback, callback_data, bot)

    @staticmethod
    async def new_channel(message, bot):
        controller.stack.delete_position_in_stack(message.from_user.id)
        await create.start_menu(message, bot)
