from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery
from ..loader import lexicon
from ..keyboards.random_kb import random_kb

router = Router()

def format_random_cmd():
    entry = lexicon.random_word()
    text = (
        f"🎲 <b>Случайное слово:</b> «{entry['word']}»\n\n"
        f"📖 <i>{entry['definition']}</i>\n\n"
        "👉 Нажми «🔄 Ещё слово», чтобы получить новое."
    )
    return entry, text

@router.message(Command("random"))
async def cmd_random(message: Message):
    entry, text = format_random_cmd()
    await message.answer(text, reply_markup=random_kb(entry['word']))


@router.callback_query(lambda c: c.data == 'random:next')
async def cb_random(callback: CallbackQuery):
    entry, text = format_random_cmd()
    await callback.message.edit_text(text, reply_markup=random_kb(entry['word']))
    await callback.answer()