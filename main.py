import sys, logging, asyncio

from aiogram.types import BotCommand

from loader import bot, dp
from database.db_users import setup_users
import handlers

commands = [
    BotCommand(command="start", description="Botni ishga tushirish"),
    BotCommand(command="help", description="Yordam")
]


async def main():
    await setup_users()
    await bot.set_my_commands(commands)
    await dp.start_polling(bot)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())