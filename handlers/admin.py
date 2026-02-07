import aiosqlite
from aiogram.types import Message
from aiogram.filters import CommandStart
#
from loader import router_admin
from database.db_users import DB
from keyboards.main import admin_keyboard
from middlewares.admin_filter import AdminFilter


@router_admin.message(CommandStart(), AdminFilter())
async def admin_start(message: Message):
    await message.answer(
        "👑 <b>Admin panel</b>\n\n"
        "Quyidagi menyudan foydalaning:",
        reply_markup=admin_keyboard
    )

@router_admin.message(AdminFilter(), lambda m: m.text == "📊 Statistika")
async def show_statistics(message: Message):
    async with aiosqlite.connect(DB) as db:
        users_count = await (await db.execute(
            "SELECT COUNT(*) FROM users"
        )).fetchone()

        channels_count = await (await db.execute(
            "SELECT COUNT(*) FROM channels"
        )).fetchone()

    await message.answer(
        "📊 <b>Bot statistikasi</b>\n\n"
        f"👤 Foydalanuvchilar: <b>{users_count[0]}</b>\n" # type: ignore
        f"📢 Kanallar: <b>{channels_count[0]}</b>" # type: ignore
    )
