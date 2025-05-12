from aiogram.filters.callback_data import CallbackData
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder


class QuizCD(CallbackData, prefix="quiz"):
    idx: int

def quiz_kb(options: list[str]) -> InlineKeyboardMarkup:
    kb = InlineKeyboardBuilder()
    for i, opt in enumerate(options):
        kb.add(
            InlineKeyboardButton(
                text=opt,
                callback_data=QuizCD(idx=i).pack()
            )
        )
    return InlineKeyboardMarkup(inline_keyboard=kb.adjust(1).export())

def quiz_more_kb() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🔄 Ещё", callback_data='quiz:next')]
    ])