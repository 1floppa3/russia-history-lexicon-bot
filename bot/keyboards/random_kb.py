from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def random_kb(word: str):
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='⭐ Добавить в избранное', callback_data='fav:add:'+word)],
        [InlineKeyboardButton(text='🔄 Ещё слово', callback_data='random:next')]
    ])