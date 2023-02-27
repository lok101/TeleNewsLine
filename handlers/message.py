from aiogram.filters import Command
from aiogram.fsm.state import State, StatesGroup
from aiogram import Router

from navigations.menu import Create
from control import controller
from parce.pyrogram_client import my_handler

router = Router()
create = Create()


class EnterChannelName(StatesGroup):
    choosing_name = State()


@router.message(EnterChannelName.choosing_name)
async def input_new_channel_name(message, bot, state):
    channel = await my_handler(message)
    controller.db.set_new_channel(channel, message)
    controller.stack.delete_last_position(message.from_user.id)
    await create.start_menu(message, bot)
    await state.clear()


@router.message(Command("start"))
async def input_start_command(message, bot):
    controller.db.add_new_user(message)
    await create.start_menu(message, bot)
