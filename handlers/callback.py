from aiogram import types, Router

from navigations.data_classes import FactoryDefaultButton, FactoryEmptyButton, FactoryBackButton
from navigations.menu import Create
from handlers.message import EnterChannelName

router = Router()
create = Create()


@router.callback_query(FactoryDefaultButton.filter())
async def handles_press_default_button(callback, callback_data, bot, state):
    await create.send_menu_on_button_click(callback, callback_data, bot)
    if callback_data.page_name == 'new_channel':
        await state.set_state(EnterChannelName.choosing_name)


@router.callback_query(FactoryEmptyButton.filter())
async def handles_press_empty_button(callback):
    await callback.answer()


@router.callback_query(FactoryBackButton.filter())
async def handles_press_back_button(callback, callback_data, bot):
    create.is_back_button_click = True
    await create.send_menu_on_button_click(callback, callback_data, bot)
