import logging
import asyncio
from bot.loader import bot, dp
from bot.handlers import register_handlers
from bot.middlewares.user import UserMiddleware
from bot.services.daily_scheduler import schedule_daily_word

async def main():
    dp.message.middleware.register(UserMiddleware())
    dp.callback_query.middleware.register(UserMiddleware())
    register_handlers(dp)
    schedule_daily_word()
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, format="%(asctime)s | %(name)s | %(levelname)s | %(message)s")
    asyncio.run(main())