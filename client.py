import os


from telethon import events
from telethon import TelegramClient


client = TelegramClient('NewsLine', int(os.environ['API_ID']), os.environ['API_HASH'])


def client_activate():
    client.start()
    client.run_until_disconnected()


@client.on(events.NewMessage(chats='***'))
async def normal_handler(event):
    message = event.message.to_dict()['message']
    await client.send_message('***', message)
