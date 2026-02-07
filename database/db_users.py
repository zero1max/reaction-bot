import aiosqlite
from datetime import datetime

DB = "users.db"

async def setup_users():
    async with aiosqlite.connect(DB) as db:
        await db.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER UNIQUE,
                username TEXT,
                full_name TEXT,
                joined_at TEXT
            )
        """)
        await db.commit()
        
        

async def add_user(user_id: int, username: str, full_name: str):
    async with aiosqlite.connect(DB) as db:
        await db.execute("""
            INSERT OR IGNORE INTO users (user_id, username, full_name, joined_at)
            VALUES (?, ?, ?, ?)
        """, (
            user_id,
            username,
            full_name,
            datetime.now().isoformat()
        ))
        await db.commit()