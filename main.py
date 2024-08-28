import asyncio
import logging

from aiogram import Bot, Dispatcher

import config
from app.handlers import router
from administration.adminhandlers import admin_router

bot = Bot(token=config.BOT_TOKEN)
dp = Dispatcher()


async def main():
    dp.include_router(router)
    dp.include_router(admin_router)
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)  # выключить на этапе продакшена
    asyncio.run(main())
