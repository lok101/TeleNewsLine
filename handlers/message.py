from aiogram.filters import Command
from aiogram.fsm.state import State, StatesGroup
from aiogram import Router

from control import controller
from navigations.menu_navigation import ControlNavigation
from parce.pyrogram_client import get_channel_data

router = Router()
page_navigation = ControlNavigation()


class EnterChannelName(StatesGroup):
    choosing_name = State()


# todo отключить срабатывание на команды.
@router.message(EnterChannelName.choosing_name)
async def input_new_channel_name(message, bot, state):
    channel = await get_channel_data(message)
    controller.db.set_new_channel(channel, message)
    await page_navigation.new_channel(message, bot)
    await state.clear()


@router.message(Command("start"))
async def input_start_command(message, bot):
    controller.db.add_new_user(message)
    await page_navigation.start(message, bot)
