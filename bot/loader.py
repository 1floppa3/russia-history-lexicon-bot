from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage

from bot.config import BOT_TOKEN, WORDS_DB_FILE, USER_DATA_DB_FILE
from bot.services.lexicon import LexiconService
from bot.services.user_data import UserDataService

bot = Bot(token=BOT_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher(storage=MemoryStorage())
lexicon = LexiconService(WORDS_DB_FILE)
user_data = UserDataService(USER_DATA_DB_FILE)
