from aiogram.filters import Command
from aiogram.fsm.state import State, StatesGroup
from aiogram import Router

from control import controller
from navigations.message_creator_to_send import MessageCreator
from navigations.transition_stack import NAV_HISTORY
from parce.pyrogram_client import get_channel_data

router = Router()


class EnterChannelName(StatesGroup):
    choosing_name = State()


# todo отключить срабатывание на команды.
@router.message(EnterChannelName.choosing_name)
async def input_new_channel_name(message, bot, state):
    message_data = MessageCreator(message)

    NAV_HISTORY.add_position_in_stack(message_data)

    message_data.set_session_and_message_data()

    channel = await get_channel_data(message)
    controller.db.set_new_channel(channel, message)
    await bot.send_message(message_data)
    await state.clear()


@router.message(Command("start"))
async def input_start_command(message, bot):
    message_data = MessageCreator(message)

    NAV_HISTORY.add_position_in_stack(message_data)

    message_data.set_session_and_message_data()

    controller.db.add_new_user(message)
    await bot.send_message(message_data)
