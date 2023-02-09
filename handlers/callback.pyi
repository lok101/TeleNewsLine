from aiogram import types, Router, Bot
from aiogram.fsm.context import FSMContext

from navigations.data_classes import FactoryDefaultButton, FactoryEmptyButton, FactoryBackButton, \
    FactoryNewChannelButton

router = Router()


@router.callback_query(FactoryDefaultButton.filter())
async def handler_press_default_button(
        callback: types.callback_query,
        callback_data: FactoryDefaultButton,
        bot: Bot,
) -> None: ...


@router.callback_query(FactoryEmptyButton.filter())
async def handler_press_empty_button(
        callback: types.callback_query,
) -> None: ...


@router.callback_query(FactoryNewChannelButton.filter())
async def handler_press_new_channel_button(
        callback: types.callback_query,
        callback_data: FactoryDefaultButton,
        bot: Bot,
        state: FSMContext,
) -> None: ...


@router.callback_query(FactoryBackButton.filter())
async def handler_press_back_button(
        callback: types.callback_query,
        callback_data: FactoryBackButton,
        bot: Bot,
) -> None: ...
