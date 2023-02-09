from aiogram.filters import Command
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from aiogram import types, Router, Bot

from navigations.menu import Create
from navigations.control import controller

router = Router()


class EnterChannelName(StatesGroup):
    choosing_name = State()


@router.message(EnterChannelName.choosing_name)
async def input_new_channel_name(message: types.Message, bot: Bot, state: FSMContext):
    controller.channels.set_new_channel(message)
    await Create.start_menu(message, bot)
    await state.clear()


@router.message(Command("start"))
async def input_start_command(message: types.Message, bot: Bot):
    await Create.start_menu(message, bot)
