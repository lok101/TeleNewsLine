from aiogram.filters import Command
from aiogram.fsm.state import State, StatesGroup
from aiogram import Router

from navigations.menu import Create
from navigations.control import controller

router = Router()
create = Create()


class EnterChannelName(StatesGroup):
    choosing_name = State()


@router.message(EnterChannelName.choosing_name)
async def input_new_channel_name(message, bot, state):
    controller.channels.set_new_channel(message)
    await create.start_menu(message, bot)
    await state.clear()


@router.message(Command("start"))
async def input_start_command(message, bot):
    await create.start_menu(message, bot)
