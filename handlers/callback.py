from aiogram.fsm.state import State
from aiogram import types, Router, Bot

from navigations.data_classes import NavButtonCallback
from navigations.menu import Create

router = Router()


@router.callback_query(NavButtonCallback.filter(), State('*'))
async def handles_press_button(callback: types.callback_query, callback_data: NavButtonCallback, bot: Bot):
    await Create.send_menu_from_callback(callback, callback_data, bot)
