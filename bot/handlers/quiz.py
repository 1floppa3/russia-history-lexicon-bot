from aiogram import Router
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command
from ..loader import lexicon
from ..keyboards.quiz_kb import quiz_kb, QuizCD, quiz_more_kb

router = Router()

@router.message(Command("quiz"))
async def cmd_quiz(message: Message, state: FSMContext):
    correct, options = lexicon.generate_quiz()
    correct_idx = options.index(correct["definition"])
    await state.update_data(correct_idx=correct_idx, options=options)
    text = (
        f"🎯 <b>Викторина!</b>\n"
        f"Угадайте значение слова: <b>{correct['word']}</b>"
    )
    await message.answer(text, reply_markup=quiz_kb(options))

@router.callback_query(QuizCD.filter())
async def cb_quiz(callback: CallbackQuery, callback_data: QuizCD, state: FSMContext):
    data = await state.get_data()
    correct_idx = data["correct_idx"]
    options = data["options"]
    selected = callback_data.idx

    if selected == correct_idx:
        reply = "✅ Правильно! Молодец! 🎉"
    else:
        right = options[correct_idx]
        reply = f"❌ Неправильно. Правильный ответ: {right}"

    await state.clear()
    await callback.answer(reply, show_alert=True)
    await callback.message.edit_text("👉 Нажми «🔄 Ещё», чтобы запустить ещё одну викторину.", reply_markup=quiz_more_kb())

@router.callback_query(lambda c: c.data == 'quiz:next')
async def cb_quiz_more(callback: CallbackQuery, state: FSMContext):
    correct, options = lexicon.generate_quiz()
    correct_idx = options.index(correct["definition"])
    await state.update_data(correct_idx=correct_idx, options=options)

    await callback.message.edit_text(
        f"🎯 <b>Викторина!</b>\nУгадайте значение слова: <b>{correct['word']}</b>",
        reply_markup=quiz_kb(options)
    )
    await callback.answer()