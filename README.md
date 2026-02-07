# reaction-bot 🤖🔥

A Telegram bot built with **aiogram** that automatically adds emoji reactions to new posts in channels it is added to.

---

## ✨ Features

- 🤖 Automatically reacts to **new channel posts**
- 📢 Supports **multiple users and channels**
- 🔐 Bot works only after being added as **channel admin**
- 📊 **Admin panel** with statistics
- 🗄️ SQLite database (`users` & `channels`)
- ⚡ Fast and lightweight (aiogram 3.x)

---

## 🚀 How It Works

1. A user starts the bot with `/start`
2. The user adds the bot to their **Telegram channel**
3. The bot is granted **admin permissions**
4. From that moment on:
   - Every new post in the channel gets an **automatic emoji reaction**

> ⚠️ Due to Telegram API limitations, the bot reacts **only to new posts**, not old ones.

---

## 🛠️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/reaction-bot.git
cd reaction-bot

### 2. Create virtual environment (optional)

```bash
python -m venv venv
source venv/bin/activate  # Linux / Mac
venv\Scripts\activate     # Windows

### 3. Install dependencies

```bash
pip install -r requirements.txt

## ⚙️ Configuration

Create a .env file in the project root:

```bash
BOT_TOKEN=your_telegram_bot_token

Edit loader.py and set your Telegram ID as admin:

```bash
ADMIN_IDS = [123456789]

## ▶️ Run the Bot

```bash
python main.py


## 📜 License

MIT License — free to use, modify, and distribute.