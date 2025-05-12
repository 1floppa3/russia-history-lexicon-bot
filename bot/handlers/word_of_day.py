from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command

from ..loader import user_data

router = Router()

@router.message(Command("word_of_day"))
async def cmd_word_of_day(message: Message):
    uid = message.from_user.id
    parts = (message.text or "").split(maxsplit=1)
    if len(parts) < 2:
        status = "✅ включена" if user_data.is_daily_enabled(uid) else "❌ выключена"
        await message.answer(
            f"⏰ Рассылка «Слово дня» сейчас: {status}.\n"
            "Чтобы включить — отправьте <b>/word_of_day 1</b>\n"
            "Чтобы выключить — отправьте <b>/word_of_day 0</b>."
        )
        return

    arg = parts[1].strip().lower()
    if arg in ("on", "1"):
        user_data.enable_daily(uid)
        await message.answer("✅ Вы подписались на «Слово дня». Приходить будет каждый день в 09:00.")
    elif arg in ("off", "0"):
        user_data.disable_daily(uid)
        await message.answer("❌ Вы отписались от «Слова дня».")
    else:
        await message.answer("❓ Используйте <b>/word_of_day on</b> или <b>/word_of_day off</b>.")
