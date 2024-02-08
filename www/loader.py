from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from environs import Env

env = Env()
env.read_env()
BOT_TOKEN = env.str("BOT_TOKEN")
ADMINS = env.list("ADMINS")

bot = Bot(token=BOT_TOKEN, parse_mode=types.ParseMode.HTML)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)
