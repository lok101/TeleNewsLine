import os
import re

from pyrogram import Client

from db.data_classes import ChannelData


async def get_channel_data(message):
    async with Client(
            "check_channel",
            bot_token="6140637338:AAH9wzvolM1YsyPtrbiNc9O7wZ4GhLBFUUM",
            api_id=int(os.environ['API_ID']),
            api_hash=os.environ['API_HASH']) \
            as app:
        mention = re.search(r'@(\w+)', message.text).group(1)
        if mention:
            peer_user = await app.resolve_peer(mention)
            channel_id = peer_user.channel_id
            return ChannelData(id=channel_id, name=mention)
