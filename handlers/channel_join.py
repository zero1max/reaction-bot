import aiosqlite
from datetime import datetime
from aiogram.types import ChatMemberUpdated
#
from loader import router_channel, ADMIN_IDS
from database.db_users import DB


@router_channel.my_chat_member()
async def bot_added_to_channel(event: ChatMemberUpdated):
    if event.chat.type != "channel":
        return

    if event.new_chat_member.status in ("administrator", "creator"):
        async with aiosqlite.connect(DB) as db:

            # USER
            if event.from_user and event.from_user.id not in ADMIN_IDS:
                await db.execute("""
                    INSERT OR IGNORE INTO users
                    (user_id, username, full_name, joined_at)
                    VALUES (?, ?, ?, ?)
                """, (
                    event.from_user.id,
                    event.from_user.username,
                    event.from_user.full_name,
                    datetime.now().isoformat()
                ))

            # CHANNEL
            await db.execute("""
                INSERT OR IGNORE INTO channels
                (channel_id, channel_title, channel_username, owner_id, added_at)
                VALUES (?, ?, ?, ?, ?)
            """, (
                event.chat.id,
                event.chat.title,
                event.chat.username,
                event.from_user.id if event.from_user else None,
                datetime.now().isoformat()
            ))

            await db.commit()
