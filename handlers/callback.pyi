from aiogram import types, Router
from aiogram.fsm.context import FSMContext

from my_bot import MyBot
from navigations.data_classes import FactoryDefaultButton, FactoryEmptyButton, FactoryBackButton, \
    FactoryNewChannelButton, FactoryNavButton

router = Router()


@router.callback_query(FactoryDefaultButton.filter())
async def handler_press_default_or_page_button(
        callback: types.callback_query,
        callback_data: FactoryDefaultButton,
        bot: MyBot,
) -> None: ...


@router.callback_query(FactoryEmptyButton.filter())
async def handler_press_empty_button(
        callback: types.callback_query,
) -> None: ...

@router.callback_query(FactoryNavButton.filter())
async def handler_press_nav_button(
        callback: types.callback_query,
        callback_data: FactoryNavButton,
        bot: MyBot,
) -> None: ...


@router.callback_query(FactoryNewChannelButton.filter())
async def handler_press_new_channel_button(
        callback: types.callback_query,
        callback_data: FactoryNewChannelButton,
        bot: MyBot,
        state: FSMContext,
) -> None: ...


@router.callback_query(FactoryBackButton.filter())
async def handler_press_back_button(
        callback: types.callback_query,
        callback_data: FactoryBackButton,
        bot: MyBot,
        state: FSMContext,
) -> None: ...
