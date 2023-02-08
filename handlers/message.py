from aiogram.filters import Command
from aiogram.fsm.state import State
from aiogram import types, Router, Bot

from service import Create

router = Router()


@router.message(Command("start"), State('*'))
async def input_start_command(message: types.Message, bot: Bot):
    await Create.start_menu(message, bot)
