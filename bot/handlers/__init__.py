from aiogram import Dispatcher
from .start import router as start_router
from .help import router as help_router
from .word import router as word_router
from .random import router as random_router
from .books import router as books_router
from .quiz import router as quiz_router
from .favorites import router as favorites_router
from .word_of_day import router as wod_router

__all__ = [
    start_router,
    help_router,
    word_router,
    random_router,
    books_router,
    quiz_router,
    favorites_router,
    wod_router
]

def register_handlers(dp: Dispatcher):
    for router in __all__:
        dp.include_router(router)