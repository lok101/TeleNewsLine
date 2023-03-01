from aiogram import Router

from navigations.data_classes import FactoryDefaultButton, FactoryEmptyButton, FactoryBackButton, \
    FactoryNewChannelButton, FactoryProductButton, FactoryNavButton
from navigations.menu_navigation import ControlNavigation
from handlers.message import EnterChannelName

router = Router()
page_navigation = ControlNavigation()


@router.callback_query(FactoryDefaultButton.filter())
async def handler_press_default_button(callback, callback_data, bot):
    await page_navigation.forth(callback, callback_data, bot)


@router.callback_query(FactoryProductButton.filter())
async def handler_press_default_button(callback, callback_data, bot):
    await page_navigation.forth(callback, callback_data, bot)


@router.callback_query(FactoryEmptyButton.filter())
async def handler_press_empty_button(callback):
    await callback.answer()


@router.callback_query(FactoryNavButton.filter())
async def handler_press_nav_button(callback, callback_data, bot):
    await page_navigation.nav(callback, callback_data, bot)


@router.callback_query(FactoryNewChannelButton.filter())
async def handler_press_new_channel_button(callback, callback_data, bot, state):
    await page_navigation.forth(callback, callback_data, bot)
    await state.set_state(EnterChannelName.choosing_name)


@router.callback_query(FactoryBackButton.filter())
async def handler_press_back_button(callback, callback_data, bot, state):
    await page_navigation.back(callback, callback_data, bot)
    await state.clear()
