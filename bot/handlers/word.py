from aiogram import Router
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import Message
from aiogram.filters import Command

from ..keyboards.word_kb import word_kb
from ..loader import lexicon

router = Router()

class WordStates(StatesGroup):
    waiting_for_word = State()

async def process_word(message: Message, word: str, state: FSMContext):
    results = lexicon.find(word)
    if results:
        entry = results[0]
        text = (
            f"🔍 <b>«{entry['word']}»</b> ({entry['source']})\n\n"
            f"📖 <i>{entry['definition']}</i>\n"
        )
        await message.answer(text, reply_markup=word_kb(word))
        return

    nearest_list = lexicon.nearest(word, 5)
    if nearest_list:
        suggestions = ", ".join(f"<b>{w['word']}</b>" for w in nearest_list)
        text = (
            f"❗️ Не нашёл «<b>{word}</b>».\n"
            f"🔎 Возможно, ты имел в виду: {suggestions}"
        )
    else:
        text = f"❗️ К сожалению, слово «<b>{word}</b>» не найдено\n"

    await state.clear()
    await message.answer(text)

@router.message(Command("word"))
async def cmd_word(message: Message, state: FSMContext):
    text = message.text or ""
    parts = text.split(maxsplit=1)
    if len(parts) < 2 or not parts[1].strip():
        await message.answer("❓ Пожалуйста, введите слово, которое хотите найти:")
        await state.set_state(WordStates.waiting_for_word)
    else:
        word = parts[1].strip()
        await process_word(message, word, state)

@router.message(WordStates.waiting_for_word)
async def cmd_word_waited(message: Message, state: FSMContext):
    word = message.text.strip()
    await process_word(message, word, state)