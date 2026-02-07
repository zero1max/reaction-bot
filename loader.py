import os
from aiogram import Dispatcher , Router, Bot
from aiogram.enums import ParseMode
from aiogram.client.default import DefaultBotProperties
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("BOT_TOKEN")
ADMIN_IDS = [5471452269]

dp = Dispatcher()
router_admin = Router()
router_user = Router()
router_channel = Router()
bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML)) # type: ignore
dp.include_router(router=router_admin)
dp.include_router(router=router_user)
dp.include_router(router=router_channel)