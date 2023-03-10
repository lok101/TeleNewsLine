import asyncio
import os

from aiogram import Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage

from handlers import message, callback
from my_bot import MyBot


async def bot_activate():
    bot = MyBot(token=os.environ['BOT_TOKEN'])
    dp = Dispatcher(storage=MemoryStorage())

    dp.include_router(callback.router)
    dp.include_router(message.router)

    await dp.start_polling(bot, skip_updates=True)


if __name__ == "__main__":
    asyncio.run(bot_activate())
