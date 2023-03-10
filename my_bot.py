from typing import Union

from aiogram import Bot, types


class MyBot(Bot):
    async def send_message(self, message_data, *args, **kwargs) -> types.Message:
        return await super().send_message(
            chat_id=message_data.chat_id,
            text=message_data.text,
            reply_markup=message_data.reply_markup,
            parse_mode="Markdown",
            *args, **kwargs
        )

    async def edit_message_text(self, message_data, *args, **kwargs) -> Union[types.Message, bool]:
        return await super().edit_message_text(
            chat_id=message_data.chat_id,
            message_id=message_data.message_id,
            text=message_data.text,
            reply_markup=message_data.reply_markup,
            parse_mode="Markdown",
            *args, **kwargs
        )