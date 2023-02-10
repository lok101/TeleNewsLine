import os

from telethon import events
from telethon import TelegramClient
import logging

logging.basicConfig()
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

try:
    api_id = int(os.environ['API_ID'])
    api_hash = os.environ['API_HASH']
    bot_token = os.environ['BOT_TOKEN']
    logger.debug('Переменные среды загружены.')
except(KeyError, ValueError):
    logger.critical('Укажите корректные переменные среды.')


def client_activate():
    with TelegramClient('NewsLine', int(os.environ['API_ID']), os.environ['API_HASH']) as client:
        @client.on(events.NewMessage(chats='https://t.me/lentest111'))
        async def normal_handler(event):
            message = event.message.to_dict()['message']
            await client.send_message('https://t.me/lok101', message)

        client.loop.run_until_complete(client.send_message('https://t.me/lok101', 'Hello!'))
        client.start()
        client.run_until_disconnected()


def bot_activate():
    with TelegramClient('bot', api_id, api_hash).start(bot_token=bot_token) as bot:

        @bot.on(events.NewMessage)
        async def echo(event):
            """Echo the user message."""
            await event.respond(event.text)

        bot.start()
        bot.run_until_disconnected()


if __name__ == '__main__':
    try:
        bot_activate()
    except Exception as ex:
        logger.exception('Неизвестное исключение.')
