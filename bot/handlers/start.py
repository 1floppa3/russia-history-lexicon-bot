from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command

router = Router()

@router.message(Command("start"))
async def cmd_start(message: Message):
    text = (
        "👋 <b>Привет!</b> Ты в боте <b>«Лексикон XVIII века»</b>.\n\n"
        "👥 <i>Проект выполнен в рамках курса «История России» ВШЭ.</i>\n"
        "🎓 Выполняли: <b>Кочетков Денис</b> и <b>Ерощук Владислав</b>\n\n"
        "❓ Что я умею:\n"
        "   • <b>/word «слово»</b> — найти значение слова\n"
        "   • <b>/random</b> — показать случайное слово\n"
        "   • <b>/books</b> — список доступных источников\n"
        "   • <b>/quiz</b> — проверка знаний в мини-викторине\n"
        "   • <b>/favorites</b> — посмотреть слова из «Избранного»\n"
        "   • <b>/word_of_day 1/0</b> — включить/выключить Слово дня\n"
        "   • <b>/help</b> — справка по командам\n\n"
        "⏰ Каждый день я буду присылать тебе <b>Слово дня</b> автоматически.\n"
        "Готов? Введи <b>/word «слово»</b> и попробуй найти своё первое слово! 😉"
    )
    await message.answer(text)
