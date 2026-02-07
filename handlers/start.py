import random, aiosqlite
from aiogram import F
from aiogram.types import Message
from aiogram.types import ReactionTypeEmoji
from aiogram.filters import CommandStart
#
from loader import router_user, router_channel
from database.db_users import DB, add_user


START_TEXT = (
    "👋 Assalomu alaykum!\n\n"
    "Men kanalingizga tashlangan postlarga avtomatik reaksiya bildiraman 🤖🔥\n\n"
    "1️⃣ Avval meni *kanalingizga qo‘shing*\n"
    "2️⃣ Keyin *admin qilib qo‘ying*\n\n"
    "Admin qilgach, men avtomatik ishlay boshlayman ✅"
)



@router_user.message(CommandStart())
async def start_handler(msg: Message):
    await add_user(
        msg.from_user.id, # type: ignore
        msg.from_user.username, # type: ignore
        msg.from_user.full_name # type: ignore
    )

    await msg.answer(START_TEXT)


EMOJIS = ["❤️‍🔥", "🕊"]

@router_channel.channel_post()
async def react_only_saved_channels(message):
    async with aiosqlite.connect(DB) as db:
        cursor = await db.execute(
            "SELECT 1 FROM channels WHERE channel_id = ?",
            (message.chat.id,)
        )
        channel = await cursor.fetchone()

    if not channel:
        return

    await message.bot.set_message_reaction(
        chat_id=message.chat.id,
        message_id=message.message_id,
        reaction=[ReactionTypeEmoji(emoji=random.choice(EMOJIS))]
    )