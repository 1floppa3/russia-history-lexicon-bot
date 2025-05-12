from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from ..loader import lexicon

router = Router()

@router.message(Command("books"))
async def cmd_books(message: Message):
    sources = lexicon.list_books()
    text = (
        "📚 <b>Доступные источники:</b>\n" +
        "\n".join(f"• {s}" for s in sources) + "\n\n"
        "🔍 Чтобы искать в конкретном источнике, просто вводи /word «слово» — "
        "я сам проверю оба текста!"
    )
    await message.answer(text)
