from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def word_kb(word: str):
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='⭐ Добавить в избранное', callback_data='fav:add:'+word)]
    ])
