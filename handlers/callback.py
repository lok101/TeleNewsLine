from aiogram import types, Router, Bot
from aiogram.fsm.context import FSMContext

from navigations.data_classes import FactoryDefaultButton, FactoryEmptyButton, FactoryBackButton
from navigations.menu import Create
from handlers.message import EnterChannelName

router = Router()


@router.callback_query(FactoryDefaultButton.filter())
async def handles_press_default_button(
        callback: types.callback_query, callback_data: FactoryDefaultButton, bot: Bot, state: FSMContext):
    await Create.send_menu_from_callback(callback, callback_data, bot)
    if callback_data.page_name == 'new_channel':
        await state.set_state(EnterChannelName.choosing_name)


@router.callback_query(FactoryEmptyButton.filter())
async def handles_press_empty_button(callback):
    await callback.answer()


@router.callback_query(FactoryBackButton.filter())
async def handles_press_back_button(callback):
    await callback.answer()
