from aiogram.filters import Command
from aiogram.fsm.state import State, StatesGroup
from aiogram import Router

from control import controller
from navigations.message_creator_to_send import MessageCreator
from parce.pyrogram_client import get_channel_data

router = Router()


class EnterChannelName(StatesGroup):
    choosing_name = State()


# todo отключить срабатывание на команды.
@router.message(EnterChannelName.choosing_name)
async def input_new_channel_name(message, bot, state):
    message_data = MessageCreator(message)
    channel = await get_channel_data(message)
    controller.db.set_new_channel(channel, message)
    await bot.send_message(message_data)
    await state.clear()


@router.message(Command("start"))
async def input_start_command(message, bot):
    message_data = MessageCreator(message)
    controller.db.add_new_user(message)
    await bot.send_message(message_data)
