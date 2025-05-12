from aiogram import BaseMiddleware
from aiogram.types import Message, CallbackQuery, Update
from ..loader import user_data

class UserMiddleware(BaseMiddleware):
    async def __call__(self, handler, event: Update, data: dict):
        user_id = None
        if isinstance(event, Message) and event.from_user:
            user_id = event.from_user.id
        elif isinstance(event, CallbackQuery) and event.from_user:
            user_id = event.from_user.id

        if user_id:
            user_data.ensure_user(user_id)
        return await handler(event, data)