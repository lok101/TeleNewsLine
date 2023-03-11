from aiogram import Router

from logger import logger
from handlers.message import EnterChannelName
from navigations.data_classes import FactoryDefaultButton, FactoryEmptyButton, FactoryBackButton, \
    FactoryNewChannelButton, FactoryProductButton, FactoryNavButton
from navigations.message_creator_to_send import MessageCreator
from navigations.transition_stack import NAV_HISTORY


router = Router()


@router.callback_query(FactoryDefaultButton.filter())
@router.callback_query(FactoryProductButton.filter())
async def handler_press_default_or_page_button(callback, callback_data, bot):
    message_data = MessageCreator(callback, callback_data)

    NAV_HISTORY.add_position_in_stack(message_data)

    message_data.set_session_and_message_data()

    await bot.edit_message_text(message_data)
    logger.debug(NAV_HISTORY.data)


@router.callback_query(FactoryEmptyButton.filter())
async def handler_press_empty_button(callback):
    await callback.answer()


@router.callback_query(FactoryNavButton.filter())
async def handler_press_nav_button(callback, callback_data, bot):
    message_data = MessageCreator(callback, callback_data)

    NAV_HISTORY.replace_last_position(message_data)

    message_data.set_session_and_message_data()

    await bot.edit_message_text(message_data)


@router.callback_query(FactoryNewChannelButton.filter())
async def handler_press_new_channel_button(callback, callback_data, bot, state):
    message_data = MessageCreator(callback, callback_data)

    NAV_HISTORY.add_position_in_stack(message_data)

    message_data.set_session_and_message_data()

    await bot.edit_message_text(message_data)

    await state.set_state(EnterChannelName.choosing_name)


@router.callback_query(FactoryBackButton.filter())
async def handler_press_back_button(callback, callback_data, bot, state):
    message_data = MessageCreator(callback, callback_data)
    message_data.handel_back_button_press()

    message_data.set_session_and_message_data()

    await bot.edit_message_text(message_data)

    await state.clear()
