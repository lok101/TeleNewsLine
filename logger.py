from aiologger.levels import LogLevel
from aiologger.loggers.json import JsonLogger

import logging

async_logging = JsonLogger.with_default_handlers(
    level=LogLevel.DEBUG,
)

logging.basicConfig(level=logging.DEBUG)
