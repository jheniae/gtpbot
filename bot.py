import logging
import asyncio
from aiogram import Bot, Dispatcher, types
# from aiogram.contrib.middlewares.logging import LoggingMiddleware
# from aiogram.types import ParseMode

from config import TELEGRAM_BOT, ALLOWED_USERS
from db import on_startup as bd_on_startup
from middleware import CheckUserMiddleware
from handler import user_router


logger = logging.getLogger(__name__)


async def main():
    bot = Bot(TELEGRAM_BOT, parse_mode="HTML")
    dp = Dispatcher()
    dp.include_router(user_router)
    # dp.middleware.setup(LoggingMiddleware())
    dp.message.outer_middleware(CheckUserMiddleware)
    dp.callback_query.outer_middleware(CheckUserMiddleware)
    await bd_on_startup()
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logger.error("Bot stopped")
