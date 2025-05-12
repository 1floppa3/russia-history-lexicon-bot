from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.cron import CronTrigger
import logging

from bot.loader import bot, lexicon, user_data

logger = logging.getLogger(__name__)

def schedule_daily_word():
    scheduler = AsyncIOScheduler(timezone="Europe/Berlin")
    trigger = CronTrigger(hour=21, minute=11)  # каждый день в 09:00
    scheduler.add_job(_send_daily_to_all, trigger)
    scheduler.start()
    logger.info("Scheduler started for daily word at 09:00 Europe/Berlin")

async def _send_daily_to_all():
    users = user_data.list_daily_users()
    for user_id in users:
        try:
            entry = lexicon.random_word()
            text = (
                f"⏰ <b>Слово дня:</b> «{entry['word']}»\n\n"
                f"📖 <i>{entry['definition']}</i>"
            )
            await bot.send_message(chat_id=user_id, text=text)
        except Exception as e:
            logger.error(f"Failed to send daily word to {user_id}: {e}")
