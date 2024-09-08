import asyncio
import logging

from aiogram import Bot, Dispatcher

import config
from app.handlers import router
from administration.adminhandlers import admin_router
from database.models import async_main

bot = Bot(token=config.BOT_TOKEN)
dp = Dispatcher()


async def main():
    await async_main()
    dp.include_router(router)
    dp.include_router(admin_router)
    # dp.pre_checkout_query.register(pre_checkout_query)

    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)  # выключить на этапе продакшена
    asyncio.run(main())
