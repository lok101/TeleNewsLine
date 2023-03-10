from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram import types, Router

from my_bot import MyBot

router = Router()


class EnterChannelName(StatesGroup):
    choosing_name = State()


@router.message(EnterChannelName.choosing_name)
async def input_new_channel_name(message: types.message, bot: MyBot, state: FSMContext): ...


@router.message(Command("start"))
async def input_start_command(message: types.message, bot: MyBot): ...