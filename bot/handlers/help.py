from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command

router = Router()

@router.message(Command("help"))
async def cmd_help(message: Message):
    text = (
        "🆘 <b>Справка по командам</b>:\n\n"
        "<b>🔍 /word «слово»</b> — найти значение слова\n"
        "<b>🎲 /random</b> — случайное слово из базы\n"
        "<b>📚 /books</b> — какие книги в базе\n"
        "<b>❓ /quiz</b> — викторина: угадай значение слова\n"
        "<b>🏷️ /favorites</b> — посмотреть слова из «Избранного»\n"
        "<b>⚙️ /word_of_day 1/0</b> — включить/выключить Слово дня\n\n"
        "Просто выбери команду и следуй подсказкам. Удачи в изучении! 🍀"
    )
    await message.answer(text)
