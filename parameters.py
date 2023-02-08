import os


from telethon import TelegramClient

client = TelegramClient('NewsLine', int(os.environ['API_ID']), os.environ['API_HASH'])

