from aiogram import Router
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command
from ..loader import user_data, lexicon

router = Router()

@router.message(Command("favorites"))
async def cmd_favorites(message: Message):
    user_id = message.from_user.id
    fav_list = user_data.list_favorites(user_id)

    if not fav_list:
        await message.answer(
            "⭐ <b>У вас пока нет избранных слов.</b>\n"
            "Чтобы добавить слово, найдите его через /word и нажмите кнопку «⭐ Добавить в избранное»."
        )
        return

    text = ["⭐ <b>Ваши избранные слова:</b>\n"]
    for w in fav_list:
        results = lexicon.find(w)
        if results:
            entry = results[0]
            text.append(f"• <b>{entry['word']}</b> — {entry['definition']}")
        else:
            text.append(f"• <b>{w}</b> — (не найдено в словаре)")
    await message.answer("\n".join(text))

@router.callback_query(lambda c: c.data and c.data.startswith("fav:add:"))
async def cb_add_favorite(callback: CallbackQuery):
    _, _, word = callback.data.partition("fav:add:")
    user_id = callback.from_user.id

    user_data.add_favorite(user_id, word)

    await callback.answer(f"✅ Слово «{word}» добавлено в избранное!", show_alert=True)